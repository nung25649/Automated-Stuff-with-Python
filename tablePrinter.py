def printTable(table):
    shift = [0] * len(tableData)
    for i in range(len(table)):
        max = 0
        for j in range(len(table[i])):
            if len(table[i][j]) > max:
                max = len(table[i][j])
        shift[i] = max
    
    for i in range(len(table[0])):
        for j in range(len(table)):
            text = table[j][i].rjust(shift[j]) + ' '
            print(text, end = '')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)