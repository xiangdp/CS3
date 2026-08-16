def yearquestion():
    while True:
        userinput = input("Enter your birth year: ")
        try:
            birthyear = int(userinput)
            if birthyear >= 1900:
                return birthyear
            print("Invalid year, it should not be earlier than 1900.")
        except ValueError:
            print(
                "Invalid text, please enter ONLY your birth year fully in integer form."
            )


def decideoutput(birthyear):
    zodiacnumber = (birthyear - 1900) % 12
    zodiaclist = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)",
    ]
    zodiac = zodiaclist[zodiacnumber]
    print(f"Your Chinese Zodiac Sign is : {zodiac}")


def main():
    result = yearquestion()
    decideoutput(result)


main()