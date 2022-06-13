from datetime import datetime
from CuModules import ls
from CuModules.consCMDs import Commands
instance = Commands()

programList = ["ls", "calc"]
progLogList = ["started system", # 0
							"ran 'ls'.", # 1, ls
							"ran 'calc'.", "left 'calc'.", # 2 & 3, calc
							"ran '3'.", "left '3'.", # 4 & 5,
							"ran '4'.", "left '4'."] # 6 & 7,

class ts:
	# fully self contained timestamp function
	# (ok maybe not quite)
	def timestamp(programRegister):
		dateTimeObj = datetime.now()
		global dateTimeStr
		dateTimeStr = str(dateTimeObj)
		f = open("logs.txt", "a")
		actAppend = progLogList[programRegister]
		logAct = "["+dateTimeStr+"] user "+actAppend+"\n"
		f.write(logAct)
		f.close()

class prop: # (pr)ogram (op)ener
	def prStr(prName): # all tools
		print("ye")
		if progSelStr == "calc":
				ts.timestamp(2)
				print("calculator")
				ts.timestamp(3)
			
	def prSel(progSelInt): # (prog)ram (sel)ect
		if progSelStr not in programList:
			print("you stupid")
		else:
			pass
		if progSelStr == "cl":
			instance.ClearConsole()
		elif progSelStr == "ls":
			ts.timestamp(1)
			ls.list()
		else:
			prop.prStr(progSelStr)

cont = True
while cont == True:
	progSelStr = input("> ")
	prop.prSel(progSelStr)
