# beehive-solver
A script I wrote to solve the NYT "Beehive" word puzzle (or whatever it's actually called).

The puzzle consists of seven hexagons -- a central hexagon surrounded by a ring of six others -- with each containing a single letter.  The goal was to form as many words as possible from the provided letters, with a couple additional rules.  As I recall:
* The solution word must be at least 4 letters long.
* The solution word must use the central letter.
* Provided letters may be repeated in the solution word.
* And while I don't remember how scoring worked, I do know that solution words using all available letters are PANGRAMS and score double points, so obviously you want to find those.

I think that's about all there is to the game.

Initially I played with a couple different ideas on how to approach the problem, until in the shower one day (naturally) it occurred to me that this problem was actually a question of _sets_:  if the set of letters in a candidate solution word was a subset of the provided letters, it must be a valid solution.  Moreover, if the set of letters in a candidate was _equal to_ the set of provided letters, well, then you've got yourself a PANGRAM!

The coding wasn't hard after that realization.

And yes, I know there's room for optimization.  But here I favored emphasizing "sets as solution" over any code optimization that might distract from this fact.  It just felt like the right thing to do.  :)

Finally, I owe a debt of gratitude to whoever produced the dictionary file I used for candidate solution words.  Well, really, I owe a proper attribution, but sadly I wrote this so long ago that I have no idea where I got the file.  I couldn't have written this script without it, though, so thank you and fine work, kind stranger!
