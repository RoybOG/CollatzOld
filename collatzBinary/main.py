import re
import json
import numpy as np
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
BINARYSTRINGSDIR = "./BINARYSTRINGSDICT.json"

def formatBinNum(n):
   

        

  consecutiveOnesPattern = re.compile(r'1{2,}')
  alternatingOnesPattern = re.compile(r'1(?:01)+')
    

  t =format(n, 'b') #np.base_repr(n,base=4) #
  #print(t)
   #print(re.findall(consecutiveOnesPattern, t))
  coloredT =re.sub(alternatingOnesPattern,f"\033[1;31m\\g<0>\033[39m", t)
  #coloredT =re.sub(consecutiveOnesPattern,f"\033[1;33m\\g<0>\033[39m", t)
 # if n % 2 == 1:  
  #  coloredT =  coloredT + "*"
#coloredT = coloredT.replace("/","\\")
  return coloredT
  #print(coloredT)
# Syntax structure: \033[STYLE;COLORm Your Text \033[0m


def seperateBins(binStr):
    carryCascades = True
    seperatorPatterns = {"00":False, "11":True}
    binParts = []
    binPart = binStr[-1]
    for i in range(len(binStr)-1,0,-1):
        twoBits = binStr[i:i+1]
        if twoBits in seperatorPatterns:
            if seperatorPatterns[twoBits] ^ carryCascades:
                carryCascades = seperatorPatterns[twoBits]



toBitStr = lambda b: format(b, 'b')

def seperateBins(n):
    carryCascades = True
    seperatorPatterns = {0:False, 3:True} # 00, 11
    getLastBits = lambda d=1: n & (2**d - 1)
    
    binParts = [""]
    
    while n >0:
        lastTwoBits = getLastBits(2)
        if lastTwoBits in seperatorPatterns and n >=2: #n is at least 2 bin digits (10=2)
            
            if seperatorPatterns[lastTwoBits] ^ carryCascades:
                binParts = binParts + [f"{lastTwoBits:02b}"]
                carryCascades = seperatorPatterns[lastTwoBits]    
                #binParts.append(""
            else:
                binParts[-1] = f"{lastTwoBits:02b}{binParts[-1]}"

            n = n >> 2
        else:
            binParts[-1] = toBitStr(getLastBits()) + binParts[-1]
            n = n >> 1

    return [s for s in binParts if s][::-1]


    binParts[-1] =  binParts[-1] + format(n & 1, 'b')

def collatzBin(userNum):#, formatFunc):
    n=userNum
    finalText = ""
    binStringsDictGlobal = {}
    with open(BINARYSTRINGSDIR, "r", encoding="utf-8") as file:
        binStringsDictGlobal = json.load(file)   
    binStringsList = []
#printNum(n)

    while n > 1 :
       
        #finalText  = finalText + formatBinNum(n) + "\n"
        if n % 2 == 0:
            n = n // 2 
        else: 
            print(f"{n}: {seperateBins(n)}")
             
            binStringsList.append(format(n, 'b'))
            finalText  = finalText + "\n" #+ formatBinNum(n) + "\n"

            n = n * 3 + 1 
            finalText  = finalText+ "\n"# + formatBinNum(n) + "\n"
        #   printNum(n)
    else:

        #d = {num: i for i,num in enumerate(reversed(binStringsList))}
        #finalText  = finalText 
        finalText = f"{len(binStringsList)} steps \n" + finalText  + "1"
        with open(f"./binaryFiles/binaryText-{userNum}({format(userNum, 'b')}).txt", "w") as f:
            f.write(finalText)
            print(finalText)
        #print(binStringsDictGlobal)

        binStringsDictGlobal.update(zip(binStringsList, range(len(binStringsList) - 1, -1, -1)))
        #binStringsDictGlobal.sort()
        with open(BINARYSTRINGSDIR, "w", encoding="utf-8") as file:
            json.dump(dict(sorted(binStringsDictGlobal.items(), key=lambda x: (x[1],x[0]))),file, indent=4)
        #print(1)


def is_binary(s):
    # מחזיר True רק אם המחרוזת לא ריקה וכוללת רק 0 ו-1
    return set(s).issubset({'0', '1'})


#userNum = int("100101001", 2) 
userNumRaw = input("Enter a number: ") ##27 #
userNum = int(userNumRaw, 0)
#print(userNum)

#collatzBin(27)

collatzBin(userNum)
