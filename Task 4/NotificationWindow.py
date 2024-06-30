import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class NotificationWindow:
    def __init__(self, title, message, image_path=None):
        self.root = tk.Toplevel()
        self.root.title(title)
 
        self.message_label = ttk.Label(self.root, text=message, wraplength=300, font=('Helvetica', 12))
        self.message_label.pack(padx=20, pady=10)

        if image_path:
            try:
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)
                self.image_label = ttk.Label(self.root, image=photo)
                self.image_label.image = photo
                self.image_label.pack(pady=10)

                # Update the root to properly display the image
                self.root.update()
            except IOError:
                messagebox.showwarning("Image Error", "Unable to load image!")

        close_button = ttk.Button(self.root, text="Close", command=self.root.destroy)
        close_button.pack(pady=10)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Example usage
    title = "Notification"
    message = "This is a sample notification message."
    image_path = r"C:\Users\vijay\OneDrive\Desktop\TASK_4\image.png"

    notification = NotificationWindow(title, message, image_path)
    notification.run()
