# -*- coding: utf-8 -*-

import hashlib

def calculate_hash(timestamp, previous_hash, data):
    
    block_contents = f"{timestamp}{previous_hash}{data}"
    return hashlib.sha256(block_contents.encode()).hexdigest()

def validate_block(current_block, previous_block):
   
    
    if current_block.hash != calculate_hash(
        current_block.timestamp, current_block.previous_hash, current_block.data
    ):
        return False

    if current_block.previous_hash != previous_block.hash:
        return False

    return True
