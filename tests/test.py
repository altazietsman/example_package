from testpackage import mean,add,SayHello

def mean():

    assert mean(3,3) == 3, 'incorrect'
    assert mean(2, 4) == 3, 'incorrect'

def add():

    assert add(3,3) == 6, 'incorrect'
    assert add(2, 4) == 6, 'incorrect'


def SayHello():

    assert SayHello('Alta') == 'Hello Alta', 'incorrect'
    assert SayHello('Linda') == 'Hello Linda', 'incorrect'
