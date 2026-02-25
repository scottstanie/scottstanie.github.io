---
---

<div class="post-filters">
  <a href="#" class="filter-btn active" data-filter="all">All</a>
  <a href="#" class="filter-btn" data-filter="articles">Articles</a>
  <a href="#" class="filter-btn" data-filter="til">TIL</a>
  <a href="#" class="filter-btn" data-filter="consumed">Consumed</a>
  <a href="#" class="filter-btn" data-filter="notes">Notes</a>
</div>

<ul class="post-list">
{% for post in site.posts %}
  <li data-category="{{ post.category }}">
    <article>
      <a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a>
      <span class="entry-date">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
      </span>
      <span class="entry-category">{{ post.category }}</span>
    </article>
  </li>
{% endfor %}
</ul>

<script>
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', e => {
    e.preventDefault();
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    document.querySelectorAll('.post-list li').forEach(li => {
      li.style.display = (filter === 'all' || li.dataset.category === filter) ? '' : 'none';
    });
  });
});
</script>
