restaurants = [{"name": "The Great Restaurant", "rating": 4.5, "cuisine": "Italian", "active": True},
              {"name": "Sushi Place", "rating": 4.0, "cuisine": "Japanese", "active": False},
              {"name": "Burger Joint", "rating": 3.5, "cuisine": "American", "active": False},]

# welcome to function to greet the user
def welcome():
    print('Welcome to the Restaurant Management System!')
    print('Please select an option from the menu below:\n')

# print the options for the user
def options():
    print('1. Add a restaurant')
    print('2. View all restaurants')
    print('3. Active/Deactivate a restaurant')
    print('4. Exit\n')

# get user input for the option
def back_to_menu():
    input('press enter to back to menu\n')
    main()

# function to handle invalid options
def invalid_option():
    print('Invalid option, please try again.\n')
    main()

# function to close the program
def close_program():
    print('Exiting the program. Goodbye!\n')

# function to get user input and call the appropriate function based on the input
def get_user_input():
    try:
        input_user = int(input('Please select an option: '))

        if input_user == 1:
            add_restaurant()
        elif input_user == 2:
            view_restaurants()
        elif input_user == 3:
            active_restaurant()
        elif input_user == 4:
            close_program()
        else:
            invalid_option()
    except:
        invalid_option()

# functions for add a new restaurant
def add_restaurant():
    name = input('Please enter the restaurant name: ')
    rating = float(input('Please enter the restaurant rating (0-5): '))
    cuisine = input('Please enter the restaurant cuisine: ')

    restaurant_data = {"name": name,
                       "rating": rating,
                       "cuisine": cuisine,
                       "active": False
                       }

    restaurants.append(restaurant_data)
    back_to_menu()

# function to view all restaurants
def view_restaurants():
    print(f"{'Restaurant Name:':<25} {'Rating':<10} {'Cuisine':<10} {'Status'}")
    print('-' * 60)
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_rating = restaurant['rating']
        restaurant_cuisine = restaurant['cuisine']
        restaurant_active = 'Active' if restaurant['active'] else 'Inactive'
        print(f"{restaurant_name:<25} {restaurant_rating:<10} {restaurant_cuisine:<10} {restaurant_active}")
    print('\n')

    back_to_menu()

# function to activate a restaurant
def active_restaurant():
    restaurant_name = input('Please enter the name of the restaurant to activate/deactivate: ')
    for restaurant in restaurants:
        if restaurant['name'].lower() == restaurant_name.lower():
            restaurant['active'] = not restaurant['active']
            print(f"Restaurant '{restaurant['name']}' is now {'active' if restaurant['active'] else 'inactive'}.")
            break
    else:
        print(f"No restaurant found with the name '{restaurant_name}'.")

    back_to_menu()

# main function to run the program
def main():
    welcome()
    options()
    get_user_input()

if __name__ == '__main__':
    main()