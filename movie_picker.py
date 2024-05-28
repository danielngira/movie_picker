import csv
import random


def process_file(file_name):
    try:
        movies = []
        with open(file_name, mode='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)
            for lines in csvFile:
                movies.append(lines[1])
        return movies
    except FileNotFoundError:
        print("The file was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
 

def pick_movie(movies):
    if movies:
        return random.choice(movies)
    else:
        return "No movies available to pick from."


if __name__ == "__main__":
    file_name = input("Enter the CSV file name (with extension): ")
    movies = process_file(file_name)
    suggested_movie = pick_movie(movies)
    print(f"Suggested movie: {suggested_movie}")
