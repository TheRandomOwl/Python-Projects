def removeDuplicates(aList):
    '''
    Function to remove duplicates from a list
    aList: a list
    returns: None (aList should be modified in place)
    '''
    new =  list(set(aList))
    aList.clear()
    aList.extend(new)

def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    removeDuplicates(myList)
    print(myList)

if __name__ == '__main__':
    main()