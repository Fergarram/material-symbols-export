MATERIAL SYMBOLS EXPORT, one ima tsx component per icon

WHAT THIS IS
	Reads the Material Symbols variable fonts and writes each requested
	icon as its own .tsx module, so an app imports only what it uses.
	The outline is taken from the font at the given axis values (FILL,
	wght, GRAD, opsz), flipped into the same 0 -960 960 960 viewBox as
	Google's svg downloads. One <path>, fill currentColor, sized by
	--icon-size like the <icon> element (icon-N utilities work).

FILES
	fetch-source.py     downloads the pinned Outlined, Rounded and Sharp
	                    variable fonts, codepoints files and license
	build.py            writes <out>/<style>/<name>.tsx, out defaults
	                    to dist/

BUILD
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python fetch-source.py
	.venv/bin/python build.py home search settings
	.venv/bin/python build.py --fill home        writes outlined/home-filled.tsx
	.venv/bin/python build.py --style rounded --wght 300 favorite
	.venv/bin/python build.py --all

	Into a site, any folder:
	.venv/bin/python build.py --style sharp --all --out <dir>
	.venv/bin/python build.py --style sharp --all --fill --out <dir>
	writes <dir>/sharp/<name>.tsx and <name>-filled.tsx

	--format svg writes plain <name>.svg files instead, one path in the
	same viewBox, for use as <img>, css mask or background:
	.venv/bin/python build.py --style sharp --all --format svg --out <dir>

USE
	Names are the codepoints file names. Files are kebab-case, components
	are Icon + PascalCase (Icon prefix keeps 10k and 3d_rotation valid),
	--fill adds a -filled / Filled suffix (home-filled.tsx, IconHomeFilled).
	Names like home_filled are aliases of the base glyph in the font, so
	they are skipped and their file name goes to the real filled icon.

	```html
	<script type="blob-module" name="material-symbols/outlined/home" lang="tsx" remote="/path/to/outlined/home.tsx"></script>
	```

	```tsx
	import { IconHome } from "material-symbols/outlined/home";

	<span class="icon-24 text-blue-500"><IconHome title="Home" /></span>
	```

	Without title the svg is aria-hidden, with it role="img".

SOURCE
	google/material-design-icons, commit 10ecc147 (same as matemoji),
	variablefont/MaterialSymbols{Outlined,Rounded,Sharp}[FILL,GRAD,opsz,wght].ttf
	Apache 2.0.
