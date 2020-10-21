#!/usr/bin/env python3

#print numbers in (1,100) that cannot be divided by 7 or contains "7".
for i in range(1,101):
    if i%7 == 0:
        continue
    if '7' in str(i):
        continue
    print(i)
