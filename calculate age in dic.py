dec = {1:{'name':'john', 'age':27, 'sex':'male'},
      2: {'name':'marie', 'age':22, 'sex':'female'},
      3: {'name':'sali', 'age':23, 'sex':'female'} }

for i in dec.items():
    if i[1]['age'] > 22:
         print(i[1]['name'])

print("")
print("------------------------------")
order = dict(sorted(dec.items(), key=lambda item: item[1]['age']))

   
for i in order.items():
    if i[1]['age'] >= 22:
         print(i[1]['name'])
    
