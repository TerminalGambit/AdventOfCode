# the program runs as follows:
# ./run-program.zsh yy dd part type

# yy: year is two digits and corresponds to the file name for example if yy=15 it's 2015/
# dd: day is two digits and corresponds to the file name for example if dd=01 it's day01/
# part: part is the part of the day, it can be either 1 or 2
# type: type is the type of the file, it can be either test or actual

# Example:
# ./run-program.zsh 15 01 1 test

# The program will run the following command:
# python3 ./2015/day01/code/day01-1.py