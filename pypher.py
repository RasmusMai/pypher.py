import re
class Caesar:
	def decrypt(encrypted_string,key):
		encrypted_array = list(encrypted_string)
		decrypted_array = []
		try:
			if key < 0:
				key = 26 + key
			for i in encrypted_array:
				if re.search("^[A-Z]+$", i): #65 - 90, case preserving
					if ord(i) - key < 65:
						n = 91 - (65 - (ord(i) - key))#Safe switch on underflow
						decrypted_array.append(chr(n))
					else:
						decrypted_array.append(chr(ord(i) - key))
				elif re.search("^[a-z]+$", i): #97 - 122
					if ord(i) - key < 97:
						n = 123 - (97 - (ord(i) - key))
						decrypted_array.append(chr(n))
					else:
						decrypted_array.append(chr(ord(i) - key)) 
				else:
					decrypted_array.append(i) #In case it's not a letter, just pass it on
			return (''.join(decrypted_array))
		except:
			return ("Sorry, no key")
		
	def checkdictionary(word):
		try:
			dictionary = open('/usr/share/dict/american-english','r')
		except:
			print ("Currently only supports some Linux distros with american-english dictionary.")
		for line in dictionary:
			if word.lower() == line[:-1].lower():
				dictionary.close()
				return True
		dictionary.close()
		return False

	def crackkey(encrypted_string):
		print('Hacking SkyNet')
		encrypted_words = encrypted_string.split(' ')
		dictionary = open('/usr/share/dict/american-english','r')
		for i in encrypted_words:
			print ("Testing word: {}".format(i))
			encrypted_word_array = list(encrypted_words)
			for x in range(1, 26):
				word = Caesar.decrypt(i, x)
				print ("Trying key: {}, Decrypted: {}".format(x, word))
				if Caesar.checkdictionary(word):
					print ("Found key: {}".format(x))
					return (x)

	def main():
		encrypted_string = input("Your string ==> ")
		try:
			key = int(input("Key (leave blank if unknown) ==> "))
		except:
			key = Caesar.crackkey(encrypted_string)
		print (Caesar.decrypt(encrypted_string, key))

class Atbash:
	def decrypt(string):
		encrypted_array = list(string)
		decrypted_array = []
		try:
			for i in encrypted_array:
				if re.search("^[A-Z]+$", i): #65 - 90, case preserving
					n = 90-(ord(i) - 65)
					decrypted_array.append(chr(n))
				elif re.search("^[a-z]+$", i): #97 - 122
					n = 122-(ord(i) - 97)
					decrypted_array.append(chr(n))
				else:
					decrypted_array.append(i)
			return (''.join(decrypted_array))
		except:
			return ("Couldn't do it, yo")
	def main():
		string = input("Your string ==> ")
		print (Atbash.decrypt(string))

class Vigenere:
	def encrypt(string, key):
		stringarray = list(string)
		keyarray = list(key)
		print (string,key)
		nonalphacount = 0
		encrypted_array = []
		for c, i in enumerate(stringarray):
			if re.search("^[a-z]+$", i): #97 - 122
				currentkey = 123 - ord(keyarray[(c - nonalphacount) % len(keyarray)]) #its fine
				n = ord(i) - currentkey
				if n < 97:
					n = 123 - (97 - n)
				encrypted_array.append(chr(n))
			else:
				nonalphacount += 1
				encrypted_array.append(i)
		return (''.join(encrypted_array))
	def decrypt(string, key): 
		pass #TODO

	def main():
		while True:
			print ('''Vigenere Cipher
1* Encrypt
2* Decrypt
0* Quit''')
			menu = int(input("==> "))
			string = input("Your string ==> ").lower()
			key = input("Your key ==> ").lower()
			if menu == 0:
				break
			elif menu == 1:
				print(Vigenere.encrypt(string, key))
				break
			elif menu == 2:
				print(Vigenere.decrypt(string, key))
				break
			else:
				print ("Select an existing entry")
def main ():
	while True:
		print ('''Choose cipher method
1* Caesar
2* Atbash
3* Vigenere
0* Quit''')
		menu = int(input("==> "))
		if menu == 0:
			break
		elif menu == 1:
			Caesar.main()
			break
		elif menu == 2:
			Atbash.main()
			break
		elif menu == 3:
			Vigenere.main()
			break
		else:
			print ("Select an existing entry")
if __name__ == "__main__":
	main()