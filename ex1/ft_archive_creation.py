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
        return
    finally:
        if f is not None:
            f.close()
            print(f"File '{args[1]}' closed.")

    print("Transform data:\n---\n\n")

    f = None
    f_w = None
    new_content: str = ""
    try:
        f = open(args[1], "r")
        for line in f:
            if line != "\n":
                new_content += line.replace("\n", "") + "#\n"
            else:
                new_content += line
        print(f"{new_content}")
        print("---")
        file_to_save: str = input("Enter new file name (or empty): ")
        if file_to_save == "":
            print("Not saving data")
        else:
            print(f"Saving data to '{file_to_save}'")
            f_w = open(file_to_save, "w")
            f_w.write(new_content)
    except Exception as e:
        print(f"Error opening file '{args[1]}': {e}")
    finally:
        if f is not None:
            f.close()
        if f_w is not None:
            f_w.close()


if __name__ == "__main__":
    main()
