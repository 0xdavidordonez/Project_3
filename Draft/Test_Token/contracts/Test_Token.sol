// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts ^5.0.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Test_Token is ERC20 {
    constructor() ERC20("Test_Token", "TEST") {
        _mint(msg.sender, 200000 * 10 ** decimals());
    }
}
