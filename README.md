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

![Screenshot (7)](https://user-images.githubusercontent.com/76725762/170815933-9a0aa00a-ef0f-4bf3-9f70-0f5f4fc385b2.png)

#

![Screenshot (8)](https://user-images.githubusercontent.com/76725762/170815942-993afea1-2140-4a24-ac9c-42004b18b99d.png)

#

![Screenshot (4)](https://user-images.githubusercontent.com/76725762/170815511-be0b5c55-e9aa-44c3-931b-7fb4b04fc152.png)



###### Note: Search is based on first 500 movies show on home page if want to include all 8000+ movies in search then remove [:500] in line no 206 in app.py
> before code 


>         return render_template("home.html", username=username, movies=recomend_movies[:500])


![Screenshot (9)](https://user-images.githubusercontent.com/76725762/170824725-e6efe3c9-bb3d-4930-a16b-d9469e2495fc.png)

 
>after code


>        return render_template("home.html", username=username, movies=recomend_movies)


![Screenshot (10)](https://user-images.githubusercontent.com/76725762/170824731-8c9990ac-5897-435d-a665-7f45368a54db.png)

