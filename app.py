# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first-innings-score-lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()

    if request.method == 'POST':
        #runs	wickets	overs	runs_last_5	wickets_last_5 venue	bat_team	bowl_team

        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

        temp_array = temp_array + [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]

        venue=request.form['venue']
        if venue == 'De Beers Diamond Oval':
            temp_array = temp_array +[0]
        elif venue == 'Subrata Roy Sahara Stadium':
            temp_array = temp_array +[1]
        elif venue == 'Buffalo Park':
            temp_array = temp_array +[2]
        elif venue == 'OUTsurance Ova':
            temp_array = temp_array +[3]
        elif venue == 'Holkar Cricket Stadium':
            temp_array = temp_array +[4]
        elif venue == 'Barabati Stadium':
            temp_array = temp_array +[5]
        elif venue == 'Newlands':
            temp_array = temp_array +[6]
        elif venue == 'Maharashtra Cricket Association Stadium':
            temp_array = temp_array +[7]
        elif venue == 'Shaheed Veer Narayan Singh International Stadium':
            temp_array = temp_array +[8]
        elif venue == 'New Wanderers Stadium':
            temp_array = temp_array +[9]
        elif venue == 'Dr DY Patil Sports Academy':
            temp_array = temp_array +[10]
        elif venue == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            temp_array = temp_array +[11]
        elif venue == 'JSCA International Stadium Complex':
            temp_array = temp_array +[12]
        elif venue == 'Sharjah Cricket Stadium':
            temp_array = temp_array +[13]
        elif venue == "St George's Park":
            temp_array = temp_array +[14]
        elif venue == 'Sheikh Zayed Stadium':
            temp_array = temp_array +[15]
        elif venue == 'Dubai International Cricket Stadium':
            temp_array = temp_array +[16]
        elif venue == 'SuperSport Park':
            temp_array = temp_array +[17]
        elif venue == 'Himachal Pradesh Cricket Association Stadium':
            temp_array = temp_array +[18]
        elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            temp_array = temp_array +[19]
        elif venue == 'Kingsmead':
            temp_array = temp_array +[20]
        elif venue == 'Sardar Patel Stadium, Motera':
            temp_array = temp_array +[21]
        elif venue == 'Brabourne Stadium':
            temp_array = temp_array +[22]
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array +[23]
        elif venue == 'Sawai Mansingh Stadium':
            temp_array = temp_array +[24]
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array +[25]
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array +[26]
        elif venue == 'Feroz Shah Kotla':
            temp_array = temp_array +[27]
        elif venue == 'Eden Gardens':
            temp_array = temp_array +[28]
        elif venue == 'Wankhede Stadium':
            temp_array = temp_array +[29]
        elif venue == 'M Chinnaswamy Stadium':
            temp_array = temp_array +[30]

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [5]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [1]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [6]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [3]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [7]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [2]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [4]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0]


        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [7]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [2]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [6]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [4]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [3]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [5]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0]




        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])

        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)



if __name__ == '__main__':
	app.run(debug=True)
