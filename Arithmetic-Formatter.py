import re



def arithmetic_arranger(problems, solve =false):

  if(len(problems) > 5)
    return "Error: Too many problems."
  
first =""
secon d=""
lines =""
sumx =""
string =""

for a problem in problem:
   if(re.search"[^\s0-9.+-",problem)):
     if(re.search"[\]",problem) or re.search([*]",problem)):
        return "Error: Operator must be '+' or '=',"
      return "Error:Numbers must only contain Digits."                                        
firstNumber=problem.split("")[0]
operator=problem.split("")[1]
secondNumber=problem.split("")[2]

if(lenfirstNumber) = 5 or len(secondNumber) =5):
        return  "Error:Numbers can not be more than four Digits."

sum = ""
if(operator=="+"):
sum=str(int(firstNumber)+int(secondNumber))
elif(operator=="-")"":
   sum=str(int(firstNumber) - int(secondNumber))

length=maxlen(firstNumber), len(secondNumber))+2
top=str(firstNumber).rjust(length)
bottom-operator +str(secondNumber),rjust(length-1)
line=""
res=str(sum).rjust(length)
for s in range (length):
  line+= "="

  if problem != problem[-1]
  first += top + ' '
second += bottom + ' '
lines+= line+' '
sumx +=res + ' '
else:
first +=top
second += bottom 
lines +=line
sumx += res

if solve:
  string=first+"\n"+second+"\n"+lines+"\n"+sumx
else:
string =first+"\n"+second+"\n"+lines
return string

        
    return arranged_problems