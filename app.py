import keyword
from myinitial import *
from mydatabase import *


@login.user_loader
def load_user(sno):
    return userpassword_db.query.get(sno)


# TODO: login logout and signup
# TODO: login logout and signup
@app.route("/login", methods=['Get', 'Post'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = userpassword_db.query.filter_by(
            username=username, password=password).first()
        if user:
            login_user(user)
            return redirect("/")
        else:
            return render_template("login.html", message="No such user exists")

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/signup", methods=['Get', 'Post'])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user = userpassword_db.query.filter_by(username=username).first()
        if user:
            return render_template("login.html", message="username already exists")
        else:
            if password == confirm_password:
                if len(password) > 5:
                    user = userpassword_db(
                        username=username, password=password)
                    db.session.add(user)
                    db.session.commit()
                    user_object = userpassword_db.query.filter_by(
                        username=username).first()
                    login_user(user_object)
                    return redirect("/")
                return render_template("login.html", message="password length is too short")
            else:
                return render_template("login.html", message="password and confirm password are not same")

    return render_template("login.html")

# TODO: login logout and signup  end
# TODO: login logout and signup  end


# TODO transfering csv data to sqlalchemy one time process only

# with open("CSV/my_movies.csv", 'r', encoding='utf-8') as file:
#     data_df = pd.read_csv(file)
#     data_df.to_sql('movies_db', con="sqlite:///todo.db",
#                    index=True, if_exists='replace')
#     db.session.commit()

# TODO transfering csv data to sqlalchemy one time process only


# TODO: Algorithm
# TODO: Algorithm
# TODO: Algorithm
# TODO: Algorithm
movies = pd.read_sql_table("movies_db",  con="sqlite:///todo.db")


# "Release_Date","Title","Overview","Popularity","Original_Language","Poster_Url","id","imdb_id","original_title","belongs_to_collection","Genre","tagline","cast","keywords","crew"}


movies['TitleN'] = movies['Title'].apply(lambda x: str(x).split())
movies['OverviewN'] = movies['Overview'].apply(lambda x: str(x).split())
movies['taglineN'] = movies['tagline'].apply(lambda x: str(x).split())

movies['Original_LanguageN'] = movies['Original_Language'].apply(
    lambda x: str(x).split())

movies['GenreN'] = movies['Genre'].apply(lambda x: str(x).split("|"))

movies['belongs_to_collectionN'] = movies['belongs_to_collection'].apply(
    lambda x: [i.replace(" ", "") for i in ast.literal_eval(x)])

movies['castN'] = movies['cast'].apply(
    lambda x: [i.replace(" ", "") for i in ast.literal_eval(x)])

movies['keywordsN'] = movies['keywords'].apply(
    lambda x: [i.replace(" ", "") for i in ast.literal_eval(x)])

movies['crewN'] = movies['crew'].apply(
    lambda x: [i.replace(" ", "") for i in ast.literal_eval(x)])


movies['Tags'] = movies['TitleN']+movies['OverviewN']+movies['taglineN']+movies['Original_LanguageN'] + \
    movies['GenreN']+movies['belongs_to_collectionN'] + \
    movies['castN']+movies['keywordsN']+movies['crewN']
movies['Tags'] = movies['Tags'].apply(lambda x: " ".join(x))
movies['Tags'] = movies['Tags'].apply(lambda x: x.lower())

ps = PorterStemmer()


def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)


movies = movies[["index", "Release_Date", "Title", "Overview", "Popularity", "Original_Language", "Poster_Url", "id",
                 "imdb_id", "original_title", "belongs_to_collection", "Genre", "tagline", "cast", "keywords", "crew", "Tags"]]

movies['Tags'] = movies['Tags'].apply(stem)


cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['Tags']).toarray()


similarity = cosine_similarity(vectors)


def recommend(mymovie):

    distances = None
    movie_index = movies[movies['Title'] == mymovie[0].name].index[0]
    distances = similarity[movie_index]

    distances = [distances[x]*(mymovie[0].rating)
                 for x in range(len(distances))]
    if len(mymovie) > 1:
        for movie in mymovie[1:]:
            movie_index = movies[movies['Title'] == movie.name].index[0]
            distance = similarity[movie_index]

            distances = [distances[x] + distance[x] *
                         (movie.rating) for x in range(len(distances))]

    movies_list = movies
    movies_list['recomodation_score'] = movies['index'].apply(
        lambda index: distances[index])

    movies_list = movies_list.sort_values(
        by="recomodation_score", axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')

    movies_list = [movies_list.iloc[x] for x in range(len(movies_list))]
    return movies_list

# TODO: Algorithm
# TODO: Algorithm
# TODO: Algorithm
# TODO: Algorithm


# TODO: Home Page
# TODO: Home Page
# TODO: Home Page
# TODO: Home Page

@login_required
@app.route("/", methods=['Get', 'Post'])
def home():
    user_object = load_user(current_user.get_id())
    if user_object:
        username = user_object.username
        mymovies = ratings_db.query.filter_by(username=username).all()
        if mymovies:
            recomend_movies = recommend(mymovies)
        else:
            recomend_movies = movies_db.query.order_by(
                desc(movies_db.Popularity)).all()
        return render_template("home.html", username=username, movies=recomend_movies[:150])

    return render_template('login.html')

# TODO: Home Page end
# TODO: Home Page end
# TODO: Home Page end
# TODO: Home Page end


@login_required
@app.route("/yourvideos")
def myvideos():
    user_object = load_user(current_user.get_id())
    if user_object:
        username = user_object.username
        my_movies = ratings_db.query.filter_by(username=username).all()
        return render_template("myvideos.html", movies=my_movies)
    return render_template("myvideos.html", movies=[])

# TODO:: Ratings
# TODO:: Ratings
# TODO:: Ratings


@app.route("/rate/<string:type>/<string:id>")
def rate(id, type):
    user_object = load_user(current_user.get_id())
    username = user_object.username

    movie = movies_db.query.filter_by(index=id).first()
    myrating = ratings_db.query.filter_by(
        username=username, movie_index=id).first()
    if myrating:
        if myrating.type == type == "w":
            myrating.rating += 0.2
        else:
            if type == "l":
                myrating.rating = 5
                myrating.type = "l"
            else:
                myrating.rating = -1
                myrating.type = "u"
    else:
        if type == "w":
            myrating = ratings_db(username=username, rating=2,
                                  movie_index=id, type=type, name=movie.Title, Release_Date=movie.Release_Date, Overview=movie.Overview, Popularity=movie.Popularity, Original_Language=movie.Original_Language, Poster_Url=movie.Poster_Url, Genre=movie.Genre, tagline=movie.tagline, cast=movie.cast, keywords=movie.keywords, crew=movie.crew)
        elif type == "l":
            myrating = ratings_db(username=username, rating=5,
                                  movie_index=id, type=type, name=movie.Title, Release_Date=movie.Release_Date, Overview=movie.Overview, Popularity=movie.Popularity, Original_Language=movie.Original_Language, Poster_Url=movie.Poster_Url, Genre=movie.Genre, tagline=movie.tagline, cast=movie.cast, keywords=movie.keywords, crew=movie.crew)
        else:
            myrating = ratings_db(username=username, rating=-1,
                                  movie_index=id, type=type, name=movie.Title, Release_Date=movie.Release_Date, Overview=movie.Overview, Popularity=movie.Popularity, Original_Language=movie.Original_Language, Poster_Url=movie.Poster_Url, Genre=movie.Genre, tagline=movie.tagline, cast=movie.cast, keywords=movie.keywords, crew=movie.crew)
        db.session.add(myrating)
    db.session.commit()
    return f"movie {movie.Title} successfully rated"
# TODO:: Ratings
# TODO:: Ratings
# TODO:: Ratings


# TODO:: Admin
# TODO:: Admin
# TODO:: Admin
admin = Admin(app, name="data base", template_mode='bootstrap3')
admin.add_view(ModelView(userpassword_db, db.session))
admin.add_view(ModelView(movies_db, db.session))
admin.add_view(ModelView(ratings_db, db.session))

# TODO:: Admin
# TODO:: Admin
# TODO:: Admin


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
