# grade scenario - which works?
def get_grade1(s):
   if 100 < s > 90:
      return 'A'
   if 90 < s > 80: 
      return 'B' 
   if 80 < s > 70: 
      return 'C' 
   return 'F'

def get_grade3(s): 
   if 100 >= s >= 90:
     return 'A'
   if 90 > s >= 80:
     return 'B' 
   if 80 > s >= 70:
     return 'C'
   return 'F'

def get_grade2(s): 
   if s >= 90: 
      return 'A' 
   if s >= 80: 
      return 'B' 
   if s >= 70: 
      return 'C' 
   return 'F'
s = [95, 75, 65] # should return an 'A' 'B' then 'F'

for i in gr:  
  print("1 {get_grade1(gr[i])}")
  print("2 {get_grade2(gr[i])}")
  print("3 {get_grade3(gr[i])}")

# Vowel scenario - which works?

def any_vowel_1(w):
    for c in s:
        if c in 'aeiou':
            return True
    return False
  
def any_vowel_2(w):
    for c in s:
        if 'c' in 'aeiou':
            return 'True'
        else:
            return 'False'

def any_vowel_3(w):
    for c in s:
        flag = c not in 'aeiou'
    return flag

w = ["hello", "sky"]
for j in w:  
  print("1 {any_vowel1(w[j])}")
  print("2 {any_vowel2(w[j])}")
  print("3 {any_vowel3(w[j])}")

# Sentence Scenario - which works?

def count_1(sentence, target):
    words = sentence.split()
    count = 0
    for word in words:
        if word == target:
            count = count + 1
    return count

def count_2(sentence, target):
    words = sentence.split()
    count = 0
    for word in words:
        if word == target:
            count += 1
            return count
    return count 

def count_3(sentence, target):
    words = sentence.split()
    count = 0
    for word in words:
        if target in word:
            count = count + 1
    return count

print(count_1("the cat and the dog", "the"))
print(count_2("the cat and the dog", "the"))
print(count_3("the cat and the dog", "the"))

