print("Welcome to the Temperature Conversion System!!")
temp_unit=str(input("Enter the unit in celcius or fahreheit "))
try:
    temp=float(input("Enter the temperature:-"))
except:
    temp=float(input("Enter the temperature:-"))
print("Input Temperature -",temp,temp_unit)
if(temp_unit=='C' or temp_unit=='c'):
    temp=(temp*(9/5))+32
    temp_unit='F'
else:
    temp=(temp-32)*(5/9)
    temp_unit='C'
print("Converted Temperature -",temp,temp_unit)


