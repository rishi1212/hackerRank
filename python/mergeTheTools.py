import textwrap

S = input()
K = int(input())

for ti in textwrap.wrap(S, K):
    modified_ti = ""
    for ch in ti:
        if ch not in modified_ti:
            modified_ti += ch

    print(modified_ti)