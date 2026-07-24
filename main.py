root = tk.Tk()
root.title("AI Sales Prediction")
root.geometry("420x320")
root.resizable(False, False)

title = tk.Label(
    root,
    text="AI Sales Prediction",
    font=("Arial", 18, "bold"),
    fg="darkblue"
)
title.pack(pady=10)

label = tk.Label(
    root,
    text="Enter Month:",
    font=("Arial", 12)
)
label.pack(pady=5)

entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20,
    justify="center"
)
entry.pack(pady=5)

predict_btn = tk.Button(
    root,
    text="Predict Revenue",
    command=predict,
    width=18,
    bg="green",
    fg="white"
)
predict_btn.pack(pady=8)

graph_btn = tk.Button(
    root,
    text="Show Graph",
    command=graph,
    width=18,
    bg="orange"
)
graph_btn.pack()

result = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    fg="blue"
)
result.pack(pady=15)