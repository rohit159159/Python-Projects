import psutil
import tkinter as tk
from tkinter import ttk
from plyer import notification 

class SystemHealthChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("💻 System Health Checker")
        self.root.geometry("625x625")
        self.root.resizable(False, False)
        self.root.configure(bg="#0a0a2a")

        tk.Label(
            root, text="System Health Monitor",
            font=("Poppins", 18, "bold"), fg="#00FFCC", bg="#0a0a2a"
        ).pack(pady=15)

        self.cpu_label = tk.Label(root, text="CPU Usage: --%", font=("Poppins", 14),
                                  fg="white", bg="#0a0a2a")
        self.cpu_label.pack(pady=5)
        self.cpu_bar = ttk.Progressbar(root, length=350, mode="determinate")
        self.cpu_bar.pack(pady=5)

    
        self.ram_label = tk.Label(root, text="RAM Usage: --%", font=("Poppins", 14),
                                  fg="white", bg="#0a0a2a")
        self.ram_label.pack(pady=5)
        self.ram_bar = ttk.Progressbar(root, length=350, mode="determinate")
        self.ram_bar.pack(pady=5)

        self.disk_label = tk.Label(root, text="Disk Usage: --%", font=("Poppins", 14),
                                   fg="white", bg="#0a0a2a")
        self.disk_label.pack(pady=5)
        self.disk_bar = ttk.Progressbar(root, length=350, mode="determinate")
        self.disk_bar.pack(pady=5)

        self.status_label = tk.Label(
            root, text="", font=("Poppins", 13), fg="#00FF99", bg="#0a0a2a"
        )
        self.status_label.pack(pady=10)

        self.alert_shown = False
        self.update_stats()

    def update_stats(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage("/").percent

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.ram_label.config(text=f"RAM Usage: {ram_usage}%")
        self.disk_label.config(text=f"Disk Usage: {disk_usage}%")

        # Update bars
        self.cpu_bar["value"] = cpu_usage
        self.ram_bar["value"] = ram_usage
        self.disk_bar["value"] = disk_usage

        def get_color(value):
            if value < 50:
                return "#00FF99"  # green
            elif value < 80:
                return "#FFD700"  # yellow
            else:
                return "#FF4D4D"  # red

        color_cpu = get_color(cpu_usage)
        color_ram = get_color(ram_usage)
        color_disk = get_color(disk_usage)

 

        # Alerts
        if cpu_usage > 20 and not self.alert_shown:
            notification.notify(
                title="⚠️ High CPU Usage Alert!",
                message=f"CPU usage is at {cpu_usage}%. System may slow down.",
                timeout=5
            )
            self.status_label.config(text="⚠️ Warning: High CPU Usage!", fg="#FF4D4D")
            self.alert_shown = True
        elif cpu_usage <= 20:
            self.alert_shown = False
            self.status_label.config(text="System Running Smoothly ✅", fg="#00FF99")
        self.root.after(5000, self.update_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemHealthChecker(root)
    root.mainloop()
