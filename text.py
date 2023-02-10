import random

with open('words.txt', 'r') as wordfile:
    texts = wordfile.readlines()
    textsnew = [text.replace('\n', '') for text in texts]
    

print(random.choice(textsnew))
