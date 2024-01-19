#You are a secret service agent and you need a code to identify yourself. This is how they identify themselves
# If your names starts with 
# a-first number will be one
# z-number will be 26
#Find out the code for an agent called Ruth

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(len(alphabet))

# letter = 'r'
# index = alphabet.find(letter)
# print(index)

# letter_5 = alphabet[4] 
# print(letter_5)

# position = "z"
# position_2 = "a"
# index_z = alphabet.find(position) +1
# index_r = alphabet.find(position_2) +1
# print(str(index_z) + str(index_r))


def agent_code(agent_name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hashed_name = agent_name.lower()
    code_name = ""
    for letter in hashed_name:
        position = str(alphabet.find(letter) +1)
        code_name = code_name+position
    return int(code_name)

print(agent_code("Maik"))


def sum_agent_code(agent_name):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lower_code = agent_name.lower()
    agent_sum = 0
    for letter in lower_code:
        position = alphabet.find(letter) +1
        agent_sum = agent_sum+position 
    return agent_sum

print(sum_agent_code("Maik"))
print(agent_code("Ruth"))
print(sum_agent_code("Ruth"))
print(sum_agent_code("Lukorito"))
print(agent_code("Lukorito"))
print(agent_code("Diana"))
print(sum_agent_code("Diana"))



# For people earning 30k and below they pay a flatrate of 15% of gross salary for tax
# 30001-60k - Pay 20% of salary as tax
# 60001 -100 -40 %
# 100001 and above -80%
#Write a function that takes in salary  gross pay integer in form and returns their net pay

def net_salary(gross_salary):
    if gross_salary > 100000:
        tax = 80/100 * gross_salary
    elif gross_salary > 60000:
        tax = 40/100 * gross_salary
    elif gross_salary > 30000:
        tax = 20/100 * gross_salary
    else:
        tax = 15/100 * gross_salary

    net_salary = gross_salary - tax
    return net_salary

print(net_salary(120000))
print(net_salary(70000))
print(net_salary(20000))

   
















    












