#!/usr/bin/env python3
import CCCFunctions
from PyNetTools import PyNetTools
from PyPrintSystem import PyPrintSystem
from getpass import getuser as user
from pygments import highlight, lexers, formatters
from json import dumps as JSON

def doHelp(verbose):
	PyPrintSystem.p("Displaying help dialog", 'v', verbose)
	PyPrintSystem.p("devices\t\t\tShows the scanned devices", 'i')
	PyPrintSystem.p("forget <\033[93;1mChromeCastIP\033[0m>\tShows a menu to forget certain WiFi networks for the specified <\033[93;1mChromeCastIP\033[0m>", 'i')
	PyPrintSystem.p("help\t\t\tDisplays the current dialog", 'i')
	PyPrintSystem.p("id <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates certificate data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("info <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates general data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("locale <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates locale data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("lan <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates saved network data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("reboot <\033[93;1mChromeCastIP\033[0m>/all\tReboots the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("reset <\033[93;1mChromeCastIP\033[0m>/all\tResets the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("scan\t\t\tScans for ChromeCast devices", 'i')
	PyPrintSystem.p("timezone <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates timezone data from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'i')
	PyPrintSystem.p("quit\t\t\tExits ChromeCastControl", 'i')
	PyPrintSystem.p("verbose\t\t\tShows cools messages like this! Currently: '\033[93;1m" + str(verbose) + "\033[90;2m'", 'v', True)
	PyPrintSystem.p("wifi <\033[93;1mChromeCastIP\033[0m>/all\tEnumerates all WiFi netoworks from the specified <\033[93;1mChromeCastIP\033[0m>, or all ChromeCasts scanned", 'p')

def multiDeviceHandler(CCDevices, command, arguments, type, verbose):

	if len(arguments) == 0:
		PyPrintSystem.p("Need to specify the IP (argument 1), like so: '\033[93;1m" + command + " " + PyNetTools.getPrivateIP() + "\033[0m'", 'e')
	else:
		if arguments[0] == "all":
			PyPrintSystem.p("All scanned targets selected", 'v', verbose)
			if len(CCDevices) == 0:
				PyPrintSystem.p("There are no devices found, please use '\033[93;1mscan\033[0m' first!", 'e')
			else:
				PyPrintSystem.p("Action: " + type, 'v', verbose)
				for IP in [i[0] for i in CCDevices]:
					PyPrintSystem.p(IP + ":", 'i')
					if type == "id":
						for i in highlight(JSON(CCCFunctions.CCID(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							PyPrintSystem.p(i, 's')
						print()
					elif type == "info":
						for i in highlight(JSON(CCCFunctions.CCInfo(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							PyPrintSystem.p(i, 's')
						print()
					elif type == "lan":
						for i in highlight(JSON(CCCFunctions.CCSavedNetworks(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							PyPrintSystem.p(i, 's')
						print()
					elif type == "locale":
						for i in highlight(JSON(CCCFunctions.CCLocales(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							PyPrintSystem.p(i, 's')
						print()
					elif type == "reboot":
						PyPrintSystem.p("Rebooting...", 'v', verbose)
						CCCFunctions.CCReboot(arguments[0])
					elif type == "reset":
						PyPrintSystem.p("Resetting...", 'v', verbose)
						CCCFunctions.CCFactoryReset(arguments[0])
					elif type == "timezone":
						for i in highlight(JSON(CCCFunctions.CCTimeZones(IP), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							PyPrintSystem.p(i, 's')
						print()
					elif type == "wifi":
						for i in highlight(JSON(CCCFunctions.CCScanNetworks(IP, 15), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
							PyPrintSystem.p(i, 's')
						print()
		else:
			PyPrintSystem.p("Verifying target: " + arguments[0], 'v', verbose)
			if CCCFunctions.CCVerify(arguments[0]):
				PyPrintSystem.p("Target verified", 'v', verbose)
				if type == "id":
					for i in highlight(JSON(CCCFunctions.CCID(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						PyPrintSystem.p(i, 's')
				elif type == "info":
					for i in highlight(JSON(CCCFunctions.CCInfo(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						PyPrintSystem.p(i, 's')
				elif type == "lan":
					for i in highlight(JSON(CCCFunctions.CCSavedNetworks(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						PyPrintSystem.p(i, 's')
				elif type == "locale":
					for i in highlight(JSON(CCCFunctions.CCLocales(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						PyPrintSystem.p(i, 's')
				elif type == "reboot":
					PyPrintSystem.p("Rebooting: " + arguments[0], 'v', verbose)
					CCCFunctions.CCReboot(arguments[0])
				elif type == "reset":
					PyPrintSystem.p("Resetting: " + arguments[0], 'v', verbose)
					CCCFunctions.CCFactoryReset(arguments[0])
				elif type == "timezone":
					for i in highlight(JSON(CCCFunctions.CCTimeZones(arguments[0]), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						PyPrintSystem.p(i, 's')
				elif type == "wifi":
					for i in highlight(JSON(CCCFunctions.CCScanNetworks(arguments[0], 15), indent=2, sort_keys=True), lexers.JsonLexer(), formatters.TerminalFormatter()).splitlines():
						PyPrintSystem.p(i, 's')
			else:
				PyPrintSystem.p(arguments[0] + " is not a valid ChromeCast device", 'e')

def quitCCC(verbose, exitCode = 0):
	PyPrintSystem.p("Exitting CCC", 'v', verbose)
	PyPrintSystem.doHeart("Thank you for using ChromeCastControl!", 2)
	PyPrintSystem.p("Exit code: " + str(exitCode), 'v', verbose)
	exit(exitCode)

def toggleVerbose(verbose):
	PyPrintSystem.p("Verbose toggled", 'v', verbose)
	return not verbose

verbose = False
commands = [
	["devices", "cc", "chromecasts", "hosts"],
	["forget", "delete", "remove", "del"],
	["help", "h", "?"],
	["id", "identity", "identifier"],
	["info", "enum", "enumerate", "recon", "reconnaissance"],
	["lan", "savednetwork", "savednetworks", "localnetwork", "localnetworks"],
	["locale", "locales", "langs", "languages"],
	["quit", "q", "exit", "bye"],
	["reboot", "restart", "power"],
	["reset", "factory", "facreset", "format"],
	["scan", "map", "detect"],
	["timezone", "timezones", "tz", "time"],
	["verbose", "v"],
	["wifi", "enumwifi", "scanwifi", "wifiscan", "wifienum"]
]
CCDevices = []
selectedMenuItem = -1

PyPrintSystem.doHeart("Welcome, " + user() + ", to ChromeCastControl!")
PyPrintSystem.p("Try '\033[93;1mhelp\033[0m' for a list of commands", 'i')

while True:
	try:
		userInput = PyPrintSystem.i("CCC> ", 'i')
	except KeyboardInterrupt:
		PyPrintSystem.p("KeyboardInterupt detected, closing CCC", 'v', verbose)
		quitCCC(verbose, 1)
	print()

	if userInput[:1] == "/":
		PyPrintSystem.p("Easter egg?", 'v', verbose)
		PyPrintSystem.p("Hey, this isn't Minecraft!", 'w')
		print()
		userInput = userInput[1:]

	command = userInput.split()[0]
	arguments = userInput.split()[1:]

	if any(command in i for i in commands):
		if command in [i for i in commands if i[0] == "devices"][0]:
			if len(CCDevices) == 0:
				PyPrintSystem.p("There are no devices found, please use '\033[93;1mscan\033[0m' first!", 'e')
			elif len(CCDevices) == 1:
				PyPrintSystem.p("There was one device found:", 'w')
				PyPrintSystem.p(CCDevices[0][1]["name"] + " (" + CCDevices[0][0] + ")", 's')
			else:
				PyPrintSystem.p("There were '\033[93;1m" + str(len(CCDevices)) + "\033[0m' devices found:", 's')
				for i in CCDevices:
					PyPrintSystem.p(i[1]["name"] + " (" + i[0] + ")", 's')

		elif command in [i for i in commands if i[0] == "forget"][0]:
			PyPrintSystem.p("Verifying target: " + arguments[0], 'v', verbose)
			if CCCFunctions.CCVerify(arguments[0]):
				PyPrintSystem.p("Target verified", 'v', verbose)
				savedNetworkArray = CCCFunctions.CCSavedNetworks(arguments[0])

				for i in savedNetworkArray:
					PyPrintSystem.p("[" + str(savedNetworkArray.index(i)) + "] " + i["ssid"] + " (" + str(i["wpa_id"]) + ")")

				while selectedMenuItem not in range(0, len(savedNetworkArray)):
					PyPrintSystem.p("Not a valid selection: " + str(selectedMenuItem), 'v', verbose)
					selectedMenuItem = int(PyPrintSystem.i("CCC>Forget> ", 'i'))

				PyPrintSystem.p("Forgetting WiFi network: " + savedNetworkArray[selectedMenuItem]["ssid"], 'v', verbose)
				CCCFunctions.CCForgetWiFi(arguments[0], str(savedNetworkArray[selectedMenuItem]["wpa_id"]))
			else:
				PyPrintSystem.p(arguments[0] + " is not a valid ChromeCast device", 'e')

		elif command in [i for i in commands if i[0] == "help"][0]:
			doHelp(verbose)

		elif command in [i for i in commands if i[0] == "id"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "id", verbose)

		elif command in [i for i in commands if i[0] == "info"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "info", verbose)

		elif command in [i for i in commands if i[0] == "lan"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "lan", verbose)

		elif command in [i for i in commands if i[0] == "locale"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "locale", verbose)

		elif command in [i for i in commands if i[0] == "quit"][0]:
			quitCCC(verbose)

		elif command in [i for i in commands if i[0] == "reboot"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "reboot", verbose)

		elif command in [i for i in commands if i[0] == "reset"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "reset", verbose)

		elif command in [i for i in commands if i[0] == "scan"][0]:
			PyPrintSystem.p("Clearing device list", 'v', verbose)
			CCDevices = []
			for i in PyNetTools.portScan(PyNetTools.getPrivateIP(), 8008):
				PyPrintSystem.p("Verifying: " + i, 'v', verbose)
				if CCCFunctions.CCVerify(i):
					PyPrintSystem.p("Verified: " + i, 'v', verbose)
					PyPrintSystem.p("Device found: " + i + " (" + CCCFunctions.CCInfo(i)["name"] + ")", 's')
					CCDevices.append([i, CCCFunctions.CCInfo(i)])
				else:
					PyPrintSystem.p(i + " is not a valid ChromeCast device (port: '\033[93;1m8008\033[0m' open!)", 'w')

		elif command in [i for i in commands if i[0] == "timezone"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "timezone", verbose)

		elif command in [i for i in commands if i[0] == "verbose"][0]:
			PyPrintSystem.p("Toggling verbose (" + str(verbose) + " -> " + str(toggleVerbose(verbose)) + ")", 'i')
			verbose = toggleVerbose(verbose)

		elif command in [i for i in commands if i[0] == "wifi"][0]:
			PyPrintSystem.p("Launching mutliDeviceHandler for command: " + command, 'v', verbose)
			multiDeviceHandler(CCDevices, command, arguments, "wifi", verbose)

		else:
			PyPrintSystem("An unknown error has occured!", "e")

	else:
		PyPrintSystem.p("Unknown command. Try '\033[93;1mhelp\033[0m' for a list of commands", 'e')
