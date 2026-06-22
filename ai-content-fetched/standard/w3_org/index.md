---
title: Decentralized Identifiers (DIDs) v1.0
source: www.w3.org
url: https://www.w3.org/TR/did-core
category: standard
---
# Decentralized Identifiers (DIDs) v1.0

```html
<a href="https://www.w3.org/"><img src="https://www.w3.org/StyleSheets/TR/2021/logos/W3C" alt="W3C" /></a>

<h1>去中心化标识符（DID）v1.0</h1>

<p>核心架构、数据模型和表示形式</p>

<p><a href="https://www.w3.org/standards/types#REC">W3C 推荐标准</a>，2022 年 7 月 19 日</p>

<p>关于本文档的更多详情</p>

<p><strong>本版本：</strong><br />
<a href="https://www.w3.org/TR/2022/REC-did-core-20220719/">https://www.w3.org/TR/2022/REC-did-core-20220719/</a></p>

<p><strong>最新发布版本：</strong><br />
<a href="https://www.w3.org/TR/did-core/">https://www.w3.org/TR/did-core/</a></p>

<p><strong>最新编辑草案：</strong><br />
<a href="https://w3c.github.io/did-core/">https://w3c.github.io/did-core/</a></p>

<p><strong>历史：</strong><br />
<a href="https://www.w3.org/standards/history/did-core">https://www.w3.org/standards/history/did-core</a><br />
<a href="https://github.com/w3c/did-core/commits/main">提交历史</a></p>

<p><strong>实现报告：</strong><br />
<a href="https://w3c.github.io/did-test-suite/">https://w3c.github.io/did-test-suite/</a></p>

<p><strong>编辑：</strong></p>
<ul>
<li><a href="http://manu.sporny.org/">Manu Sporny</a>（<a href="https://digitalbazaar.com/">Digital Bazaar</a>）</li>
<li><a href="https://rhiaro.co.uk/">Amy Guy</a>（<a href="https://digitalbazaar.com/">Digital Bazaar</a>）</li>
<li><a href="https://www.linkedin.com/in/markus-sabadello-353a0821">Markus Sabadello</a>（<a href="https://danubetech.com/">Danube Tech</a>）</li>
<li><a href="https://www.linkedin.com/in/drummondreed/">Drummond Reed</a>（<a href="https://www.evernym.com/">Evernym/Avast</a>）</li>
</ul>

<p><strong>作者：</strong></p>
<ul>
<li><a href="http://manu.sporny.org/">Manu Sporny</a>（<a href="https://digitalbazaar.com/">Digital Bazaar</a>）</li>
<li><a href="https://github.com/dlongley">Dave Longley</a>（<a href="https://digitalbazaar.com/">Digital Bazaar</a>）</li>
<li><a href="https://www.linkedin.com/in/markus-sabadello-353a0821">Markus Sabadello</a>（<a href="https://danubetech.com/">Danube Tech</a>）</li>
<li><a href="https://www.linkedin.com/in/drummondreed/">Drummond Reed</a>（<a href="https://www.evernym.com/">Evernym/Avast</a>）</li>
<li><a href="https://www.linkedin.com/in/or13b/">Orie Steele</a>（<a href="https://transmute.industries/">Transmute</a>）</li>
<li><a href="https://www.linkedin.com/in/christophera">Christopher Allen</a>（<a href="https://www.BlockchainCommons.com">Blockchain Commons</a>）</li>
</ul>

<p><strong>反馈：</strong></p>
<ul>
<li><a href="https://github.com/w3c/did-core/">GitHub w3c/did-core</a>（<a href="https://github.com/w3c/did-core/pulls/">拉取请求</a>、<a href="https://github.com/w3c/did-core/issues/new/choose">新建 issue</a>、<a href="https://github.com/w3c/did-core/issues/">开放的 issue</a>）</li>
<li><a href="mailto:public-did-wg@w3.org?subject=%5Bdid-core%5D%20YOUR%20TOPIC%20HERE">public-did-wg@w3.org</a>，主题行 “[did-core] … 消息主题 …”（<a href="https://lists.w3.org/Archives/Public/public-did-wg/">存档</a>）</li>
</ul>

<p><strong>勘误表：</strong><br />
<a href="https://w3c.github.io/did-core/errata.html">勘误表已有</a>。</p>

<p><strong>相关文档：</strong></p>
<ul>
<li><a href="https://www.w3.org/TR/did-use-cases/">DID 使用案例与需求</a></li>
<li><a href="https://www.w3.org/TR/did-spec-registries/">DID 规范注册表</a></li>
<li><a href="https://w3c.github.io/did-test-suite/">DID Core 实现报告</a></li>
</ul>

<p><strong>另请参阅：</strong><br />
<a href="https://www.w3.org/Translations/?technology=did-core">翻译</a>。</p>

<p><a href="https://www.w3.org/Consortium/Legal/ipr-notice#Copyright">版权</a> © 2022 <a href="https://www.w3.org/">W3C</a>®（<a href="https://www.csail.mit.edu/">MIT</a>、<a href="https://www.ercim.eu/">ERCIM</a>、<a href="https://www.keio.ac.jp/">Keio</a>、<a href="https://ev.buaa.edu.cn/">Beihang</a>）。W3C <a href="https://www.w3.org/Consortium/Legal/ip">责任</a>。</p>
```

*原文: https://www.w3.org/TR/did-core*