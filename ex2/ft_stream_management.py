#!/usr/bin/env python3

import sys


def main() -> None:
    args: list[str] = sys.argv

    if len(args) != 2:
        sys.stdout.write("Usage: ft_stream_management.py <file>\n")
        return

    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{args[1]}'\n")

    f = None
    try:
        f = open(args[1], "r")
        content: str = f.read()
        sys.stdout.write("---\n\n\n\n")
        sys.stdout.write(f"{content}\n")
        sys.stdout.write("---\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{args[1]}': {e}\n")
        return
    finally:
        if f is not None:
            f.close()
            sys.stdout.write(f"File '{args[1]}' closed.\n")

    sys.stdout.write("Transform data:\n---\n\n\n")

    f = None
    f_w = None
    new_content: str = ""
    file_to_save: str = ""
    try:
        f = open(args[1], "r")
        while True:
            line = f.readline()
            if not line:
                break
            if line != "\n":
                new_content += line.replace("\n", "") + "#\n"
            else:
                new_content += line
        sys.stdout.write(f"{new_content}\n")
        sys.stdout.write("---\n")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        file_to_save = sys.stdin.readline().strip()
        if file_to_save == "":
            sys.stdout.write("Not saving data.\n")
        else:
            sys.stdout.write(f"Saving data to '{file_to_save}'\n")
            f_w = open(file_to_save, "w")
            f_w.write(new_content)
            sys.stdout.write(f"Data saved in file '{file_to_save}'.\n")
    except Exception as e:
        error_file = file_to_save if file_to_save else args[1]
        sys.stderr.write(f"[STDERR] Error opening file '{error_file}': {e}\n")
        sys.stdout.write("Data not saved.\n")
    finally:
        if f is not None:
            f.close()
        if f_w is not None:
            f_w.close()


if __name__ == "__main__":
    main()
