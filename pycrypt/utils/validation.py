"""Input validation helpers."""
import os


def validate_input_path(path: str):
    if not os.path.isfile(path):
        raise SystemExit(f"[!] Error: Input file '{path}' does not exist.")
    if not path.endswith('.py'):
        raise SystemExit("[!] Error: Input file must be a `.py` file.")


def validate_layers(layers: int):
    if layers < 1:
        raise SystemExit("[!] Error: Layers must be at least 1.")


def validate_xor_key(key: int):
    if not 0 <= key <= 255:
        raise SystemExit("[!] Error: XOR key must be between 0 and 255.")
