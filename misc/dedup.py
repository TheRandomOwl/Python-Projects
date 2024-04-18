def removeDuplicates(aList):
    uniqueList = []
    for item in aList:
        if item not in uniqueList:
            uniqueList.append(item)
    aList.clear()
    aList.extend(uniqueList)


def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    removeDuplicates(myList)
    print(myList)

if __name__ == '__main__':
    main()