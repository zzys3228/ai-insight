"""
Task queue for concurrent fetching with rate limiting
"""

import time
import asyncio
from typing import Callable, List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
from .config import MAX_CONCURRENT, REQUEST_DELAY


@dataclass
class TaskResult:
    """Result of a task execution"""
    url: str
    success: bool
    result: Any = None
    error: str = ""
    elapsed: float = 0.0


class TaskQueue:
    """Async task queue with concurrency control and rate limiting"""

    def __init__(
        self,
        max_concurrent: int = MAX_CONCURRENT,
        delay: float = REQUEST_DELAY,
        max_retries: int = 3
    ):
        self.max_concurrent = max_concurrent
        self.delay = delay
        self.max_retries = max_retries

        self.queue: List[tuple] = []
        self.running = 0
        self.results: List[TaskResult] = []
        self.failed: List[TaskResult] = []

        self.last_request_time = 0.0

    def add(self, url: str, fetcher_func: Callable, *args, **kwargs):
        """
        Add a task to the queue.

        Args:
            url: URL being fetched (for logging)
            fetcher_func: Async function to call
            *args, **kwargs: Arguments to pass to fetcher_func
        """
        self.queue.append((url, fetcher_func, args, kwargs))

    async def execute(self) -> List[TaskResult]:
        """
        Execute all tasks in the queue.

        Returns:
            List of TaskResults
        """
        while self.queue or self.running > 0:
            # Add tasks up to max_concurrent
            while self.queue and self.running < self.max_concurrent:
                url, fetcher_func, args, kwargs = self.queue.pop(0)
                asyncio.create_task(self._execute(url, fetcher_func, *args, **kwargs))
                self.running += 1

            # Rate limiting
            await self._rate_limit()

            # Small delay to prevent tight loop
            await asyncio.sleep(0.1)

        return self.results

    async def _execute(
        self,
        url: str,
        fetcher_func: Callable,
        *args,
        **kwargs
    ) -> TaskResult:
        """
        Execute a single task with retry logic.

        Args:
            url: URL being fetched
            fetcher_func: Async function to call
            *args, **kwargs: Arguments to pass

        Returns:
            TaskResult
        """
        start_time = time.time()
        last_error = ""

        for attempt in range(self.max_retries):
            try:
                if asyncio.iscoroutinefunction(fetcher_func):
                    result = await fetcher_func(*args, **kwargs)
                else:
                    result = fetcher_func(*args, **kwargs)

                elapsed = time.time() - start_time
                task_result = TaskResult(
                    url=url,
                    success=True,
                    result=result,
                    elapsed=elapsed
                )
                self.results.append(task_result)
                self.running -= 1
                return task_result

            except Exception as e:
                last_error = str(e)
                if attempt < self.max_retries - 1:
                    wait_time = self.delay * (attempt + 1)
                    print(f"Retry {attempt + 1}/{self.max_retries} for {url} after {wait_time}s: {e}")
                    await asyncio.sleep(wait_time)

        # All retries failed
        elapsed = time.time() - start_time
        task_result = TaskResult(
            url=url,
            success=False,
            error=last_error,
            elapsed=elapsed
        )
        self.results.append(task_result)
        self.failed.append(task_result)
        self.running -= 1
        return task_result

    async def _rate_limit(self):
        """Apply rate limiting between requests"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            await asyncio.sleep(self.delay - elapsed)
        self.last_request_time = time.time()

    def get_stats(self) -> Dict[str, Any]:
        """
        Get queue statistics.

        Returns:
            Dictionary with stats
        """
        return {
            "total": len(self.results),
            "success": len([r for r in self.results if r.success]),
            "failed": len(self.failed),
            "pending": len(self.queue),
            "running": self.running,
            "success_rate": len([r for r in self.results if r.success]) / max(len(self.results), 1)
        }


class SyncTaskQueue:
    """Synchronous task queue for simpler use cases"""

    def __init__(
        self,
        delay: float = REQUEST_DELAY,
        max_retries: int = 3
    ):
        self.delay = delay
        self.max_retries = max_retries
        self.results: List[TaskResult] = []
        self.failed: List[TaskResult] = []

    def add(self, url: str, func: Callable, *args, **kwargs):
        """Add a task to execute"""
        self.results.append((url, func, args, kwargs))

    def execute(self) -> List[TaskResult]:
        """Execute all tasks"""
        task_results = []

        for url, func, args, kwargs in self.results:
            start_time = time.time()
            last_error = ""

            for attempt in range(self.max_retries):
                try:
                    result = func(*args, **kwargs)
                    elapsed = time.time() - start_time
                    task_result = TaskResult(
                        url=url,
                        success=True,
                        result=result,
                        elapsed=elapsed
                    )
                    task_results.append(task_result)

                    if self.delay > 0 and attempt == 0:
                        time.sleep(self.delay)

                    break

                except Exception as e:
                    last_error = str(e)
                    if attempt < self.max_retries - 1:
                        wait_time = self.delay * (attempt + 1)
                        print(f"Retry {attempt + 1}/{self.max_retries} for {url}: {e}")
                        time.sleep(wait_time)
            else:
                elapsed = time.time() - start_time
                task_result = TaskResult(
                    url=url,
                    success=False,
                    error=last_error,
                    elapsed=elapsed
                )
                task_results.append(task_result)

        return task_results
