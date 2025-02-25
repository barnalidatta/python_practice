import pytest

def solution(my_str:str, ends:str):
    if my_str.endswith(ends):
        return True
    else:
        return False

# def test_endswith():
#     res = solution("abc", "bc")
#     assert res == True
                   
print(solution("abc","bc"))
print(solution("abc","d"))