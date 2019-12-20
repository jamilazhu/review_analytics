data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data)) 

print("Finish reading the file, Total", len(data) , "of files")

# %余数
sum_len = 0 
for d in data:
    sum_len += len(d) #累计每一笔length
    print(sum_len)
print('The average length is', sum_len/len(data))#每笔留言长度

