x=len(s)
count=0
for i in range (x):
  if(s[i]=='a'):
    count+=1
  elif(s[i]=='e'):
    count+=1
  elif(s[i]=='i'):
    count+=1
  elif(s[i]=='o'):
    count+=1
  elif(s[i]=='u'):
    count+=1

print("number of vowels:", count)
