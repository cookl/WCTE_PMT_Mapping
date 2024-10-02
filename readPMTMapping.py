import json

#an example script to read out LED mapping from the json created by makeMappingJson.py

def get_positions_from_entry(long_form_id):
    #longform id is just the mpmt_id*100 + pmt_id 
    return long_form_id//100, long_form_id%100
    


def get_key_from_value(json_data, input_value):
    for key, value in json_data.items():
        if value == input_value:
            return key
    return None  # Return None if no match is found    

# Open and read the JSON file
with open('PMT_Mapping.json', 'r') as file:
    pmt_data = json.load(file)
    
#example 1 get position id (offline data format) from electronics channel and card id (raw data format) 

card_id = 104 
pmt_channel = 1 #1,2 or 3

slot_id, pmt_pos = get_positions_from_entry(pmt_data[str((100*card_id)+pmt_channel)])
print("mPMT with card id",card_id,"pmt channel",pmt_channel,"-> slot id",slot_id,"position id",pmt_pos )

#example 2 going the other way around 
slot_id=slot_id
pmt_pos=pmt_pos

long_form_value = 100*(slot_id)+pmt_pos
card_id, pmt_channel =  get_positions_from_entry(int(get_key_from_value(pmt_data,long_form_value)))
print("mPMT with slot id",slot_id,"pmt position",pmt_pos,"-> card id",card_id,"channel id",pmt_channel)
