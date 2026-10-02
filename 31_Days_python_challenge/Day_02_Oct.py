"""DE Task 1: Given the rows below, load the good ones into a clean list and 
put the bad ones into a quarantine list, using continue. A row is bad if the email is empty or the amount is not greater than zero. 
Print a summary at the end."""

rows = [
    {"id": 1, "email": "a@x.com", "amount": 500},
    {"id": 2, "email": "",        "amount": 900},
    {"id": 3, "email": "c@x.com", "amount": 0},
    {"id": 4, "email": "d@x.com", "amount": 1500},
]

quality_data = []
messy_data = []

for r in rows:
    if r["email"] == "" or r["amount"] < 0:
        messy_data.append(r)
        continue
    quality_data.append(r)

print(f"rows in quality data: {len(quality_data)} \n rows in messy data: {len(messy_data)}")



#DE Task 2. Same rows. This time the business says a single bad row must abort the whole load. Rewrite it with break so nothing is loaded once a bad row appears."""

quality_data = []
messy_data = []

for r in rows:
    if r["email"] == "" or r["amount"] < 0:
        messy_data.append(r)
        break
    quality_data.append(r)

print(f"rows in quality data: {len(quality_data)} \n rows in messy data: {len(messy_data)}")

raw_transactions = [
    {"id": 1, "user": "ahmed",  "amount": 5000,  "currency": "NGN", "status": "success"},
    {"id": 2, "user": "lahla",  "amount": 0,     "currency": "NGN", "status": "failed"},
    {"id": 3, "user": "judith", "amount": 120,   "currency": "USD", "status": "success"},
    {"id": 4, "user": "",       "amount": 800,   "currency": "NGN", "status": "success"},
    {"id": 5, "user": "uche",   "amount": -40,   "currency": "USD", "status": "success"},
    {"id": 6, "user": "ahmed",  "amount": 2500,  "currency": "NGN", "status": "pending"},
    {"id": 7, "user": "judith", "amount": 300,   "currency": "NGN", "status": "success"},
    {"id": 8, "user": "lahla",  "amount": 90,    "currency": "USD", "status": "success"},
]

#print(f"{len(raw_transactions)} raw rows received")

"""What to build
Work through these in order. Each one is a loop you have already written today.

Validate. Split the rows into clean and rejected. A row is rejected if the user is empty, or the amount is not greater than zero. Use continue.

Count by status. Build a dictionary like {"success": 4, "pending": 1, ...} counting the clean rows only.

Total by currency. Build a dictionary of the total amount per currency, for clean rows with status "success" only.

Unique users. Build a set of the distinct users in the clean rows and print how many there are.

Biggest transaction. Find the single clean row with the highest amount and print its id, user and amount. (Track a biggest variable as you loop.)

Print a report. Something a human would actually want to read, for example:"""

cleaned = []
rejected =[]

for tx in raw_transactions:
    if tx["user"] == "" or tx["amount"] <= 0:
        rejected.append(tx)
        continue
    cleaned.append(tx)

#print(f"{len(cleaned)} rows met the category of being clean.")
#print("Here is the status report based on cleaned transactions:")

#Count by status
status_count = {}

for tx in cleaned:
    status = tx["status"]

    if status not in status_count:
        status_count[status] = 1
    else:
        status_count[status] += 1
# print(status_count)


#Total by currency
total = {}

for tx in cleaned:
    currency = tx["currency"]

    if tx["status"] == "success":
        if currency not in total:
            total[currency] = tx["amount"]
        else:
            total[currency] += tx["amount"]

# #print(total)

# for currency, amount in total.items():
#     print(f"{currency}: {amount}")

 #Unique users. Build a set of the distinct users in the clean rows and print how many there are
seen =  set()


for tx in cleaned:
    user = tx["user"]
    if user not in seen:
       seen.add(user)
# print(seen)

# print(f"There are {len(seen)} unique users who met the clean category")

#Biggest transaction. Find the single clean row with the highest amount and print its id, user and amount. (Track a biggest variable as you loop.)
biggest = None

for tx in cleaned:
    if biggest is None or tx["amount"] > biggest["amount"]:
        biggest = tx

# print(f"ID: {biggest['id']}")
# print(f"User: {biggest['user']}")
# print(f"Amount: {biggest['amount']}")

#reort/General summary'

print("=== PIPELINE REPORT ===")
print(f"Rows in: {len(raw_transactions)}") 
print(f"Rows loaded:   {len(cleaned)}")
print(f"Rows rejected: {len(rejected)}")
for tx in rejected:
    if tx["user"] == "":
        print(f" -> id {tx["id"]} rejected due to no user indicated")
    else:
        print(f" ->id  {tx["id"]} rejected due to amount less than 0")

print(f"Status counts in cleaned data:  {status_count}\n")
print("currency grouping in the cleaned data below:")
for currency, amount in total.items():
    print(f"{currency}: {amount}\n")

print(f"Distinct users: {seen}\n")

print(f"Largest transaction details:")
print(f"ID: {biggest['id']}")
print(f"User: {biggest['user']}")
print(f"Amount: {biggest['amount']}\n")

# #Task 3:
"""Reject any row whose status is not one of {"success", "failed", "pending"}."""
valid_statuses = {"success", "failed", "pending"}

for tx in raw_transactions:
    status = tx["status"]

    if status not in valid_statuses:
        rejected.append(tx)

"""Print the percentage of rows that were rejected, rounded to 1 decimal place."""
percent = round((len(rejected)/len(raw_transactions)) * 100, 1)
print(f"The percentage of rows that were rejected is: {percent}\n")

"""Print each user's total spend, sorted is not required, a plain loop is fine."""
user_spend = {}

for tx in raw_transactions:
    user = tx["user"]

    if user not in user_spend:
        user_spend[user] = tx["amount"]
    else:
        user_spend[user] += tx["amount"]
print("The indiviual user spending details are as follows:")
for user, amount in user_spend.items():
    if user == "":
        user = "unknown"
    print(f"{user}: {amount}")

#Task 4. Write square(n) that returns n multiplied by itself. Print the result of square(7).
def square(n):
    return n *n

print(square(4))

#Task 5. Write is_even(n) that returns True or False. Use it inside a loop over [1, 2, 3, 4, 5, 6] to print only the even numbers.
def is_even(n):
    return n % 2 == 0

print(is_even(7))
numbers = [1,2,3,5,4,6,7]
for n in numbers:
    if is_even(n):
        print(n)

#Task 6. Write greet(name, greeting="Hello") that returns the greeting string instead of printing it. Call it twice, once with the default and once with "Sannu".
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Lorreta"))
print(greet("Lorreta", "Sannu"))

#Task 7. Write longest_word(words) that takes a list of words and returns the longest one. Test it with ["python", "sql", "airflow", "dbt"].
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(["python", "sql", "airflow", "dbt"]))

#Task 8. Write stats(numbers) that returns three things: the count, the total and the average. Unpack them into three variables and print each.
def stats(numbers):
    count = len(numbers)
    total = sum(numbers)
    av= total/count
    return count, total, av
#f"count: {count}, \n Sum: {total}, \n average: {av}"

count, total, av = stats([3,4,5,6,87,9,0,1,2,3,4,5,6,7,8,9])
print(f"count: {count}")
print(f"total: {total}")
print(f"average: {av}")


#Task 9. Write shout(*words) that accepts any number of words and returns them joined with spaces, in capitals. shout("data", "is", "power") should return "DATA IS POWER"
#. (Hint: " ".join(list_of_strings))"""

def shout(*words):
    return " ".join(words).upper()

print(shout("Uche", "is", "a", "data", "engineer"))

#DE Task 10. Write is_valid_email(email) that returns True only if the
#  string contains "@" and a "." after the @. Test it on ["a@x.com", "bad-email", "no@dotcom", ""].

def is_valid_email(email):
    at_position = email.find("@")
    dot_position = email.find(".", at_position) #searches the position of dot immediately after the position of the @

    if at_position == -1 or dot_position == -1: #.find() returns -1 if it cannot find what we requested
    return True
emails = ["a@x.com", "bad-email", "no@dotcom", ""]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")