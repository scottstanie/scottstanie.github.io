---
---

<h3>Tutorials, lunchtime learnings, teachings, explorations</h3>
<ul class="post-list">
{% for post in site.posts %} 
    {% if post.path contains '/articles/' %} 
    {% include post-entry.html %}
    {% endif %} 
{% endfor %}
</ul>

<h3>TILs</h3>
<ul class="post-list">
{% for post in site.posts %} 
    {% if post.path contains '/til/' %} 
    {% include post-entry.html %}
    {% endif %} 
{% endfor %}
</ul>

<h3>Consumed - shorter notes on articles, videos, etc.</h3>
<ul class="post-list">
{% for post in site.posts %} 
    {% if post.path contains '/consumed/' %} 
    {% include post-entry.html %}
    {% endif %} 
{% endfor %}
</ul>
