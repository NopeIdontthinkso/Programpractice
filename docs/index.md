<link rel="stylesheet" type="text/css" media="all" href="style.css" />

# Game
by Jevil

![game](vid.gif)
## Introduction

玩家要在九個房間中不斷穿梭，尋找出現的敵人並將其擊殺獲取分數

---

## Implementation Details

我使用了python和pycat去製作這個遊戲
在Pycat我使用了``Color``, ``KeyCode``, ``Sprite``, ``Window``, ``Scheduler``,和``Label`` 的定義
也用了random裡的randint，我使用的技巧有inheritance, iteration, lists, conditionals, variables, functions, etc.

最難的的部分是如何做出牆的變化和從房間A的特定方向進入房間B之邏輯運算，實際上整個迷宮是同樣的九個大方塊重複呈現而已

這是進入下一個房間的判斷式

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

這是牆的顯現程式，寫在'玩家'裡並會偵測當前的房間來改變顯示的特定方塊

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
