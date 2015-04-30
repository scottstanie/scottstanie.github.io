# How does GPS work?

This is a summary of the ideas behind GPS, and how various parts are implemented. 

First, what exactly is the Global Positioning System, besides something that tells you where you are on your phone? GPS started as a military project by the Department of Defense in the 80s. It is a system of satellies owned by the government that circles the globe and emits a signal. This signal contains both the times on the satellite clock and position of the satellite. 

How does this lead to you being able to figure out where you are? There are two key points about those pieces of information:
1. If you know the time a signal was sent out, and you are keeping track of time yourself, you can convert this *time difference* to a *distance*.
  - This is because all electromagnetic wave signal travel at the same speed, \\(3 \time 10^8 \frac{m}{s}\\)
2. If you know the distances to 3 points in space and their locations, you can figure out your own position.
This second point comes the idea of ***triangulation***.  Looking in two dimension says that if you know the location of two points and how far they are from you, then you can figure out your own position. The formula used for this is 

