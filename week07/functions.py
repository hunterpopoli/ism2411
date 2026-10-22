# Self-Assessment Questions
# 1. The first bug I spotted was the missing colon on line 10. I found it from simply observing the code when I first opened the file. This tells me that I know the easy basics of writing code and that I am able to spot basic mistakes like that.
# 2. apply_discount(price,tier) creates a blueprint for a function that you can later on simply type your parameters/inputs in it and use it for any various input you can apply to it. The inputs are the price of a product after each tier of discounts that you may apply to. It returns final discounted price based on your tier.
# 3. DISCLOSURE COMMENT: I used ChatGPT for the broken sales file for exercise 5. The AI was very helpful in explaining the errors in simple terms so that I can understand them and then continue to fix the errors myself.


# Exercise 1

# Define a calculate tax function

def calculate_tax(price,rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax(250,0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00

# Exercise 2

def apply_discount(price,tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price,tier):.2f}") # loop that prints all tiers and their prices

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(200,"gold") # used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 6

x = 100 # apple # Global

def double_it():
    x = 999 # another apple (not the same apple as above) # Local
    return x * 2

print(x)
print(double_it())
print(x)