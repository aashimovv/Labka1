# -*- coding: utf-8 -*-
import hashlib

class Block:
    def __init__(self, timestamp, previous_hash, data):
        """Inicializaciya bloka."""
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Vychislenie khesha dlya tekushchego bloka."""
        block_content = f"{self.timestamp}{self.previous_hash}{self.data}".encode('utf-8')
        return hashlib.sha256(block_content).hexdigest()

    def __repr__(self):
        """Predstavlenie bloka v vide stroki."""
        return f"Block(timestamp={self.timestamp}, previous_hash={self.previous_hash}, hash={self.hash}, data={self.data})"
