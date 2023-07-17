import matplotlib.pyplot as plt
import math

def main():
    CAFFEINE_HALFLIFE = 5
    TIME_INCREMENT = 0.25

    drinks = []
    # get caffiene from user
    while True:
        # get individual caffeine input
        caffeine = get_numerical_input("How much caffeine did you have (mg)?  ")
        time = get_numerical_input("How long ago did you have it (hours)? ")
        drinks.append((caffeine, time))
        done = not get_y_n_input("Did you have more caffeine? (y/n) ")
        if done:
            break
        print()
    
    print("You currently have: " + str(round(calculate_caffeine(drinks, CAFFEINE_HALFLIFE), 2)) + "mg of caffeine in your system")
    # graph
    if (get_y_n_input("Would you like a graph of your caffeine intake? ")):
        (x, y) = calculate_caffeine_over_time(drinks, CAFFEINE_HALFLIFE, TIME_INCREMENT)
        plt.plot(x, y)
        plt.xlim(drinks[0][1], 0)
        plt.xlabel("Time (hours)")
        plt.ylabel("Caffeine (mg)")
        plt.title("Caffeine Intake")
        plt.show()


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
        total_caffeine += calculate_halflife(drink[0], drink[1], CAFFEINE_HALFLIFE)
    return total_caffeine

def calculate_caffeine_over_time(drinks, CAFFEINE_HALFLIFE, time_increment):
    t = 1 / time_increment
    x = []
    y = []
    # get times to sort drinks
    drinks = sort_list_of_tuple_by_second_value_smallest_first(drinks)
    # calculate every 30 min increment
    current_caffeiene = 0
    # for i in sorted_drinks:
    for i in range(int(drinks[0][1] * t), 0, -1):
        # append corresponding time
        x.append(i / t)
        # calculate current caffeine levels
        applicable_drinks = []
        for k in drinks:
            if (k[1] >= i / t):
                applicable_drinks.append((k[0], k[1] - i / t))

        current_caffeiene = calculate_caffeine(applicable_drinks, CAFFEINE_HALFLIFE)
        
        y.append(current_caffeiene)
    return (x, y)

def calculate_halflife(amount, time_elpased, halflife):
    return amount * 0.5 ** (time_elpased / halflife)

def sort_list_of_tuple_by_second_value_smallest_first(list):
    for i in range(0, len(list)):
        for j in range(0, len(list) - i - 1):
            if (list[j][1] < list[j + 1][1]):
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

if __name__ == "__main__":
    main()
