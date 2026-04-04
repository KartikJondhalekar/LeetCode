// Problem #1404: Number of Steps to Reduce a Number in Binary Representation to One
// Difficulty : Medium
// Language   : csharp
// Runtime    : 68 ms
// Memory     : 22.8 MB
// URL        : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

public class Solution
{
    public int NumSteps(string s)
    {
        int res = 0;
        int carry = 0;
        for (int i = s.Length - 1; i > 0; i--)
        {
            if (s[i] - '0' + carry == 1)
            {
                res++;
                carry = 1;
            }
            res++;
        }

        return res + carry;
    }
}