import os, sys, threading
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


def main(file):
    print(f'running {file}')
    parcedFile = parce(file)
    print(len(parcedFile))
    for i in range(len(parcedFile)):
        #print("".join(parcedFile[i]))
        simple.interpriter(parcedFile[i])
    
    pass



    
    
if __name__ == '__main__':
    main(getArgs(sys.argv[1:]))