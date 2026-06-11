#!/usr/bin/env python3

import sys


def main() -> None:
    args: list[str] = sys.argv

    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{args[1]}'")

    f = None
    try:
        f = open(args[1], "r")
        content: str = f.read()
        print("---\n\n\n")
        print(f"{content}")
        print("---")
    except Exception as e:
        print(f"Error opening file '{args[1]}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"File '{args[1]}' closed.")


if __name__ == "__main__":
    main()
