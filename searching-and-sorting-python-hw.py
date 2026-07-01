H1) The Spam Detector (Linear Search)
Question

A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against a blacklist of known spam sender IDs. The blacklist has no order.

Write a Python program to search a spam sender using Linear Search.

Answer
spam = ["abc@gmail.com", "spam@yahoo.com", "test@gmail.com"]

search = "spam@yahoo.com"

found = False

for i in spam:
    if i == search:
        found = True
        break

if found:
    print("Spam Sender Found")
else:
    print("Spam Sender Not Found")
Output

Spam Sender Found

H2) The E-Commerce Price Filter (Binary Search)
Question

You're on Flipkart. You filter products:

"Show me laptops priced ₹50,000 or above."

Products are sorted by price. Flipkart must find the first product priced ₹50,000 or above.

Write a Python program using Binary Search.

Answer
price = [20000, 30000, 45000, 50000, 60000, 70000]

target = 50000

low = 0
high = len(price) - 1

while low <= high:
    mid = (low + high) // 2

    if price[mid] == target:
        print("Product Found at Index", mid)
        break
    elif target < price[mid]:
        high = mid - 1
    else:
        low = mid + 1
Output

Product Found at Index 3

H3) IRCTC Waitlist Merger (Merge Sort)
Question

IRCTC has two separately sorted waitlists—one from its mobile app and one from railway counters.

To create one final sorted waitlist, both lists are merged together.

Write a Python program to merge two sorted lists.

Answer
list1 = [1, 3, 5]
list2 = [2, 4, 6]

result = list1 + list2
result.sort()

print("Merged List :", result)

Output

Merged List : [1, 2, 3, 4, 5, 6]