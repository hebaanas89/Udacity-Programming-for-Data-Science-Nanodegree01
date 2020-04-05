{"now":1584544378437,"date":"Wed Mar 18 2020 15:12:58 GMT+0000 (UTC)"}

import time
import pandas as pd
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

print('this program developed to allow user to explore an US bikeshare system database to retrieve information from database')
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or
                      "all" to apply no month filter
        (str) day - name of the day of week to filter by, or
                    "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('choose a city to explore the bikeshare data. ' +
                     'Chicago, New York City, or Washington?\n')
        if city.lower() in CITY_DATA.keys():
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Specify the month of data to explore. All, January ' +
                      'February, March, April, May, or June?\n')
        if month.lower() in ['All', 'january', 'february', 'march',
                             'april', 'may', 'june']:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Specify the day of data to explore. ' +
                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +
                    'Saturday, Sunday?\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday',
                           'friday', 'saturday', 'sunday']:
            break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month
    and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all"
                      to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
                    to apply no day filter
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

    # filter by month
    if month != 'all':
        # use the index of the months list
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n displaying The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    print('\n the Most Common Month is:')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('\n the Most Common Day is:')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\n the Most Common Start Hour is:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    print('\n the Most Common Start Station is:')
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\n the Most Common End Station is:')
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\n the Most Frequency Start and end Combination')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()

    # display total travel time
    print('\n the Total Travel Time is:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].sum())))

    # display mean travel time
    print('\n the Mean Travel Time is:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User Types:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('\nCounts of Genders:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include genders')

    # Display earliest, most recent, and most common year of birth
    print('\nEarliest, Latest & Most Common Date of Birth:')
    try:
        print('Earliest: {}\nLatest: {}\nMost Common: {}'
              .format(df['Birth Year'].min(), df['Birth Year'].max(),
                      df['Birth Year'].mode()[0]))
                      Print('this is a program allow the user to explore an US bikeshare system database and retrieve information from the database')
    except:
        print('Data does not include date of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Iterate through 5 entries at a time.
    Returns:
        Print five row entries of data to terminal
    """

    view_more = 'yes'
    while view_more == 'yes':
        for i in df.iterrows():
            count = 0
            while count < 5:
                print(i)
                count += 1
            reaction = input('\n Do you like to  display more data ? Yes or No?\n')
            if reaction.lower() == 'no':
                view_more = 'no'
                break


def main():
    """Main body of program"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Yes or No?\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
