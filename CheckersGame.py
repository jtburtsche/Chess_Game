# Author: John Burtsche
# GitHub username: jtburtsche
# Date: 3/14/2023
# Description: This program will use two classes (Checkers and Player) which will work together in order to create a playable checkers game. The checkers class is where the game will be played and the original data will be created. The Player class will hold different statistics of the individual players.

class OutofTurn(Exception):
    """Exception when the player moving is out of turn"""
    pass

class InvalidSquare(Exception):
    """Exception when the player tries to move a piece to an invalid location"""
    pass

class InvalidPlayer(Exception):
    """Exception when the wrong player tries to make a turn"""
    pass


class Checkers:
    """Class Checkers that initializes the board, initializes the player to be used in the Player class, plays the game by manipulating the board correctly for every turn, determines a winner if there are no pieces left, prints board, and gets checker details"""

    def __init__(self):
        self._board = [                                                         #initializes the board with multiple arrays
            [None, "White", None, "White", None, "White", None, "White"],
            ["White", None, "White", None, "White", None, "White", None],
            [None, "White", None, "White", None, "White", None, "White"],
            [None, None, None, None,None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["Black", None, "Black", None, "Black", None,"Black", None],
            [None, "Black", None, "Black", None, "Black", None, "Black"],
            ["Black", None, "Black", None, "Black", None,"Black", None]]
        self._turn = "Black"                                                    #sets start to black
        self._players = []                                                      #hold place for turns names and players
        self._noturn= []
        self._blackname = []
        self._whitename = []
        self._PlayerA= []
        self._PlayerB = []


    def create_player(self, player_name, piece_color):
        """creates a player within the Player class and utilizes the information to set details for who's turn it is"""

        if piece_color != "White" and piece_color != "Black":                   #exception if the color is invalid
            raise   InvalidPlayer("Piece color is unnacceptable")


        player = Player(player_name, piece_color)                               #sets Player class object

        self._players.append(player_name)

        if piece_color == "White":                                              #key details on who's turn
            self._noturn = player_name
            self._whitename = player_name
            self._PlayerA = player
            return player

        if piece_color == "Black":
            self._blackname = player_name
            self._PlayerB = player
            return player                                                          #returns player class object


    def play_game(self, player_name, starting_square_location, destination_square_location):
        """contains a lot of necessary information regarding moving a piece from one location to the next and stores certain data(captures, kings) in the player class"""

        capture = 0                                                             #sets capture to 0


        if player_name not in self._players:                                    #raises exceptions if it's not the players turn
            raise InvalidPlayer("Player name is invalid")

        if player_name in self._noturn:
            raise InvalidPlayer("Wrong Turn")




        start_y,start_x = starting_square_location                              #makes starting location more accessible based on axis's

        if not 0 <= start_x <= 7:                                               #exceptions if starting location is not on the board
            raise  InvalidSquare("Starting Location error")

        if not 0 <= start_y <= 7:
            raise  InvalidSquare("Starting Location error")

        dest_y, dest_x = destination_square_location                            #makes destination location more accessible based on axis's

        if not 0 <= dest_x <= 7:
            raise InvalidSquare("Destination Location error")                   #exceptions if destination location is not on the board

        if not 0 <= dest_y <= 7:
            raise InvalidSquare("Destination Location error")




        if self._turn == "Black":                                               #checks that the piece is one of the 3 types
            if self._board[start_y][start_x] != "Black":
                if self._board[start_y][start_x] != "Black_King":
                    if self._board[start_y][start_x] != "Black_Triple_King":
                        raise InvalidSquare("Piece is not owned")


        if self._turn == "White":                                               #checks if the piece is one of the 3 types and raises an exception if not
            if self._board[start_y][start_x] != "White":
                if self._board[start_y][start_x] != "White_King":
                    if self._board[start_y][start_x] != "White_Triple_King":
                        raise InvalidSquare("Piece is not owned")




        if self._board[dest_y][dest_x] != None:                                 #makes sure that the destination is empty and raises an exception if not
            raise InvalidSquare("Square is filled")



        #different types of moves starts here



        if self._board[start_y][start_x] == "Black":                            #simple jump one square black
            if start_y - 1 == dest_y:
                if start_x - 1 == dest_x or start_x + 1 == dest_x:
                    self._board[start_y][start_x] = None                        #sets start location to none and destination to black

                    self._board[dest_y][dest_x] = "Black"
                else: raise InvalidSquare("Can't move the piece in that direction")


        if self._board[start_y][start_x] == "White":                            #simple jump one square white
            if start_y + 1 == dest_y:
                if start_x - 1 == dest_x or start_x + 1 == dest_x:
                    self._board[start_y][start_x] = None                        #sets start location to none and destination to white

                    self._board[dest_y][dest_x] = "White"
                else: raise InvalidSquare("Can't move the piece in that direction")


        #single piece capture


        if self._board[start_y][start_x] == "Black":                            #black capture
            if start_y - 2 == dest_y:                                           #parameters for this type of capture
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "White" or self._board[start_y - 1][start_x - 1] == "White_King" or self._board[start_y - 1][start_x - 1] == "White_Triple_King":       #if the piece moves by 2 in x and y axis and the piece in between is a white
                        self._board[start_y][start_x] = None                    #sets piece in between to none, start to none, and destination to black

                        self._board[start_y-1][start_x-1] = None
                        capture +=1
                        self._PlayerB.set_captured_pieces()      #increments the captured pieces in the player class

                        self._board[dest_y][dest_x] = "Black"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                       #other parameters (x axis change) for this type of capture
                    if self._board[start_y - 1][start_x + 1] == "White" or self._board[start_y - 1][start_x + 1] == "White_King" or self._board[start_y - 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None                    #sets piece in between to none, start to none, and destination to black

                        self._board[start_y - 1][start_x + 1] = None
                        capture += 1
                        self._PlayerB.set_captured_pieces()      #increments the captured pieces in the player class

                        self._board[dest_y][dest_x] = "Black"
                    else:
                        raise InvalidSquare("Invalid Jump")




        if self._board[start_y][start_x] == "White":                            #white capture (same thing as black just different parameters)
            if start_y + 2 == dest_y:
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "Black" or self._board[start_y + 1][start_x - 1] == "Black_King" or self._board[start_y + 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y+1][start_x-1] = None

                        capture +=1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:
                    if self._board[start_y + 1][start_x + 1] == "Black" or self._board[start_y + 1][start_x + 1] == "Black_King" or self._board[start_y + 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y + 1][start_x + 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White"
                    else:
                        raise InvalidSquare("Invalid Jump")



        #king simple move


        if self._board[start_y][start_x] == "Black_King":                               #black king simple move
            if start_y - 1 == dest_y or start_y + 1 == dest_y:                          #makes sure move is legal (adds both y directions)
                if start_x - 1 == dest_x or start_x + 1 == dest_x:
                    self._board[start_y][start_x] = None                                #returns none in original location and Black_King in dest

                    self._board[dest_y][dest_x] = "Black_King"
                else: raise InvalidSquare("Can't move the piece in that direction")


        if self._board[start_y][start_x] == "White_King":                               #white king simple move (same as black just different parameters)
            if start_y + 1 == dest_y or start_y - 1 == dest_y:
                if start_x - 1 == dest_x or start_x + 1 == dest_x:
                    self._board[start_y][start_x] = None

                    self._board[dest_y][dest_x] = "White_King"
                else: raise InvalidSquare("Can't move the piece in that direction")




        if self._board[start_y][start_x] == "White_King":                               #white king capture
            if start_y + 2 == dest_y:                                                   #sets y and x
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "Black" or self._board[start_y + 1][start_x - 1] == "Black_King" or self._board[start_y + 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None                            #checked that an enemy piece is there and performs the capture

                        self._board[start_y+1][start_x-1] = None
                        capture +=1                                                     #increments captured piece
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                              #same as White King capture just different x direction
                    if self._board[start_y + 1][start_x + 1] == "Black" or self._board[start_y + 1][start_x + 1] == "Black_King" or self._board[start_y + 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y + 1][start_x + 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y - 2 == dest_y:                                                 #same as previous just differrent y destination
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "Black" or self._board[start_y - 1][start_x - 1] == "Black_King" or self._board[start_y - 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y - 1][start_x - 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()
                        self._board[dest_y][dest_x] = "White_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same as previous just different x direction
                    if self._board[start_y - 1][start_x + 1] == "Black" or self._board[start_y - 1][start_x + 1] == "Black_King" or self._board[start_y - 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y - 1][start_x + 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_King"

                    else:
                        raise InvalidSquare("Invalid Jump")


        if self._board[start_y][start_x] == "Black_King":                               #same as white king capture just for black king instead
            if start_y - 2 == dest_y:
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "White" or self._board[start_y - 1][start_x - 1] == "White_King" or self._board[start_y - 1][start_x - 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y-1][start_x-1] = None
                        capture +=1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same as white king capture just for black king instead
                    if self._board[start_y - 1][start_x + 1] == "White" or self._board[start_y - 1][start_x + 1] == "White_King" or self._board[start_y - 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y - 1][start_x + 1] = None
                        capture += 1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y + 2 == dest_y:                                                   #same as white king capture just for black king instead
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "White" or self._board[start_y + 1][start_x - 1] == "White_King" or self._board[start_y + 1][start_x - 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y+1][start_x-1] = None
                        capture +=1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same as white king capture just for black king instead
                    if self._board[start_y + 1][start_x + 1] == "White" or self._board[start_y + 1][start_x + 1] == "White_King" or self._board[start_y + 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y + 1][start_x + 1] = None
                        capture += 1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_King"
                    else:
                        raise InvalidSquare("Invalid Jump")



        #Triple king simple move



        if self._board[start_y][start_x] == "Black_Triple_King":
            if start_y - 1 == dest_y or start_y + 1 == dest_y:                          #checks that start and end are just incremented by 1
                if start_x - 1 == dest_x or start_x + 1 == dest_x:
                    self._board[start_y][start_x] = None                                #replaces start and end with correct string

                    self._board[dest_y][dest_x] = "Black_Triple_King"
                else: raise InvalidSquare("Can't move the piece in that direction")


        if self._board[start_y][start_x] == "White_Triple_King":                        #same as Black Triple King, but White
            if start_y + 1 == dest_y or start_y - 1 == dest_y:
                if start_x - 1 == dest_x or start_x + 1 == dest_x:
                    self._board[start_y][start_x] = None

                    self._board[dest_y][dest_x] = "White_Triple_King"
                else: raise InvalidSquare("Can't move the piece in that direction")


        #Triple King capture


        if self._board[start_y][start_x] == "White_Triple_King":
            if start_y + 2 == dest_y:                                                   #sets x and y dest and makes sure there is a piece in between
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "Black" or self._board[start_y + 1][start_x - 1] == "Black_King" or self._board[start_y + 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y+1][start_x-1] = None                        #updates start abd destination as well as updates the capture list
                        capture +=1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same as previous different x axis
                    if self._board[start_y + 1][start_x + 1] == "Black" or self._board[start_y + 1][start_x + 1] == "Black_King" or self._board[start_y + 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y + 1][start_x + 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y - 2 == dest_y:                                                   #same as previous different y axis
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "Black" or self._board[start_y - 1][start_x - 1] == "Black_King" or self._board[start_y - 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y - 1][start_x - 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same as previous different x axis
                    if self._board[start_y - 1][start_x + 1] == "Black" or self._board[start_y - 1][start_x + 1] == "Black_King" or self._board[start_y - 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y - 1][start_x + 1] = None
                        capture += 1
                        self._PlayerA.set_captured_pieces()

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")


        if self._board[start_y][start_x] == "Black_Triple_King":                        #same as White_Triple_King with different parameters
            if start_y - 2 == dest_y:
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "White" or self._board[start_y - 1][start_x - 1] == "White_King" or self._board[start_y - 1][start_x - 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y-1][start_x-1] = None
                        capture +=1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:
                    if self._board[start_y - 1][start_x + 1] == "White" or self._board[start_y - 1][start_x + 1] == "White_King" or self._board[start_y - 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y - 1][start_x - 1] = None
                        capture += 1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y + 2 == dest_y:
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "White" or self._board[start_y + 1][start_x - 1] == "White_King" or self._board[start_y + 1][start_x - 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y+1][start_x-1] = None
                        capture +=1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:
                    if self._board[start_y + 1][start_x + 1] == "White" or self._board[start_y + 1][start_x + 1] == "White_King" or self._board[start_y + 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[start_y + 1][start_x + 1] = None
                        capture += 1
                        self._PlayerB.set_captured_pieces()

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")



        #Triple King Friendly Jump



        if self._board[start_y][start_x] == "White_Triple_King":
            if start_y + 2 == dest_y:                                                   #checks destination and start locations are correct
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "White" or self._board[start_y + 1][start_x - 1] == "White_King" or self._board[start_y + 1][start_x - 1] == "White_Triple_King":       #makes sure the same color is in the inbetween space
                        self._board[start_y][start_x] = None                            #changes start to none and destination to Triple King


                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same just different x axis
                    if self._board[start_y + 1][start_x + 1] == "White" or self._board[start_y + 1][start_x + 1] == "White_King" or self._board[start_y + 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y - 2 == dest_y:                                                   #same just different y axis
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "White" or self._board[start_y - 1][start_x - 1] == "White_King" or self._board[start_y - 1][start_x - 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:                                               #same just different x axis
                    if self._board[start_y - 1][start_x + 1] == "White" or self._board[start_y - 1][start_x + 1] == "White_King" or self._board[start_y - 1][start_x + 1] == "White_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")


        if self._board[start_y][start_x] == "Black_Triple_King":                        #same as previous, just for the color black
            if start_y - 2 == dest_y:
                if start_x - 2 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "Black" or self._board[start_y - 1][start_x - 1] == "Black_King" or self._board[start_y - 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:
                    if self._board[start_y - 1][start_x + 1] == "Black" or self._board[start_y - 1][start_x + 1] == "Black_King" or self._board[start_y - 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y + 2 == dest_y:
                if start_x - 2 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "Black" or self._board[start_y + 1][start_x - 1] == "Black_King" or self._board[start_y + 1][start_x - 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 2 == dest_x:
                    if self._board[start_y + 1][start_x + 1] == "Black" or self._board[start_y + 1][start_x + 1] == "Black_King" or self._board[start_y + 1][start_x + 1] == "Black_Triple_King":
                        self._board[start_y][start_x] = None

                        self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")



        #Triple King double bounce



        if self._board[start_y][start_x] == "White_Triple_King":
            if start_y + 3 == dest_y:                                                   #checks that destination is within 3 spaces along x and y
                if start_x - 3 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "Black" or self._board[start_y + 1][start_x - 1] == "Black_King" or self._board[start_y + 1][start_x - 1] == "Black_Triple_King":           #checks that both inbetween pieces are black
                        if self._board[start_y + 2][start_x - 2] == "Black" or self._board[start_y + 2][start_x - 2] == "Black_King" or self._board[start_y + 2][start_x - 2] == "Black_Triple_King":
                            self._board[start_y][start_x] = None

                            self._board[start_y+1][start_x-1] = None                    #sets black locations/start to none and destination as triple king as well as raises captures by 2
                            capture +=1
                            self._PlayerA.set_captured_pieces()

                            self._board[start_y+2][start_x-2] = None
                            capture +=1
                            self._PlayerA.set_captured_pieces()

                            self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 3 == dest_x:                                               #same as previous just different x axis
                    if self._board[start_y + 1][start_x + 1] == "Black" or self._board[start_y + 1][start_x + 1] == "Black_King" or self._board[start_y + 1][start_x + 1] == "Black_Triple_King":
                        if self._board[start_y + 2][start_x + 2] == "Black" or self._board[start_y + 2][start_x + 2] == "Black_King" or self._board[start_y + 2][start_x + 2] == "Black_Triple_King":
                            self._board[start_y][start_x] = None

                            self._board[start_y + 1][start_x + 1] = None
                            capture += 1
                            self._PlayerA.set_captured_pieces()

                            self._board[start_y + 2][start_x + 2] = None
                            capture += 1
                            self._PlayerA.set_captured_pieces()

                            self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y - 3 == dest_y:                                                   #same as previous just different y axis
                if start_x - 3 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "Black" or self._board[start_y - 1][start_x - 1] == "Black_King" or self._board[start_y - 1][start_x - 1] == "Black_Triple_King":
                        if self._board[start_y - 2][start_x - 2] == "Black" or self._board[start_y - 2][start_x - 2] == "Black_King" or self._board[start_y - 2][start_x - 2] == "Black_Triple_King":
                            self._board[start_y][start_x] = None

                            self._board[start_y - 1][start_x - 1] = None
                            capture += 1
                            self._PlayerA.set_captured_pieces()

                            self._board[start_y - 2][start_x - 2] = None
                            capture += 1
                            self._PlayerA.set_captured_pieces()

                            self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 3 == dest_x:                                               #same as previous just differnt x axis
                    if self._board[start_y - 1][start_x + 1] == "Black" or self._board[start_y - 1][start_x + 1] == "Black_King" or self._board[start_y - 1][start_x + 1] == "Black_Triple_King":
                        if self._board[start_y - 2][start_x + 2] == "Black" or self._board[start_y - 2][start_x + 2] == "Black_King" or self._board[start_y - 2][start_x + 2] == "Black_Triple_King":

                            self._board[start_y][start_x] = None

                            self._board[start_y - 1][start_x + 1] = None
                            capture += 1
                            self._PlayerA.set_captured_pieces()

                            self._board[start_y - 2][start_x + 2] = None
                            capture += 1
                            self._PlayerA.set_captured_pieces()

                            self._board[dest_y][dest_x] = "White_Triple_King"

                    else:
                        raise InvalidSquare("Invalid Jump")


        if self._board[start_y][start_x] == "Black_Triple_King":                        #same as white triple king double jump, just for black instead
            if start_y - 3 == dest_y:
                if start_x - 3 == dest_x:
                    if self._board[start_y - 1][start_x - 1] == "White" or self._board[start_y - 1][start_x - 1] == "White_King" or self._board[start_y - 1][start_x - 1] == "White_Triple_King":
                        if self._board[start_y - 2][start_x - 2] == "White" or self._board[start_y - 2][start_x - 2] == "White_King" or self._board[start_y - 2][start_x - 2] == "White_Triple_King":

                            self._board[start_y][start_x] = None

                            self._board[start_y-1][start_x-1] = None
                            capture +=1
                            self._PlayerB.set_captured_pieces()

                            self._board[start_y-2][start_x-2] = None
                            capture +=1
                            self._PlayerB.set_captured_pieces()

                            self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")


                if start_x + 3 == dest_x:
                    if self._board[start_y - 1][start_x + 1] == "White" or self._board[start_y - 1][start_x + 1] == "White_King" or self._board[start_y - 1][start_x + 1] == "White_Triple_King":
                        if self._board[start_y - 2][start_x + 2] == "White" or self._board[start_y - 2][start_x + 2] == "White_King" or self._board[start_y - 2][start_x + 2] == "White_Triple_King":

                            self._board[start_y][start_x] = None

                            self._board[start_y - 1][start_x + 1] = None
                            capture += 1
                            self._PlayerB.set_captured_pieces()

                            self._board[start_y - 2][start_x + 2] = None
                            capture += 1
                            self._PlayerB.set_captured_pieces()

                            self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

            if start_y + 3 == dest_y:
                if start_x - 3 == dest_x:
                    if self._board[start_y + 1][start_x - 1] == "White" or self._board[start_y + 1][start_x - 1] == "White_King" or self._board[start_y + 1][start_x - 1] == "White_Triple_King":
                        if self._board[start_y + 2][start_x - 2] == "White" or self._board[start_y + 2][start_x - 2] == "White_King" or self._board[start_y + 2][start_x - 2] == "White_Triple_King":

                            self._board[start_y][start_x] = None

                            self._board[start_y+1][start_x-1] = None
                            capture +=1
                            self._PlayerB.set_captured_pieces()

                            self._board[start_y+2][start_x-2] = None
                            capture +=1
                            self._PlayerB.set_captured_pieces()

                            self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")

                if start_x + 3 == dest_x:
                    if self._board[start_y + 1][start_x + 1] == "White" or self._board[start_y + 1][start_x + 1] == "White_King" or self._board[start_y + 1][start_x + 1] == "White_Triple_King":
                        if self._board[start_y + 2][start_x + 2] == "White" or self._board[start_y + 2][start_x + 2] == "White_King" or self._board[start_y + 2][start_x + 2] == "White_Triple_King":

                            self._board[start_y][start_x] = None

                            self._board[start_y + 1][start_x + 1] = None
                            capture += 1
                            self._PlayerB.set_captured_pieces()

                            self._board[start_y + 2][start_x + 2] = None
                            capture += 1
                            self._PlayerB.set_captured_pieces()

                            self._board[dest_y][dest_x] = "Black_Triple_King"
                    else:
                        raise InvalidSquare("Invalid Jump")





        #finishing up




        if self._board[dest_y][dest_x] == "White":                                  #sets white piece to king if it reaches the end of the board
            if dest_y ==7:
                self._board[dest_y][dest_x] = "White_King"
                self._turn = "Black"                                                #changes turn, and raises king count
                self._noturn = player_name
                self._PlayerA.set_king_count()
                return capture


        if self._board[dest_y][dest_x] == "White_King":                             #sets white piece to Triple king if it reaches the end of the board
            if dest_y ==0:
                self._board[dest_y][dest_x] = "White_Triple_King"
                self._turn = "Black"                                                #changes turn, and raises triple king count
                self._noturn = player_name
                self._PlayerA.set_triple_king()
                return capture


        if self._board[dest_y][dest_x] == "Black":                                  #sets black piece to king if it reaches the end of the board
            if dest_y == 0:
                self._board[dest_y][dest_x] = "Black_King"
                self._turn = "White"                                                #changes turn, and raises triple king count
                self._noturn = player_name
                self._PlayerB.set_king_count()
                return capture

        if self._board[dest_y][dest_x] == "Black_King":                             #sets black piece to Triple king if it reaches the end of the board
            if dest_y == 7:
                self._board[dest_y][dest_x] = "Black_Triple_King"
                self._turn = "White"                                                #changes turn, and raises triple king count
                self._noturn = player_name
                self._PlayerB.set_triple_king()
                return capture


        if self._turn == "Black":                                                   #changes turn if no captures were made
            if capture ==0:
                self._turn = "White"
                self._noturn = player_name
                return capture

        if self._turn == "White":
            if capture ==0:
                self._turn = "Black"
                self._noturn = player_name

        return capture


    def get_checker_details(self, square_location):
        square_y,square_x = square_location


        if not 0 <= square_x <= 7:
            raise  InvalidSquare("Location error")

        if not 0 <= square_y <= 7:
            raise  InvalidSquare("Location error")

        print(self._board[square_y][square_x])


    def print_board(self):
        print(self._board)                                                      #prints board

    def game_winner(self):
        white=0                                                                 #sets white piece and black piece count to 0
        black=0

        for row in self._board:                                                 #loops through the board and increments the color for every piece that it
            for piece in row:

                if piece == "White" or piece =="White_King" or piece == "White_Triple_King":    #if loop lands on white piece
                    white += 1


                if piece == "Black" or piece == "Black_King" or piece == "Black_Triple_King":   #if loop lands on black piece
                    black += 1

        if black == 0:
            return self._whitename                                              #returns the name of the white player saved in create a player function

        if white == 0:
            return self._blackname                                              #returns the name of the black player saved in create a player function

        else:
            return "Game has not ended"                                         #if game isn't over

class Player:
    """class player that holds the data for each of the players in the game, including there kings, triple kings, and captured pieces"""
    def __init__(self, player_name, checker_color):
        self._player_name = player_name
        self._checker_color = checker_color
        self._kings = 0
        self._triple_kings = 0
        self._captured_pieces = 0


    def get_king_count(self):                                                   #simple get methods for data
        return self._kings

    def get_triple_king_count(self):
        return self._triple_kings

    def get_captured_pieces_count(self):
        return self._captured_pieces

    def set_king_count(self):                                                   #increments each of the categories based on what happens in the play game function of the Checkers class
        self._kings +=1

    def set_triple_king(self):
        self._triple_kings +=1

    def set_captured_pieces(self):
        self._captured_pieces +=1





if __name__ == "__main__":
    game= Checkers()
    Player1 = game.create_player("Lucy", "White")
    Player2 = game.create_player("Jacob", "Black")
    game.play_game("Jacob", (5,6), (4,7))
    game.play_game("Lucy", (2,5),(3,6))
    game.play_game("Jacob", (4,7), (2,5))
    game.play_game("Jacob", (5,0), (4,1))
    game.play_game("Lucy", (1,4), (3,6))
    game.play_game("Lucy", (2,1), (3,0))
    game.play_game("Jacob", (4,1),(3,2))
    game.play_game("Lucy", (2,3), (3,4))
    game.play_game("Jacob",(3,2), (2,3))
    game.play_game("Lucy", (0,5),(1,4))
    game.play_game("Jacob", (5,2), (4,1))
    game.play_game("Lucy", (1,4), (2,5))
    game.play_game("Jacob", (2,3), (1,4))
    game.play_game("Lucy", (1,0), (2,1))
    game.play_game("Jacob",(1,4),(0,5))
    game.play_game("Lucy", (3,6),(4,7))
    game.play_game("Jacob", (0,5), (1,4))
    game.play_game("Lucy", (3,4),(4,5))
    game.play_game("Jacob", (1,4),(3,6))
    game.get_checker_details((4,7))

    print(Player2.get_captured_pieces_count())
    print(Player2.get_king_count())
    game.print_board()