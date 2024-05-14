The main folder is the **NFT_APP** folder.
Note that unless you're looking at the **Draft**..
..the only thing that needs to be changed is the api keys with Pinata & OpenAI including the rpc in order to get the page working.

**As of May 13th, 2024:**

We have deployed the Dynamic NFT onto a testnet. For the OpenAI's Dalle AI image generator for tokenization portion of the project, it only works on the local blockchain with **Ganache**.

Future implementations might or might not be on streamlit. It might even be a hybrid. It's still undecided.....where this project might ultimately turn out like.

Originally, we wanted to take this project in so many directions.
We wanted to hook it up to BitTensor's image generator via a **discord token**, but decided to go with OpenDalle instead because of API related issues.
The discord token regenerates every so few minutes. We can't have that going on for our app until their is a solution figured for it.

We wanted to host it on "[InfinityFree](https://www.infinityfree.com/)" with WordPress utilizing iframes for the Streamlit application via **Replit**.
The idea, was to have [Uptimerobot](http://uptimerobot.com/) monitor the website's up time and with a specific script we can keep pinging the website while it's hosted on **Replit** so the streamlit application doesn't automatically shutoff and it can continiously be hosted via an iframe on a wordpress website.
Haven't figured out that portion yet so it's functional.

We also wanted to deploy the NFT registry token onto a testnet with Brownie, but we didn't take that route either.

..it didn't go out as planned, but we learned alot. This is pretty much all our work-in-progress. We decided to just stick with streamlit since it's what's mostly used in class.

If we did went with the route of wordpress, it would be here, a wordpress website / streamlit hybrid.

[arcana.rf.gd](http://arcana.rf.gd/) (currently down)

_________________________________________________________

**Whitepaper:
Leveraging Blockchain Technology for Dynamic NFTs and Decentralized Art Management
Abstract**

Here at Arcana, we have developed tools that utilizes blockchain technology to manage and deploy dynamically evolving Non-Fungible Tokens (NFTs). What we have built here incorporates Solidity for Ethereum-based smart contract development & Chainlink Automation for time-based event handling utilizing standards from OpenZeppelin for secure smart contract functionalities.

**Introduction**

Non-Fungible Tokens (NFTs) have transformed digital ownership and created new markets for unique digital assets. Traditional NFTs are static, meaning their properties do not change after being minted. However, there is growing interest in dynamic NFTs, which can evolve over time or in response to external inputs. This paper introduces a system that combines blockchain technology, automated smart contracts, and AI-generated content to create a more interactive and engaging NFT experience.

**System Overview**

The dapp currently comprises two primary components: a smart contract framework for minting and managing NFTs, and a frontend application for user interaction and visualization. Key features include:

    1) Dynamic NFT Smart Contract:
        A Solidity smart contract that allows NFTs to evolve based on time intervals using Chainlink Automation.
    
    2) Decentralized Storage:
        Utilization of IPFS for storing NFT metadata and associated digital assets, ensuring content is tamper-proof and permanently accessible.
    
    3) AI-Driven Content Generation:
        Integration with OpenAI’s DALL-E to dynamically generate images based on user inputs, enhancing the uniqueness of each NFT.
    
    4) Art Registry and Management:
        A system to register and track digital artworks, tying them to unique NFTs and ensuring artist attribution and provenance.

**Technical Architecture**

    1) Smart Contracts:
        Lootbox: Inherits ERC721 standard for NFTs; uses Chainlink Automation to evolve NFTs based on predefined time intervals.
        
    2)  NFT_Registry:
        Manages a registry of digital artworks, associating each with a unique NFT.

    3) Decentralized File Storage:
        Utilizes IPFS for storing image files and metadata in a decentralized manner to avoid single points of failure and ensure integrity.

    4) Image Generation:
        Leverages OpenAI’s API to generate images through DALL-E 3, based on descriptive inputs from users. These images are minted as NFTs, providing dynamic and personalized content.

    5) Frontend Application:
        A Streamlit-based interface that allows users to interact with the smart contracts, generate images, and register artworks.

**Use Cases**

    1) Dynamic Collectibles:
        NFTs that evolve visually or in complexity over time, increasing engagement and long-term value.
    
    2) Artist Portfolios:
        Artists can register their artworks, mint associated NFTs, and manage their digital portfolio in a decentralized manner.
    
    3) Gaming:
        In-game assets represented as NFTs can evolve based on player achievements or in-game events.

**Challenges and Considerations**

    1) Scalability:
        Handling high transaction volumes and large data storage on IPFS can increase costs and affect performance.
    
    2) Security:
        Smart contracts must be audited thoroughly to prevent vulnerabilities that could be exploited.
    
    3) Legal and Ethical:
        Issues around copyright, artist rights, and AI-generated content need careful consideration.

**Conclusion**

The integration of blockchain technology, IPFS, and AI-generated content provides a robust platform for managing dynamic NFTs and digital art. By addressing the technical challenges and ethical considerations, this system can significantly enhance the digital collectibles market and offer new opportunities for artists and collectors.

**Future Work**

    - Explore layer-2 solutions for scalability improvements.
    - Improve & expand the AI integration.

This approach not only revolutionizes how digital assets are perceived and traded, but also opens up new avenues for creative expression and digital interaction in the blockchain space.
