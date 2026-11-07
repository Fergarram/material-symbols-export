#!/usr/bin/env python3
# Downloads the pinned Material Symbols variable fonts (Outlined, Rounded,
# Sharp), their codepoints files and the Apache 2.0 license into source/.
#
# usage: fetch-source.py

import os
import urllib.parse
import urllib.request

#
# Constants
#

ROOT = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(ROOT, "source")

# same commit as matemoji
COMMIT = "10ecc14790612ca8fd164e3f4ffe9c16fc50d5b7"
BASE_URL = f"https://github.com/google/material-design-icons/raw/{COMMIT}"
STYLES = ["Outlined", "Rounded", "Sharp"]

FILES = [("LICENSE", "LICENSE.txt")]
for style in STYLES:
    stem = f"MaterialSymbols{style}[FILL,GRAD,opsz,wght]"
    FILES.append((f"variablefont/{stem}.ttf", f"MaterialSymbols{style}.ttf"))
    FILES.append((f"variablefont/{stem}.codepoints", f"MaterialSymbols{style}.codepoints"))

#
# Functions
#

def main():
    os.makedirs(SOURCE_DIR, exist_ok=True)
    for remote, name in FILES:
        path = os.path.join(SOURCE_DIR, name)
        if os.path.exists(path):
            print(f"have {name}")
            continue
        url = f"{BASE_URL}/{urllib.parse.quote(remote)}"
        print(f"get  {url}")
        urllib.request.urlretrieve(url, path)


#
# Code execution
#

if __name__ == "__main__":
    main()
