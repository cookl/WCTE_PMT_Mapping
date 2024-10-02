import json
import numpy as np
# def find_key_by_value(dictionary, value):
#     # Iterate through the dictionary items
#     for key, val in dictionary.items():
#         if val == value:
#             return key
#     return None  # Return None if the value is not found


# Open and read the JSON file
with open('modulo_dump.json', 'r') as file:
    data = json.load(file)

outputMapping = {}
output_csv = []
for mPMT in data["data"]:
    # print(mPMT)
    mpmtin = mPMT["MPMTIN"]
    if mpmtin is not None:
        #missing slots and fd mPMTs are none right now
        parts = mpmtin.split('-')
        card_id = int(parts[-1])  # Get the last part
        
        slot_id = mPMT["slot_id"]
        channel_mapping = mPMT["channel_mapping"]
        
        for pmt in range(19):
            channel = channel_mapping["pmt_"+str(pmt)+"_chan_id"]
            key = str(card_id*100+channel)
            value = slot_id*100+pmt
            outputMapping[key]=value
            output_csv.append((int(key),value))
 
 
outputMapping_json = json.dumps(outputMapping, indent=2)
# optionally save as csv
# output_csv = np.array(output_csv,dtype=int)
# np.savetxt("cardIDMapping.csv",output_csv,fmt='%d',delimiter=",", header="#cardid*100+ch -> slotid*100 + pmt_position")

with open('../PMT_Mapping.json', 'w') as file:
    file.write(outputMapping_json)

    # print("card_id:",card_id,"slot_id",slot_id)
        # print(mpmtin)
        # print(mPMT["channel_mapping"])
        # input()