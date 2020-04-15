class panel(object):
    def __init__(self):
        self.x = self.y= 0
        self.rgb = ""
        selfstate= False
        
    def setPos(x,y):
        self.x=x
        self.y=y

    def toString():
        return str(x)+","+str(y)


grid = input("Enter Grid Width and Height(Integer)(Use the comma): w,h")
grid_data = grid.split(",")
width=int(grid_data[0])
height=int(grid_data[1])

##now to create a algorithm to fill an array/other datastruct. w/ a full grid

##first of all can you just print the co-ordinates of the full grid out
i = j =0
while(i < height):
    
    stree=": "
    while( j < width):
        stree = stree+ str(i) + ","+ str(j) +" : "
        j = j+1
    print(stree)
    i = i+1
    j=0

##important question do you start with your origin on the top or the bottom
#bottoms better
print("----------------")
i = height
j = 0
while(i >= 0):
    stree=": "
    while( j < width):
        stree = stree+ str(i) + ","+ str(j) +" : "
        j = j+1
    print(stree)
    i = i -1
    j=0





"""
color red
|0| | |0|
|0| | |0|
|0|0|0|0|
|0| | |0|
|0| | |0|

=== drawing shit output blocks in pygame tkinter
"""
