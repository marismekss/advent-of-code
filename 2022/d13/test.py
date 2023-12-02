import re

p1 = '[[1],[2,3,4]]'



tmp1 = list(re.search('\[(.*?)\]',p1)[1].split(','))
print(tmp1)
#tmp2 = list(re.search('\[(.*?)\]',p2)[1].split(','))

#tmp1 = list(map(int,tmp1))
#tmp2 = list(map(int,tmp2))




#for i,j in zip(tmp1,tmp2):
    #print(f"{i}   {j}")

#['[1,1,3,1,1]', '[1,1,5,1,1]']