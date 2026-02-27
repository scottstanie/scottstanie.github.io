---
category: til
created: 2025-08-13T10:19
tags:
- software
- geospatial
title: Virtual reference file for OPERA Displacement
---


I got a working example (with the [very large VirtualiZarr update](https://github.com/zarr-developers/VirtualiZarr/compare/v1.3.2...v2.0.0) for version 2.0 three weeks ago) for creating a Kerchunk-style stack of the full OPERA DISP-S1 displacement time series per frame:  
[https://gist.github.com/scottstanie/c5a7ade5ef2083716d91a90231d6dfbc](https://gist.github.com/scottstanie/c5a7ade5ef2083716d91a90231d6dfbc)

```python
In [1]: import xarray as xr
In [2]: %time ds = xr.open_dataset('disp_s1_reference_44055.parq', engine='kerchunk')
CPU times: user 1.11 s, sys: 112 ms, total: 1.23 s
Wall time: 695 ms

In [6]: ds
Out[6]:
<xarray.Dataset> Size: 672GB
Dimensions:                         (time: 209, y: 7721, x: 9462)
Coordinates:
  * time                            (time) datetime64[ns] 2kB 2016-07-26T00:0...
  * x                               (x) float64 76kB 7.268e+04 ... 3.565e+05
  * y                               (y) float64 62kB 3.487e+06 ... 3.256e+06
Data variables: (12/13)
    connected_component_labels      (time, y, x) float32 61GB ...
    displacement                    (time, y, x) float32 61GB ...
    estimated_phase_quality         (time, y, x) float32 61GB ...
    persistent_scatterer_mask       (time, y, x) float32 61GB ...
    phase_similarity                (time, y, x) float32 61GB ...
    recommended_mask                (time, y, x) float32 61GB ...
    ...                              ...
    short_wavelength_displacement   (time, y, x) float32 61GB ...
    shp_counts                      (time, y, x) float32 61GB ...
    spatial_ref                     (time) float64 2kB ...
    temporal_coherence              (time, y, x) float32 61GB ...
    timeseries_inversion_residuals  (time, y, x) float32 61GB ...
    water_mask                      (time, y, x) float32 61GB ...
Attributes:
    Conventions:         CF-1.8
    contact:             opera-sds-ops@jpl.nasa.gov
    institution:         NASA JPL
    mission_name:        OPERA
    reference_document:  JPL D-108765
    title:               OPERA_L3_DISP-S1 Product
```

The first access is moderately fast, and subsequent accesses depth-wise accesses are faster:
```python
In [7]: %time np.asarray(ds.displacement[:, 4000, 4000])
CPU times: user 1.7 s, sys: 190 ms, total: 1.89 s
Wall time: 5.42 s
Out[7]: (209,)

In [8]: %time np.asarray(ds.displacement[:, 4000, 5003]).shape
CPU times: user 1.35 s, sys: 139 ms, total: 1.48 s
Wall time: 1.45 s
Out[8]: (209,)
```

Since I made the output using parquet instead of JSON, and it looks like each directory-thing they produce is 6-12 MB for all the dates:  

```
$ du -h -d1
8.9M    ./disp_s1_reference_44055.parq
11M     ./disp_s1_reference_12640.parq
9.7M    ./disp_s1_reference_08882.parq
11M     ./disp_s1_reference_08622.parq
7.1M    ./disp_s1_reference_44043.parq
6.9M    ./disp_s1_reference_44042.parq
8.3M    ./disp_s1_reference_36259.parq
9.9M    ./disp_s1_reference_28486.parq
6.2M    ./disp_s1_reference_44041.parq
```

This seems promising, but I stumbled on multiple sharp edges which may be wondering if it's worth near-term effort:
- The reference files point to S3 buckets, which are behind a NASA login wall, but if I store these in a private bucket, the libraries seem unable to handle the two seets of credentials (one for the bucket, one for the AWS account)
- There were several "all 0" errors during a big run. This is the kind of error I could post, but they would have nothing to work with, and trying to replicate it on a smaller subset would be as much effort as becoming a full maintainer of the library.

I'm hoping as use grows, things will smooth out, since this would be quite an easy access point to the OPERA data.
