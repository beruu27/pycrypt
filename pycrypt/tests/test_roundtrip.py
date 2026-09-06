"""Roundtrip test ensuring that packing/unpacking works end-to-end."""
from core.obfuscator import Obfuscator
from core.packer import Packer
from core.loader import Loader


def test_roundtrip_execution():
    ob = Obfuscator(layers=1)
    src = 'y=123\n'
    payload = ob.compile_and_obfuscate(src)
    packer = Packer()
    packed = packer.pack(payload, xor_key=9)
    loader = Loader()
    stub = loader.build_loader(packed, add_dummy=False, xor_key=9)

    ns = {}
    exec(stub, ns)
    assert ns.get('y') == 123
