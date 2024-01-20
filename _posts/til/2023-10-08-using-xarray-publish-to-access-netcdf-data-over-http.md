---
created: 2023-10-08 16:40:00
tags:
- software
- web
- geospatial
title: Using `xarray-publish` to access NetCDF data over HTTP
---

**Context**: I've been starting to think of how to visualize/explore/debug the results of large geospatial workflows. The output format is going to be a set of geospatial rasters, one per date. We may have a few hundred separate files, each around 5000 x 5000 pixels each, which is `300 * 5000 * 5000 * 4 / 1e9 = 30` GB of data. 
- We can't have everyone download all the files each time they want to plot it themselves (and can't use `matplotlib` and load it all anyway)
- We would like to have a way to have multiple people plot/explore the data remotely

This is a problem many people are thinking about and building for in the geospatial community. Within the climate community, `zarr` is a format that's getting a big push, and `xarray` is the tool many people are recommending to interact with this.

While I have some reservations (mostly performance related) about doing everything with `xarray` and letting `dask` handle all the parallelism, I'm interested in some of the auxiliary tools that are popping up around these library. One which seemed like it could be great for our purposes was [`xarray-publish`](https://github.com/xpublish-community/xpublish). They want to make it as easy to distribute your data via a web API as writing.
```python
ds.rest.serve()
```

### Using it with non-Zarr data

Since my data is going to be separate files, if I want to avoid copying all of it into a single zarr file (which I do), I can try to work around that to still get it into `xarray` using `open_mfdataset`.

(The pre-processing step is to extract the `time` dimension. If the format changes to become `(1, rows, cols)` with dimensions `(time, y, x)`, I can skip this step):
```python
from pathlib import Path
import xarray as xr
import pandas as pd

def prep(ds):
    from dolphin.utils import get_dates  # Parse all dates from filenames
    date = get_dates(ds.encoding["source"])[-1]
    if len(ds.band) == 1:
        ds = ds.sel(band=ds.band[0])

    return ds.expand_dims(time=[pd.to_datetime(date)])

ds = xr.open_mfdataset( Path(".").glob("*.nc"), preprocess=prep, engine="rasterio")

```
This gives me a nice `xarray` Dataset with all of my layers through the 20 time steps:
```
In [47]: ds
Out[47]:
<xarray.Dataset>
Dimensions:                     (time: 20, x: 3389, y: 2225)
Coordinates:
  * time                        (time) datetime64[ns] 2022-11-19 ... 2023-07-29
    band                        int64 1
  * x                           (x) float64 2.152e+05 2.152e+05 ... 3.168e+05
  * y                           (y) float64 4.398e+06 4.397e+06 ... 4.331e+06
    spatial_ref                 int64 0
Data variables:
    unwrapped_phase             (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    connected_component_labels  (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    temporal_correlation        (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    spatial_correlation         (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    tropospheric_delay          (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    ionospheric_delay           (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    solid_earth_tide            (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
    plate_motion                (time, y, x) float32 dask.array<chunksize=(1, 2225, 3389), meta=np.ndarray>
Attributes:
    description:         Phase corrections applied to the unwrapped_phase
    contact:             operaops@jpl.nasa.gov
    Conventions:         CF-1.8
    institution:         NASA JPL
    mission_name:        OPERA
    reference_document:  TBD
    title:               OPERA L3_DISP-S1 Product
```

Running `ds.rest.serve(host="localhost")` starts up a [FastAPI](https://fastapi.tiangolo.com/) server, which allows me to go to `localhost:9000/docs` to explore the API
```
In [48]: ds.rest.serve()
INFO:     Started server process [71510]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit)
```
{% include image.html url="/images/2023-10-07-1696708121479.jpeg" alt="None" %}

This is pretty cool. Now to access it from elsewhere, even though I didn't have `zarr` data to being with, I can open it as though it's now a `zarr` file in another terminal:
```python
from fsspec.implementations.http import HTTPFileSystem

fs = HTTPFileSystem()

# The URL 'http://0.0.0.0:9000/zarr/' here is serving my dataset, running in another window
http_map = fs.get_mapper("http://0.0.0.0:9000/zarr/")

# open as another Xarray Dataset
ds_new = xr.open_zarr(http_map, consolidated=True)
```

I can access it with normal `xarray` syntax (where I have to add `.compute()` if I want the actual number, because `dask` is making it lazy)
```python
In [37]: %time ds_new.unwrapped_phase[:, 1256:1258, 1256:1258].mean().compute()
CPU times: user 141 ms, sys: 109 ms, total: 250 ms
Wall time: 817 ms
Out[37]:
<xarray.DataArray 'unwrapped_phase' ()>
array(18.994, dtype=float32)
```

If I look at the window running the server, I see a bunch of HTTP requests coming in:
```bash
INFO:     127.0.0.1:60030 - "GET /zarr/unwrapped_phase/0.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60031 - "GET /zarr/unwrapped_phase/1.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60035 - "GET /zarr/unwrapped_phase/5.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60034 - "GET /zarr/unwrapped_phase/4.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60032 - "GET /zarr/unwrapped_phase/2.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60038 - "GET /zarr/unwrapped_phase/8.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60033 - "GET /zarr/unwrapped_phase/3.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60039 - "GET /zarr/unwrapped_phase/9.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60036 - "GET /zarr/unwrapped_phase/6.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60037 - "GET /zarr/unwrapped_phase/7.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60030 - "GET /zarr/unwrapped_phase/10.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60031 - "GET /zarr/unwrapped_phase/11.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60035 - "GET /zarr/unwrapped_phase/12.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60034 - "GET /zarr/unwrapped_phase/13.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60032 - "GET /zarr/unwrapped_phase/14.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60038 - "GET /zarr/unwrapped_phase/15.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60033 - "GET /zarr/unwrapped_phase/16.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60039 - "GET /zarr/unwrapped_phase/17.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60036 - "GET /zarr/unwrapped_phase/18.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60037 - "GET /zarr/unwrapped_phase/19.0.0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60037 - "GET /zarr/band/0 HTTP/1.1" 200 OK
INFO:     127.0.0.1:60037 - "GET /zarr/spatial_ref/0 HTTP/1.1" 200 OK
```
### Chunking problems

Now if I know that I'm going to access all points in time as my default access mode, I probably don't want the chunks to be like this:
```python
print(ds_new.chunks)
Frozen({'time': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'y': (2225,), 'x': (3389,)})
```
The accessor seems to make one HTTP call per chunks... so when `open_mfdataset` chunks the dataset as 1-per-file, this will be quite inefficient to get data over the network.

But luckily, rechunking the data seems to work even with the multi-file dataset. On the server side, running
```python
ds_rechunked = ds.chunk({"time": 20, "x": 128, "y": 128})
```
means that now when I access one slice for all time steps, I get one HTTP call:

```bash
INFO:     127.0.0.1:57058 - "GET /zarr/unwrapped_phase/0.9.9 HTTP/1.1" 200 OK
```

I still can't tell if this will be the most direct way to solve our immediate visualization problem, as it could require some more networking setup with AWS. Also, it doesn't solve the problem of getting overviews fast for NetCDF data. But it has a lot of promise for easy sharing and demonstration of large datasets that are stored remotely.