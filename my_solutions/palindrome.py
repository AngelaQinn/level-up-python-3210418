def is_palindrome(txt):
  revtext = ''
  for i in txt:
    revtext = i+revtext
    if txt == revtext:
      print('yes')
    else:
      print('no')
