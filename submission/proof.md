# Baseline: 15 integers in 1..50 with no 3-term arithmetic progression

S = {1, 3, 4, 9, 10, 12, 13, 27, 28, 30, 31, 36, 37, 39, 40}: every integer from 1 to 50 whose base-3 digits are all 0 or 1.

Proof. Write a, b, c in S in base 3 with digits in {0, 1}. Adding a and c digit by digit, each digit sum is 0, 1 or 2, so there
are no carries; doubling b also has none, giving digits 0 or 2. If a + c = 2b then a_i + c_i = 2 b_i for every digit i, which
forces a_i = c_i, so a = c. Hence no three distinct elements a < b < c satisfy a + c = 2b. |S| = 15.
