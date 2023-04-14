from pathlib import Path


cwd = Path.cwd()
print(f"Current Working Directory: {cwd}")


home = Path.home()
print(f"Home Directory: {home}")


# creating a new file
# Path.touch(Path.cwd() / "new_file.txt")


# Writing to file
def write_to_file():
    file = Path.cwd() / "new_file.txt"
    print(f"Writing to file: {file.name}")
    file.write_text("Hello World!\n Hi Manisha!\n I love Python!")


write_to_file()


def read_from_file():
    file = Path.cwd() / "new_file.txt"
    print(f"Reading from file: {file.name}")
    print(file.read_text())


read_from_file()


# removing file
Path.touch(Path.cwd() / "demo.txt")
file = Path.cwd() / "demo.txt"

# Getting file extension with .
print(f"Extension of file: {file.suffix}")

# Getting file extension without .
print(f"Extension of file: {file.suffix[1:]}")


print(f"Deleting file: {file}")
file.unlink()
