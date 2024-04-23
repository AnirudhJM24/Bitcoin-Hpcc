def base58_encode(data):
    """
    Encode bytes into a base58-encoded string
    """
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    n = int.from_bytes(data, 'big')
    res = []
    while n > 0:
        n, r = divmod(n, 58)
        res.append(alphabet[r])
    res = ''.join(res[::-1])
    czero = 0
    pad = 0
    while czero < len(data) and data[czero] == 0:
        pad += 1
        czero += 1
    return alphabet[0] * pad + res

def parse_script_pubkey(script_pubkey_hex):
    if script_pubkey_hex.startswith('76a914') and len(script_pubkey_hex) == 50:
        # P2PKH script
        
        pub_key_hash_hex = script_pubkey_hex[6:-4]
        pub_key_hash_bytes = bytes.fromhex(pub_key_hash_hex)

        version_prefixed = b'\x00' + pub_key_hash_bytes

        checksum = sha256(sha256(version_prefixed).digest()).digest()[:4]

        address_bytes = version_prefixed + checksum
        address = base58_encode(address_bytes)
        return address
    elif script_pubkey_hex.startswith('a914') and len(script_pubkey_hex) == 46:
        # P2SH script
        pub_key_hash_hex = script_pubkey_hex[4:-2]
        pub_key_hash_bytes = bytes.fromhex(pub_key_hash_hex)

        version_prefixed = b'\x00' + pub_key_hash_bytes

        checksum = sha256(sha256(version_prefixed).digest()).digest()[:4]

        address_bytes = version_prefixed + checksum
        address = base58_encode(address_bytes)
        return address
    else:
        address = None
    return address


# Example script_pubkey_hex
script_pubkey_hex = '76a914af8e14a2cecd715c363b3a72b55b59a31e2acac988ac'
#address = parse_script_pubkey(script_pubkey_hex)
address1 = Script.parse_hex(script_pubkey_hex)
print(address1.hash_type)
#address1 = Address(address1.keys)

print(address1)