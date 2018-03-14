from Labyrinth import Labyrinth, Wall

def test_Labyrinth_init():
    laby = Labyrinth()

def test_Wall_init():
    wall = Wall(5,5)
    wall2 = Wall(3,3,'north')

glb_labyrinth = Labyrinth()

def test_borders():
    lab = Labyrinth(5,5)
    assert lab.get_borders() == [[2,2,2,2,2],
                                 [2,1,1,1,2],
                                 [2,1,1,1,2],
                                 [2,1,1,1,2],
                                 [2,2,2,2,2]
                                ]
