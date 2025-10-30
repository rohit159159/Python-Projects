import psutil
import tkinter as tk
from tkinter import ttk
from plyer import notification

class BatteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔋 Battery Level Checker")
        self.root.geometry("625x625")
        self.root.configure(bg="#0a0a2a")
        self.root.resizable(False, False)
        tk.Label(
            root,
            text="Battery Level Checker",
            font=("Poppins", 18, "bold"),
            fg="#00ffcc",
            bg="#0a0a2a"
        ).pack(pady=15)
        
        self.percent_level=tk.Label(
            root,
            text="Battery Level: --%",font=("Poppins", 14, "bold"),
            fg="white", bg="#0a0a2a"
        ) 
        self.percent_level.pack(pady=10)
        self.status_level=tk.Label(
            root,
            text="Status: --%",font=("Poppins", 14, "bold"),
            fg="white", bg="#0a0a2a"
        )
        self.status_level.pack(pady=5)
        
        self.style=ttk.Style()
        self.style.configure("TProgressbar",
        thickness=25, troughcolor="#1a1a40", background="#00ff99")
        
        self.progress=ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate"
                                      , style="TProgressbar")
        self.progress.pack(pady=20)
        self.alert_shown=False
        self.update_battery_info()
        
    def update_battery_info(self):
        battery = psutil.sensors_battery()
        if battery is None:
            self.percent_level.config(text="No battery detected")
            return
        percent=battery.percent
        plugged=battery.power_plugged
        
        self.percent_level.config(text=f"Battery Level: {percent}%")
        self.status_level.config(text=f"Status: {'Plugged In 🔌' if plugged else'On Battery 🔋' }")
        self.progress["value"]=percent
        
        if percent<20:
            color="#ff4D4D"
        elif percent<50:
            color="#FFD700"
        else:
            color="#00FF99"
        self.style.configure("TProgressbar", background=color)
        
        if percent<50 and not self.alert_shown:
            notification.notify(title="⚠️ Battery Low Wrning", message=F"Battery is at{percent}%. Please plug in yor charger", timeout=6)
            self.alert_shown=True
        elif percent>=50:
            self.alert_shown=False
            
        self.root.after(10000, self.update_battery_info)
            
if __name__=="__main__":
    root=tk.Tk()
    app=BatteryApp(root)
    root.mainloop()