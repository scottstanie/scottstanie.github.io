---
category: notes
created: 2025-08-15T09:28
tags:
- ai
title: How do you describe problems that AI is good at?
---

If you ask some people how useful they think AI is, they will say that it's completely useless because you never know when it's hallucinating. "We know that they make things up; how can we ever trust it?"

Besides falling prey to the mental model of "AI is a better search engine" (which it is not), they are missing the problems that are NP.

When I'm thinking about whether a LLM will be a useful tool for some task I have, I keep coming back to the concept of "NP problems" from computer science complexity theory. One of the [biggest open question in computer science theory](https://www.quantamagazine.org/videos/p-vs-np-the-greatest-unsolved-problem-in-computer-science/) is whether "P = NP": Roughly speaking, for a problem that can be solved by a computer, some problems can be solved quickly ("solved in polynomial time"); these are the "easy problems". Other problems are harder, where the best known algorithms involve some type of searching, or guessing among a huge number of possible solutions; but, once a solution is found, it can be verified quickly (again in polynomial runtime). These are the "NP problems". Sudoku is an example: while you are solving, there are heuristics to finding solutions quickly, but the only sure algorithms involve a lot of guess and check. As the size of the problem grows, the runtime for solving a sudoko grows exponentially. However, once you have a solution, you can very quickly check if it's right — just verify that each row, column, and tile has the numbers 1-9.

I like giving AI these types of problems:
- I don't care if it hallucinates a wrong answer. I can quickly verify that it's wrong.
- I *could* do it myself, but the solution finding process may take a me very long time
- Bonus points if the solution finding process is not one that I'm in the mood for, or if it's an inherently boring task.

