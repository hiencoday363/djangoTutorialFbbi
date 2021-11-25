import hashlib


def HashPass(val):
    encode_raw = val.encode()
    hasher = hashlib.sha256(encode_raw)
    hex_dig = hasher.hexdigest()
    return hex_dig
