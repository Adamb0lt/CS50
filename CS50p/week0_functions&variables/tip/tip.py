def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    cash = float(d.replace("$",""))
    dolla = round(cash,1)
    return dolla



def percent_to_float(p):
    # TODO
    percentage = p.replace("%","")
    perc = float(percentage)/100
    return perc



main()