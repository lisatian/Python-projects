PIECES_PER_WORKER_6_TO_10 = 30
PIECES_PER_WORKER_10_TO_14 = 40
PIECES_PER_WORKER_14_T0_18 = 35
NO_PRODUCTION = 0


def pieces_produced(hour, workers):
    """
    -------------------------------------------------------
    Given the hour of the day and the number of workers,
    this function calculates and returns the total number
    of pieces produced in that hour.
    Use: total_pieces = pieces_produced(hour, workers)
    -------------------------------------------------------
    Preconditions:
        hour - hour of the day in twenty-four hour format (int)
        workers - number of workers (int >= 0)
    Postconditions:
        returns
        total_pieces - total number of pieces produced during that hour (int >= 0),
        or an error message for invalid hour if the hour isn't between 0 and 23 (str)
    -------------------------------------------------------
    """

    if 0 <= hour <= 23:
        if 6 <= hour < 10:
            total_pieces = workers * PIECES_PER_WORKER_6_TO_10
        elif 10 <= hour < 14:
            total_pieces = workers * PIECES_PER_WORKER_10_TO_14
        elif 14 <= hour < 18:
            total_pieces = workers * PIECES_PER_WORKER_14_T0_18
        else:
            total_pieces = workers * NO_PRODUCTION
    else:
        total_pieces = "Invalid hour"

    return total_pieces
