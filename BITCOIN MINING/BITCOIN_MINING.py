import hashlib

def mine_block(block_data, difficulty):
    for nonce in range(100000000):
        data = block_data + str(nonce)
        hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
        if hash[:difficulty] == '0' * difficulty:
            return (hash, nonce)
    return None

# Minen Sie einen Block mit Schwierigkeit 4
block_data = 'Das sind meine Blockdaten'
difficulty = 4
result = mine_block(block_data, difficulty)
if result:
    print(f'Geminter Block mit Hash: {result[0]} und Nonce: {result[1]}')
else:
    print('Es konnte kein gültiger Block gefunden werden')

