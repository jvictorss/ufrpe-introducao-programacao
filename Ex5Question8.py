"""
Grade | if Greater than or equal to
A  | 93,33
A- | 90
B+ | 86,67
B  | 83,33
B- | 80
C+ | 76,67
C  | 73,33
C- | 70
D+ | 66,67
D  | 63,33
D- | 60
F  | 0
"""

grade = float(input("Insira sua nota exata: "))

if 0 <= grade < 60:
    print("Sua nota é F")
elif 60 <= grade < 63.33:
    print("Sua nota é D-")
elif 63.33 <= grade < 66.67:
    print("Sua nota é D")
elif 66.67 <= grade < 70:
    print("Sua nota é D+")
elif 70 <= grade < 73.33:
    print("Sua nota é C-")
elif 73.33 <= grade < 76.66:
    print("Sua nota é C")
elif 76.66 <= grade < 80:
    print("Sua nota é C+")
elif 80 <= grade < 83.33:
    print("Sua nota é B-")
elif 83.33 <= grade < 86.66:
    print("Sua nota é B")
elif 86.66 <= grade < 90:
    print("Sua nota é B+")
elif 90 <= grade < 93.33:
    print("Sua nota é A-")
elif 93.33 <= grade < 96.66:
    print("Sua nota é A")
elif 96.66 <= grade <=100:
    print("Sua nota é A+")