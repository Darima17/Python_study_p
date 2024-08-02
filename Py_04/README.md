# Day 04 - Python Bootcamp

** Energy Flow Exercise
In this exercise, we will implement a function called fix_wiring that takes three lists as input: cables, sockets, and plugs. The function filters out any non-string elements from the input lists and then zips them together to create a new list of tuples. The function then filters out any tuples where the second and third elements are not None. Finally, it applies a mapping function to the filtered list to construct strings based on the values in the tuples.

**Personalities Exercise
In this exercise, we will implement a function called turrets_generator that generates instances of a dynamically generated class called Turret. The class will have five personality traits: neuroticism, openness, conscientiousness, extraversion, and agreeableness. Each trait will be a random number between 0 and 100, and the sum of all five traits for each instance should be 100. The class will also have three methods: shoot, search, and talk, which will print the corresponding strings.

**Backpressure Exercise
In this exercise, we will implement a generator function called emit_gel that simulates the measured pressure of a liquid. The function will generate an infinite stream of numbers from 0 to 100 with a random step sampled from the range [0, step], where step is an argument to the generator.

To implement pressure control, we will write another function called valve that will loop over the values of emit_gel and use the .send() method to reverse the sign of the current step.

To implement an emergency break, we will check if the pressure is above 90 or below 10. If so, the emit_gel generator will gracefully close and the script will exit.

Feel free to experiment and choose a step so that your script runs for a few seconds before exiting. You can add a delay between pressure measurements to avoid using too much CPU to generate and process the sequence.
