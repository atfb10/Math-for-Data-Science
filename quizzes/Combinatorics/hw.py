import numpy as np

'''
Question 1 — You have to solve 5 tasks in parallel and have 5 engineers at your
disposal. Each engineer can only work on one task. How many possibilities are
there to distribute the tasks?
'''

# NOTE: Permutation no repeat n! / (n - k)!
n = 5
k = 5

numerator = np.math.factorial(n)
denominator = np.math.factorial(n - k)
result = numerator / denominator # 120

'''
Question 2 — In how many ways can you arrange a card deck of 32 cards?
'''
result = np.math.factorial(32) # 263130836933693530167218012160000000

'''
Question 3 — You want to extend your company with two new locations. There
are 5 possible spots available. However, due to the current material shortage,
you can only build one office at the time. How many possibilities exist to build
the two offices?
'''

# NOTE: Permutation no repeat n! / (n - k)!

n = 5
k = 2
numerator = np.math.factorial(n)
denominator = np.math.factorial(n - k)
result = numerator / denominator # 20

'''
Question 4 — You have 6 new features for your website and want to compare
them against each other using A/B testing. How many iterations do you need
to run?
'''

# NOTE: combination no repeat n!/k!(n-1)!
n = 6
k = 2
numerator = np.math.factorial(n)
denominator = np.math.factorial(k) * (np.math.factorial(n - k))
result = numerator / denominator
print (result)

'''
Question 5 — You want to find a secure password, consisting of the letters
[a-z], [A-Z], and digits 0-9. Imagine a modern computer which can test 1 billion
passwords a second. How many characters should your password have so that
the attacker would need at least a year to guess it?
'''

# NOTE: permutation w/ repeats

seconds_in_year = 365 * 24 * 60 * 60 # days * hours * minutes * seconds
n = 62 # 26 char + 26 char + 10 digits
pwd_guess_per_minute = 1000000000
is_long_enough = False 
k = 1
pwd_complexity = 0
while True:
    pwd_complexity = n ** k
    is_long_enough = (pwd_complexity / pwd_guess_per_minute) >= seconds_in_year
    if is_long_enough:
        break
    k += 1

# K = 10