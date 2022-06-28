# creating dataset which i need from all csv  i have one time process i already done it the dataset i need is stored in my_movies.csv
# creating dataset which i need from all csv  i have one time process i already done it the dataset i need is stored in my_movies.csv
# creating dataset which i need from all csv  i have one time process i already done it the dataset i need is stored in my_movies.csv
# creating dataset which i need from all csv  i have one time process i already done it the dataset i need is stored in my_movies.csv


from myinitial import *
from mydatabase import *


# movies1=None
# credits1=None
# keywords1=None
# with open("CSV/movies_metadata.csv", 'r', encoding='utf-8') as file:
#     movies1 = pd.read_csv(file)
# with open("CSV/credits.csv", 'r', encoding='utf-8') as file:
#     credits1 = pd.read_csv(file)
# with open("CSV/keywords.csv", 'r', encoding='utf-8') as file:
#     keywords1 = pd.read_csv(file)
# movies1['id']=movies1['id'].apply(lambda x:str(x))
# credits1['id']=credits1['id'].apply(lambda x:str(x))
# keywords1['id']=keywords1['id'].apply(lambda x:str(x))


# movies=movies1.merge(credits1, how='left', on = 'id')
# movies=movies.merge(keywords1, how='left', on = 'id')


# mymovies=movies.dropna(subset=['imdb_id','original_title',"id","poster_path"])


# # belongs_to_collection,budget,genres,id,imdb_id,original_language,original_title,overview,poster_path,release_date,tagline,title,cast,keywords, crew
# mymovies=mymovies[["id","imdb_id","original_language","original_title","overview","poster_path","release_date","belongs_to_collection","genres","budget","tagline","title","cast","keywords","crew"]]

# mymovies=mymovies.dropna(subset=['title','cast','keywords','id','imdb_id','original_title'])

# mymovies.to_csv('CSV/movies.csv')


# mymovies=mymovies[["id","imdb_id","original_language","original_title","overview","poster_path","release_date","belongs_to_collection","genres","budget","tagline","title","cast","keywords","crew"]]
# mymovies=None
# with open("CSV/movies.csv", 'r', encoding='utf-8') as file:
#     mymovies = pd.read_csv(file)

# import ast
# def convert3(obj):
#     L=[]
#     if type(obj):
#         return []
#     obj=ast.literal_eval(obj)
#     print(obj['name'])
#     L.append(obj['name'])
#     return L


# def fetch(obj):
#     L=[]
#     for i in ast.literal_eval(obj):
#         if i['job']=='Director':
#             L.append(i['name'])
#             break
#     return L
# def convert2(obj):
#     L=[]
#     c=0
#     for i in ast.literal_eval(obj):
#         if c<5:
#             L.append(i['name'])
#         else:
#             break

#         c=c+1
#     return L


# def convert(obj):
#     L=[]
#     for i in ast.literal_eval(obj):
#         L.append(i['name'])
#     return L


# mymovies['genres']=mymovies['genres'].apply(convert)
# mymovies['keywords']=mymovies['keywords'].apply(convert)
# mymovies['cast']=mymovies['cast'].apply(convert2)
# mymovies['crew']=mymovies['crew'].apply(fetch)
# mymovies.to_csv('CSV/movies.csv')
# mymovies['belongs_to_collection']=mymovies['belongs_to_collection'].apply(convert3)
# mymovies.to_csv('CSV/movies.csv')


# movies1= None
# movies2= None
# with open("CSV/movies.csv", 'r', encoding='utf-8') as file:
#     movies1 = pd.read_csv(file)
# with open("CSV/mymoviedb.csv", 'r', encoding='utf-8') as file:
#     movies2 = pd.read_csv(file)

# movies=movies2.merge(movies1, how='left', left_on = 'Title',right_on='title')
# print(movies.isnull().sum())
# movies=movies.dropna(subset=['title','crew'])
# print(movies)
# movies=movies[["Release_Date","Title","Overview","Popularity","Original_Language","Poster_Url","id","imdb_id","original_title","belongs_to_collection","Genre","tagline","cast","keywords","crew"]]
# print(movies.isnull().sum())
# movies=movies.drop_duplicates(subset="Title")
# print(movies)
# movies.to_csv('CSV/my_movies.csv')
