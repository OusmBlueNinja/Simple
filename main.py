import os, sys,  time
import getopt
import simple

errors = False

global DEBUG
DEBUG = True

start = 0.01 # default start time
end = 0.01

def getArgs(argv):
   global start
   global inputfile
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:t",["ifile="])
   except getopt.GetoptError:
      print('test.py -t <tells you run time> -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -t <tells you run time> -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-t", "--time"):
        start = time.time()
      
   return inputfile

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def error(lineNum, file, error):
  print(f'{b.ENDC}[{b.FAIL}ERROR{b.ENDC}] {error} on line: {lineNum} \n')

class syntax:
  global inputfile
  global errors
  def __init__(self):
    errors = False
    self.terminator = ";"

  def check(self, line, lineNumber):
    if line[(len(line) - 1 )] == ";":
      #print(lineNumber)
      pass
    
    else:
      error(lineNumber, inputfile, "missing ';'")
      errors = True
    
    
    
  
  
syntax = syntax()

def parce(filename):
    with open(filename, 'r') as file:
        data = file.read()
        
    block = []
    blocks = []
    blockNum = 0
    
    for i in range(len(data)):
        if data[i] == ';' :
            block.append(data[i])
            blockNum += 1
            blocks.append(block)
            syntax.check(blocks[(len(blocks)-1)], len(blocks))
            block = []
        elif data[i] == "\n":
            pass
        else:
            block.append(data[i])
    #with open(f'{inputfile}.a.out', 'a') as f:
    #  f.write(str(blocks))
    return blocks

    



def main(file):
    global errors, end
    #print(f'Parceing {file}')
    simple.startFile()
    parcedFile = parce(file)
    if errors:
      #print("error")
      return
    else:
      #print("not")
      pass

    #time.sleep(10)
    #print(f'Running {file} with {len(parcedFile)} lines of code')
    #time.sleep(0.5)
    clear()
    i = 0
    fileLen = len(parcedFile)
    while i <= fileLen:
        try:
          blockLen = len(parcedFile[i])
        except IndexError:
          error((i+1), file, "unexpected end of file")
          return
        #print(f'{parcedFile[i]} {blockLen}')
        #print(parcedFile[i][blockLen-1])
        if not parcedFile[i][blockLen-1]==";":
          error((i+1), file, "missing ; ")
          return
        
        #print("".join(parcedFile[i]))
        OPT = 0
        OPT = simple.interpriter(parcedFile[i], i)
        #print(OPT)
        if OPT == None:
          error(0, None, "unknown operator")
          return 
        
        #print(i)
        #print(type(i), type(fileLen), type(OPT)) 
        #print(OPT)
        if OPT == "valErr":
           error(0, None, "Sytax Error")
           return
        elif OPT == "END":
          return
        elif OPT == "END1": # error return value
          return
        
          
        if OPT != 0:
           
           if int(OPT) <= 0:
              return
           elif int(OPT) >= 0:
             if int(OPT) > fileLen:
               error(i, None, "Out of range")
               if DEBUG:
                 print(f'[{b.FAIL}Out of range{b.ENDC}] Proram tring to jump to invalid line {i}')
               return
             i = (int(OPT)-1)
             
        else:
          i = i + 1
        
            
              
    
    end = time.time()



    
    
if __name__ == '__main__':
    main(getArgs(sys.argv[1:]))
    if start != 0.01:
      delta = time.time() - start
      #delta = delta/1000000000
    
      print(f'finished in [{round(abs(delta), 0)}] seconds')