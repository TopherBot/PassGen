#!/usr/bin/env python3
"""PassGen – Tiny secure password generator.

Author: TopherBot (topherbot@proton.me)
License: MIT
"""

import argparse
import secrets
import string
import sys

# ------------------------------------------------------------
# Helper: Build character pool based on user‑specified flags
# ------------------------------------------------------------
def build_charset(selection: str) -> str:
    """Return a string containing the characters to use.

    Parameters
    ----------
    selection: str
        Combination of letters: 'l' (lowercase), 'u' (uppercase),
        'd' (digits), 's' (symbols).
    """
    charset = []
    if 'l' in selection:
        charset.append(string.ascii_lowercase)
    if 'u' in selection:
        charset.append(string.ascii_uppercase)
    if 'd' in selection:
        charset.append(string.digits)
    if 's' in selection:
        charset.append(string.punctuation)

    if not charset:
        raise ValueError(
            "Character set selection is empty. Include at least one of 'l', 'u', 'd', 's'."
        )
    return "".join(charset)

# ------------------------------------------------------------
# Core: Generate password
# ------------------------------------------------------------
def generate_password(length: int, charset: str) -> str:
    """Generate a random password of *length* using *charset*.

    Uses `secrets.choice` for cryptographic randomness.
    """
    return "".join(secrets.choice(charset) for _ in range(length))

# ------------------------------------------------------------
# CLI argument parsing with proactive checks
# ------------------------------------------------------------
def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="passgen",
        description="Generate a secure random password.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="Length of the password (minimum 4).",
    )
    parser.add_argument(
        "-c",
        "--charset",
        type=str,
        default="luds",
        help="Characters to include: l=lowercase, u=uppercase, d=digits, s=symbols.",
    )
    args = parser.parse_args(argv)

    # Proactive validation
    if args.length < 4:
        parser.error("Password length must be at least 4 characters.")
    try:
        # Normalise charset string to lower case and remove duplicates
        args.charset = "".join(sorted(set(args.charset.lower())))
        _ = build_charset(args.charset)  # Will raise if empty/invalid
    except ValueError as exc:
        parser.error(str(exc))

    return args

# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------
def main() -> int:
    args = parse_args()
    charset = build_charset(args.charset)
    password = generate_password(args.length, charset)
    print(password)
    return 0

if __name__ == "__main__":
    sys.exit(main())
