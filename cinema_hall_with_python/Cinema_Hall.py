class Star_Cinema:
    hall_list = []

    @classmethod
    def hall_entry(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        super().__init__()

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.show_list.append(show)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seat(self, id, seat_list):
        if id not in self.seats:
            raise ValueError(f'Invalid Show ID : {id}')
        for row, col in seat_list:
            if row >= self.rows and col >= self.cols:
                raise ValueError(f'There is no row and col with this value ({row},{col}).')
            if self.seats[id][row][col] == 1:
                raise ValueError(f'Seat : ({row},{col}) is already booked')
            self.seats[id][row][col] = 1

    def view_show_list(self):
        for show in self.show_list:
            print(f'Show ID : {show[0]}, Movie name : {show[1]}, Time : {show[2]}')

    def available_seats(self, id):
        if id not in self.seats:
            raise ValueError(f'Invalid ID : {id}')
        print(f'Available seats for show {id} :')
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 0:
                    print(f'({row}, {col})', end=' ')
            print()


star = Star_Cinema()

cineplex = Hall(5, 6, 100)
cineplex.entry_show(101, 'Toofan', '7:00')
cineplex.entry_show(102, 'Ghore baire', '12:00')
cineplex.entry_show(103, 'Dekha hobe pore', '4:00')
cineplex.view_show_list()
cineplex.book_seat(101, [(1, 1), (3, 3), (4, 4)])
cineplex.available_seats(101)