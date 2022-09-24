from pycat.core import Sprite


class Turtle(Sprite):

    def draw_forward(self, f:int = 10):
        a = self.position
        self.move_forward(f)
        b = self.position
        self.window.create_line(a.x, a.y, b.x, b.y)
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
        
