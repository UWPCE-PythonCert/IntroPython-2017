from labyrinth.Player import Player


def test_player_creation():
    player = Player()
    player2 = Player(5, 5)


def test_player_moveRight():
    player = Player()
    player.moveRight()
    assert player.rect.x == 26


def test_player_moveLeft():
    player = Player()
    player.moveLeft()
    assert player.rect.x == 24


def test_player_moveUp():
    player = Player()
    player.moveUp()
    assert player.rect.y == 24


def test_player_moveDown():
    player = Player()
    player.moveDown()
    assert player.rect.y == 26
