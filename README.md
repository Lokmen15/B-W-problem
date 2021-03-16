# Solving the B&W sheeps problem

The goal of this code is to move all the black sheeps to the right and all the white sheeps to the left knowing that :
- A sheep must move to an empty space, or jump over another sheep and land on an empty space
- A sheep can't jump over more than one sheep
- A sheep always faces the same direction and can't move backward or jump backward

Let's represent the white and black sheeps in a list like the following example,
['B', 'B', 'B', 'B', 'B', 'space', 'W', 'W', 'W', 'W', 'W']


##### The approach is the following:

- If no white sheep can move we move a black sheep.

- If no black sheep can move we move a white sheep.

While moving a sheep, we check if it can move by one space first, if not we move it by 2 spaces (jump)
- If both black and white sheeps can move we check : 

-If the empty space is between two sheeps of the same color, we jump with the sheep with the opposite color to the desired direction.

-If the empty space is between two sheeps with different colors, we pick a random sheep to move and check if the resulting new position of the empty space is between 2 sheeps of the same color or a sheep and an edge. if not we move the other sheep.




system info:

- ubuntu 18.04

- python 3.6.9





## usage


```bash
$ python XQUANT.py  --b number of black sheeps desired   --w number of white sheeps desired
```