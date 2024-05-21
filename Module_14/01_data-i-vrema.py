from datetime import datetime

SEASON = {'Summer': (6, 7, 8),
          'Autumn': (9, 10, 11),
          'Winter': (12, 1, 2),
          'Spring': (3, 4, 5),
          }

TIME_OF_DAY = {'Morning': (6, 7, 8, 9, 10, 11),
               'Day': (12, 13, 14, 15, 16, 17),
               'Evening': (18, 19, 20, 21, 22, 23),
               'Night': (0, 1, 2, 3, 4, 5)
               }


class SuperDate(datetime):
    def get_season(self):
        for k, v in SEASON.items():
            if self.month in v:
                return k

    def get_time_of_day(self):
        for k, v in TIME_OF_DAY.items():
            if self.hour in v:
                return k


a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())

"""
Winter
Day
"""