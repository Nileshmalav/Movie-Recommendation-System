# Recomodation-Engine-Algorithm


## to run this project in local machine

1. install python
2. install dependencies
> pip install -r requirements.txt
3. run app.py
> python app.py



# Movies-Recomodation-System Based On Content Based Recomodation/Filtering
![Screenshot (3)](https://user-images.githubusercontent.com/76725762/170815498-45a7c711-8e3b-4ab8-a07f-18fa2a251f1e.png)

#

![Screenshot (17)](https://user-images.githubusercontent.com/76725762/170856432-1999e8be-54f3-41a0-bd6d-9f98805564b9.png)

#

![Screenshot (16)](https://user-images.githubusercontent.com/76725762/170856437-7c3957a5-0f55-45d8-813f-6a1b69b46d00.png)

#

![Screenshot (4)](https://user-images.githubusercontent.com/76725762/170815511-be0b5c55-e9aa-44c3-931b-7fb4b04fc152.png)



## Note: Search is based on first 500 movies show on home page if want to include all 8000+ movies in search then remove [:500] in line no 206 in app.py
> before code 


>         return render_template("home.html", username=username, movies=recomend_movies[:500])


![Screenshot (12)](https://user-images.githubusercontent.com/76725762/170856383-19d1a46b-2444-4c64-97af-4a59795e9ac6.png)

 
>after code


>        return render_template("home.html", username=username, movies=recomend_movies)


![Screenshot (13)](https://user-images.githubusercontent.com/76725762/170856388-162aebfd-bbf5-47e2-9bca-ec54db0137ed.png)



#

![Screenshot (18)](https://user-images.githubusercontent.com/76725762/170856491-c3f1535c-c0f9-4e35-a469-207e991b9da0.png)



# Movie Recommendation based on user likes and dislikes , watched and watched again
![Screenshot (19)](https://user-images.githubusercontent.com/76725762/170856542-68c264dc-d3ab-4f49-94ef-894ca4106463.png)
