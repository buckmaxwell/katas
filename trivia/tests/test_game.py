import pytest
from ..trivia import Game, GameError, GameFullError  # Import the class from your module
from ..original import Game as OriginalGame


def test_game_cannot_be_played_with_one_person(capfd):
    """Test if the Game class initializes correctly."""
    game = Game()
    game.add("Alice")
    _out, _err = capfd.readouterr()
    game.start()
    out, _err = capfd.readouterr()
    assert out == "Game is not playable\n"


def test_game_can_be_played_with_two_people(capfd):
    """Test if the Game class initializes correctly."""
    game = Game()
    game.add("Alice")
    game.add("Bob")
    _out, _err = capfd.readouterr()
    game.start()
    out, _err = capfd.readouterr()
    assert out != "Game is not playable\n"


def test_game_can_be_played_with_six_people(capfd):
    """Test if the Game class initializes correctly."""
    game = Game()
    game.add("Alice")
    game.add("Bob")
    game.add("Tom")
    game.add("Jerry")
    game.add("Lisa")
    game.add("Maggie")

    _out, _err = capfd.readouterr()
    game.start()
    out, _err = capfd.readouterr()
    assert out != "Game is not playable\n"


def test_game_cannot_be_played_with_seven_people():
    """Test if the Game class initializes correctly."""
    game = Game()
    game.add("Alice")
    game.add("Bob")
    game.add("Tom")
    game.add("Jerry")
    game.add("Lisa")
    game.add("Maggie")
    with pytest.raises(GameFullError):
        game.add("Homer")
