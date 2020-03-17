from increment import countDecimalPlaces
from random import randrange, shuffle


def test_stamente_one():
    assert countDecimalPlaces(1) == 1

def test_stamente_two():
    assert countDecimalPlaces(9) == 2

def test_4_decimals():
    assert countDecimalPlaces(1000) == 4

def test_5_decimals():
    assert countDecimalPlaces(10000) == 5

def test_6_decimals():
    assert countDecimalPlaces(10000) == 5

def test_11_decimals():
    assert countDecimalPlaces(createNumber(10)) == 11

def test_1001_decimals():
    assert countDecimalPlaces(createNumber(1000)) == 1001

def test_100001_decimals():
    assert countDecimalPlaces(createNumber(100000)) == 100001

def test_200001_decimals():
    assert countDecimalPlaces(createNumber(200000)) == 200001

def test_createNumber():
    assert createNumber(10) == 10000000000
    assert createNumber(20) == 100000000000000000000
    assert createNumber(100) == 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


def createNumber(to):
    if ((to % 10) != 0):
        raise Exception('Bad input')
    value = '1'

    if ((to % 100) == 0):
        for _i in range(int(to/100)):
            value += '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        
        return int(value)
    
    for _i in range(int(to/10)):
        value += '0000000000'
    
    return int(value)