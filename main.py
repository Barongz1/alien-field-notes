"""Alien Field Notes — entry for make.fun.

Writes one line to /output/entry.txt.
The line is an alien tourist's review of Earth, at most 200 characters.
"""
import os

LINE = "Earth: great views, terrible traffic, and the locals keep asking me for directions while standing on the wrong side of the road."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
