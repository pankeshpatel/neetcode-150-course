# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

# I am assuming that the input string won't have "#" character

Input = ["we", "say", ":", "yes", "!@$%^&*()"]
encoded_string = ""

# encode string
for index in range(0, len(Input)):
    encoded_string += f"{len(Input[index])}" + "#" + Input[index]

print(f"{encoded_string}")


# decoded string
decoded_string_arr = []

# for i in range(0, len(encoded_string)):
i = 0
while i < len(encoded_string):
    length = int(encoded_string[i])
    print(length)
    result = encoded_string[i + 2 : (i + 2) + int(encoded_string[i])]
    decoded_string_arr.append(result)
    i = (i + 2) + int(encoded_string[i])

print(f"{decoded_string_arr}")
