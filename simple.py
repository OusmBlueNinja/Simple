# interpriter for the programing language " Simple "
# by https://github.com/ousmblueninja
import os, random


LOGFILE = f"./logs/log_{random.randrange(11111,99999)}.log"
print(LOGFILE)

try:
  os.mkdir("./logs")
except FileExistsError as e:
  pass

class b:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\u001b[31m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  WHITE = '\u001b[37m'


def error(lineNum, error):
  print(f'{b.ENDC}[{b.FAIL}ERROR{b.ENDC}] {error} on line: {lineNum} \n')
  with open(LOGFILE, "a") as f:

    DebugData = f"[ERROR] {error} on line: {lineNum}"
    f.write(str(DebugData))
    f.write("\n")


import time

commands = [
  "print", "input", "sleep", "//", "goto", "RESET", "END", "var", "ALOC", "if",
  "PSTK", "DEF", "DEFEND", "RUNDEF", "CLR", "IF"
]

# OLD \/
# [pointer, name, data]
# NEW \/
# [name, data]
data = []

defRun = False
callLn = 0

# [function name, line number]
functions = []

inFunc = False

DEBUG = True


def startFile():
  with open('debug.log', 'w') as f:
    f.write("LineNum  Operator  |  Variables  |  Functions")
    f.write("\n")


def debugger(ln, operator):
  global inFunc, callLn, data, functions, DEBUG, defRun
  with open(LOGFILE, "a") as f:
    spaces = (12 - len(operator))

    DebugData = f"{ln}        {operator}{' '*spaces}|   {data}   |      {functions}"
    f.write(str(DebugData))
    f.write("\n")


def saveToVar(indata, varname):
  global data
  savedVariable = [len(data), varname, indata]

  for i in range(len(data)):
    #print(data[i])
    try:
      if data[i][1] == varname:
        pos = data[i][0]
        data.pop(i)
        savedVariable = [pos, varname, indata]
    except IndexError:
      pass

  data.append(savedVariable)


def interpriter(raw, lineNum):
  ###############################
  #         DEFEND;             #
  ###############################

  # Moved To Top

  global data, inFunc, functions, callLn, defRun, DEBUG
  #print(inFunc)
  # if DEBUG:
  #   saveDebufData(data)
  # print(data, lineNum)
  global commands
  #print(data)
  code = "".join(raw)
  operator = "".join(raw).split(" ")[0].split(";")[0]
  debugger(lineNum, operator)

  if code.startswith(commands[6]):
    code = code.replace(commands[6] + '', "")
    code = code.replace(';', "")
    #print(code)
    if inFunc == False and defRun:
      with open(LOGFILE, "a") as f:

        f.write(str("EOF Program over."))
        f.write("\n")
      return "END"
  elif code.startswith(commands[12]):
    code = code.replace(commands[12], "")
    code = code.replace(';', "")
    inFunc = False
    if defRun == True:
      return callLn
    else:
      return 0

  if inFunc is True:
    return 0

  #print(data)
  #print("".join(raw))
  if code.startswith(commands[0]):
    #print("printing ")
    code = code.replace(commands[0] + ' "', "")
    code = code.replace('";', "")
    if code.startswith("$"):
      code = code.replace("$", "")
      for i in range(len(data)):
        #print(data[i])
        if data[i][1] == code:

          print(data[i][2], end="")

          return 0
      error((lineNum + 1), "Undifined Variable")
      return "END1"

    else:
      for i in range(len(code)):
        if code[i] == "\\" and code[i + 1] == "n":
          print("")
        elif code[i] == "n" and code[i - 1] == "\\":
          print("")
        else:
          print(code[i], end="")

      return 0
  elif code.startswith(commands[1]):
    code = code.replace(commands[1] + ' ', "")
    code = code.replace(';', "")
    with open(LOGFILE, "a") as f:
      f.write(str("(INPUT: taking User Input \n"))
    inData = input("")
    with open(LOGFILE, "a") as f:
      f.write(
        str(
          f'(DEBUG: User input saved as [ {code} ] with data [ {inData} ] \n'))
    savedVariable = [len(data), code, inData]

    for i in range(len(data)):
      #print(data[i])
      try:
        if data[i][1] == code:
          pos = data[i][0]
          data.pop(i)
          savedVariable = [pos, code, inData]
      except IndexError:
        pass

    data.append(savedVariable)

    #print(data)

    return 0
  elif code.startswith(commands[2]):
    code = code.replace(commands[2] + '(', "")
    code = code.replace(');', "")
    #print(code)
    try:
      time.sleep(int(code))
      return 0
    except ValueError:
      return "valErr"

  elif code.startswith(commands[3]):
    return 0
  elif code.startswith(commands[4]):
    code = code.replace(commands[4] + ' ', "")
    code = code.replace(';', "")
    return code
  elif code.startswith(commands[5]):
    data = []
    return 0

  elif code.startswith(commands[7]):
    code = code.replace(commands[7] + ' ', "")
    code = code.replace(';', "")
    #print(code)
    raw = code.split("=")
    #print(raw)
    raw[1] = raw[1].replace('"', "")
    #print(raw)
    if raw[1].startswith('$'):
      #print(raw[1])
      raw[1] = raw[1].replace('$', "")
      #print(raw)
      valid = False
      for i in range(len(data)):
        if data[i][1] == raw[1]:
          raw[1] = data[i][2]
          #print(raw)
          valid = True
          break
        else:
          valid = False
      if not valid:
        error((lineNum + 1), "undeclaired variable")

      pass

    #print("\n\n", code, data, raw)
    inData = raw[1]
    savedVariable = [len(data), raw[0], inData]

    # checks if dta variable exists \/ \/ \/

    for i in range(len(data)):
      #print(data[i])
      try:
        if data[i][1] == raw[0]:
          data.pop(i)
      except IndexError:
        pass

    # ____________________________________________ end

    data.append(savedVariable)

    #print(data)

    return 0
  elif code.startswith(commands[8]):
    code = code.replace(commands[8] + ' ', "")
    code = code.replace(';', "")
    #print("\n", code)
    for i in range(len(data)):
      #print(data[i])
      try:
        if data[i][1] == code:
          data.pop(i)
          return 0
      except IndexError:
        pass
    return 0
  elif code.startswith(commands[9]):
    code = code.replace(commands[9] + ' (', "")
    code = code.replace(';', "")
    #print("\n", code)
    raw = code.split("==")
    raw.append("")
    #print(raw)
    rawTwo = raw[1].split(')')
    rawTwo[0] = rawTwo[0].replace('"', "")
    #print(rawTwo)
    #print(raw, rawTwo, len(rawTwo))
    for i in range(2):
      raw[(i + 1)] = rawTwo[i - 1]

    cash = raw[1]
    raw[1] = raw[2]
    raw[2] = cash
    del cash
    #raw[1] = raw[1].replace("")
    #print(raw)
    if raw[0].startswith("$"):
      raw[0] = raw[0].replace("$", "")
      for i in range(len(data)):

        #print(data[i])
        if data[i][1] == raw[0]:
          #print(data[i][2])
          raw[0] = data[i][2]
    if raw[1].startswith("$"):
      raw[1] = raw[1].replace("$", "")
      for i in range(len(data)):

        #print(data[i])
        if data[i][1] == raw[1]:
          #print(data[i][2])
          raw[1] = data[i][2]
    raw[2] = raw[2].replace("{", "")
    raw[2] = raw[2].replace("}", "")

    #print(raw)

    if raw[2][0] == "*":
      FuncName = raw[2].strip("*")
      FuncLine = 0

      for x, y in functions:
        if x == FuncName:
          FuncLine = y

      raw[2] = FuncLine

      #print(raw, lineNum)

      for i in range(len(functions)):
        if functions[i][0] == FuncName:
          callLn = (lineNum + 1)
          defRun = True
          inFunc = False
          #print(callLn)
        #print(f"goin to ln {functions[i][1]}")
        #print(functions[i][1])
    else:
      FuncLine = raw[2]

    #print(code, raw, "\n")

    if raw[0] == raw[1]:

      #print(raw)
      return (int(FuncLine))
    else:
      return 0

    #for i in range(len(data)):
    #        #print(data[i])
    #        try:
    #          if data[i][1] == code:
    #            pass
    #        except IndexError:
    #          pass

    return 0

  elif code.startswith(commands[10]):
    code = code.replace(commands[10] + ' (', "")
    code = code.replace(';', "")
    print(data)
    return 0

  elif code.startswith(commands[14]):
    # clear terminal
    os.system("clear")

    return 0
    ###############################
    #         DEF;                #
    ###############################
  elif code.startswith(commands[11]):
    code = code.replace(commands[11] + " ", "")
    code = code.replace(';', "")
    #print(code)
    NewFunc = [code, (lineNum + 2)]
    for i in range(len(functions)):
      if functions[i][0] == code:
        error((lineNum + 1), "Function already exists")
        return "END1"
    functions.append(NewFunc)
    #print(functions)
    inFunc = True

    return 0

    ###############################
    #         RUNDEF;             #
    ###############################
  elif code.startswith(commands[13]):
    code = code.replace(commands[13] + " ", "")
    code = code.replace(';', "")
    #print(code)
    if defRun == True:
      defRun = False
      return 0
    for i in range(len(functions)):
      if functions[i][0] == code:
        callLn = (lineNum + 1)
        defRun = True
        inFunc = False
        #print(f"goin to ln {functions[i][1]}")
        return functions[i][1]

    return "valErr"
