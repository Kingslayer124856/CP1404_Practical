


from Practical 6.Guitairs! import Guitairs!

THIS_YEAR = 2018

def run_test():
    name="Gibson L-5 CES"
    year= 1922
    cost=1823.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)
    print("{} get_age() -Expected {}.Got".format(guitar.name, 95,
                                                guitar.get_age()))
    print("{} get_age() -Expected {}.Got".format(guitar.name, 5,
                                                 guitar.get_age()))
    print()
    print("{} is_vintage() - Expected {}.Got{}",format(guitar.name,
                                                       True,
                                                       guitar.is_vintage()))
    print("{} is_vintage() -Expected {}.Got{}".format(onther.name,
                                                      False,
                                                      other.is_vinatge))
if __name__ == '__main__':
    run_test()

