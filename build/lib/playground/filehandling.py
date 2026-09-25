from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import base64



def generate_keys():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign_manifest(private_key, path):
    content = path.read_bytes()
    return private_key.sign(content)

def encode_bytes(key):
    return base64.b64encode(key).decode()

def write_file(path, content):
    path.write_text(content)
