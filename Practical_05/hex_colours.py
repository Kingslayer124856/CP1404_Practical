

COLOUR_CODES = {"blue": "#0000ee", "pink": "#ff1493", "purple": "#9932cc",
                "gold": "#ffc125", "turquoise": "#48d1cc", "green": "#32cd32"
                "red" "#ff0000", "brown": "#8b4513", "yellow": "#ffff00", "black": "#000000"
               }


def main():
    colour_name = input("Enter a colour: ")
    while colour_name != "":
        print("The code for \"{}\" is {}".format(colour_name,
                                                 COLOUR_CODES.get(colour_name)))
        colour_name = input("Enter colour name: ")
main()