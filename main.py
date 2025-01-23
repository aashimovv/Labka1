
from blockchain import Blockchain

def main():
    blockchain = Blockchain()

    blockchain.add_block("First block data")
    blockchain.add_block("Second block data")

    print("Blockchain valid:", blockchain.is_chain_valid())
    for block in blockchain.chain:
        print(block)

if __name__ == "__main__":
    main()
