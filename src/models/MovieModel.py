from database.db import get_connection
from .entities.Movie import Movie

class MovieModel():

    @classmethod #static method
    def get_movies(self):
        try:
            connection = get_connection()
            movies = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT id, title, duration, released FROM movie ORDER BY title ASC')
                resultset = cursor.fetchall()

                for row in resultset:
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())

            connection.close()
            print(movies)
            return movies
        except Exception as ex:
            raise Exception(ex)

    @classmethod #static method
    def get_movie(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, title, duration, released FROM movie WHERE id = %s', (id,))
                row = cursor.fetchone()

                movie = None
                if row != None:
                    movie = Movie(row[0],row[1],row[2],row[3])
                    movie = movie.to_JSON()

            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)


    @classmethod #static method
    def add_movie(self, movie):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO movie (id, title, duration, released)
                VALUES(%s, %s, %s, %s)""", (movie.id, movie.title, movie.duration, movie.released))
            affected_rows = cursor.rowcount()
            connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)