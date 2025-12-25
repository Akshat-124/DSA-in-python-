def hashing(n,m):                             #numbers list using dictionary table
    freq={}
    for i in n:
        freq[i]=freq.get(i,0)+1
    for x in m:
        print(freq.get(x,0))
n = list(map(int, input("enter list n: ").split(",")))
m = list(map(int, input("enter list m: ").split(",")))

hashing(n, m)

print("--------------------")

def hashing(s,q):                              #character table without dictionary table
    freq=[0]*26
    for ch in s:
        ascii_val=ord(ch)
        index=ascii_val-97
        freq[index]+=1
    for ch in q:
        ascii_val=ord(ch)
        index=ascii_val-97
        print(freq[index])
s=input("enter string s: ")
q=input("enter query string: ")
hashing(s,q)

print("--------------------")

def hashing(s,q):                     #chartable with dictionary table
    dic={}
    for ch in s :
        dic[ch]=dic.get(ch,0)+1
    for ch in q :
        print(dic.get(ch,0))
s=input("enter string s: ")
q=input("enter query string: ")
hashing(s,q)

     