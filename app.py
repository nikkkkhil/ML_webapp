from flask import Flask, render_template, jsonify, redirect, request

from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/scrape", methods=['GET'])
def scrape():
    listings = mongo.db.listings
    listings_data = scrape_craigslist.scrape()
    listings.update(
        {},
        listings_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

@app.route('/get-user-data', methods=['POST'])
def predict_stuff():
    if request.method == 'POST':
        model = joblib.load('trained_house_classifier_model1.pkl')

        # print('-----line 27--------')
        # print(request.form.get('year_built'))
        #
        # year_built = int(request.form.get('year_built'))

        print('line 31')

        # stories = int(request.form.get('stories'))
        Number of balcony	 = int(request.form.get('balcony'))
        Number of bathrooms = int(request.form.get('bath'))
        total_sqft = int(request.form.get('total_sqft'))
        # garage_sqft = int(request.form.get('garage_sqft'))
        #
        # carport_sqft = int(request.form.get('carport_sqft'))
        # has_fireplace = request.form.get('has_fireplace')
        #
        # has_pool = request.form.get('has_pool')
        #
        # has_central_heating = request.form.get('has_central_heating')
        #
        # has_central_cooling = request.form.get('has_central_cooling')
        #
        #
        # has_fireplace = request.form.get('has_fireplace')

        Place = request.form.get('location')

        Size = request.form.get('size')

        Area Type =  request.form.get('area_type')

        house_to_value = [
            # House features
            Number of balcony
            Number of bathrooms
            total_sqft
            # full_bathrooms,      # full_bathrooms
            # half_bathrooms,      # half_bathrooms
            # livable_sqft,   # livable_sqft
            # total_sqft,   # total_sqft
            # garage_sqft,      # garage_sqft
            # carport_sqft,      # carport_sqft
            # 1 if (has_fireplace == 'on') else 0,   # has_fireplace
            # 1 if (has_pool == 'on') else 0,  # has_pool
            # 1 if (has_central_heating == 'on') else 0,   # has_central_heating
            # 1 if (has_central_cooling == 'on') else 0,   # has_central_cooling

            # Garage type: Choose only one
            1 if (Place == 'Electronic City Phase II') else 0,      # attached
            1 if (Place == 'Chikka Tirupathi') else 0,
            1 if (Place == 'Uttarahalli') else 0,
            1 if (Place == 'Lingadheeranahalli') else 0,
            1 if (Place == 'Kothanur') else 0,
            1 if (Place == 'Whitefield') else 0,
            1 if (Place == 'Marathahalli') else 0,
            1 if (Place == '7th Phase JP Nagar') else 0,
            1 if (Place == 'Gottigere') else 0,
            1 if (Place == 'Sarjapur') else 0,
            1 if (Place == 'Mysore Road') else 0,
            1 if (Place == 'Bisuvanahalli	') else 0,
            1 if (Place == 'Raja Rajeshwari Nagar	') else 0,
            1 if (Place == 'Ramakrishnappa Layout	') else 0,
            1 if (Place == 'Manayata Tech Park') else 0,
            1 if (Place == 'Kengeri	') else 0,
            1 if (Place == 'Binny Pete') else 0,
            1 if (Place == 'Thanisandra	') else 0,
            1 if (Place == 'Bellandur') else 0,
            1 if (Place == 'Mangammanapalya') else 0,
            1 if (Place == 'Electronic City') else 0,
            1 if (Place == 'Whitefield') else 0,
            1 if (Place == 'Ramagondanahalli') else 0,
            1 if (Place == 'Yelahanka') else 0,
            1 if (Place == 'Bisuvanahalli') else 0,
            1 if (Place == 'Hebbal') else 0,
            1 if (Place == 'Gubbalala') else 0,
            1 if (Place == 'Mahadevpura') else 0,
            1 if (Place == 'Sarjapur Road') else 0,
            1 if (Place == 'Weavers Colony') else 0,
            1 if (Place == 'Udayapur Village') else 0,
            1 if (Place == 'Sultan Palya') else 0,
            1 if (Place == 'Haralur Road') else 0,
            1 if (Place == 'Cox Town') else 0,
            1 if (Place == 'Kenchenahalli') else 0,
            1 if (Place == 'Hosakerehalli') else 0,
            1 if (Place == 'Kothanur') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,
            # 1 if (Place == '') else 0,


            1 if (Place == 'none') else 0,      # none

            # Area Type type: Choose only one
            1 if (Area Type == 'Super built-up Area') else 0,      # attached
            1 if (Area Type == 'Plot Area') else 0,      # detached
            1 if (Area Type == 'Built-up Area') else 0,      # detached
            1 if (Area Type == 'none') else 0,      # none

            # City: Choose only one
            1 if (Size == '1 BHK') else 0,      # Amystad
            1 if (size == '2 BHK	') else 0,      # Davidtown
            1 if (Size == '3 BHK') else 0,      # Chadstad
            1 if (Size == '4 BHK') else 0,      # Clarkberg
            1 if (Size == '1 Bedroom') else 0,      # Brownport
            1 if (Size == '4 Bedroom') else 0,      # Coletown
            1 if (size == '5 Bedroom') else 0,      # Davidfort
            1 if (size == '7 Bedroom') else 0,      # Davidtown
            0,      # East Amychester
            0,      # East Janiceville
            0,      # East Justin
            0,      # East Lucas
            0,      # Fosterberg
            0,      # Hallfort
            0,      # Jeffreyhaven
            0,      # Jenniferberg
            0,      # Joshuafurt
            0,      # Julieberg
            0,      # Justinport
            0,      # Lake Carolyn
            0,      # Lake Christinaport
            0,      # Lake Dariusborough
            0,      # Lake Jack
            0,      # Lake Jennifer
            0,      # Leahview
            0,      # Lewishaven
            0,      # Martinezfort
            0,      # Morrisport
            0,      # New Michele
            0,      # New Robinton
            0,      # North Erinville
            0,      # Port Adamtown
            0,      # Port Andrealand
            0,      # Port Daniel
            0,      # Port Jonathanborough
            0,      # Richardport
            0,      # Rickytown
            0,      # Scottberg
            0,      # South Anthony
            0,      # South Stevenfurt
            0,      # Toddshire
            0,      # Wendybury
            0,      # West Ann
            0,      # West Brittanyview
            0,      # West Gerald
            0,      # West Gregoryview
            0,      # West Lydia
            0       # West Terrence
        ]

        # scikit-learn assumes you want to predict the values for lots of houses at once, so it expects an array.
        # We just want to look at a single house, so it will be the only item in our array.
        homes_to_value = [
            house_to_value
        ]

        # return render_template("index.html", pred=house_to_value)

        # Run the model and make a prediction for each house in the homes_to_value array
        predicted_home_values = model.predict(homes_to_value)

        # Since we are only predicting the price of one house, just look at the first prediction returned
        predicted_value = predicted_home_values[0]

        return render_template("index.html", pred=predicted_value)


if __name__ == "__main__":
    app.run()
