
<h1 align="center">🕵️‍♂️ PyCrypt - Script Obfuscator</h1>
<p align="center"><em>"enkripsi Python-mu agar tidak tercopas/edit"</em></p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=440&lines=Encrypt+Python+Scripts;XOR+%2B+Marshal+%2B+Base64;Stay+Stealthy+With+beruu27" alt="Typing SVG" />
</p>

---

## 🔐 Tentang PyCrypt

**PyCrypt** adalah alat obfuscator/enkripsi source code Python berbasis CLI yang memanfaatkan kombinasi:
- `marshal` untuk mengkompilasi bytecode
- `base64` untuk encoding
- `XOR` untuk penyamaran
- Kode dummy random sebagai pengalih perhatian

Dirancang oleh `beruu27` agar script Python kamu tidak mudah di-*copas*, dibaca, atau dicolong.

---

## 🚀 Fitur Utama

- 🔁 Multi-layer `marshal` compiler
- 🔑 XOR encrypt custom key (0–255)
- 🧬 Obfuscasi variable otomatis
- 🧪 Inject dummy code acak
- 🧠 CLI interaktif gaya retro
- 📦 Output file `.py` yang tetap bisa dijalankan

---

## ⚙️ Cara Pakai

```bash
python pycrypt.py
```

Ikuti input di CLI:

```plaintext
📂 masukan file path ( example.py): contoh.py
💾 simpan sebagai ( hasil.py): hasil_awikwok.py
🔁 beraoa lapis? (default 3): 4
🔑 XOR key (0-255): 23
🛡️ Add dummy code for extra obfuscation? (y/n, default y): y
```

Hasil terenkripsi akan disimpan ke file yang kamu tentukan.

---

## 📂 Contoh Output

```python
# hawoo
# VYcQgPjZqWokTyNvKrpT
xG73Y = lambda a: ''.join([chr(i) for i in a])
mZ7pK = __import__(xG73Y([109,97,114,115,104,97,108]))
bASX8 = __import__(xG73Y([98,97,115,101,54,52]))
dO6xM = [120, 210, 38, 77, ...]
dO6xM = bytes([c ^ 23 for c in dO6xM])
exec(mZ7pK.loads(bASX8.b64decode(dO6xM)))
```

---

## 💡 Catatan Penting

- file hasil obfuscasi tetap `.py`, bisa di-*run*, tapi tidak mudah dibaca.
- jangan gunakan untuk malware/aktivitas ilegal. Hanya untuk proteksi script **legal dan pribadi**.

---

## 👨‍💻 Author

**beruu27**  
📎 GitHub: [@beruu27](https://github.com/beruu27)  
🧠 Motto: *"fortis fortuna adiuvat"*

---

## ⚠️ Disclaimer

> Tools ini dibuat untuk **edukasi dan proteksi**. Segala penyalahgunaan adalah tanggung jawab pengguna. Gunakan dengan bijak!

---

## ⭐ Support

jika kamu suka proyek ini, beri ⭐ di repo GitHub dan bantu share agar makin banyak dev bisa melindungi script-nya!
