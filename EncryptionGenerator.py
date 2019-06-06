import random

codes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*']
dictHash = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','0':''}

length = len(codes)

def randomChar(bitLength): #bitLength shows the encryption rate eg. 16bit, 32bit
	encpt  = ""
	for j in range(0,bitLength):
		rvalue = random.randint(0,length-1)
		encpt   = encpt + codes[rvalue]
	return encpt

print(".........Initializing.........")
encryptRate = int(input("Encryption length (eg.8,16) : "))
print("Generating new combinations with" , encryptRate , "length")
for k in dictHash:
	dictHash[k] = randomChar(encryptRate)
	print(k + " : " + dictHash[k])
print("done! new encryption keys are generated successfully.")

# Exporting to file
expStat = input("Export as ini file? (y/n) : ")
if(expStat=='y' or expStat=='Y'):
	#Deleting old data if any
	print("Setting up encryptKey.ini file")
	f = open("encryptKey.ini", "w")
	f.write("")
	f.close()
	#Appending data
	print("Writing data to file...")
	f = open("encryptKey.ini", "a")
	for i in dictHash:
		x = i + ' : ' + dictHash[i] + '\n'
		f.write(x)
	f.close()
	print("done! File successfully written")
