---
category: essays
created: 2026-10-22T13:04
description: A small hardware project I expected to take days was one-shotted while
  eating dinner. What counts as an ambitious hardware project now?
tags:
- hardware
- ai
- software
- signal-processing
title: Expanding ambition for hardware projects
---

I recently saw online that a [German group building](https://espargos.net/) low-cost phased arrays from cheap [ESP32 microcontrollers](https://en.wikipedia.org/wiki/ESP32) had found a hidden feature that allows users to [access IQ samples](https://espargos.net/espsdr/) that would normally be processed by the Wi-Fi module. This enables applications in the realm of [software-defined radio (SDR)](https://www.rtl-sdr.com/about-rtl-sdr/), which normally required hardware that was [moderately](https://limemicro.com)-to-[very](https://www.ettus.com/all-products/usrp-x420/) expensive.

Now, this description is already niche enough that even tech people (if they don't have sufficient electrical and signal processing background) will have no idea why this is remotely interesting. The simplest explanation I can give is that some people find it interesting to play with and poke at all the hidden messages floating around us all the time, contained in the radio spectrum.

After seeing the hack they found, since ESP32s are only about ~$5 each, I thought it sounded cool enough to try 1) seeing if it does work to record the data, and 2) test out a real-time display (also called a ["waterfall plot"](https://en.wikipedia.org/wiki/Waterfall_plot)) of the spectrum on an [LCD screen attached to an ESP32](https://www.amazon.com/dp/B0FKG7WRWV).

This is the kind of project that might have taken me a few days or weeks if I have to spread out the small tinkering time to get it working. Embedded software is hard if you don't work with it full time, and can be much more finicky, prone to obscure errors and dead end debugging than high level software. Since this was only one of many projects I had in my head at one time, I wasn't interested in going through the full zero-AI version of figuring this out and making it work. Part of the project idea was "I think this is cool, it would have been kinda hard 3+ years ago, how fast can I make this work now?"

Well I probably shouldn't have been surprised by it, but I described what I wanted with the LCD, plugged in the USB to give access, and walked away for dinner. When I came back, I saw a working waterfall plot on the screen:
{% include image.html url="/images/Expanding ambition for hardware projects-1794412759451.webp" alt="" %}
With one or two more questions (suggesting that it come up with a way to inspect screenshots and close the debugging loop), I had a working version, one that could see the excess pulses of energy near a running microwave:
{% include image.html url="/images/Expanding ambition for hardware projects-1794412821794.webp" alt="" %}

After the surprise of seeing this, my reactions were a mix of 
- Slight disappointment: I spent some time thinking of a project, possibly to learn or tinker. This felt like the equivalent of setting that up, then clicking Buy Now from Amazon on an equivalent product.
- Chagrin, at my own surprise: If I had read online that someone wrote "I plugged in an ESP32, and Opus 5.5 was able to set up the firmware and create a waterfall plot in C", I wouldn't even click on it because I already know it can handle tasks like that. Somehow I still wasn't expecting it to work on a real device in my room, where you can see a change in the world more tangible than the world of pure software.

But the end was feeling some excitement at what this might open up. As I said, this probably would have taken me at least a few days, probably weeks to get something close to the result I did, not having expert C and firmware programming knowledge. It was well scoped to be challenging, for 2022. Now the only way for it to be a challenge is if I were to use zero AI (which would only make sense to specifically practice C coding, or firmware development). Rather than that, I have to ask: what is an appropriately ambitious hardware project now, for a person assisted by AI agents?


