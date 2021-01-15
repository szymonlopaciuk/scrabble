
from copy import deepcopy
from secrets import choice

# ----------- Persistence ------------
# Don't want to use a database. 
# Currently relying on Python's 
# thread-safe built-in data-types 

# For all socketio rooms and their contents, 
# aliased as game IDs
rooms = dict()
# -------------------------------------

# The weight each scrabble piece carries
pieces_weight = {
    ' ': 0,
    'A': 1,
    'E': 1,
    'I': 1,
    'N': 1,
    'O': 1,
    'R': 1,
    'S': 1,
    'W': 1,
    'Z': 1,
    'C': 2,
    'D': 2,
    'K': 2,
    'L': 2,
    'M': 2,
    'P': 2,
    'T': 2,
    'Y': 2,
    'B': 3,
    'G': 3,
    'H': 3,
    'J': 3,
    'Ł': 3,
    'U': 3,
    'Ą': 5,
    'Ę': 5,
    'F': 5,
    'Ó': 5,
    'Ś': 5,
    'Ż': 5,
    'Ć': 6,
    'Ń': 7,
    'Ź': 9,
}

# The number of pieces each scrabble piece has
pieces_number = {
    ' ': 2,
    'A': 9,
    'E': 7,
    'I': 8,
    'N': 5,
    'O': 6,
    'R': 4,
    'S': 4,
    'W': 4,
    'Z': 5,
    'C': 3,
    'D': 3,
    'K': 3,
    'L': 3,
    'M': 3,
    'P': 3,
    'T': 3,
    'Y': 4,
    'B': 2,
    'G': 2,
    'H': 2,
    'J': 2,
    'Ł': 2,
    'U': 2,
    'Ą': 1,
    'Ę': 1,
    'F': 1,
    'Ó': 1,
    'Ś': 1,
    'Ż': 1,
    'Ć': 1,
    'Ń': 1,
    'Ź': 1,
}


pieces = list(pieces_number.keys())


def make_bag():
    """Creates a scrabble bag for a game session"""
    return deepcopy(pieces_number)

def update_scores(room, name, score):
    """Updates the final scores of the players in a room"""
    rooms[room]['final_scores'].append(dict(name=name, score=score))

def get_player_to_play(room_id):
    """Returns the player to play next in a given room"""
    return next(rooms[room_id]['player_turns'])    

## --------------------------------------------------
## Keep cache of players' scores to prevent changing
## scores by DOM manipulation
def get_player_score(name, room_id):
    """Returns the player's score in a given room"""
    return rooms[room_id]['player_scores'].get(name)

def set_player_score(name, room_id, score):
    """Sets the player's score in a given room"""
    rooms[room_id]['player_scores'][name] = score

## ---------------------------------------------------

def get_remaining_pieces(room_id): 
    """
    Returns the number of pieces left 
    in the bag of a room
    """
    return sum(rooms[room_id]['bag'].values()) 

def get_all_pieces(room_id): 
    """
    Returns all the pieces left in the 
    bag of a room, sorted.
    """
    return sorted(rooms[room_id]['bag'].items(), key=lambda x: x[0])

def get_pieces(amount, room_id):
    """
    Gets pieces from the bag 
    and updates the bag, of course
    """
    # Storage for the requested new pieces
    new_pieces = [] 

    # Get the number of the remaining tiles
    bag_length = get_remaining_pieces(room_id)

    # If the requested amount is less than the number of
    # pieces in the bag, re-assign the amount to the remainder
    amount = bag_length if bag_length < amount else amount

    # Fill up the requested new pieces
    while len(new_pieces) != amount:
        # Get a random piece
        piece = choice(pieces)
        
        # Get items from the bag
        session_bag = rooms[room_id]['bag']

        # If the piece hasn't been exhausted
        if session_bag.get(piece) > 0:

            # Add it to the result array
            new_pieces.append(dict(letter=piece, value=pieces_weight[piece]))
            
            # Decrease the number of said piece
            session_bag[piece] -= 1   

    return new_pieces