import asyncio
from Robos import textRobot
from Robos.inputRobot import askAndReturnPrefix, askAndReturnSeachTerm
from Robos import stateRobot
from Robos import ImageRobot


async def start():
    content = {'SeachTerm': askAndReturnSeachTerm(), 'prefix': askAndReturnPrefix()}
    stateRobot.save(content)
    await textRobot.ActivateTextBoot()
    await ImageRobot.ActivateImageBoot()


asyncio.run(start())
