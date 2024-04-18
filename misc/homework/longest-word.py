def longestWord(wordList):
    length = 0
    long_word = ''

    for word in wordList:
        if len(word) > length:
            length = len(word)
            long_word = word

    return long_word

def main():
    wordList = ['Python', 'is', 'a', 'widely-used', 'high-level', 'programming', 'language']
    print(longestWord(wordList))

if __name__ == '__main__':
    main()