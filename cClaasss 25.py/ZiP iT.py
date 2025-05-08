n1 = [1,2,3,4]
n2 = [3,5,6,8]
nzip = list(zip(n1,n2))
print(nzip)
rzip = list(zip(n1,n2[::-1]))
print(rzip)
stocks = ["Reliance","infoys","tcs"]
price = [12345,3508,1245]
dic1 = { st:p  for  st,p  in  zip (stocks , price)}
print(dic1)