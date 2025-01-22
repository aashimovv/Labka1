
def simple_hash(data):
    hash_value = 0
    for char in data:
        hash_value = (hash_value * 31 + ord(char)) % 1000000007
    return hash_value

# Тест
data = "Blockchain Basics"
print(f"Data: {data}, Hash: {simple_hash(data)}")
