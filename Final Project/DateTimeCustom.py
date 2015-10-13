from datetime import datetime
import copy


class DateTimeCustom(object):
    # hour recorded in military time

    def __init__(self, _day, _hour, _minute):
        self.dt = datetime.now()
        self.dt = self.dt.replace(day=_day, hour=_hour, minute=_minute, second=0)

    # creates a DateTimeCustom object from the current time
    def makeObj(self):
        temp = datetime.now()
        return copy.deepcopy(DateTimeCustom(temp.day, temp.hour, temp.minute))

    # returns other >= self
    # in this case, self is the goal time
    def greaterEqualTo(self):
        # print datetime.now().second, datetime.now() >= self.dt, datetime.now()
        return datetime.now() >= self.dt

if __name__ == "__main__":
    endTime = DateTimeCustom(10, 15, 49)

    while not (endTime.greaterEqualTo()):
        print endTime.greaterEqualTo()