from string import punctuation
import matplotlib.pyplot as plt
import math

text = open('text.txt')

def count(text):
	dic = dict()
	for line in text:
		word = line.split()
		for item in word:
			item = item.strip(punctuation)
			word_lowercase = item.lower()
			if word_lowercase in dic:
				dic[word_lowercase] += 1
			else:
				dic[word_lowercase] = 1
	return sorted(dic.items(),key=lambda items:items[1],reverse=True)


def draw_zipf(text):
	dic1 = dict(count(text))
	lst_x = []
	lst_y = []
	for rank,fre in enumerate(dic1,1):
		if dic1[fre] > 100:
			x = math.log10(dic1[fre])
			lst_x.append(x)
			y = math.log10(rank)
			lst_y.append(y)
	plt.plot(lst_x,lst_y)
	plt.xlabel('log f')
	plt.ylabel('log x')
	plt.show()

draw_zipf(text)
