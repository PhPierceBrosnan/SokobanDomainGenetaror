
#input map
sokobanMap = open("sokobanLevel.txt", "r").read()
mapLines = sokobanMap.split("\n")
maxLength = len(mapLines)

for x in mapLines:
    if len(x) > maxLength:
        maxLength = len(x)

lenSquared = maxLength * maxLength


#defining goal state
goalState = ""

invalidTiles = list()

for i in range(0, maxLength):
    for j in range(0, maxLength):
        if i < len(mapLines):
            if j < len(mapLines[i]):
                if (mapLines[i][j] == "."):
                    goalState += "R "
                elif (mapLines[i][j] == "+"):
                    goalState += "R "
                elif (mapLines[i][j] == "*"):
                    goalState += "R "
                elif (mapLines[i][j] == "#"):
                    goalState += "- "
                    invalidTiles.append((i,j))
                else:
                    goalState += "- "
            else:
                goalState += "- "
                invalidTiles.append((i,j))
        else:
            goalState += "- "
            invalidTiles.append((i,j))



#output domain rules

output = open("outputDomain.psvn", "w")

transitions = list()


output.write("DOMAIN tile 4\n	P R W N\n\n"+str(lenSquared)+"\n\n")

for x in range(0, lenSquared):
    output.write("tile ")

output.write("\n\n")


""" 

P - Player
R - Rock
W - Wall
N - Nothing

"""

#pushing rock right transitions
for x in range(0, maxLength):
    for y in range(0, maxLength-2):

        if(not((x,y) in invalidTiles) and not((x,y+1) in invalidTiles) and not((x,y+2) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "P R N "
                    i += 3

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N P R "
                    i += 3

            transitionString += " LABEL ROCKRIGHT COST 1"

            transitions.append(transitionString)


#pushing rock left transitions
for x in range(0, maxLength):
    for y in range(0, maxLength-2):

        if(not((x,y) in invalidTiles) and not((x,y+1) in invalidTiles) and not((x,y+2) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N R P "
                    i += 3

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "R P N "
                    i += 3

            transitionString += " LABEL ROCKLEFT COST 1"

            transitions.append(transitionString)



#pushing rock up transitions
for x in range(0, maxLength-2):
    for y in range(0, maxLength):

        if(not((x,y) in invalidTiles) and not((x+1,y) in invalidTiles) and not((x+2,y) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            #lenSquared = map biggest line/column length squared
            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "R "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "P "
                    i += 2 * (maxLength-1) + 3

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "R "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "P "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "N "
                    i += 2 * (maxLength-1) + 3

            transitionString += " LABEL ROCKUP COST 1"

            transitions.append(transitionString)
      


#pushing rock down transitions
for x in range(0, maxLength-2):
    for y in range(0, maxLength):
        if(not((x,y) in invalidTiles) and not((x+1,y) in invalidTiles) and not((x+2,y) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            #lenSquared = map biggest line/column length squared
            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "P "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "R "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "N "
                    i += 2 * (maxLength-1) + 3

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "P "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "R "
                    i += 2 * (maxLength-1) + 3

            transitionString += " LABEL ROCKDOWN COST 1"

            transitions.append(transitionString)



#player only movement



#moving right transitions
for x in range(0, maxLength):
    for y in range(0, maxLength-1):
        if(not((x,y) in invalidTiles) and not((x,y+1) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "P N "
                    i += 2

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N P "
                    i += 2

            transitionString += " LABEL MOVERIGHT COST 0"

            transitions.append(transitionString)


#moving left transitions
for x in range(0, maxLength):
    for y in range(0, maxLength-1):
        if(not((x,y) in invalidTiles) and not((x,y+1) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N P "
                    i += 2

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "P N "
                    i += 2

            transitionString += " LABEL MOVELEFT COST 0"

            transitions.append(transitionString)



#moving up transitions
for x in range(0, maxLength-1):
    for y in range(0, maxLength):
        if(not((x,y) in invalidTiles) and not((x+1,y) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            #lenSquared = map biggest line/column length squared
            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "P "
                    i +=  (maxLength-1) + 2

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "P "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "N "
                    i += (maxLength-1) + 2

            transitionString += " LABEL MOVEUP COST 0"

            transitions.append(transitionString)
      


#moving down transitions
for x in range(0, maxLength-1):
    for y in range(0, maxLength):
        if(not((x,y) in invalidTiles) and not((x+1,y) in invalidTiles)):
            index = x * maxLength + y
            transitionString = ""

            i = 0

            #lenSquared = map biggest line/column length squared
            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "P "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "N "
        
                    i += (maxLength-1) + 2

            transitionString += "=> "
            i = 0

            while(i < lenSquared):
                if(not(i == index)):
                    transitionString += "- "
                    i += 1

                else:
                    transitionString += "N "
                    for z in range(0, maxLength-1):
                        transitionString += "- "
                    transitionString += "P "

                    i += (maxLength-1) + 2

            transitionString += " LABEL MOVEDOWN COST 0"

            transitions.append(transitionString)






for x in transitions:
    output.write(x+"\n")


output.write("\n\nGOAL "+goalState)

