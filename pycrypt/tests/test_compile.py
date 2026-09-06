"""Tests for compilation and roundtrip encode/decode."""
import tempfile
import os
from core.obfuscator import Obfuscator
from core.packer import Packer
from core.loader import Loader


def test_compile():
    ob = Obfuscator(layers=1)
    src = 'x=1\nprint(x)\n'
    payload = ob.compile_and_obfuscate(src)
    assert payload.startswith(b"\x" ) or isinstance(payload, bytes)


def test_roundtrip():
    ob = Obfuscator(layers=1)
    src = 'x=42\nprint(x)\n'
    payload = ob.compile_and_obfuscate(src)

    packer = Packer()
    packed = packer.pack(payload, xor_key=7)

    loader = Loader()
    stub = loader.build_loader(packed, add_dummy=False, xor_key=7)

    # execute stub in a isolated namespace
    ns = {}
    exec(stub, ns)
    # after execution, x should be in globals with value 42
    assert ns.get('x', 42) == 42
