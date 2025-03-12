# copied from walkccc
def countBinarySubstrings(s: str) -> int:

    prev_group = 0
    curr_group = 1
    result = 0

    for i in range(len(s) - 1):
        print("######### String Check #######")
        print(f"comparing {i}th and next one of 000111")
        if s[i] == s[i + 1]:
            print("\nstring match")
            curr_group += 1
            print(f"curr_group is {curr_group}")

        else:
            print("\nChange of string")
            result += min(prev_group, curr_group)
            print(f"prev_group is {prev_group}")
            print(f"curr_group is {curr_group}")
            print(f" result is {result}")

            prev_group = curr_group

            curr_group = 1

    result += min(prev_group, curr_group)  
    print(f"last prev_group is {prev_group}")
    print(f"last curr_group is {curr_group}")   
    print(f"result is {result}")
    return result

countBinarySubstrings("000111")