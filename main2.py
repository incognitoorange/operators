print("Welcome to World Bank")
name = input("Enter your name: ")
print("Welcome", name, "to the bank")

print("Enter the amount that you would like to withdraw")
amount = int(input("Enter the amount: "))

note1000 = amount // 1000
note500 = (amount % 1000) // 500
note200 = ((amount % 1000) % 500) // 200
note100 = (((amount % 1000) % 500) % 200) // 100
note50 = ((((amount % 1000) % 500) % 200) % 100) // 50
note20 = (((((amount % 1000) % 500) % 200) % 100) % 50) // 20
note10 = ((((((amount % 1000) % 500) % 200) % 100) % 50) % 20) // 10
note5  = (((((((amount % 1000) % 500) % 200) % 100) % 50) % 20) % 10) // 5

print("\nYou will receive:")
print("₦1000 notes:", note1000)
print("₦500 notes:", note500)
print("₦200 notes:", note200)
print("₦100 notes:", note100)
print("₦50 notes:", note50)
print("₦20 notes:", note20)
print("₦10 notes:", note10)
print("₦5 notes:", note5)
