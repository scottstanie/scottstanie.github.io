---
layout: default
title: Posts
excerpt: "An archive of articles."
---

<h3>Tutorials, lunchtime learnings, teachings, explorations</h3>
<ul class="post-list">
{% for post in site.categories.articles %} 
    <li>
        <article>
            <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
            <span class="entry-date">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                {{ post.date | date: "%B %d, %Y" }}
                </time>
            </span>
                <!-- {% if post.excerpt %}
                <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>
                {% endif %} -->
        </article>
    </li>
{% endfor %}
</ul>
