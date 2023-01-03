from bonus.bonus7 import feet_inches, parse, convert

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to result")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")
#
# litres = int(input("Enter litres"))
# def liters_to_m3(liters):
#     m3 = float(liters / 1000)
#     return m3
#
# print(liters_to_m3(litres))

# user_password = input("Enter new password: ")
#
# def strength(password,digit = False,uppercase = False):
#     result = {}
#     if len(password) >= 8:
#         result["length"] = True
#     else:
#         result["length"] = False
#
#     for i in password:
#         if i.isdigit:
#             digit = True
#
#     result["digits"] = digit
#
#     for i in password:
#         if i.isupper():
#             uppercase = True
#
#     result["upper-case"] = uppercase
#
#     if all(result.values()):
#         return "Strong password"
#     else:
#         return "Weak password"
#
# print(strength(user_password))



