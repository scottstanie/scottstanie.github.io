---
---

<h3>Tutorials, lunchtime learnings, teachings, explorations</h3>
<ul class="post-list">
{% for post in site.posts %} 
    {% if post.path contains '/articles/' %} 
    <li>
        <article>
            <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
            <span class="entry-date">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                {{ post.date | date: "%B %d, %Y" }}
                </time>
            </span>
        </article>
    </li>
    {% endif %} 
{% endfor %}
</ul>

<h3>TILs</h3>
<ul class="post-list">
{% for post in site.posts %} 
    {% if post.path contains '/til/' %} 
    <li>
        <article>
            <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
            <span class="entry-date">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                {{ post.date | date: "%B %d, %Y" }}
                </time>
            </span>
        </article>
    </li>
    {% endif %} 
{% endfor %}
</ul>

