
print("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")

import statistics


def main():
    print("Devops Lab 2")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")

def get_user_input():
    inputlist = [int(x) for x in input().split(',')]
    print("Input are:", inputlist)
    return inputlist

def calc_average(inputlist):
    total = 0
    for temp in inputlist:
        total = total + temp
    number = len(inputlist)
    avrg = total / number
    return avrg

def find_min_max(inputlist):
    minmax = min(inputlist), max(inputlist)
    return minmax


def sort_temperature(inputlist):
   inputlist.sort()
   return inputlist

def calc_median_temperature(inputlist):
    v = statistics.median(inputlist)
    return v

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    average = calc_average(num_list)
    print("The average temperature is:", average)
    minmax = find_min_max(num_list)
    print( "The minimum and maximum temperature is: ", minmax )
    sort = sort_temperature(num_list)
    print("The sorted temperature is :", sort)
    median = calc_median_temperature(num_list)
    print("The median temperature is: ", median)



if __name__ == "__main__":
    main()

