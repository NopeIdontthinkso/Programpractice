from pycat.core import Window
answer=input('Hey dude')
size=input('Hey dude')
window=Window(1500,800)
food=window.create_sprite()
if answer=='owl':
    food.image='owl.gif'
    print('You looks hungry,go eating the',answer)
if answer=='pig':
    food.image='pig.png'
    print('You looks hungry,go eating the',answer)
if size=='big':
    food.scale = 2
if size=='small':
    food.scale = 0.5
food.x=750
food.y=400
# else:
#     print('There is a disgusting rat,kill it')
#     food.image='rat.png'
#     food.x=300
#     food.y=100
window.run()