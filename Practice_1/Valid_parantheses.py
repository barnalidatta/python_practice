# Return True if every opening bracket has a matching closing bracket in the correct order.
# Stack

def valid_p(s):
    stack = []
    # s1 = s[0:len(s):2]
    # s2 = s[1:len(s):2]
    # s2 = s2[::-1]
    mapping = {")": "(", "}": "{", "]": "["}
    
    for ch in s:
        # print(ch)

        # you can check the key in dictionary " if key in dictionary"
        # you can't check the value in same way as key but "if value in dict.values():
        # Of course I know "
        # key is  closing bracket, value is opening bracket
        # 
        # if the incoming string character (opening bracket) is not a "key" of the mapped dictionary, that means if the key is not found, it will fall to the else condition, which is adding the string character (opening bracket) to the stack. 
        # if the incoming string character (closing bracket) is a "key" of the mapped dictionary and its value (opening bracket) is not the top element in the stack, then pop the item, which is popping the opening bracket.

        # When see Opening bracket → push the Opening bracket onto stack

        # When see Closing bracket → pop the Opening bracket from stack, but before that the opening bracket of that Closing bracket must match the opening bracket at the top of the stack before popping it
        if ch in mapping:
            if not stack:
                return False
            if stack[-1] != mapping[ch]:     # stack will have just opening brackets
                return False
            print(f"popping from stack - {ch}")
            stack.pop()
        else:
            print(f"Adding to stack - {ch}")
            stack.append(ch)

    if len(stack) == 0:
        return True
    else:
        return False

print(valid_p("()[]{}"))
print(valid_p("((({[[{()}]]})))"))
