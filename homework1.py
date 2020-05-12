from string import punctuation


text = open('text.txt')
word = open('words.txt')

text_lst = []
word_lst = []

for line in text:
	word1 = line.split()
	for i in word1:
		i = i.strip(punctuation)
		word_low = i.lower()
		text_lst.append(word_low)
		
new_text = set(text_lst)

for k in word:
	k = k.strip()
	word_lst.append(k)

new_word = set(word_lst)

count = 0
lst = []
for item in new_text:
	if item not in new_word:
		count += 1
		lst.append(item)

count_num = 0
for x in new_text:
	try:
		if type(int(x)) == int or type(float(x)) == float:
			count_num += 1
	except:
		pass

print('There are {} words not in the word list.\nThere are {} numbers in the text.'.format(count,count_num))
