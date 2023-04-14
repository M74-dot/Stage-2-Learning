import pytest
import assignment1
from pathlib import Path


def test_writeToFile():
    file = open("new_file.txt",'r')
    # expected = "Hello World!\n Hi Manisha!\n I love Python!"
    # assert expected==file.read()
    assert file.read() == "Hello World!\n Hi Manisha!\n I love Python!"


def test_readFromFile():
    file = open("new_file.txt",'r')
    assert file.read() == "Hello World!\n Hi Manisha!\n I love Python!"
   