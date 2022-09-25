import json
from flask import Flask, request
import numpy as np

#routing API endpoints
app = Flask(__name__)

#list of locations
locations = [
    "Dallas", "San Francisco", "Patterson", "Wichita"
]


#Dictionaries to send back to front-end
introAndAbout = {
    'Introduction': "Hi, welcome to [insert name here]. The goal of this game is to create an insurance plan and avoid the obstacles throughout the game. There" 
              " will be obstacles throughout the course of the game and the goal is to get the best net balance from "
              "the game possible. There will be 10 years to go through the game and each year may have an obstacle "
              "that might hinder you. Try your best to get through the game with the least amount of money to pay! "
              "Good luck!"
}

locationDescription = {
    'Dallas': "",
    'San Francisco': "",
    'Patterson': "",
    'Wichita': ""
}

#Dictionaries to send back to front-end
introAndAbout = {
    'Introduction': "Hi, welcome to [insert name here]. The goal of this game is to create an insurance plan and avoid the obstacles throughout the game. There" 
              " will be obstacles throughout the course of the game and the goal is to get the best net balance from "
              "the game possible. There will be 10 years to go through the game and each year may have an obstacle "
              "that might hinder you. Try your best to get through the game with the least amount of money to pay! "
              "Good luck!"
}

insuranceEarthquake = {
    'Cost': 42900,
    'Description': "There was a devastating 8.4 magnitude earthquake near San Francisco! Your house sustained"
                   "$92,500 in structural damage and you will need to file a claim!",
    'Result'     : "Luckily, you included earthquake coverage with your State Farm homeowner's insurance and they're"
                   "here to help! You will only pay up to your deductible amount of $42,900, and State Farm will cover"
                   "the remaining amount!"
}

notCoveredEarthquake = {
    'Cost': 92500,
    'Description': "There was a devastating earthquake in your area and it caused the hanging items in your house, "
                   "damaging the walls and the floors of your house.",
    'Result'     : "Sadly, you decided to not get the earthquake coverage in addition to your plan, and that turned out "
                   "to be a risky bet which backfired. The amount of money that you need to repair the damages in the "
                   "house was $8,500, which you have to pay out of pocket. "
}

insuranceLandslide = {
    'Cost': 12000,
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. However, since you chose to protect "
                   "your home with wilfire insurance, your insurance will help pay [insert amount here] in repair costs, "
                   "leaving you with [insert num here] to pay out of pocket. The intended amount to fully repair the damages was "
                   "[insert num here]."
}

notCoveredLandslide = {
    'Cost': 12000,
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. Unfortunately, since you did "
                   "not end up choosing to cover your house with wildfire insurance, you have to end up paying for all the "
                   "damages out of pocket. The total cost of the damages ended up being [insert num here]."
}

insuranceWindstorm = {
    'Cost': 6000,
    'Description': "Oh no! Weather condiitions were really bad and the perfect conditions were created for the perfect hurricane storm! "
                   "Your house suffered major roof damage as a result. Thankfully, since you opted into hurricane insurance to cover, "
                   "your insurance will cover [insert num here], so you will in turn only have to pay [insert num here] out of pocket. "
                   "The total cost for repairs was [insert num here]."
}

notCoveredWindstorm = {
    'Cost': 6000,
    'Description': "Oh no! Weather condiitions were really bad and the perfect conditions were created for the perfect hurricane storm! "
                   "Your house suffered major roof damage as a result. However, since you did not opt to cover in your insurance for "
                   "hurricane damage, you have to pay all the damages out of pocket, which totals [insert num here]."
}

insuranceFlood = {
    'Cost': 2500,
    'Description': "Bad news! It rained so much on one day to cause a major flash flood, and your house suffered internal pipe damages "
                   "as a result. Fortunately, you chose to include flood coverage in your insurance plan, which will help cover "
                   "[insert num here], totaling only [insert num here] to be paid out of pocket. The total cost of damages was "
                   "[insert num here]."
}

notCoveredFlood = {
    'Cost': 25000,
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

essentialPremiumsDallas = {
    'Name': "Essential Premiums Plan",
    'Policy Premium': 3621,
    'Deductible': 6880
}
essentialPremiumsAndWindstormDallas = {
    'Name': "Essential Premiums and Windstorm Coverage Plan",
    'Policy Premium': 5321,
    'Deductible': 6880
}
premiumPremiumsDallas = {
    'Name': "Premium Premiums",
    'Policy Premium': 4802,
    'Deductible': 3440
}
premiumPremiumsAndWindstormDallas = {
    'Name': "Premium Premiums and Windstorm Coverage Plan",
    'Policy Premium': 6502,
    'Deductible': 3440
}

essentialPremiumsSanFran = {
    'Name': "Essential Premiums Plan",
    'Policy Premium': 1119,
    'Deductible': 8580
}
essentialPremiumsAndEarthquakeSanFran = {
    'Name': "Essential Premiums and Earthquake Coverage Plan",
    'Policy Premium': 3619,
    'Deductible': 8580
}
premiumPremiumsSanFran = {
    'Name': "Premium Premiums Plan",
    'Policy Premium': 1474,
    'Deductible': 2145
}
premiumPremiumsAndEarthquakeSanFran = {
    'Name': "Premium Premiums and Earthquake Coverage Plan",
    'Policy Premium': 3974,
    'Deductible': 2145
}

essentialPremiumsPatterson = {
    'Name': "Essential Premiums Plan",
    'Policy Premium': 1522,
    'Deductible': 3220
}
essentialPremiumsAndFloodPatterson = {
    'Name': "Essential Premiums and Flood Coverage Plan",
    'Policy Premium': 2222,
    'Deductible': 3220
}
premiumPremiumsPatterson = {
    'Name': "Premium Premiums Plan",
    'Policy Premium': 2218,
    'Deductible': 1000
}
premiumPremiumsAndFloodPatterson = {
    'Name': "Premium Premiums and Flood Coverage Plan",
    'Policy Premium': 2918,
    'Deductible': 1000
}

essentialPremiumsWichita = {
    'Name': "Essential Premiums Plan",
    'Policy Premium': 3621,
    'Deductible': 10520
}
essentialPremiumsAndLandslideWichita = {
    'Name': "Essential Premiums and Landslide Coverage Plan",
    'Policy Premium': 4871,
    'Deductible': 10520
}
premiumPremiumsWichita = {
    'Name': "Premium Premiums Plan",
    'Policy Premium': 4933,
    'Deductible': 2630
}
premiumPremiumsAndLandslideWichita = {
    'Name': "Premium Premiums and Landslide Coverage Plan",
    'Policy Premium': 6183,
    'Deductible': 2630
}

#determine probabilities in a list
probEarthquake = 0.0
probFlood = 0.0
probWindstorm = 0.0
probLandslide = 0.0
total = 0.0

probList = []

def probability(currentLocation):

    if currentLocation in locations:
        if currentLocation == "Dallas":
            probEarthquake = 0.25
            probFlood = 0.05
            probWindstorm = 0.02
            probLandslide = 0.15
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
        elif currentLocation == "San Francisco":
            probEarthquake = 0.05
            probFlood = 0.25
            probWindstorm = 0.10
            probLandslide = 0.02
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
        elif currentLocation == "Patterson":
            probEarthquake = 0.05
            probFlood = 0.15
            probWindstorm = 0.25
            probLandslide = 0.02
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
        elif currentLocation == "Wichita":
            probEarthquake = 0.15
            probFlood = 0.02
            probWindstorm = 0.05
            probLandslide = 0.25
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
    else:
        print("Invalid Location")



    probList.append(total)
    probList.append(probEarthquake)
    probList.append(probFlood)
    probList.append(probWindstorm)
    probList.append(probLandslide)
    return probList


@app.route("/explain", methods=['GET'])
def explain():
    if request.method == 'GET':
        return json.dumps(introAndAbout)
    else:
        return json.dumps(error404)


@app.route("/locations", methods=['GET'])
def locationsList():
    if request.method == 'GET':
        return json.dumps(locations)
    else:
        return json.dumps(error404)


@app.route("/locDescription", methods=['GET'])
def locDescription():
    if request.method == 'GET':
        return json.dumps(locationDescription)
    else:
        return json.dumps(error404)


dallasPlans = [essentialPremiumsDallas, essentialPremiumsAndWindstormDallas, premiumPremiumsDallas, premiumPremiumsAndWindstormDallas]
sanFranPlans = [essentialPremiumsSanFran, essentialPremiumsAndEarthquakeSanFran, premiumPremiumsSanFran, premiumPremiumsAndEarthquakeSanFran]
pattersonPlans = [essentialPremiumsPatterson, essentialPremiumsAndFloodPatterson, premiumPremiumsPatterson, premiumPremiumsAndFloodPatterson]
wichitaPlans = [essentialPremiumsWichita, essentialPremiumsAndLandslideWichita, premiumPremiumsWichita, premiumPremiumsAndLandslideWichita]


@app.route("/plans/<location>", methods=['GET'])
def plans(location):
    if request.method == 'GET':
        if location == "Dallas":
            return json.dumps(dallasPlans)
        if location == "San Francisco":
            return json.dumps(sanFranPlans)
        if location == "Patterson":
            return json.dumps(pattersonPlans)
        if location == "Wichita":
            return json.dumps(wichitaPlans)
    else:
        return json.dumps(error404)


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
            if "Windstorm" in currPlan:
                return json.dumps(insuranceWindstorm)
            else:
                return json.dumps(insuranceWindstorm)
        if numChose == 5:
            if "Landslide" in currPlan:
                return json.dumps(insuranceLandslide)
            else:
                return json.dumps(insuranceLandslide)
    else:
        return json.dumps(error404)


if __name__ == "__main__":
    app.run()
