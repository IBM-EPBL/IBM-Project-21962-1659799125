# -*- coding: utf-8 -*-
"""Assignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12legr5FbcJNoNZsZvwtBPGSzbUwHzXMk
"""

import random

t = random.randint(0,100)
h = random.randint(0,100)

print("Temperature is = ",t)
print("Humidity is = ",h)

if t >60 and h > 60:
    print("alarm ON : It's seems to be risky")
elif t > 60 and h < 60:
    print("alarm ON : It's seems to be high temperature")
else:
    print("alarm OFF")