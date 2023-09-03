import pymongo
from decouple import config
myclient = pymongo.MongoClient(config("MONGODB_URL"))
mydb = myclient["JeffreysSandbox"]

mycol = mydb["RamenRating"]

myResult = mydb["Result"]

print("Welcome to ramen recommender! Answer some questions to find your Ramen! Or write your own review!")

print("add review: 1")
print("find top 3 reviews: 2")
add_R = input("Pick 1 or 2:")

if add_R == "1":
    addDict = {}


    myquery = {}
    isunqiue=0


    #first find latest review #
    myquery["Review #"] = str(int(mycol.find_one().get("Review #")))
    while (isunqiue != 1):
        isunqiue=1

        mydoc = mycol.find(myquery)
        for x in mydoc:
            if x.get("Review #") == myquery["Review #"]:
                isunqiue=0
                myquery["Review #"] = str(int(myquery["Review #"]) + 1)





    addDict["Review #"] = myquery["Review #"]
    print(addDict)
    brand = input("What brand is your ramen?")
    addDict["Brand"] = brand
    variety = input("What is kind of variety (name) is your ramen?")
    addDict["Variety"] = variety
    style = input("What is the style of your ramen?(cup, pack, bowl, etc)")
    addDict["Style"] = style
    country = input("What country is your ramen from?")
    addDict["Country"] = country
    stars = input("What is your rating?")
    addDict["Stars"]=stars
    comments = input("You can add your own comments, but it will not be saved.")

    print(addDict)

    mycol.insert_one(addDict)

if add_R == "2":
    Style = input("What style do you like your Ramen? (Pack/Cup/Box/Bowl)")

    #ask some questions to filter out suggestions
    prefBrand = input("Do you have a preferred brand? (yes/no)")
    brand = "no"
    if (prefBrand == "yes"):
        Brand = input("what is it?")


    ratingMin = input("what is your minimum star rating? (From 1 to 5)")

    ratingMax = input("what is your maximum star rating? (From 1 to 5)")


    country = input("what country would you prefer your ramen from? (e.g. Japan, USA)")

    Top3 = 0
    print("Here are our 3 choices of Ramen for you:")
    if brand=="no":
        for rate in mycol.find({"Stars": {"$gte": ratingMin},
                                  "Stars": {"$lte": ratingMax},
                                  "Style": Style,
                                  "Country":country} ).sort("Stars", pymongo.DESCENDING):#Give Highest rating ones
            if Top3 < 3:
                Top3 = Top3 + 1
                print("Brand:" + rate.get('Brand'))
                print(rate.get('Variety'))
                print("Rating:" + rate.get('Stars'))

    if brand=="yes":
        for rate in mycol.find({"Stars": {"$gte": ratingMin},
                          "Stars": {"$lte": ratingMax},
                          "Style": Style,
                          "Country":country,
                          "Brand":Brand}).sort("Stars", pymongo.DESCENDING):
            if Top3 < 3:
                Top3 = Top3 + 1
                print(rate.get('Variety'))
                print("Rating:" + rate.get('Stars'))



#print(mydb.list_collection_names())

