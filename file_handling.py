file = None
try:
  file = open("employee.txt","x")
  file.write("\n chandan ")
except Exception as e:
  print(f"Error: {e}")
finally:
  if file:
   file.close()
