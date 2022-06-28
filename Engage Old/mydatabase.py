# database flask sql alchemy tables/classes
# database flask sql alchemy tables/classes
from myinitial import *

# for storing username and password username is unique and used for user identification


class userpassword_db(UserMixin, db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def get_id(self):
        return self.sno


# movies database used for getting recommodation
class movies_db(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    Release_Date = db.Column(db.Text)
    Title = db.Column(db.Text)
    Overview = db.Column(db.Text)
    Popularity = db.Column(db.Text)
    Original_Language = db.Column(db.Text)
    Poster_Url = db.Column(db.Text)
    id = db.Column(db.Text)
    imdb_id = db.Column(db.Text)
    original_title = db.Column(db.Text)
    belongs_to_collection = db.Column(db.Text)
    Genre = db.Column(db.Text)
    tagline = db.Column(db.Text)
    cast = db.Column(db.Text)
    keywords = db.Column(db.Text)
    crew = db.Column(db.Text)


# user ratings used for recomodation
class ratings_db(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)

    # used for getting movie information from database
    movie_index = db.Column(db.Integer)
    name = db.Column(db.Text)  # movie name

    type = db.Column(db.Text)  # w for watched l for liked u for unliked
    # rating default -1 for unlike 2 for watched 5 for liked and +0.2 for watched again
    rating = db.Column(db.Float, default=0)

    Release_Date = db.Column(db.Text)
    Overview = db.Column(db.Text)
    Popularity = db.Column(db.Text)
    Original_Language = db.Column(db.Text)
    Poster_Url = db.Column(db.Text)

    Genre = db.Column(db.Text)
    tagline = db.Column(db.Text)
    cast = db.Column(db.Text)
    keywords = db.Column(db.Text)
    crew = db.Column(db.Text)
