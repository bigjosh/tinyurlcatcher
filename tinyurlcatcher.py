"""TinyURLCatcher - Displays URLs passed as command-line arguments."""

import sys
import tkinter as tk


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else None

    root = tk.Tk()
    root.title("TinyURLCatcher")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    window_width = 500
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    frame = tk.Frame(root, padx=15, pady=15)
    frame.pack(fill=tk.BOTH, expand=True)

    if url:
        tk.Label(frame, text="Captured URL:", anchor="w").pack(fill=tk.X)

        url_var = tk.StringVar(value=url)
        entry = tk.Entry(frame, textvariable=url_var, state="readonly", readonlybackground="white")
        entry.pack(fill=tk.X, pady=(5, 10))
        entry.select_range(0, tk.END)

        btn_frame = tk.Frame(frame)
        btn_frame.pack()

        status_var = tk.StringVar()
        status_label = tk.Label(frame, textvariable=status_var, fg="green")
        status_label.pack()

        def copy_to_clipboard():
            root.clipboard_clear()
            root.clipboard_append(url)
            status_var.set("Copied!")
            root.after(1500, lambda: status_var.set(""))

        tk.Button(btn_frame, text="Copy to Clipboard", command=copy_to_clipboard, width=16).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Close", command=root.destroy, width=10).pack(side=tk.LEFT, padx=5)
    else:
        tk.Label(frame, text="No URL provided.", anchor="center").pack(expand=True)
        tk.Button(frame, text="Close", command=root.destroy, width=10).pack(pady=(10, 0))

    root.mainloop()


if __name__ == "__main__":
    main()
