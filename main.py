import tkinter as tk
import ctypes
import win32api
import win32con
import win32gui

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(' Mira ')

        native_widht = self.winfo_screenwidth()
        native_height = self.winfo_screenheight()

        widht = 100
        height = 100

        x = (native_widht - widht) // 2
        y = (native_height - height) // 2

        self.geometry(f'{widht}x{height}+{x}+{y}')
        self.attributes('-topmost', True)
        # self.attributes('-fullscreen', True)
        self.overrideredirect(True)
        self.attributes('-transparentcolor', 'white')
        # self.wm_attributes('-disabled', True)
        self.make_window_click_through()

        x_centro = widht // 2
        y_centro = height // 2
        raio = 2

        canvas = tk.Canvas(self, width = widht, height = height, bg="white")
        canvas.create_oval(x_centro - raio, y_centro - raio, x_centro + raio, y_centro + raio, fill = "black")
        canvas.pack()

    def make_window_click_through(self):
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        # 0x00000020: WS_EX_TRANSPARENT
        # 0x00000080: WS_EX_LAYERED
        current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
        ctypes.windll.user32.SetWindowLongW(hwnd, -20, current_style | 0x00000020 | 0x00000080)

if __name__ == '__main__':
    app = App()
    app.mainloop()