---
category: essays
created: 2026-10-14T10:22
date: 2026-11-23
description: AI makes internalized knowledge more valuable, which makes it worth to
  increase personal deliberate training.
tags:
- learning
- ai
- academia
title: A gym culture for knowledge work
---

Despite the understandable turmoil caused by AI's effects on math, software, and knowledge work, I believe AI will make internalized knowledge more valuable. It’s what lets us guide the tools effectively and assess the resulting work. But knowledge workers who used to rely on keeping their relevant skills sharp from the job itself may need to develop a “mental gym-culture”, where conscious, deliberate training is expected as a portion of the job, similar to athletes and other high-performance physical jobs.

A formative point in my research career was reading Michael Nielsen's [Augmenting Long-Term Memory](https://augmentingcognition.com/ltm.html) essay on Anki and spaced repetition[^1]. The timing was ironic, as I read it only after receiving my Ph.D. (i.e., completing 21 years of school). At that point, I was like many in thinking that flash cards are most useful for language learners or med students cramming for their Step 2. But as I got up to speed at my new job (as an engineer/researcher at JPL), I would regularly have meetings with groups of 5-10 experts in my field, where a "basic" topic would come up that would cause nearly everyone to draw a blank. Clearly everyone knew these things at one point, but similar to how most adults accept that they've forgotten all calculus from high school, many working researchers would accept that they don't remember everything they learned and can look it up. It's fine to not expect 100% recall... but the surprising part to me was that nearly everyone leaves what will stick up to chance.

I actually meant to write up this whole topic years ago, close to the episode at JPL. Since that time, I've [gone](https://scottstaniewicz.com/chatting-with-claude-circa-november-2024-a-smart-colleague-emerges/) [through](https://scottstaniewicz.com/chatting-with-o1-circa-jan-2025-getting-schooled/) [several stages](https://scottstaniewicz.com/learning-new-programming-languages/) of reckoning with AI (really it's still ongoing), but I've come out thinking that these lessons might become more important than ever.

### Why internalize?

In grad school, I would regularly hear some people avoid memorization at all costs, with reasons like  "I don't want to memorize this stuff, I can just re-derive it when I need to". I tried to point out how much easier it was to just make a flash card for content known to be on the test, but some never accepted that deriving a result is easiest when you have already seen and memorized the result. They wanted to "understand" the material behind the problems deeply, but I wanted to [get used to](https://wist.info/von-neumann-john/44309/) solving them.

However, the utility of flash cards goes well beyond studying for exams in grad school. It's commonly said that you don't [truly know a poem until you've memorized it](https://www.newyorker.com/books/page-turner/why-we-should-memorize). When thinking analytically, having a corpus of facts — for example, the correct orders of magnitude about your domain — changes how you reason from the start. If you try to speed up software without internalizing any of the [common computer latency numbers](https://www.norvig.com/21-days.html#answers), you'll just be thrashing around with random guesses. But even outside very technical jobs, any time you have to stop a meeting or brainstorming session to look something up because nobody knows it, you've killed the flow of ideas. 

### Why aren't you (or I) solving Erdős problems? 

The value of internalization is not always obvious when working with AI. I've been in conversations with more experienced colleagues, asking me how hard I think it would be to implement some technical idea of theirs...  and 20 minutes into the discussion, I realize the whole thing could have been ~80% completed by Opus or Astra in the same time that it took to get me on the phone and explain the whole context. Here, the likely difference between us is that I've spent more time with agentic coding tools, and the colleague was a little behind on what is possible today.

That might suggest that "AI fluency" is more important than internalized knowledge, but I think it's the reverse. Consider an extreme example like  [Terence Tao working through the solution to Erdős problem #728](https://chatgpt.com/share/695e7cbd-605c-8010-809b-ccba75560c76) or [the Jacobian conjecture proof](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56). These are the same models I have access to, but I simply could not have had that conversation. Tao's enormous baseline knowledge lets him ask the right questions and recognize the promising directions to follow up on.

Frontier LLMs are extremely good at meeting you at your level: if you ask a novice question, you get a generic answer. If you don't already know what the frontier of knowledge looks like in an area, you have no chance of leading an AI or guiding it to produce new frontier knowledge. So while anyone can pay for a ChatGPT or Claude subscription, there are still very few people who are going to make real progress in any given subject.

So the internalized knowledge helps on the "generation" side of knowledge — guiding the conversation and direction — but it also helps in the ability to evaluate quickly — having a good "sniff test". This can only come from dedicated practice and learning effort, which then makes it unsurprising that some college students [notice little improvement between](https://www.lesswrong.com/posts/ySXuvJcqRindQwAk7/how-my-students-think-about-ai#Perspective__1__There_has_not_been_rapid_AI_progress) 2023 models and 2026 models — they have not had the time to build up their expertise and have that background knowledge (and their tasks were already solvable in 2023-2024!).

### Gym culture for knowledge work

As more people have moved to jobs without any physical labor component, gym culture has become more prominent. This is a phenomenon that really only took off in the past 150 years, since before that time, most people could stay in shape from the physical part of their daily lives. Similarly, most knowledge workers could expect that their day-to-day activities would keep the mental skills that are relevant to their job sharp. But now that AI is allowing people to move faster, [people are noticing that](https://cacm.acm.org/news/the-ai-deskilling-paradox/) the bulk of people's time is spent in fast decision making modes, and less time is spent doing slower tasks that would build and maintain mental muscle.

Suppose that knowledge work used to be like running. The work itself kept you in shape, and it was enjoyable for many people[^2]. Now, it has become Formula 1 racing: the goal is similar in that it's "racing", but it's incomparably faster, and much more mentally and physically draining than just jogging. Plenty of software engineers are now complaining of burnout from agentic coding that did not happen from traditional software roles. Others have noted that [the trairs of quality programmers of the past have some overlap with those succeeding now, but they are a different set of skills](https://x.com/antirez/status/2104130171305680972) and it has very much become a different job.

But the part of this F1 analogy most relevant here: F1 drivers cross train hard outside the track on areas required by the sport — core strength, endurance, cardio — since the driving alone doesn't provide all the strength that the sport demands.

I think that it's time to promote a "mental gym" culture. The two most common reactions I'm seeing to the rise in AI — "we shouldn't use it at all" and "we need our workers to use it way more to go faster" — are taking extreme positions. They treat it as a choice between human skill and work speed, but setting aside time for deliberate training lets you keep the speed offered by AI, while avoiding deskilling yourself.

### Navigation skills and walking skills

Recently I was asked to talk about my satellite remove sensing career path to a class of undergraduate and graduate students. Two other friends were speaking, and right I was supposed to start, the speaker ended with how important software engineering skills are to research and data analysis, and that you should spend a whole lot of time writing and reading code. I then realized I was planning on noting the exact opposite thing, something like "I've barely written any code by hand for 6-9 months, I've mostly been managing parallel tasks and doing lots of QA testing on the outputs." Also, I realized my own description was not going to be useful advice for these 20-24 year olds! My description that "I've basically become an engineering manager" only makes sense if you know what normal engineering is first. I would have totally concurred and reinforced what the still-looks-at-code colleague said, if I had given the talk any time before 2026. But most of my career-path stories about how I found comparative advantages in jobs have become descriptive, not prescriptive.

I found the talk surprisingly hard overall. It feels like when you go talk to students who are 10-15 years younger than you, you should have a few bits of obviously-good advice to give. But it was hard to convey to them just how weird things are right now, where everyone, at all career stages, is struggling with the same question: what do I even work on learning and maintaining?

More and more colleagues are grappling with the fact that AI has reached or exceeded their technical abilities in math or programming. At one work discussion, some colleagues were posing this question of what to focus on and what to automate as "It's getting easier to pass off tasks to AI, but we have to ask ourselves: what do we still want to own?" The part that sounded off to me was "*want to*": In the context of work, it's not exactly relevant what you "want your job to be like", if that thing no longer fits economically. You may "want" to have to sew your own clothes to wear to work and include it as part of your job, but if you tell your employer that you're going to spend 15 out of your 40 hours per week doing this, they will think you've gone insane. The question shouldn't be about what you want to own, but about what pays off to internalize.

In some ways[^3], AI is the latest stage in a long series of automations. Each step replaces some skill humans had developed, but not all are worth holding onto. Cars let us travel places that would have been impossible on foot or horse, and they add so much convenience that we drive regularly. But walking has enough physical benefits that it's a bad idea to drive everywhere all the time. 

On the other hand, the combination of GPS and smartphones means that we don't generally learn the navigation skill that would have been common hundreds of years ago. But I don't find this a sad fact that's worth fighting. Navigating by map and compass seems like a fun challenge (and useful in emergencies), but regularly eschewing GPS adds little value to me.

To translate this into how I've been transforming my own Anki deck:

- My "navigation" skills I'm letting go: All the HTML or JavaScript syntax cards I had created. I had enough rudimentary skills to create my own website, but now even the weakest open-weight models are better than I will be even with months of effort. The marginal payoff from my attempt to internalize web syntax has gone to zero. 
- Walking skills I still practice: Topics that I consider more "fundamental knowledge" (physics, electronics, certain math topics). These are subjects that shape my thinking and frame my understanding of the world.
- Undecided/still evolving: I've been on the fence about other programming or computer science questions that come up. It's another area where my relative advantage is quite low, but they are clearly more interesting as a subject than HTML syntax.

I don't think there's a universal answer for what to train, partly because people have different thinking styles and preferences. There have always been Freeman Dyson's [birds and frogs](https://www.ams.org/notices/200902/rtx090200212p.pdf): some people enjoy digging in one direction to learn all details, while others need to bounce around and try to unify many separate fields. Both are still needed! 

On the positive side, it's never been easier to try branching out and learning hard subjects.  I’m sure more and better tools will continue popping up, but software like [LearnHarness](https://learnharness.ai/)  is already incredible compared to what was available 4 years ago, and this came about from one person's effort over a few weeks.
### Understanding can't be mandated

As discouraged as many mathematicians and programmers are, I feel strongly there must still be humans in the loop who understand our systems.

I'm sure that at some point in this essay, I would lose people who are in the camp "No I really don't care if a robot does it. Academia shouldn't be a jobs program for mathematicians". But without some human understanding at some level, we are surely ceding control to AI in a way that is fragile and will lead to disasters.

Regulating this is certainly a challenge, since it comes down to individuals' awareness of how much they know or don't know. That is, any attempt to enforce human oversight at the level of "a human must understand and be in control of X" seems doomed. For example, a company may think they're in control, because a VP says their team knows, because managers say their team knows, because the critical person says he knows... but really at the bottom, he's been claude-ing and not caring for months.  Nobody can mandate understanding in a top-down way, since the "yes we understand"s only get tested once something has broken. It surprised me at JPL that researchers would leave their own understanding up to chance, but now there's a broader risk that organizations may leave understanding up to chance. That understanding can only exist if individuals decide to keep training.

-----

[^1]: There is plenty more in the Nielsen essay on the benefits of long term memory, and I'd encourage reading the essay in full if you're interested, but the most transformative ideas for me were (1) Anki cards as regression tests: A pattern in testing software is that when someone finds a bug, they write up a small test that shows how it's triggered, then fix the software, and verify that the test now passes. Come across a situation where you forgot something you thought you should remember? Make a flash card or 5!  (2) Dispelling the stigma around "rote memorization": Like many STEM-inclined students, one reason I preferred math was that it didn't feel like you needed to memorize a bunch of facts in order to do well. The essay (written by a former quantum physicist) makes a good case for why this is the wrong framing, even for math and physics, and why the sooner you embrace some amount of memory work, the easier your "advanced problem solving" becomes. (3) Using one deck for everything: It turns out that in the real world, useful recall often looks like jumping between completely unrelated topics throughout the day. Thus, jamming everything you wish to remember into one deck ends up being a better strategy for Anki.

[^2]: Or at least that's what my runner friends tell me.

[^3]: Mostly for the sake of this discussion really. I think in most ways, AI is quite different than the other leaps of automation, but [others would disagree with me](https://knightcolumbia.org/research/ai-as-normal-technology).
