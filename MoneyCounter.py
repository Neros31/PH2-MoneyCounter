from pathlib import Path
import re
import sys

file_path = sys.argv[1]
map = Path(file_path).read_text()
allmoney = 0

Stealables = {
"Secret Files" : 3000,
"Extra VIP Spawn" : 10000,
"Cash Stack" : 5000,
"Cash Pile" : 5000,
"Gold Bar" : 8000,
"Jewelry" : 2000,
"Cash Notes" : 1000,
"Jewelry Case" : 6000,

"ATM" : 5000,
"Wall ATM" : 5000,
"Arcade Machine" : 3000,
"Cash Register" : 5000
}
for Item in Stealables:
   amount = map.count(Item+"@")
   print(f"\t+ {Item} ({Stealables[Item]}$) x {amount} = {amount * Stealables[Item]}$ ")
   allmoney += amount * Stealables[Item]
 
 
 #regex shit lol
Customs = re.findall( "Custom Stealable.*",map)
for Object in Customs:
   name = re.findall( r"(?<=Name=)\w+",Object)
   if (name == []) :
      name = ["Unnamed Custom Object"]
   value = re.findall( r"(?<=Value=)\d+",Object)
   if (value == []) :
      value = [0]
   print("\t+" ,name[0], value[0] , "$")
   allmoney += int(value[0])


print("------------------------------------------------------------------------------------------")
print(" Total =",allmoney,"$")
input()
quit()