from pathlib import Path


cwd = Path.cwd()
print(f"Current Working Directory: {cwd}")


home = Path.home()
print(f"Home Directory: {home}")


# creating a new file
# Path.touch(Path.cwd() / "new_file.txt")


# Writing to file
file = Path.cwd() / "new_file.txt"
print("Writing to file...")
file.write_text("Hello World!\n Hi Manisha!\n I love Python!")
print(file.read_text())


# removing file
Path.touch(Path.cwd() / "demo.txt")
file = Path.cwd() / "demo.txt"
print(f"Deleting file: {file}")
file.unlink()
