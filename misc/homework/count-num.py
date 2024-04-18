def countDigits(inString):
    count = 0
    for char in inString:
        if char.isdigit():
            count += 1
    return count

def main():
    string = '''The year 1776 is the year of the United States of America's independence.
The Declaration of Independence was adopted on July 4, 1776.'''

    print(countDigits(string))

if __name__ == '__main__':
    main()