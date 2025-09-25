#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if len(row) < 8 or row[0] == "product_id":
        continue
    try:
        star = float(row[2])  # star_rating
        review = row[6]  # review_body
        length = len(review.split())  # word count
        print(f"{star}\t{length}")  # Emit star_rating and word count as a key-value pair
    except Exception as e:
        print(f"Error processing row: {row} | Error: {e}", file=sys.stderr)
        continue
