---
category: notes
created: 2026-01-24 11:25:00
tags:
- ai
- software
title: On the end of programming language learning as a skill investment
---

The urge to learn new programming languages is at an all-time low. Volatility is high for what skills will be useful in 2+ years. Three or four years ago, I would have strongly recommended to my non-programming friends who do any data analysis that they should learn enough Python to, e.g., load a CSV file, transform it slightly to clean the data, and plot it or dump to Excel.

Now, unless you find programming inherently interesting, or you plan on continuing to learn and develop, that beginner level of software knowledge isn't more useful than knowing "I can do these things on a computer". You can program at beginner skill level using natural language (English) with today's models, even the crappy open-source models that run on your laptop. The top-tier models have leapfrogged early developer skills by decades, meaning there's some threshold of maybe the top 10 - 20[^1] percent of software-literate people who are still more skilled than Claude/ChatGPT. Everyone else gets better results, for any well-defined task, by asking the robots.

I had started learning Rust about 1 year ago — it appealed to me aesthetically, was heavily hyped as a pleasant, performant language, and I had been growing tired of using Numba for everything. My initial reactions were positive, and, noticing how simple it was for a brand new user to understand the compiler errors, I realized that this would make pair-programming with an LLM especially effective.  The author of "Agentic Coding Recommendations" ([2025 - 03 March](/2025-03-march/)) mentions similar benefits to using Go.
Learning one of these seemed like a forward-looking choice, even in the age of LLMs, even if I never fully caught up to the model's ability to one-shot a Leet-code problem in the language.

But, I started learning this at a time when I was still in the mindset "things in software will look mostly the same for experienced people". I was using LLMs every day, but still in the driver's seat: the models could often solve hard problems, and certainly do it quicker, but they lacked the taste of top programmers, and they clearly failed to produce large, well-designed codebases. Even with those limitations, by mid- to late-2025, the software output quality was better than 50-70% of the JPL colleagues I had (who are all clearly smart and experienced, but, for the most part, seemed to not care specifically about programming style).

Then at the end of the year, Claude Opus 4.5 came out, and Anthropic's fine-tuning around the Claude Code harness was so good that it set people into frenzy. I gave in to the hype, tried out the Max subscription of Claude... and found that the hype was correct. There was a step-change in abilities: Claude could understand 5,000 - 10,000 line codebases easily, make tasteful decisions, pinpoint bugs with even a poorly-contextualized traceback. 

Now I question whether there are benefits to learning more than the basics of a new programming language. Will I ever get good enough to spot-check them? Or is the choice of language for a project more like a high-level managerial decision. "What language would this tool be best in?" is a real question you can ask when starting a project, if you're willing to give up the idea that you'll understand the code.

[^1]: I'm being very generous to human programmers here.
