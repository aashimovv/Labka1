# -*- coding: utf-8 -*-
from block import Block
import time

class Blockchain:
    def __init__(self):
        """Initsializatsiya blockchain-a s genesis-blokom."""
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Sozdaet genesis-blok s fiksirovannymi dannymi."""
        return Block(timestamp=time.time(), previous_hash="0", data="Genesis blok")

    def get_latest_block(self):
        """Vozvrashchaet posledniy blok v tsepochke."""
        return self.chain[-1]

    def add_block(self, data):
        """Dobavlyaet novyy blok v tsepochku blokov."""
        latest_block = self.get_latest_block()
        new_block = Block(
            timestamp=time.time(),
            previous_hash=latest_block.hash,
            data=data
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Proveryaet tselostnost tsepochki blokov."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Proverka khesha tekushchego bloka
            if current_block.hash != current_block.calculate_hash():
                return False

            # Proverka sootvetstviya khesha predydushchego bloka
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __repr__(self):
        """Predstavlenie blockchain-a v chitayemom vide."""
        return "\n".join([str(block) for block in self.chain])
