def removeDuplicates(aList):
    for item in aList:
        while aList.count(item) > 1:
            aList.remove(item)

def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    removeDuplicates(myList)
    print(myList)

if __name__ == '__main__':
    main()