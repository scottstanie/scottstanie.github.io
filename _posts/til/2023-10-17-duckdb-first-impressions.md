---
created: 2023-10-17 16:35:00
tags:
- software
- databases
title: DuckDB first impressions
---

I can't remember what prompted me to look at [DuckDB](https://duckdb.org/). Even though I used to write a lot of SQL, I had never heard of [OLAP](https://www.ibm.com/topics/olap) (still don't really get it), so I couldn't guess what an  "OLAP database management system". But the enticement of [their benchmarks](https://duckdblabs.github.io/db-benchmark/), where somehow they outperform basically any similar library, made me spend some hours trying to get started with it.

My current use case was making a historical database of "burst image" acquisitions for Sentinel-1, [very similar to what Descarte's Labs made](https://blog.descarteslabs.com/sentinel-1-burst-mapping). I couldn't use theirs because 1. it's proprietary, and 2. they've adopted a naming scheme separate from the "official burst ID map" [published by ESA](https://sentinel.esa.int/web/sentinel/-/publication-of-brust-id-maps-for-copernicus-sentinel-1/1.1). After much data munging and API querying, I had a CSV of 53 million rows with columns `(burst ID, sensing time, geometry, granule)`. 53 million wouldn't be too huge to query in some ways, but the `geometry` column was WKT, and by itself took up about 17 GB uncompressed. This meant that while I *could* load it into memory and use (Geo)Pandas, the loading/parsing to `shapely.geometry` took upwards of 5 minutes.

So I started testing DuckDB. They good starting instructions and a very simple install process (downloading one file, like `sqlite`). The question that kept tripping me up was "what is their data format, and how do I get it into that?"
Most of their docs for data formats talk about [importing/exporting from CSV](https://duckdb.org/docs/guides/import/csv_import), or [from parquet](https://duckdb.org/docs/guides/import/parquet_import), or even [from SQLite](https://duckdb.org/docs/guides/import/query_sqlite). But I spent a weirdly long time wondering "ok but just what format does it want the data in so I can query it?"

It turns out that *the data format barely matters* for DuckDB, which is one of it's biggest strengths. DuckDB talks about "[using columnar vectorized query engine](https://duckdb.org/why_duckdb#fast-analytical-queries)", which I thought meant that it needed a columnar data format (e.g. Parquet) to work best (that's not what it means).  While it's true that converting your data to columnar storage with parquet will probably make it run faster and take up less space, the crazy thing was that *DuckDB can run the same SQL query on the CSV files, unconverted*. I would have thought you need to load it into memory somehow, or transform it first (and maybe that's what it does?). But DuckDB could run the same query directly on the CSV file faster than Pandas could do it, *even after Pandas loaded it all into memory*.

Also, not only is it faster than Pandas (apparently most things are, according to the benchmark), but I did a test against SQLite: I converted the data to a SQLite database, created an index on the two columns I was going to do a `SELECT a, max(b) FROM table GROUP BY 1`, then timed how long it would take to run and dump the results to new file. It turns out that DuckDB is still faster *even when I ran DuckDB on the CSV!* That blew my mind, that even SQLite could get it just in the right format and have the right indexes, and still be twice as slow as DuckDB on a suboptimal data format.

Once I saw the results of my SQLite test, I was sold. The initial usage, while confusing because I had such a different mental model going in, was extremely pleasant. It's nice to be able to write SQL, to use it from Python or from the command, and to have a CLI editor that doesn't crap out and become uneditable with any mistake like SQLite's. 