from ..trivia import Game
from unittest import mock as mocker


@mocker.patch("trivia.trivia.Game.get_current_category")
def test_deck_never_runs_out_of_questions(mock_get_current_category, capfd):
    def ask_10_questions(game):
        for _ in range(10):
            game.ask_question()
            out, _ = capfd.readouterr()
            assert "Q_" in out

    game = Game()
    game.sports_questions = ["Q_SPORTS1", "Q_SPORTS2", "Q_SPORTS3"]
    mock_get_current_category.return_value = "Sports"
    ask_10_questions(game)

    game.pop_questions = ["Q_POP1", "Q_POP2", "Q_POP3"]
    mock_get_current_category.return_value = "Pop"
    ask_10_questions(game)

    game.science_questions = ["Q_SCIENCE1", "Q_SCIENCE2", "Q_SCIENCE3"]
    mock_get_current_category.return_value = "Science"
    ask_10_questions(game)

    game.rock_questions = ["Q_ROCK1", "Q_ROCK2", "Q_ROCK3"]
    mock_get_current_category.return_value = "Rock"
    ask_10_questions(game)
