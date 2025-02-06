# Bikeshare.py Method Explanations

## get_filters()
This method interacts with the user to get input for filtering the bikeshare data. It:
- Prompts the user to select a city (Chicago, New York City, or Washington)
- Asks for a month to filter by (January to December, or 'all')
- Requests a day of the week to filter by (Monday to Sunday, or 'all')
- Uses while loops to ensure valid input for each prompt
- Returns the selected city, month, and day as strings

## load_data(city, month, day)
This method loads and filters the data based on the user's input:
- Reads the appropriate CSV file based on the selected city
- Converts the 'Start Time' column to datetime
- Creates new columns for month and day of the week
- Filters the dataframe by month if a specific month was chosen
- Filters the dataframe by day if a specific day was chosen
- Returns the filtered dataframe

## time_stats(df)
Calculates and displays statistics about the most frequent times of travel:
- Finds and prints the most common month
- Finds and prints the most common day of the week
- Finds and prints the most common start hour

## station_stats(df)
Calculates and displays statistics about the most popular stations and trip:
- Finds and prints the most commonly used start station
- Finds and prints the most commonly used end station
- Finds and prints the most frequent combination of start station and end station trip

## trip_duration_stats(df)
Calculates and displays statistics on the total and average trip duration:
- Calculates and prints the total travel time
- Prints the mean travel time

## user_stats(df)
Displays statistics on bikeshare users:
- Counts and displays the number of users by type
- Counts and displays the number of users by gender
- Finds and displays the earliest, most recent, and most common year of birth

## main()
The main method that runs the program:
- Calls get_filters() to get user input
- Calls load_data() to load and filter the data
- Calls the various statistics methods to display the results
- Asks if the user wants to restart and loops if the answer is yes