# 1
def any_lowercase1(s):
   for c in s:
     if c.islower():
        return True
     else:
        return False

# 2
def any_lowercase2(s):
   for c in s:
     if 'c'.islower():
        return 'True'
     else:
        return 'False'

# 3
def any_lowercase3(s):
   for c in s:
     flag = c.islower()
   return flag

# 4
def any_lowercase4(s):
   flag = False
   for c in s:
     flag = flag or c.islower()
   return flag

# 5
def any_lowercase5(s):
   for c in s:
     if not c.islower():
        return False
   return True

s = "lowercase"
s1 = "UPPERCASE"
s2 = "mIx MiX"
print("#1 lowercase, uppercase, mix")
print(any_lowercase1(s))
print(any_lowercase1(s1))
print(any_lowercase1(s2))

print("#2 lowercase, uppercase, mix")
print(any_lowercase2(s))
print(any_lowercase2(s1))
print(any_lowercase2(s2))

print("#3 lowercase, uppercase, mix")
print(any_lowercase3(s))
print(any_lowercase3(s1))
print(any_lowercase3(s2))

print("#4 lowercase, uppercase, mix")
print(any_lowercase4(s))
print(any_lowercase4(s1))
print(any_lowercase4(s2))

print("#5 lowercase, uppercase, mix")
print(any_lowercase5(s))
print(any_lowercase5(s1))
print(any_lowercase5(s2))

