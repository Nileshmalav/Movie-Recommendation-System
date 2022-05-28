# Recomodation-Engine-Algorithm


## to run this project in local machine

1. install python
2. install dependencies
> pip install -r requirements.txt
3. run app.py
> python app.py



# Movies-Recomodation-System Based On Content Based Recomodation/Filtering
![Screenshot (3)](https://user-images.githubusercontent.com/76725762/170815498-45a7c711-8e3b-4ab8-a07f-18fa2a251f1e.png)
![Screenshot (4)](https://user-images.githubusercontent.com/76725762/170815511-be0b5c55-e9aa-44c3-931b-7fb4b04fc152.png)



###### Note: Search is based on first 500 movies show on home page if want to include all 8000+ movies in search then remove [:500] in line no 187 in app.py
> before code 


>         return render_template("home.html", username=username, movies=recomend_movies[:500])


![Screenshot (5)](https://user-images.githubusercontent.com/76725762/170815695-d2fa38d4-3902-438d-bd67-bce73c855760.png)
 
>after code


>        return render_template("home.html", username=username, movies=recomend_movies)


![Screenshot (6)](https://user-images.githubusercontent.com/76725762/170815704-7ad81a9b-24d3-44a8-ae89-628ce2b796cd.png)
