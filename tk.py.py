# import tkinter as tk
# from tkinter import simpledialog, messagebox

# homework_texts = {}

# def open_text_window(homework_number):
#     def save_text():
#         global homework_texts
#         content = text_area.get("1.0", tk.END)
#         homework_texts[homework_number] = content
#         with open(f"homework_{homework_number}.txt", 'w') as file:
#             file.write(content)
#         messagebox.showinfo("Saved", f"Homework {homework_number} saving!")

#     text_window = tk.Toplevel()
#     text_window.title(f"Homework {homework_number}")
#     # text_window.geometry("700x700")
#     text_area = tk.Text(text_window, width=80, height=20,bg=("#333333"),fg="red",font=("Arial"))
#     text_area.pack()

#     if homework_number in homework_texts:
#         text_area.insert(tk.END, homework_texts[homework_number])
#     else:
#         try:
#             with open(f'homework_{homework_number}.txt', 'r') as f:
#                 content = f.read()
#                 text_area.insert(tk.END, content)
#                 homework_texts[homework_number] = content
#         except FileNotFoundError:
#             messagebox.showwarning("File Not Found", f"Homework {homework_number} file not found!")

#     save_button = tk.Button(text_window, text="Save", command=save_text)
#     save_button.pack()

# root = tk.Tk()
# root.title("Python Homework 1")
# root.geometry("340x440")
# root.configure(bg="#333333")

# for i in range(1, 5):
#     hw_label = tk.Label(root, text=f"{i} - H.W", bg="#333333", fg="white", font=("Arial", 10))
#     hw_label.grid(row=i, column=0)
#     login_button = tk.Button(root, text="Open", bg="red", fg="white", font=("Arial", 8),
#                              command=lambda i=i: open_text_window(i))
#     login_button.grid(row=i, column=1, padx=8, pady=8)

# root.mainloop()


