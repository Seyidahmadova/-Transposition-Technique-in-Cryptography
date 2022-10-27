plaintext = 'Pure transposition cipher is easily recognized '
copyplain = plaintext.replace(' ', '').lower()
if (len(copyplain)%6!=0):
    remind = 6-len(copyplain)%6

copyplain+=('x'*remind)

arr =  []
count = 0
newarr = []
for i in range(len(copyplain)):
    newarr.append(copyplain[i]) 
    count+=1
    if(count==6):
        arr.append(newarr)
        count=0
        newarr=[]

for i in range( int (len(arr)/2)):
   temp = []
   temp = arr[i]
   arr[i]=arr[len(arr)-i-1]
   arr[len(arr)-i-1]=temp



for k in range(len(arr)):
    for i in range( int (len(arr[k])/2)):
        temp = []
        temp = arr[k][i]
        arr[k][i]=arr[k][len(arr[k])-i-1]
        arr[k][len(arr[k])-i-1]=temp



for i in range(len(arr)):
    temp=[]
    temp.append(arr[i][2])
    temp.append(arr[i][4])
    temp.append(arr[i][1])
    temp.append(arr[i][5])
    temp.append(arr[i][3])
    temp.append(arr[i][0])
    arr[i]=temp



ciphertext = ''
for k in range(len(arr)):
    for i in range( int (len(arr[k]))):
        ciphertext+=arr[k][i]

print(ciphertext)   



