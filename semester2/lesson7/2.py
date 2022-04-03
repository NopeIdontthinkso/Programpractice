from pycat.core import Window, Point, Sprite

w = Window()


class Turtle(Sprite):

    def draw_forward(self, f:int = 10):
        a = self.position
        self.move_forward(f)
        b = self.position
        w.create_line(a.x, a.y, b.x, b.y)
    def draw_circle(self, f):
        for _ in range(2880):
            self.draw_forward(f)
            self.rotation += 1/8
    def draw_triangle(self,f):
        for _ in range(3):
            self.draw_forward(f)
            self.rotation += 120
    def draw_square(self, f):
        for _ in range(4):
            self.draw_forward(f)
            self.rotation += 90
    
    def draw_regular_polygon(self, sides, f):
        for _ in range(sides):
            self.draw_forward(f)
            self.rotation += 360/sides
    def draw_star(self, sides, f):
        for _ in range(sides):
            self.draw_forward(f)
            self.rotation += 180-360/sides
        
    

t = w.create_sprite(Turtle, x= w.width/2, y= w.height/2)


t.draw_star(20, 100)


        











w.run()