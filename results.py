from flask import Flask
import json
import numpy as np

app = Flask(__name__)

file = open("[name].json")
data = json.load(file)

currentLocation = data("Location")
currPlan = data("Insurance")

#flood, earthquake, wildfire, hurricane

insuranceEarthquake = {
    'Cost': 5500,
    'Description': "There was a devastating earthquake in your area and it caused the hanging items in your house, "
                   "damaging the walls and the floors of your house. Luckily, you decided to get the earthquake "
                   "coverage in addition to your plan, and that turned out to be a good idea, since now your "
                   "insurance will cover $3,000 in repair costs. The amount of money that you needed to repair "
                   "the damages in the house was $8,500, so you ended up paying $5,500 out of pocket. Good job!"
}

notCoveredEarthquake = {
    'Cost': 8500,
    'Description': "There was a devastating earthquake in your area and it caused the hanging items in your house, "
                   "damaging the walls and the floors of your house. Sadly, you decided to not get the earthquake "
                   "coverage in addition to your plan, and that turned out to be a risky bet which backfired. "
                   "The amount of money that you need to repair the damages in the house was $8,500, which you "
                   "have to pay out of pocket. "
}

insuranceWildfire = {
    'Cost': [num],
    'Description': "There was a wildfire near your area, and the wildfire spread near your house and ended up burning "
                   "some parts of the roof and the exterior of your house has some burn marks. "
}

notCoveredWildfire = {
    'Cost': [num],
    'Description': "This happened blah blah blah"
}

insuranceHurricane = {
    'Cost': [num],
    'Description': "This happened blah blah blah"
}

notCoveredHurricane = {
    'Cost': [num],
    'Description': "This happened blah blah blah"
}

insuranceFlood = {
    'Cost': [num],
    'Description': "This happened blah blah blah"
}

notCoveredFlood = {
    'Cost': [num],
    'Description': "This happened blah blah blah"
}

safe = {
    'Cost': 0
    'Description': "You are safe for this time mwhahahahhahhahahahhaahah!"
}

locations = ["[name1]", "[name2]", "[name3]", "[name4]"]
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


@app.route("/results")
def get():
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

