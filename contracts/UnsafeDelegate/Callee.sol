pragma solidity 0.8.10;

contract Callee {
    uint256 public myNum;

    function setFavoriteNumber(uint256 _myNum) external {
        myNum = _myNum;
    }
}