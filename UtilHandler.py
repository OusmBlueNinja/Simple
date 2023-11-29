import json, time, os, sys


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


class file:
  def read(self,filename):
    try:
      with open(filename, 'r') as f:
        return f.read()
    except Exception as e:
      return e
  def write(self,filename, data):
    try:
      with open(filename, 'w') as f:
        f.write(data)
    except Exception as e:
      return e
  def append(self,filename, data):
    with open(filename, 'a') as f:
      f.write(data)
  def remove(self,filename):
    try:
      os.remove(filename)
    except Exception as e:
      return e

file = file()




def FileHandle(code):
    opt = code.split('file.')[1]
    #print(opt)
    if opt.startswith('read'):
      filename = opt.split('"')
      saveVar = filename[2].replace('as', '')
      saveVar = saveVar.replace(' ', '')
      saveVar = saveVar.replace(';', '')
      #print(filename, saveVar, filename[1])
      try:
        data = file.read(filename[1])
        #print(file.read(filename[1]))
      except:
        return 0
      #print(saveVar)
      return data, saveVar
    return 0


def exicute(code, lineNum):
  
  if code.startswith('file.'):
    return FileHandle(code)
  else:
    error((lineNum+1), "Unknown Operator")
    exit()
    