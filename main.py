import os

LINE = "My resume says \"detail-oriented.\" Page two says \"detail-orientated.\" I stand by it."

# One-liner entries must be a single line: reject any newline/CR so a
# stray line break can never sneak into entry.txt and break the format.
assert "\n" not in LINE and "\r" not in LINE, "LINE must not contain a newline"

try:
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
except OSError:
    os.makedirs("./output", exist_ok=True)
    out_path = "./output/entry.txt"

with open(out_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open(out_path, "rb") as f:
    content = f.read()
assert content == LINE.encode("utf-8"), "entry.txt does not match LINE byte-for-byte"

print(f"OK: wrote {len(LINE)} characters ({len(content)} bytes) to {out_path}; verified entry.txt matches LINE byte-for-byte")
