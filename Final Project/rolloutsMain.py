from CasinoBJTableL import CasinoBJTable
from StaticBJLogger import StaticBJLogger
from datetime import datetime
from DateTimeCustom import DateTimeCustom

# change this number on each computer!
StaticBJLogger.init(0)

# Fill in (date, hour, minute)
# date is the calendar date
# hour is the hour in military time
endTime = DateTimeCustom(10, 23, 25)

while not endTime.greaterEqualTo():
    # print endTime.greaterEqualTo()
    table = CasinoBJTable(6, 1)
    table.initPlayers()
    table.playRound()

    del table
