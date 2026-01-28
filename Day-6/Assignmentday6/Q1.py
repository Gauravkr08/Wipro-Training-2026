import re

emp_id = "EMP123"

match_result = re.match(r"(EMP)(\d{3})", emp_id)

if match_result:
    print("Valid Employee ID")
    print("Full Match :", match_result.group(0))
    print("Group 1 (Prefix):", match_result.group(1))
    print("Group 2 (Digits):", match_result.group(2))
else:
    print("Invalid Employee ID")

print("--------------------------------")

text = "Please contact us at support123@example.com for assistance."

email_pattern = r"(\w+@\w+\.\w+)"
search_result = re.search(email_pattern, text)

if search_result:
    print("Email Found")
    print("Full Email :", search_result.group(0))
    print("Username   :", search_result.group(1))
else:
    print("No Email Found")

print("--------------------------------")

pattern = r"(\w+)\s*(\d+\.?\d*)"

sample_text = "Item price 250.75"
meta_result = re.search(pattern, sample_text)
if meta_result:
    print("Meta-character Match Found")
    print("Word  :", meta_result.group(1))
    print("Number:", meta_result.group(2))