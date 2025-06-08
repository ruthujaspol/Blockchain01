import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash="0"):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generate SHA-256 hash for the block"""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def display_block(self):
        """Display block details"""
        print(f"Block {self.index}:")
        print(f"  Timestamp: {self.timestamp}")
        print(f"  Data: {self.data}")
        print(f"  Previous Hash: {self.previous_hash}")
        print(f"  Hash: {self.hash}")
        print(f"  Nonce: {self.nonce}")
        print("-" * 50)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Create the first block (Genesis Block)"""
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        """Add a new block with the given data"""
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        print("\nBLOCKCHAIN:")
        print("=" * 50)
        for block in self.chain:
            block.display_block()

    def is_chain_valid(self):
        """Check the validity of the blockchain"""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"Block {i} has been tampered (Hash mismatch)")
                return False

            if current.previous_hash != previous.hash:
                print(f"Block {i} has invalid link to previous block")
                return False

        return True

def main():
    blockchain = Blockchain()

    print("Creating blockchain with 3 blocks...\n")
    blockchain.add_block("Ravi sends 10 BTC to Priya")
    blockchain.add_block("Anjali sends 5 BTC to Arjun")
    blockchain.add_block("Neha sends 15 BTC to Karan")

    # Display blockchain
    blockchain.display_chain()
    print(f"\nBlockchain Valid? {blockchain.is_chain_valid()}\n")

    # Tampering
    print("TAMPERING BLOCK 1 DATA...\n")
    blockchain.chain[1].data = "Ravi sends 1000 BTC to Priya"

    print("BLOCKCHAIN AFTER TAMPERING:")
    blockchain.display_chain()
    print(f"\nBlockchain Valid? {blockchain.is_chain_valid()}\n")

    # Fixing blockchain
    print("FIXING THE BLOCKCHAIN...\n")
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
    for i in range(2, len(blockchain.chain)):
        blockchain.chain[i].previous_hash = blockchain.chain[i-1].hash
        blockchain.chain[i].hash = blockchain.chain[i].calculate_hash()

    print("BLOCKCHAIN AFTER FIXING:")
    blockchain.display_chain()
    print(f"\nBlockchain Valid? {blockchain.is_chain_valid()}")

if __name__ == "__main__":
    main()