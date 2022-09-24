from pycat.core import Window
x=input('enter x:')
y=input('enter y:')
window=Window(1500,800)
food=window.create_sprite()
food.image='owl.gif'
food.x=float(x)
food.y=float(y)
massange='my sprite has image='+food.image+',x='+str(food.x)+',y='+str(food.y)
print(massange)
window.run()