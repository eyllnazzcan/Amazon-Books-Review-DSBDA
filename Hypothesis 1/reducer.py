#!/usr/bin/env python3
# reducer.py
# Input: lines "WORD-LABEL" sorted by word (Hadoop Streaming guarantees grouping)
# Output: "word | pos_count | neg_count | total | pos_ratio | neg_ratio"
import sys

current_word = None
pos = 0
neg = 0
MIN_TOTAL = 50  # filter rare words

header_printed = False  # flag to print header once

def flush(word, pos, neg):
    total = pos + neg
    if total >= MIN_TOTAL:
        pos_ratio = pos / total
        neg_ratio = neg / total
        print(f"{word}\t{pos}\t{neg}\t{total}\t{pos_ratio:.4f}\t{neg_ratio:.4f}")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    word, label = parts
    if current_word is None:
        current_word = word

    if word != current_word:
        if not header_printed:
            print("word\tpos_count\tneg_count\ttotal\tpos_ratio\tneg_ratio")
            header_printed = True
        # output previous, removing words that appears only in positive or negative reviews
        if pos > 0 and neg > 0:
            flush(current_word, pos, neg)
        # reset counters
        current_word = word
        pos = 0
        neg = 0

    if label == 'P':
        pos += 1
    elif label == 'N':
        neg += 1
    else:
        # ignore unknown labels
        pass

# flush last
if current_word is not None:
    flush(current_word, pos, neg)