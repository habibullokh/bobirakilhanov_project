# ---------------------------------------------------------------------- 1

kun = int(input("Enter day to know how many days equal to month and year: "))
yil = kun // 365
kunlar = kun % 365
oy = kun // 30
kun = kun % 30
print(f"Yil: { yil }\nOy: { oy }\nKunlar: {kun}\n")

# ---------------------------------------------------------------------- 2

f_number = input("Enter first number: ")
s_number = input('Enter second number: ')
if f_number.find(s_number) >= 0:
  print("True")
else:
  print("False")

---------------------------------------------------------------------- 3

str = "The quick brown fox jumps over the lazy dog."
z = "sajdhlkanKLHEW"
n = True
for x in z:
  if x not in str.lower():
    n = False
    if n == True:
      print(True)
    else:
      print(False)
