#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:28:21 2024

@author: kimseongcheol
"""
def sum1(a, b):
    x = a + b
    return x

def sum2(*args):
    x = 0
    for i in args:
        x += i
    return x

a = 5
b = 3

print(sum1(a, b))
print(sum1(3, 5))
print(sum2(1, 2, 3, 4, 5))
print(sum2(2, 3.5, 10))