#!/usr/bin/python

#!Creating Exponent Functions

print(49**3) #!this is the same as saying 49^3

#!Using forloops

def power_raise (base_number, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_number
    return result

print(power_raise(54, 3))

#!Go ahead and test it out!!!
