____________________

Why did I use this instead of remix? It's because of efficiency. The goal will be to try to automate certain task.

The reason why this token exist is because we're trying to identify a way where we can generate a solidity contract via python and then deploy it automatically as soon as it is minted on the dapp. Users can then go to opensea to view the NFTs.

____________________

This is **Test_Token**, a token I created and deployed onto the Ethereum's testnet (**Sepolia**) utilizing **Brownie**, a python framework dedicated to making it more efficient to deploy smart contracts on the blockchain.

https://sepolia.etherscan.io/tx/0x23f0a8e69f9016a706dc4e9c6247e187c632f8d57ac508c825e7aa72dfd4c6ad

**NOTE:**

**Brownie:**

https://github.com/eth-brownie/brownie

In the near future brownie will be discontinued and **Ape** from **ApeWorx** will be it's successor.

**Ape**

https://github.com/ApeWorX/ape

I decided to stick way Brownie because people are still using it and their a ton of tutorials out there for this.

____________________

**Important Terminal Commands:**
1) pip install eth-brownie
     - Install **Brownie**, a popular framework you can utilize with python to help you create, test and deploy smartcontracts.
3) brownie --help
4) brownie network list
   - identify RPCs available to connect. More can be added.
5) brownie run scripts/deploy_Test_Token.py
   - this is necessary to run the python script necessary to compile and deploy the contract

..their are more, but those are the ones I mostly used.

**Docs:**
1) **Brownie:**
   - https://eth-brownie.readthedocs.io/

3) **OpenZeppelin:**
   - https://docs.openzeppelin.com/
  
**Other Resources:**
1) **Infura**
   - infura.io
     - Needed an endpoint to connect directly to the blockchain in order to interact/deploy contracts.
