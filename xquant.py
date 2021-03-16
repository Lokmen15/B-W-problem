  
"""
python script that solves the B&W sheeps problem using recursivity
usage: 
    $ python XQUANT.py  --b number of black sheeps desired   --w number of white sheeps desired

    exp:
    $ python xquant.py --b 5 --w 8

"""


import argparse

def moveForward(list,indexOfSpace, nextSpaceIndex):
    '''
    This function takes three arguments, the list to modify ,
    the index of space and the future index of space.
    '''
    list[indexOfSpace], list[nextSpaceIndex] = list[nextSpaceIndex], list[indexOfSpace] 



def canSheepMove(list, indexOfSpace, isWhiteSheep):
    '''
    check if the sheep can move, the function takes the list, the index of space
    and   isWhiteSheep is boolean so we can use it for both white and black sheeps.
    check also the index so it should not be out of range
    '''
    if (isWhiteSheep):
        return (indexOfSpace +1 < len(list) and list[indexOfSpace+1] == "W") or (indexOfSpace +2 < len(list) and list[indexOfSpace+2] == "W" )
    else:
        return (indexOfSpace -1 >=0 and list[indexOfSpace-1] == "B") or (indexOfSpace -2 >=0 and list[indexOfSpace-2]== "B")

def areSheepOfsameColor(list,indexOfSpace):
    '''
    check here if the space is between two sheeps of the same color.
    '''

    res = False
    if (indexOfSpace -1 >= 0) and (indexOfSpace+1 < len(list)):
        if(list[indexOfSpace-1]==list[indexOfSpace+1]):
            res = True
    return res
    
def isGoodMove(list,indexOfSpace,nextSpaceIndex):
    '''
    check if the resulting new position of the empty space is between 2 sheeps
    of the same color or a sheep and an edge using a copy of the list. 
    if not we move the other sheep.
    '''
    cplist=list[:]
    cplist[indexOfSpace], cplist[nextSpaceIndex] = cplist[nextSpaceIndex], cplist[indexOfSpace] 
    leftSide= rightSide='NONE'

    
    if (nextSpaceIndex -1 >=0):
        leftSide = cplist[nextSpaceIndex-1]
    else:
        return True

    if (nextSpaceIndex +1 < len(cplist)):
        rightSide = cplist[nextSpaceIndex+1]
    else:
        return True

    if (leftSide == rightSide):
        return True
    else:
        return False
    

    
def solve(list,indexOfSpace):
    print(list)
    # check the legal moves of each the black and white
    canWhiteSheepMove= canSheepMove(list,indexOfSpace,True)
    canBlackSheepMove= canSheepMove(list,indexOfSpace,False)
    
    #initializing the next index of space
    nextSpaceIndexIfBlackMoves=0
    nextSpaceIndexIfWhiteMoves=0

    if (indexOfSpace -1 >=0 and list[indexOfSpace-1] == "B"):
        nextSpaceIndexIfBlackMoves=indexOfSpace-1
    elif (indexOfSpace -2 >=0 and list[indexOfSpace-2] == "B"):
         nextSpaceIndexIfBlackMoves=indexOfSpace-2
    
    if (indexOfSpace +1 < len(list) and list[indexOfSpace+1] == "W"):
        nextSpaceIndexIfWhiteMoves=indexOfSpace+1
    elif (indexOfSpace +2 < len(list) and list[indexOfSpace+2] == "W"):
         nextSpaceIndexIfWhiteMoves=indexOfSpace+2
            
    if (not canWhiteSheepMove and not canBlackSheepMove):
        return list
    
    elif (canWhiteSheepMove and not canBlackSheepMove):
        #between black and white and only white can move
        moveForward(list,indexOfSpace,nextSpaceIndexIfWhiteMoves)
        indexOfSpace = nextSpaceIndexIfWhiteMoves
        solve(list,indexOfSpace)
        
    elif (canBlackSheepMove and not canWhiteSheepMove):
        #between black and white and only black can move
        moveForward(list,indexOfSpace,nextSpaceIndexIfBlackMoves)
        indexOfSpace = nextSpaceIndexIfBlackMoves
        solve(list,indexOfSpace)
        
    elif (canWhiteSheepMove and canBlackSheepMove):
        #same color
        if (areSheepOfsameColor(list,indexOfSpace)):
            color = list[indexOfSpace -1]
            # if the color is black we move the white
            if color=='B':
                moveForward(list,indexOfSpace,nextSpaceIndexIfWhiteMoves)
                indexOfSpace = nextSpaceIndexIfWhiteMoves
                solve(list,indexOfSpace)
            # if the color is white we move the black
            else:
                moveForward(list,indexOfSpace,nextSpaceIndexIfBlackMoves)
                indexOfSpace = nextSpaceIndexIfBlackMoves
                solve(list,indexOfSpace)
        # else if it's between two diffrent we check if it's a good move 
        # to move the balck or not so we can have the empty spaec between 
        #two sheep we the same  colors
        elif (isGoodMove(list,indexOfSpace,nextSpaceIndexIfBlackMoves)):
            moveForward(list,indexOfSpace,nextSpaceIndexIfBlackMoves)
            indexOfSpace = nextSpaceIndexIfBlackMoves
            solve(list,indexOfSpace)
        else:
            moveForward(list,indexOfSpace,nextSpaceIndexIfWhiteMoves)
            indexOfSpace = nextSpaceIndexIfWhiteMoves
            solve(list,indexOfSpace)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", help="set the number of black sheeps",type=int)
    parser.add_argument("--w", help="set the number of white sheeps",type=int)
    args = parser.parse_args()
    listOfWhite = ['W'] * args.w
    listOfBlack = ['B'] * args.b
    list=listOfBlack+['space']+listOfWhite
    indexOfSpace = list.index('space')
    solve(list,indexOfSpace)