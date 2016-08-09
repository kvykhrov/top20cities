import json
import flask
from pymongo import MongoClient



app = flask.Flask(__name__) 

@app.route("/") 
def hello():
    client = MongoClient()
    db = client.TestDB
    coll = db.MyCollection
    result = coll.find().sort("pop",-1).limit(20)
    cities = [{'misto':x['city'],'naslnnya':x['pop']} for x in result]
    return flask.render_template("chart_bar.html", msg = cities)

@app.route("/data")
def data():
    client = MongoClient()
    db = client.TestDB
    coll = db.MyCollection
    result = coll.aggregate( [ {"$group": {"_id":"$city","naslnnia":{"$max":"$pop"}}},{"$sort":{"naslnnia":-1}},{"$limit":20}] )
    top20mista = [ {'label': x['_id'] ,'value':x['naslnnia']} for x in result ]
    return  json.dumps([ 
    {
      "key": "Cumulative Return",
      "values": top20mista
    }
  ])

if (__name__ == "__main__"):
    app.run(port = 5000)
