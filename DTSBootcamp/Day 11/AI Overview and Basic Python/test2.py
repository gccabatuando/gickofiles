a = 20
b = 20

if ( a is b ):
   print("Line 1 - a and b have same identity")
else:
   print("Line 1 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print("Line 2 - a and b have same identity")
else:
   print("Line 2 - a and b do not have same identity")

