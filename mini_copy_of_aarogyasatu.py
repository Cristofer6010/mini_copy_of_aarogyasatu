print ("Hello user")
a = input ("Are you ready to attand corona test : ")
if ("yes" in a):
    print ("So let's start the test")
elif ("no" in a ):
    i = 0
    for i in range(4):
        i = i + 1
        if i == 3:
            break
name = input("Enter your name : ")
input("Enter your age : ")
d = ["Cold","Fever","Diffeculty in breathing","Pain in lungs","Flow of nose","Related to corona sympterms",
['''Type the diseas othewise type no and continue''']]
for item in d:
    print (item)
c = input("Are you suffring from the following diseas : ")
b = ["Are you travel outside the country before 14 days","Are you a Health worker","Are you in Police","etc","yes"]
for items in b:
    print (items)
z = input("Are to relatad to the above work : ")
if (c and z in d or b):
    print ("Stay safe, you have high risk of infection")
else:
    print ('''You have low risk of infection 
    But be alert and stay safe and stay healthy''')
print ('''Thanks to check your corona test''')
print ("Take corona test daily")
print (f"Good buy {name}")
