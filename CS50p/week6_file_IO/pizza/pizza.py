import sys
import csv
from tabulate import tabulate

def main():

    #ensures only 1 argument
    if len(sys.argv) == 2:
        print(check(sys.argv[1]))
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def check(arg):

    #list for holding dictionary
    chart = []

    #for checking if file exists
    try:

        #checks if it ends with py
        if arg.endswith(".csv"):

            #opens file and checks lines of CSV
            with open(arg) as file:
                #for loop to create dictionary that is then appended to the chart
                reader = csv.reader(file)

                #table that is created from the chart
                return tabulate(reader, headers="firstrow", tablefmt='grid')
        else:
            sys.exit("Not a CSV file")

    except FileNotFoundError:
        sys.exit("File not found")
        
''' will produce the same outcome but not needed. Also don't need the list of chart
                for pizza, cost1, cost2 in reader:
                    chart.append({"pizza": pizza , "cost1": cost1 , "cost2": cost2 })
'''

''' this also works
                 for line in file:
                    pizza,cost1,cost2 = line.strip().split(",")
                    menu = {"pizza" : pizza, "cost1" : cost1, "cost2" : cost2}
                    menu["pizza"] = pizza
                    menu["cost1"] = cost1
                    menu["cost2"] = cost2
                    chart.append(menu)
'''


if __name__ == "__main__":
    main()


