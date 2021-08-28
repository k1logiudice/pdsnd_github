### Date created
2021-08-28 (28 Aug 2021)

### Project Title
🚲 _**Bike Share project**_

### Description
**Overview:**

Interactively displays US Bike Share usage summary statistics and, optionally, sets of detail records for the user-specified filters.

**Details:**

* **Filters available:**
  1. City:  Chicago, New York City, Washington, or None or Quit
  2. Date:  Day of Week or Month or Both or None or Quit


* **Summary Statistics available:**
      1. Time (hour)
      2. Station
      3. Trip Duration
      4. User Demographics:  user type, gender, birth year


* **Detail record display:**

    Allows the user to optionally view detailed bike share data **5 (five)** records at a time for the user-specified filters.

* **User Experience Features:**
    * Provides the user with multiple opportunities to either confirm their choice or make different selection, to exit or restart the program.
      - If the data frame resulting from the chosen filters is empty, provides the user the opportunity to select a different set of options.
    * Accepts upper case, lower case, or mixed case responses.
    * Minimizes the typing required of the user by accepting responses of:  
      - 1 letter for the city
      - 1 letter for the date filter option
      - 2 letters for the day of the week
      - 3 letters for the month


### Files used
**Code:**

Files containing code:
  * bikeshare.py
  * .github/workflows/manual.yml

**Packages:**  

The following python packages are used in this script:
  * time
  * pandas as pd
  * numpy as np
  * math

**Data:**

Expected bike share data files:
  * chicago.csv
  * new_york_city.csv
  * washington.csv

### Credits
The following resources were used as references when coding this program:
  1. https://docs.python.org/3/
  2. https://pandas.pydata.org/pandas-docs
  3. Udacity "Inroduction to Python" course materials
  4. StackOverflow
  5. GeeksForGeeks
  6. https://www.python.org/dev/peps/pep-0008
  7. https://realpython.com/
