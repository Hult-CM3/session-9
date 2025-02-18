# grade scenario - which works?
def get_grade1(s): # does not work
   if 100 < s > 90:
      return 'A'
   if 90 < s > 80: 
      return 'B' 
   if 80 < s > 70: 
      return 'C' 
   return 'F'

def get_grade3(s): # works
   if 100 >= s >= 90:
     return 'A'
   if 90 > s >= 80:
     return 'B' 
   if 80 > s >= 70:
     return 'C'
   return 'F'

def get_grade2(s): # works!
   if s >= 90: 
      return 'A' 
   if s >= 80: 
      return 'B' 
   if s >= 70: 
      return 'C' 
   return 'F'

gr = [95, 85, 75, 65] # should return an 'A' 'B' 'C' then 'F'

for i in gr:
    print(f"1 {get_grade1(i)}")
    print(f"2 {get_grade2(i)}")
    print(f"3 {get_grade3(i)}")

# Vowel scenario - which works?

def any_vowel_1(s): # works
    for c in s:
        if c in 'aeiou':
            return True
    return False
  
def any_vowel_2(s): # doesn't work
    for c in s:
        if 'c' in 'aeiou':
            return 'True'
        else:
            return 'False'

def any_vowel_3(s): # doesn't work
    for c in s:
        flag = c not in 'aeiou'
    return flag

w = ["hello", "sky"]

for j in w:
    print(f"1 {j} - {any_vowel_1(j)}")
    print(f"2 {j} - {any_vowel_2(j)}")
    print(f"3 {j} - {any_vowel_3(j)}")

# Sentence Scenario - which works?

def count_1(sentence, target): # works 
    words = sentence.split()
    count = 0
    for word in words:
        if word == target:
            count = count + 1
    return count

def count_2(sentence, target): # doesn't work
    words = sentence.split()
    count = 0
    for word in words:
        if word == target:
            count += 1
            return count
    return count 

def count_3(sentence, target): # works
    words = sentence.split()
    count = 0
    for word in words:
        if target in word:
            count = count + 1
    return count

print(f"1 - {count_1("the cat and the dog go to the moon", "the")}")
print(f"2 - {count_2("the cat and the dog go to the moon", "the")}")
print(f"2 - {count_3("the cat and the dog go to the moon", "the")}")


