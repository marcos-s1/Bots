from Robos import textRobot
from Robos.inputRobot import askAndReturnPrefix, askAndReturnSeachTerm
from Robos import stateRobot
from Robos import ImageRobot


def start():
    content = {'SeachTerm': askAndReturnSeachTerm(), 'prefix': askAndReturnPrefix()}
    stateRobot.save(content)
    textRobot.ActivateTextBoot()
    ImageRobot.ActivateImageBoot()


start()
