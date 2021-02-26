## Double Char

def double_char(s):
    y=""
    for x in s:
        y+=x+x
    print(y)
    
s="1234!_ "
double_char(s)
# test.assert_equals(double_char("String"),"SSttrriinngg")
# test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
# test.assert_equals(double_char("1234!_ "),"11223344!!__  ")