import tkinter as tk
from tkinter import simpledialog

def get_answers(words):
    answers = {}
    for word in words:
        answer = simpledialog.askstring("Input", f"Enter a word for {word}:")
        answers[word] = answer
    return answers

def replace_words(story, words, answers):
    for word in words:
        story = story.replace(word, answers[word])
    return story

def main():
    with open("story.txt", "r") as f:
        story = f.read()

    words = []
    start_of_word = -1
    target_start = "<"
    target_end = ">"

    for i, char in enumerate(story):
        if char == target_start:
            start_of_word = i

        if char == target_end and start_of_word != -1:
            word = story[start_of_word:i + 1]
            words.append(word)
            start_of_word = -1

    answers = get_answers(words)

    modified_story = replace_words(story, words, answers)

    root = tk.Tk()
    root.title("Story Modifier")

    text_widget = tk.Text(root, wrap="word", height=15, width=50)
    text_widget.insert("1.0", modified_story)
    text_widget.config(state="disabled")
    text_widget.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()