def whatday(num):
  # Put your code here
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num-1] if num >= 1 and num <= 7 else "Wrong, please enter a number between 1 and 7"
