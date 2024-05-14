// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";
import "@openzeppelin/contracts@4.6.0/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts@4.6.0/utils/Counters.sol";

contract LootBox is ERC721, ERC721URIStorage, AutomationCompatibleInterface {
    using Counters for Counters.Counter;

    Counters.Counter public tokenIdCounter;
 
   // Metadata information for each stage of the NFT on IPFS.
    string[] IpfsUri = [
        "https://ipfs.io/ipfs/QmeHDVWaKg6e9ESy2PGHj132Kqw8Xxkv8ArZYDMLj2Ee6G?/filename=box3.json",
        "https://ipfs.io/ipfs/QmSu7iNxrN1LH8fSjHxcGXDkjtfLm6LJ81ybPcyfUCeW1c?/filename=art14.json"
    ];

    uint public immutable interval;
    uint public lastTimeStamp;

    constructor(uint updateInterval) ERC721("Block Magic NFT Collection", "BLOCKS") {
        interval = updateInterval;
        lastTimeStamp = block.timestamp;
        safeMint(msg.sender);
    }

    function safeMint(address to) public {
        uint256 tokenId = tokenIdCounter.current();
        tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, IpfsUri[0]);
    }

    // determine the stage of the Box
    function BoxStage(uint256 _tokenId) public view returns (uint256) {
        string memory _uri = tokenURI(_tokenId);
        // Box
        if (compareStrings(_uri, IpfsUri[0])) {
            return 0;
        }
        // ART
        if (
            compareStrings(_uri, IpfsUri[1])
        ) {
            return 1;
        }
        // Must be ART
        return 2;
    }

    function EvolveBox(uint256 _tokenId) public {
        if(BoxStage(_tokenId) >= 2){return;}
        // Get the current stage of box and add 1
        uint256 newVal = BoxStage(_tokenId) + 1;
        // store the new URI
        string memory newUri = IpfsUri[newVal];
        // Update the URI
        _setTokenURI(_tokenId, newUri);
    }

    // helper function to compare strings
    function compareStrings(string memory a, string memory b)
        public pure returns (bool)
    {
        return (keccak256(abi.encodePacked((a))) ==
            keccak256(abi.encodePacked((b))));
    }

    function checkUpkeep(bytes calldata /* checkData */) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        if ((block.timestamp - lastTimeStamp) > interval ) {
            uint256 tokenId = tokenIdCounter.current() - 1;
            if (BoxStage(tokenId) < 2) {
                upkeepNeeded = true;
            }
        }
        
    }

    function performUpkeep(bytes calldata /* performData */) external override {
        //revalidating the upkeep in the performUpkeep function
        if ((block.timestamp - lastTimeStamp) > interval ) {
            uint256 tokenId = tokenIdCounter.current() - 1;
            if (BoxStage(tokenId) < 2) {
                lastTimeStamp = block.timestamp;            
                EvolveBox(tokenId);
            }
        }
        
    }
    
    function tokenURI(uint256 tokenId)
        public view override(ERC721, ERC721URIStorage) returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    // The following function is an override required by Solidity.
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

}

