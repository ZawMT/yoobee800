from core import Keeper
from botfactory import Maker
from tracker import Screen, Record

manager = Keeper()

screen = Screen()
record = Record()

unit1 = Maker.produce("helper", "AlphaBot")
unit2 = Maker.produce("friend", "BetaBot")

manager.add_unit(unit1)
manager.add_unit(unit2)

for unit in manager.units:
    unit.action()
    screen.notice(f"{unit.id} completed an action")
    record.notice(f"{unit.id} completed an action")
