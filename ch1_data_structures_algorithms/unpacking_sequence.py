#!/usr/bin/env python3

p = (4, 5)
x, y = p
print("x:", x, "y", y)

my_list = [1, "hello"]
r, s = my_list
# r = 1, s = "hello"

some_string = "hi"
t, u = some_string

# Can use throwaway variable names if you want to discard certain things
data = ["useful", "useless"]
needed, _ = data

quick_experiment = [1,2,3]
# a,b = quick_experiment
# Throws an error

c = 1
d = 2
another_experiment = c,d
print(another_experiment) # (1, 2)
