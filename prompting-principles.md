# Principles of Prompting

## Principle 1: Write clear and specific instructions

### Tactic 1. Use delimiters such as triple quotes ("""), triple bacticks (```), triple dashes (---), angle brackets (<>), or XML tags (`<tag></tag>`) 
```
Example: 
Summarize the below paragraph delimited by three dashes.

---
{text}
```

### Tactic 2. Ask for structued output.
```
Example: 
Generate a list of three made-up book titles along with their authors and genres. Provide them in JSON format with the following keys: book_id, title, author, genre.
```

### Tactic 3. Check wether conditions are satisfied.
```
Example: 
Check the paragraph for a sequence of instructions. If there are none, reply with "no instructions found".
```

### Tactic 4. Few-shot prompting by providing successful examples of completing tasks then ask model to perform the task.
```
Example: 
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
```

## Principle 2: Give the model time to think

### Tactic 1. Specify the steps to complete a task.
```
Example:

```
