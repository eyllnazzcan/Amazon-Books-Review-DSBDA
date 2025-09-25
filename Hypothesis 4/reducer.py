#!/usr/bin/env python3
import sys
from collections import defaultdict

sums = defaultdict(float)
counts = defaultdict(int)

for i, line in enumerate(sys.stdin):
    parts = line.strip().split("\t")
    if len(parts) != 3:
        continue 
    product_id, ym, rating = parts
    try:
        rating = float(rating)
    except ValueError:
        continue
    
    key = (product_id, ym)
    sums[key] += rating
    counts[key] += 1
    
    #if i < 20:
    #   print(f"DEBUG REDUCER: {product_id}\t{ym}\t{rating}", file=sys.stderr) 

for product_id, ym in sorted(sums.keys()):
    total = sums[(product_id, ym)]
    count = counts[(product_id, ym)]
    if count == 0:
        continue
    avg = total / count
    print(f"{product_id}\t{ym}\t{round(avg, 2)}")
