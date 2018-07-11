
#take two string, return one sorted uniq string
def longest(s1, s2):
     return "".join(sorted(set(s1 + s2)))
