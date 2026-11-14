"""food-picture-01 entry: a bright, glossy tonkotsu ramen photograph.

The picture is shipped beside this program as entry.jpg (a JPEG,
1024x768, 267,713 bytes -- within the 1 MiB / 1024x1024 limits).
This program copies those exact bytes to /output/entry.png.

The picture is a user-supplied photograph of tonkotsu ramen: a tall
glossy noodle pull lifted by chopsticks, a dripping soft egg yolk,
charred chashu slices, green onion and nori over a rich broth, in a
warm, bright setting. No drawing, no network, no randomness: a pure
deterministic copy, standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SOURCE = os.path.join(_HERE, "entry.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(_SOURCE, out_path)
    # Sanity check the copy: the sealed run must see exactly the
    # shipped bytes, so refuse to finish on a short or missing write.
    if os.path.getsize(out_path) != os.path.getsize(_SOURCE):
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
