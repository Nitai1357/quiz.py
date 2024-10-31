import random

# Quiz questions for list operations
questions = [
    {
        "question": "How do you add an element to the end of a list?",
        "options": ["A) list.add(element)", "B) list.insert(element)", "C) list.append(element)", "D) list.push(element)"],
        "answer": "C"
    },
    {
        "question": "Which method would you use to insert an element at a specific index in a list?",
        "options": ["A) list.append(index, element)", "B) list.insert(index, element)", "C) list.add(index, element)", "D) list.put(index, element)"],
        "answer": "B"
    },
    {
        "question": "What does the list.pop() function do?",
        "options": ["A) Removes the last element and returns it", "B) Adds an element to the list", "C) Removes the first element and returns it", "D) Deletes all elements in the list"],
        "answer": "A"
    },
    {
        "question": "How would you remove a specific element by value from a list?",
        "options": ["A) list.delete(element)", "B) list.remove(element)", "C) list.pop(element)", "D) list.clear(element)"],
        "answer": "B"
    },
    {
        "question": "What will `my_list[1:4]` return if `my_list = [10, 20, 30, 40, 50]`?",
        "options": ["A) [10, 20, 30]", "B) [20, 30, 40]", "C) [30, 40, 50]", "D) [20, 30, 40, 50]"],
        "answer": "B"
    },
    {
        "question": "Which method will you use to count occurrences of an element in a list?",
        "options": ["A) list.count(element)", "B) list.count()", "C) list.index(element)", "D) list.contains(element)"],
        "answer": "A"
    },
    {
        "question": "How can you reverse the elements in a list?",
        "options": ["A) list.reverse()", "B) reversed(list)", "C) list[::-1]", "D) All of the above"],
        "answer": "D"
    },
    {
        "question": "What does `list.clear()` do?",
        "options": ["A) Clears all elements from the list", "B) Clears the last element only", "C) Clears elements by value", "D) Clears elements by index"],
        "answer": "A"
    },
    {
        "question": "How do you combine two lists together?",
        "options": ["A) list1.add(list2)", "B) list1.append(list2)", "C) list1.extend(list2)", "D) list1.push(list2)"],
        "answer": "C"
    },
    {
        "question": "Which of these methods would you use to get the index of an element in a list?",
        "options": ["A) list.find(element)", "B) list.index(element)", "C) list.position(element)", "D) list.search(element)"],
        "answer": "B"
    }
]

def start_quiz(questions):
    score = 0
    random.shuffle(questions)  # Shuffle questions for random order
    print("Welcome to the Python List Operations Quiz!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    print("Thank you for playing!")

# Start the quiz
start_quiz(questions)
