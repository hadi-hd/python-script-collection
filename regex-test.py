import re

txt = "0912-345-6789"
_phonenumber1 = re.search(r"0?\d{3}[\s-]*\d{3}[\s-]*\d{4}$", txt)

txt = "+98 912 345 6789"
_phonenumber2 = re.search(r"(\+?98)?[\s-]*\d{3}[\s-]*\d{3}[\s-]*\d{4}$", txt)

txt = "0, 1, 2, 3, 4, 5"
_splitmatch = re.split(r"(?:\s*),(?:\s*)", txt)

print(_phonenumber1.group() + "\r\n" + _phonenumber2.group() + "\r\n" + " ".join(_splitmatch))
