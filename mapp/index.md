<link rel="stylesheet" type="text/css" media="all" href="style.css" />

# Game
by Jevil

![game](vid.gif)
## Introduction

Players have to constantly shuttle in nine rooms, looking for enemies that appear and killing them to get points.

---

## Implementation Details


This model is made in pycat and python.
I import ``Color``, ``KeyCode``, ``Sprite``, ``Window``, ``Scheduler``,and``Label`` from pycat.
Also import randint from random, the tricks I used include inheritance, iteration, lists, conditionals, variables, functions, etc.

The hardest part is how to make the change of the wall and the logical operation of entering room B from a specific direction in room A. In fact, the entire maze is just repeated presentation of the same nine large squares in different way.

This is the judgmental formula for entering the next room.

    ``` Python
    def nextroom(room , dir):

        if room == 1:
            return {'left': room, 'right': 2, 'up' : room, 'down': 4}[dir]
        elif room == 2:
            return {'left': 1, 'right': 3, 'up' : room, 'down': 5}[dir]
        elif room == 3:
            return {'left': 2, 'right': room, 'up' : room, 'down': 6}[dir]
        elif room == 4:
            return {'left': room, 'right': 5, 'up' : 1, 'down': 7}[dir]
        elif room == 5:
            return {'left': 4, 'right': 6, 'up' : 2, 'down': 8}[dir]
        elif room == 6:
            return {'left': 5, 'right': room, 'up' : 3, 'down': 9}[dir]
        elif room == 7:
            return {'left': room, 'right': 8, 'up' : 4, 'down': room}[dir]
        elif room == 8:
            return {'left': 7, 'right': 9, 'up' : 5, 'down': room}[dir]
        elif room == 9:
            return {'left': 8, 'right': room, 'up' : 6, 'down': room}[dir]
    ```

This is the program for the wall.They are written in 'player',and will detect the current room state to change the specific block displayed

    ``` Python
    if self.room == 1:
        visibility = [True, True, True, True, False, False, True, False, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 2:
        visibility = [True, True, True, False, False, False, True, False, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 3:
        visibility = [True, True, True, False, False, True, True, False, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 4:
        visibility = [True, False, True, True, False, False, True, False, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]        
    if self.room == 5:
        visibility = [True, False, True, False, False, False, True, False, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 6:
        visibility = [True, False, True, False, False, True, True, False, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 7:
        visibility = [True, False, True, True, False, False, True, True, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 8:
        visibility = [True, False, True, False, False, False, True, True, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    if self.room == 9:
        visibility = [True, False, True, False, False, True, True, True, True]
        for i in range(9):
            walls[i].is_visible = visibility[i]
    ```


A link to the [integral code](https://github.com/NopeIdontthinkso/pythonclass0/blob/main/mapp/map.py)
