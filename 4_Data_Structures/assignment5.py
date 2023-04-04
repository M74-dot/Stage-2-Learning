""" dict comprehension to get len of each word in list """

word_list = ["Tom Holland", "Tom Cruise", "Ian Somerholder", "Paul Wisely"]

word_dict = {word : len(word) for word in word_list}

print(word_dict)
