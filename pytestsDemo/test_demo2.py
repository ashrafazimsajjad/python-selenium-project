import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = 'Hello'
    assert msg == 'Hi', 'This test failed'


def test_secondProgram():
    a=4
    assert a+2 == 6, 'Test failed'
