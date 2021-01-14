def RPN(request):
  maththingy = request.split(' ')
  otherthingy = []

  for i in range(0,len(maththingy)):
    if isnumber(maththingy[i]) == True:
      otherthingy.append(float(maththingy[i]))
    elif maththingy[i] == '+':
      otherthingy.append(otherthingy.pop() + otherthingy.pop())
    elif maththingy[i] == '-':
      last = otherthingy.pop()
      first = otherthingy.pop()
      otherthingy.append(first - last)
    elif maththingy[i] == '*':
      otherthingy.append(otherthingy.pop() * otherthingy.pop())
    elif maththingy[i] == '/':
      last = otherthingy.pop()
      first = otherthingy.pop()
      otherthingy.append(first / last)
    elif maththingy[i] == 'x':
      exit()
    elif maththingy[i] == 'p':
      print(otherthingy)
    elif maththingy[i] == 'i':
      otherthingy.append(1/otherthingy.pop())
    elif maththingy[i] == 'n':
      otherthingy.append(-1 * otherthingy.pop())
    else:
        bunger = 1 
        bunger += bunger
        
  return otherthingy

def isnumber(s):
    try:
        n = float(s)
        return True
    except ValueError:
        return False

def main():
  print(RPN(input("Please enter your request\n")))

main()