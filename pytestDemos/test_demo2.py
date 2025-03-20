def test_firstProgram(setup):
    msg = "Hey, How are you?"
    assert msg == "Hey", "Test failed because strings do not match"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"
