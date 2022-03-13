import re

m=input()
x=re.sub(r'(?<!^)(?=[A-Z])', '_', m).lower()
print(x)