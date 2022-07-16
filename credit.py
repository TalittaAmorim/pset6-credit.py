
cartao = input("Cartão: ")
copy_cartao = cartao[::-1]

# pulando os numeros a partir do penúltimo digito do cartao
sum1 = sum([(int(x) * 2) // 10 +( (int(x) * 2) % 10)for x in copy_cartao[1::2]])
# somar dos múmeros que foram pulados
sum2 = sum( [int(x) for x in copy_cartao[0::2] ])


total = sum1 + sum2
   # verificar cartao válido 
if total % 10 == 0:
  
  #Diferencia cartao 
  if len(cartao) == 15 and cartao[0:2] in ['34', '37']:
   print("AMEX")
  if len(cartao) in [13,16] and cartao[0] == '4':
    print("VISA")
  if len(cartao) == 16 and int(cartao[0:2]) <=56:
     print("MASTERCARD")
  else:
    print("INVALID")
else: 
  print("INVALID")
