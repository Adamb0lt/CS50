def main():
    amount = 50
    print(f"Amount due: {amount}")
    while amount > 0:
        coin = int(input("Insert coin: "))
        match coin:
            case 25 | 10 | 5:
                amount -= coin
                if amount > 0:
                    print(f"Amount Due: {amount}")
                else:
                   print(f"Change Owed: {abs(amount)}")
                   break
            case _:
                amount = amount
                print(f"Amount Due: {amount}")




main()


