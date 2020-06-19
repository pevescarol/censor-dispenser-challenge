import re

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Censurar solo "learning algorithms"
def censor_one(text, censor):
  return text.replace(censor, "######## ##########")

#print(censor_one(email_one, "learning algorithms"))

# Censurar para cualquier otra palabra
def censor_word(text, censor):
  censored = ""
  for i in range(len(censor)):
    if censor[i] == " ":
      censored = censored + " "
    else:
    	censored = censored + "#"
  return text.replace(censor, censored)

#print(censor_word(email_one, "the system with the internet"))

# Censura para email_two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_two(email, lst):
  new_text = ''
  i = 0
  for item in lst:
    censored = []
    while len(censored) < len(item):
      censored.append('#')
    censored_join = ''.join(censored)

    if i == 0:
      regex =  "\\b"+ item + "\\b"
      new_text = re.sub(regex, censored_join, email, flags = re.IGNORECASE)
      i += 1
    else:
      regex =  "\\b"+ item + "\\b"
      new_text = re.sub(regex, censored_join, new_text, re.IGNORECASE)

  return new_text

#print(censor_two(email_two, proprietary_terms))

#Censurar email_three

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
  
def negative_proprietary_censor(email, lst1, lst2):
  new_text = ''
  i = 0
  j = 0
  for item in lst1:
    censored = []
    while len(censored) < len(item):
      censored.append('#')
    censored_join = ''.join(censored)

    regex =  "\\b"+ item + "\\b"
    tmp_lst = re.search(regex, email)
    if tmp_lst != None:
      i += 1
    if i >= 2:
      break

  for word in lst1:
    if i >=2 and j == 0 :
      regex = "\\b"+ word + "\\b"
      new_text = re.sub(regex, censored_join, email, flags = re.IGNORECASE)
      j += 1

    elif i >= 2 and j != 0:
      regex = "\\b"+ word + "\\b"
      new_text = re.sub(regex, censored_join, new_text, flags = re.IGNORECASE)

  new_text = censor_two(new_text, lst2)
  return new_text
  

#print(negative_proprietary_censor(email_three, negative_words,proprietary_terms))


def censor_it_all(email, lst1, lst2):
  censor_email = negative_proprietary_censor(email, lst1, lst2)
  split_email = censor_email.split(' ')
  new_split_email = []
  i = 0
  j = 0
  for word in split_email:
    if j < i:
      j += 1
      continue
    else:
      tmp_value1 = word.find('#')
      tmp_value2 = word.find('\n')
      if tmp_value1 == -1:
        if split_email[i + 1].find('#') != -1 :
          censored = []
          while len(censored) < len(word):
            censored.append('#')

          censored_join = ''.join(censored)
          new_split_email.append(censored_join)
          i += 1
          j += 1
        else:
          new_split_email.append(word)
          i += 1
          j += 1
      else:
        if tmp_value2 == -1:
          if split_email[i +1].find('#') == -1 :
            censored = []
            while len(censored) < len(split_email[i + 1]):
              censored.append('#')
            censored_join = ''.join(censored)
            new_split_email.append(word)
            new_split_email.append(censored_join)
            i += 2
            j += 1
          else:
            new_split_email.append(word)
            i += 1
            j += 1
        else:
          new_split_email.append(word)
          i += 1
          j += 1
  return ' '.join(new_split_email)
     

print(censor_it_all(email_four,negative_words,proprietary_terms))