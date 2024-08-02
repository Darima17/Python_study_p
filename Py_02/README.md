## Python Bootcamp

### Exercise 00: Gaining Access

You need to describe a Python class `Key' so that an instance of this class would pass the checks listed above. Note that your code in this exercise shouldn't create containers of size 404 or smaller. Even without them, you should be able to pass these checks.

You are encouraged to write an actual set of tests to simulate the key checks according to the bugs above (and to make peer review easier). This will be graded as a bonus.

### Exercise 01: Morality

ZAX told of the simple game of candy, where there is a machine that controls the supply of candy to two groups of people based on whether one or both of two operators put candy in it:

|  | Both cooperate | 1 cheats, 2 cooperates | 1 cooperates, 2 cheats | Both cheat |
|------------|----------|----------|----------|---------|
| Operator 1 | +2 candy | +3 candy | -1 candy | 0 candy |
| Operator 2 | +2 candy | -1 candy | +3 candy | 0 candy |

So if everyone cooperates and puts candy into the machine as agreed, everyone gets a reward. But both participants also have the temptation to cheat and only pretend to put a candy into the machine, because in this case their group will get 3 candies back by taking only one candy from a second group. The problem is that if both operators decide to play dirty, then nobody gets anything.

ZAX also mentioned five behavioral models that he used to run experiments:

| Behavior type | Player Actions                                                                                                                                                                                         |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cheater       | Always cheats                                                                                                                                                                                          |
| Cooperator    | Always cooperates                                                                                                                                                                                      |
| Copycat       | Starts with cooperating, but then just repeats whatever the other guy is doing                                                                                                                         |
| Grudger       | Starts by always cooperating, but switches to Cheater forever if another guy cheats even once                                                                                                          |
| Detective     | First four times goes with [Cooperate, Cheat, Cooperate, Cooperate],  and if during these four turns another guy cheats even once — switches into a Copycat. Otherwise, switches into Cheater himself |

-----

