import os
import re
from collections import Counter
import socket

DATA_PATH = "/home/data"
OUTPUT_PATH = "/home/data/output"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def read_file(filename):
    with open(os.path.join(DATA_PATH, filename), "r", encoding="utf-8") as f:
        return f.read()

def clean_and_split(text, split_contractions=False):
    if split_contractions:
        text = re.sub(r"(\w+)'(\w+)", r"\1 \2", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.lower().split()
    return words

# Read files
if_text = read_file("IF.txt")
always_text = read_file("AlwaysRememberUsThisWay.txt")

# Count words
if_words = clean_and_split(if_text)
always_words = clean_and_split(always_text, split_contractions=True)

if_count = len(if_words)
always_count = len(always_words)
grand_total = if_count + always_count

# Top 3 in IF.txt
if_top3 = Counter(if_words).most_common(3)

# Top 3 in AlwaysRememberUsThisWay.txt
always_top3 = Counter(always_words).most_common(3)

# Get IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Write results
result_path = os.path.join(OUTPUT_PATH, "result.txt")

with open(result_path, "w") as f:
    f.write(f"Word count in IF.txt: {if_count}\n")
    f.write(f"Word count in AlwaysRememberUsThisWay.txt: {always_count}\n")
    f.write(f"Grand total word count: {grand_total}\n\n")

    f.write("Top 3 words in IF.txt:\n")
    for word, count in if_top3:
        f.write(f"{word}: {count}\n")

    f.write("\nTop 3 words in AlwaysRememberUsThisWay.txt:\n")
    for word, count in always_top3:
        f.write(f"{word}: {count}\n")

    f.write(f"\nContainer IP Address: {ip_address}\n")

# Print output before exit
with open(result_path, "r") as f:
    print(f.read())
