"""Core compiler: public CLI interface and glue."""
from .obfuscator import Obfuscator
from .packer import Packer
from .loader import Loader
from ..utils.validation import validate_input_path, validate_layers, validate_xor_key

import argparse
import sys

def build_parser():
    p = argparse.ArgumentParser(prog='pycrypt', description='PyCrypt v2 - script obfuscator')
    p.add_argument('input', help='input python file')
    p.add_argument('output', help='output file (.py)')
    p.add_argument('-l','--layers', type=int, default=3, help='number of marshal layers')
    p.add_argument('-k','--key', type=int, default=13, help='XOR key (0-255)')
    p.add_argument('--no-dummy', action='store_true', help='do not inject dummy code')
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    # validation
    validate_input_path(args.input)
    validate_layers(args.layers)
    validate_xor_key(args.key)

    ob = Obfuscator(layers=args.layers, xor_key=args.key, add_dummy=not args.no_dummy)
    packer = Packer()
    loader = Loader()

    src = ob.read_file(args.input)
    payload = ob.compile_and_obfuscate(src)
    packed = packer.pack(payload, xor_key=args.key)
    stub = loader.build_loader(packed, add_dummy=not args.no_dummy)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(stub)

    print(f"[✓] file berhasil terenkripsi ➜ {args.output} (Layers: {args.layers}, XOR Key: {args.key})")
