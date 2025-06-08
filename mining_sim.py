import hashlib
import time

def mine_block(data, difficulty):
    prefix = '0' * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        text = f"{data}{nonce}"
        new_hash = hashlib.sha256(text.encode()).hexdigest()
        if new_hash.startswith(prefix):
            break
        nonce += 1

    end_time = time.time()
    return nonce, new_hash, end_time - start_time

def main():
    data = "Sita sends 7 BTC to Arjun"
    difficulty = 4

    print(f"Mining block with data: '{data}' and difficulty: {difficulty}")
    nonce, hash_result, duration = mine_block(data, difficulty)
    print(f"\n✅ Block Mined Successfully!")
    print(f"Nonce      : {nonce}")
    print(f"Hash       : {hash_result}")
    print(f"Time Taken : {duration:.2f} seconds")

if __name__ == "__main__":
    main()