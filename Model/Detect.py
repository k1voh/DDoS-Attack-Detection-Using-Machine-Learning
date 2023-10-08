import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import json

"""
        json_input = [{
            'Fwd Seg Size Min' : integer,
            'Flow IAT Min' : integer,
            'Src Port' : integer,
            'Tot Fwd Pkts' : integer,
            'Init Bwd Win Byts' : integer,
            'Src IP' : string,
            'Dst IP' : string,
            'Timestamp' : string
        }]
"""
'''
    Below is the input after preprocessing of data
    
    json_input = {
    "Fwd Seg Size Min":20,
    "Flow IAT Min":13,
    "Src Port":50018,
    "Tot Fwd Pkts":3,
    "Init Bwd Win Byts":149,
    "new_SRC_IP":4367,
    "new_DST_IP":3370,
    "new_Timestamp":46713}
'''

''' REMOVE '#' AFTER CREATING AND JOINING FRONT-END
    AND REMOVE X=inputSet'''

def detectDdos(json_input):
    inputSet = pd.DataFrame(pd.json_normalize(json_input))
    
    inputSet['new_SRC_IP'] = LabelEncoder().fit_transform(inputSet['Src IP'])
    inputSet['new_DST_IP'] = LabelEncoder().fit_transform(inputSet['Dst IP'])
    inputSet['new_Timestamp'] = LabelEncoder().fit_transform(inputSet['Timestamp'])
    
    X = inputSet.drop(['Timestamp','Src IP','Dst IP'], axis='columns')
    X = inputSet
    with open("Model/Detect_DDoS.pickle", "rb") as pickle_model:
        model = pickle.load(pickle_model)
        
    return model.predict(inputSet)

''' REMOVE BELOW CODE AFTER FRONT-END '''
#json_input = json.loads('{"Fwd Seg Size Min":20,"Flow IAT Min":13,"Src Port":50018,"Tot Fwd Pkts":3,"Init Bwd Win Byts":149,"new_SRC_IP":4367,"new_DST_IP":3370,"new_Timestamp":46713}')

#print(detectDdos(json_input))
