import model_helper as helper
from datetime import datetime

def get_history():
    return(helper.forex_historic)

def generate_data():
    current = helper.generate()
    for i in range(30):
        current = helper.generate_offest(current)
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        helper.keep_data(current,now)
    return(helper.forex_historic, helper.time_historic)

def refresh():
    current = helper.forex_historic[-1]
    new = helper.generate_offest(current)
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    helper.keep_data(new,now)
    return(helper.forex_historic, helper.time_historic)
