import pymongo

myclient = pymongo.MongoClient("Probably shouldn't show this")
mydb = myclient["JeffreysSandbox"]

mycol = mydb["RamenRating"]

myResult = mydb["Result"]

print("Welcome to ramen recommender! Answer some questions to find your Ramen!")

Style = input("What style do you like your Ramen? (Pack/Cup/Box/Bowl)")

#ask some questions to filter out suggestions
prefBrand = input("Do you have a preferred brand? (yes/no)")
brand = "no"
if (prefBrand == "yes"):
  brand = input("what is it?")


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
      print(rate.get('Variety'))
      print("Rating:" + rate.get('Stars'))

if brand=="yes":
  for rate in mycol.find({"Stars": {"$gte": ratingMin},
                          "Stars": {"$lte": ratingMax},
                          "Style": Style,
                          "Country":country,
                          "Brand":brand}).sort("Stars", pymongo.DESCENDING):
    if Top3 < 3:
      Top3 = Top3 + 1
      print(rate.get('Variety'))
      print("Rating:" + rate.get('Stars'))



#print(mydb.list_collection_names())