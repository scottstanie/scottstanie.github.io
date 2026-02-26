---
category: notes
created: 2025-08-15T09:28
tags:
- ai
title: How do you describe problems that AI is good at?
---

If you ask some people how useful they think AI is, they will say that it's completely useless because you never know when it's hallucinating. "We know that they make things up; how can we ever trust it?"

When I'm thinking about whether a LLM will be a useful tool for some task I have, I keep coming back to the concept of "[NP problems]((https://www.quantamagazine.org/videos/p-vs-np-the-greatest-unsolved-problem-in-computer-science/)" from computer science. Roughly speaking, some problems are easy, and can be solved quickly by an algorithm (in "polynomial time"). Other problems are exponentially harder as the problem size grows, where the best known algorithms involve some type of searching, or guessing among many combinations; but, once a solution is found, it can be **verified** quickly. These are the "NP problems".

Sudoku is an example: while you are solving, there are heuristics to finding solutions quickly, but the only sure algorithms involve a lot of guess and check. As the size of the problem grows, the runtime for solving a sudoko grows exponentially. However, once you have a solution, you can very quickly check if it's right — just verify that each row, column, and tile has the numbers 1-9.

I like giving AI these types of problems because:
1. I don't care if it hallucinates a wrong answer. I can quickly verify that it's wrong.
2. I *could* do it myself, but the solution finding process may take a me very long time, or is very boring.

Some of this problem framing is not LLM specific, which is why it confused me when I would see smart people echoing the "hallucinations! useless!" talking point. It's not that they don't understand this search/verification distinction for problems, it's that they are still thinking of AI as a tool— something closer to a power drill or a search engine than a junior employee.