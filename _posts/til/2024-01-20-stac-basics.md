---
permalink: /til/stac-basics/
category: til
created: 2024-01-20T22:12
tags:
- geospatial
- web
- data
title: STAC Basics
---

The key parts of a Spatio-Temporal Asset Catalog (STAC) are **Items, Catalogs**, and **Collections**. 

1. **Item**: Usually one image. Has an `href` where you can find this image.

> An [Item](https://github.com/radiantearth/stac-spec/blob/v1.0.0/item-spec/item-spec.md) represents a single [spatiotemporal asset](https://github.com/radiantearth/stac-spec/blob/v1.0.0/overview.md#what-is-a-spatiotemporal-asset) as [GeoJSON](https://geojson.org/) so it can be searched.

Also-

>  An **Item** is a [GeoJSON](http://geojson.org/) [Feature](https://tools.ietf.org/html/rfc7946#section-3.2) augmented with [foreign members](https://tools.ietf.org/html/rfc7946#section-6) relevant to a STAC object.

The item has "**assets**" which are the links to the actual images. The item can have multiple assets (e.g. a full-res image, a thumbnail, and a metadata XML file.)

2. **Catalog**
A group of Items, or other Catalogs. Analogy: a folder on your filesystem.
Can also group together collections (i.e. you can have a Catalog that just points to other Catalogs, or other Collections).

3. **Collection**
Like a Catalog (shares much of the same metadata), but goes further and has things like
- a license
- temporal / spatial extent
- provider
- summaries
- keywords
Each item contained in a collection links to the collection to make it easy to find the relevant metadata.

The Diagram is probably too complex for a starting point, but shows all possible links:
{% include image.html url="/images/STAC Basics-20240120221446633.webp" alt="None" %}

## References
1. https://github.com/radiantearth/stac-spec/blob/v1.0.0/overview.md
2. https://github.com/radiantearth/stac-spec/blob/v1.0.0/item-spec/item-spec.md