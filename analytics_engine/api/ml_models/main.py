import pickle
import numpy as np
import pandas as pd

def predict_calories(data):

    with open('./ml_models/type_encoder.pkl', 'rb') as file:
        type_encoder = pickle.load(file)

    with open('./ml_models/month_encoder.pkl', 'rb') as file:
        month_encoder = pickle.load(file)

    with open('./ml_models/day_of_week_encoder.pkl', 'rb') as file:
        day_of_week_encoder = pickle.load(file)

    with open('./ml_models/random_forest_regressor.pkl', 'rb') as file:
        model = pickle.load(file)
    
    month = data['session_time'].strftime('%B')
    day_of_week = data['session_time'].strftime('%A')

    data_dict = {
                'climb (m)': float(data['climb']),
                'duration(s)': float(data['duration']),
                'distance(m)': float(data['distance']),
                'type_Cycling': type_encoder.transform(np.array([str(data['session_type']).title()]).reshape(1, -1)).toarray()[0][0],
                'type_Running': type_encoder.transform(np.array([str(data['session_type']).title()]).reshape(1, -1)).toarray()[0][1],
                'month_April': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][0],
                'month_August': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][1],
                'month_December': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][2],
                'month_February': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][3],
                'month_January': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][4],
                'month_July': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][5],
                'month_June': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][6],
                'month_March': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][7],
                'month_May': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][9],
                'month_November': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][9],
                'month_October': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][10],
                'month_September': month_encoder.transform(np.array([str(month).title()]).reshape(1, -1)).toarray()[0][11],
                'day_of_week_Friday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][0],
                'day_of_week_Monday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][1],
                'day_of_week_Saturday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][2],
                'day_of_week_Sunday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][3],
                'day_of_week_Thursday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][4],
                'day_of_week_Tuesday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][5],
                'day_of_week_Wednesday': day_of_week_encoder.transform(np.array([str(day_of_week).title()]).reshape(1, -1)).toarray()[0][6]
    }
    df = pd.DataFrame([data_dict])

    return round(model.predict(df)[0], 4)
