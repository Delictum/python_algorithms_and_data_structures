class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            list.append(self, x)

import datetime


year, month, day = map(int, input().split())
days = int(input())

result = datetime.date(year, month, day) + datetime.timedelta(days)
print(result.year, result.month, result.day)
