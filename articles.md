---
---

<p class="post-sections">
  <a href="#essays">Essays</a> · <a href="#technical">Technical</a> · <a href="#notes">Notes &amp; TIL</a> · <a href="#reading">Reading</a>
</p>

<h2 id="essays">Essays</h2>
<ul class="post-list essay-list">
{% assign essays = site.posts | where: "category", "essays" %}
{% for post in essays %}
  {% assign minutes = post.content | strip_html | number_of_words | divided_by: 230 | at_least: 1 %}
  <li>
    <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.description %}<p class="post-desc">{{ post.description }}</p>{% endif %}
    <span class="post-meta"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %Y" }}</time> · {{ minutes }} min read</span>
  </li>
{% endfor %}
</ul>

<h2 id="technical">Technical</h2>
<ul class="post-list compact-list">
{% assign technical = site.posts | where: "category", "technical" %}
{% for post in technical %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y" }}</time>
  </li>
{% endfor %}
</ul>

<h2 id="notes">Notes &amp; TIL</h2>
<ul class="post-list compact-list">
{% assign notes_posts = site.posts | where: "category", "notes" %}
{% assign til_posts = site.posts | where: "category", "til" %}
{% assign short_posts = notes_posts | concat: til_posts | sort: "date" | reverse %}
{% for post in short_posts %}
  <li>
    <span class="post-kind">{% if post.category == "til" %}TIL{% else %}note{% endif %}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
  </li>
{% endfor %}
</ul>

<h2 id="reading">Reading</h2>
<p class="section-note">Monthly roundups of what I've been reading.</p>
{% assign reading = site.posts | where: "category", "reading" | sort: "title" %}
{% assign reading_years = reading | group_by_exp: "p", "p.title | slice: 0, 4" | reverse %}
<ul class="post-list reading-years">
{% for year in reading_years %}
  <li>
    <span class="reading-year">{{ year.name }}</span>
    {% for p in year.items %}<a href="{{ p.url | relative_url }}">{{ p.title | split: " " | last | slice: 0, 3 }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}
  </li>
{% endfor %}
</ul>
