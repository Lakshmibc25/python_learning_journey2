students = ["chandan3", "darshan3", "narendra3"]

with open("class.txt", "w") as file:

  for student in students:
    file.write(f"{student}\n")

