import time
import pandas as pd
import numpy as np
import math

#fpath = 'C:/Users/krist/Documents/Work-Kristi/'  # << EDIT BEFORE SUBMISSION
fpath = ''

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv',
             'quit': 'none'}

# set up day dictionaries, including reversed dictionary
daynum_dict = {'M': 0, 'Tu': 1, 'W': 2, 'Th': 3, 'F': 4, 'Sa': 5, 'Su': 6}
numday_dict = {valnum: keyday for keyday, valnum in daynum_dict.items()}
dayful_dict = {'M': "Monday", 'Tu': "Tuesday", 'W': "Wednesday",
               'Th': "Thursday", 'F': "Friday", 'Sa': "Saturday",
               'Su': "Sunday"}
days_list = [0, 1, 2, 3, 4, 5, 6]
# days_list could be dynamically derived from the data in the selected city's
# file using the following:   days_list = list(df['Start DOW'].unique())

# 1) add dictionary entries where the key is the first letter of the city and
# the value is the city from the cities that are keys in CITY_DATA
# 2) create a string with each city letter and city formatted for readability
# 3) format city instructions string
CITY_LETTER = {}
city_letter_str = ""
for city in CITY_DATA:
    # print(city[0], city)
    CITY_LETTER[city[0]] = city
    city_letter_str += "\t{} for {}\n".format(city[0].upper(), city.title())

city_instructions = ('Enter a letter to choose a single city or to quit:\n{}'
                     '\n<Enter the letter for your choice:> '.
                     format(city_letter_str))

# set up month dictionaries, including reversed dictionary
monthnum_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
nummonth_dict = {valnum: key_mmm for key_mmm, valnum in monthnum_dict.items()}
monthful_dict = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March',
                 'Apr': 'April', 'May': 'May', 'Jun': 'June', 'Jul':
                 'July', 'Aug': 'August', 'Sep': 'September', 'Oct': 'October',
                 'Nov': 'November', 'Dec': 'December'}
fulmonth_dict = {fulmth: key_mmm for key_mmm, fulmth in monthful_dict.items()}
months_list = [1, 2, 3, 4, 5, 6]
# months_lit could be dynamically derived from the data in the selected city's
# file using the following:   months_list = list(df['Start Month'].unique())

# defining filter note here since it is used in multiple functions
filter_note = ('\tNOTE: Figures are calculated using data that '
               'has been filtered'
               '\n\tbased on your selections shown below:')


def get_day(days_list):
    """
    Asks user to specify a day of week filter selection by day abbreviation.
    Accepts any case - upper, lower, or mixed.

    Args:
        (list) days_list - list of day numbers found in the data.
               List is currently hard coded but could be obtained
               dynamically from the selected city file.

    Returns:
        (str) day_abbrev - one or two letter abbreviation in title case of the
                           name of the day of the week to filter by.
    """
    days_list.sort()
    print("="*79)
    day_str = ("Select the day of data you want to see by typing the day "
               "abbreviation (Abbrev) \n"
               "from the list shown below:\n"
               "\t#\tAbbrev\tDay\n\t-\t------\t------------\n")
    for day in days_list:
        day_abbrev = numday_dict.get(day, None)
        day_full = dayful_dict.get(day_abbrev, None)
        day_str += "\t{}\t{}\t{}\n".format(day, day_abbrev, day_full)
    day_str += "<Enter your choice:> "
    # print(day_str)

    day_num = None
    while day_num is None:
        day_choice = input(day_str).title()
        if daynum_dict.get(day_choice, None) is not None:
            day_num = daynum_dict.get(day_choice, None)

        if day_num in days_list:
            day_abbrev = numday_dict.get(day_num, None)
            day_name = dayful_dict.get(day_abbrev, None)
            print("\nYou selected:  day number {}, {} ({}).\n".
                  format(day_num, day_abbrev, day_name))
            # print("month_num Type : ", type(month_num))
        else:
            day_num = None
            print("\n{} is not a valid choice. Please try again.\n".
                  format(day_choice))

    return day_abbrev


def get_month(months_list):
    """
    Asks user to specify a month filter selection by month abbreviation.
    Accepts any case - upper, lower, or mixed.

    Args:
        (list) months_list - list of month numbers found in the data.
               List is currently hard coded but could be obtained
               dynamically from the selected city file.

    Returns:
        (str) month_abbrev - title case three letter abbreviation of the name
              of the month to filter by.
    """
    months_list.sort()
    print("="*79)
    month_str = ("Select the month of data you want to see by typing the first"
                 "\nthree letters of a month (Abbrev)"
                 " from the list shown below:\n"
                 "\t#\tAbbrev\tMonth\n\t-\t------\t------------\n")
    for month in months_list:
        month_abbrev = nummonth_dict.get(month, None)
        month_full = monthful_dict.get(month_abbrev, None)
        # print("\t{}\t{}\t{}".format(month, month_abbrev, month_full))
        month_str += "\t{}\t{}\t{}\n".format(month, month_abbrev, month_full)
    month_str += "<Enter your choice:> "
    # print(month_str)

    month_num = None
    while month_num is None:
        month_choice = input(month_str).title()[0:3]
        if monthnum_dict.get(month_choice, None) is not None:
            month_num = monthnum_dict.get(month_choice, None)

        if month_num in months_list:
            month_abbrev = nummonth_dict.get(month_num, None)
            month_name = monthful_dict.get(month_abbrev, None)
            print("\nYou selected:  month number {}, {} ({}).\n".
                  format(month_num, month_abbrev, month_name))
            # print("month_num Type : ", type(month_num))
        else:
            month_num = None
            print("\n{} is not a valid choice. Please try again.\n".
                  format(month_choice))

    return month_abbrev


def get_city():
    """
    Asks user to specify a city selection by first letter of the city
    or by the city name. Accepts any case - upper, lower, or mixed.

    Returns:
        (str) city - lower case city name to match to the keys of the
              city and file name dictionary, or 'quit'.
    """
    print("="*79)

    city = None
    while city is None:
        city_input = input(city_instructions)
        city_lower = city_input.lower()
        city_lower_1 = city_input.lower()[0]
        # print(city_lower_1, city_lower, city_input)

        if CITY_DATA.get(city_lower, None) is not None:
            selection = "You selected: {}".format(city_input.title())
            city = city_lower
        elif CITY_LETTER.get(city_lower_1, None) is not None:
            selection = ("You selected: {} ({})".format(city_input,
                         CITY_LETTER.get(city_lower_1, None).title()))
            city = CITY_LETTER.get(city_lower_1, None)
        else:
            selection = ("{} is not a valid selection! "
                         "Please try again.".format(city_input))

        print("\n" + selection + "\n")

    return city


def get_date_filter():
    """
    Asks user to choose whether or not a date filter should be
    applied to the data for the selected city and what type of
    date filter should be applied.
    Accepts a single letter or the choice spelled out.
    Accepts any case - upper, lower, or mixed.

    Returns:
        (str) date_choice - lower case date filter choice value
              such as day, month, both, none, quit.
    """
    letter_choice_dict = {'m': 'month', 'd': 'day', 'b': 'both',
                          'n': 'none', 'q': 'quit'}
    choice_letter_dict = {val: key for key, val in letter_choice_dict.items()}
    print("="*79)
    prompt_str = ("Would you like to filter the data by date?"
                  "\nSelect one of the options below:\n"
                  '\t"m" or "month" for month filter.\n'
                  '\t"d" or "day"   for day filter.\n'
                  '\t"b" or "both"  for both month and day filters.\n'
                  '\t"n" or "none"  for no date filter.\n'
                  '\t"q" or "quit"  to quit.\n'
                  '<Enter the letter for your choice:> ')

    date_choice = None
    while date_choice is None:
        choice = input(prompt_str).lower()
        letter = choice[0]
        lookup_choice = choice_letter_dict.get(choice, None)
        lookup_letter = letter_choice_dict.get(letter, None)
        if lookup_choice is not None:
            selection = "You selected: {}".format(choice.title())
            date_choice = choice
        elif lookup_letter is not None:
            selection = "You selected: {}".format(lookup_letter.title())
            date_choice = lookup_letter
        else:
            selection = ("{} is not a valid selection! Please try again.".
                         format(choice))
            date_choice = None

        print("\n" + selection + "\n")

    return date_choice


def get_filters():
    """
    Calls functions for selections for some or all of the following filters:
        function             filter          returns
        ------------------   --------------  --------------
        get_city             city            city
        get_date_filter      date choice     date_choice
        get_month            month (if any)  month_abbrev
        get_day              day (if any)    day_abbrev
    Asks user to choose the filters that will be applied to the data.
    The user must specify a city filter or quit.
    The user must select a date filter choice or quit.
    Month and Day filters, or Both month and day filters are optional.
    See the called functions definitions for further details.

    Returns:
        (str) city - lower case city name to match to the keys of the
              city and file name dictionary, or 'quit'.
        (str) quit_it - set to 'quit' if user chooses the quit option
              in either the get_city or get_date_filter routines.
        (str) date_choice - lower case date filter choice value
              such as day, month, both, none, quit.
        (str) month_abbrev - title case three letter abbreviation of the name
              of the month to filter by or None if no month filter was
              selected.
        (str) day_abbrev - one or two letter abbreviation in title case of the
              name of the day of the week to filter by or None if no day filter
              was selected.
    """
    quit_it = None
    city, date_choice, month_abbrev, day_abbrev = None, None, None, None

    city = get_city()

    if city == 'quit':
        quit_it = 'quit'

    if quit_it != 'quit':
        date_choice = get_date_filter()

        if date_choice == 'quit':
            quit_it = 'quit'

    if quit_it != 'quit':
        month_abbrev = 'all'
        day_abbrev = 'all'
        if date_choice == 'both':
            month_abbrev = get_month(months_list)
            day_abbrev = get_day(days_list)
        elif date_choice == 'month':
            month_abbrev = get_month(months_list)
        elif date_choice == 'day':
            day_abbrev = get_day(days_list)
        elif date_choice == 'none':  # default - added for clarity
            month_abbrev = 'all'
            day_abbrev = 'all'

    print()
    print("="*79)
    print("Here is a summary of your selections:")
    print("\t Quit Now:\t\t{}".format(quit_it))
    print("\t City:\t\t\t{}".format(city))
    print("\t Date Filter:\t{}".format(date_choice))
    print("\t Month:\t\t\t{}".format(month_abbrev))
    print("\t Day:\t\t\t{}".format(day_abbrev))
    print("="*79)
    print()

    return quit_it, city, date_choice, month_abbrev, day_abbrev


def load_data(city, month_abbrev, day_abbrev):
    """
    Loads data for the specified city and filters by month and day
    if applicable.

    Args:
        (str) city - name of the city to analyze - lower case
        (str) month_abbrev - name of the month to filter by, or "all" to apply
              no month filter
        (str) day_abbrev - title case one or two letter abbreviaation for
              name of the day of week to filter by, or "all" to apply no day
              filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("="*79)
    print("Loading file for . . . {} . . .".format(city.title()))
    start_time = time.time()
    # print("Choices: {} {} {}".format(city, month_abbrev, day_abbrev))
    filename = CITY_DATA[city]
    fileandpath = fpath + filename
    # print("Filepath: {}".format(fpath))
    # print("Filename: {}".format(filename))
    print("fileandpath: {}".format(fileandpath))

    # load data file into a dataframe
    df = pd.read_csv(fileandpath)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week and hour from Start Time
    # to create new columns in the dataframe
    df['Start Year'] = df['Start Time'].dt.year
    df['Start Month'] = df['Start Time'].dt.month
    df['Start Month Abbrev'] = df['Start Time'].dt.strftime('%b')
    df['Start DOW'] = df['Start Time'].dt.dayofweek  # weekday()
    df['Start Day'] = df['Start Time'].dt.strftime('%a')
    df['Start Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month_abbrev.lower() != 'all':
        print("Applying Month filter . . . ")
        # use the index of the month abbreviations list to get the
        # corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month_abbrev.lower()) + 1

        # filter by month number to create the new dataframe
        df = df[df['Start Month'] == month]

    # filter by day if applicable
    if day_abbrev.lower() != 'all':
        print("Applying Day filter . . . ")
        # use the index of the day abbreviations list to get the
        # corresponding int
        days = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
        day = days.index(day_abbrev.title())

        # filter by day number to create the new dataframe
        df = df[df['Start DOW'] == day]

    print("\nLoad took %s seconds." % (time.time() - start_time))
    print('='*79)

    return df


def time_stats(df, filters):
    """
    Displays statistics on the most frequent times (hours) of travel.
    Displays statistics for the top 5 travel hours.
    Uses Start Hour to calculate the statistics.

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month & day
        (str) filters - string containing the filters the user selected
              to be displayed in the statistics output

    Returns:
        Nothing returned. Statics are printed to console.

    """

    print()
    print("="*79)
    print('Calculating The Most Frequent Times of Travel . . .\n')
    print(filter_note)
    print(filters)
    start_time = time.time()

    # Display the most popular Month, Day, Hour based on trip counts
    print('-'*79)
    # display the most common month
    top_month = df['Start Month Abbrev'].mode()[0]
    print('Most Popular Start Month:', top_month)
    # display the most common day of week
    top_day_abbrev = df['Start Day'].mode()[0]
    print('Most Popular Start Day  :', top_day_abbrev)
    # display the most common start hour
    top_hour = df['Start Hour'].mode()[0]
    print('Most Popular Start Hour :', top_hour)

    # Display the Top 5 Months, Days, Hours
    #
    # Display Top 5 Months
    print()
    print('-'*79)
    top05_months = (df['Start Month Abbrev'].value_counts(dropna=False).
                    iloc[:5].rename_axis('Month').reset_index(name='Trips'))
    print("Top 5 Most Popular Start Months with trip count:\n")
    print(top05_months)

    # Display Top 5 Days
    print()
    print('-'*79)
    top05_day_abbrev = (df['Start Day'].value_counts(dropna=False).
                        iloc[:5].rename_axis('Day').reset_index(name='Trips'))
    print("Top 5 Most Popular Start Days with trip count:\n")
    print(top05_day_abbrev)

    # Display Top 5 Hours
    print()
    print('-'*79)
    top05_hours = (df['Start Hour'].value_counts(dropna=False).
                   iloc[:5].rename_axis('Hour').reset_index(name='Trips'))
    print("Top 5 Most Popular Start Hours with trip count:\n")
    print(top05_hours)

    print("\nTime Stats took %s seconds." % (time.time() - start_time))
    print('='*79)


def station_stats(df, filters):
    """
    Displays statistics on the most popular Start Station and top 5.
    Displays statistics on the most popular End Station and top 5.
    Displays statistics on the most popular Trip and top 5. A trip is
    defined by the Start Station and End Station combination.

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month & day
        (str) filters - string containing the filters the user selected
              to be displayed in the statistics output

    Returns:
        Nothing returned. Statics are printed to console.
    """

    print()
    print("="*79)
    print('Calculating The Most Popular Stations and Trip . . .\n')
    print(filter_note)
    print(filters)
    start_time = time.time()

    # Display most commonnly used start station, end station and
    # start-end combination
    print()
    print('-'*79)

    # display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', top_start_station)

    # display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', top_end_station)

    # display most frequent combination of start station and end station trip
    top_trip_df = (df.value_counts(['Start Station', 'End Station']).
                   iloc[:1].reset_index(name='Trips'))
    top_trip_dict = top_trip_df.to_dict()  # see sample below
    # {'Birth Year': {0: 1989.0}, 'Trips': {0: 14666}}
    # print(top_trip_dict)
    top_start = top_trip_dict.get('Start Station').get(0)
    top_end = top_trip_dict.get('End Station').get(0)
    top_count = math.ceil(top_trip_dict.get('Trips').get(0))
    print("Most popular Trip:\n\tStart Station: {}"
          "\n\tEnd Station  : {}\n\tNumber of trips: {}".
          format(top_start, top_end, top_count))

    # Display Top 5 start stations, end stations ans start-end combinations
    print('-'*79)
    # Display Top 5 start stations
    top05_start_stations = (df['Start Station'].value_counts(dropna=False).
                            iloc[:5].rename_axis('Start Station').
                            reset_index(name='Trips'))
    print("Top 5 Most Popular Start Stations with trip count:\n")
    print(top05_start_stations)
    print('-'*79)

    # Display Top 5 end stations
    top05_start_stations = (df['End Station'].value_counts(dropna=False).
                            iloc[:5].rename_axis('End Station').
                            reset_index(name='Trips'))
    print("Top 5 Most Popular End Stations with trip count:\n")
    print(top05_start_stations)
    print('-'*79)

    # Display Top 5 start-end combinations
    top05_trips = (df.value_counts(['Start Station', 'End Station']).
                   iloc[:5].reset_index(name='Trips'))
    print("Top 5 Most Popular Trips (Starting and Ending Stations) "
          "with trip count:\n")
    print(top05_trips)
    print('-'*79)

    print("\nStation Stats took %s seconds." % (time.time() - start_time))
    print('='*79)


def trip_duration_stats(df, filters):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month & day
        (str) filters - string containing the filters the user selected
              to be displayed in the statistics output

    Returns:
        Nothing returned. Statics are printed to console.
    """
    print()
    print("="*79)
    print('Calculating Trip Duration Stats . . .\n')
    print(filter_note)
    print(filters)
    start_time = time.time()

    # display total travel time
    print()
    print("Total Trip Duration: {} seconds".
          format(math.ceil(df['Trip Duration'].sum())))

    # display mean travel time
    print("Average Trip Duration: {} seconds".
          format(math.ceil(df['Trip Duration'].mean())))

    print("\nDuration Stats took %s seconds." % (time.time() - start_time))
    print('='*79)


def user_stats(df, filters):
    """
    Displays demographics statistics on the bikeshare users.
    Demographic attributes: User Types, Gender, Birth Year.
    Gender and Birth Year statistics are displayed only if
    those attributes exist in the file for the selected city.

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month & day
        (str) filters - string containing the filters the user selected
              to be displayed in the statistics output

    Returns:
        Nothing returned. Statics are printed to console.
    """
    print()
    print("="*79)
    print('Calculating User Stats . . .\n')
    print(filter_note)
    print(filters)
    start_time_all = time.time()

    # Display counts of user types
    print("-"*79)
    print('Calculating User Stats for User Type . . .\n')
    start_time = time.time()
    user_types = (df['User Type'].value_counts(dropna=False).
                  rename_axis('User Type').reset_index(name='Trips'))
    print("User Types by trip count:\n")
    print(user_types)
    print("\nUser Types Stats took %s seconds." % (time.time() - start_time))

    # Get list of columns in the dataframe to use to check whether or not the
    # Gender and Birth Year columns are available in the selected file.
    col_list = list(df.columns)
    # print(col_list)

    # Display counts of gender
    if 'Gender' in col_list:
        print("-"*79)
        print('Calculating User Stats for Gender . . .\n')
        start_time = time.time()
        genders = (df['Gender'].value_counts(dropna=False).
                   rename_axis('Gender').reset_index(name='Trips'))
        print("User Gender by trip count:\n")
        print(genders)
        print("\nGender Stats took %s seconds." % (time.time() - start_time))
    else:
        print()
        print("The data for the selected city does not have a Gender column.")
        print()

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in col_list:
        print("-"*79)
        print('Calculating User Stats for Birth Year . . .\n')
        start_time = time.time()
        top_years = (df['Birth Year'].value_counts(dropna=False).
                     iloc[:5].rename_axis('Birth Year').
                     reset_index(name='Trips'))
        print("Top 5 User Birth Years by trip count:\n")
        print(top_years)
        top_year_df = (df['Birth Year'].value_counts(dropna=True).
                       iloc[:1].rename_axis('Birth Year').
                       reset_index(name='Trips'))
        top_year_dict = top_year_df.to_dict()  # see sample below
        # {'Birth Year': {0: 1989.0}, 'Trips': {0: 14666}}
        top_year = math.ceil(top_year_dict.get('Birth Year').get(0))
        top_count = math.ceil(top_year_dict.get('Trips').get(0))
        print()
        print("Earliest    Birth Year: {}".
              format(math.ceil(df['Birth Year'].min())))
        print("Most Recent Birth Year: {}".
              format(math.ceil(df['Birth Year'].max())))
        print("Most Common Birth Year: {} (excluding NaN) "
              "has a trip count of: {}".format(top_year, top_count))
        print()
        print("Birth Year Stats took %s seconds." % (time.time() - start_time))
        print("-"*79)
    else:
        print()
        print("The data for the selected city does not have a "
              "Birth Year column.")
        print()

    print()
    print("User Stats took %s seconds total." % (time.time() - start_time_all))
    print('='*79)


def display_raw(df, len_df):
    """
    Displays raw data in sets of five rows for each request.

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month & day
        (int) len_df - length of the dataframe, i.e., the number of rows.
              Used to ensure the print of the raw data doesn't go beyond
              the end of file.

    Returns:
        Nothing returned. Raw data rows are printed to console.
    """
    chunk_size = 5  # print 5 rows of raw data at a time
    start_index = 0  # start at index 0
    see_more = 'y'
    while see_more.lower()[0] == 'y' and start_index < len_df:

        print()
        for i in range(1,   chunk_size + 1):
            if start_index < len_df:
                print(df[start_index:start_index + 1].to_dict('records'))
            start_index += 1

        if start_index < len_df:
            see_more = input("\nWould you like to see 5 MORE lines raw data? "
                             "\n<Enter 'y' for yes or 'n' for no:> ")
        else:
            print()
            print("****************** End of Data Reached ******************")
            print("Quitting raw data display. Toodles!\n")

    if see_more.lower()[0] != 'y':
        print("Quitting raw data display. Toodles!\n")


def get_raw(df):
    """
    Asks user to choose whether or not they would like to view raw data.
    Calls function to display the raw data 5 rows at a time if user
    responds in the affirmative.

    Calls the following functions:
        display_raw - displays raw data 5 rows at a time.

    Args:
        (df) df - Pandas DataFrame containing city data filtered by month & day

    Returns:
        Nothing returned. Raw data rows are printed to console.
    """
    see_raw = input("Would you like to see 5 lines of raw data? "
                    "\n<Enter 'y' for yes or 'n' for no:> ")
    if see_raw.lower()[0] == 'y':
        print("\nOK. Displaying raw data . . .\n")
        len_df = len(df)
        display_raw(df, len_df)
    else:
        print("\nOK. NOT displaying raw data.\n")


def confirm_choice():
    """
    Asks user to confirm the city and date filtering selections.

    Returns:
        (str) confirm - 'y' means the user has confirmed the selections
              and the program will continue. 'n' or any response other than
              'y' means the program will give the user the opportunity to
              restart and make new selections or quit.
    """

    confirm_input = input("Please confirm your selection."
                          "\n<Enter 'y' to confirm, 'n' to try again:> ")
    confirm = confirm_input[0].lower()
    if confirm == 'y':
        print("Confirmed.")
        confirm = 'y'
    else:
        print("Trying again.\n")
        confirm = 'n'
    return confirm


def main():

    print("\nHello! Let's explore some US Bikeshare data!\n")

    while True:

        quit_it, city, date_choice, month_abbrev, day_abbrev = get_filters()

        if quit_it == 'quit':
            print("Quitting. Toodles!")
            break

        filters = ('\t\tCity: {}, Date Filters: {}, Month: {}, Day: {}.\n'.
                   format(city.title(), date_choice, month_abbrev.title(),
                          day_abbrev.title()))

        confirm = confirm_choice()
        if confirm == 'y':
            df = load_data(city, month_abbrev, day_abbrev)
            if df.empty:
                print()
                print('DataFrame is empty after filtering!')
                print('Please select different options.')
            else:
                time_stats(df, filters)
                station_stats(df, filters)
                trip_duration_stats(df, filters)
                user_stats(df, filters)
                get_raw(df)

        restart = input("\nWould you like to restart?"
                        "\n<Enter 'R' to restart or"
                        " or 'Q' to quit:> \n")
        if restart.lower()[0] != 'r':
            print("Quitting. Toodles!")
            break


if __name__ == "__main__":
    main()
