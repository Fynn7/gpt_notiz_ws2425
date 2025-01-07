import sys

try:
    seconds=int(sys.argv[1])
except ValueError:
    print("Bitte geben Sie eine Zahl ein, nicht",sys.argv[1])
    sys.exit()

Y = 60*60*24*365    # 31536000 Sekunden pro Jahr
D = 60*60*24        # 86400 Sekunden pro Tag
H = 60*60           # 3600 Sekunden pro Stunde
M = 60              # 60 Sekunden pro Minute

# s = y*Y + d*D + h*H + m*M + s
# Beispiel: seconds = 3701

# seconds=31536000+1000
y = seconds // Y            # Anzahl der ganzen Jahre
d = seconds % Y // D        # eliminiert alle ganzen Jahre; Alternativ: `d=(seconds-y*Y)//D`
h = seconds % D // H   
m = seconds % H // M
s = seconds % M 

print(y, "Jahr(e),", d, "Tag(e),", h, "Stunde(n),",
      m, "Minute(n) und", s, "Sekunde(n).")