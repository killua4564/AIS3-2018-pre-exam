import string
import hashlib

max_nonce = pow(2, 32)

def proof_of_work(header, difficulty_bits):
    target = pow(2, (256 - difficulty_bits))
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256(bytes(str(header) + str(nonce), 'utf8')).hexdigest()
        if int(hash_result, 16) < target: return (hash_result, nonce)
    return nonce

def main_function(string):
    nonce, hash_result = 0, ''
    for difficulty_bits in range(32):
        difficulty = pow(2, difficulty_bits)
        new_block = string + hash_result
        hash_result, nonce = proof_of_work(new_block, difficulty_bits)
        if hash_result[:6] == '000000': return new_block + str(nonce)

print(main_function("4FW6NX"))