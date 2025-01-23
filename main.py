# -*- coding: utf-8 -*-


from blockchain import Blockchain

if __name__ == "__main__":
    # Blockchain құру
    blockchain = Blockchain()

    # Жаңа блоктарды қосу
    blockchain.add_block("1-bloktyn derekteri")
    blockchain.add_block("2-bloktyn derekteri")

    # Blockchain-ді басып шығару
    print("Blockchain:")
    print(blockchain)

    # Blockchain-нің бүтіндігін тексеру
    print("Blockchain durys pa:", blockchain.is_chain_valid())

