import re
import textminer.validator as val

def words(x):
    return val.words(x)

def phone_number(x):
    if val.phone_number(x):
        numbers = re.sub(r'[\D]', '', x)
        return {"area_code" : numbers[:3], "number" : numbers[3:6]+'-'+numbers[6:]}

def money(x):
    if val.money(x):
        money = re.sub(r'[,]', '', x)
        return {"currency" : "$", "amount" : float(money[1:])}

def zipcode(x):
    if val.zipcode(x):
        if len(x) == 10:
            return {"zip": x[:5], "plus4": x[6:]}
        else:
            return {"zip": x[:5], "plus4": None}

def date(x):
    if val.date(x):
        date = re.split(r'[/-]', x)
        return {"month": date[0], "day": date[1], "year": date[2]}
