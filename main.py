"""
Given a string as input, print the first 3 chars and the last 3 chars of the string.
Input-> "Acting"
Output-> 
First3: Act Last3: ing
"""

st = "Acting"
ln = len(st)
fir = ""
lst = ""
for i in range(0,3):
  ch = st[i]
  fir = fir + ch
for j in range(3,ln):
  e = st[j]
  lst = lst + e
print(f"First3:{fir}")
print(f"Last3:{lst}")
