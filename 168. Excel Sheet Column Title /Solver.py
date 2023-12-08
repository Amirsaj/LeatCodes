






def convertToTitle(columnNumber: int):
    ColumnAlphabet = ''

    while columnNumber > 0 :
        adad = columnNumber % 26
        print('in',adad)
        if adad == 0 :
            adad = 26
        ColumnAlphabet = ColumnAlphabet + chr(64+adad)
        columnNumber = columnNumber - adad
        columnNumber = columnNumber // 26
        print('dovom',columnNumber,ColumnAlphabet)

    print(ColumnAlphabet[::-1])
convertToTitle(701)