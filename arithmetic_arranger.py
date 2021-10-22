def arithmetic_arranger(problems, sol=False):
  arranged_problems = ""
  if(len(problems) > 5):
    return "Error: Too many problems."
  prob = []
  for i in range(len(problems)):
    prob.append(problems[i].split())
    if (prob[i][1] == '+' or prob[i][1] == '-') == False:
      return "Error: Operator must be '+' or '-'."
    if (prob[i][0].isdigit() == False) or (prob[i][2].isdigit() == False):
      return "Error: Numbers must only contain digits."
    if (len(prob[i][0]) >= 5 or len(prob[i][2]) >= 5):
      return "Error: Numbers cannot be more than four digits."
  lenDashes = max(len(prob[0][0]), len(prob[0][2])) + 2
  fourspaces = '    '
  for i in range(len(problems)):
    # lenDashes is length of dashes
    lenDashes = max(len(prob[i][0]), len(prob[i][2])) + 2
    # len1 is the length before first operand
    len1 = lenDashes - len(prob[i][0])
    space1 = ""
    for _ in range(len1):
      space1 = space1 + " "
    arranged_problems += space1
    arranged_problems += prob[i][0]
    if i != (len(problems) - 1):
      arranged_problems += fourspaces
  arranged_problems += '\n'
  for i in range(len(problems)):
    arranged_problems += prob[i][1]
    # len2 as the length before second operand
    # if 2nd operand > 1st operand, print one space
    # else print 1st operand - 2nd operand space + one space
    len2 = 0
    space2 = ""
    if len(prob[i][2]) >= len(prob[i][0]):
      space2 = " "
    else:
      len2 = len(prob[i][0]) - len(prob[i][2]) + 1
      for _ in range(len2):
        space2 += " "
    arranged_problems += space2
    arranged_problems += prob[i][2]
    if i != (len(problems) - 1):
      arranged_problems += fourspaces
  arranged_problems += '\n'
  for i in range(len(problems)):
    lenDashes = max(len(prob[i][0]), len(prob[i][2])) + 2
    dash3 = ""
    for _ in range(lenDashes):
      dash3 += "-"
    arranged_problems += dash3
    if i != (len(problems) - 1):
      arranged_problems += fourspaces
  if sol == True:
    arranged_problems += '\n'
    for i in range(len(problems)):
      o1 = int(prob[i][0])
      o2 = int(prob[i][2])
      ans = 0
      if prob[i][1] == '+':
        ans = o1 + o2
      elif prob[i][1] == '-':
        ans = o1 - o2
      lenDashes = max(len(prob[i][0]), len(prob[i][2])) + 2
      ansstrlen = len(str(ans))
      lenspace4 = lenDashes - ansstrlen
      space4 = ""
      for _ in range(lenspace4):
        space4 += " "
      arranged_problems += space4
      arranged_problems += str(ans)
      if i != (len(problems) - 1):
        arranged_problems += fourspaces

  # print(arranged_problems)
  return arranged_problems