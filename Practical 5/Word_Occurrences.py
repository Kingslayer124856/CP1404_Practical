

def main():
    odd_words = {}
    text = input("Text: ")
    words = text.split()
    for word in words:
        frequency = odd_words.get(word, 0)
        odd_words[word] = frequency + 1
    words = list(odd_words.keys())
    words.sort()
    max_length = max((len(word) for wor in words))
    for word in words:
        print("{:{}}".format(word, max_length, odd_words[word]))
main()