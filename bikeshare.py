import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

OPTIONS = { 'cities': ['chicago', 'new york city', 'washington'],
            'months': ['all', 'january', 'february', 'march', 'april', 'may', 'june'],
            'days': ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New york city, or Washington?\n').lower()
    while city not in OPTIONS['cities']:
        city = input('Please enter valid city. (chicago, new york city, washington)\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month? all, january, february, march, april, may, or june?\n').lower()
    while month not in OPTIONS['months']:
        month = input('Please enter valid month. (all, january, february, march, april, may, or june)\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day? all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday?\n').lower()
    while day not in OPTIONS['days']:
        day = input('Please enter valid day. (all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday)\n')

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
    
    # extract month and day of week ftom the Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month of applicable
    if month != 'all':
        # use the index of months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to get the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to get the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_dayofweek)
    # TO DO: display the most common start hour
    # extract hour from Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Commonly used start station:', common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('commonly used end station:', common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    common_combination = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip:', common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts for each user type:', user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('Counts for each user gender:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_of_birth = df['Birth Year'].min()
    print('Earliest year of birth:', earliest_year_of_birth)
    recent_year_of_birth = df['Birth Year'].max()
    print('Most recent year of birth:', recent_year_of_birth)
    common_year_of_birth = df['Birth Year'].mode()[0]
    print('Most common year of birth:', common_year_of_birth)
    
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
