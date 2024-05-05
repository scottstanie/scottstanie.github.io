---
category: til
created: 2024-01-21T17:50
tags:
- geospatial
- web
title: Map Tile Jargon
---

WMS? WMTS? XYZ? TMS? These are terms you will find while working with different geospatial mapping libraries.
They all are relating to making web map tiles, but their definitions can be confusing and seemingly overlapping. 
One of the simplest explanations is found on [the leaflet documentation](https://leafletjs.com/examples/wms/wms.html)[^1]. 

Some of my confusion was because these terms are, in fact, mostly doing the same thing[^2]:- Creating small RGB images of your map to be loaded by some viewing software. Ordering from simplest to most complex, we have:

1. **XYZ**,  also called ["Slippy map" format](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) popularized by [Open Street Maps](https://developers.planet.com/docs/planetschool/xyz-tiles-and-slippy-maps/).  A file/URL has an `{z}/{x}/{y}` in the name to represent the current Zoom and X/Y tile location. All images are 256 x 256 pixels. When serving pre-computed tile images, each zoom is a directory.
	- Example: https://tile.openstreetmap.org/2/1/0.png is the tile at zoom level 2, x=1,y=0. 
	- `https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}` is the Google Satellite tile URL. E.g. https://mt1.google.com/vt/lyrs=s&x=2&y=4&z=4
 
2. **Tile Map Service (TMS)**: one specification for making tiled web maps. Uses a URL or URI, generally following a client-server architecture (some client requests tiles, a serve provides them). XYZ maps are an example of this. Because of this structure, it's most Served as the basis for....

3. **Web Map Tile Service** (WMTS): Specification by the Open Geospatial Consortium (OGC) for serving map tiles over the internet.

4. **Web Map Service (WMS)**: a way of publishing maps found in professional GIS software. It is like map tiles, but "more generic and not so well optimized for use in web maps" (so probably the name it's a misnomer?). Usually produced by a map server from a GIS database. It was developed in the 90's for desktop GIS software, and it is definitely complex.

## Extra confusion: there's another "TMS" associated with tiles 

`TileMatrixSet` (TMS) is [standard](https://docs.ogc.org/is/17-083r4/17-083r4.html) for the describing a scheme to divide a 2D planar surface into a regular grid. Not going into the details here except to say that the standard early web maps (like slippy tiles) all use the Web Mercator project, [EPSG:3857](https://epsg.io/3857), so if you want tiles of a web map over Antarctica you need a different TileMatrixSet. The [`morecantile`](https://developmentseed.org/morecantile/) tool was made to work with these TMS's.

{% include image.html url="/images/Map Tile Jargon-20240121202349430.webp" alt="None" %}


[^1]: Fitting, since Leaflet is one of the simplest and easiest to use libraries in the GIS space.
[^2]: Why do we need all these? As much as I don't like linking to XKCD, [it feels like this is another instance of the software standards problem](https://xkcd.com/927/).


