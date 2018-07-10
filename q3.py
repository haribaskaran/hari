l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
	print("%s is a constant"% l)
else:
	print("%s invalid" % l)
