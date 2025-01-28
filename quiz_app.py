import tkinter as tk
from tkinter import messagebox, font

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator")
        self.root.geometry("600x700")  # window size
        self.root.configure(bg="#f0f0f0")  # background color

        #fonts
        self.title_font = font.Font(family="Arial", size=16, weight="bold")
        self.label_font = font.Font(family="Arial", size=12)
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        self.feedback_label_font = font.Font(family="Arial", size=12, weight="bold")

        # Title Label
        self.title_label = tk.Label(root, text="Python Code Quiz Generator", font=self.title_font, bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Topic Input Frame with Border
        self.topic_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief="solid", padx=10, pady=10)
        self.topic_frame.pack(pady=10, fill="x", padx=20)

        self.topic_label = tk.Label(self.topic_frame, text="Enter Python Topic (e.g., loops, lists, strings):", font=self.label_font, bg="#f0f0f0", anchor="w")
        self.topic_label.pack(anchor="w")

        self.topic_entry = tk.Entry(self.topic_frame, font=self.label_font, width=40)
        self.topic_entry.pack(pady=5, anchor="w")

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Python Question", font=self.button_font, bg="#4CAF50", fg="white", command=self.generate_question)
        self.generate_button.pack(pady=10)

        # Question Display Frame with Border
        self.question_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief="solid", padx=10, pady=10)
        self.question_frame.pack(pady=10, fill="x", padx=20)

        self.question_label = tk.Label(self.question_frame, text="", font=self.label_font, bg="#f0f0f0", wraplength=500, anchor="w")
        self.question_label.pack(anchor="w")

        self.code_label = tk.Label(self.question_frame, text="", font=("Courier", 12), bg="#f0f0f0", anchor="w")
        self.code_label.pack(pady=10, anchor="w")

        # Options Frame with Border
        self.options_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief="solid", padx=10, pady=10)
        self.options_frame.pack(pady=10, fill="x", padx=20)

        self.option_var = tk.IntVar()
        self.option_buttons = []

        for i in range(4):
            option_frame = tk.Frame(self.options_frame, bg="#f0f0f0", bd=1, relief="solid", padx=5, pady=5)
            option_frame.pack(fill="x", pady=2)
            rb = tk.Radiobutton(option_frame, text="", variable=self.option_var, value=i, font=self.label_font, bg="#f0f0f0", anchor="w")
            rb.pack(side="left")
            self.option_buttons.append(rb)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", font=self.button_font, bg="#008CBA", fg="white", command=self.check_answer)
        self.submit_button.pack(pady=20)

        # Feedback Label
        self.feedback_label = tk.Label(root, text="", font=self.label_font, bg="#f0f0f0", fg="#4CAF50")
        self.feedback_label.pack()

        self.current_question = None

    def generate_question(self):
        topic = self.topic_entry.get().strip().lower()
        filtered_questions = [q for q in questions if q["topic"].lower() == topic]
        if filtered_questions:
            self.current_question = filtered_questions[0]
            self.question_label.config(text=self.current_question["question"])
            self.code_label.config(text=self.current_question["code"])
            for i, option in enumerate(self.current_question["options"]):
                self.option_buttons[i].config(text=option)
        else:
            messagebox.showinfo("Info", "No questions found for the given topic.")

    def check_answer(self):
        if self.current_question is not None:
            selected_option = self.option_var.get()
            if selected_option == self.current_question["answer"]:
                self.feedback_label.config(text="Correct! Well done!", fg="#4CAF50", font=self.feedback_label_font)
            else:
                self.feedback_label.config(text="Incorrect. Try again.", fg="#FF0000", font=self.feedback_label_font)
        else:
            messagebox.showinfo("Info", "Please generate a question first.")

if __name__ == "__main__":
    questions = [
        {
            "topic": "Loops",
            "question": "What will be the output of this Python code?",
            "code": "for i in range(3):\n    print(i)",
            "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
            "answer": 0  # Position in the options array (0-based index)
        },
        {
            "topic": "Lists",
            "question": "What will be the output of this Python code?",
            "code": "my_list = [1, 2, 3]\nprint(my_list[1])",
            "options": ["1", "2", "3", "Error"],
            "answer": 1
        },
        {
            "topic": "Strings",
            "question": "What will be the output of this Python code?",
            "code": "s = 'Hello'\nprint(s[1:3])",
            "options": ["He", "el", "lo", "el"],
            "answer": 3
        },
        {
            "topic": "Functions",
            "question": "What will be the output of this Python code?",
            "code": "def add(a, b):\n    return a + b\nprint(add(2, 3))",
            "options": ["5", "6", "23", "Error"],
            "answer": 0
        },
        {
            "topic": "Dictionaries",
            "question": "What will be the output of this Python code?",
            "code": "my_dict = {'a': 1, 'b': 2}\nprint(my_dict['b'])",
            "options": ["1", "2", "'b'", "Error"],
            "answer": 1
        }
    ]

    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()