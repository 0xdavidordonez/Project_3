// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

// Import the ERC721Full contract from OpenZeppelin to use for creating non-fungible tokens.
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

// Define the NFT_Registry contract, which inherits from ERC721Full, to manage a registry of NFT artworks.
contract NFT_Registry is ERC721Full {
    // Constructor that initializes the ERC721Full contract with a name and symbol for the token.
    constructor() public ERC721Full("NFT_Registry", "NFTREG") {}

    // Struct to store information about each artwork.
    struct Artwork {
        string name;    // Name of the artwork
        string artist;  // Name of the artist
        string artJson; // Metadata in JSON format for the artwork
    }

    // A mapping from token ID to Artwork, storing each token's associated artwork data.
    mapping(uint256 => Artwork) public artCollection;
    
    // Function to retrieve the JSON metadata URI for a given token.
    function imageUri(uint256 tokenId) public view returns (string memory imageJson) {
        return artCollection[tokenId].artJson;
    }
    
    // Function to register a new artwork and mint an associated NFT.
    // The function requires details about the artwork and the owner's address.
    function registerArtwork(
        address owner,
        string memory name,
        string memory artist,
        string memory tokenURI,
        string memory tokenJSON
    ) public returns (uint256) {
        uint256 tokenId = totalSupply(); // Get the current total supply of tokens to use as the new token's ID.
        _mint(owner, tokenId); // Mint a new token for the owner.
        _setTokenURI(tokenId, tokenURI); // Set the token's URI to the provided URI.
        artCollection[tokenId] = Artwork(name, artist, tokenJSON); // Store the artwork data in the mapping.
        return tokenId; // Return the newly created token's ID.
    }
}
