import random

def uniqueValuesOnDiagonals(table):
    '''
    table: a list of lists where the number of rows and columns are equal
    returns: a tuple with two values:
      (1) a sorted list of unique values in the diagonal from top-left to bottom-right
      (2) a sorted list of unique values in the diagonal from top-right to bottom-left
    '''
    tl = []
    tr = []
    for i in range(len(table)):
        if table[i][i] not in tl:
            tl.append(table[i][i])
        if table[i][-i-1] not in tr:
            tr.append(table[i][-i-1])
    return (sorted(tl),sorted(tr))
            
            

def main():
    table = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
    print(uniqueValuesOnDiagonals(table))

if __name__ == '__main__':
    main()