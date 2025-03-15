#!/usr/bin/env python
from pydantic import BaseModel, conlist, model_validator
from pydantic.fields import Field
from typing import List

from collections import OrderedDict

# from random import randrange

MAX_PLAYERS = 6
MIN_PLAYERS = 2
CARDS_PER_CATEGORY = 50


class GameError(Exception):
    pass


class GameFullError(GameError):
    pass


class Game(BaseModel):
    players: conlist(str, min_length=MIN_PLAYERS, max_length=MAX_PLAYERS) = Field(
        default_factory=list
    )
    places: List[int] = Field(default_factory=lambda: [0] * MAX_PLAYERS)
    purses: List[int] = Field(default_factory=lambda: [0] * MAX_PLAYERS)
    in_penalty_box: List[int] = Field(default_factory=lambda: [False] * MAX_PLAYERS)

    categories: OrderedDict[str, List[str]] = Field(
        default_factory=lambda: OrderedDict(
            [("Pop", []), ("Science", []), ("Sports", []), ("Rock", [])]
        )
    )

    current_player: int = 0
    is_getting_out_of_penalty_box: bool = False

    @model_validator(mode="after")
    def post_init(self):
        for category, questions in self.categories.items():
            for i in range(CARDS_PER_CATEGORY):
                questions.append(f"{category} Question {i}")
        return self

    def is_playable(self):
        return (
            self.number_of_players() >= MIN_PLAYERS
            and self.number_of_players() <= MAX_PLAYERS
        )

    def number_of_players(self):
        return len(self.players)

    def add(self, player_name):
        if self.number_of_players() >= MAX_PLAYERS:
            raise GameFullError("Game is full!")
        self.players.append(player_name)
        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

    def move_player(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12

        print(
            self.players[self.current_player]
            + "'s new location is "
            + str(self.places[self.current_player])
        )
        print("The category is %s" % self.get_current_category())

    def take_turn(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)
        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print(
                    "%s is getting out of the penalty box"
                    % self.players[self.current_player]
                )
                self.move_player(roll)
                self.ask_question()
            else:
                print(
                    "%s is not getting out of the penalty box"
                    % self.players[self.current_player]
                )

                self.is_getting_out_of_penalty_box = False
        else:
            self.move_player(roll)
            self.ask_question()

    def ask_question(self):
        deck = self.categories[self.get_current_category()]
        question = deck.pop(0)
        deck.append(question)
        print(question)

    def get_current_category(self):
        number_of_categories = len(self.categories)
        return list(self.categories.keys())[
            self.places[self.current_player] % number_of_categories
        ]

    def update_current_player(self):
        self.current_player += 1
        if self.current_player == len(self.players):
            self.current_player = 0

    def award_gold_coin(self):
        self.purses[self.current_player] += 1
        print(
            self.players[self.current_player]
            + " now has "
            + str(self.purses[self.current_player])
            + " Gold Coins."
        )

    def did_player_win(self):
        return self.purses[self.current_player] == 6

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print("Answer was correct!!!!")
                self.award_gold_coin()
            else:
                pass
        else:
            print("Answer was corrent!!!!")
            self.award_gold_coin()

    def wrong_answer(self):
        print("Question was incorrectly answered")
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

    def start(self):
        if not self.is_playable():
            print("Game is not playable")
            return

        roll1 = 1
        roll2 = 0
        while True:

            # game.take_turn(randrange(5) + 1)
            rolled_dice = roll1
            self.take_turn(rolled_dice)

            # if randrange(9) == 7:
            if roll2 == 7:
                self.wrong_answer()
            else:
                self.was_correctly_answered()
                has_winner = self.did_player_win()
            self.update_current_player()

            if has_winner:
                break
            roll1 += 1
            if roll1 > 6:
                roll1 = 1

            roll2 += 1
            if roll2 > 9:
                roll2 = 0


if __name__ == "__main__":
    try:
        game = Game()

        game.add("Chet")
        game.add("Pat")
        game.add("Sue")

        game.start()
    except GameError as exc:
        print(exc)
