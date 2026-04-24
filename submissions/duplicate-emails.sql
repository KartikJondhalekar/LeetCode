-- Problem #182: Duplicate Emails
-- Difficulty : Easy
-- Language   : mysql
-- Runtime    : 395 ms
-- Memory     : 0B
-- URL        : https://leetcode.com/problems/duplicate-emails/

# Write your MySQL query statement below
SELECT email
FROM Person
GROUP BY email
HAVING count(email) > 1;