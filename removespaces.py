str=input()
import re
pattern=r" "
newstr=re.sub(pattern, "", str)
print(newstr)