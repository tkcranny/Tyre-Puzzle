# Tyre Puzzle

At a café in Toowoomba, some friends and I were intrigued by a
simple-looking puzzle made to entertain children. It was made of a
couple dozen tyres laid out, with coloured planks attaching adjacent
ones. The rules were simple, just follow the planks in order of
**Red**, **Blue**, **Green**, starting from the single tyre next to the
rules board, and get to the tyre in the very centre.

A simple enough diversion for a few minutes; we thought we'd quickly
beat it and carry on our way.

![](./images/puzzle.jpeg)

Half an hour later, we still hadn't solved it. I was starting to wonder
if this was solvable at all, or if Toowoombanese children are just far
smarter than me. No one in our brainy group was even getting close.
We eventually called it quits and left without ever getting to the last
tyre.

I did however take couple photos of the puzzle, thinking that there
ought to be a way to plug it into a computer to at least see if it's
solvable at all. For the rest of our outing, I roughly planned how I
though I'd solve it. First, I'd translate the puzzle into a trusty
[Directed Acyclic
Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph), run it
through a tweaked copy of [Djikstra's
algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), and
voila, we'd have the answer.

I didn't have my computer with me, but I did have an iPad with
Pythonista installed. The rest of the afternoon, while chatting and
drinking, I plugged away, sketching the puzzle, and translating the
edges into a format describing a graph.
