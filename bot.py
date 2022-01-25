import discord
import discord.ext.tasks
from random import randint as random_randint
# import datetime
from datetime import datetime
# import time
# import json
from json import dumps as json_dumps
from json import loads as json_loads
import io
import inspect
import re
import os
# import math




startTime = (datetime.now())

# timeOffset = (((datetime.utcnow()) - (datetime.now())).total_seconds())
timeOffset = (((datetime.utcfromtimestamp(startTime.timestamp())) - (datetime.fromtimestamp(startTime.timestamp()))).total_seconds())

activeHelpEmbeds = []

statusScheduleOverridden = False
statusSchedulePosition = -1



discordClassNamesDict = {}
discordClassAttributesDict = {}
discordClassNameAttributesDict = {}
indexJson = {}
virtualParameters = None
generatedEmbeds = {}
typeEmojis = {}
commandsEnabled = True
discordClassAttributesOverridesDict = {}
progressMessage = None
progressMessagePercentage = 0







def readSettings():

    global settingsJson
    global token
    global master
    global authorisedUsers
    global logFile
    global logChannel
    global streamingSettings
    global shortAutoclearTime
    global longAutoclearTime
    global maxSearchDepth
    # global allDataAttributes
    global attributeMaxLength
    global validCommands
    global serverSettings
    global defaultStatus
    global deleteMessages
    global typeEmojis
    global reactionsEnabled
    global discordClassOverridesDict
    global discordClassOverridesOverridesDict





    settingsFile = open(r"C:\Users\MattL\Documents\visual studio projects\test website\bot\bot.json", "r")
    settingsText = settingsFile.read()
    settingsJson = json_loads(settingsText)
    settingsFile.close()

    token = (os.environ["BOT_TOKEN"])
    master = settingsJson["master"]
    authorisedUsers = settingsJson["authorisedUsers"]
    logFile = settingsJson["logFile"]
    logChannel = settingsJson["logChannel"]

    streamingSettings = settingsJson["streamingSettings"]

    shortAutoclearTime = settingsJson["shortAutoclearTime"]
    longAutoclearTime = settingsJson["longAutoclearTime"]
    maxSearchDepth = settingsJson["maxDepth"]

    # allDataAttributes = settingsJson["allDataAttributes"]

    attributeMaxLength = settingsJson["attributeMaxLength"]

    validCommands = settingsJson["validCommands"]

    serverSettings = settingsJson["serverSettings"]

    defaultStatus = settingsJson["defaultStatus"]

    deleteMessages = settingsJson["deleteMessages"]

    typeEmojis = settingsJson["typeEmojis"]

    reactionsEnabled = settingsJson["reactionsEnabled"]

    discordClassOverridesDict = settingsJson["classOverrides"]

    discordClassOverridesOverridesDict = settingsJson["classOverridesOverrides"]


    # print(shortAutoclearTime)
    # print(maxSearchDepth)





def writeSettings():

    settingsJson["serverSettings"] = serverSettings

    settingsFile = open(r"C:\Users\MattL\Documents\visual studio projects\test website\bot\bot.json", "w")
    settingsText = json_dumps(settingsJson, indent = 4)
    settingsFile.write(settingsText)
    settingsFile.close()


















def stripRaw(message):
    return (message.strip(" `"))







def recalculateCommands():
    global validCommands

    validCommands["preReplies"] = {

        "trollHelpEmbed": {"message": "no help for you!", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "eggEmoji": {"message": "\U0001F95A", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "handEmoji": {"message": ":wave_tone1:", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "why": {"message": "no...", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},
        "snowflakeEmoji": {"message": ":snowflake:", "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},

        "ls": {"message": "```pi@raspberrypi: ~ $ ls\nREADME.txt```", "embed": None, "deleteTime": 4, "permissions": 0},
        "cat": {"message": "```pi@raspberrypi: ~ $ cat README.txt\nwell done...```", "embed": None, "deleteTime": 4, "permissions": 0},
        "nano": {"message": "```GNU nano 3.2                       README.txt                                 \n\nwell done...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                [ Read 1 line ]                               \n^G Get Help  ^O Write Out ^W Where Is  ^K Cut Text  ^J Justify   ^C Cur Pos   \n^X Exit      ^R Read File ^\ Replace   ^U Uncut Text^T To Spell  ^_ Go To Line\n```", "embed": None, "deleteTime": 4, "permissions": 0},

        "helpEmbed": {"function": "createHelpEmbed()", "message": None, "embed": None, "deleteTime": longAutoclearTime, "permissions": 0},
        "randomNumber": {"function": "generateRandom()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 0},

        "upTime": {"function": "getUptime()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        # "attendanceEmbed": {"message": (format(((datetime.now()) - startTime), "code")), "embed": ((grablink(9))), "deleteTime": shortAutoclearTime, "permissions": 1},
        "attendanceEmbed": {"message": None, "embed": "timetables", "deleteTime": shortAutoclearTime, "permissions": 0},

        "getTimetables": {"message": None, "embed": "forms", "deleteTime": shortAutoclearTime, "permissions": 0},

        "prettyPrint": {"function": "prettyPrint()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "getHistory": {"function": "getHistory()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "ifEmptyCodeBlock": {"function": "generateBlock(\"Empty\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifZeroCodeBlock": {"function": "generateBlock(\"Zero\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifLongCodeBlock": {"function": "generateBlock(\"Long\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "ifGreaterCodeBlock": {"function": "generateBlock(\"Greater\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifLessCodeBlock": {"function": "generateBlock(\"Less\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifGreaterLessCodeBlock": {"function": "generateBlock(\"GreaterLess\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "ifTrueCodeBlock": {"function": "generateBlock(\"Truthy\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "forIteratorCodeBlock": {"function": "generateBlock(\"FIterator\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "whileIteratorCodeBlock": {"function": "generateBlock(\"WIterator\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},
        "dictionaryIteratorCodeBlock": {"function": "generateBlock(\"DIterator\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "fileCodeBlock": {"function": "generateBlock(\"Filey\")", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "autoClear": {"function": "removeMessages()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "generateTimetable": {"function": "getPeriod()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "removeSmirk": {"function": "removeSmirk()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "deleteCallingMessage": {"function": "deleteCallingMessage()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "writeSettings": {"function": "saveSettings()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "listAttributes": {"function": "listAttributes()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "setStatus": {"function": "setStatus()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "rebuildIndex": {"function": "rebuildIndex()", "message": None, "embed": None, "deleteTime": 4, "permissions": 1},

        "checkForCommander": {"function": "checkForCommander()", "message": None, "embed": None, "deleteTime": 8, "permissions": 0},

        "testPing": {"function": "testPing()", "message": None, "embed": None, "deleteTime": 8, "permissions": 0},

        "acknowledgementsHelpEmbed": {"message": None, "embed": "acknowledgementsHelpEmbed", "deleteTime": shortAutoclearTime, "permissions": 1},

        "owoify": {"function": "owoify()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 1},

        "startListening": {"function": "listening(True)", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 3},

        "stopListening": {"function": "listening(False)", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 3},

        "terminate": {"function": "terminate()", "message": None, "embed": None, "deleteTime": shortAutoclearTime, "permissions": 3},

        "copyUserText": {"function": "copyUserText()", "message": None, "embed": None, "deleteTime": None, "permissions": 3},

        "revokeAllInvites": {"function": "revokeAllInvites()", "message": None, "embed": None, "deleteTime": None, "permissions": 1},

        "addListeners": {"function": "addListeners()", "message": None, "embed": None, "deleteTime": None, "permissions": 3},

        "joinVoice": {"function": "joinVoice()", "message": None, "embed": None, "deleteTime": None, "permissions": 3},




    }







def format(message, format, language = ""):

    message = (str(message))

    if ("code" in format):
        message = ("`" + (str(message)) + "`")
    if ("cBlock" in format):
        message = ("```" + language + "\n" + (str(message)) + "\n" + "```")
    if ("italic" in format):
        message = ("*" + (str(message)) + "*")
    if ("bold" in format):
        message = ("**" + (str(message)) + "**")
    if ("underline" in format):
        message = ("__" + (str(message)) + "__")
    if ("strikethrough" in format):
        message = ("~~" + (str(message)) + "~~")
    if ("quote" in format):
        message = ("> " + (str(message)))
        message = message.replace("\n", "\n> ")

    return message











def grablink(year):

    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds

    today = datetime.today()
    if int(today.strftime("%W")) % 2 == 0:
        week = "Week+A"
    else:
        week = "Week+B"


    if ((seconds > 31800) and (seconds <= 32280)):
        period = "RC"
    elif ((seconds > 32400) and (seconds <= 34800)):
        period = "1"
    elif ((seconds > 35100) and (seconds <= 37500)):
        period = "2"
    elif ((seconds > 38700) and (seconds <= 41100)):
        period = "3"
    elif ((seconds > 41400) and (seconds <= 43800)):
        period = "4"
    elif ((seconds > 46200) and (seconds <= 47400)):
        period = "5"
    elif ((seconds > 48900) and (seconds <= 51300)):
        period = "6"
    else:
        period = "NULL"

    if year == 8:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSdBn_QwHom86htHoZYGuG6YjXTvjL_-IJoCdoiYMVVbZMwU9g" + "/" + "viewform" + "?" + "usp=pp_url" + "&"

    elif year == 9:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSc1aXXrENpHmaJ30zlmR4xWnNv6mRw4jKJSiZeUErAG9e6bdw" + "/" + "viewform" + "?" + "usp=pp_url" + "&"

    elif year == 10:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSew3K82Uj9SRrtd0C1wHyC4Rn9neUmOCy1AzcCz7tRYJzFHGw" + "/" + "viewform" + "?" + "usp=pp_url" + "&"

    elif year == 12:
        rtnval = "https://docs.google.com/forms/d/e/" + "1FAIpQLSdqg7NnSAYiZjIafsTDwsaemF1ZRmBNi4yP5uYxEw5f0O0d6A" + "/" + "viewform" + "?" + "usp=pp_url" + "&"




    rtnval += "entry.1193583720" + "=" + today.strftime("%Y-%m-%d") + "&"
    rtnval += "entry.1166771392" + "=" + week + "&"
    rtnval += "entry.449469481" + "=" + today.strftime("%A") + "&"
    rtnval += "entry.1844771487" + "=" + today.strftime("%A") + "&"


    if week == "Week+A":
        if today.strftime("%A") == "Monday":
            rtnval += "entry.669622984" + "=" + period
        elif today.strftime("%A") == "Tuesday":
            rtnval += "entry.1898890906" + "=" + period
        elif today.strftime("%A") == "Wednesday":
            rtnval += "entry.371344035" + "=" + period
        elif today.strftime("%A") == "Thursday":
            rtnval += "entry.1449705738" + "=" + period
        elif today.strftime("%A") == "Friday":
            rtnval += "entry.524423421" + "=" + period

    elif week == "Week+B":
        if today.strftime("%A") == "Monday":
            rtnval += "entry.1662723045" + "=" + period
        elif today.strftime("%A") == "Tuesday":
            rtnval += "entry.614317995" + "=" + period
        elif today.strftime("%A") == "Wednesday":
            rtnval += "entry.855393316" + "=" + period
        elif today.strftime("%A") == "Thursday":
            rtnval += "entry.105918712" + "=" + period
        elif today.strftime("%A") == "Friday":
            rtnval += "entry.115181569" + "=" + period



    return [

        {
            "title": "Click to open",
            "url": rtnval,
            "description": "Year 9/10 only",
            "color": 0x8000C0,
        },
        {
            "name": "Attendance Form",
            "url": "",
            "icon_url": "",
        },
        {
            "text": "this is not fully automatic",
        },
        [
        ]

    ]





def generateDiscordClasses():

    global discordClassNamesDict
    global discordClassAttributesDict
    global discordClassAttributesOverridesDict
    global discordClassNameAttributesDict
    global discordClassAttributesOverridesOverridesDict

    discordModuleMembers = (inspect.getmembers(discord))
    discordModuleMembersLength = len(discordModuleMembers)
    discordClassNamesDict = {}


    repeats = 0
    while (repeats < discordModuleMembersLength):

        if ((discordModuleMembers[repeats][0])[0] == "_"):
            pass
        elif ((discordModuleMembers[repeats][0])[0] != "_"):

            if ((inspect.isclass(discordModuleMembers[repeats][1])) == True):
                discordClassNamesDict[(discordModuleMembers[repeats][1])] = (discordModuleMembers[repeats][0])
            elif ((inspect.isclass(discordModuleMembers[repeats][1])) == False):
                pass

        repeats = repeats + 1



    indexFile = open(r"C:\Users\MattL\Documents\visual studio projects\test website\bot\index.json", "r")
    indexText = indexFile.read()
    indexJson = json_loads(indexText)
    indexFile.close()


    discordClassNameAttributesDict = indexJson["discordClassNameAttributesDict"]
    discordClassNameAttributesLength = len(discordClassNameAttributesDict)
    discordClasses = list(discordClassNamesDict.keys())

    discordClassAttributesDict = {}

    repeats = 0
    while (repeats < discordClassNameAttributesLength):

        discordClassAttributesDict[(discordClasses[repeats])] = discordClassNameAttributesDict[(discordClassNamesDict[(discordClasses[repeats])])]

        repeats = repeats + 1




    discordClassAttributesOverridesDict = discordClassAttributesDict.copy()
    repeats = 0
    while (repeats < discordClassNameAttributesLength):

        try:
            discordClassAttributesOverridesDict[(discordClasses[repeats])] = discordClassOverridesDict[(discordClassNamesDict[(discordClasses[repeats])])]

        except Exception as exception:
            pass


        repeats = repeats + 1





    discordClassAttributesOverridesOverridesDict = discordClassAttributesDict.copy()
    repeats = 0
    while (repeats < discordClassNameAttributesLength):

        try:
            discordClassAttributesOverridesOverridesDict[(discordClasses[repeats])] = discordClassOverridesOverridesDict[(discordClassNamesDict[(discordClasses[repeats])])]

        except Exception as exception:
            pass


        repeats = repeats + 1














def regenerateClassAttributes():

    global indexJson
    global discordClassNameAttributesDict


    discordClasses = list(discordClassNamesDict.keys())


    discordClassesLength = len(discordClasses)
    discordClassNameAttributesDict = {}


    repeats = 0
    while (repeats < discordClassesLength):

        discordClassNameAttributes = (inspect.getmembers(discordClasses[repeats]))
        discordClassNameAttributesLength = (len(discordClassNameAttributes))

        discordClassNameAttributesDict[(discordClassNamesDict[(discordClasses[repeats])])] = []


        repeats1 = 0
        while (repeats1 < discordClassNameAttributesLength):

            if (((discordClassNameAttributes[repeats1][0][0]) != "_") == True):

                if ((inspect.isfunction(discordClassNameAttributes[repeats1][1])) == True):
                    pass

                elif ((inspect.isfunction(discordClassNameAttributes[repeats1][1])) == False):

                    if ((inspect.ismethod(discordClassNameAttributes[repeats1][1])) == True):
                        pass

                    elif ((inspect.ismethod(discordClassNameAttributes[repeats1][1])) == False):
                        (discordClassNameAttributesDict[(discordClassNamesDict[(discordClasses[repeats])])]).append(discordClassNameAttributes[repeats1][0])

            elif (((discordClassNameAttributes[repeats1][0][0]) != "_") == False):
                pass


            repeats1 = repeats1 + 1


        repeats = repeats + 1



    indexJson["discordClassNameAttributesDict"] = discordClassNameAttributesDict


    indexFile = open(r"C:\Users\MattL\Documents\visual studio projects\test website\bot\index.json", "w")
    indexText = json_dumps(indexJson, indent = 4)
    indexFile.write(indexText)
    indexFile.close()






def generateEmbeds():


    global generatedEmbeds

    metaInfoFile = open(r"C:\Users\MattL\Documents\visual studio projects\test website\bot\metainfo.json", "r")
    metaInfoText = metaInfoFile.read()
    metaInfoJson = json_loads(metaInfoText)
    metaInfoFile.close()


    prebuiltEmbedNames = list(metaInfoJson.keys())
    prebuiltEmbedNamesLength = (len(prebuiltEmbedNames))

    repeats = 0
    while (repeats < prebuiltEmbedNamesLength):

        title = (metaInfoJson[(prebuiltEmbedNames[repeats])][0])
        header = (metaInfoJson[(prebuiltEmbedNames[repeats])][1])
        footer = (metaInfoJson[(prebuiltEmbedNames[repeats])][2])
        fields = (metaInfoJson[(prebuiltEmbedNames[repeats])][3])
        fieldsLength = (len(fields))

        newEmbed = discord.Embed(**title)

        newEmbed.set_author(**header)
        newEmbed.set_footer(**footer)

        typeEmojisKeys = list(typeEmojis.keys())
        typeEmojisKeysLength = (len(typeEmojisKeys))

        repeats1 = 0
        while (repeats1 < fieldsLength):

            repeats2 = 0
            while (repeats2 < typeEmojisKeysLength):
                (fields[repeats1]["name"]) = (fields[repeats1]["name"]).replace(("$" + (typeEmojisKeys[repeats2]) + "$"), ("<" + ":" + (typeEmojisKeys[repeats2]) + ":" + (typeEmojis[(typeEmojisKeys[repeats2])]) + ">"))
                repeats2 = repeats2 + 1

            newEmbed.add_field(**(fields[repeats1]))
            repeats1 = repeats1 + 1


        generatedEmbeds[(prebuiltEmbedNames[repeats])] = newEmbed

        repeats = repeats + 1










































class MyClient(discord.Client):



    async def printOutputToLogs(self, output, message = None):

        print((repr(output)) + "\n")


        if (message == None):
            await botLogger.send(format(("Administration" + "\n\n" + output), "cBlock"))
        elif (message != None):


            if "embed" in output:
                output["embed"] = (repr(output["embed"]))

            if "reference" in output:
                output["reference"] = (repr(output["reference"]))

            if "file" in output:
                output["file"] = (repr(output["file"]))




            result = ("Replied with" + "\n\n" + (str(json_dumps(output, indent = 4))) + "\n\n\n\n" + "to" + "\n\n" + (str(message.content)) + "\n\n\n\n" + "from" + "\n\n" + (self.generateDisplayName()))
            result = (format(result, "cBlock"))


            if (len(result) < 256):
                result = result
                await botLogger.send(result)
            elif (len(result) >= 256):
                tempFile = io.BytesIO(result.encode())
                discordFile = (discord.File(tempFile, "message.txt"))
                await botLogger.send(file = discordFile)




    async def checkForCommander(self):

        if ((callingMessage.author.id) in authorisedUsers):
            return [("commanderYes", {}), "embed"]
        elif ((callingMessage.author.id) not in authorisedUsers):
            return [("commanderNo", {}), "embed"]




    async def testPing(self):
        utcTime = datetime.utcnow()
        sentTime = callingMessage.created_at
        return [("roundTripTime", {"title": "Round trip time", "description": ((format("Total:", "bolden")) + " " + (format(((str(round((((utcTime - sentTime).total_seconds()) * 1000), 3))) + " " + "ms"), "code")) + "\n" + (format("WebSocket:", "bolden")) + " " + (format(((str(round(((client.latency) * 1000), 3))) + " " + "ms"), "code")))}), "embed"]


    async def listening(self, enabled):

        global commandsEnabled
        commandsEnabled = enabled

        if (commandsEnabled == True):
            await client.change_presence(status = (discord.Status.idle), activity = (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime))))
            return [("taskCompleted", {"description": "Now listening!"}), "embed"]

        elif (commandsEnabled == False):
            await client.change_presence(status = (discord.Status.dnd), activity = (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime))))
            return [("taskCompleted", {"description": "Now sleeping!"}), "embed"]








    def generateDisplayName(self):
        return ((str(callingMessage.author.display_name)) + "#" + (str(callingMessage.author.discriminator)) + " " + "(" + (str(callingMessage.author.id)) + ")")


    async def rebuildIndex(self):

        # regenerateClassAttributes()

        # return [("taskCompleted", {"description": "index rebuilt"}), "embed"]
        return [(format("too slow for use", "code")), "message"]



    async def saveSettings(self):

        # writeSettings()

        # return [("taskCompleted", {"description": "settings saved"}), "embed"]
        return [(format("too slow for use", "code")), "message"]




    async def sendMessage(self, sendOptions, reactions = {}):

        if ((("reference" in sendOptions) == True) or (("mention_author" in sendOptions) == True)):
            sendOptions["reference"] = sendOptions["reference"]
            sendOptions["mention_author"] = sendOptions["mention_author"]
        elif ((("reference" in sendOptions) == False) and (("mention_author" in sendOptions) == False)):
            sendOptions["reference"] = (callingMessage.to_reference())
            sendOptions["mention_author"] = False



        if ((sendOptions["delete_after"]) == None):
            pass
        elif ((sendOptions["delete_after"]) != None):

            if ((str(callingMessage.guild.id)) in serverSettings):

                if ((serverSettings[(str(callingMessage.guild.id))]["deleteCalls"]) == True):
                    await callingMessage.delete(delay = 4)
                elif ((serverSettings[(str(callingMessage.guild.id))]["deleteCalls"]) == False):
                    pass

            elif ((str(callingMessage.guild.id)) not in serverSettings):
                pass


        sentMessage = await callingMessage.channel.send(**sendOptions)



        if (reactions == None):
            pass
        elif (reactions != None):
            repeats = 0
            while (repeats < (len(reactions))):
                await sentMessage.add_reaction(reactions[repeats])
                repeats = repeats + 1



        await self.printOutputToLogs(sendOptions, callingMessage)




    async def listAttributes(self):

        return [(format((json_dumps(discordClassNameAttributesDict, indent = 4)), "cBlock", "json")), "message"]



    async def setStatus(self):

        global statusScheduleOverridden
        global statusSchedulePosition



        if (virtualParameters == None):
            statusScheduleOverridden = True

        elif (virtualParameters != None):
            statusScheduleOverridden = False




        parameters = await self.getParameters()


        statuses = {

            "streaming": {
                "status": (discord.Status.idle),
                "activity": (discord.Streaming(**streamingSettings)),
            },

            "competing": {
                "status": (discord.Status.online),
                "activity": (discord.Activity(type = (discord.ActivityType.competing), name = (streamingSettings["name"]), start = (startTime)))
            },

            "online": {
                "status": (discord.Status.online),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },
            "idle": {
                "status": (discord.Status.idle),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },
            "dnd": {
                "status": (discord.Status.dnd),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },
            "invisible": {
                "status": (discord.Status.invisible),
                "activity": (discord.Activity(type = (discord.ActivityType.listening), name = (streamingSettings["name"]), start = (startTime)))
            },

        }


        if (parameters == "schedule"):

            statusSchedulePosition = statusSchedulePosition



            if (statusScheduleOverridden == True):
                statusScheduleOverridden = False

            elif (statusScheduleOverridden == False):
                pass

            await self.changeStatus()


            return [("taskCompleted", {"description": ("Status set to" + " " + parameters + "!")}), "embed"]

        elif (parameters != "schedule"):


            statusSchedulePosition = -1


            if ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible))(, ?\".{0,24}\")?$", (parameters.lower())))) == True):


                if ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible)), ?\".{0,24}\"$", (parameters.lower())))) == True):
                    status = (((parameters.lower()).split(",", 1))[0])
                    activity = ((((parameters.lower()).split(",", 1))[1])[(((re.search("\".{0,24}\"", (((parameters.lower()).split(",", 1))[1]))).start()) + 1):(((re.search("\".{0,24}\"", (((parameters.lower()).split(",", 1))[1]))).end()) - 1)])

                    presence = (statuses[status])
                    
                    (presence["activity"]) = (discord.Activity(type = (discord.ActivityType.competing), name = (activity), start = (startTime)))

                    await client.change_presence(**(presence))



                    if (statusScheduleOverridden == True):
                        await self.printOutputToLogs("Changed status to" + " " + "'" + ((statuses[status]["status"]).name) + "'")
                        await self.printOutputToLogs("Changed activity to" + " " + "'" + activity + "'")

                    elif (statusScheduleOverridden == False):
                        pass




                elif ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible)), ?\".{0,24}\"$", (parameters.lower())))) == False):

                    await client.change_presence(**(statuses[(parameters.lower())]))


                    if (statusScheduleOverridden == True):
                        await self.printOutputToLogs("Changed status to" + " " + "'" + ((statuses[(parameters.lower())]["status"]).name) + "'")
                        await self.printOutputToLogs("Changed activity to" + " " + "'" + ((statuses[(parameters.lower())]["activity"]).name) + "'")

                    elif (statusScheduleOverridden == False):
                        pass




                return [("taskCompleted", {"description": ("Status set to" + " " + parameters + "!")}), "embed"]


            elif ((bool(re.match("^((streaming)|(competing)|(online)|(idle)|(dnd)|(invisible))(, ?\".{0,24}\")?$", (parameters.lower())))) == False):
                # return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <parameters>", "code")))}), "embed"]
                return [("invalidParameters", {"description": ("status provided is invalid" + "\n" + "command should be in the format" + " " + (format("\\command <streaming|competing|online|idle|dnd|invisible>", "code")))}), "embed"]










    async def owoify(self):

        parameters = await self.getParameters()

        modifications = list(re.finditer(r"(([^lrw])(l{1,}|r{1,})([BCDFGHJKMNOPQSTVXYZ|bcdfghjkmnopqstvxyz]))|(([BCDFGHJKMNOPQSTVXYZ|bcdfghjkmnopqstvxyz])(l{1,}|r{1,})([^elrw\W]))", parameters))
        modificationsLength = (len(modifications))



        modificationIndex = []
        repeats = 0

        while (repeats < modificationsLength):
            modificationIndex = modificationIndex + (list(range(((((modifications[repeats]).span())[0]) + 1), ((((modifications[repeats]).span())[1]) - 1))))
            repeats = repeats + 1

        modifiedString = list(parameters)
        repeats = 0

        while (repeats < (len(modificationIndex))):
            (modifiedString[(modificationIndex[repeats])]) = "w"
            repeats = repeats + 1


        convertedString = ""
        repeats = 0
        while (repeats < (len(modifiedString))):
            convertedString = convertedString + (modifiedString[repeats])
            repeats = repeats + 1

        return [(format(convertedString, "cBlock")), "message"]



















    async def terminate(self):

        print(client.is_ws_ratelimited())

        await client.close()

        return [("taskCompleted", {}), "embed"]







    async def copyUserText(self):

        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\say <text>", "code")))}), "embed"]

        elif (parameters != ""):
            await callingMessage.delete(delay = 1)
            return [parameters, "message", None, [None, False]]





    async def addListeners(self):


        global pingListeningGuilds
        global pingListeningGuildsLogs
        global verificationListeningChannels
        global verificationListeningChannelsLogs
        global verificationListeningChannelsRequiredRoles
        global verificationListeningChannelsRoles
        global roleListeningChannels
        global roleListeningChannelsLogs
        global roleListeningChannelsPosition
        global roleListeningChannelsRoles
        global statusSchedule

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        print(fetchedOptions)
        # print(fetchedOptions["pings"])




        pingListeningGuilds = []
        pingListeningGuildsLogs = {}
        verificationListeningChannels = []
        verificationListeningChannelsLogs = {}
        verificationListeningChannelsRequiredRoles = {}
        verificationListeningChannelsRoles = {}
        roleListeningChannels = []
        roleListeningChannelsLogs = {}
        roleListeningChannelsPosition = {}
        roleListeningChannelsRoles = {}

        statusSchedule = (fetchedOptions["schedule"])



        repeats = 0
        while (repeats < (len(fetchedOptions["pings"]))):
            pingListeningGuilds.append(fetchedOptions["pings"][repeats][0])
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["pings"]))):
            pingListeningGuildsLogs[(fetchedOptions["pings"][repeats][0])] = fetchedOptions["pings"][repeats][1]
            repeats = repeats + 1




        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannels.append(fetchedOptions["verification"][repeats][0])
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannelsLogs[(fetchedOptions["verification"][repeats][0])] = fetchedOptions["verification"][repeats][1]
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannelsRequiredRoles[(fetchedOptions["verification"][repeats][0])] = fetchedOptions["verification"][repeats][2]
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["verification"]))):
            verificationListeningChannelsRoles[(fetchedOptions["verification"][repeats][0])] = fetchedOptions["verification"][repeats][3]
            repeats = repeats + 1






        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannels.append(fetchedOptions["customRoles"][repeats][0])
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannelsLogs[(fetchedOptions["customRoles"][repeats][0])] = fetchedOptions["customRoles"][repeats][1]
            repeats = repeats + 1


        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannelsPosition[(fetchedOptions["customRoles"][repeats][0])] = fetchedOptions["customRoles"][repeats][2]
            repeats = repeats + 1

        repeats = 0
        while (repeats < (len(fetchedOptions["customRoles"]))):
            roleListeningChannelsRoles[(fetchedOptions["customRoles"][repeats][0])] = fetchedOptions["customRoles"][repeats][3]
            repeats = repeats + 1





        print("\n\n\n")

        print(pingListeningGuilds, pingListeningGuildsLogs, verificationListeningChannels, verificationListeningChannelsLogs, verificationListeningChannelsRequiredRoles, verificationListeningChannelsRoles, roleListeningChannels, roleListeningChannelsLogs, roleListeningChannelsPosition, roleListeningChannelsRoles)
        print(verificationListeningChannels, verificationListeningChannelsLogs)
        print(verificationListeningChannelsRequiredRoles)
        print(verificationListeningChannelsRoles)

        print("\n\n\n")

        """

        if ((len(message.mentions)) > 0):

            if ((message.guild.id) in pingListeningGuilds):

                callingMessage = message
                messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])
                await messageGuildLogChannel.send((((message.author).mention) + " " + "mentioned" + " " + (((message.mentions)[0]).mention) + "\n" + (format((json_dumps((self.reformatMessage(callingMessage, 1)), indent = 4)), "cBlock"))), allowed_mentions = (discord.AllowedMentions(users = False)))


        if ((len(message.role_mentions)) > 0):


            if ((message.guild.id) in pingListeningGuilds):

                callingMessage = message
                messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])
                await messageGuildLogChannel.send((((message.author).mention) + " " + "mentioned" + " " + (((message.role_mentions.mentions)[0]).mention) + "\n" + (format((json_dumps((self.reformatMessage(callingMessage, 1)), indent = 4)), "cBlock"))), allowed_mentions = (discord.AllowedMentions(users = False)))



        """



        return [("taskCompleted", {"description": "Listeners updated!"}), "embed"]



    async def addRoleListener(self, channel, newRole):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        (fetchedOptions["customRoles"][(roleListeningChannels.index(channel))][3]).append(newRole)
        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()




    async def addVerificationListener(self, verificationData):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        (fetchedOptions["verification"]).append(verificationData)
        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()



    async def removeVerificationListener(self, verificationDataPosition):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))

        (fetchedOptions["verification"]).pop(verificationDataPosition)

        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()





    async def addMentionListener(self, mentionData):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))
        (fetchedOptions["pings"]).append(mentionData)
        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()




    async def removeMentionListener(self, mentionDataPosition):

        optionsChannel = client.get_channel(910324268800307262)
        fetchedOptions = (json_loads(((await ((optionsChannel.history(limit = 1)).flatten()))[0]).content))

        (fetchedOptions["pings"]).pop(mentionDataPosition)

        await optionsChannel.send(json_dumps(fetchedOptions, separators = (", ", ": \n")))
        await self.addListeners()





    async def createHelpEmbed(self):

        return [("helpMenu", {}), "embed"]


    async def joinVoice(self):


        return ["connected", "message"]


        voiceChannelToJoin = ((callingMessage.channel_mentions)[0])

        if ((voiceChannelToJoin.type) == (discord.ChannelType.voice)):

            global connectedVoiceChannels
            connectedVoiceChannels.append(await voiceChannelToJoin.connect())



        return ["connected", "message"]





    async def revokeAllInvites(self):

        guildInvites = await ((callingMessage.guild).invites())
        guildInvitesLength = (len(guildInvites))

        guildInvitesData = []

        repeats = 0
        while (repeats < guildInvitesLength):
            guildInvitesData.append(repr(self.reformatData(guildInvites[repeats])))
            await (guildInvites[repeats]).delete()
            repeats = repeats + 1


        # return [("taskCompleted", {}), "embed"]
        return [(format((json_dumps(guildInvitesData, indent = 4)), "cBlock", "json")), "message"]


















    async def deleteCallingMessage(self):

        parameters = await self.getParameters()

        print(str(callingMessage.guild.id))
        print(serverSettings)

        if ((str(callingMessage.guild.id)) in serverSettings):
            pass
        elif ((str(callingMessage.guild.id)) not in serverSettings):
            serverSettings[(str(callingMessage.guild.id))] = {}




        try:
            parameters = (self.evaluateBoolean(parameters))

        except Exception as exception:
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\dc|deletecall <enabled>", "code")))}), "embed"]


        if (parameters == True):

            serverSettings[(str(callingMessage.guild.id))]["deleteCalls"] = True
            return [("taskCompleted", {"description": "Delete calling messages set to true"}), "embed"]
            # return [(format("delete calling messages set to true", "code")), "message"]

        elif (parameters == False):

            serverSettings[(str(callingMessage.guild.id))]["deleteCalls"] = False
            return [("taskCompleted", {"description": "Delete calling messages set to false"}), "embed"]
            # return [(format("delete calling messages set to false", "code")), "message"]




    async def removeSmirk(self):

        parameters = await self.getParameters()


        smirkEmoji = "\U0001F60F"


        try:
            smirkUser = ((parameters.split(" ", 1))[0])
            limit = ((parameters.split(" ", 1))[1])

        except Exception as exception:
            return [("unspecifiedParameters", {"description": ("parameter missing" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]

        await self.createProgress(0)

        try:
            limit = (int(limit))

            if ((limit >= 0) and (limit <= 128)):
                pass
            elif (limit < 0):
                await self.createProgress(100)
                return [("invalidParameters", {"description": ("search limit is too low" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]
            elif (limit > 128):
                await self.createProgress(100)
                return [("invalidParameters", {"description": ("search limit is too high" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]


        except Exception as exception:
            await self.createProgress(100)
            return [("invalidParameters", {"description": ("search limit is not an integer" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]

        try:
            smirkUser = await client.fetch_user(smirkUser)

        except Exception as exception:
            await self.createProgress(100)
            return [("invalidParameters", {"description": ("user id provided is invalid" + "\n" + "command should be in the format" + " " + (format("\\rs|removesmirk <user> <searchlimit>", "code")))}), "embed"]


        await self.createProgress(20)

        his = await ((callingMessage.channel.history(limit = limit)).flatten())

        repeats = 0
        while (repeats < (len(his))):

            reactionsLength = (len((his[repeats]).reactions))

            repeats1 = 0
            while (repeats1 < reactionsLength):

                # print(((his[repeats]).reactions)[repeats1])

                if (((((his[repeats]).reactions)[repeats1]).emoji) == smirkEmoji):
                    await (his[repeats]).remove_reaction(smirkEmoji, smirkUser)
                elif (((((his[repeats]).reactions)[repeats1]).emoji) != smirkEmoji):
                    pass

                repeats1 = repeats1 + 1



            if ((repeats % (round((len(his)) / 3))) == 0):

                if (repeats == 0):
                    pass
                elif (repeats != 0):
                    await self.createProgress(((repeats / (round((len(his)) / 3))) * 20) + 20)

            elif ((repeats % (round((len(his)) / 3))) != 0):
                pass



            repeats = repeats + 1


        await self.createProgress(100)

        return [("taskCompleted", {"description": "Smirks removed!"}), "embed"]













    async def changeStatus(self):


        global statusSchedulePosition
        global virtualParameters

        print("Changing status")


        timeOffset = 39600
        secondsElapsed = ((((datetime.now()).timestamp()) + timeOffset) % 86400)


        
        if (statusScheduleOverridden == True):
            pass

        elif (statusScheduleOverridden == False):

            statusScheduleLength = (len(statusSchedule))

            repeats = 0
            while (repeats < statusScheduleLength):

                if ((secondsElapsed >= (((statusSchedule[repeats])[0])[0])) and (secondsElapsed < (((statusSchedule[repeats])[0])[1]))):
                    
                    if (repeats == statusSchedulePosition):
                        pass

                    elif (repeats != statusSchedulePosition):

                        statusSchedulePosition = repeats
                        virtualParameters = ((statusSchedule[statusSchedulePosition])[1])
                        await self.setStatus()
                        break

                elif ((secondsElapsed < (((statusSchedule[repeats])[0])[0])) or (secondsElapsed >= (((statusSchedule[repeats])[0])[1]))):
                    repeats = repeats + 1
                    


















    async def getPeriod(self):

        now = datetime.now()
        midnight = now.replace(hour = 0, minute = 0, second = 0, microsecond=0)
        seconds = (now - midnight).seconds

        if int(now.strftime("%W")) % 2 == 0:
            week = "Week A"
        else:
            week = "Week B"


        day = (now.strftime("%A"))


        if (day == "Monday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 33600)):
                period = "Roll Call"
                startTime = 31800
                endTime = 33600

            elif ((seconds > 33600) and (seconds <= 36600)):
                period = "Period 1"
                startTime = 33600
                endTime = 36600

            elif ((seconds > 36600) and (seconds <= 39600)):
                period = "Period 2"
                startTime = 36600
                endTime = 39600

            elif ((seconds > 39600) and (seconds <= 40800)):
                period = "Recess"
                startTime = 39600
                endTime = 40800

            elif ((seconds > 40800) and (seconds <= 43740)):
                period = "Period 3"
                startTime = 40800
                endTime = 43740

            elif ((seconds > 43740) and (seconds <= 46680)):
                period = "Period 4"
                startTime = 43740
                endTime = 46680

            elif ((seconds > 46680) and (seconds <= 49020)):
                period = "Lunch"
                startTime = 46680
                endTime = 49020

            elif ((seconds > 49020) and (seconds <= 51960)):
                period = "Period 5"
                startTime = 49020
                endTime = 51960

            elif ((seconds > 51960) and (seconds <= 54900)):
                period = "Period 6"
                startTime = 51960
                endTime = 54900

            elif ((seconds > 54900) and (seconds <= 86400)):
                period = "After School"
                startTime = 54900
                endTime = 86400








        elif (day == "Tuesday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35100)):
                period = "Period 1"
                startTime = 32280
                endTime = 35100

            elif ((seconds > 35100) and (seconds <= 37920)):
                period = "Period 2"
                startTime = 35100
                endTime = 37920

            elif ((seconds > 37920) and (seconds <= 39000)):
                period = "Recess"
                startTime = 37920
                endTime = 39000

            elif ((seconds > 39000) and (seconds <= 41820)):
                period = "Period 3"
                startTime = 39000
                endTime = 41820

            elif ((seconds > 41820) and (seconds <= 44640)):
                period = "Period 4"
                startTime = 41820
                endTime = 44640

            elif ((seconds > 44640) and (seconds <= 45720)):
                period = "Lunch"
                startTime = 44640
                endTime = 45720

            elif ((seconds > 45720) and (seconds <= 48540)):
                period = "Period 5"
                startTime = 45720
                endTime = 48540

            elif ((seconds > 48540) and (seconds <= 51360)):
                period = "Period 6"
                startTime = 48540
                endTime = 51360

            elif ((seconds > 51360) and (seconds <= 86400)):
                period = "After School"
                startTime = 51360
                endTime = 86400








        elif (day == "Wednesday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35640)):
                period = "Period 1"
                startTime = 32280
                endTime = 35640

            elif ((seconds > 35640) and (seconds <= 39000)):
                period = "Period 2"
                startTime = 35640
                endTime = 39000

            elif ((seconds > 39000) and (seconds <= 40200)):
                period = "Recess"
                startTime = 39000
                endTime = 40200

            elif ((seconds > 40200) and (seconds <= 43560)):
                period = "Period 3"
                startTime = 40200
                endTime = 43560

            elif ((seconds > 43560) and (seconds <= 46800)):
                period = "Period 4"
                startTime = 43560
                endTime = 46800

            elif ((seconds > 46800) and (seconds <= 52200)):
                period = "Lunch"
                startTime = 46800
                endTime = 52200

            elif ((seconds > 52200) and (seconds <= 52200)):
                period = "Period 5"
                startTime = 52200
                endTime = 52200

            elif ((seconds > 52200) and (seconds <= 52200)):
                period = "Period 6"
                startTime = 52200
                endTime = 52200

            elif ((seconds > 52200) and (seconds <= 86400)):
                period = "After School"
                startTime = 52200
                endTime = 86400








        elif (day == "Thursday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35280)):
                period = "Period 1"
                startTime = 32280
                endTime = 35280

            elif ((seconds > 35280) and (seconds <= 38280)):
                period = "Period 2"
                startTime = 35280
                endTime = 38280

            elif ((seconds > 38280) and (seconds <= 39480)):
                period = "Recess"
                startTime = 38280
                endTime = 39480

            elif ((seconds > 39480) and (seconds <= 42480)):
                period = "Period 3"
                startTime = 39480
                endTime = 42480

            elif ((seconds > 42480) and (seconds <= 45480)):
                period = "Period 4"
                startTime = 42480
                endTime = 45480

            elif ((seconds > 45480) and (seconds <= 48900)):
                period = "Lunch"
                startTime = 45480
                endTime = 48900

            elif ((seconds > 48900) and (seconds <= 51900)):
                period = "Period 5"
                startTime = 48900
                endTime = 51900

            elif ((seconds > 51900) and (seconds <= 54900)):
                period = "Period 6"
                startTime = 51900
                endTime = 54900

            elif ((seconds > 54900) and (seconds <= 86400)):
                period = "After School"
                startTime = 54900
                endTime = 86400








        elif (day == "Friday"):

            if ((seconds > 0) and (seconds <= 31800)):
                period = "Before School"
                startTime = 0
                endTime = 31800

            elif ((seconds > 31800) and (seconds <= 32280)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32280

            elif ((seconds > 32280) and (seconds <= 35460)):
                period = "Period 1"
                startTime = 32280
                endTime = 35460

            elif ((seconds > 35460) and (seconds <= 38640)):
                period = "Period 2"
                startTime = 35460
                endTime = 38640

            elif ((seconds > 38640) and (seconds <= 39840)):
                period = "Recess"
                startTime = 38640
                endTime = 39840

            elif ((seconds > 39840) and (seconds <= 43020)):
                period = "Period 3"
                startTime = 39840
                endTime = 43020

            elif ((seconds > 43020) and (seconds <= 46200)):
                period = "Period 4"
                startTime = 43020
                endTime = 46200

            elif ((seconds > 46200) and (seconds <= 48540)):
                period = "Lunch"
                startTime = 46200
                endTime = 48540

            elif ((seconds > 48540) and (seconds <= 51720)):
                period = "Period 5"
                startTime = 48540
                endTime = 51720

            elif ((seconds > 51720) and (seconds <= 54900)):
                period = "Period 6"
                startTime = 51720
                endTime = 54900

            elif ((seconds > 54900) and (seconds <= 86400)):
                period = "After School"
                startTime = 54900
                endTime = 86400





        elif ((day == "Saturday") or (day == "Sunday")):


            if ((seconds > 00000) and (seconds <= 31800)):
                period = "Before School"
                startTime = 00000
                endTime = 31800
            elif ((seconds > 31800) and (seconds <= 32400)):
                period = "Roll Call"
                startTime = 31800
                endTime = 32400
            elif ((seconds > 32400) and (seconds <= 34800)):
                period = "Period 1"
                startTime = 32400
                endTime = 34800
            elif ((seconds > 34800) and (seconds <= 35100)):
                period = "Break 1-2"
                startTime = 34800
                endTime = 35100
            elif ((seconds > 35100) and (seconds <= 37500)):
                period = "Period 2"
                startTime = 35100
                endTime = 37500
            elif ((seconds > 37500) and (seconds <= 38700)):
                period = "Recess"
                startTime = 37500
                endTime = 38700
            elif ((seconds > 38700) and (seconds <= 41100)):
                period = "Period 3"
                startTime = 38700
                endTime = 41100
            elif ((seconds > 41100) and (seconds <= 41400)):
                period = "Break 3-4"
                startTime = 41100
                endTime = 41400
            elif ((seconds > 41400) and (seconds <= 43800)):
                period = "Period 4"
                startTime = 41400
                endTime = 43800
            elif ((seconds > 43800) and (seconds <= 46200)):
                period = "Lunch"
                startTime = 43800
                endTime = 46200
            elif ((seconds > 46200) and (seconds <= 48600)):
                period = "Period 5"
                startTime = 46200
                endTime = 48600
            elif ((seconds > 48600) and (seconds <= 48900)):
                period = "Break 5-6"
                startTime = 48600
                endTime = 48900
            elif ((seconds > 48900) and (seconds <= 51300)):
                period = "Period 6"
                startTime = 48900
                endTime = 51300
            elif ((seconds > 51300) and (seconds <= 86400)):
                period = "After School"
                startTime = 51300
                endTime = 86400
            else:
                period = "NULL"




        return [("timetable", {"title": "Current Period", "description": ("<@&877323402329866240>" + " " + "It is" + " " + ((datetime.today()).strftime("%A")) + ", " + week + ", " + period + "\n" + "Starting" + " " + ("<" + "t" + ":" + (str((int(midnight.timestamp())) + startTime)) + ":" + "R" + ">") + " and " + "Ending" + " " + ("<" + "t" + ":" + (str((int(midnight.timestamp())) + endTime)) + ":" + "R" + ">"))}), "embed"]




    async def removeMessages(self):

        parameters = await self.getParameters()

        try:
            limit = (int(parameters))

            if ((limit >= 0) and (limit <= 128)):
                pass
            elif (limit < 0):
                return [("invalidParameters", {"description": ("search limit is too low" + "\n" + "command should be in the format" + " " + (format("\\cl|clear <searchlimit>", "code")))}), "embed"]
            elif (limit > 128):
                return [("invalidParameters", {"description": ("search limit is too high" + "\n" + "command should be in the format" + " " + (format("\\cl|clear <searchlimit>", "code")))}), "embed"]

        except Exception as exception:
            return [("invalidParameters", {"description": ("search limit is not an integer" + "\n" + "command should be in the format" + " " + (format("\\cl|clear <searchlimit>", "code")))}), "embed"]


        his = await ((callingMessage.channel.history(limit = limit)).flatten())
        hisLen = (len(his))

        repeats = 0
        while (repeats < hisLen):

            if (((his[repeats]).author.id) == (self.user.id)):
                await (his[repeats]).delete()

            repeats = repeats + 1

        return [("taskCompleted", {"description": "Messages cleared!"}), "embed"]











    async def getParameters(self):

        global virtualParameters

        if (virtualParameters == None):

            try:
                parameters = (str((((callingMessage.content)[1:]).split(" ", 1))[1]))
            except Exception as exception:
                parameters = ""

        elif (virtualParameters != None):
            parameters = (str(virtualParameters))
            virtualParameters = None

        return parameters





    def createEmbed(self, embedName, modifications = {}):

        newEmbed = generatedEmbeds[embedName]
        newEmbed.set_footer(text = ("Requested by" + " " + (self.generateDisplayName())), icon_url = (callingMessage.author.avatar_url))

        if ("title" in modifications):
            newEmbed.title = (modifications["title"])
        if ("description" in modifications):
            newEmbed.description = (modifications["description"])
        if ("author" in modifications):
            newEmbed.author = (modifications["author"])

        return newEmbed



    async def getUptime(self):
        return [("uptime", {"title": "Time since start", "description": ((format("Time:", "bolden")) + " " + (format(((datetime.now()) - startTime), "code")))}), "embed"]



    async def generateRandom(self):


        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

        elif (parameters != ""):

            try:
                startValue = ((parameters.split(" ", 1))[0])
                endValue = ((parameters.split(" ", 1))[1])

                try:
                    startValue = (int(startValue))
                    endValue = (int(endValue))

                    if (startValue <= endValue):
                        startValue = startValue
                        endValue = endValue
                    elif (startValue > endValue):
                        tempValue = startValue
                        startValue = endValue
                        endValue = tempValue

                    if ((startValue >= -18446744073709551615) and (startValue <= 18446744073709551615)):
                        pass
                    elif ((startValue < -18446744073709551615) or (startValue > 18446744073709551615)):
                        return [("invalidParameters", {"description": ("start value is out of range" + "\n" + "command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

                    if ((endValue >= -18446744073709551615) and (endValue <= 18446744073709551615)):
                        pass
                    elif ((endValue < -18446744073709551615) or (endValue > 18446744073709551615)):
                        return [("invalidParameters", {"description": ("start value is out of range" + "\n" + "command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

                    return [("randomNumber", {"title": "Random number Generator", "description": ((format("Result:", "bolden")) + " " + (format(("    " + (str(random_randint(startValue, endValue))) + "    "), "code")))}), "embed"]

                except Exception as exception:
                    return [("invalidParameters", {"description": ("values provided are not integers" + "\n" + "command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]

            except Exception as exception:
                return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\rng|random <start> <end>", "code")))}), "embed"]





    async def generateBlock(self, type):

        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <parameters>", "code")))}), "embed"]

        elif (parameters != ""):

            comment = ""

            if ((parameters.isidentifier()) == True):
                comment = comment
            elif ((parameters.isidentifier()) == False):
                comment = comment + "# variable name is not valid\n"

            if ((len(parameters)) <= 1024):
                comment = comment
            elif ((len(parameters)) > 1024):
                return [("invalidParameters", {"description": ("variable name is too long" + "\n" + "command should be in the format" + " " + (format("\\command <variable> <size>", "code")))}), "embed"]

            if (type == "Zero"):
                return [(format((comment + "\nif (" + parameters + " == 0):\n    print(" + parameters + ")\nelif (" + parameters + " != 0):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]
            elif (type == "Empty"):
                return [(format((comment + "\nif (" + parameters + " == \"\"):\n    print(" + parameters + ")\nelif (" + parameters + " != \"\"):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]
            elif (type == "Long"):
                return [(format((comment + "\nif ((len(" + parameters + ")) == 0):\n    print(" + parameters + ")\nelif ((len(" + parameters + ")) != 0):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]


            elif ((type == "Greater") or (type == "Less") or (type == "GreaterLess")):

                comment = ""

                try:
                    variable = ((parameters.split(" ", 1))[0])
                    size = ((parameters.split(" ", 1))[1])
                except Exception as exception:
                    return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <variable> <size>", "code")))}), "embed"]

                if ((variable.isidentifier()) == True):
                    comment = comment
                elif ((variable.isidentifier()) == False):
                    comment = "# variable name is not valid\n"

                if ((size.isdigit()) == True):
                    comment = comment
                elif ((size.isdigit()) == False):
                    comment = comment + "# int provided is not valid\n"

                if (type == "Greater"):
                    return [(format((comment + "\nif (" + variable + " > " + size + "):\n    print(" + variable + ")\nelif (" + variable + " <= " + size + "):\n    pass"), "cBlock", "python")), "message"]
                elif (type == "Less"):
                    return [(format((comment + "\nif (" + variable + " < " + size + "):\n    print(" + variable + ")\nelif (" + variable + " >= " + size + "):\n    pass"), "cBlock", "python")), "message"]
                elif (type == "GreaterLess"):

                    comment = ""

                    try:
                        minsize = ((size.split(" ", 1))[0])
                        maxsize = ((size.split(" ", 1))[1])

                        try:
                            (int(minsize))
                            (int(maxsize))

                            if ((int(minsize)) < (int(maxsize))):
                                comment = comment
                            elif ((int(minsize)) >= (int(maxsize))):
                                comment = comment + "# arguments are not valid in this context\n"

                            if ((variable.isidentifier()) == True):
                                comment = comment
                            elif ((variable.isidentifier()) == False):
                                comment = "# variable name is not valid\n"

                        except Exception as exception:
                            comment = comment + "# arguments are not valid in this context\n"


                    except Exception as exception:
                        return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <variable> <minsize> <maxsize>", "code")))}), "embed"]

                    return [(format((comment + "\nif ((" + variable + " > " + minsize + ") and (" + variable + " <= " + maxsize + ")):\n    print(" + variable + ")\nelif ((" + variable + " <= " + minsize + ") or (" + variable + " > " + maxsize + ")):\n    pass"), "cBlock", "python")), "message"]

            elif (type == "Truthy"):
                return [(format((comment + "\nif (" + parameters + " == True):\n    print(" + parameters + ")\nelif (" + parameters + " == False):\n    print(" + parameters + ")"), "cBlock", "python")), "message"]
            elif (type == "FIterator"):
                return [(format((comment + "\nfor (i in " + parameters + "):\n    print(i)"), "cBlock", "python")), "message"]
            elif (type == "WIterator"):
                return [(format((comment + "\n" + parameters + "Length = (len(" + parameters + "))\n\nrepeats = 0\nwhile (repeats < " + parameters + "Length):\n    print(" + parameters + "[repeats])\n    repeats = repeats + 1"), "cBlock", "python")), "message"]
            elif (type == "DIterator"):
                return [(format((comment + "\n" + parameters + "Keys = list(" + parameters + ".keys())\n" + parameters + "KeysLength = (len(" + parameters + "Keys))\nrepeats = 0\nwhile (repeats < " + parameters + "KeysLength):\n    print(" + parameters + "[(" + parameters + "Keys[repeats])])\n    repeats = repeats + 1"), "cBlock", "python")), "message"]
            elif (type == "Filey"):
                return [(format((comment + "\n" + "# import json\n" + parameters + "File = open(r\"C:\\Users\", \"r\")\n" + parameters + "Text = " + parameters + "File.read()\n" + parameters + "Json = json.loads(" + parameters + "Text)\n" + parameters + "File.close()"), "cBlock", "python")), "message"]




    async def readIcal(self):

        print(callingMessage)

        if ((((((callingMessage.attachments)[0]).filename)[-3:]) == "ics") and (((((callingMessage.attachments)[0]).filename)[0:12]) == "my_timetable") and ((((callingMessage.attachments)[0]).size) < 102400)):
            print(((callingMessage.attachments)[0]))
            rawIcal = await (((callingMessage.attachments)[0]).read())
            print(rawIcal)

        return [("unused"), "message"]






    async def prettyPrint(self):

        parameters = await self.getParameters()



        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <parameters>", "code")))}), "embed"]

        elif (parameters != ""):

            try:
                jsonDictionary = (json_loads(str(parameters)))
                prettyJsonDictionary = json_dumps(jsonDictionary, indent = 4)
                return [(format(prettyJsonDictionary, "cBlock", "json")), "message"]
            except Exception as exception:
                return [(format(("Invalid JSON" + ", " + "(" + (str(exception)) + ")"), "code")), "message"]






    def reformatIterable(self, data, maxDepth = 2, depth = 1):

        if (depth <= maxDepth):


            if ((type(data)) == tuple):

                data = (list(data))

                dataLength = (len(data))
                repeats1 = 0
                while (repeats1 < dataLength):
                    data[repeats1] = self.reformatIterable(data, maxDepth, (depth + 1))
                    repeats1 = repeats1 + 1

                data = (tuple(data))

            elif ((type(data)) == dict):

                dataKeys = list(data.keys())

                dataKeysLength = (len(dataKeys))
                repeats1 = 0
                while (repeats1 < dataKeysLength):
                    data[dataKeys] = data[repeats1] = self.reformatIterable(data, maxDepth, (depth + 1))
                    repeats1 = repeats1 + 1

            elif ((type(data)) == list):

                dataLength = (len(data))
                repeats1 = 0
                while (repeats1 < dataLength):
                    data[repeats1] = self.reformatIterable(data, maxDepth, (depth + 1))
                    repeats1 = repeats1 + 1


            return (data)


        elif (depth > maxDepth):
            try:
                return (data.id)

            except Exception as exception:

                if (((type(data)) == tuple) or ((type(data)) == dict) or ((type(data)) == list)):
                    return (data)
                elif (((type(data)) != tuple) and ((type(data)) != dict) and ((type(data)) != list)):
                    return (repr(data))








    def reformatJSON(self, jsonToFormat):

        if ((type(jsonToFormat)) == dict):

            jsonToFormatKeys = list(jsonToFormat.keys())
            jsonToFormatKeysLength = (len(jsonToFormatKeys))
            
            repeats = 0
            while (repeats < jsonToFormatKeysLength):

                if ((type(jsonToFormat[(jsonToFormatKeys[repeats])])) == dict):
                    
                    if ((len(jsonToFormat[(jsonToFormatKeys[repeats])])) == 0):
                        del(jsonToFormat[(jsonToFormatKeys[repeats])])
                    elif ((len(jsonToFormat[(jsonToFormatKeys[repeats])])) == 1):
                        jsonToFormat[((jsonToFormatKeys[repeats]) + "." + ((list((jsonToFormat[(jsonToFormatKeys[repeats])]).keys()))[0]))] = ((jsonToFormat[(jsonToFormatKeys[repeats])])[((list((jsonToFormat[(jsonToFormatKeys[repeats])]).keys()))[0])])
                        del(jsonToFormat[(jsonToFormatKeys[repeats])])
                    elif (((len(jsonToFormat[(jsonToFormatKeys[repeats])])) != 0) and ((len(jsonToFormat[(jsonToFormatKeys[repeats])])) != 1)):
                        (jsonToFormat[(jsonToFormatKeys[repeats])]) = self.reformatJSON(jsonToFormat[(jsonToFormatKeys[repeats])])
                        
                elif ((type(jsonToFormat[(jsonToFormatKeys[repeats])])) == list):
                    (jsonToFormat[(jsonToFormatKeys[repeats])]) = self.reformatJSON(jsonToFormat[(jsonToFormatKeys[repeats])])

                repeats = repeats + 1



            return jsonToFormat


        elif ((type(jsonToFormat)) == list):

            jsonToFormatLength = (len(jsonToFormat))

            repeats = 0
            while (repeats < jsonToFormatLength):

                if ((type(jsonToFormat[repeats])) == dict):
                    jsonToFormat[repeats] = self.reformatJSON(jsonToFormat[repeats])
                elif ((type(jsonToFormat[repeats])) == list):
                    jsonToFormat[repeats] = self.reformatJSON(jsonToFormat[repeats])

                    
                repeats = repeats + 1



            return jsonToFormat











    def reformatCategory(self, data, maxDepth = 1, depth = 1):

        if (depth <= maxDepth):



            if (depth < maxDepth):
                wantedAttributes = (discordClassAttributesOverridesDict[(type(data))])
            elif (depth >= maxDepth):
                wantedAttributes = (discordClassAttributesOverridesOverridesDict[(type(data))])


            wantedAttributesLength = (len(wantedAttributes))
            knownAttributes = {}

            repeats = 0
            while (repeats < wantedAttributesLength):

                try:

                    newAttribute = (eval("data" + "." + (wantedAttributes[repeats])))


                    if ((type(newAttribute)) in discordClassNamesDict):

                        if ((isinstance(newAttribute, (discord.Asset))) == True):
                            newAttribute = (str(newAttribute))
                        elif ((isinstance(newAttribute, (discord.Asset))) == False):
                            newAttribute = self.reformatCategory(newAttribute, maxDepth, (depth + 1))

                    elif ((type(newAttribute)) == str):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == int):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == float):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == tuple):

                        newAttribute = (list(newAttribute))

                        newAttributeLength = (len(newAttribute))
                        repeats1 = 0
                        while (repeats1 < newAttributeLength):
                            newAttribute[repeats1] = (self.reformatCategory((newAttribute[repeats1]), maxDepth, (depth + 1)))
                            repeats1 = repeats1 + 1

                        newAttribute = (tuple(newAttribute))

                    elif ((type(newAttribute)) == bool):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == dict):

                        newAttributeKeys = list(newAttribute.keys())

                        newAttributeKeysLength = (len(newAttributeKeys))
                        repeats1 = 0
                        while (repeats1 < newAttributeKeysLength):
                            newAttribute[newAttributeKeys] = (repr(newAttribute[newAttributeKeys]))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == list):

                        newAttributeLength = (len(newAttribute))
                        repeats1 = 0
                        while (repeats1 < newAttributeLength):
                            newAttribute[repeats1] = (self.reformatCategory((newAttribute[repeats1]), maxDepth, (depth + 1)))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == datetime):
                        newAttribute = (newAttribute.isoformat())
                    else:

                        try:
                            newAttribute = [(newAttribute.name), (newAttribute.value)]

                        except Exception as exception:
                            newAttribute = (repr(newAttribute))


                    knownAttributes[(wantedAttributes[repeats])] = newAttribute

                except Exception as exception:
                    knownAttributes[(wantedAttributes[repeats])] = None

                repeats = repeats + 1

            return knownAttributes









        elif (depth > maxDepth):
            try:
                return (data.id)

            except Exception as exception:

                if (((type(data)) == str) or ((type(data)) == int) or ((type(data)) == float) or ((type(data)) == tuple) or ((type(data)) == bool) or ((type(data)) == dict) or ((type(data)) == list) or ((type(data)) == datetime)):
                    return (data)
                elif (((type(data)) != str) and ((type(data)) != int) and ((type(data)) != float) and ((type(data)) != tuple) and ((type(data)) != bool) and ((type(data)) != dict) and ((type(data)) != list) and ((type(data)) != datetime)):
                    return (repr(data))

















    def reformatMessage(self, data, maxDepth = 1, depth = 1):

        if (depth <= maxDepth):

            wantedAttributes = [
                "channel.name",
                "author.display_name",
                "created_at",
                "content",
            ]


            wantedAttributesLength = (len(wantedAttributes))
            knownAttributes = {}

            repeats = 0
            while (repeats < wantedAttributesLength):

                try:

                    newAttribute = (eval("data" + "." + (wantedAttributes[repeats])))


                    if ((type(newAttribute)) in discordClassNamesDict):
                        newAttribute = self.reformatCategory(newAttribute, maxDepth, (depth + 1))
                    elif ((type(newAttribute)) == str):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == int):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == float):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == tuple):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == bool):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == dict):

                        newAttributeKeys = list(newAttribute.keys())

                        newAttributeKeysLength = (len(newAttributeKeys))
                        repeats1 = 0
                        while (repeats1 < newAttributeKeysLength):
                            newAttribute[newAttributeKeys] = (repr(newAttribute[newAttributeKeys]))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == list):

                        newAttributeLength = (len(newAttribute))
                        repeats1 = 0
                        while (repeats1 < newAttributeLength):
                            newAttribute[repeats1] = (repr(self.reformatCategory((newAttribute[repeats1]), maxDepth, (depth + 1))))
                            repeats1 = repeats1 + 1

                    elif ((type(newAttribute)) == datetime):
                        newAttribute = (newAttribute.isoformat())
                    else:
                        newAttribute = (repr(newAttribute))

                    knownAttributes[(wantedAttributes[repeats])] = newAttribute

                except Exception as exception:
                    knownAttributes[(wantedAttributes[repeats])] = None

                repeats = repeats + 1


            return knownAttributes









        elif (depth > maxDepth):
            try:
                return (data.id)

            except Exception as exception:

                if (((type(data)) == str) or ((type(data)) == int) or ((type(data)) == float) or ((type(data)) == tuple) or ((type(data)) == bool) or ((type(data)) == dict) or ((type(data)) == list) or ((type(data)) == datetime)):
                    return (data)
                elif (((type(data)) != str) and ((type(data)) != int) and ((type(data)) != float) and ((type(data)) != tuple) and ((type(data)) != bool) and ((type(data)) != dict) and ((type(data)) != list) and ((type(data)) != datetime)):
                    return (repr(data))




















    def reformatData(self, data, maxDepth = 3, depth = 1):

        if (depth <= maxDepth):

            returnData = {}

            dataAttributes = discordClassAttributesDict[(type(data))]
            dataLength = (len(dataAttributes))

            repeats = 0
            while (repeats < (dataLength - 1)):

                try:

                    newAttribute = (getattr(data, (dataAttributes[repeats])))

                    if ((type(newAttribute)) in discordClassNamesDict):
                        newAttribute = self.reformatData(newAttribute, maxDepth, (depth + 1))
                    elif ((type(newAttribute)) == str):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == int):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == float):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == tuple):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == bool):
                        newAttribute = newAttribute
                    elif ((type(newAttribute)) == dict):
                        newAttribute = (repr(newAttribute))
                    elif ((type(newAttribute)) == list):
                        newAttribute = (repr(newAttribute))
                    elif ((type(newAttribute)) == datetime):
                        newAttribute = (newAttribute.isoformat())
                    else:
                        newAttribute = (repr(newAttribute))


                    if (len(newAttribute) < attributeMaxLength):
                        newAttribute = newAttribute
                    elif (len(newAttribute) >= attributeMaxLength):
                        newAttribute = ("<" + "Warning" + ":" + " " + "Attribute is longer than" + " " + (str(attributeMaxLength)) + " " + "characters" + ">")

                    returnData[(dataAttributes[repeats])] = newAttribute

                except Exception as exception:

                    returnData[(dataAttributes[repeats])] = (None)




                repeats = repeats + 1

            return [(returnData), "message"]

        elif (depth > maxDepth):
            return [(repr(data)), "message"]






    def evaluateBoolean(self, booleanString):
        booleanYes = ["true", "1", "=", "+", "on", "yes"]
        booleanNo = ["false", "0", "-", "off", "no"]

        if ((booleanString.lower()) in booleanYes):
            return True
        elif ((booleanString.lower()) in booleanNo):
            return False
        else:
            raise Exception("ERROR")






    def evaluatePositive(self, positiveInt):

        if (positiveInt < 1):
            raise Exception("ERROR")
        elif (positiveInt >= 1):
            pass



    async def createProgress(self, percentage):

        global progressMessage
        global progressMessagePercentage

        if (percentage == progressMessagePercentage):
            pass
        elif (percentage != progressMessagePercentage):

            if (percentage < 100):

                progressMessagePercentage = percentage

                width = 20
                progressCharacters = ["\u2593", "\u2591"]

                progress = (percentage / 100)

                progressDisplay = ""
                progressDisplay = progressDisplay.ljust((round(progress * width)), (progressCharacters[0]))
                progressDisplay = progressDisplay.ljust((round(width)), (progressCharacters[1]))

                if (progressMessage == None):

                    progressMessage = await callingMessage.channel.send(content = ("processing" + ": " + progressDisplay + " " + (str(percentage)) + "%"), embed = None)
                    await callingMessage.channel.trigger_typing()

                elif (progressMessage != None):

                    await progressMessage.edit(content = ("processing" + ": " + progressDisplay + " " + (str(percentage)) + "%"), embed = None)

            elif (percentage >= 100):

                if (progressMessage == None):
                    pass
                elif (progressMessage != None):

                    await progressMessage.delete()

                    progressMessage = None










    async def getHistory(self):

        parameters = await self.getParameters()

        if (parameters == ""):
            return [("unspecifiedParameters", {"description": ("command should be in the format" + " " + (format("\\command <message|server|channel|category> <condensed> <searchlimit> <depth>", "code")))}), "embed"]

        elif (parameters != ""):

            await self.createProgress(0)

            try:
                type = ((parameters.split(" ", 3))[0])
                condensed = ((parameters.split(" ", 3))[1])
                collapsed = ((parameters.split(" ", 3))[2])
                options = ((parameters.split(" ", 3))[3])

                messageLimit = ((options.split(" ", 1))[0])
                maximumDepth = ((options.split(" ", 1))[1])



                condensed = (self.evaluateBoolean(condensed))
                collapsed = (self.evaluateBoolean(collapsed))

                messageLimit = (int(messageLimit))
                maximumDepth = (int(maximumDepth))

                self.evaluatePositive(messageLimit)
                self.evaluatePositive(maximumDepth)


            except Exception as exception:
                return [("invalidParameters", {"description": ("command should be in the format" + " " + (format("\\command <searchLimit> <maximumDepth>", "code")))}), "embed"]


            attribs = []
            dataToSend = {}

            await self.createProgress(10)

            if (condensed == True):






                if (type == "message"):

                    if (((messageLimit * (8 ** maximumDepth)) >= 0) and ((messageLimit * (8 ** maximumDepth)) <= 262144)):
                        pass
                    elif ((messageLimit * (8 ** maximumDepth)) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((messageLimit * (8 ** maximumDepth)) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]



                    messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())

                    await self.createProgress(40)

                    messageHistoryLength = (len(messageHistory))

                    repeats = 0
                    while (repeats < messageHistoryLength):

                        attribs.append(self.reformatCategory((messageHistory[repeats]), maximumDepth))

                        repeats = repeats + 1


                    await self.createProgress(60)


                    dataToSend["common"] = {}
                    dataToSend["common"]["guild.id"] = ((messageHistory[0]).guild.id)
                    dataToSend["common"]["channel.category.id"] = ((messageHistory[0]).channel.category.id)
                    dataToSend["common"]["channel.id"] = ((messageHistory[0]).channel.id)


                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["messages"] = attribs


                elif (type == "server"):

                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    await self.createProgress(40)

                    attribs.append(self.reformatCategory(((messageHistory[0]).guild), maximumDepth))

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs

                    dataToSend["server"] = attribs





                elif (type == "channel"):

                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]

                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())
                    channelsLength = (len((messageHistory[0]).guild.channels))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < channelsLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.channels[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["channels"] = attribs


                elif (type == "role"):


                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    rolesLength = (len((messageHistory[0]).guild.roles))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < rolesLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.roles[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)




                    dataToSend["common"] = {}
                    dataToSend["common"]["guild.id"] = ((messageHistory[0]).guild.id)


                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["roles"] = attribs



                elif (type == "member"):


                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    membersLength = (len((messageHistory[0]).guild.members))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < membersLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.members[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["members"] = attribs




                elif (type == "emoji"):


                    if (((64 ** maximumDepth) >= 0) and ((64 ** maximumDepth) <= 262144)):
                        pass
                    elif ((64 ** maximumDepth) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((64 ** maximumDepth) > 262144):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    # maximumDepth = 1

                    # messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())
                    messageHistory = await ((callingMessage.channel.history(limit = 1)).flatten())

                    emojisLength = (len((messageHistory[0]).guild.emojis))

                    await self.createProgress(40)

                    repeats = 0
                    while (repeats < emojisLength):

                        attribs.append(self.reformatCategory(((messageHistory[0]).guild.emojis[repeats]), maximumDepth))

                        repeats = repeats + 1

                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs

                    
                    dataToSend["emojis"] = attribs




                elif ((type != "message") and (type != "server") and (type != "channel") and (type != "role") and (type != "member") and (type != "emoji")):
                    await self.createProgress(100)
                    return [("invalidParameters", {"description": ("command should be in the format" + " " + (format("\\command <searchLimit> <maximumDepth>", "code")))}), "embed"]











            elif (condensed == False):








                if (type == "message"):

                    if (((messageLimit * (8 ** maximumDepth)) >= 0) and ((messageLimit * (8 ** maximumDepth)) <= 256)):
                        pass
                    elif ((messageLimit * (8 ** maximumDepth)) < 0):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too low!", "code")), "message"]
                    elif ((messageLimit * (8 ** maximumDepth)) > 256):
                        await self.createProgress(100)
                        return [(format("Maximum search/depth is too high!", "code")), "message"]


                    messageHistory = await ((callingMessage.channel.history(limit = messageLimit)).flatten())

                    await self.createProgress(40)

                    messageHistoryLength = (len(messageHistory))

                    repeats = 0
                    while (repeats < messageHistoryLength):

                        attribs.append(self.reformatData((messageHistory[repeats]), maximumDepth))
                        print(messageHistory[repeats])
                        # return (repr(attribs))

                        repeats = repeats + 1


                    await self.createProgress(60)



                    if (collapsed == True):
                        attribs = self.reformatJSON(attribs)
                    elif (collapsed == False):
                        attribs = attribs


                    dataToSend["messages"] = attribs






                elif (type == "server"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]

                elif (type == "channel"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]

                elif (type == "role"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]


                elif (type == "member"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]

                elif (type == "emoji"):
                    await self.createProgress(100)
                    return [(format("too slow for use", "code")), "message"]


                elif ((type != "message") and (type != "server") and (type != "channel") and (type != "role") and (type != "member") and (type != "emoji")):
                    await self.createProgress(100)
                    return [("invalidParameters", {"description": ("command should be in the format" + " " + (format("\\command <searchLimit> <maximumDepth>", "code")))}), "embed"]





            await self.createProgress(80)

            await self.createProgress(100)



            # print(dataToSend)


            dataToSend["metadata"] = {}
            dataToSend["metadata"]["message"] = (callingMessage.jump_url)
            dataToSend["metadata"]["caller"] = (callingMessage.author.id)
            dataToSend["metadata"]["guild"] = (callingMessage.guild.id)
            dataToSend["metadata"]["date"] = ((callingMessage.created_at).isoformat())
            dataToSend["metadata"]["parameters"] = {}
            dataToSend["metadata"]["parameters"]["type"] = type
            dataToSend["metadata"]["parameters"]["condensed"] = condensed
            dataToSend["metadata"]["parameters"]["messageLimit"] = messageLimit
            dataToSend["metadata"]["parameters"]["maximumDepth"] = maximumDepth




            return [(format((json_dumps(dataToSend, indent = 2)), "cBlock", "json")), "message"]








    async def createMessage(self, originalMessage, function = None, message = "\u200B", embed = None, deleteTime = None, permissions = 0):

        global callingMessage
        callingMessage = originalMessage

        passedPerms = True
        file = None

        if ((permissions & 1) == 1):

            if ((originalMessage.author.id) in authorisedUsers):
                passedPerms = passedPerms & True
            elif ((originalMessage.author.id) not in authorisedUsers):
                passedPerms = passedPerms & False
                await self.sendMessage({"content": None, "embed": (self.createEmbed("unauthorisedUser", {"description": (format(("You have not been authorised to use the command" + " " + "[" + (((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) + "]" + "!"), "code"))})), "delete_after": 8, "allowed_mentions": None})

        elif ((permissions & 1) != 1):
            passedPerms = passedPerms & True


        if ((permissions & 2) == 2):
            passedPerms = passedPerms & True
        elif ((permissions & 2) != 2):

            if (commandsEnabled == True):
                passedPerms = passedPerms & True
            elif (commandsEnabled == False):
                passedPerms = passedPerms & False
                await self.sendMessage({"content": None, "embed": (self.createEmbed("commandDisabled", {"description": (format(("The command" + " " + "[" + (((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) + "]" + " " + "has been disabled" + "!"), "code"))})), "delete_after": 8, "allowed_mentions": None})






        if (passedPerms == True):

            if (function == None):
                message = message
            elif (function != None):

                dataToSend = await (eval("self" + "." + function))


                if ((dataToSend[1]) == "message"):
                    message = (dataToSend[0])

                elif ((dataToSend[1]) == "embed"):
                    embed = (dataToSend[0])

                try:

                    if ((dataToSend[3]) == None):
                        additionalSendOptions = False
                    elif ((dataToSend[3]) != None):
                        additionalSendOptions = True

                except Exception as exception:
                    additionalSendOptions = False









            if ((message == None) and (embed == None) and (file == None)):
                pass
            elif ((message != None) or (embed != None) or (file != None)):




                if (deleteMessages == True):
                    deleteTime = deleteTime
                elif (deleteMessages == False):
                    deleteTime = None

                if (embed == None):
                    embed = None
                if (embed != None):
                    await self.printOutputToLogs(embed, callingMessage)

                    if ((type(embed)) == tuple):
                        embed = self.createEmbed((embed[0]), (embed[1]))
                    elif ((type(embed)) != tuple):
                        embed = self.createEmbed(embed)



                    if (((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) == "?") or ((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) == "help")):
                        await self.sendMessage({"content": message, "embed": embed, "delete_after": deleteTime}, ["<:home:882810562126417930>", "<:restricted:882810562214518835>", "<:automated:915861328235757599>", "<:code:882810561690222613>", "<:symbols:882810561786699817>", "<:acknowledgements:882810562055131186>"])


                    elif (((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) != "?") and ((((((callingMessage.content)[1:]).split(" ", 1))[0]).lower()) != "help")):
                        await self.sendMessage({"content": message, "embed": embed, "delete_after": deleteTime})





                elif (message != None):

                    if (len(message) < 2000):
                        
                        if (additionalSendOptions == True):
                            await self.sendMessage({"content": message, "delete_after": deleteTime, "reference": (dataToSend[3][0]), "mention_author": (dataToSend[3][1])})
                        elif (additionalSendOptions == False):
                            await self.sendMessage({"content": message, "delete_after": deleteTime})


                    elif (len(message) >= 2000):

                        if ((((bool(re.search("^```.{0,24}\n", (message[0:32]))))) == True) and ((bool(re.search("```$", (message[-8:])))) == True)):
                            extension = (message[(((re.search("^```.{0,24}\n", (message[0:32]))).start()) + 3):(((re.search("^```.{0,24}\n", (message[0:32]))).end()) - 1)])
                            message = message[((re.search("^```.{0,24}\n", (message[0:32]))).end()):(((re.search("```$", (message[-8:]))).start()) - 8)]
                            tempFile = io.BytesIO(message.encode())
                            discordFile = (discord.File(tempFile, ("message" + "." + extension)))
                        elif ((((bool(re.search("^```.{0,24}\n", (message[0:32]))))) == False) or ((bool(re.search("```$", (message[-8:])))) == False)):
                            tempFile = io.BytesIO(message.encode())
                            discordFile = (discord.File(tempFile, "message.txt"))

                        await self.sendMessage({"file": discordFile, "delete_after": deleteTime})






        elif (passedPerms == False):
            print(callingMessage)








    async def on_ready(self):

        global botItself
        global botMaster
        global botLogger
        # global botSecondaryLogger
        global virtualParameters
        global connectedVoiceChannels

        botItself = await client.fetch_user(self.user.id)
        botMaster = await client.fetch_user(master)
        botLogger = await client.fetch_channel(logChannel)
        # botSecondaryLogger = await client.fetch_channel(887489153418289202)
        connectedVoiceChannels = []

        await self.addListeners()

        await self.printOutputToLogs("Logged in as " + "'" + (str(self.user.name)) + "'" + " (" + (str(self.user.id)) + ")")

        # virtualParameters = defaultStatus
        # await self.setStatus()



        async def changeStatusLoop():
            await self.changeStatus()

        
        changeStatusLoop = (discord.ext.tasks.loop(minutes = 120)(changeStatusLoop))
        changeStatusLoop.start()



        """


        countingChannel = await client.fetch_channel(882058561377673228)
        baseCount = (int((await ((countingChannel.history(limit = 1)).flatten()))[0]))
        maximumCount = 10
        repeats = 0
        while (repeats < maximumCount):
            await countingChannel.send(str(baseCount + repeats))
            repeats = repeats + 1


        """






    async def on_message(self, message):

        if ((message.author.id) == (self.user.id)):
            pass

        elif ((message.author.id) != (self.user.id)):

            if ((message.author.bot) == True):
                pass



            elif ((message.author.bot) == False):




                global callingMessage
                messageContent = message.content




                if ((len(message.mentions)) > 0):

                    if ((message.guild.id) in pingListeningGuilds):

                        callingMessage = message
                        messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])
                        messageMentions = ""


                        repeats = 0
                        while (repeats < (len(message.mentions))):
                            messageMentions = messageMentions + (((message.mentions)[repeats]).mention) + ", "
                            repeats = repeats + 1


                        messageMentions = messageMentions[0:-2]

                        await messageGuildLogChannel.send((((message.author).mention) + "\n" + (format("mentioned", "bold")) + "\t" + messageMentions + "\n" + (format("in", "bold")) + "\t\t\t\t\t" + ((message.channel).mention) + "\n" + (format("at", "bold")) + "\t\t\t\t\t" + (("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "d" + ">")) + " " + ("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "T" + ">")) + " " + "(" + (format((str(((message.created_at).timestamp()) - timeOffset)), "code")) + ")") + "\n" + (format("with", "bold")) + "\n" + (format((message.content), ["quote", "cBlock"]))), allowed_mentions = (discord.AllowedMentions(users = False)))




                if ((len(message.role_mentions)) > 0):

                    if ((message.guild.id) in pingListeningGuilds):

                        callingMessage = message
                        messageGuildLogChannel = await client.fetch_channel(pingListeningGuildsLogs[(message.guild.id)])

                        messageMentions = ""


                        repeats = 0
                        while (repeats < (len(message.role_mentions))):
                            messageMentions = messageMentions + (((message.role_mentions)[repeats]).mention) + ", "
                            repeats = repeats + 1


                        messageMentions = messageMentions[0:-2]



                        await messageGuildLogChannel.send((((message.author).mention) + "\n" + (format("mentioned", "bold")) + "\t" + messageMentions + "\n" + (format("in", "bold")) + "\t\t\t\t\t" + ((message.channel).mention) + "\n" + (format("at", "bold")) + "\t\t\t\t\t" + (("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "d" + ">")) + " " + ("<" + "t" + ":" + (str(int(((message.created_at).timestamp()) - timeOffset)) + ":" + "T" + ">")) + " " + "(" + (format((str(((message.created_at).timestamp()) - timeOffset)), "code")) + ")") + "\n" + (format("with", "bold")) + "\n" + (format((message.content), ["quote", "cBlock"]))), allowed_mentions = (discord.AllowedMentions(users = False)))





                if ((bool(re.match("^register mentions logging to {0,2}<#\d{1,20}> {0,2}$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):



                        callingMessage = message

                        await message.channel.trigger_typing()
                        # messageContent = "register mentions logging to <#456>"
                        extractedMessage = []
                        splitMessageContent = (messageContent.split("register mentions logging to", 1))
                        extractedMessage.append(splitMessageContent[1])
                        print(extractedMessage)


                        try:

                            newMentionsLogsChannel = ((re.findall("<#\d{0,20}>", (extractedMessage[0])))[0])
                            newMentionsLogsChannelId = (int((re.findall("\d{1,20}", newMentionsLogsChannel))[0]))

                            if (((message.guild.id) in pingListeningGuilds) == True):
                                await self.sendMessage({"content": "mention logging already exists in this guild\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                            elif (((message.guild.id) in pingListeningGuilds) == False):

                                newMentionData = [(message.guild.id), newMentionsLogsChannelId]
                                await self.addMentionListener(newMentionData)

                                await self.sendMessage({"content": "mention logging activated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})


                        except Exception as exception:
                            await self.sendMessage({"content": "syntax error\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})



                    elif ((message.author.id) not in authorisedUsers):
                        pass






                if ((bool(re.match("^unregister mentions logging$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):



                        callingMessage = message

                        await message.channel.trigger_typing()


                        mentionDataPosition = pingListeningGuilds.index(message.guild.id)

                        if ((mentionDataPosition >= 0) and (mentionDataPosition <= (len(pingListeningGuilds)))):
                            await self.removeMentionListener(mentionDataPosition)
                            await self.sendMessage({"content": "mention logging deactivated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                        elif ((mentionDataPosition < 0) or (mentionDataPosition > (len(pingListeningGuilds)))):
                            await self.sendMessage({"content": "mention logging deactivation failed\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})


                    elif ((message.author.id) not in authorisedUsers):
                        pass











                if ((bool(re.match("^create role .{0,32}, ?#[0-9A-Fa-f]{6}$", messageContent))) == True):

                    if ((message.channel.id) in roleListeningChannels):

                        if (commandsEnabled == True):

                            callingMessage = message

                            await message.channel.trigger_typing()

                            newRole = await (message.guild).create_role(name = (messageContent[12:-9]), color = (int((messageContent[-6:]), 16)), reason = ("user" + " " + " " + " " + "requested"))
                            await newRole.edit(position = (((message.guild.get_role(roleListeningChannelsPosition[(message.channel.id)])).position) - 1))
                            await message.author.add_roles(newRole, reason = ("user" + " " + " " + " " + "requested"))
                            await self.sendMessage({"content": ("role" + " " + (newRole.mention) + " " + "created by" + " " + ((message.author).mention)), "embed": None, "delete_after": None, "allowed_mentions": None})
                            await self.addRoleListener((message.channel.id), (newRole.id))


                        elif (commandsEnabled == False):
                            pass



                elif ((bool(re.match("^create role .{0,32}, ?#[0-9A-Fa-f]{6}$", messageContent))) == False):
                    pass










                if ((bool(re.match("^assign role <@&!?\d{1,20}>$", messageContent))) == True):

                    if ((message.channel.id) in roleListeningChannels):

                        if (commandsEnabled == True):

                            callingMessage = message

                            await message.channel.trigger_typing()

                            if ((message.raw_role_mentions)[0]) in (roleListeningChannelsRoles[(message.channel.id)]):

                                await message.author.add_roles(((message.role_mentions)[0]), reason = ("user" + " " + " " + " " + "requested"))
                                await self.sendMessage({"content": ("role" + " " + (((message.role_mentions)[0]).mention) + " " + "assigned by" + " " + ((message.author).mention)), "embed": None, "delete_after": None, "allowed_mentions": None})

                            elif ((message.raw_role_mentions)[0]) not in (roleListeningChannelsRoles[(message.channel.id)]):

                                await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`role requested is not a custom role`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                        elif (commandsEnabled == False):
                            pass



                elif ((bool(re.match("^assign role <@&!?\d{1,20}>$", messageContent))) == False):
                    pass














                if ((bool(re.match("^rep /.{0,256}/, \d{1,20}$", messageContent))) == True):

                    if ((message.author.id) in authorisedUsers):



                        callingMessage = message

                        await message.channel.trigger_typing()


                        regexToMatch = ((messageContent[((re.search("^rep ", messageContent)).end()):((re.search(", \d{1,20}$", messageContent)).start())])[1:-1])
                        messagesToSearch = (int(messageContent[((re.search("\d{1,20}$", messageContent)).start()):]))



                        if ((messagesToSearch >= 0) and (messagesToSearch <= 128)):
                            pass
                        elif (messagesToSearch < 0):
                            await self.sendMessage({"content": "the number of messages requested is out of the acceptable range\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                        elif (messagesToSearch > 128):
                            await self.sendMessage({"content": "the number of messages requested is out of the acceptable range\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})



                        channelMessages = (await (((message.channel).history(limit = messagesToSearch)).flatten()))


                        messagesToDelete = []
                        messagesToDeleteDescriptions = []

                        try:

                            repeats = 0
                            while (repeats < (len(channelMessages))):

                                print(((channelMessages[repeats]).content))

                                if ((bool(re.search(regexToMatch, ((channelMessages[repeats]).content)))) == True):
                                    messagesToDelete.append(channelMessages[repeats])
                                    messagesToDeleteDescriptions.append((channelMessages[repeats]).content)

                                elif ((bool(re.search(regexToMatch, ((channelMessages[repeats]).content)))) == False):
                                    pass

                                repeats = repeats + 1


                        except Exception as exception:
                            await self.sendMessage({"content": "regex parsing error" + "\n" + "||`" + (str(exception) + "`||"), "embed": None, "delete_after": None, "allowed_mentions": None})



                            repeats = repeats + 1



                        print(messagesToDelete)


                        await self.sendMessage({"content": ("ready to delete" + "\n" + ((json_dumps(messagesToDeleteDescriptions, separators = (",\n", ":\n")))[0:1792])), "embed": None, "delete_after": None, "allowed_mentions": None})


                    elif ((message.author.id) not in authorisedUsers):
                        pass










                # verificationListeningChannels = []
                # verificationListeningChannelsLogs = {}
                # verificationListeningChannelsRoles = {}
                # verificationListeningChannelsRequiredRoles = {}



                # messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.guild.id)])
                # await messageGuildLogChannel.send((((message.author).mention) + " " + "mentioned" + " " + (((message.mentions)[0]).mention) + "\n" + (format((json_dumps((self.reformatMessage(callingMessage, 1)), indent = 4)), "cBlock"))), allowed_mentions = (discord.AllowedMentions(users = False)))



                if ((bool(re.match("^i verify <@!?\d{1,20}>$", (messageContent.lower())))) == True):

                    if ((message.channel.id) in verificationListeningChannels):



                        callingMessage = message

                        await message.channel.trigger_typing()



                        if ((message.author.id) in authorisedUsers):

                            rolesToAddIds = (verificationListeningChannelsRoles[(message.channel.id)])
                            rolesToAdd = []

                            repeats = 0
                            while (repeats < (len(rolesToAddIds))):
                                rolesToAdd.append(message.guild.get_role(rolesToAddIds[repeats]))
                                repeats = repeats + 1

                            print(rolesToAdd)

                            await ((message.mentions)[0]).add_roles(*rolesToAdd)
                            await self.sendMessage({"content": None, "embed": (self.createEmbed("userVerified", {"description": ("verified user" + " " + (((message.mentions)[0]).name) + "#" + (((message.mentions)[0]).discriminator))})), "delete_after": None, "allowed_mentions": None})

                            messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                            await messageGuildLogChannel.send(("\u2705" + " " + ((message.author).mention) + " " + "verified" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))





                        elif ((message.author.id) not in authorisedUsers):






                            if (commandsEnabled == True):



                                requiredRoles = (verificationListeningChannelsRequiredRoles[(message.channel.id)])
                                requiredRolesIds = []

                                repeats = 0
                                while (repeats < (len(requiredRoles))):
                                    requiredRolesIds.append(message.guild.get_role(requiredRoles[repeats]))
                                    repeats = repeats + 1



                                if ((len((set(message.author.roles)).intersection(set(requiredRolesIds)))) == 0):
                                    await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`(you must have 'nsbhs' to use this command)`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                                    messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                    await messageGuildLogChannel.send(("\u274E" + " " + ((message.author).mention) + " " + "verify denied" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))

                                elif ((len((set(message.author.roles)).intersection(set(requiredRolesIds)))) != 0):

                                    if ((((message.mentions)[0]).bot) == True):
                                        await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`(you cannot verify non-humans)`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                                        messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                        await messageGuildLogChannel.send(("\u274E" + " " + ((message.author).mention) + " " + "verify denied" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))

                                    elif ((((message.mentions)[0]).bot) == False):

                                        if ((len((set(((message.mentions)[0]).roles)).intersection(set(requiredRolesIds)))) == 0):

                                            rolesToAddIds = (verificationListeningChannelsRoles[(message.channel.id)])
                                            rolesToAdd = []

                                            repeats = 0
                                            while (repeats < (len(rolesToAddIds))):
                                                rolesToAdd.append(message.guild.get_role(rolesToAddIds[repeats]))
                                                repeats = repeats + 1


                                            await ((message.mentions)[0]).add_roles(*rolesToAdd)
                                            await self.sendMessage({"content": None, "embed": (self.createEmbed("userVerified", {"description": ("verified user" + " " + (((message.mentions)[0]).name) + "#" + (((message.mentions)[0]).discriminator))})), "delete_after": None, "allowed_mentions": None})
                                            messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                            await messageGuildLogChannel.send(("\u2705" + " " + ((message.author).mention) + " " + "verified" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))

                                        elif ((len((set(((message.mentions)[0]).roles)).intersection(set(requiredRolesIds)))) != 0):
                                            await self.sendMessage({"content": "...i don't think there are enough bugs in me for that to work...\n||`(you cannot verify already verified users)`||", "embed": None, "delete_after": None, "allowed_mentions": None})
                                            messageGuildLogChannel = await client.fetch_channel(verificationListeningChannelsLogs[(message.channel.id)])
                                            await messageGuildLogChannel.send(("\u274E" + " " + ((message.author).mention) + " " + "verify denied" + " " + (((message.mentions)[0]).mention)), allowed_mentions = (discord.AllowedMentions(users = False)))





                            elif (commandsEnabled == False):
                                pass








                if ((bool(re.match("^register verification in {0,2}<#\d{1,20}> {0,2}logging to {0,2}<#\d{1,20}> {0,2}requiring {0,2}(<@&!?\d{1,20}>,? ?){1,} {0,2}applying {0,2}(<@&!?\d{1,20}>,? ?){1,} {0,2}$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):


                        callingMessage = message

                        await message.channel.trigger_typing()
                        # messageContent = "register verification in <#123> logging to <#456> requiring <@&789> applying <@&000>"
                        extractedMessage = []
                        splitMessageContent = (messageContent.split("register verification in", 1))
                        splitMessageContent = (splitMessageContent[1]).split("logging to", 1)
                        extractedMessage.append(splitMessageContent[0])
                        splitMessageContent = (splitMessageContent[1]).split("requiring", 1)
                        extractedMessage.append(splitMessageContent[0])
                        splitMessageContent = (splitMessageContent[1]).split("applying", 1)
                        extractedMessage.append(splitMessageContent[0])
                        extractedMessage.append(splitMessageContent[1])
                        print(extractedMessage)


                        try:
                            # newVerificationChannel = ((re.findall("\d{1,20}", (extractedMessage[0])))[0])
                            # newVerificationLogsChannel = ((re.findall("\d{1,20}", (extractedMessage[1])))[0])
                            # newVerificationRoles = (re.findall("\d{1,20}", (extractedMessage[2])))
                            # newVerificationAppliedRoles = (re.findall("\d{1,20}", (extractedMessage[3])))

                            newVerificationChannel = ((re.findall("<#\d{0,20}>", (extractedMessage[0])))[0])
                            newVerificationLogsChannel = ((re.findall("<#\d{0,20}>", (extractedMessage[1])))[0])
                            newVerificationRoles = (re.findall("<@&!?\d{0,20}>", (extractedMessage[2])))
                            newVerificationAppliedRoles = (re.findall("<@&!?\d{0,20}>", (extractedMessage[3])))

                            newVerificationChannelId = (int((re.findall("\d{1,20}", newVerificationChannel))[0]))
                            newVerificationLogsChannelId = (int((re.findall("\d{1,20}", newVerificationLogsChannel))[0]))
                            newVerificationRolesIds = []
                            newVerificationAppliedRolesIds = []

                            repeats = 0
                            while (repeats < (len(newVerificationRoles))):
                                newVerificationRolesIds.append(int((re.findall("\d{1,20}", (newVerificationRoles[repeats])))[0]))
                                repeats = repeats + 1

                            repeats = 0
                            while (repeats < (len(newVerificationAppliedRoles))):
                                newVerificationAppliedRolesIds.append(int((re.findall("\d{1,20}", (newVerificationAppliedRoles[repeats])))[0]))
                                repeats = repeats + 1



                            if ((newVerificationChannel in verificationListeningChannels) == True):
                                await self.sendMessage({"content": "verification already exists for the specified channel\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                            elif ((newVerificationChannel in verificationListeningChannels) == False):

                                newVerificationData = [newVerificationChannelId, newVerificationLogsChannelId, newVerificationRolesIds, newVerificationAppliedRolesIds]
                                await self.addVerificationListener(newVerificationData)

                                await self.sendMessage({"content": "verification activated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})


                        except Exception as exception:
                            await self.sendMessage({"content": "syntax error\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})




                    elif ((message.author.id) not in authorisedUsers):
                        pass



                if ((bool(re.match("^unregister verification in {0,2}<#\d{1,20}> {0,2}$", (messageContent.lower())))) == True):

                    if ((message.author.id) in authorisedUsers):

                        callingMessage = message

                        await message.channel.trigger_typing()

                        verificationDataPosition = verificationListeningChannels.index(((message.channel_mentions)[0]).id)

                        if ((verificationDataPosition >= 0) and (verificationDataPosition <= (len(verificationListeningChannels)))):
                            await self.removeVerificationListener(verificationDataPosition)
                            await self.sendMessage({"content": "verification deactivated\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})

                        elif ((verificationDataPosition < 0) or (verificationDataPosition > (len(verificationListeningChannels)))):
                            await self.sendMessage({"content": "verification deactivation failed\n||`...`||", "embed": None, "delete_after": None, "allowed_mentions": None})






                if ((messageContent.startswith("\\")) == True):

                    command = ((((messageContent[1:]).split(" ", 1))[0]).lower())




                    if (command in (validCommands["commands"])):

                        await message.channel.trigger_typing()

                        await self.createMessage(originalMessage = message, **(validCommands["preReplies"][(validCommands["replies"][command])]))


                elif ((messageContent.startswith("\\")) == False):
                    pass




                if (botItself in (message.mentions)):



                    if ((bool(re.match("^ {0,2}<@!?\d{1,20}> {0,2}$", (messageContent.lower())))) == True):


                        if (commandsEnabled == True):

                            callingMessage = message
                            await message.channel.trigger_typing()

                            await self.sendMessage({"content": "*did you mean to use* \u2009`\\?` *?*", "embed": None, "delete_after": 4, "allowed_mentions": None})

                        elif (commandsEnabled == False):
                            pass








        else:
            await self.printOutputToLogs("Something went seriously wrong at \'MyClient\\on_message\'")





    async def on_reaction_add(self, reaction, user):



        if (reactionsEnabled == True):


            if (commandsEnabled == True):




                if ((user.id) == (self.user.id)):
                    pass

                elif ((user.id) != (self.user.id)):

                    reactions = {
                        "<:home:882810562126417930>": "helpMenu",
                        "<:restricted:882810562214518835>": "restrictedHelpMenu",
                        "<:automated:915861328235757599>": "automatedHelpMenu",
                        "<:code:882810561690222613>": "iteratorHelpMenu",
                        "<:symbols:882810561786699817>": "symbolKeyHelpEmbed",
                        "<:acknowledgements:882810562055131186>": "acknowledgementsHelpEmbed",
                    }

                    reactionNames = list(reactions.keys())



                    reactedMessage = (reaction.message)

                    if ((reactedMessage.author.id) == (self.user.id)):



                        if ((str(reaction.emoji)) in reactionNames):


                            emojiUser = await client.fetch_user(user.id)

                            embed = self.createEmbed(reactions[str(reaction.emoji)])


                            await reactedMessage.remove_reaction((reaction.emoji), emojiUser)
                            await reactedMessage.edit(content = None, embed = embed, allowed_mentions = (discord.AllowedMentions(everyone = False, users = False, roles = False, replied_user = False)))


                        elif ((str(reaction.emoji)) == "\U0001F9D0"):

                            messageReactions = ((reaction.message).reactions)
                            print(messageReactions)

                            if ((((messageReactions[((len(messageReactions)) - 1)]).emoji) == "\U0001F9D0") and (((messageReactions[((len(messageReactions)) - 2)]).emoji) == "\U0001FA84")):

                                emojiUser = await client.fetch_user(user.id)

                                await (reaction.message).remove_reaction((messageReactions[((len(messageReactions)) - 1)]), emojiUser)
                                await (reaction.message).remove_reaction((messageReactions[((len(messageReactions)) - 2)]), emojiUser)

                                embed = self.createEmbed("undocumentedHelpMenu")

                                await (reaction.message).edit(content = None, embed = embed, allowed_mentions = (discord.AllowedMentions(everyone = False, users = False, roles = False, replied_user = False)))













                    elif ((reactedMessage.author.id) != (self.user.id)):
                        pass








            elif (commandsEnabled == False):
                pass




        elif (reactionsEnabled == False):
            pass





































readSettings()








generateDiscordClasses()


generateEmbeds()






recalculateCommands()



client = MyClient()
client.run(token)



input("Press enter to close")
