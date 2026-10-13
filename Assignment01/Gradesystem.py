mark=int(input('Enter the mark: '))

if mark >= 90:
  print("Grade A")
if mark >= 75 and mark<90:
  print("Grade B")
if mark >= 50 and mark<75:
  print("Grade C")
if mark <50:
  print("Grade D")