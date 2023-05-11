import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model =None


def predict_price(location, sqft, bath, rooms):
    try :
        loc_index = __data_columns.index(location.lower())
    except: loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] =bath
    x[2]= rooms

    if loc_index>=0:
        x[loc_index] = 1

    return __model.predict([x])[0]


def get_location_names():
    return __locations


def load_saved_artefacts():
    print("loading")
    global __data_columns
    global  __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns= json.load(f)['data_columns']
        __locations= __data_columns[3:]

    global __model
    if __model is None:
        with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loaded artefacts")



if __name__ == '__main__':
    load_saved_artefacts()
    print(get_location_names())
    print(predict_price('1st Phase JP Nagar', 1000,2,3))