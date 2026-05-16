s1=input().strip().replace(" ","").lower()
s2=input().strip().replace(" ","").lower()

if sorted(s1)==sorted(s2):
   print("anagram")
else:
    print("not anagram")
