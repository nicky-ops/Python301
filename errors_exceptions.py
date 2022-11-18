num = input("Enter a number")
try:
    num = int(num)
except Exception:
    num = "Unknown"

print(num)