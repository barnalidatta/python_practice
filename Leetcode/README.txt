Two pointer method
-------------------
2Sum
1. sorted array
2. left pointer at start, right pointer at end
3. calculate sum of left and right
4. if sum is greater than target, then decrement the right pointer( pointing second last)
5. if sum is less than target, then increment the left pointer.
6. move left and right to get the exact target.

3sum
1. two pointers plus additional fix pointer (loop variable) 
2. fix pointer (loop variable,i )is initially set on first element.
3. when looping for first variable, apply two sum on rest of array.

https://leetcode.com/discuss/study-guide/1688903/solved-all-two-pointers-problems-in-100-days

Fast and slow pointer
---------------------
1. fast and slow pointer is two pointer method with different speed
2. Used for linked list

Sliding window
--------------
Use to find Substring/Subarray
1. fixed size - window size =k
2. variable size - increase or shrink the window by incrementing
                    right or left pointer