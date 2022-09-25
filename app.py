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
    'Introduction': "Welcome to the Insurance Game! This game simulates what you can expect when you have State Farm as "
                    "your home insurance provider over a 10 year period. Pick a place to live, what home insurance "
                    "plan you want, and you're off!"
}

insuranceEarthquake = {
    'Cost': 42900,
    'Description': "Oh no! There was a devastating 8.4 magnitude earthquake nearby! You are safe and sound "
                   "but your house sustained $92,500 in structural damage and you will need to file a claim!",
    'Result'     : "Luckily, you included earthquake coverage with your State Farm homeowner's insurance and they're "
                   "here to help! You will only pay up to your deductible amount of $42,900, and State Farm will cover "
                   "the remaining amount!"
}

notCoveredEarthquake = {
    'Cost': 92500,
    'Description': "Oh no! There was a devastating 8.4 magnitude earthquake nearby! You are safe and sound "
                   "but your house sustained $92,500 in structural damage and you will need to file a claim!",
    'Result'     : "Unfortunately, you did not opt for State Farm's earthquake coverage and will need to pay for the "
                   "entire repairs yourself."
}

insuranceLandslide = {
    'Cost': 12000,
    'Description': "It's been quite the rainy year! While this was great for your vegetable garden,"
                   "it wasn't so great for your house. The record setting rainfall eroded the ground on the hills near "
                   "your house and caused a landslide that cause $12,000 in damages to your house's siding.",
    'Result'     : "Unfortunately, your landslide coverage deductible is $26,300 so if you file a claim with State "
                   "Farm you will need to pay the total cost out of pocket."
}

notCoveredLandslide = {
    'Cost': 12000,
    'Description': "It's been quite the rainy year! While this was great for your vegetable garden, "
                   "it wasn't so great for your house. The record setting rainfall eroded the ground on the hills near "
                   "your house and caused a landslide that cause $12,000 in damages to your house's siding.",
    'Result'     : "You did not opt in to State Farm's landslide coverage, and so you will need to pay for this "
                   "one yourself!"

}

insuranceWindstorm = {
    'Cost': 35000,
    'Description': "You were hoping that the weather channel was wrong, but alas, the windstorm swept through the "
                   "area, pelting the side of your house with rocks tearing open a part of your "
                   "roof. You get a quote to repair the house and find out it will be a whopping $35,000.",
    'Result'     : "You know this is going to cost and immediately spring into action and call Jake from "
                   "State Farm. He reminds you that you opted for State Farm's windstorm insurance, and they will be "
                   "covering the majority of the cost."

}

notCoveredWindstorm = {
    'Cost': 35000,
    'Description': "You were hoping that the weather channel was wrong, but alas, the windstorm swept through the "
                   "area, pelting the side of your house with rocks tearing open a part of your "
                   "roof. You get a quote to repair the house and find out it will be a whopping $35,000.",
    'Result'     : "Unfortunately, you did not opt in to State Farm's windstorm coverage and so you will be paying for "
                   "this yourself. Looks like that new boat will have to wait."

}

insuranceFlood = {
    'Cost': 2500,
    'Description': "What started off as a simple Saturday night, waiting for the heavy rain to subside while at your "
                   "favorite diner, quickly became scary as flash flooding occurs. You rush home to find a inch of "
                   "standing water in your house. A quote the next day tells you that you are looking at a $25,000 "
                   "repair.",
    'Result'     : "Luckily, you have State Farm's flood insurance and immediately file a claim, knowing that your "
                   "deductible is only $2,500."

}

notCoveredFlood = {
    'Cost': 25000,
    'Description': "What started off as a simple Saturday night, waiting for the heavy rain to subside while at your "
                   "favorite diner, quickly became scary as flash flooding occurs. You rush home to find a inch of "
                   "standing water in your house. A quote the next day tells you that you are looking at a $25,000 "
                   "repair.",
    'Result'     : "You curse yourself for not getting flood coverage through State Farm, and know that you will be "
                   "responsible for the entire cost of the repair."
}

safe = {
    'Cost': 0,
    'Description': "This year was a great year! You finally got to take that Hawaiian vacation you always wanted, you "
                   "picked up some new hobbies, and you got promoted at work! You're excited for the years ahead."
}

error404 = {
    '404': "Error 404, page not found."
}

dallasEssential = {
    'Name': "Essential",
    'Policy Premium': 3621,
    'Deductible': 6880
}
dallasEssentialWindstormCoverage = {
    'Name': "Essential with Windstorm Coverage",
    'Policy Premium': 5321,
    'Deductible': 6880
}
dallasPremium = {
    'Name': "Premium",
    'Policy Premium': 4802,
    'Deductible': 3440
}
dallasPremiumWindstormCoverage = {
    'Name': "Premium with Windstorm Coverage",
    'Policy Premium': 6502,
    'Deductible': 3440
}
sfEssential = {
    'Name': "Essential",
    'Policy Premium': 1119,
    'Deductible': 8580
}
sfEssentialEarthquakeCoverage = {
    'Name': "Essential with Earthquake Coverage",
    'Policy Premium': 3619,
    'Deductible': 8580
}
sfPremium = {
    'Name': "Premium",
    'Policy Premium': 1474,
    'Deductible': 2145
}
sfPremiumEarthquakeCoverage = {
    'Name': "Premium with Earthquake Coverage",
    'Policy Premium': 3974,
    'Deductible': 2145
}

pattersonEssential = {
    'Name': "Essential",
    'Policy Premium': 1522,
    'Deductible': 3220
}
pattersonEssentialFloodCoverage = {
    'Name': "Essential with Flood Coverage",
    'Policy Premium': 2222,
    'Deductible': 3220
}
pattersonPremium = {
    'Name': "Premium",
    'Policy Premium': 2218,
    'Deductible': 1000
}
pattersonPremiumFloodCoverage = {
    'Name': "Premium with Flood Coverage",
    'Policy Premium': 2918,
    'Deductible': 1000
}

wichitaEssential = {
    'Name': "Essential",
    'Policy Premium': 3621,
    'Deductible': 10520
}
wichitaEssentialLandslideCoverage = {
    'Name': "Essential with Landslide Coverage",
    'Policy Premium': 4871,
    'Deductible': 10520
}
wichitaPremium = {
    'Name': "Premium",
    'Policy Premium': 4933,
    'Deductible': 2630
}
wichitaPremiumLandslideCoverage = {
    'Name': "Premium with Landslide Coverage",
    'Policy Premium': 6183,
    'Deductible': 2630
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


dallasPlans = [dallasEssential, dallasEssentialWindstormCoverage, dallasPremium, dallasPremiumWindstormCoverage]
sanFranPlans = [sfEssential, sfEssentialEarthquakeCoverage, sfPremium, sfPremiumEarthquakeCoverage]
pattersonPlans = [pattersonEssential, pattersonEssentialFloodCoverage, pattersonPremium, pattersonPremiumFloodCoverage]
wichitaPlans = [wichitaEssential, wichitaEssentialLandslideCoverage, wichitaPremium, wichitaPremiumLandslideCoverage]


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
