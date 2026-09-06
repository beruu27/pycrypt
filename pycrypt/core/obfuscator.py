"""Obfuscator: handles compilation and optional obfuscation."""
import marshal
from ..utils.randomize import secure_token

class Obfuscator:
    def __init__(self, layers=3, xor_key=13, add_dummy=True):
        self.layers = layers
        self.xor_key = xor_key
        self.add_dummy = add_dummy

    def read_file(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def compile_and_obfuscate(self, src: str) -> bytes:
        # embed a versioned payload header
        code = f"import marshal\n# pycrypt-payload-v2\n" + src
        bytecode = compile(code, '<pycrypt>', 'exec')
        for _ in range(self.layers):
            bytecode = compile(
                f"import marshal\nexec(marshal.loads({repr(marshal.dumps(bytecode))}))",
                '<pycrypt>', 'exec'
            )
        return marshal.dumps(bytecode)
