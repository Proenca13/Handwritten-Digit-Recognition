# src/app.py

import tkinter as tk
from PIL import Image, ImageDraw
from predict import predict_digit


class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognizer")

        # Create a PIL image to draw on
        self.image = Image.new("RGB", (280, 280), "black")
        self.draw_image = ImageDraw.Draw(self.image)

        # Canvas for drawing
        self.canvas = tk.Canvas(root, width=280, height=280, bg="black")
        self.canvas.pack(pady=10)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.draw)

        # Prediction label
        self.label_result = tk.Label(root, text="Draw a digit (0-9)", font=("Arial", 16))
        self.label_result.pack(pady=10)

        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.button_predict = tk.Button(button_frame, text="Predict",
                                        command=self.predict_digit,
                                        bg="green", fg="white", font=("Arial", 12))
        self.button_predict.pack(side="left", padx=10)

        self.button_clear = tk.Button(button_frame, text="Clear",
                                      command=self.clear_canvas,
                                      bg="red", fg="white", font=("Arial", 12))
        self.button_clear.pack(side="right", padx=10)

    def draw(self, event):
        x, y = event.x, event.y
        r = 12  # brush radius

        # Draw on canvas (for display)
        self.canvas.create_oval(x - r, y - r, x + r, y + r,
                                fill="white", outline="white")

        # Draw on PIL image (for prediction)
        self.draw_image.ellipse([x - r, y - r, x + r, y + r],
                                fill="white", outline="white")

    def clear_canvas(self):
        self.canvas.delete("all")
        # Clear the PIL image too
        self.image = Image.new("RGB", (280, 280), "black")
        self.draw_image = ImageDraw.Draw(self.image)
        self.label_result.config(text="Draw a digit (0-9)")

    def predict_digit(self):
        try:
            digit = predict_digit(self.image)
            self.label_result.config(
                text=f"Prediction: {digit}"
            )
        except Exception as e:
            self.label_result.config(text=f"Error: {str(e)}")
            print(f"Prediction error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = DigitRecognizerApp(root)
    root.mainloop()