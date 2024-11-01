# Mailing Assignment ICS3U0

## Overview

This program calculates the price of a parcel based on weight categories and displays it to the user. The assignment instructions can be found on [this document](https://docs.google.com/document/d/1-4Nd8E3EBB_kx5UjoOJ_iYRpRsbuNEji45VQ6OAyCBQ/edit?tab=t.0).

## Features

- Clear, centered title that is relevant to the program's function
- User-friendly prompt for input.
- Displays the final price in a formatted manner.
- User user-friendly error message when a valid positive integer is not inputted

## Logic

### Creating the Title
The title is set using the variable `title` but then the centered version of it is stored in the variable `new_title`. This new variable is then printed to display a centered title.

### Assessing User Input
1. The program first asks the user for their input to identify the weight of the parcel, defining a variable called `weight`.

2. Uses a set of `if` and `elif` statements in order to create multiple weight categories ranging from 0 - 100 grams . However, for weights greater than 100 grams, another method must be used to calculate the cost, rate included.

3. For weights greater than 100 grams, a variable named `extra_weight` is created which represents the weight left over after 100 grams is subtracted.

4. Now, since the rate is 25 sinas/50g over the limit, I must ensure that the program understands what increments of 50 are.

5. So, I set a new variable named `increment`. This takes the `extra_weight` variable and adds 49 to it, ensuring that it is at least equal to 50, if not more.

6. Next, floored division is performed by 50 in order to find the number of times `extra_weight` exceeds the 50g  increments. The quotient of this division problem will be the final value of the `increment` variable.

7. Rate is calculated by multiplying the variable `increment` with 25.

8. The final cost is the base price (in sinas) of `70 + increment`, which adds 25 sinas tothe base price for every 50g exceeding 100g

### User Error

The entire program, starting from the input statement on `line 10`, where the user inputs the weight, is place in a `try` and `except` in order to account for ny user errors. This program only accepts positive integers, and as such, will display an error message if a 