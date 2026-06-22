# AI Fetch Robot Skill

## Description
Fetch robot company news, product updates, and technical blogs. Covers Tesla Optimus, Figure AI, Boston Dynamics, 1X, Agility, and other robotics companies.

## Usage
```
/ai-fetch-robot              # Fetch all robot news
/ai-fetch-robot --figure   # Fetch Figure AI news
/ai-fetch-robot --bostondynamics # Boston Dynamics
```

## Supported Companies
| Company | URL | Content |
|---------|-----|---------|
| Figure AI | figure.ai/news | News and announcements |
| Boston Dynamics | bostondynamics.com/news | Atlas, Spot news |
| Tesla Optimus | x.com/Tesla | Official updates |
| 1X Technologies | 1x.tech/neo | NEO humanoid |
| Agility Robotics | agilityrobotics.com | Digit |
| Physical Intelligence | pi.website | π0 VLA model |

## Output
Files saved to: `ai-content-fetched/robot/{company}/{news_slug}.md`
- Each news item as separate markdown file
- Full article content
- Translated to Chinese

## Technical
- News page scraping
- Dynamic content with Playwright
- Proxy required for some sites
