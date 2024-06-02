from poker import poker 

def pokerhiddentestcases():
  file = open('Pokertest.txt')
  lines = list(file)
  lines_parsed = [line.replace('\n', '') for line in lines]
  Inputs = []
  for line in lines_parsed:
    if len(line) == 29:
      Inputs.append(line)
  Outputs = []
  for line in lines_parsed:
    if len(line) == 8:
      Outputs.append(line)
  return Inputs, Outputs

def check(cases, output):
  if poker(cases) != output:
    print("Failed for input : " + str(cases) + "\nOutput : " + output)
    return False
  return True
  
def test():
  I, O = pokerhiddentestcases()
  count = 0
  for number in range(len(I)):
    if O[number] == "Player 1":
      out = I[number][:14].strip() 
    else:
      out = I[number][14:].strip()
    if check([I[number][:14].strip(), I[number][14:].strip()], out):
      count += 1
  return count, len(I)
  
p = test()
print("Summary")
print("Testcases : " + str(p[0]) + "/" + str(p[1]))