def main():
    groceryList = {}

    calc = groceryListCalc()
    
    groceryList = calc.addToList(groceryList, 'chicken', 10.00)
    groceryList = calc.addToList(groceryList, 'steak', 35.78)
    
    calc.printList(groceryList)

    return

class groceryListCalc:
    def addToList(self, groceryList, item, price):
        groceryList[item] = price

        return groceryList

    def printList(self, groceryList):
        subTotal = 0

        for item, price in groceryList.items():
            print(item, ' : ', price)

            subTotal += price

        # sub total
        print()
        print('Subtotal: ', subTotal)
        print()

        # total with tax
        total = '{0:.2f}'.format(subTotal + (subTotal * .07))

        print('Total + .07% tax: ', total)

        return


if __name__ == '__main__':
    main()
