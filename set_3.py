'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #following lists for the from_member and the to_member
    fmf = social_graph[from_member]["following"]
    tmf = social_graph[to_member]["following"]

    #follower conditions
    if to_member in fmf and from_member not in tmf:
        return "follower"
        
    #followed by conditions
    elif to_member not in fmf and from_member in tmf:
        return "followed by"
        
    #friends conditions
    elif to_member in fmf and from_member in tmf:
        return "friends"
        
    #no relationship
    else:
        return "no relationship"
    
def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
     This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #rows
    for c in range(len(board)):
        if board[c][0] != "" and all(board[c][0]==board[c][r] for r in range(len(board))):
            return board[c][0]
            
    #columns
    for r in range(len(board)):
        if board[0][r] != "" and all(board[0][r]==board[c][r] for c in range(len(board))):
            return board[0][r]
        
    #diagonal1
    if board[0][0] != "" and all(board[0][0]==board[d1][d1] for d1 in range(len(board))):
        return board[0][0]
    
    #diagonal2
    if board[0][len(board)-1] != "" and all(board[0][len(board)-1]==board[d2][len(board)-1-d2] for d2 in range(len(board))):
        return board[0][len(board)-1]
    
    #draw
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.for

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
            the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    current_stop = first_stop
    result = 0
    while current_stop!=second_stop:
        for (start_stop, end_stop) in route_map.keys():
            if start_stop==current_stop:
                result+=route_map[(start_stop, end_stop)]["travel_time_mins"]
                current_stop = end_stop
                break

    return result 
