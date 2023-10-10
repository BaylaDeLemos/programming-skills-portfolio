"""
Chapter 5 Exercise 2: Glossary 

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.    
"""
glossary={
   'loop': 'Work through a collection of items, one at a time.',
   'list': 'A collection of items in a particular order.',
   'print': 'is used to send message or output to the screen.',
    'strings': 'are text enclosed in single or double quotes.',
    'boolean': 'can be represented as true or false.'
    }

print("\nLoop:",glossary["loop"],
      "\n\nList:",glossary["list"],
      "\n\nPrint:",glossary["print"],
      "\n\nStrings:",glossary["strings"],
      "\n\nBoolean:",glossary["boolean"])