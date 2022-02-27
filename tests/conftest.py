import pytest
from brownie import Callee, UnsafeCaller, Underflow, accounts;

@pytest.fixture(scope="module")
def callee():
    return accounts[0].deploy(Callee)

@pytest.fixture(scope="module")
def unsafeCaller():
    return accounts[0].deploy(UnsafeCaller)

@pytest.fixture(scope="module")
def underflow():
    return accounts[0].deploy(Underflow)