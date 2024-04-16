# Author: John Burtsche
# GitHub username: jtburtsche
# Date: 3/15/23
# Description: Contains 5 different unit tests for CheckersGame.py

import unittest
from CheckersGame import Checkers, Player

game = Checkers()                                       #basic setup for start of the game
Player1 = game.create_player("Lucy", "White")
Player2 = game.create_player("Jacob", "Black")



class TestForCheckersGame(unittest.TestCase):

    def test_1(self):
        """Checks that moving a black checker changes the original location"""
        game.play_game("Jacob", (5, 6), (4, 7))                                 #black piece moves
        result = game.get_checker_details((5,6))

        self.assertIsNot(result, "Black")                                       #moved space does not equal black

    def test_2(self):
        """Checks if moving a white checker changes the new location to white"""
        game.play_game("Lucy", (2, 5), (3, 6))                                  #white piece moves
        result = game.get_checker_details((3,6))

        self.assertEqual(result, None)                                          #original space is none


    def test_3(self):
        """Checks if Black_King jumping works"""
        game.play_game("Jacob", (4, 7), (2, 5))
        game.play_game("Jacob", (5, 0), (4, 1))
        game.play_game("Lucy", (1, 4), (3, 6))                      #1 captured piece for test 5
        game.play_game("Lucy", (2, 1), (3, 0))
        game.play_game("Jacob", (4, 1), (3, 2))
        game.play_game("Lucy", (2, 3), (3, 4))
        game.play_game("Jacob", (3, 2), (2, 3))
        game.play_game("Lucy", (0, 5), (1, 4))
        game.play_game("Jacob", (5, 2), (4, 1))
        game.play_game("Lucy", (1, 4), (2, 5))
        game.play_game("Jacob", (2, 3), (1, 4))
        game.play_game("Lucy", (1, 0), (2, 1))
        game.play_game("Jacob", (1, 4), (0, 5))                     #1 King for test 4
        game.play_game("Lucy", (3, 6), (4, 7))
        game.play_game("Jacob", (0, 5), (1, 4))
        game.play_game("Lucy", (3, 4), (4, 5))
        game.play_game("Jacob", (1, 4), (3, 6))
        result = game.get_checker_details((2,5))
        self.assertIs(result, None)

    def test_4(self):
        """Tests that the king count works in the Player class"""
        result = Player2.get_king_count()
        self.assertEqual(result, 1)

    def test_5(self):
        """Test that the captured pieces works in the Player Class"""
        result = Player1.get_captured_pieces_count()
        self.assertEqual(result,1)



if __name__ == '__main__':
    unittest.main()