"""Packer: encoding and authenticated encryption of the payload."""
import base64
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from ..utils.randomize import secure_bytes

class Packer:
    def __init__(self):
        self.version = 2

    def pack(self, payload: bytes, xor_key: int = 13) -> dict:
        # XOR obfuscation
        xored = bytes(b ^ xor_key for b in payload)
        # authenticated encryption with ChaCha20-Poly1305
        key = secure_bytes(32)
        aead = ChaCha20Poly1305(key)
        nonce = secure_bytes(12)
        ct = aead.encrypt(nonce, xored, b'pycrypt-v2')
        return {
            'version': self.version,
            'key': base64.b64encode(key).decode('ascii'),
            'nonce': base64.b64encode(nonce).decode('ascii'),
            'ciphertext': base64.b64encode(ct).decode('ascii'),
        }
