""" set comprehension """

text = 'set comprehension is a concise way to create a new set based on existing iterable'

unique_set = set(word for word in text.split())

print(unique_set)
