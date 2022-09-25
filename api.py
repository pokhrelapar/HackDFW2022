import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
import numpy as np

#routing API endpoints
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#list of locations
locations = [
    {"id": 'dallas', 'name': 'Dallas, TX', 'desc': "A well-rounded city with lots of attractions, weather is fairly consistent but is in 'tornado alley', therefore "
                                                   "prone to windstorms."
    }, 
    {"id": "san francisco", "name": "San Francisco, CA", "desc": "One of the most populat tourist cities to visit in California, "
                                                                    "lots of good food and attractions to see, "
                                                                    "however near a fault line, therefore prone to earthquakes."},
    {"id": "patterson", "name": "Patterson, GA", "desc": "A relatively unpopulated city, totaling at only 750 people, but known for being "
                                                         "near the heart of Atlanta, lots of tourist attractions, but frequent flooding "
                                                         "due to Georgia's proximity to the coast."},
    {"id": "wichita", "name": "Wichita, KA", "desc": "Known as the 'Air Capital of the World', Wichita is known for being the birthplace "
                                                     "of the popular fast food pizza. However, Landslides are one of the most common "
                                                     "natural disasters that occur in Kansas, being that it's in the heart of tornado valley."}
]

#Dictionaries to send back to front-end
introAndAbout = {
    'introduction': "Welcome to the Insurance Game! This game simulates what you can expect when you have State Farm as "
                    "your home insurance provider over a 10 year period. Pick a place to live, what home insurance "
                    "plan you want, and you're off!"
}

insuranceEarthquake = {
    'cost': 42900,
    'description': "Oh no! There was a devastating 8.4 magnitude earthquake nearby! You are safe and sound "
                   "but your house sustained $92,500 in structural damage and you will need to file a claim!",
    'result'     : "Luckily, you included earthquake coverage with your State Farm homeowner's insurance and they're "
                   "here to help! You will only pay up to your deductible amount of $42,900, and State Farm will cover "
                   "the remaining amount!",
}

notCoveredEarthquake = {
    'cost': 92500,
    'description': "Oh no! There was a devastating 8.4 magnitude earthquake nearby! You are safe and sound "
                   "but your house sustained $92,500 in structural damage and you will need to file a claim!",
    'result'     : "Unfortunately, you did not opt for State Farm's earthquake coverage and will need to pay for the "
                   "entire repairs yourself."
}

insuranceLandslide = {
    'cost': 12000,
    'description': "It's been quite the rainy year! While this was great for your vegetable garden,"
                   "it wasn't so great for your house. The record setting rainfall eroded the ground on the hills near "
                   "your house and caused a landslide that cause $12,000 in damages to your house's siding.",
    'result'     : "Unfortunately, your landslide coverage deductible is $26,300 so if you file a claim with State "
                   "Farm you will need to pay the total cost out of pocket."
}

notCoveredLandslide = {
    'cost': 12000,
    'description': "It's been quite the rainy year! While this was great for your vegetable garden, "
                   "it wasn't so great for your house. The record setting rainfall eroded the ground on the hills near "
                   "your house and caused a landslide that cause $12,000 in damages to your house's siding.",
    'result'     : "You did not opt in to State Farm's landslide coverage, and so you will need to pay for this "
                   "one yourself!"

}

insuranceWindstorm = {
    'cost': 35000,
    'description': "You were hoping that the weather channel was wrong, but alas, the windstorm swept through the "
                   "area, pelting the side of your house with rocks tearing open a part of your "
                   "roof. You get a quote to repair the house and find out it will be a whopping $35,000.",
    'result'     : "You know this is going to cost and immediately spring into action and call Jake from "
                   "State Farm. He reminds you that you opted for State Farm's windstorm insurance, and they will be "
                   "covering the majority of the cost."

}

notCoveredWindstorm = {
    'cost': 35000,
    'description': "You were hoping that the weather channel was wrong, but alas, the windstorm swept through the "
                   "area, pelting the side of your house with rocks tearing open a part of your "
                   "roof. You get a quote to repair the house and find out it will be a whopping $35,000.",
    'result'     : "Unfortunately, you did not opt in to State Farm's windstorm coverage and so you will be paying for "
                   "this yourself. Looks like that new boat will have to wait."

}

insuranceFlood = {
    'cost': 2500,
    'description': "What started off as a simple Saturday night, waiting for the heavy rain to subside while at your "
                   "favorite diner, quickly became scary as flash flooding occurs. You rush home to find a inch of "
                   "standing water in your house. A quote the next day tells you that you are looking at a $25,000 "
                   "repair.",
    'result'     : "Luckily, you have State Farm's flood insurance and immediately file a claim, knowing that your "
                   "deductible is only $2,500."

}

notCoveredFlood = {
    'cost': 25000,
    'description': "What started off as a simple Saturday night, waiting for the heavy rain to subside while at your "
                   "favorite diner, quickly became scary as flash flooding occurs. You rush home to find a inch of "
                   "standing water in your house. A quote the next day tells you that you are looking at a $25,000 "
                   "repair.",
    'result'     : "You curse yourself for not getting flood coverage through State Farm, and know that you will be "
                   "responsible for the entire cost of the repair."
}

safe = {
    'cost': 0,
    'description': "This year was a great year! You finally got to take that Hawaiian vacation you always wanted, you "
                   "picked up some new hobbies, and you got promoted at work! You're excited for the years ahead."
}

error404 = {
    '404': "Error 404, page not found."
}

dallasEssential = {
    'id': 'dallasEssential',
    'name': "Essential",
    'policyPremium': 3621,
    'deductible': 6880
}
dallasEssentialWindstormCoverage = {
    'id': 'dallasEssentialWindstormCoverage',
    'name': "Essential with Windstorm Coverage",
    'policyPremium': 5321,
    'deductible': 6880
}
dallasPremium = {
    'id': 'dallasPremium',
    'name': "Premium",
    'policyPremium': 4802,
    'deductible': 3440
}
dallasPremiumWindstormCoverage = {
    'id': 'dallasPremiumWindstormCoverage',
    'name': "Premium with Windstorm Coverage",
    'policyPremium': 6502,
    'deductible': 3440
}
sfEssential = {
    'id': 'sfEssential',
    'name': "Essential",
    'policyPremium': 1119,
    'deductible': 8580
}
sfEssentialEarthquakeCoverage = {
    'id': 'sfEssentialEarthquakeCoverage',
    'name': "Essential with Earthquake Coverage",
    'policyPremium': 3619,
    'deductible': 8580
}
sfPremium = {
    'id': 'sfPremium',
    'name': "Premium",
    'policyPremium': 1474,
    'deductible': 2145
}
sfPremiumEarthquakeCoverage = {
    'id': 'sfPremiumEarthquakeCoverage',
    'name': "Premium with Earthquake Coverage",
    'policyPremium': 3974,
    'deductible': 2145
}

pattersonEssential = {
    'id': 'pattersonEssential',
    'name': "Essential",
    'policyPremium': 1522,
    'deductible': 3220
}
pattersonEssentialFloodCoverage = {
    'id': 'pattersonEssentialFloodCoverage',
    'name': "Essential with Flood Coverage",
    'policyPremium': 2222,
    'deductible': 3220
}
pattersonPremium = {
    'id': 'pattersonPremium',
    'name': "Premium",
    'policyPremium': 2218,
    'deductible': 1000
}
pattersonPremiumFloodCoverage = {
    'id': 'pattersonPremiumFloodCoverage',
    'name': "Premium with Flood Coverage",
    'policyPremium': 2918,
    'deductible': 1000
}

wichitaEssential = {
    'id': 'wichitaEssential',
    'name': "Essential",
    'policyPremium': 3621,
    'deductible': 10520
}
wichitaEssentialLandslideCoverage = {
    'id': 'wichitaEssentialLandslideCoverage',
    'name': "Essential with Landslide Coverage",
    'policyPremium': 4871,
    'deductible': 10520
}
wichitaPremium = {
    'id': 'wichitaPremium',
    'name': "Premium",
    'policyPremium': 4933,
    'deductible': 2630
}
wichitaPremiumLandslideCoverage = {
    'id': 'wichitaPremiumLandslideCoverage',
    'name': "Premium with Landslide Coverage",
    'policyPremium': 6183,
    'deductible': 2630
}

def probability(currentLocation):
    probEarthquake = 0.0
    probFlood = 0.0
    probWindstorm = 0.0
    probLandslide = 0.0
    total = 0.0

    probList = []

    if currentLocation in locations:
        if currentLocation == "Dallas":
            probEarthquake = 0.02
            probFlood = 0.05
            probWindstorm = 0.55
            probLandslide = 0.15
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
            probList.append(total)
            probList.append(probEarthquake)
            probList.append(probFlood)
            probList.append(probWindstorm)
            probList.append(probLandslide)
            return probList
        elif currentLocation == "San Francisco":
            probEarthquake = 0.55
            probFlood = 0.05
            probWindstorm = 0.10
            probLandslide = 0.02
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
            probList.append(total)
            probList.append(probEarthquake)
            probList.append(probFlood)
            probList.append(probWindstorm)
            probList.append(probLandslide)
            return probList
        elif currentLocation == "Patterson":
            probEarthquake = 0.05
            probFlood = 0.55
            probWindstorm = 0.10
            probLandslide = 0.02
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
            probList.append(total)
            probList.append(probEarthquake)
            probList.append(probFlood)
            probList.append(probWindstorm)
            probList.append(probLandslide)
            return probList
        elif currentLocation == "Wichita":
            probEarthquake = 0.15
            probFlood = 0.02
            probWindstorm = 0.05
            probLandslide = 0.55
            total = 1.0 - (probWindstorm + probLandslide + probFlood + probEarthquake)
            probList.append(total)
            probList.append(probEarthquake)
            probList.append(probFlood)
            probList.append(probWindstorm)
            probList.append(probLandslide)
            return probList
    else:
        print("Invalid Location")


@app.route("/explain", methods=['GET'])
def explain():
    if request.method == 'GET':
        return json.dumps(introAndAbout)
    else:
        return json.dumps(error404)


@app.route("/location", methods=['GET'])
def getLocation():
    if request.method == 'GET':
        return json.dumps(locations)
    else:
        return json.dumps(error404)


dallasPlans = [dallasEssential, dallasEssentialWindstormCoverage, dallasPremium, dallasPremiumWindstormCoverage]
sanFranPlans = [sfEssential, sfEssentialEarthquakeCoverage, sfPremium, sfPremiumEarthquakeCoverage]
pattersonPlans = [pattersonEssential, pattersonEssentialFloodCoverage, pattersonPremium, pattersonPremiumFloodCoverage]
wichitaPlans = [wichitaEssential, wichitaEssentialLandslideCoverage, wichitaPremium, wichitaPremiumLandslideCoverage]


@app.route("/plans/<location>", methods=['GET'])
def plans(location):
    if request.method == 'GET':
        if location == "dallas":
            return json.dumps(dallasPlans)
        if location == "san francisco":
            return json.dumps(sanFranPlans)
        if location == "patterson":
            return json.dumps(pattersonPlans)
        if location == "wichita":
            return json.dumps(wichitaPlans)
    else:
        return json.dumps(error404)


@app.route("/results/<location>/<plan>", methods=['GET'])
def results(location, plan):
    currPlan = plan
    currLocation = location
    if request.method == 'GET':
        numChose = np.random.choice(np.arange(1, 6), p=probability(currLocation))
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
                return json.dumps(notCoveredWindstorm)
        if numChose == 5:
            if "Landslide" in currPlan:
                return json.dumps(insuranceLandslide)
            else:
                return json.dumps(notCoveredLandslide)
    else:
        return json.dumps(error404)


if __name__ == "__main__":
    app.run()


