# Blockchain01
# Blockchain Simulation
This repository presents a hands-on Python based simulation suite that introduces key concepts of blockchain technology. The project covers block creation, mining logic, and a comparison of major consensus mechanisms.
## Project Overview

### 1. Basic Blockchain Structure (`blockchain.py`)

A simple blockchain implementation showcasing the foundational design of a blockchain.

**Highlights:**
- Block structure with index, timestamp, data, nonce, and hashes
- SHA-256 hashing for block security
- Block-to-block linking using previous hashes
- Chain integrity check and tamper detection
- Basic Proof-of-Work simulation

**Concepts Covered:**
- Block Anatomy: index, data, nonce, previous hash, current hash
- Hashing: cryptographic linkage using SHA-256
- Tampering Demo: how altering a block breaks the chain
- Validation: checking the integrity of the entire chain

---

### 2. Mining Simulation (`mining_sim.py`)

A simulation that replicates block mining using increasing difficulty levels.

**Highlights:**
- Adjustable difficulty (e.g., hash starts with `0000`)
- Real-time mining feedback and statistics
- Performance metrics: number of attempts, time taken
- Hashrate calculation (hashes/sec)

**Concepts Covered:**
- Proof of Work (PoW): brute-force mining with nonce
- Difficulty tuning: how hash conditions impact mining time
- Performance monitoring: time, attempts, efficiency

---

### 3. Consensus Algorithms Demo (`consensus_sim.py`)

A demonstration of three major blockchain consensus methods.

**Highlights:**
- Proof of Work (PoW): random power-based selection
- Proof of Stake (PoS): selection based on staked value
- Delegated Proof of Stake (DPoS): vote-based validator selection
- Console-based selection output and explanation

**Concepts Covered:**
- Consensus Models: PoW, PoS, DPoS
- Validator selection logic
- Comparing security and efficiency trade-offs
