ciphertext = 'eidnzxcroyegseisaleprihiotniicpnoasseutprr'

key = [2,4,1,5,3,0]

arr =  []
count = 0
newarr = []
for i in range(len(ciphertext)):
    newarr.append(ciphertext[i]) 
    count+=1
    if(count==6):
        arr.append(newarr)
        count=0
        newarr=[]



def decKey(key):
    for i in range(len(arr)):
        temp = []
        for j in range(0,6):
            ind = key.index(j)
            temp.append(arr[i][ind])
           
        arr[i]=temp

    return arr


decKey(key)

for k in range(len(arr)):
    for i in range( int (len(arr[k])/2)):
        temp = []
        temp = arr[k][i]
        arr[k][i]=arr[k][len(arr[k])-i-1]
        arr[k][len(arr[k])-i-1]=temp



for i in range( int (len(arr)/2)):
   temp = []
   temp = arr[i]
   arr[i]=arr[len(arr)-i-1]
   arr[len(arr)-i-1]=temp



plaintext = ''
for k in range(len(arr)):
    for i in range( int (len(arr[k]))):
        plaintext+=arr[k][i]

print(plaintext)  



