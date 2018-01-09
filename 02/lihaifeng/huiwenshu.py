while True:
 input_number = raw_input("please input a number/exit:")
 if input_number == 'exit':
   break
 num_list = []
 num_list.extend(input_number)
 if num_list == num_list[::-1]:
   print 'The number is a Palindrome number'
 else:
  print 'The number is not a Palindrome number'
