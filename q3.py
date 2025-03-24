# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

with open("romeo_and_juliet.txt", "r") as f:
    story = f.read()

# Count how many times the word "Juliet" appears
counter = 0
for word in story.split(" "):
    if "Juliet" in word:
        counter += 1

print(counter)