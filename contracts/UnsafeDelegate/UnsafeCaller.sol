pragma solidity 0.8.10;

contract UnsafeCaller {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function delegateToCallee(address _addr, uint256 _n) external returns(bool, bytes memory) {
        (bool success, bytes memory response) = _addr.delegatecall(abi.encodeWithSignature("setFavoriteNumber(uint256)", _n));
        return (success, response);
    }
}

