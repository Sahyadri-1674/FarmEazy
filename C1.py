import tkinter as tk

root = tk.Tk()
root.title("36 Districts, 36 Crops!")
root.configure(bg='#FFA500')

frame = tk.Frame(root, bg='#FFA500')
frame.pack(fill='both', expand=True)

# create heading label
heading_label = tk.Label(frame, text="36 Districts, 36 Crops!", font=('Arial', 30, 'bold'))
heading_label.grid(row=0, column=0, columnspan=6, pady=20)

districts = ["Ahmednagar", "Akola", "Amravati", "Aurangabad", "Beed", "Bhandara", "Buldhana", "Chandrapur", "Dhule", "Gadchiroli", "Gondia", "Hingoli", "Jalgaon", "Jalna", "Kolhapur", "Latur", "Mumbai City", "Mumbai Suburban", "Nagpur", "Nanded", "Nandurbar", "Nashik", "Osmanabad", "Palghar", "Parbhani", "Pune", "Raigad", "Ratnagiri", "Sangli", "Satara", "Sindhudurg", "Solapur", "Thane", "Wardha", "Washim", "Yavatmal"]

# create images for each district
images = []
for district in districts:
    img = tk.PhotoImage(file=f"{district}.png")
    images.append(img)

# create function to display image in new frame
def display_image(img):
    image_frame = tk.Toplevel(root)
    image_frame.title("District Image")
    image_label = tk.Label(image_frame, image=img)
    image_label.pack(padx=10, pady=10)

# create buttons for each district
buttons = []
for i, district in enumerate(districts):
    row = i // 6 + 1
    col = i % 6
    btn = tk.Button(frame, text=district, width=12, height=2, font=('Arial', 12, 'bold'), bg='#000080', fg='white', highlightbackground='white', anchor='center')
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    buttons.append(btn)

# bind function to display image to each button
for i, btn in enumerate(buttons):
    img = images[i]
    btn.config(command=lambda img=img: display_image(img))

root.mainloop()
