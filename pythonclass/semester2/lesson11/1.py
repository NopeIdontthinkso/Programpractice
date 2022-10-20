from pycat.core import Window, Sprite, Color, Scheduler, Label
from enum import Enum, auto
from random import choice, randint
from os.path import dirname


w = Window()
point = 0
best_score = 0
with open(dirname(__file__) + '/best_score.txt', 'r') as file:
    best_score = int(file.readline())


class Group(Enum):
    NOUNS = auto()
    VERBS = auto()
    ADJECTIVES = auto()
    
    def __str__(self):
        if self is Group.NOUNS:
            return 'NOUN'
        if self is Group.VERBS:
            return 'VERB'
        if self is Group.ADJECTIVES:
            return 'ADJECTIVE'


words = dict()
with open(dirname(__file__) + '/noun.txt', 'r') as file:
    words[Group.NOUNS] = [w.strip() for w in file.readlines()]
with open(dirname(__file__) + '/verb.txt', 'r') as file:
    words[Group.VERBS] =  [w.strip() for w in file.readlines()]
with open(dirname(__file__) + '/adjective.txt', 'r') as file:
    words[Group.ADJECTIVES] = [w.strip() for w in file.readlines()]
point_type = choice(list(words))


class Point(Label):

    def on_update(self, dt):
        self.text = 'Point:' + str(point)
class PointType(Label):

    def on_create(self):
        self.text = 'Point Type:' + str(point_type)
        self.y = a.y - self.content_height
    def on_update(self, dt):
        self.text = 'Point Type:' + str(point_type)
class BestScore(Label):

    def on_create(self):
        self.text = 'Best Score:' + str(best_score)
        self.y = b.y - self.content_height
    def on_update(self, dt):
        self.text = 'Best Score:' + str(best_score)


class Word(Sprite):

    def on_create(self):
        self.color = Color.BLUE
        self.type = choice(list(words))
        self.label = w.create_label(text = choice(words[self.type]))
        self.width = self.label.content_width + 20
        self.height = self.label.content_height + 20
        self.x=randint(0, w.width)
        self.y=w.height
        self.label.x = self.x - self.width/2 + 10
        self.label.y = self.y + self.height/2 - 10
    def on_update(self, dt):
        self.y -= 2
        self.label.x = self.x - self.width/2 + 10
        self.label.y = self.y + self.height/2 - 10
        if self.y < 50:
            self.delete()
    def on_left_click(self):
        global point
        global point_type
        global best_score
        if self.type is point_type:
            point += 1
            if point > best_score:
                with open(dirname(__file__) + '/best_score.txt', 'w') as file:
                    best_score = point
                    file.write(str(best_score))
        else:
            point -= 1
        self.delete()
    def delete(self):
        super().delete()
        self.label.delete()


def create_word():
    a = w.create_sprite(Word)


Scheduler.update(create_word, 1/2)
a = w.create_label(Point)
b = w.create_label(PointType)
c = w.create_label(BestScore)


w.run()