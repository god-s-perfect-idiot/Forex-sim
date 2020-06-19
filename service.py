import model
import time

balance = 1000

def reset_balance():
    global balance
    balance = 1000
    return balance

def transaction(amount, duration, current, ttype):
    global balance

    if(int(amount)<=balance):
        balance = balance - int(amount)
        time.sleep(int(duration)*5)
        hs = model.get_history()
        print(hs)
        if(float(current) >= hs[20] and ttype=="down"):
            balance += int(amount) + int(amount)*0.8
            return 1
        elif(float(current) <= hs[20] and ttype=="up"):
            balance += int(amount) + int(amount)*0.8
            return 1
        else:
            return 1

    return 0
