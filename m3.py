from urllib.request import urlopen

url = "http://www.gutenberg.org/files/100/100-0.txt"
book = urlopen(url)
word_list = []

for line in book:
    words = line.decode("utf8").split()

    for word in words:
        word_list.append(word)

print(f"Ingested {len(word_list)} words.")

book.close()
