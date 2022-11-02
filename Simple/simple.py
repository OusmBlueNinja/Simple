# interpriter for the programing language Simple
# by https://github.com/ousmblueninja

commands = ["print", "input", "sleep"]

data = []

def interpriter(raw):
    code = "".join(raw)
    #print("".join(raw))
    if code.startswith(commands[0]):
        #print("printing ")
        code = code.replace(commands[0] + ' "', "")
        code = code.replace('";',"")
        if code.startswith("$"):
            code = code.replace("$", "")
            print(data[code])
            pass
        else:
            for i in range(len(code)):
              if code[i]=="\\" and code[i+1] == "n":
                print("")
              elif code[i]=="n" and code[i-1] == "\\":
                print("")
              else:
                print(code[i], end="")
    elif code.startswith(commands[1]):
        code = code.replace(commands[1] + ' ', "")
        code = code.replace(';',"")
        savedVariable = [code, input("")]
        data.append(savedVariable)
        print(data)
    
        
        
        
        
        
    
    
    