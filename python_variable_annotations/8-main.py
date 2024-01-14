#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
# this makes the multiplier function that multiplies by 2.22
fun = make_multiplier(2.22)
# this call of fun multiplies arg 2.22 by the multiplier 2.22
print("{}".format(fun(2.22)))
