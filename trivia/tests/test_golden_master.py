from ..trivia import Game, GameError


def test_golden_master(capfd):

    try:
        game = Game()

        game.add("Chet")
        game.add("Pat")
        game.add("Sue")

        game.start()
    except GameError as exc:
        print(exc)

    out, _ = capfd.readouterr()
    with open("golden_master.txt") as f:
        assert out == f.read()
