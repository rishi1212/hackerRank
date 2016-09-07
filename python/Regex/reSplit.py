import re
print "\n".join(filter(lambda x: x != '', re.split(r'[.,]', raw_input())))