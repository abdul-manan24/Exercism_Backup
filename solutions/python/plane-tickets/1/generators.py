"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    seat_letters = ["A", "B", "C", "D"]
    current_index = 0
    current_iter = 0

    while current_iter < number:
        yield seat_letters[current_index]
        if current_index == 3:
            current_index = 0
        else:
            current_index += 1
        current_iter += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    current_row = 0
    current_iter = 0
    seat_letter = generate_seat_letters(number)
    
    while current_iter < number:
        current_letter = next(seat_letter)
        if current_letter == "A":
            current_row += 1

        if current_row == 13:
            current_row += 1
            
        yield f'{current_row}{current_letter}'
        current_iter += 1
        


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    passenger_seats = {}
    seats = generate_seats(len(passengers))

    for passenger in passengers:
        passenger_seats[passenger] = next(seats)

    return passenger_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        ticket_id = seat_number + flight_id
        trailing_zeros = 12 - len(ticket_id)
        ticket_id = ticket_id + "0" * trailing_zeros
        yield ticket_id
