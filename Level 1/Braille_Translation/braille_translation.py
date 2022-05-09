import string
def solution(s):
  alphadict = {'a': '1', 'b': '12', 'c': '14', 'd': '145', 'e': '15', 'f': '124', 'g': '1245', 'h': '125', 'i': '24', 'j': '245', 'k': '13','l': '123', 'm': '134', 'n': '1345', 'o': '135', 'p': '1234', 'q': '12345', 'r': '1235', 's': '234', 't': '2345', 'u': '136','v': '1236', 'w': '2456', 'x': '1346', 'y': '13456', 'z': '1356',' ':'' }
  list1 = list(string.ascii_lowercase)
  ascii_uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  answer = ""
  for i in range(len(s)):
    if s[i] in ascii_uppercase:
      answer += "000001"
      s = list(s)
      s[i] = s[i].lower()
      s = ''.join(s)

    str1 = "000000"
    list1 = list(str1)
    transcribe = alphadict[s[i]]
    for j in range(len(transcribe)):
      k = int(transcribe[j]) - 1
      list1[k] = "1"
    str1 = ''.join(list1)
    answer += (str1)
  return(answer)
