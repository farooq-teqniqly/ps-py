class Aircraft:
    """Represents an aircraft."""

    """
    Initializes an Aircraft instance.
    
    Args:
        registration: The aircraft's registration.
        model: The aircraft's model.
        num_rows: The number of passenger seating rows.
        num_seats_per_row: The number of seats per row.
    """
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    """Gets the aircraft's registration."""
    def registration(self):
        return self._registration

    """Gets the aircraft's model."""
    def model(self):
        return self._model

    """
        Gets the aircraft's seating plan.
        
        Returns:
            A two element tuple. The first element contains a range of rows starting at 1 and the second element
            contains a string representing the seat letters.
    """
    def seating_plan(self):
        return (range(1, self._num_rows + 1)), "ABCDEFGHJK"[:self._num_seats_per_row]


class Flight:
    """Represents a flight."""

    """
        Initializes a Flight instance.

        Args:
            flight_number: The flight number.
            aircraft: The aircraft carrying out the flight.
            
        Raises:
            ValueError: If the first two flight_number characters (airline identifier) are not upper-case letters or 
            the characters after the second when converted to a number (route number) is greater than 9999.
        """
    def __init__(self, flight_number, aircraft):
        if not flight_number[:2].isalpha():
            raise ValueError(f"Invalid airline code.")

        if not flight_number[:2].isupper():
            raise ValueError(f"Invalid airline code.")

        if not (flight_number[2:].isdigit() and int(flight_number[2:]) <= 9999):
            raise ValueError(f"Invalid route number.")

        self._flight_number = flight_number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    """Gets the flight number."""
    def number(self):
        return self._flight_number

    """Gets the airline identifier portion of the flight number."""
    def airline(self):
        return self._flight_number[:2]

    """Gets the route number portion of the flight number."""
    def route_number(self):
        return self._flight_number[2:]

    """Gets the aircraft's registration."""
    def registration(self):
        return self._aircraft.registration

    """
        Assign a seat to a passenger.
        
        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.
            
        Raises:
            ValueError: The seat letter or row is invalid or the seat is already assigned.
    """
    def assign_seat(self, seat, passenger):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]

        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter '{letter}'.")

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row '{row_text}'.")

        if row not in rows:
            raise ValueError(f"Invalid row number '{row}'.")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat '{seat}' is already occupied.")

        self._seating[row][letter] = passenger

    """Returns a seat map."""
    def seat_map(self):
        for index, row in enumerate(self._seating):
            if index == 0:
                continue
            yield index, row

    """Returns the assigned seats."""
    def assigned_seats(self):
        rows, seat_letters = self._aircraft.seating_plan()

        for row in rows:
            for seat_letter in seat_letters:
                passenger = self._seating[row][seat_letter]

                if passenger is not None:
                    yield passenger, f"{row}{seat_letter}"


def get_boarding_card(passenger, seat, flight_number, aircraft):
    output = (
        f"| Name: {passenger}"
        f"  Flight: {flight_number}"
        f"  Seat: {seat}"
        f"  Aircraft: {aircraft}"
        "|")

    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    return card
