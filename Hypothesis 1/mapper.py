#!/usr/bin/env python3
# mapper.py
# Input: CSV with columns (in this exact order):
# "product_id", "product_title", "star_rating", "helpful_votes", "total_votes", "review_headline", "review_body", "review_date"
# Output: lines "WORD-LABEL"
import sys
import csv
import re

STOPWORDS ={'a','an','the','and','or','but','if','then','else','when','is','are','was','were','be','been','has','have','had','do','does','did','of','in','on','for','with','as','by','at','from','that','this','these','those','it','its','they','them','he','she','we','you','your','i','me','my','mine','not','so','too','very','just','about','into','up','down','out','over','under','again','new','more','most','one','also','what','which','who','how','why','where','because','during','before','after','than','then'}

MIN_WORD_LEN = 3  # ignore words shorter than this

word_re = re.compile(r"[a-zA-Z']{2,}")

def tokenize(text):
    if not text:
        return []
    tokens = word_re.findall(text.lower())
    clean = []
    for t in tokens:
        t = t.strip("'")  # remove edge apostrophes
        if len(t) >= MIN_WORD_LEN and t not in STOPWORDS and not t.isdigit():
            clean.append(t)
    return clean

def main():
    reader = csv.reader(sys.stdin) # read one line at the time
    first = True
    for row in reader:
        # check to avoid empty lines
        if not row:
            continue
        # Skip header if present
        if first:
            first = False
            if len(row) >= 1 and row[0].strip().lower() == 'product_id':
                continue
        # check to ensure we have at least 8 columns
        if len(row) < 8:
            continue
        # star_rating converted as integer
        try:
            rating_raw = row[2].strip()
            rating = int(float(rating_raw))
        except:
            continue
        if rating in (4, 5):
            label = 'P'
        elif rating in (1, 2):
            label = 'N'
        else:
            # skip neutral 3-star reviews
            continue

        # combine headline + body (index 5 and 6)
        text = ''
        if row[5]:
            text += row[5] + ' '
        if row[6]:
            text += row[6]
        if not text.strip():
            continue

        for w in tokenize(text):
            # emit word and label
            print(f"{w}\t{label}")

# run the main function if the code is executed from terminal. 
# Otherwise, this code could be imported as an object in another code using "import mapper"
if __name__ == "__main__":
    main()