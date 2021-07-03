'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

'''

def closeStrings(self, word1: str, word2: str) -> bool:
	d1={}
	d2={}
	if len(word1) != len(word2):
		return False
	else:
		for i in word1:
			if i not in d1:
				d1[i]=1
			else:
				d1[i]+=1
		print(d1)
		for i in word2:
			if i not in d2:
				d2[i]=1
			else:
				d2[i]+=1
		if d1.keys()==d2.keys():
			return sorted(list(d1.values()))==sorted(list(d2.values()))
	