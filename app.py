from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

app = Flask(__name__)

# Load data
data = pd.DataFrame({
    'date': ['01-05-2024', '02-05-2024', '03-05-2024', '04-05-2024', '05-05-2024', '06-05-2024', 
             '07-05-2024', '08-05-2024', '09-05-2024', '10-05-2024', '11-05-2024', '12-05-2024', 
             '13-05-2024', '14-05-2024', '15-05-2024', '16-05-2024', '17-05-2024', '18-05-2024', 
             '19-05-2024'],
    'highesttemperature': [39, 40, 40, 40, 39, 38, 38, 38, 38, 36, 37, 34, 34, 36, 33, 34, 34, 33, 31],
    'lowesttemperature': [26, 26, 28, 27, 27, 26, 25, 26, 26, 24, 24, 23, 23, 24, 24, 24, 23, 22, 22]
})

# Convert date strings to datetime objects
data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y')

# Feature engineering: Extract day of year from date
data['day_of_year'] = data['date'].dt.dayofyear

# Train linear regression models
X = data[['day_of_year']]
y_highest = data['highesttemperature']
y_lowest = data['lowesttemperature']

model_highest = LinearRegression()
model_highest.fit(X, y_highest)

model_lowest = LinearRegression()
model_lowest.fit(X, y_lowest)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction results
@app.route('/predict', methods=['POST'])
def predict():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    future_dates = pd.date_range(start=start_date, end=end_date)
    future_day_of_year = future_dates.dayofyear
    
    future_predictions_highest = model_highest.predict(future_day_of_year.values.reshape(-1, 1))
    future_predictions_lowest = model_lowest.predict(future_day_of_year.values.reshape(-1, 1))
    
    predictions = []
    for date, highest_temp, lowest_temp in zip(future_dates, future_predictions_highest, future_predictions_lowest):
       
        highest_temp = str(int(round(highest_temp)))+"°C"
        lowest_temp = str(int(round(lowest_temp)))+"°C"
        predictions.append({'date': date.strftime('%Y-%m-%d'), 'highest_temp': highest_temp, 'lowest_temp': lowest_temp})
    
    return render_template('results.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
