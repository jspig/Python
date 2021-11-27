code = input("Enter the coded phrase here: ")
distance = int(input("Enter the Ceasar symbol here: "))
PT = " "
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
                      (distance - (ord('a') - ordValue - 1))
        PT += chr(cipherValue)
print(PT)
            
