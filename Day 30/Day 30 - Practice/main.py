# #KeyError
# a_dict = {"Key":"Value"}
# print(a_dict["test"])

# # TypeError
# value_a = "Hello"
# value_b = 2
# sum = value_a + value_b

# # IndexError
# list_a = ["a","b"]
# print(list_a[2])

# # FileNotFoundError
# x = open("a_test.txt")

# # to catch all these exceptions we use
# try: [try this first]
# except: [if it throws error do this]
# else: [if it does not throw error then do this]
# finally: [do this irrespective of any errors]

# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("something")
# except KeyError as error_message: #getting a hold of the error
#     print(f"The key - {error_message} doesnt exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("Haha Gotcha!")


