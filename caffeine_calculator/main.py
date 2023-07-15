def main():
    CAFFEINE_HALFLIFE = 5
    drinks = []
    # get caffiene from user
    while True:
        # get individual caffeine input
        caffeine = get_numerical_input("How much caffeine did you have (mg)?  ")
        time = get_numerical_input("How long ago did you have it (hours)? ")
        done = get_y_n_input("Did you have more caffeine? (y/n) ")
        if not done:
            drinks.append((caffeine, time))
            break
        print()
    
    print("You currently have: " + str(round(calculate_caffeine(drinks, CAFFEINE_HALFLIFE), 2)) + "mg of caffeine in your system")

def get_numerical_input(message):
    while True:
        response = input(message)
        try:
            responseNum = eval(response)
            return responseNum
        except:
            print("Please input a number!")

def get_y_n_input(message):
    while True:
        response = input(message).lower()
        if (response == "y" or response == "yes"):
            return True
        elif (response == "n" or response == "no"):
            return False
        
def calculate_caffeine(drinks, CAFFEINE_HALFLIFE):
    total_caffeine = 0
    for drink in drinks:
        total_caffeine += drink[0] * 0.5 ** (drink[1] / (CAFFEINE_HALFLIFE / 2))
    return total_caffeine

if __name__ == "__main__":
    main()
