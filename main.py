import sys

__AUTHOR__ = "t0gu ~ Twitter: @t0guu"

if len(sys.argv) < 2:
    print(">>> usage: main.py <YourPayLoad>")
    print(f"{__AUTHOR__}")
    sys.exit(1)

print(f"{__AUTHOR__}")

string = sys.argv[1]

normalized_less_than = ["＜", "﹤", "≮"]
normalized_higher_than = ["≯","﹥", "＞"]
normalize_quote = ["＇","＂"]
normalize_grave = ["`","｀"]
normalized_semicolon = [";", "︔", "﹔", "；"]
normalize_quote = ["⩴", "⩴", "︓", "﹕", "："]
normalize_slash = ["／"]
normalize_back_slash = ["＼", "﹨"]
open_brackets = ["︷", "﹛", "｛"]
close_brackets = ["︸", "﹜", "｝"]
open_col = ["﹇", "［"]
close_col = ["﹈", "］"]
open_para = ["⁽", "₍"]
close_para = ["⁾", "₎"]


payload = ""

for i in string:
    if i == "<":
        for n1 in normalized_less_than:
            print(string.replace(i,n1))
    if i == ">":
        for n2 in normalized_higher_than:
            print(string.replace(i,n2))
    if i == "'":
        for n3 in normalize_quote:
            print(string.replace(i,n3))
    if i == "`":
        for n4 in normalize_quote:
            print(string.replace(i,n4))
    if i == "`":
        for n5 in normalize_grave:
            print(string.replace(i,n5))
    if i == ":":
        for n6 in normalize_quote:
            print(string.replace(i,n6))
    if i == "/":
        for n7 in normalize_slash:
            print(string.replace(i,n7))
    if i == '\\':
        for n8 in normalize_back_slash:
            print(string.replace(i,n8))
    if i == "{":
        for n9 in open_brackets:
            print(string.replace(i,n9))
    if i == "}":
        for n10 in close_brackets:
            print(string.replace(i,n10))
    if i == "[":
        for n11 in open_col:
            print(string.replace(i,n11))
    if i == "]":
        for n12 in close_col:
            print(string.replace(i,n12))
    if i == "(":
        for n13 in open_para:
            print(string.replace(i,n13))
    if i == ")":
        for n14 in close_para:
            print(string.replace(i,n14))
