from flask import Flask, request, jsonify
import pymongo
import os
from dotenv import load_dotenv
import requests

from decouple import config

myclient = pymongo.MongoClient(config("MONGODB_URL"))
mydb = myclient["JeffreysSandbox"]

mycol = mydb["RamenRating"]

myResult = mydb["Result"]

load_dotenv()
# initalize flask app
app = Flask(__name__)

@app.route('/add/setlist', methods=["POST"])
def add_setlist():
    #try:
        # get request json from flask
    req = request.get_json(force=True)
        # get concert id from request
    reviewNum = req["Review #"]
    brand = req["Brand"]
    variety = req["Variety"]
    style = req["Style"]
    country = req["Country"]
    stars = req["Stars"]

    #except:
        # error is song or concert id is not in request's json
        #return {"ERROR": "Invalid input"}

    # new setlist item consisting of a concert name, a song, a concert id from ticketmaster, number of up/downvotes
    my_setlist_item = {"Review #": reviewNum, "Brand": brand, "Variety": variety, "Style": style, "Country": country, "Stars": stars}

    # insert into koble database
    mycol.insert_one(my_setlist_item)

    return {"result": "successfully added to setlist",
            "Review #": reviewNum, "Brand": brand, "Variety": variety,
                           "Style": style, "Country": country, "Stars": stars}
    #dictToReturn = {'text': req['Brand']}
    #return(dictToReturn)

# get setlist endpoint
@app.route('/get/setlist/<reviewNum>', methods=["GET"])
def get_setlist(reviewNum):
    # from koble database's setlist collection, find document that has concert_id that matches concert_id from
    # the request's URL parameter
    # also do not return _id from document, or it will break endpoint
    setlist = mycol.find({"Review #": reviewNum}, {"_id": False})
    return {"setlist": list(setlist)}

app.run(port=5000)

