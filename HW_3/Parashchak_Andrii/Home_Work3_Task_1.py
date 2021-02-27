# 1111111111111
zen_of_python = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

find_better = int(zen_of_python.count("better"))
find_never = int(zen_of_python.count("never"))
find_is = int(zen_of_python.count("is"))

print("Amount of better words:", find_better)
print("Amount of never words:", find_never)
print("Amount of is words:", find_is)


# 2222222222222222
upper_text = zen_of_python.upper()
print(upper_text)


# 3333333333333333
change = zen_of_python.replace("i", "&")
print(change)