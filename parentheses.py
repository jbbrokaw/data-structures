#!/usr/bin/env python
from __future__ import unicode_literals


def parse_parens(text):
    open_parentheticals = 0
    for i in text:
        if i == '(':
            open_parentheticals += 1
        if i == ')':
            open_parentheticals += -1
        if open_parentheticals == -1:
            return -1
    if open_parentheticals > 0:
        return 1
    if open_parentheticals < 0:
        return -1
    return 0
