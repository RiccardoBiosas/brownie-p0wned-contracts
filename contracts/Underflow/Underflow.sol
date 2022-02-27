pragma solidity 0.7.6;

contract Underflow {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount) external {
        require(balances[msg.sender] - _amount >= 0, "NOT ENOUGH BALANCE");
        (bool success, bytes memory result) = msg.sender.call{value: _amount}("");
        require(success == true, "transfer unsuccessful");
        balances[msg.sender] = balances[msg.sender] - _amount;
    }
}