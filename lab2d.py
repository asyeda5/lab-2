#!/usr/bin/env python3
import sys

# Check for the number of arguments
if len(sys.argv) == 1:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()
elif len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()

name = sys.argv[1]  # first argument (name)
age = sys.argv[2]   # second argument (age)

print('Hi ' + name + ', you are ' + age + ' years old.')

