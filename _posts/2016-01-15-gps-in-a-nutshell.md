---
title: 'GPS In A Nutshell'
layout: default
---

# What Is GPS?

This is a summary of a Lunchtime Learning talk given at Cogo Labs on the basics of GPS, full of beautiful graphics and compelling PowerPoint art.
The talk gave an overview of the GPS system, described the concepts that make GPS possible, and dove into some of the signal processing under the covers.

### What GPS Is Not

Before saying exactly what GPS is, we can first clarify what it is not. 

- It's not an iPhone app
  - Phones have a full GPS receiver inside (looks like a small chip)
- It's not a service that knows where you are
  - GPS receivers calcualte their own position internally
- It's not a system that is unique to America
  - Russia, China, the EU, and India all currently have or are building systems for themselves


### ...so then what is it?

As described by the gps.gov website:

> The Global Positioning System (GPS) is a U.S.-owned utility that provides users with positioning, navigation, and timing (PNT) services.

In short, GPS is a constellation of satellites orbiting earth that broadcast their position and time to anyone listening.
There are currently 31 in space, all owned by the government.
They use radio waves to send out their information, which is why anyone with a receiver can use them to figure out their position.

GPS is divided into **3 segments**:

- **Space segment**
  - This is the set of satellites in space
- **Control segment**
  - There is a group of control stations around the world that watch over all the satellites, send data to them, and make sure they are working correctly
- **User Segment**
  - This the segment we are most familiar with. Anyone who's used a GPS receiver is part of the user segment

{% include image.html url="/images/segments.png" description="Aim your lasers well." height="280" width="320" %}


## Well how does it actually work?

So you might be asking, "If the satellites don’t know where I am, what do they know?". The answer to that is that they know their own **position in space** and their **time**.

{% include image.html url="/images/receiver.png" height="280" width="320" %}

The next question would be "How does that help me know where I am?". This is where **trilateration** comes in.

### Trilateration

{% include image.html url="/images/trilateration.png" height="280" width="320" %}

The principal of trilateration (in two dimensions) is this: *if you have the distance to three known locations, you know where you are*.

Now before we can directly use that fact, we first have to figure out these distances, as the satellites only know *position* and *time*. 
However, we can combine this with the fact that all radio waves, being just ordinary electromagnetic waves, move at the speed of light.

$$
  c = 3 \times 10\^8 \frac{m}{s}
$$

So if satellites mark what time they sent a message, and you know what time you received the message, you can estiamte the distance using the **time difference**:

$$
  speed\_\{light\} * \( t\_{received} - t\_{sent} \) = distance
$$

We can plug these distances, along with the satellite positions, into the trilateration equations to find our location:

{% include image.html url="/images/trileqs.png" height="300" width="400" %}

{% include image.html url="/images/tril.gif" description="The magic of PowerPoint art." height="450" width="600" %}


#### But in 3D?
Now this is all clearly in two dimensions- what does it look like as we add the 3rd-D?

{% include image.html url="/images/3dtril.png" description="Adding the 3rd D." height="450" width="600" %}

We can see that two spheres intersect at a *plane*. 
Once we have this 2-D plane, we are now back to our former example: the next sphere intersection at two points, and the final one secures our location. 

While we do need 4 spheres to definitively know our location, you might be asking, "Well isn't the Earth a sphere?" 

You'd be right!

{% include image.html url="/images/3dearth.png" description="Really more of an oblate spheroid" height="450" width="600" %}

However, the problem with this comes from the fact that we can't be *absolutely certain* that the ranges we get from our speed of light calculations are correct.
There are some error bounds that end up fattening where our spheres intersect.
The real situation is more like below, where the exact coordinates are a best estimate from the data:

{% include image.html url="/images/pr.png" height="450" width="600" %}

To understand more about where these error bounds come from, we'll have to take a deeper dive into how we actually pick up these signals.

## The GPS Signal Processing

Before I mentioned that the signal is just a radio wave. 
Now this doesn't mean you can just turn your radio to 1575.42 MHz and listen in. 
This would work if the satellites could output a more powerful signal, but they are so far away in space that the GPS signal is actually 
**below the [thermal noise floor](https://en.wikipedia.org/wiki/Noise_floor)** (which is just the total background radio noise from all energy producing signals).

{% include image.html url="/images/noisefloor.png" height="240" width="300" %}

What this means is that by the time the signals reach Earth, they are **too quiet to be picked up without special processing**.

The extra juice for the signal comes from using **[spread spectrum](http://www.eetimes.com/document.asp?doc_id=1271899)** technologies. 

Without getting too far into the signal processing behind this, the basic idea is a follows:

1. Take the data that you need to transmit from the satellite and turn it into a signal. It will just be a series of 1s and 0s, which in signal form, looks like this: 
    {% include image.html url="/images/data-signal.jpg" height="120" width="300" %}

2. Multiply this by a *spreading signal*. GPS uses a **[pseudo rangom noise (PRN)](https://en.wikipedia.org/wiki/Pseudorandom_noise)** code. This is also a series of 1s and 0s that oscillate much faster than the data, and the code is known by all GPS receivers: 
    {% include image.html url="/images/ca-code.gif" height="130" width="300" %}

3. Combining these two signals takes the frequencies of the data signal, which formerly where narrowly concentrated (red), and spreads them over a much wider range (blue):
    {% include image.html url="/images/spread-fig1.jpg" height="240" width="300" %} {% include image.html url="/images/spread-fig2.jpg" height="240" width="300" %}

4. Once a GPS receiver gets this signal, it can take the PRN code, line it up in time with the GPS code, and the magic of spread spectrum occurs:
    {% include image.html url="/images/corrpeak.png" height="240" width="300" %}

This figure is the outcome of **[cross correlating](https://en.wikipedia.org/wiki/Cross-correlation)** the receiver's copy of the code with the GPS signal.
Upon lining up the two signals, there is a huge spike in the detectable power. 
Suddenly the GPS signal is over *100 times* stronger than what it would be normally.
The satellite data goes from being too weak to detect to perfectly readable, and once the receiver gets the signals from 4 satellites, it can figure out it's position.

However, because it can be difficult to perfectly line up the PRN codes, the *exact* time match is hard to know.
Since the signals move so fast, a small offset in time means a much bigger unknown in the distance. 
This leads to those fat sphere errors we described above.


### Closing comments
Some of my favorite facts about GPS are:

- Until 1995, the government purposely added enough noise to the civilian GPS signal to make it difficult to know your position better than **50 meters** (so much for driving apps). This was called [selective availability](http://www.gps.gov/systems/gps/modernization/sa/)
- In 2013 a Texas professor and his team [pirated a yacht ship](http://www.insidegnss.com/node/3659) by sending out fake GPS signals while on board, fooling the ship's navigation sysem.

To close, I leave you with some GIFs of the Fourier transform. Enjoy.

{% include image.html url="/images/fourier1.gif" height="240" width="300" %}
{% include image.html url="/images/fourier2.gif" height="240" width="500" %}
{% include image.html url="/images/fourierlong.gif" height="240" width="400" %}


