import marshal
import base64
import random
import string
import hashlib
import os
from typing import Optional

def xor_encrypt(data: bytes, key: int = 13) -> bytes:
    return bytes(b ^ key for b in data)

def generate_random_key(length: int = 8) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encode_layers(code_str: str, layers: int = 3, salt: str = "") -> bytes:
    code = f"import marshal\n# Salt: {salt}\n" + code_str
    bytecode = compile(code, "<beruu27>", "exec")
    for _ in range(layers):
        bytecode = compile(
            f"import marshal\nexec(marshal.loads({repr(marshal.dumps(bytecode))}))",
            "<beruu27>", "exec"
        )
    return marshal.dumps(bytecode)

def to_int_list(bytez: bytes) -> str:
    return ','.join(str(b) for b in bytez)

def generate_dummy_code() -> str:
    dummy_lines = [
        f"# {''.join(random.choices(string.ascii_letters, k=20))}",
        f"x = {random.randint(1000, 9999)}  # decoy",
        f"if False: print('{generate_random_key(10)}')",
    ]
    return "\n".join(random.sample(dummy_lines, k=random.randint(1, len(dummy_lines))))

def camouflage_encoder(
    input_file: str,
    output_file: str,
    layers: int = 3,
    xor_key: int = 13,
    add_dummy: bool = True
) -> Optional[str]:
    try:
        if not os.path.isfile(input_file):
            return f"[!] Error: Input file '{input_file}' does not exist."
        if not input_file.endswith('.py'):
            return f"[!] Error: Input file must be a `.py` file."

        if not output_file.endswith('.py'):
            output_file += '.py'

        with open(input_file, "r", encoding="utf-8") as f:
            src = f.read()

        salt = generate_random_key(12)

        encoded = encode_layers(src, layers, salt)

        xor_payload = xor_encrypt(base64.b64encode(encoded), key=xor_key)
        payload_list = to_int_list(xor_payload)

        var_x = generate_random_key(5)
        var_m = generate_random_key(5)
        var_b = generate_random_key(5)
        var_d = generate_random_key(5)

        dummy_code = generate_dummy_code() if add_dummy else ""


        ninja_code = f"""# hawoo
{dummy_code}
{var_x} = lambda a: ''.join([chr(i) for i in a])
{var_m} = __import__({var_x}([109,97,114,115,104,97,108]))
{var_b} = __import__({var_x}([98,97,115,101,54,52]))
{var_d} = [{payload_list}]
{var_d} = bytes([c ^ {xor_key} for c in {var_d}])
exec({var_m}.loads({var_b}.b64decode({var_d})))
"""

        # Write to output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(ninja_code)

        return f"[✓] file berhasil terenkripsi ➜ {output_file} (Layers: {layers}, XOR Key: {xor_key})"

    except Exception as e:
        return f"[!] gagal enkripsi: {str(e)}"

def main():
    print("""
╭────────────────────────────────────────────────╮
│                🕵  beruu27                      │
│   enkripsi scriptmu agar tidak tercopas        │
╰────────────────────────────────────────────────╯
""")

    while True:
        src = input("📂 masukan file path ( example.py): ").strip()
        dst = input("💾 simpan sebagai ( hasil.py): ").strip()
        layer_input = input("🔁 beraoa lapis? (default 3): ").strip()
        xor_key_input = input("🔑 XOR key (0-225): ").strip()
        dummy_input = input("🛡️ Add dummy code for extra obfuscation? (y/n, default y): ").strip().lower()

        try:
            layers = int(layer_input) if layer_input else 3
            if layers < 1:
                print("[!] Error: Layers must be at least 1.")
                continue

            xor_key = int(xor_key_input) if xor_key_input else 13
            if not 0 <= xor_key <= 255:
                print("[!] Error: XOR key must be between 0 and 255.")
                continue

            add_dummy = dummy_input != 'n'

            result = camouflage_encoder(src, dst, layers, xor_key, add_dummy)
            print(result)

            again = input("\n[?] enkripsi file lain? (y/n): ").strip().lower()
            if again != 'y':
                print("👋 Exiting beruu27. stay stealthy!")
                break

        except ValueError:
            print("[!] Error: Invalid input for layers or XOR key. Please enter numbers.")
        except Exception as e:
            print(f"[!] Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
