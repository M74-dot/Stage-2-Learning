""" list comprehension to get files with .txt extension """
import os


# get path using pwd command
dir_path = "/home/manisha/Stage2Learning"

files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

print(files)
