import re
text1="aptekab"
task_1 = re.findall(r'ab*', text1)

text2="abbb"
task_2 = re.findall(r'ab{2,3}', text2)

text3="hello_world"
task_3 = re.findall(r'\b[a-z]+_[a-z]+\b', text3)

text4="Bioject"
task_4 = re.findall(r'\b[A-Z][a-z]+\b', text4)

text5="alphabetb"
task_5 = re.findall(r'a.*?b', text5)

text6="Hello, world."
task_6 = re.sub(r'[ ,.]', ':', text6)

def snake_to_camel(match):
    parts = match.group().split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
text7 = "hello_world"
task_7 = re.sub(r'\b[a-z]+_[a-z]+\b', snake_to_camel, text7)

text8="HelloWorldRegex"
task_8 = re.split(r'(?=[A-Z])', text8)

text9="ThisIsATest"
task_9 = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text9)

text10="camelCase"
task_10 = re.sub(r'([a-z])([A-Z])', r'\1_\2', text10).lower()


print("1: ",task_1)
print("2: ",task_2)
print("3: ",task_3)
print("4: ",task_4)
print("5: ",task_5)
print("6: ",task_6)
print("7: ",task_7)
print("8: ",task_8)
print("9: ",task_9)
print("10: ",task_10)
