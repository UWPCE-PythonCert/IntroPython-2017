from labyrinth.Labyrinth import Labyrinth, Wall
from random import choice
import pytest

def test_Labyrinth_init():
    laby = Labyrinth()

def test_Wall_init():
    wall = Wall(5,5)
    wall2 = Wall(3,3,'north')

def test_borders():
    lab = Labyrinth(5,5)
    assert lab.get_borders() == [[2,2,2,2,2],
                                 [2,1,1,1,2],
                                 [2,1,1,1,2],
                                 [2,1,1,1,2],
                                 [2,2,2,2,2]
                                ]

def test_peek():
    lab = Labyrinth()
    directions = ['north', 'south', 'east', 'west']
    lab.labyrinth = [[1,Wall(0, 1, 'south'),1],
                     [1,Wall(1,1, 'east'),1],
                     [Wall(2, 0, 'west'), 1, Wall(2,2, 'north')]
                    ]
    assert lab.peek(lab.labyrinth[1][1])
    assert lab.peek(lab.labyrinth[2][2]) is False
    assert lab.peek(lab.labyrinth[2][0])
    assert lab.peek(lab.labyrinth[0][1])
