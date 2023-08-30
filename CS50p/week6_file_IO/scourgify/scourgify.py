import csv
import sys

def main():
    #ensures only 2 argument
    if len(sys.argv) == 3:
        create(sys.argv[1], sys.argv[2])
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

def create(arg1, arg2):
    #potential new list to store re organized names
    new_list = []

    try:
        #checks that both are csv files
        if arg1.endswith(".csv") and arg2.endswith(".csv"):

            #opens before.csv and reads in each row
            with open(arg1) as file: #read by default
                file1 = csv.DictReader(file)

                #for loop to store names in quotes into 2 variables
                for line in file1:
                    last, first = line["name"].split(",") # splits by comma
                    first = first.strip().replace('"',"") # strips any spaces of variable into 2 and replaces quote with blank,
                    last = last.strip().replace('"',"")
                    house = line["house"]
                    new_list.append({
                        'first': first,
                        'last': last,
                        'house': house
                        })



                    #TODO try some stuff without the loop and just printing all indexes of new_list[0:]

                    #takes 2nd file and writes in the changes
                with open(arg2, 'w') as file2:
                    fields = ['first', 'last', 'house']
                    writer = csv.DictWriter(file2, fieldnames = fields)

                    writer.writeheader()
                    writer.writerows(new_list)



        #must adjust to state what file couldnt be read so maybe more try except in the try except

    except FileNotFoundError:
        sys.exit(f"Could not read {arg1}")


if __name__ == "__main__":
    main()


'''while count1 < count:
                    with open(arg2, 'w') as file2:

                        fieldnames = ['first name', 'last name', 'house']
                        writer = csv.DictWriter(file2, fieldnames = fieldnames)

                        if count1 == 0:
                            writer.writeheader()
                        else:
                            pass
                        writer.writerow(new_list[count1])
                        count1 += 1
                return file2'''