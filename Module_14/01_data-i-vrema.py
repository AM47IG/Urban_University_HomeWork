from datetime import datetime

SEASON = {(6, 7, 8): 'Summer',
          (9, 10, 11): 'Autumn',
          (12, 1, 2): 'Winter',
          (3, 4, 5): 'Spring',
          }

TIME_OF_DAY = {(6, 7, 8, 9, 10, 11): 'Morning',
               (12, 13, 14, 15, 16, 17): 'Day',
               (18, 19, 20, 21, 22, 23): 'Evening',
               (0, 1, 2, 3, 4, 5): 'Night'
               }


class SuperDate(datetime):
    def get_season(self):
        for k in SEASON:
            if self.month in k:
                return SEASON[k]

    def get_time_of_day(self):
        for k in TIME_OF_DAY:
            if self.hour in k:
                return TIME_OF_DAY[k]


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())

"""
Winter
Day
"""
