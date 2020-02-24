# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:28:40 2020

@author: tatan
"""

from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/graficas")
def graficos():
     ww=plt.hist(dataRts1)
     yy=plt.eventplot(datalikes)
     ww = []
     yy = []
     return render_template("graficos.html", ww = ww, yy =yy)
    


@app.route("/about")
def about():
    b1, b2, b3, b4, b5,  b6, b7, b11, b12, b13, b14, b15, b16,
    return render_template("about.html",b1=b1, b2=b2, b3=b3, b4=b4,
                           b5=b5, b6=b6, b7=b7,b11=b11,b12=b12,b13=b13,b14=b14,b15=b15,
                           b16=b16)

@app.route("/nike")
def nike():
    a1, a2, a3, a4, a5,  a6, a7, a11, a12, a13, a14, a15, a16
    return render_template("nike.html",a1=a1, a2=a2, a3=a3,
                           a4=a4, a5=a5, a6=a6, a7=a7,a11=a11,a12=a12,a13=a13,a14=a14,
                           a15=a15,a16=a16)
 
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


import tweepy
import io
import numpy as np
import pandas as pd
import statistics as st
from IPython.display import display
from matplotlib import pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.backends.backend_agg import FigureCanvasAgg

#Accesos para la base de datos de twitter
consumer_key="mXYfGhRG7j9s3vOnKlgoFHXH3"
consumer_secret="O35JsGB2nHZsYqA0mx7ph2GAMwBKSwTqbVPlwDYglrUpE1Z15h"
access_token = "1519510435-iS5JJQQsFt6lRbw8gAS5OBvINIWHcqWtbyhyDC8"
access_token_secret="tyK0BR9oT5EtuYFHOMtHH9wgdQFsNeC9niN1mrB6JWUzA"

#configuramos y autenticamos
def twitter_setup():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)    
    api = tweepy.API(auth)
    return api

#Creamos una variable para extraer datos
extra= twitter_setup()
#Creamos una lista con la informacion extraida
Tweets =extra.user_timeline(screen_name="nike",count=200)
print("num" , format(len(Tweets)))

for tweet in Tweets[:5]:
    muestra=tweet.text
#creamos un dataframe con la informacion
data=pd.DataFrame(data=[tweet.text for tweet in Tweets],columns=['Tweets'])    
display(data.head(10))

#Llamamos los datos del primet twet
print(dir(Tweets[0]))
print(Tweets[0].id)
print(Tweets[0].created_at)
print(Tweets[0].source)
print(Tweets[0].favorite_count)
print(Tweets[0].retweet_count)
print(Tweets[0].geo)
print(Tweets[0].coordinates)
print(Tweets[0].entities)

#unimos los datos importantes a la base de datos
data['Longitud']= np.array([len(tweet.text)for tweet in Tweets])
data['ID']= np.array([tweet.id for tweet in Tweets])
data['Fecha']= np.array([tweet.created_at for tweet in Tweets])
data['Fuente']= np.array([tweet.source for tweet in Tweets])
data['Likes']= np.array([tweet.favorite_count for tweet in Tweets])
data['RTs']= np.array([tweet.retweet_count for tweet in Tweets])


display(data.head(10))


datalikes=data["Likes"]
dataRts=data["RTs"]

a1=np.corrcoef(datalikes,dataRts)
a2=st.mean(datalikes)
a3=st.median(datalikes)
a4=st.mode(datalikes)
a5=np.std(datalikes)
a6=st.pvariance(datalikes)
a7=st.variance(datalikes)

a11=st.mean(dataRts)
a12=st.median(dataRts)
a13=st.mode(dataRts)
a14=np.std(dataRts)
a15=st.pvariance(dataRts)
a16=st.variance(dataRts)

plt.hist(datalikes)
plt.title("Histograma datalikes")
plt.show()

plt.hist(dataRts)
plt.title("Histograma dataRts")
plt.show()

plt.scatter(datalikes, dataRts,c="g", alpha=1, marker=r'$\clubsuit$',
            label="Luck")
plt.xlabel("datalikes")
plt.ylabel("dataRts")
plt.legend(loc='upper left')
plt.show()


plt.eventplot(datalikes)
plt.plot(datalikes)



##Realizamos lo mismo ahora para adidas


Tweets1 =extra.user_timeline(screen_name="adidas",count=200)
print("num" , format(len(Tweets1)))

for tweet in Tweets1[:5]:
    print(tweet.text)
    print()
#creamos un dataframe con la informacion
data1=pd.DataFrame(data=[tweet.text for tweet in Tweets1],columns=['Tweets1'])    
display(data1.head(10))

#Llamamos los datos del primet tweet
print(dir(Tweets1[0]))
print(Tweets1[0].id)
print(Tweets1[0].created_at)
print(Tweets1[0].source)
print(Tweets1[0].favorite_count)
print(Tweets1[0].retweet_count)
print(Tweets1[0].geo)
print(Tweets1[0].coordinates)
print(Tweets1[0].entities)

#unimos los datos importantes a la base de datos
data1['Longitud']= np.array([len(tweet.text)for tweet in Tweets1])
data1['ID']= np.array([tweet.id for tweet in Tweets1])
data1['Fecha']= np.array([tweet.created_at for tweet in Tweets1])
data1['Fuente']= np.array([tweet.source for tweet in Tweets1])
data1['Likes']= np.array([tweet.favorite_count for tweet in Tweets1])
data1['RTs']= np.array([tweet.retweet_count for tweet in Tweets1])


display(data1.head(10))


datalikes1=data1["Likes"]
dataRts1=data1["RTs"]

b1=np.corrcoef(datalikes1,dataRts1)
b2=st.mean(datalikes1)
b3=st.median(datalikes1)
b4=st.mode(datalikes1)
b5=np.std(datalikes1)
b6=st.pvariance(datalikes1)
b7=st.variance(datalikes1)
b11=st.mean(dataRts1)
b12=st.median(dataRts1)
b13=st.mode(dataRts1)
b14=np.std(dataRts1)
b15=st.pvariance(dataRts1)
b16=st.variance(dataRts1)

u1=plt.hist(datalikes1)
plt.title("Histograma datalikes1")
plt.show()
plt.hist(dataRts1)
plt.title("Histograma dataRts1")
plt.show()
plt.boxplot(datalikes1)
plt.scatter(datalikes1, dataRts1,c="g", alpha=1, marker=r'$\clubsuit$',
            label="Luck")
plt.xlabel("datalikes1")
plt.ylabel("dataRts1")
plt.legend(loc='upper left')
plt.show()
plt.eventplot(datalikes1)
plt.plot(datalikes1)


np.corrcoef(datalikes,datalikes1)
plt.scatter(datalikes, datalikes1,c="g", alpha=1, marker=r'$\clubsuit$',
            label="Luck")
plt.xlabel("datalikes")
plt.ylabel("datalikes1")
plt.legend(loc='upper left')





ind = np.arange(200)    
width = 0.35       

p1 = plt.bar(ind, datalikes, width, yerr=dataRts1)
p2 = plt.bar(ind, datalikes1, width,
             bottom=dataRts, yerr=dataRts)

plt.ylabel('Likes')
plt.title('Comparacion de likes entre nike y adidas')
plt.legend((p1[0], p2[0]), ('Datalikes', 'Datalikes1'))
plt.show()



    