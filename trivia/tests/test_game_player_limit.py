from ..trivia import Game
from unittest import mock as mocker


def test_number_of_players():
    game = Game(players=["Alice", "Bob", "Tom", "Jerry", "Lisa", "Maggie"])
    assert game.number_of_players() == 6
    game.players = ["Alice", "Bob", "Tom", "Jerry", "Lisa"]
    assert game.number_of_players() == 5
    game.players = []
    assert game.number_of_players() == 0
    game.players = ["Alice", "Bob", "Tom", "Jerry", "Lisa", "Maggie", "Homer", "Marge"]
    assert game.number_of_players() == 8


@mocker.patch("trivia.trivia.Game.number_of_players")
def test_game_is_playable(mock_number_of_players):
    game = Game()

    mock_number_of_players.return_value = 2
    assert game.is_playable() is True
    mock_number_of_players.return_value = 6
    assert game.is_playable() is True

    mock_number_of_players.return_value = 1
    assert game.is_playable() is False
    mock_number_of_players.return_value = 7
    assert game.is_playable() is False


@mocker.patch("trivia.trivia.Game.is_playable")
def test_game_start_calls_game_is_playable_property(mock_game_is_playable, capfd):
    mock_game_is_playable.return_value = False
    game = Game()
    game.start()
    out, _err = capfd.readouterr()
    assert out == "Game is not playable\n"
