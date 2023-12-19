# aoc23

[advent of code 23](https://adventofcode.com/2023)

Almost all of my solutions were reworked afterwards and commented on.

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 19   00:52:15   3546      0   01:46:01   2163      0
 18   01:54:04   5213      0   01:59:36   2527      0
 17   00:58:49   1471      0   03:33:22   3419      0
 16   00:42:46   2595      0   00:52:41   2434      0
 15   00:06:18   1901      0   00:26:05   1668      0
 14   00:14:18   2099      0   01:45:06   4343      0
 13   00:32:53   2442      0   00:45:00   1890      0
 12   00:51:16   3665      0       >24h  19646      0
 11   00:23:25   2747      0   00:50:36   4371      0
 10   00:33:42   1685      0   01:13:54   1047      0
  9   00:14:11   2365      0   00:31:36   4758      0
  8   00:16:04   4602      0   00:35:56   2308      0
  7   00:51:45   5757      0   01:19:43   5484      0
  6   00:11:37   3462      0   00:15:35   3055      0
  5   00:28:16   2703      0   15:17:52  29752      0
  4   00:10:02   3175      0   00:27:40   3877      0
  3   00:26:14   2490      0   00:38:20   2263      0
  2   00:12:47   2120      0   00:18:10   2323      0
  1   01:03:15  13818      0   01:22:51   8780      0
```

**Day 1 - Trebuchet** Woke up too late. From now on: wake-up at 5:45.

**Days 2 to 4 - Cube Conundrum/Gear Ratios/Scratchcards** I knew I was slow. It's confirmed. These initial results call for modesty. My goal is still to get 50 stars with code I can understand in a year's time. When I trained this summer with the year 2022 challenges, I saw that things were getting tougher around day 15. So far, my `aoc.Input` tool hasn't proved its worth. We'll see.

**Day 5 - If You Give A Seed A Fertilizer** The problems started earlier this year. I had to come back to it at the end of the day to find the 2nd *.

**Day 6 - Wait For It** Elegant mathematical solution for 2nd * found afterwards.

**Day 7 - Camel Cards** Nothing difficult here. Depressing to have spent so much time when comparing hands of the same type was so simplified compared to poker rules. Important rework.

**Day 8 - Haunted Wasteland** The idea of least common multiple for 2nd * came to me instantly. Still 19 minutes to write it down, partly because I did not know the `math.lcm()` function, not even the LCM acronym (it is PPCM in french). Despite everything, I am happy with the progress in ranking from 4602 to 2308! 

**Day 9 - Mirage Maintenance** A laborious prediction in the past, when all you had to do was reverse the list.

**Days 10 & 11- Pipe Maze/Cosmic Expansion** Idea was good, difficult to set up.

**Day 12 - Hot Springs** Enumerating and testing all possible arrangements was not too expansive for 1st *, and made easier with the help of `itertools.combinations()`. But I had to cheat and to look at a published solution to get the 2nd *. I'd never have thought of using a recursive function on my own.

**Day 13 - Point Of Incidence** Not quite awake this morning. More complicated to understand than to realize.

**Day 14 - Parabolic Reflector Dish** Spent a lot of time debugging. I had to insert what I thought was a calculation error to get the right answer from the test vector and finally the 2nd *! 

**Day 15 - Lens Library** Second part takes some time to understand and solved a funny bug: I wanted to reuse the `hash()` function defined in first part. But that function was not visible in scope of part 2, so I was using the buily-in `hash()` function!

**Day 16 - The Floor Will Be Lava** This is the first time that the Structural Pattern Matching paradigm, which I try to use from time to time, has really come in handy. As a result, I've got a better grasp of the syntax. ex: `case (_, _, '.') | (_, 0, '-') | (0, _, '|'):`. Need a better algorithm actually since 3min for part 2 is too much.

**Day 17 - Clumsy Crucible** My solution was a complete depth-first graph walk with some heuristic and pruning with help of `bisect`module. Happy to have the 2* at last, but not satisfied with how long it took (6min and 15min), I throw a eye to winning solutions. And learn two main things: 1) the right algorithm is [the Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) 2) the `heapq`module can help.

**Day 18 - LavaductLagoon** After wandering for a long time over a two-dimensional map of the trench, trying to reuse the method of day10, I ended up remembering that we could very simply calculate the area delimited by a closed curve. It still took some time to include the half width of the digger in the calculation with complex solutions when it's so simple. In the end the 2nd * came in 5 minutes.

**Day 19 - Aplenty** Wanted a breakfast before going for a walk into the workflow graph.



