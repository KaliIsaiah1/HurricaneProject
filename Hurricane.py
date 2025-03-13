

def classify_hurricane(wind_speed):
    """Classify the hurricane category based on wind speed."""
    if wind_speed < 0:
        return "Error: Wind speed cannot be negative."
    elif wind_speed < 39:
        return "Not a tropical storm or hurricane."
    elif wind_speed < 74:
        return "Tropical Storm: 39 – 73 mph."
    elif 74 <= wind_speed <= 95:
        return "Category 1: Very dangerous winds will produce some damage."
    elif 96 <= wind_speed <= 110:
        return "Category 2: Extremely dangerous winds will cause extensive damage."
    elif 111 <= wind_speed <= 129:
        return "Category 3: Devastating damage will occur."
    elif 130 <= wind_speed <= 156:
        return "Category 4: Catastrophic damage will occur."
    else:  # wind_speed >= 157
        return "Category 5: Catastrophic damage; high devastation."


def main():
    # Prompt the user for wind speed input
    user_input = input("Please enter the wind speed in miles per hour (mph): ")

    try:
        # Convert input to an integer
        wind_speed = int(user_input)

        # Classify the hurricane category and display the result
        result = classify_hurricane(wind_speed)
        print(result)

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for wind speed.")


# Call the main function to run the program
if __name__ == "__main__":
    main()
