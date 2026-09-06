"""Loader: builds the runnable stub that decodes and executes the payload."""
import base64
import marshal
from typing import Dict

LOADER_TMPL = '''# hawoo
{dummy}
import base64
import marshal
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

_version = {version}
_key = base64.b64decode({key!r})
_nonce = base64.b64decode({nonce!r})
_ct = base64.b64decode({ciphertext!r})

try:
    aead = ChaCha20Poly1305(_key)
    xored = aead.decrypt(_nonce, _ct, b'pycrypt-v2')
except Exception as e:
    raise SystemExit(f"[!] failed to decrypt payload: {e}")

# reverse XOR
payload = bytes([c ^ {xor_key} for c in xored])
exec(marshal.loads(payload))
'''

class Loader:
    def build_loader(self, packed: Dict, add_dummy: bool = True, xor_key: int = 13) -> str:
        dummy = ''
        if add_dummy:
            dummy = "# dummy: " + __import__('secrets').token_hex(8)
        return LOADER_TMPL.format(
            dummy=dummy,
            version=packed['version'],
            key=packed['key'],
            nonce=packed['nonce'],
            ciphertext=packed['ciphertext'],
            xor_key=xor_key,
        )
