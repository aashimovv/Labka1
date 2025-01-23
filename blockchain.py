
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, data)
        if self.is_valid_block(new_block, previous_block):
            self.chain.append(new_block)

    def is_valid_block(self, block, previous_block):
        if block.previous_hash != previous_block.hash:
            return False
        if block.hash != block.calculate_hash():
            return False
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            if not self.is_valid_block(self.chain[i], self.chain[i - 1]):
                return False
        return True

    def __repr__(self):
        return f"Blockchain({self.chain})"
