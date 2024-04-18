def smallWords(text, length):
    temp = []
    for word in text.split():
        if len(word) <= length and word not in temp:
            temp.append(word)
    temp.sort()
    return temp

def main():
    text = '''We hold these truths to be self-evident, 
that all men are created equal, that they are endowed by their Creator 
with certain unalienable Rights, that among these are Life, Liberty 
and the pursuit of Happiness.'''
    print(smallWords(text, 5))

if __name__ == '__main__':
    main()