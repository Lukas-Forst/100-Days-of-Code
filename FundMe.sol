// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces(AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe{

    mapping(address => uint256) public addressToAmountFunded;

    // payable signals that the function is used to pay. signals how much wei/gwei are used 
    function fund() public payable {
        addressToAmountFunded[msg.sender] += msg.value;

        
    }
}