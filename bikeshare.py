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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city do you want to filter? (eg. chicago, new york city, washington)\n").lower()
    while city not in CITY_DATA:
        print("\nWrong input please try again!")
        city = input("Which city do you want to filter? eg. chicago, new york city, washington:\n").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month do you want to filter? (eg. january, february etc.)\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day do you want to filter? (eg. monday, tuesday etc.)\n").lower()

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
        # use the index of the months list to get the corresponding int
        try:
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1

            # filter by month to create the new dataframe
            df = df[df['month'] == month]
        except ValueError:
            print('Invalid input for month, applying default "all" ....')

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        try:
            df = df[df['day_of_week'] == day.title()]
        except IndexError:
            print('Invalid input for week day, applying default "all" ....')


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("The most common month is:", months[df['month'].mode()[0] - 1].title())

    # TO DO: display the most common day of week
    print("The most common day of week is:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common hour is:", pd.to_datetime(df['Start Time']).dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Frequently used start station and end station are {} and {}.".
          format(df['Start Station'].mode()[0], df['Start Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The average travel time is:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('\nTotal number of gender:\n', df['Gender'].value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe earliest birth year:', df['Birth Year'].min())
        print('The most recent birth year:', df['Birth Year'].max())
        print('The most common birth year:', df['Birth Year'].mode()[0])
    except KeyError:
            print('Gender & Birth Year Key does not exist for this city!')
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        print('\n'+ ('='*20) + ' DISPLAY RESULTS ' + ('='*20))

        def display_stats(stats, display):
            """
            This display statistics base on the argument supplied
            Arg:
                (str) stats - statistics to display
                (func) display - statistical function to call
            """
            input_text = input('\nWould you like to see {} statistics? Enter yes or no.\n'.format(stats))
            if input_text.lower() == 'yes':
                display(df)

        # display time statistics
        display_stats('time', time_stats)
        # display station statistics
        display_stats('station', station_stats)
        # display trip statistics
        display_stats('trip duration', trip_duration_stats)
        # display user statistics
        display_stats('user', user_stats)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            print('\nThanks for exploring the US bikeshare data, hope you enjoy!')
            break
        elif restart.lower() != 'yes':
            print("\nIncorrect response please try again.")
            restart = input('\nWould you like to restart? Enter yes or no.\n')

if __name__ == "__main__":
    main()
