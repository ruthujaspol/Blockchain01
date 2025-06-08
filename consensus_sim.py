import random

class Validator:
    def __init__(self, name, power=0, stake=0, votes=0):
        self.name = name
        self.power = power
        self.stake = stake
        self.votes = votes

def proof_of_work(validators):
    print("\n=== Proof of Work (PoW) ===")
    selected = max(validators, key=lambda v: v.power)
    for v in validators:
        print(f"{v.name}: {v.power:.2f} hash power")
    print(f"\nSelected: {selected.name} (Highest Power)")
    return selected

def proof_of_stake(validators):
    print("\n=== Proof of Stake (PoS) ===")
    selected = max(validators, key=lambda v: v.stake)
    for v in validators:
        print(f"{v.name}: {v.stake:.2f} tokens staked")
    print(f"\nSelected: {selected.name} (Highest Stake)")
    return selected

def delegated_proof_of_stake(validators):
    print("\n=== Delegated Proof of Stake (DPoS) ===")
    selected = max(validators, key=lambda v: v.votes)
    for v in validators:
        print(f"{v.name}: {v.votes} votes")
    print(f"\nSelected: {selected.name} (Most Votes)")
    return selected

def main():
    pow_validators = [
        Validator("Ravi", power=random.uniform(50, 100)),
        Validator("Sita", power=random.uniform(50, 100)),
        Validator("Arjun", power=random.uniform(50, 100))
    ]
    pos_validators = [
        Validator("Meera", stake=random.uniform(1000, 5000)),
        Validator("Aman", stake=random.uniform(1000, 5000)),
        Validator("Priya", stake=random.uniform(1000, 5000))
    ]
    dpos_validators = [
        Validator("Lakshmi", votes=random.randint(1, 100)),
        Validator("Rahul", votes=random.randint(1, 100)),
        Validator("Deepa", votes=random.randint(1, 100))
    ]

    proof_of_work(pow_validators)
    proof_of_stake(pos_validators)
    delegated_proof_of_stake(dpos_validators)

if __name__ == "__main__":
    main()
