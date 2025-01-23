# -*- coding: utf-8 -*-

import hashlib

class Block:
    def __init__(self, address, timestamp, data):
        self.address = address
        self.timestamp = timestamp
        self.data = data

    def is_valid(self):
        """Bloktıñ validtiğini tekserip, jaramsız bolsa False qaytaradı."""
        # Jaramdılıq tekserui - adresi men timestamp arqılı
        if not self.address or not self.timestamp or not self.data:
            return False
        if len(self.address) != 64:  # Hash adresi bolıp 64 belgiden turadı
            return False
        # Qosımşa tekserwlerdi qoswğa boladı
        return True

    def __str__(self):
        return f"Address: {self.address}, Timestamp: {self.timestamp}, Data: {self.data}"

    @staticmethod
    def create_hash(data):
        """Bloktıñ xeshi (hash) funksiıası."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()


