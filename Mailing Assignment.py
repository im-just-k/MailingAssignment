# Mail Delivery Assignment
# Keyaan Wali Chowdhury

title = "<<    Mail Delivery Price Calculator    >>>" # Create a centered title
new_title = title.center(75)
print("\n"+ new_title)

try:
    weight = int(input("How heavy is the parcel in grams: "))
    if weight >= 0 and weight <= 30:
        price = 40
    elif weight > 30 and weight <= 50:
        price = 55
    elif weight > 50 and weight <= 100:
        price = 70
    elif weight > 100:
        extra_weight = weight - 100  # Find extra weight beyond 100 grams
    
        # Calculate the number of 50 g increments, rounding up
        increment = (extra_weight + 49) // 50  # Adding 49 ensures we round up for any remainder
    
        rate = increment * 25  # Calculate the rate
        price = 70 + rate  # Rate is added to the base price of 70
    
    print(f"The Price is \033[0;32m {price} \033[0;0m sinas for a parcel the weight of \033[0;32m {weight} \033[0;0m grams")
except:
    print("\033[0;31m", "Weight must be a valid positive integer", "\n")