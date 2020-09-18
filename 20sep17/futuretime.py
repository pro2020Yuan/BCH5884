#!/usr/bin/env python

now=13
hoursahead=37

then=(now+hoursahead%24)%24

print(then)
