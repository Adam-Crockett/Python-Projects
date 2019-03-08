import json
from bokeh.plotting import figure, show, output_file

# This is a dictionary of converting month number to english.
months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July",
          "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}


def get_database(path="bday_database"):
    """Access the JSON file that holds our database."""
    try:
        with open(path) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The database you are trying to access does not exist.")
    else:
        return data


def update_database(data, path="bday_database"):
    """Update the database with user input."""
    with open(path, "w") as file:
        json.dump(data, file)


def show_keys(data):
    """Display the names we have in the database."""
    print("The scientists we have access to are:")
    for name in data:
        print(name.title())


def get_birthday(name, data):
    """Get the value from the input key. Returns false if the key is not in JSON."""
    if name in data:
        return data[name]
    else:
        return False


def add_person(data):
    """Add new key/value pair to database."""
    try:
        name = input("What scientist would you like to add: ").lower()
    except TypeError:
        print("You did not give us a name we can use.")
    else:
        if name not in data:
            b_day = input("Using mm/dd/yyyy format please enter the birthday: ")
            data[name] = b_day
            update_database(data)

            print("{} with a birthday of {} has been added to the database.".format(name.title(), data[name]))


def month_count(data):
    """Creates a dictionary, then evaluates the database and adds up the birthdays in each month."""
    month_coll = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0,
                  "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}

    for name in data:  # For each name in the database
        if data[name][0:2] in months:  # If the first two elements(the month number) is in the months dict
            month_coll[months[data[name][0:2]]] += 1  # Add +1 to the corresponding month count

    return month_coll  # Return the month count


def plot_data(data):
    """Use bokeh module to plot the birth months of the scientists."""
    output_file("plot.html")
    x = [x for x in data]
    print(x)
    y = [data.get(y) for y in data]
    p = figure(plot_width=800, x_range=x, title="Number of Scientists Born Each Month")
    p.vbar(x=x, top=y, width=0.2)
    show(p)


if __name__ == '__main__':
    """Interaction with user for database, functions have a default path for JSON if no entry given."""
    entry = ""
    print("Hello, welcome to the scientist birthday database.")

    # Ask if user has their own database
    custom_database = input("Do you have your own database? If so enter file path, else say 'no': ")
    if custom_database == "no":
        print("Loading our database...")
        database = get_database()  # Loads our default JSON
    else:
        print("Loading your database...")
        database = get_birthday(custom_database)

    show_keys(database)  # Display the current keys(scientists in the database)
    print("__________________________________________________________________________")
    print("Enter 'quit' to stop and plot data or 'add' to input new scientist.")
    print("__________________________________________________________________________")

    while entry.lower() != "quit":  # Loop of getting user input
        try:
            entry = input("Who's birthday would you like to view?").lower()
        except TypeError:
            print("You did not use valid input.")
        else:
            if get_birthday(entry, database):
                print("{} had their birthday on {}".format(entry.title(), get_birthday(entry, database)))
            elif entry == "add":
                add_person(database)
            elif entry == "quit":
                print("Quantity of birthdays in each month:")
                plot_data(month_count(database))
                break
            else:
                print("The person you are looking for is not in our system.")

    print("Thank you for using our database!")
