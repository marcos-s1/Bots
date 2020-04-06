from Robos import tRobot
from Robos.inputRobot import askAndReturnPrefix, askAndReturnSeachTerm
from Robos import stateRobot


def start():
    content = {'SeachTerm': askAndReturnSeachTerm(), 'prefix': askAndReturnPrefix()}
    stateRobot.save(content)
    tRobot.ActivateBootText()


start()
