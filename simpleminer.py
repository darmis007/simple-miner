from hashlib import sha256
MAX_NONCE_VALUE = 100000000000

def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash,prefix_zeros):
  prefix_str = '0'*prefix_zeros
  for nonce in range(MAX_NONCE_VALUE):
    text=str(block_number)+transactions+previous_hash+str(nonce)
    new_hash=SHA256(text)
    if new_hash.startswith(prefix_str):
      print("Bitcoin Mined for nonce value of: {}".format(nonce))
      return new_hash
