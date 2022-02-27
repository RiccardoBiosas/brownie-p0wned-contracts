def test_unsafeCaller_initial_values(unsafeCaller, accounts):
    assert unsafeCaller.owner() == accounts[0]

def test_callee_initial_values(callee):
    assert callee.myNum() == 0

def test_callee_setNum(callee):
    callee.setFavoriteNumber(13)
    assert callee.myNum() == 13

def test_storage_corruption(unsafeCaller, callee):
    unsafeCaller.delegateToCallee(callee.address, 2)
    assert callee.myNum() == 13
    assert unsafeCaller.owner() == "0x"+"0"*38+"02"