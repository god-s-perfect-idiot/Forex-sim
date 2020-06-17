import model_helper as helper
from datetime import datetime

def generate_data():
    current = helper.generate()
    for i in range(30):
        current = helper.generate_offest(current)
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        retn = str(current)[:9]
        helper.keep_data(current,now)
    return(helper.forex_historic, helper.time_historic)

def refresh():
    current = helper.forex_historic[-1]
    new = helper.generate_offest(current)
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    retn = str(new)[:9]
    helper.keep_data(new,now)
    return(helper.forex_historic, helper.time_historic)
