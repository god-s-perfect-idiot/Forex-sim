from forex_python.converter import CurrencyRates
from datetime import datetime
import time
import random
from matplotlib import pyplot as plt

convert = CurrencyRates()
forex_historic = []
time_historic = []

def keep_data(data,now):
    global forex_historic,time_historic

    if(len(forex_historic)>20):
            forex_historic = forex_historic[1:]
            forex_historic.append(data)
            time_historic = time_historic[1:]
            time_historic.append(now)
    else:
        forex_historic.append(data)
        time_historic.append(now)

def correct():
    for i in forex_historic:
        i = float(i)

def generate_offest(current):


    val = random.randint(10,99)
    val *= 0.0000001
    opn = random.randint(1,10)
    if(opn%2 == 1):
        current += val
    else:
        current -= val
    return current


def generate():

    now = datetime.now()
    uti = convert.get_rate('USD','INR',now)
    return uti
