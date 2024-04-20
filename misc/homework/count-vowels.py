def countVowels(inString):
    '''
    Function to count the number of vowels in a string.
    inString: a string
    returns: the number of vowels in inString
    Vowels are the following letters: a, e, i, o, u (but not y)
    The count should be case-insensitive (e.g., 'A' and 'a' both count as an 'a')
    '''
    s = inString.lower()
    vowels = 'aeiou'
    count = 0
    for letter in vowels:
        count += s.count(letter)
    return count

def main():
    string = '''I must not fear. Fear is the mind-killer. 
Fear is the little-death that brings total obliteration. 
I will face my fear. I will permit it to pass over me and through me. 
And when it has gone past, I will turn the inner eye to see its path. 
Where the fear has gone there will be nothing. Only I will remain.'''

    print(countVowels(string))

if __name__ == '__main__':
    main()