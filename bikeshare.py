import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("Please enter one of the following: Chicago, New York City, or Washington?\n").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Error: Invalid input. \n")

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
    while True:
        month = input("Please enter the month: (example: January, February, March, April, May, ... or all?\n").lower()
        if month in months:
            break
        else:
            print("Error: Invalid input. \n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Please enter the day: (example Monday, Tuesday ... or all?\n").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a day of the week or all.")

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    if city == "new york city":
        df = pd.read_csv(f'new_york_city.csv')
    else: df = pd.read_csv(f'{city}.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print(f"The most common month in the dataset is: {most_common_month}")

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of week in the dataset is: {most_common_day}")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f"The most common start hour in the dataset is: {most_common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating Station Statistics...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {most_common_start}")

    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {most_common_end}")

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    print(f"The most frequent combination of start station and end station trip is: {most_common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print(f"Total travel time: {total:.2f} seconds")

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    for user_type, count in user_types.items():
        print(f"{user_type}: {count}")

    # Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("\nCounts of gender:")
    for gender, count in gender_counts.items():
        print(f"{gender}: {count}")

    # Display earliest, most recent, and most common year of birth
    print(f"\nEarliest year of birth: {int(df['Birth Year'].min())}")
    print(f"Most recent year of birth: {int(df['Birth Year'].max())}")
    print(f"Most common year of birth: {int(df['Birth Year'].mode()[0])}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
