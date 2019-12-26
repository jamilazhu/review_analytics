data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data)) 

print("Finish reading the file, Total", len(data) , "of files")

print(data[0])

# 文字计数
wc = {} #word_count的代表
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1 
        else:
            wc[word] = 1 #新增key进wc字典
for word in wc:
    if wc[word] >100:
        print(word, wc[word])

while True:
    word = input('You want to search the word:')
    if word == 'q':
        break
    if word in wc:  
        print(word, 'has apperaed', wc[word])
    else:
        print('This words has not appeared in the comment.')

print('Thanks for using this searching function')

