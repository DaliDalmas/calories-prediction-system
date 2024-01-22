import pickle


def predict_calories(data):
    # data that comes in looks like this
    # session_type='running' actual_calories_burned=1000.0 predicted_calories_burned=800.0 climb=7.0 duration=30.0 distance=5.0 session_time=datetime.datetime(2024, 1, 22, 18, 29, 8, 896000, tzinfo=TzInfo(UTC))
    with open('./type_encoder.pkl', 'rb') as file:
        type_encoder = pickle.load(file)

    with open('./month_encoder.pkl', 'rb') as file:
        month_encoder = pickle.load(file)

    with open('./day_of_week_encoder.pkl', 'rb') as file:
        day_of_week_encoder = pickle.load(file)

    with open('./random_forest_regressor.pkl', 'rb') as file:
        model = pickle.load(file)
    # data_dict = {
    #             'climb (m)': ,
    #             'duration(s)': ,
    #             'distance(m)': ,
    #             'type_Cycling': ,
    #             'type_Running': ,
    #             'month_April': ,
    #             'month_August': ,
    #             'month_December': ,
    #             'month_February': ,
    #             'month_January': ,
    #             'month_July': ,
    #             'month_June': ,
    #             'month_March': ,
    #             'month_May': ,
    #             'month_November': ,
    #             'month_October': ,
    #             'month_September': ,
    #             'day_of_week_Friday': ,
    #             'day_of_week_Monday': ,
    #             'day_of_week_Saturday': ,
    #             'day_of_week_Sunday': ,
    #             'day_of_week_Thursday': ,
    #             'day_of_week_Tuesday': ,
    #             'day_of_week_Wednesday': 
    # }


    return model.predict(data)