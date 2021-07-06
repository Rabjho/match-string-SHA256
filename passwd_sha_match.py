# Matches a breached (and therefore complete) password with a sha256 hash
# profile = 0 takes 1 raw password from each line
# profile = 1 takes passwords encompassed within a character on each side example:"passwd"
# profile = 2 takes passwords encompassed within 2 characters on each side example:""passwd""
# profile = any int and comforms to the same pattern as illustrated above
import argparse
import hashlib

parser = argparse.ArgumentParser(description='Match password with sha256 hash')
parser.add_argument("-f", "--file",required=True,help="Inputfile")
parser.add_argument("-m", "--matchingHash",required=True,help="The sha256-hash that should be matched")
parser.add_argument("-r", "--roundingCharacters",default=0,type=int,required=False,help="Amount of characters around word")
parser.add_argument("-l", "--lineShow",action=argparse.BooleanOptionalAction,default=False,required=False,help="Show entire line including word")
parser.add_argument("-s", "--splitChar",default=',',required=False,help="The character seperating items")
parser.add_argument("-e", "--encoding",required=False,help="Text encoding format")
parser.add_argument("-i", "--item",default=-1,type=int,required=False,help="Item on each line. Negative values are relative to the end")
args = vars(parser.parse_args())
mode = args["roundingCharacters"]
fileName = args["file"]
shaHash = args["matchingHash"]
print("File: "+fileName+" | Hash: "+shaHash+" | Rounding character: "+str(mode)+" | Splitter: '"+args["splitChar"]+"'")



data = open(fileName, "r", encoding=args["encoding"])
array = data.readlines()
lineNum = 0
for line in array:
  lineNum = lineNum + 1
  temp = line.split(args["splitChar"])
  if mode == '0':
    passwd = temp[args["item"]].replace("\n","")
  else:
    passwd = temp[args["item"]][mode:mode*-1-1].replace("\n","")

  sha = hashlib.sha256(passwd.encode())
  passwdhash = sha.hexdigest()
  if str(passwdhash) == shaHash:
    print("Password: "+passwd)
    if args["lineShow"] == True:
      print("Line: #"+ str(lineNum) + " | "+ line)
    break
data.close()
