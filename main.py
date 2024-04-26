import sqlite3
from openpyxl import Workbook


connection = sqlite3.connect('database.db')

cursor = connection.cursor()

# def create_table():
#     cursor.execute('CREATE TABLE IF NOT EXISTS cinema (id INTEGER PRIMARY KEY, name TEXT, address TEXT)')
#     cursor.execute('CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, year INTEGER,  description TEXT, rating REAL)')
#     cursor.execute('CREATE TABLE IF NOT EXISTS afisha (id INTEGER PRIMARY KEY, movie_id INTEGER, cinema_id INTEGER, price INTEGER, date DATE, time TIME, capacity INTEGER)')
#     cursor.execute('CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY KEY, afisha_id INTEGER, room INTEGER, row INTEGER, seat INTEGER)')
#     cursor.execute('CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, place_id INTEGER)')

# create_table()




class Order:
    def __init__(self, cinema, customer_name, movie, year, genre, seat, number_of_tickets, price):
        self.cinema = cinema
        self.customer_name = customer_name
        self.movie = movie
        self.year = year
        self.genre = genre
        self.number_of_tickets = number_of_tickets
        self.seat = seat
        self.price = price
    
    def get_customer_name(self):
        self.customer_name = input("Enter your name")
    
    def choose_cinema():
        cinema = int(input("Select a cinema (1-5)\n\n1. Arman\n2. Chaplin cinemas\n3. Kinopark\n4. Eurasia Cinema 7\n5. Arsenal\n\n"))

    
    
    def choose_movie():
        try:
            genre = int(input("Enter film genre (1-9)\n\n1. Drama\n2. Crime\n3. Action\n4. Biography\n5. Adventure\n6. Animation\n7. Comedy\n8. Horror\n9. Mystery\n\n"))
            if genre == 1:
                drama_movies = "select name from movie where genre = 'Drama'"
                for index, drama_movie in enumerate(cursor.execute(drama_movies)):
                    print(index + 1, drama_movie)
                cursor.execute(drama_movies)
                drama_movies_choice = "Select a number between (1-27)"
                drama_movie_choice = f"select name from movie where id == {drama_movies_choice}"
                connection.commit()
            elif genre == 2:
                crime_movies = "select name from movie where genre == 'Crime'"
                for index, crime_movie in enumerate(cursor.execute(crime_movies)):
                    print(index + 1, crime_movie)
                cursor.execute(crime_movies)
                crime_movies_choice = "Select a number between (1-17)"
                crime_movie_choice = f"select name from movie where id == {crime_movies_choice}"
                connection.commit()
            elif genre == 3:
                action_movies = "select name from movie where genre == 'Action'"
                for index, action_movie in enumerate(cursor.execute(action_movies)):
                    print(index + 1, action_movie)
                cursor.execute(action_movies)
                action_movies_choice = "Select a number between (1-20)"
                action_movie_choice = f"select name from movie where id == {action_movies_choice}"
                connection.commit()
            elif genre == 4:
                biography_movies = "select name from movie where genre == 'Biography'"
                for index, biography_movie in enumerate(cursor.execute(biography_movies)):
                    print(index + 1, biography_movie)
                cursor.execute(biography_movies)
                biography_movies_choice = "Select a number between (1-7)"
                biography_movie_choice = f"select name from movie where id == {biography_movies_choice}"
                connection.commit()
            elif genre == 5:
                adventure_movies = "select name from movie where genre == 'Adventure'"
                for index, adventure_movie in enumerate(cursor.execute(adventure_movies)):
                    print(index + 1, adventure_movie)
                cursor.execute(adventure_movies)
                adventure_movies_choice = "Select a number between (1-6)"
                adventure_movie_choice = f"select name from movie where id == {adventure_movies_choice}"
                connection.commit()
            elif genre == 6:
                animation_movies = "select name from movie where genre == 'Animation'"
                for index, animation_movie in enumerate(cursor.execute(animation_movies)):
                    print(index + 1, animation_movie)
                cursor.execute(animation_movies)
                animation_movies_choice = "Select a number between (1-11)"
                animation_movie_choice = f"select name from movie where id == {animation_movies_choice}"
                connection.commit()
            elif genre == 7:
                comedy_movies = "select name from movie where genre == 'Comedy'"
                for index, comedy_movie in enumerate(cursor.execute(comedy_movies)):
                    print(index + 1, comedy_movie)
                cursor.execute(comedy_movies)
                comedy_movies_choice = "Select a number between (1-7)"
                comedy_movie_choice = f"select name from movie where id == {comedy_movies_choice}"
                connection.commit()
            elif genre == 8:
                horror_movies = "select name from movie where genre == 'Horror'"
                for index, horror_movie in enumerate(cursor.execute(horror_movies)):
                    print(index + 1, horror_movie)
                cursor.execute(horror_movies)
                horror_movies_choice = "Select a number between (1-2)"
                horror_movie_choice = f"select name from movie where id == {horror_movies_choice}"
                connection.commit()
            elif genre == 9:
                mystery_movies = "select name from movie where genre == 'Mystery'"
                for index, mystery_movie in enumerate(cursor.execute(mystery_movies)):
                    print(index + 1, mystery_movie)
                cursor.execute(mystery_movies)
                mystery_movies_choice = "Select a number between (1-2)"
                mystery_movie_choice = f"select name from movie where id == {mystery_movies_choice}"
                connection.commit()   
            else:
                print("Couldn`t find a number")
        except ValueError:
            print("Enter a correct number")   
  
        
              
    def choose_place():
        select_room = "select room from place ORDER BY RANDOM()"
        room = cursor.execute(select_room)
        room = cursor.fetchone()

        select_row = "select row from place ORDER BY RANDOM()"
        row = cursor.execute(select_row)
        row = cursor.fetchone()
        
        select_seat = "select seat from place ORDER BY RANDOM()"
        seat = cursor.execute(select_seat)
        seat = cursor.fetchone()
        
        connection.commit()
     

        
    def payment():
        type_of_ticket = input("Select type of ticket\n\n1. Child\n2. Student\n3. Adult")
        try:
            if type_of_ticket == 1:
                child_ticket_price = "select price from afisha where id = 18"
            elif type_of_ticket == 2:
                student_ticket_price = "select price from afisha where id = 27"
            elif type_of_ticket == 3:
                adult_ticket_price = "select price from afisha where id = 7"
        except ValueError:
            print("Choose a number between (1-3)")
            
        
        
        
        
    def save_order(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet['A1'] = self.customer_name
        sheet['B1'] = self.movie
        sheet['C1'] = self.genre
        sheet['D1'] = self.year
        sheet['E1'] = self.number_of_tickets
        sheet['F1'] = self.seat
        sheet['G1'] = self.price
        
    
order = Order
order.get_customer_name()
order.choose_cinema()
order.choose_movie()
order.choose_place()
order.payment()
order.save_order()