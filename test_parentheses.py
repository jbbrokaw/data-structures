"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest

from parentheses import parse_parens

def test_parse_parens():
    string1 = "no parentheses"
    assert parse_parens(string1) == 0
    string2 = "(I am making an aside)"
    assert parse_parens(string2) == 0
    string3 = "((((I opened too many))"
    assert parse_parens(string3) == 1
    string4 = "(I am broken ))"
    assert parse_parens(string4) == -1
    string5 = ")I am broken a different way("
    assert parse_parens(string5) == -1
    string6 = "(I (am))) broken a different way("
    assert parse_parens(string6) == -1
    with pytest.raises(TypeError):
        parse_parens(799)
