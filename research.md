---
---

My research uses satellite radar interferometry [(InSAR)](https://www.usgs.gov/centers/ca-water-ls/science/interferometric-synthetic-aperture-radar-insar?qt-science_center_objects=0#qt-science_center_objects) to measure millimeter-level changes to Earth's surface over time.
InSAR has a huge variety of [geophysical applications](https://en.wikipedia.org/wiki/Interferometric_synthetic-aperture_radar#Applications), like mapping ground deformation due to the 2018 eruption of Kilauea:

{% include image.html url="/images/insar/kilauea_google_earth.jpg" height=500 %}

At NASA’s Jet Propulsion Laboratory, I led the algorithm development team for the [OPERA Sentinel-1 Surface Displacement product](https://www.jpl.nasa.gov/go/opera/products/), the first continental-scale InSAR ground motion product over North America.

During my Ph.D., I used InSAR to monitor surface changes over the Permian Basin in West Texas, the largest oil-producing region in the United States. To help mitigate the rising number of induced earthquakes, I worked with geologists and seismologists to deliver observational datasets and help understand the causes of the earthquakes.

[You can find my full publication list on my Google Scholar profile.](https://scholar.google.com/citations?user=TC7VtDsAAAAJ&hl=en)

## Open Source Software

I am an active contributor to the open source InSAR community. For the OPERA project, I developed the [dolphin](https://github.com/isce-framework/dolphin) library, which is a Python package implementing advanced multi-temporal "PS/DS" (combined Persistent Scatterer/Distributed Scatterer) processing and phase linking algorithms. This library is the core of software used to generate the OPERA North America Surface Displacement product.

I am also a maintainer or contributor to [dozens of other open source packages on GitHub](https://github.com/scottstanie).

## Research talks available online

### EarthScope 2025 ISCE Short Course

I presented two talks at the EarthScope 2025 ISCE Short Course:

- [InSAR Timeseries Analysis: theory and overview](https://youtu.be/3y65GR5msyA?si=XT7WcR8QNTy6E1P8)
- [OPERA North America Surface Displacement Products with MintPy](https://youtu.be/2UaE0hcXJRY?si=l25KlKy93NCTnJDc&t=9220), using [`dolphin`](https://github.com/isce-framework/dolphin) for high resolution PS/DS processing

### 2023 FRINGE (University of Leeds, UK)

[Near-real-time estimation of ground displacement time series with InSAR](https://www.youtube.com/live/MucdZ6auOd8?t=3639s)

<!-- Below is an interactive map to play around with the cumulative vertical deformation between November 2014 and January 2019 from our paper:

>Staniewicz et al., "InSAR reveals complex surface deformation patterns over an 80,000 square kilometer oil-producing region in the Permian Basin", Geophysical Research Letters (2020): 2020GL090151 

The red areas show uplift (up to ~7cm), blue areas show subsidence (down to ~13 cm), and dark red dots are the locations of the [TexNet](https://www.beg.utexas.edu/texnet/catalog) detected earthquakes in 2018.
You can also download all the deformation data products shown in the paper [at the Texas data repository](https://doi.org/10.18738/T8/AVDBOJ)


 -->
<iframe src='/extras/insar-mapbox.html'
        width='100%' height='400px'>
</iframe>
