import os, sys, threading, time
import getopt
import simple

def getArgs(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      
   return inputfile

def parce(filename):
    with open(filename, 'r') as file:
        data = file.read()
        
    block = []
    blocks = []
    blockNum = 0
    
    for i in range(len(data)):
        if data[i] == ';':
            block.append(data[i])
            blockNum += 1
            blocks.append(block)
            block = []
        elif data[i] == "\n":
            pass
        else:
            block.append(data[i])
    return blocks

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main(file):
    print(f'Parceing {file}')
    parcedFile = parce(file)
    print(f'Running {file} with {len(parcedFile)} lines of code')
    time.sleep(0.5)
    clear()
    i = 0
    fileLen = len(parcedFile)
    while i <= fileLen:
        
        #print("".join(parcedFile[i]))
        OPT = simple.interpriter(parcedFile[i])
        #print(i)
        #print(type(i), type(fileLen), type(OPT)) 
        if OPT != 0:
            i = int(OPT)
        else:
            i = i + 1   
            
              
    
    pass



    
    
if __name__ == '__main__':
    main(getArgs(sys.argv[1:]))