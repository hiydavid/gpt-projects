# Principles of Prompting

## Principle 1: Write clear and specific instructions

### Tactic 1. Use delimiters.
```
Example: 
Summarize the below paragraph delimited by the triple quotes.

"""
{text}
"""
```

### Tactic 2. Ask for structued output.
```
Example: 
Generate a list of three made-up book titles along with their authors and genres. 
Provide them in JSON format with the following keys: book_id, title, author, genre.
```

### Tactic 3. Check wether conditions are satisfied.
```
Example: 
Check the paragraph for a sequence of instructions. If there are none, reply with 
"no instructions found".
```

### Tactic 4. Few-shot prompting.
```
Example: 
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest valley flows from a modest spring; 
the grandest symphony originates from a single note; the most intricate tapestry 
begins with a solitary thread.

<child>: Teach me about resilience.
```

## Principle 2: Give the model time to think

### Tactic 1. Specify the steps to complete a task.
```
Example:
Perform the following actions:

1 - Summarize the following text delimited by triple quotes with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a JSON object that contains the following keys: french_summary, num_names.

Separate your answers with line breaks.

"""
{text}
"""
```

### Tactic 2. Instruct the model to work out its own solutions before rushing to a conclusion.
```
Example:
Your task is to determine if the student's solution is correct of not. To solve the 
problem do the following:

1 - Work out your own solution to the problem.
2 - Compare your solution to the student's solution and evaluate if the student's solution
is correct or not. Don't decide if the student's solution is correct until you have done
the problem yourself.
```

