import re
import requests

req = requests.get("http://jonghyup.com/tmp/sampledata.txt").text

phone_number = re.findall(r"010-\d{4}-\d{4}", req)

personal_number = re.findall(r"\d{6}-[1-4]\d{6}", req)

# univ_number = re.findall(r"20[0-2][0-5]\d\d\d\d\d", req)

local_number = re.findall(r"0[2-9]\d-[1-9][0-9]{2,3}-\d{4}", req) + re.findall(r"02-[1-9][0-9]{2,3}-\d{4}", req)
local_number_prof = re.findall(r"0[2-9]?\d-\d{3,4}-\d*4", req)

email = re.findall(r"[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", req)

date = re.findall(r"2\d{3}-[0-1][0-9]-\d{2}", req)

print(len(phone_number),"phone number")
print(phone_number)
print("="*20)
print(len(personal_number),"personal number")
print(personal_number)
print("="*20)
# print(len(univ_number),"univ number")
# print(univ_number)
print("="*20)
print(len(local_number),"local number")
print(local_number)
print("="*20)
print(len(email),"email")
print(email)
print("="*20)
print(len(date),"date")
print(date)


univ_number = re.findall(r"20(0[0-9]|1[0-9]|2[0-5])\d{5}", req) # 2000~2025/d/d/d/d/d New One

univ_number = re.findall(r"20[00-25]\d\d\d\d\d", req) # Old One
# 20'1~9'/d/d/d/d/d  error

print(univ_number, "univ number")
