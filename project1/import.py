import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv

if __name__ == "__main__":
    engine = create_engine(
        "postgres://rbkoemzpycogam:383c68f0a2c2b051f6b9ae8778f41d1a09247725325e4027fa82335a756671b5@ec2-79-125-26-232.eu-west-1.compute.amazonaws.com:5432/dehvr9dets08v9")
    db = scoped_session(sessionmaker(bind=engine))
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                   {"isbn": isbn, "title": title,
                    "author": author,
                   "year": year})
        print("Added book with isbn {} author {} title {} and year {}.".format(isbn, author, title, year))
    db.commit()