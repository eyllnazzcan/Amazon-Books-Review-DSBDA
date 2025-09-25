#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
for parts in reader:
    if parts[0] == "product_id":  
        continue
    product_id = parts[0]
    star_rating = float(parts[2])
    review_date = parts[7][:7]  # yy-mm
    print(f"{product_id}\t{review_date}\t{star_rating}")
