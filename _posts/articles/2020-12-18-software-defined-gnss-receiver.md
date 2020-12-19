---
title: 'Making a software defined GPS receiver'
layout: post
categories: articles
---

I recently finished the UT aerospace course "GNSS Signal Processing", where the goal is to create the full signal processing chain inside a GPS receiver. 
This means you can simulate a receiver on your compute that's able to process the raw samples from a RF front end and create the pseudorange and carrier phase measurements (which is 1 step away from finding your position). 
The idea of being able to plug in an antenna to my computer and pop out my position seemed incredibly cool to me. 
I started looking into what software defined radio was, and I found out it had become super cheap/easy to get started with SDR hardware.
To make a challenge for myself, I wanted to not only produce the receiver measurements, but calculate my position using a real antenna from my computer at the end of the semester.

I found a [$10 GPS patch antenna](https://www.amazon.com/gp/product/B07WFHNG73/) and the [$25 RTL-SDR](https://www.amazon.com/RTL-SDR-Blog-RTL2832U-Software-Defined/dp/B0129EBDS2/) USB dongle to create the IQ samples, which seemed like the cheapest viable option (although some people warned me these might be too cheap to work for GPS).

{% include image.html url="/images/rtlsdr_gps_antenna.png" description="Antenna and RTL-SDR dongle" height="420" width="600" %}

After finishing the final exam (where we were given data to acquire and track satellites from a mystery dataset), I started searching for what changes would be needed to work with the RTL-SDR.
It only took some minor struggling to figure out what type of data the <code>rtl_sdr</code> command outputs ([for the curious, it's ibyte data](https://gnss-sdr.org/docs/tutorials/understanding-data-types/)).

{% include image.html url="/images/rtlsdr_data_outside2.png" description="Avoiding the stares of neighbors collecting data" height="420" width="600" %}

I went outside to collect a minute of data, then held my breath as my acquistion code ran and tried to pick out any satellites in the sky.

{% include image.html url="/images/acq_results.png" description="PRN = satellite ID" height="420" width="600" %}

To my surprise, on the first (correctly formatted) run of the code, it picked out 8 satellites.
It seemed like it was too many to be a fluke, but I had to check what was really there:

{% include image.html url="/images/trimble_skyview.png" description="GPS satellites overhead (http://www.gnssplanning.com/#/skyplot)" height="420" width="600" %}

I had picked out 8 of the 10 satellites sitting over Austin at the time, and the two low-elevation misses were probably due to my bad data-collection spot near a building.

Once I had written the final (tedious) part to decode the navigation bits and get the satellite times (skipping a bit of the orbital calculations from some internet help), my final position was not so bad for the hacky code that produced it: 

{% include image.html url="/images/rtlsdr_nav_solution2.png" description="A near hit: ~3-4 meters away from my gray squat spot" height="400" width="550" %}
