#!/usr/bin/env python
from pydantic import BaseModel, conlist, model_validator
from pydantic.fields import Field
from typing import List


class Game(BaseModel):
    players: conlist(str, min_length=2, max_length=6) = Field(default_factory=list)
    places: List[int] = Field(default_factory=lambda: [0] * 6)
    purses: List[int] = Field(default_factory=lambda: [0] * 6)
    in_penalty_box: List[int] = Field(default_factory=lambda: [0] * 6)

    pop_questions: List[str] = Field(default_factory=list)
    science_questions: List[str] = Field(default_factory=list)
    sports_questions: List[str] = Field(default_factory=list)
    rock_questions: List[str] = Field(default_factory=list)

    current_player: int = 0
    is_getting_out_of_penalty_box: bool = False

    @model_validator(mode="after")
    def post_init(self):
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))
        return self

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2 and self.how_many_players <= 6

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print(
                    "%s is getting out of the penalty box"
                    % self.players[self.current_player]
                )
                self.places[self.current_player] = (
                    self.places[self.current_player] + roll
                )
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = (
                        self.places[self.current_player] - 12
                    )

                print(
                    self.players[self.current_player]
                    + "'s new location is "
                    + str(self.places[self.current_player])
                )
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print(
                    "%s is not getting out of the penalty box"
                    % self.players[self.current_player]
                )
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(
                self.players[self.current_player]
                + "'s new location is "
                + str(self.places[self.current_player])
            )
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        # No index error over 50 questions
        category_deck = {
            "Pop": self.pop_questions,
            "Science": self.science_questions,
            "Sports": self.sports_questions,
            "Rock": self.rock_questions,
        }
        deck = category_deck[self._current_category]
        question = deck.pop(0)
        deck.append(question)
        print(question)

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0:
            return "Pop"
        if self.places[self.current_player] == 4:
            return "Pop"
        if self.places[self.current_player] == 8:
            return "Pop"
        if self.places[self.current_player] == 1:
            return "Science"
        if self.places[self.current_player] == 5:
            return "Science"
        if self.places[self.current_player] == 9:
            return "Science"
        if self.places[self.current_player] == 2:
            return "Sports"
        if self.places[self.current_player] == 6:
            return "Sports"
        if self.places[self.current_player] == 10:
            return "Sports"
        return "Rock"

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


# from random import randrange

if __name__ == "__main__":
    not_a_winner = False

    game = Game()

    game.add("Chet")
    game.add("Pat")
    game.add("Sue")

    if not game.is_playable():
        exit()

    roll1 = 1
    roll2 = 0
    while True:

        # game.roll(randrange(5) + 1)
        game.roll(roll1)

        # if randrange(9) == 7:
        if roll2 == 7:
            game.wrong_answer()
        else:
            game.was_correctly_answered()
            has_winner = game.did_player_win()
        game.update_current_player()

        if has_winner:
            break
        roll1 += 1
        if roll1 > 6:
            roll1 = 1

        roll2 += 1
        if roll2 > 9:
            roll2 = 0
