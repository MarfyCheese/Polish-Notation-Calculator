def RPN(request):
  requestList = request.split(' ')
  stack = []

  for i in range(0,len(requestList)):
    if isnumber(requestList[i]) == True:
      stack.append(float(requestList[i]))
    elif requestList[i] == '+':
      stack.append(stack.pop() + stack.pop())
    elif requestList[i] == '-':
      last = stack.pop()
      first = stack.pop()
      stack.append(first - last)
    elif requestList[i] == '*':
      stack.append(stack.pop() * stack.pop())
    elif requestList[i] == '/':
      last = stack.pop()
      first = stack.pop()
      stack.append(first / last)
    elif requestList[i] == 'x':
      exit()
    elif requestList[i] == 'p':
      print(stack)
    elif requestList[i] == 'i':
      stack.append(1/stack.pop())
    elif requestList[i] == 'n':
      stack.append(-1 * stack.pop())
    else:
        print("the requested input, ",requestList[i], "is invalid, if this is supposed to do something, contact Chris, if its not, then why did you put it in you blockhead \n" )
        
  return stack

def isnumber(s):
    try:
        n = float(s)
        return True
    except ValueError:
        return False

def main():
  print(RPN(input("Please enter your request\n")))

main()