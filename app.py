import json
from flask import Flask, request
import numpy as np

#routing API endpoints
app = Flask(__name__)

#list of locations
locations = [
    "Dallas", "San Francisco", "Patterson", "Wichita"
]

#list of plans
plans = [

]

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
    'Cost': [insert num here],
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. However, since you chose to protect "
                   "your home with wilfire insurance, your insurance will help pay [insert amount here] in repair costs, "
                   "leaving you with [insert num here] to pay out of pocket. The intended amount to fully repair the damages was "
                   "[insert num here]."
}

notCoveredWildfire = {
    'Cost': [insert num here],
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. Unfortunately, since you did "
                   "not end up choosing to cover your house with wildfire insurance, you have to end up paying for all the "
                   "damages out of pocket. The total cost of the damages ended up being [insert num here]."
}

insuranceHurricane = {
    'Cost': [insert num here],
    'Description': "Oh no! Weather condiitions were really bad and the perfect conditions were created for the perfect hurricane storm! "
                   "Your house suffered major roof damage as a result. Thankfully, since you opted into hurricane insurance to cover, "
                   "your insurance will cover [insert num here], so you will in turn only have to pay [insert num here] out of pocket. "
                   "The total cost for repairs was [insert num here]."
}

notCoveredHurricane = {
    'Cost': [insert num here],
    'Description': "Oh no! Weather condiitions were really bad and the perfect conditions were created for the perfect hurricane storm! "
                   "Your house suffered major roof damage as a result. However, since you did not opt to cover in your insurance for "
                   "hurricane damage, you have to pay all the damages out of pocket, which totals [insert num here]."
}

insuranceFlood = {
    'Cost': [insert num here],
    'Description': "Bad news! It rained so much on one day to cause a major flash flood, and your house suffered internal pipe damages "
                   "as a result. Fortunately, you chose to include flood coverage in your insurance plan, which will help cover "
                   "[insert num here], totaling only [insert num here] to be paid out of pocket. The total cost of damages was "
                   "[insert num here]."
}

notCoveredFlood = {
    'Cost': [insert num here],
    'Description': "Bad news! It rained so much on one day to cause a major flash flood, and your house suffered internal pipe damages "
                   "as a result. Sadly, you did not opt in your plan for flooding insurance, causing you to have to pay for all "
                   "damages out of pocket, which totals [insert num here]."
}

safe = {
    'Cost': 0,
    'Description': "You are safe...for now...!"
}

error404 = {
    '404': "Error 404, page not found."
}

#determine probabilities in a list
probEarthquake, probFlood, probHurricane, probWildfire, total = 0.0
probList = []

def probability(currentLocation):

    if currentLocation in locations:
        if currentLocation == "Dallas":
            probEarthquake = 0.25
            probFlood = 0.05
            probHurricane = 0.02
            probWildfire = 0.15
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
        elif currentLocation == "San Francisco":
            probEarthquake = 0.05
            probFlood = 0.25
            probHurricane = 0.10
            probWildfire = 0.02
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
        elif currentLocation == "Patterson":
            probEarthquake = 0.05
            probFlood = 0.15
            probHurricane = 0.25
            probWildfire = 0.02
            total = 1.0 - (probWildfire + probHurricane + probFlood + probEarthquake)
        elif currentLocation == "Wichita":
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


@app.route("/explain", methods=['GET'])
def explain():
    if request.method == 'GET':
        return json.dumps(introAndAbout)
    else:
        return json.dumps(error404)

@app.route("/plans", methods=['GET'])
def plans():
    return #insert json.dumps, check for error404

@app.route("/results/<location>/<plan>", methods=['GET'])
def results(location, plan):
    currPlan = plan
    currLocation = location
    if request.method == 'GET':
        numChose = np.random.choice(np.arrange(1, 6), p=probability(currLocation))
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
        return json.dumps(error404)

if __name__ == "__main__":
    app.run()





