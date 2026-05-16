# PassGen

**PassGen** is a minimal command‑line utility written in Python that produces strong random passwords.

### Features
- Choose password length (default 16).
- Include/exclude lowercase, uppercase, digits, and symbols.
- Input validation with clear error messages.
- No external dependencies – uses only the Python standard library.

### Installation
```bash
# Clone the repository (or copy the single file)
git clone https://github.com/your-username/PassGen.git
cd PassGen
```

The script works with Python 3.7+. No installation step is required; just run it.

### Usage
```bash
python3 passgen.py [options]
```
#### Options
| Flag | Description |
|------|-------------|
| `-l`, `--length` | Desired password length (integer ≥ 4). Default: 16 |
| `-c`, `--charset` | Characters to include, as a combination of `l` (lowercase), `u` (uppercase), `d` (digits), `s` (symbols). Example: `-c lud` includes lowercase, uppercase, digits. Default: `luds` |
| `-h`, `--help` | Show help message and exit |

#### Examples
```bash
# Generate a 24‑character password with all character groups
python3 passgen.py -l 24

# Generate a 12‑character password with only letters and digits
python3 passgen.py -l 12 -c ld
```

### Contributing
Feel free to open issues or submit pull requests. Keep the script tiny and dependency‑free.

### License
MIT – see the LICENSE file in the repository.
