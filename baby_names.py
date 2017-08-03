# See: https://github.com/guipsamora/pandas_exercises/blob/master/06_Stats/US_Baby_Names/Exercises_with_solutions.ipynb

import io

import pandas as pd
import requests
import requests_cache

requests_cache.install_cache(__file__)

def number_of_female_names(baby_names):
    # Are there more male or female names in the dataset?
    return baby_names['Gender'].value_counts()#['F']

def top_five_names(baby_names):
    # group the data
    names = baby_names.groupby("Name").sum()

    # sort it from the biggest value to the smallest one
    return names.sort_values("Count", ascending=0).head()


if __name__ == '__main__':
    csv_buf = requests.get('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv').content
    baby_names = pd.read_csv(io.StringIO(csv_buf.decode('utf-8')))
    print('Read file')

    print(number_of_female_names(baby_names))
    print(top_five_names(baby_names))
