def IsPositionValid(**kwargs):

    Positions = {'1a' : 'black', '1b' : 'white', '1c' : 'black', '1d' : 'white', '1e' : 'black', '1f' : 'white', '1g' : 'black', '1h' : 'white',
                '2a' : 'white', '2b' : 'black', '2c' : 'white', '2d' : 'black', '2e' : 'white', '2f' : 'black', '2g' : 'white', '2h' : 'black',
                '3a' : 'black', '3b' : 'white', '3c' : 'black', '3d' : 'white', '3e' : 'black', '3f' : 'white', '3g' : 'black', '3h' : 'white',
                '4a' : 'white', '4b' : 'black', '4c' : 'white', '4d' : 'black', '4e' : 'white', '4f' : 'black', '4g' : 'white', '4h' : 'black',
                '5a' : 'black', '5b' : 'white', '5c' : 'black', '5d' : 'white', '5e' : 'black', '5f' : 'white', '5g' : 'black', '5h' : 'white',
                '6a' : 'white', '6b' : 'black', '6c' : 'white', '6d' : 'black', '6e' : 'white', '6f' : 'black', '6g' : 'white', '6h' : 'black',
                '7a' : 'black', '7b' : 'white', '7c' : 'black', '7d' : 'white', '7e' : 'black', '7f' : 'white', '7g' : 'black', '7h' : 'white',
                '8a' : 'white', '8b' : 'black', '8c' : 'white', '8d' : 'black', '8e' : 'white', '8f' : 'black', '8g' : 'white', '8h' : 'black'
                }
    
    PlayerElements= {'bpawms' : 8, 'bking' : 1, 'bqueen' : 1, 'bbishop' : 2, 'bknight' : 2 , 'brook' : 2,
                    'wpawms' : 8, 'wking' : 1, 'wqueen' : 1, 'wbishop' : 2, 'wknight' : 2 , 'wrook' : 2}

    Counter= {'bpawms' : 0, 'bking' : 0, 'bqueen' : 0, 'bbishop' : 0, 'bknight' : 0 , 'brook' : 0,
                    'wpawms' : 0, 'wking' : 0, 'wqueen' : 0, 'wbishop' : 0, 'wknight' : 0 , 'wrook' : 0}

    print(kwargs.items())
    for pos , element in kwargs.items():
        #print(pos, element)
        if pos not in Positions.keys() or element not in PlayerElements.keys():
            return False
        else:
            Counter[element] = Counter[element] + 1
    
    #print("I am here")
    for c, e in PlayerElements.items():
        if e < Counter[c]:
            return False
    
    return True

#print("Test 1")
print(IsPositionValid(**{'9b' :'bking', '1a' : 'wking'}))
#print("Test 2")
