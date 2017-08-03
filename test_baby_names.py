import io

import pandas as pd
import requests
import requests_cache

from baby_names import number_of_female_names, top_five_names

requests_cache.install_cache(__file__)


class TestBabyStats(object):
    def setUp(self):
        csv_buf = requests.get('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv').content
        self.baby_names = pd.read_csv(io.StringIO(csv_buf.decode('utf-8')))
        print('Read file')

    def test_number_of_female_names(self):
        assert number_of_female_names(self.baby_names) == 558846

    def test_top_five_names(self):
        assert top_five_names(self.baby_names)['Name'] == pd.Series(['Jacob'])
