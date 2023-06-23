# Making Faces

Before there were emoji, there were emoticons, whereby text like `:)` was a happy face and text like `:(` was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called `faces.py`, implement a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 (otherwise known as a slightly smiling face) and any `:(` converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`. Be sure to call `main` at the bottom of your file.

## Hints
- Recall that `input` returns a `str`, <https://per docs.python.org/3/library/functions.html#input>.
- Recall that a `str` comes with quite a few methods, per <https://docs.python.org/3/library/stdtypes.html#string-methods>.
- An emoji is actually just a character, so you can quote it like any `str`, a la `"😐"`. And you can copy and paste the emoji from this page into your own code as needed.

## Before You Begin
Execute `cd` by itself in your terminal window. You should find that your terminal window’s prompt resembles the below:

		$
Next execute

		mkdir faces
to make a folder called faces in your codespace.

Then execute

		cd faces
to change directories into that folder. You should now see your terminal prompt as faces/ $. You can now execute

		code faces.py
to make a file called faces.py where you’ll write your program.

# How to Test
Here’s how to test your code manually. At the `faces/ $` prompt in your terminal: :

1. Run your program with python faces.py. Type Hello :) and press Enter. Your program should output: `Hello 🙂`
2. Run your program with python faces.py. Type Goodbye :( and press Enter. Your program should output: `Goodbye 🙁`
3. Run your program with python faces.py. Type Hello :) Goodbye :( and press Enter. Your program should output: `Hello 🙂 Goodbye 🙁`

# Commit your progran to GITHUB
At the `faces/ $` prompt in your terminal:

		git commit -m “[descriptive message]“
Commit all changes in the REPO

		git push 
Push all changes to the REPO