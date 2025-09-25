#!/usr/bin/env python3
import sys

current_star = None
total_len = 0
count = 0

for line in sys.stdin:
    try:
        star, length = line.strip().split("\t")
        star = float(star) 
        length = int(length)
        
        # If we are still on the same star, accumulate the values
        if current_star == star:
            total_len += length
            count += 1
        else:
            # When we encounter a new star_rating, output the result for the previous one
            if current_star is not None:
                # Output the average word count for the previous star rating
                print(f"{current_star}\t{total_len / count}")
            
            # Reset for the new star_rating
            current_star = star
            total_len = length
            count = 1
    except ValueError:
        # Handle any malformed lines, skipping over them
        continue

# Print the final result for the last star_rating
if current_star is not None:
    print(f"{current_star}\t{total_len / count}")
