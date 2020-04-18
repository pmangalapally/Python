def PrintTable(tabData):

    colWidth = []
    counter = 0
    if len(tableData) > 0:
        for row in tabData:
            #print(row)
            if len(row) > 0:
                innerTab = row
                #print(innerTab)
                innerCounter = 0
                for innerrow in innerTab:
                    columnWidth = len(innerrow)
                    #print(columnWidth)
                    #print(innerrow)
                    
                    if len(colWidth) > innerCounter:
                        if columnWidth > colWidth[innerCounter]:
                            colWidth[innerCounter] = columnWidth
                    else:
                        colWidth.append(columnWidth)
                    
                    innerCounter = innerCounter + 1
                
            counter = counter + 1


    print(colWidth)

    for rowlist in tabData:
        printCounter = 0
        ToBePrinted = ''
        for printrow in rowlist:
            ToBePrinted = ToBePrinted + printrow.rjust((colWidth[printCounter]+4), ' ')
            printCounter = printCounter + 1
        
        print (ToBePrinted)

    

        


 
                        
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['apples2', 'oranges2', 'cherries2', 'banana2']]


PrintTable(tableData)