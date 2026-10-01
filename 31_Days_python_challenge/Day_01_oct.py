"""Control Flow"""

#Task 1. Start with total = 0 and a variable n = 1. 
# Keep adding n to total and increasing n by 1, until total goes above 50. Print how many numbers it took.

total = 0
n = 1

while total < 50:
    n += 1
    total += n 
    print(total)

print(n)

# Task 2. Using input(), keep asking the user for a word until they type "stop". Print "Goodbye" when they do.

word = "continue"
while word != "stop":
    word = input("Type stop when you are done").lower()
print("Goodbye")

"""
Task 3. A job is polling for a file to land. Given checks = 0, keep printing "Waiting for file..." and 
adding 1 to checks until checks reaches 6, then print "Timed out after 6 checks.
"""
checks = 0
while checks < 6:
    checks +=1
    print("Waiting for file...")
print("Timed out after 6 checks.")


"""Task 4. You have queue = ["orders", "customers", "payments", "refunds"]. Drain the queue one table at a time, printing "Loading orders... 3 
tables remaining" and so on, until it is empty."""

db = ["orders", "customers", "payments", "refunds"]

while len(db) > 0:
    table = db.pop()
    print(f"Loading {table}...{len(db)} tables remaining")

"""Task 5. You need to load 47 rows in batches of 10. Print each batch number and how many rows it carries. 
The last batch should carry 7, not 10."""

rows = 47
batch_number = 1

while rows > 0:
    batch = min(10, rows)
    print(f"{batch_number} : {batch} rows")
    rows -= batch
    batch_number += 1
print(f"There are a total of {batch_number - 1} batches")


"""Task 6. A retry loop where the wait doubles each time. Start with wait = 1 and attempt = 0. 
While attempt < 5, print "Attempt 1, waiting 1 second", then double the wait each round. Print the total time waited at the end."""

wait = 1
attempt = 0
total = 0
while attempt < 5:
    attempt = attempt + 1
    print(f"Attempt {attempt}, waiting {wait} second(s)")
    total += wait  
    wait = wait * 2
print(f"The total waiting is {total} seconds")


# Task 7
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 5)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")

"""Task 8: Given numbers = [3, 8, 12, 5, 20, 7], loop through and stop as soon as you hit a number greater than 10. Print which number stopped you."""

numbers = [3, 8, 12, 5, 20, 7]
for number in numbers:
    if number < 10:
        print(number)
    else:
        print(f"I was stopped by {number} as it is greater than the threshold: 10")
        break
        



"""

Tassk 9. Given names = ["ahmed", " ", "judith", " ", "uche"], print each real name, but skip the blank ones. Print "Skipped a blank name" before each skip. (Hint: .strip() turns " " into "")"""

names = ["ahmed", "", "judith", " ", "uche"]

for name in names:
    if name.strip() == "":
        print("skipped  a balnk name")
        continue
    print(name)

"""Task 10. Given logins = ["ok", "ok", "FAILED", "ok"], count how many succeeded, but stop counting the moment you see "FAILED"."""

logins = ["ok", "ok", "FAILED", "ok"]
count = 0

for login in logins:
    if login == "FAILED":
        print(f"{login} detected. Count stopped")
        break
    count +=1
print(f"There are {count} successful logins before failure was detected")

