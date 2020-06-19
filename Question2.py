count = 0
total = 0 
def has_no_e(text):
  if not stripped_line.find("e") != -1: 
    return True   
  else:
    return False
  
with open("C:/Users/Alex/Desktop/INF 354/INF354_HomeworkAssignment6/crossword.txt", "r") as a_file: 
  for line in a_file:
    stripped_line = line.strip()
    total += 1
    if (has_no_e(stripped_line)):
      count += 1
      
print(str(round(count/total*100, 2)) + "%")

