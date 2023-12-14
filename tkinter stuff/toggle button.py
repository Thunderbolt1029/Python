import tkinter as tk

root = tk.Tk()

def toggle():
    if toggle_btn.config('relief')[-1] == 'sunken':
        toggle_btn.config(relief="raised")
    else:
        toggle_btn.config(relief="sunken")

toggle_btn = tk.Button(text="Toggle", width=12, relief="raised", command=toggle)
toggle_btn.pack(pady=5)

root.mainloop()
