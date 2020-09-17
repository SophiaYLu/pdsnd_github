import time
import pandas as pd
import numpy as np

CITY_DATA = { 'C': 'chicago.csv',
              'N': 'new_york_city.csv',
              'W': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please select your city among Chicago, Ner York City and Washington. Type in C, N or W for your city selection:')
    while city not in ['C', 'N', 'W']:
        city = input('That\'s not a valid input. Please type in C, N or W for your city selection:')

    # get user input for month (all, january, february, ... , june)
    month = input('Please select a month bewtween 1 (Jan) and 6 (June) as filter or skip this option by selecting all. Please type in a number for the month or select all:')
    while month not in ['1', '2', '3', '4', '5', '6', 'all']:
        month = input('That\'s not a valid input. Please type in a number for the month or select all:')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select a day of the week as filter or skip this option by selecting all. Please type in full name such as Sunday or all:')
    while day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all']:
        day = input('That\'s not a valid input. Please type in full name such as Sunday or all:')

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == int(month)]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    view = input('Would like to get a glimpse of the data based on your filter? Type in yes/no: ')
    df1 = df

    while view != 'no':
        if view == 'yes':
            print(df1.head())
            df1 = df1.iloc[5:]
            view = input('Do you want to see the next 5 rows? Please type in yes/no: ')
        else:
            view = input('That\'s not a valid input. Please type in yes/no: ')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Common Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The Most Common Day of Week:', popular_day)

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('The Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The Most Commonly Used Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The Most Commonly Used End Station:', popular_end)

    # display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + '_' + df['End Station']
    popular_trip = df['start_end'].mode()[0]
    print('The Most Frequent Combination of Start Station and End Station Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time in Seconds:', total_time)

    # display mean travel time
    ave_time = df['Trip Duration'].mean()
    print('Mean Travel Time in Seconds:', ave_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('No gender data available.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('\nThe earliest year of birth:', earliest)
        print('\nThe most recent year of birth:', recent)
        print('\nThe most common year of birth:', common)
    else:
        print('No year of birth data available.')

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
