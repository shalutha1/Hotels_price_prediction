import string
import pickle
import numpy as np
from flask import Flask, render_template, request,url_for

Hotel = Flask(__name__)


def prediction(lst):
    filename = "D:/ML/sample pro/Regression/yervan hotels/Hotel_Price_predictor.pickle"
    with open(filename, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([lst])
        return pred_value

@Hotel.route('/', methods=['POST', 'GET'])
def index():
    pred = 0  # Initialize pred with a default value

    if request.method == 'POST':
        star_rating = request.form['Star Rating']
        Rating = request.form['Rating']
        Staff = request.form['Staff']
        Facilities = request.form['Facilities']
        Location = request.form['Location']
        Comfort = request.form['Comfort']
        Cleanliness = request.form['Cleanliness']
        Free_Parking = request.form['Free Parking']
        Fitness_Centre = request.form['Fitness Centre']
        Spa_and_Wellness_Centre = request.form['Spa and Wellness Centre']
        Airport_Shuttle = request.form['Airport Shuttle']
        

        feature_list = []

        feature_list.append(float(star_rating))
        feature_list.append(float(Rating))
        feature_list.append(float(Staff))
        feature_list.append(float(Facilities))
        feature_list.append(float(Location))
        feature_list.append(float(Comfort))
        feature_list.append(float(Cleanliness))

        Free_Parking_list = ['Yes','No']
        Fitness_Centre_list = ['Yes','No']
        Spa_and_Wellness_Centre_list = ['Yes','No']
        Airport_Shuttle_list = ['Yes','No']


        def traverse(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse(Free_Parking_list, Free_Parking)
        traverse(Fitness_Centre_list, Fitness_Centre)
        traverse(Spa_and_Wellness_Centre_list, Spa_and_Wellness_Centre)
        traverse(Airport_Shuttle_list, Airport_Shuttle)

        print(feature_list)


        pred = prediction(feature_list)
        pred = np.round(pred[0])

    return render_template("Hotel.html", pred=pred)



if __name__ == '__main__':
    Hotel.run(debug=True)   

        


       


