infile = open('book of John text.txt', 'r')
text = infile.readline()

words = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man', 'spirit']

word_dict = {}

for word in text.split():
    if word in words:
        word_dict[word] = text.split().count(word)

for word in word_dict:
    print(f'{word}: {word_dict[word]}')