from Practical_06.guitar import Guitar


def main():
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 1823.40))
    guitars.append(Guitar("line 6 JTV-59", 2010, 1219.5))


    print("These are my Guitars: ")

    if guitars is not None:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(Vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
                        {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
