# ULPaints
Python learning and discovery journal, whilst producing a semi-useful software.

## Objective 
As you can see from the image below this is what a project to use a new different style of media sharing would look like. You could play games like tetris, you could use block text to write messives or create pixel art movies and stream them to the wall.

In the finished project there would be light panels behind each section of the windows and they could be controlled remotely to turn on and off and display colours on demand.

Eventually my thought process turned to how are you going to have someones idea for a image or movie and convert that into what you see on the wall. I always liked the idea of Paint, MSPaint had my attention for a lot of my childhood. So I wanted to create something like Paint but for drawing block art that could be used for the project of controlling a wall of light. 

<img src="objective.jpg" alt="UL light up project" width="450" height="625"/>

## First thing I did
I wanted to create a grid that had the grid co-ordinates of each light panel for the full UL lighting up a wall face project.
To do this I created a program that accepted two inputs from the terminal, width,height and it prints out the co-ordinates starting from 0,0 up to whatever. It does it in two ways having the origin in the top left and the traditional origin starting point at bottom left.

The file is [Link to the code, coords-cli.py](coords_cli.py)

~~~~
> Enter Grid Width and Height(Integer)(Use the comma): w,h 3,5
: 0,0 : 0,1 : 0,2 : 
: 1,0 : 1,1 : 1,2 : 
: 2,0 : 2,1 : 2,2 : 
: 3,0 : 3,1 : 3,2 : 
: 4,0 : 4,1 : 4,2 : 
----------------
: 5,0 : 5,1 : 5,2 : 
: 4,0 : 4,1 : 4,2 : 
: 3,0 : 3,1 : 3,2 : 
: 2,0 : 2,1 : 2,2 : 
: 1,0 : 1,1 : 1,2 : 
: 0,0 : 0,1 : 0,2 : 
~~~~

 
