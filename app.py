import json
from flask import Flask, request
import numpy as np

#open json object
file = open("[name].json")
data = json.load(file)

#list of locations
locations = [
    "[name1]", "[name2]", "[name3]", "[name4]"
]

#gather current location and insurance plan from the json object
currentLocation = data["Location"]
currPlan = data["Insurance"]

#Dictionaries to send back to front-end
introAndAbout = {
    'Introduction': "Hi, welcome to [insert name here]. The goal of this game is to create an insurance plan and avoid the obstacles throughout the game. There" 
              " will be obstacles throughout the course of the game and the goal is to get the best net balance from "
              "the game possible. There will be 10 years to go through the game and each year may have an obstacle "
              "that might hinder you. Try your best to get through the game with the least amount of money to pay! "
              "Good luck!"
}

insuranceEarthquake = {
    'Cost': 5500,
    'Description': "There was a devastating earthquake in your area and it caused the hanging items in your house, "
                   "damaging the walls and the floors of your house.",
    'Result'     : "Luckily, you decided to get the earthquake coverage in addition to your plan, and that turned out "
                   "to be a good idea, since now your insurance will cover $3,000 in repair costs. The amount of money that "
                   "you needed to repair the damages in the house was $8,500, so you ended up paying $5,500 out of pocket. Good job!"
}

notCoveredEarthquake = {
    'Cost': 8500,
    'Description': "There was a devastating earthquake in your area and it caused the hanging items in your house, "
                   "damaging the walls and the floors of your house.",
    'Result'     : "Sadly, you decided to not get the earthquake coverage in addition to your plan, and that turned out "
                   "to be a risky bet which backfired. The amount of money that you need to repair the damages in the "
                   "house was $8,500, which you have to pay out of pocket. "
}

insuranceWildfire = {
    'Cost': 2500,
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. However, since you chose to protect "
                   "your home with wilfire insurance, your insurance will help pay [insert amount here] in repair costs, "
                   "leaving you with [insert num here] to pay out of pocket. The intended amount to fully repair the damages was "
                   "[insert num here]."
}

notCoveredWildfire = {
    'Cost': 3000,
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. Unfortunately, since you did "
                   "not end up choosing to cover your house with wildfire insurance, you have to end up paying for all the "
                   "damages out of pocket. The total cost of the damages ended up being [insert num here]."
}

insuranceHurricane = {
    'Cost': 6000,
    'Description': "Oh no! Weather condiitions were really bad and the perfect conditions were created for the perfect hurricane storm! "
                   "Your house suffered major roof damage as a result. Thankfully, since you opted into hurricane insurance to cover, "
                   "your insurance will cover [insert num here], so you will in turn only have to pay [insert num here] out of pocket. "
                   "The total cost for repairs was [insert num here]."
}

notCoveredHurricane = {
    'Cost': 7000,
    'Description': "Hello world"
}

insuranceFlood = {
    'Cost': 8000,
    'Description': "This happened blah blah blah"
}

notCoveredFlood = {
    'Cost': 1500,
    'Description': "This happened blah blah blah"
}

safe = {
    'Cost': 0,
    'Description': "You are safe for this time mwhahahahhahhahahahhaahah!"
}

#determine probabilities in a list
probEarthquake, probFlood, probHurricane, probWildfire, total = 0.0
probList = []

def probability():

    if currentLocation in locations:
        if currentLocation == "[name1]":
            probEarthquake = 0.25
            probFlood = 0.05
            probHurricane = 0.02
            probWildfire = 0.15
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
        elif currentLocation == "[name2]":
            probEarthquake = 0.05
            probFlood = 0.25
            probHurricane = 0.10
            probWildfire = 0.02
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
        elif currentLocation == "[name3]":
            probEarthquake = 0.05
            probFlood = 0.15
            probHurricane = 0.25
            probWildfire = 0.02
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
        elif currentLocation == "[name4]":
            probEarthquake = 0.15
            probFlood = 0.02
            probHurricane = 0.05
            probWildfire = 0.25
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
    else:
        print("Invalid Location")



    probList.append(total)
    probList.append(probEarthquake)
    probList.append(probFlood)
    probList.append(probHurricane)
    probList.append(probWildfire)
    return probList


#routing API endpoints
app = Flask(__name__)

@app.route("/explain", methods=['GET'])
def explain():
    if request.method == 'GET':
        return json.dumps(introAndAbout)
    else:
        return #error 404

@app.route("/results", methods=['GET'])
def results():
    if request.method == 'GET':
        numChose = np.random.choice(np.arrange(1, 6), p=probability())
        if numChose == 1:
            return json.dumps(safe)
        if numChose == 2:
            if "Earthquake" in currPlan:
                return json.dumps(insuranceEarthquake)
            else:
                return json.dumps(notCoveredEarthquake)
        if numChose == 3:
            if "Flood" in currPlan:
                return json.dumps(insuranceFlood)
            else:
                return json.dumps(notCoveredFlood)
        if numChose == 4:
            if "Hurricane" in currPlan:
                return json.dumps(insuranceHurricane)
            else:
                return json.dumps(notCoveredHurricane)
        if numChose == 5:
            if "Wildfire" in currPlan:
                return json.dumps(insuranceWildfire)
            else:
                return json.dumps(notCoveredWildfire)
    else:
        return #error 404

if __name__ == "__main__":
    app.run()
