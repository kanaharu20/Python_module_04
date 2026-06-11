#!/usr/bin/env python3


def secure_archive(
        file_name: str, option: str, content: str
        ) -> tuple[bool, str]:
    try:
        if option == "read":
            with open(file_name, "r") as file:
                print("Using 'secure_archive' to read from a regular file:")
                content_read: str = file.read()
                return (True, f'{content_read}')
        elif option == "write":
            with open(file_name, "w") as file:
                print(
                    "Using 'secure_archive' to write previous "
                    "content to a new file:"
                )
                file.write(content)
                return (True, 'Content successfully written to file')
    except (FileNotFoundError, PermissionError) as e:
        print("Using 'secure_archive' to read from a nonexistent file:")
        return (False, f"{e}")
    return (False, "Invalid option")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print(f"{secure_archive('/etc/master.passwd', 'read', '')}\n")

    print(f'{secure_archive("foo", "read", "")}\n')

    print(f'{secure_archive("ancient_fragment.txt", "read", "")}\n')

    print(f'{secure_archive("ancient_fragment.txt", "write", "Hello world")}')
