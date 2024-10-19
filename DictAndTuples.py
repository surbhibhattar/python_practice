'''
https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_tuple_exercise.md

'''

import math

countries_info = {
    "china":143,
    "india":136,
    "usa":32,
    "pakistan":21
}

def get_countries_info():
    userInput = input("Enter either print, add, remove, query: ")
    if userInput == "print":
        for country in countries_info:
            print(country+'==>'+str(countries_info[country]))
    elif userInput == "add":
        newCountry = input('Enter country name: ')
        if(newCountry in countries_info):
            print(newCountry + 'already exists')
        else:
            population = input('Enter '+newCountry+'\'s population: ')
            countries_info[newCountry] = population
            print(countries_info)
    elif userInput == "remove":
        checkCountry = input('Enter country name: ')
        if(checkCountry in countries_info):
            del countries_info[checkCountry]
            print(countries_info)
        else:
            print(checkCountry+' not found')
    elif userInput == "query":
        checkCountry = input('Enter country name: ')
        if(checkCountry in countries_info):
            print('Population of '+checkCountry+': '+str(countries_info[checkCountry]))
        else:
            print(checkCountry+' not found')

# get_countries_info()

'''Question2'''

stock_prices = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}


def print_stock(stock_prices):
    for key, values in stock_prices.items():
        avg = 0
        for v in values:
            avg += v
        avg = avg / len(values)
        print(f"{key} ==> {values} ==> avg: {avg}")


def convert_str_to_list(str):
    split_list = list(str.split(","))
    new_list = []
    for each in split_list:
        new_list.append(float(each))
    return new_list

def main_function():
    choice = input("enter print or add")
    if choice == "print":
        print_stock(stock_prices)
    elif choice == "add":
        stock_name = input("enter stock name")
        stock_price = input("enter stock price")
        if stock_name not in stock_prices:
            stock_prices[stock_name] = convert_str_to_list(stock_price)
            print_stock(stock_prices)
        else:
            stock_prices[stock_name].append(float(stock_price))
            print_stock(stock_prices)


# if __name__ == "__main__":
   # main_function()


'''Question 3'''

def circle_calc(radius):
    area = math.pi * math.pow(radius, 2)
    circumeference = 2 * math.pi * radius
    diameter = 2*radius
    return {area,circumeference,diameter}

print(circle_calc(5))