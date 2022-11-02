# interpriter for the programing language Simple
# by https://github.com/ousmblueninja

import time

commands = ["print", "input", "sleep", "//", "goto", "RESET"]

data = []

def interpriter(raw):
    global data
    code = "".join(raw)
    #print("".join(raw))
    if code.startswith(commands[0]):
        #print("printing ")
        code = code.replace(commands[0] + ' "', "")
        code = code.replace('";',"")
        if code.startswith("$"):
            code = code.replace("$", "")
            for i in range(len(data)):
                #print(data[i])
                if data[i][1] == code:
                    
            
                    print(data[i][2], end="")
                    
            return 0
        else:
            for i in range(len(code)):
              if code[i]=="\\" and code[i+1] == "n":
                print("")
              elif code[i]=="n" and code[i-1] == "\\":
                print("")
              else:
                print(code[i], end="")
                
            return 0
    elif code.startswith(commands[1]):
        code = code.replace(commands[1] + ' ', "")
        code = code.replace(';',"")
        savedVariable = [len(data), code, input("")]
        data.append(savedVariable)
        #print(data)
        return 0
    elif code.startswith(commands[2]):
        code = code.replace(commands[2] + '(', "")
        code = code.replace(');',"")
        time.sleep(int(code))
        return 0
    
    elif code.startswith(commands[3]):
        return 0
    elif code.startswith(commands[4]):
        code = code.replace(commands[4] + ' ', "")
        code = code.replace(';',"")
        return code
    elif code.startswith(commands[5]):
        data = []
        return 0
    
        
        
        
        
        
    
    
    