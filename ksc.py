# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

number = 0
for score in [90,25,67,45,93]:
    number += 1
    if score >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
        