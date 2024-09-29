import random , time , copy
width= 60
height = 20

nextcells=[]
for x in range(width):
    column=[]
    for y in range(height):
        if random.randint(0,1)==0:
            column.append('#')
        else:
            column.append(' ')
    nextcells.append(column)

while True:
    print('\n \n \n \n \n')
    currentcells= copy.deepcopy(nextcells)

    for y in range(height):
        for x in range (width):
            print(currentcells[x][y], end='')
        print()

    for x in range(width):
        for y in range(height):
            leftcord=(x-1)%width
            rightcord=(x+1)%width
            abovecord=(y-1)%height
            belowcord=(y+1)%height

            numneighbours=0
            if currentcells[leftcord][abovecord]=='#':
                numneighbours+=1
            if currentcells[x][abovecord]=='#':
                numneighbours+=1
            if currentcells[rightcord][abovecord]=='#':
                numneighbours+=1
            if currentcells[leftcord][y]=='#':
                numneighbours+=1
            if currentcells[rightcord][y]=='#':
                numneighbours+=1
            if currentcells[leftcord][belowcord]=='#':
                numneighbours+=1
            if currentcells[x][belowcord]=='#':
                numneighbours+=1
            if currentcells[rightcord][belowcord]=='#':
                numneighbours+=1

            if currentcells[x][y]=='#' and (numneighbours==2 or numneighbours==3):
                nextcells[x][y]='#'
            elif currentcells[x][y]==' ' and numneighbours==3:
                nextcells[x][y]='#'
            else:
                nextcells[x][y]=' '
    time.sleep(1)

            



    