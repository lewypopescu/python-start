import re

string = "Hello, hello, hello World! 1234"

print("Hello" in string)

pattern = re.compile("hello")
# Using re.compile to create a regex pattern
a = pattern.search(string, re.IGNORECASE)
if a:
    print(f"Found '{a.group()}' at position {a.start()}-{a.end()}")

b = pattern.findall(string)
if b:
    print(f"All matches: {b}")

c = pattern.fullmatch(string)
if c:
    print(f"Full match: {c.group()}")

d = pattern.match(string)
if d:
    print(f"Match at start: {d.group()}")


def main():
    # Example of a simple regex pattern
    pattern = r'\d+'  # Matches one or more digits
    text = "There are 123 apples and 456 oranges."

    # Find all matches in the text
    matches = re.findall(pattern, text)
    print(f"Matches found: {matches}")

    # Example of using regex to replace text
    replaced_text = re.sub(pattern, 'X', text)
    print(f"Replaced text: {replaced_text}")


main()
