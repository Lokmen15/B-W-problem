  
"""
python script that solves the B&W sheeps problem.
usage: 
    $ python XQUANT.py  --b number of black sheeps desired   --w number of white sheeps desired
"""


import argparse


def canSheepMove(list, indexOfSpace, isWhiteSheep):
    if (isWhiteSheep):
        return (indexOfSpace +1 < len(list) and list[indexOfSpace+1] == "W") or (indexOfSpace +2 < len(list) and list[indexOfSpace+2] == "W" )
    else:
        return (indexOfSpace -1 >=0 and list[indexOfSpace-1] == "B") or (indexOfSpace -2 >=0 and list[indexOfSpace-2]== "B")

def areSheepOfsameColor(list,indexOfSpace):
    res = False
    if (indexOfSpace -1 >= 0) and (indexOfSpace+1 < len(list)):
        if(list[indexOfSpace-1]==list[indexOfSpace+1]):
            res = True
    return res
    
def isGoodMove(list,indexOfSpace,nextSpaceIndex):
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
    
def moveForward(list,indexOfSpace, nextSpaceIndex):
    list[indexOfSpace], list[nextSpaceIndex] = list[nextSpaceIndex], list[indexOfSpace] 
    
def cal(list,indexOfSpace):
    print(list)
    canWhiteSheepMove= canSheepMove(list,indexOfSpace,True)
    canBlackSheepMove= canSheepMove(list,indexOfSpace,False)
    

    nextSpaceIndexIfBlackMoves=0
    nextSpaceIndexIfWhiteMoves=len(list)-1

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
        cal(list,indexOfSpace)
        
    elif (canBlackSheepMove and not canWhiteSheepMove):
        #between black and white and only black can move
        moveForward(list,indexOfSpace,nextSpaceIndexIfBlackMoves)
        indexOfSpace = nextSpaceIndexIfBlackMoves
        cal(list,indexOfSpace)
        
    elif (canWhiteSheepMove and canBlackSheepMove):
        #same color
        if (areSheepOfsameColor(list,indexOfSpace)):
            color = list[indexOfSpace -1]
            if color=='B':
                moveForward(list,indexOfSpace,nextSpaceIndexIfWhiteMoves)
                indexOfSpace = nextSpaceIndexIfWhiteMoves
                cal(list,indexOfSpace)
            else:
                moveForward(list,indexOfSpace,nextSpaceIndexIfBlackMoves)
                indexOfSpace = nextSpaceIndexIfBlackMoves
                cal(list,indexOfSpace)
        elif (isGoodMove(list,indexOfSpace,nextSpaceIndexIfBlackMoves)):
            moveForward(list,indexOfSpace,nextSpaceIndexIfBlackMoves)
            indexOfSpace = nextSpaceIndexIfBlackMoves
            cal(list,indexOfSpace)
        else:
            moveForward(list,indexOfSpace,nextSpaceIndexIfWhiteMoves)
            indexOfSpace = nextSpaceIndexIfWhiteMoves
            cal(list,indexOfSpace)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", help="set the number of black sheeps",type=int)
    parser.add_argument("--w", help="set the number of white sheeps",type=int)
    args = parser.parse_args()
    listOfWhite = ['W'] * args.w
    listOfBlack = ['B'] * args.b
    list=listOfBlack+['space']+listOfWhite
    indexOfSpace = list.index('space')
    cal(list,indexOfSpace)