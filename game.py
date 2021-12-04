"""Gues a number"""
import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input("Guess a number 1 - 100: "))
    
    if predict_number > number:
        print("Try a less number!")
        
    elif predict_number < number:
        print("Try a bigger number!")
        
    else:
        print(f"Congratulations!!! The number is {number} for {count} counts")
        break
    
    