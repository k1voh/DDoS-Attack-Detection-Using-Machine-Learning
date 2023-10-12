import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle
import json

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

def detectDdos(jsonInp):
    json_dict = {'Fwd Seg Size Min':[0],'Flow IAT Min':[0],'Src Port':[0],'Tot Fwd Pkts':[0],'Init Bwd Win Byts':[0],'Src IP':[""],'Dst IP':[""],'Timestamp':["16/02/2018 11:25:34 PM"]}
    jsonVal = json.loads(jsonInp)
    
    for attribute,value in jsonVal.items():
        json_dict[attribute]=value
    print(json_dict)
    
    inputSet = pd.DataFrame(json_dict)
    inputSet['new_SRC_IP'] = LabelEncoder().fit_transform(inputSet['Src IP'])
    inputSet['new_DST_IP'] = LabelEncoder().fit_transform(inputSet['Dst IP'])
    inputSet['new_Timestamp'] = LabelEncoder().fit_transform(inputSet['Timestamp'])
    
    X = inputSet.drop(['Timestamp','Src IP','Dst IP'], axis='columns')
    with open("Model/Detect_DDoS.pickle", "rb") as pickle_model:
        model = pickle.load(pickle_model)  
    result = model.predict(X)
    return result

''' REMOVE BELOW CODE AFTER FRONT-END '''

# json_input = json.loads('{"Fwd Seg Size Min":20,"Flow IAT Min":13,"Src Port":50018,"Tot Fwd Pkts":3,"Init Bwd Win Byts":149,"new_SRC_IP":4367,"new_DST_IP":3370,"new_Timestamp":46713}')

# json_input = json.loads('{"Fwd Seg Size Min":0,"Flow IAT Min":4,"Src Port":80,"Tot Fwd Pkts":4,"Init Bwd Win Byts":211,"new_SRC_IP":3464,"new_DST_IP":3656,"new_Timestamp":10482}')

# print(detectDdos(json_input))
