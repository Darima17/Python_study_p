import unittest
from typing import List, Tuple
from ex01 import *
from ex00 import *


class TestEx00(unittest.TestCase):
    """Test cases for the ex00 module."""

    def setUp(self) -> None:
        self.key = Key("zax2rulez")
        self.key2 = Key("1234")

    def test_key_class(self):
        try:
            assert len(self.key) == 1337, 'len(key) == 1337'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert self.key[404] == 3, 'key[404] == 3'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert self.key > 9000, 'key > 9000'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert self.key.passphrase == "zax2rulez", 'key.passphrase == "zax2rulez"'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert str(
                self.key) == "GeneralTsoKeycard", 'str(key) == "GeneralTsoKeycard"'
        except AssertionError as msg:
            print('AssertionError:', msg)

        else:
            print("Success! Everything is passed!")

    def test_key_class_fail(self):
        try:
            assert len(self.key2) == 137, 'len(key) == 1337'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert self.key2[404] == 2, 'key[404] == 3'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert self.key2 > 90, 'key > 9000'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert self.key2.passphrase == "zax2rulez", 'key.passphrase == "zax2rulez"'
        except AssertionError as msg:
            print('AssertionError:', msg)

        try:
            assert str(self.key2) == "abcd", 'str(key) == "GeneralTsoKeycard"'
        except AssertionError as msg:
            print('AssertionError:', msg)

        else:
            print("Success! Everything is passed!")


class TestEx01(unittest.TestCase):
    """Test cases for the Game class in the ex01 module."""

    def setUp(self) -> None:
        """Initialize the game before each test."""
        self.game = Game()

    def list(self) -> List[Tuple[str, int]]:
        """Get the top 3 players in the game registry."""
        top3list = []
        top3 = Counter(self.game.registry).most_common(3)
        for player, score in top3:
            top3list.append((player, score))
        return top3list

    def test_play(self) -> None:
        """Test the play method in the Game class."""
        type_charecter = [Cheater(), Cooperator(), Copycat(),
                          Grudger(), Detective()]
        for i in range(len(type_charecter)):
            for j in range(i + 1, len(type_charecter)):
                self.game.play(type_charecter[i], type_charecter[j])

        self.assertEqual(
            self.list(),
            [
                ('Copycat', 57), ('Grudger', 46), ('Cheater', 45)
            ])

    def test_Rudolf(self) -> None:
        """Test the play method with Rudolf."""
        type_charecter = [
            Cheater(),
            Cooperator(),
            Copycat(),
            Grudger(),
            Detective(),
            Rudolf()
        ]
        for i in range(len(type_charecter)):
            for j in range(i + 1, len(type_charecter)):
                self.game.play(type_charecter[i], type_charecter[j])

        self.assertEqual(
            self.list(),
            [
                ('Rudolf', 75), ('Copycat', 74), ('Grudger', 63)
            ])

    def test_Rudolf_Cooperater(self) -> None:
        """Test the play method with Rudolf and Cooperator."""
        self.game.play(Rudolf(), Cooperator())
        self.assertEqual(
            self.list(),
            [('Rudolf', 21), ('Cooperator', 17)])

    def test_Rudolf_Detective(self) -> None:
        """Test the play method with Rudolf and Detective."""
        self.game.play(Rudolf(), Detective())
        self.assertEqual(
            self.list(),
            [('Rudolf', 13), ('Detective', 9)])

    def test_Rudolf_Grudger(self) -> None:
        """Test the play method with Rudolf and Grudger."""
        self.game.play(Rudolf(), Grudger())
        self.assertEqual(
            self.list(),
            [('Rudolf', 21), ('Grudger', 17)])

    def test_Rudolf_Copycat(self) -> None:
        """Test the play method with Rudolf and Copycat."""
        self.game.play(Rudolf(), Copycat())
        self.assertEqual(
            self.list(),
            [('Rudolf', 21), ('Copycat', 17)])


if __name__ == '__main__':

    unittest.main()
