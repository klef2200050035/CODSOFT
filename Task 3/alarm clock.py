import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import winsound
import threading
import datetime


class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock App")

        self.current_time_var = tk.StringVar()
        self.current_date_var = tk.StringVar()
        self.alarms = []

        self.create_widgets()
        self.update_current_time()
        self.check_alarms()

    def create_widgets(self):
        # Current Time and Date Display
        current_time_label = ttk.Label(self.root, textvariable=self.current_time_var, font=('Helvetica', 24))
        current_time_label.pack(pady=20)

        current_date_label = ttk.Label(self.root, textvariable=self.current_date_var, font=('Helvetica', 16))
        current_date_label.pack()

        # New Alarm Setting
        alarm_frame = ttk.Frame(self.root, padding=(20, 20, 20, 0))
        alarm_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(alarm_frame, text="Set New Alarm", font=('Helvetica', 16)).pack()

        self.alarm_time_var = tk.StringVar()
        self.alarm_time_picker = ttk.Entry(alarm_frame, textvariable=self.alarm_time_var, font=('Helvetica', 14))
        self.alarm_time_picker.pack(pady=10)

        ttk.Label(alarm_frame, text="Choose Alarm Tone", font=('Helvetica', 14)).pack()

        self.alarm_tone_var = tk.StringVar()
        self.alarm_tone_select = ttk.Combobox(alarm_frame, textvariable=self.alarm_tone_var,
                                              values=['Tone 1', 'Tone 2', 'Tone 3'], font=('Helvetica', 12))
        self.alarm_tone_select.pack(pady=10)

        set_alarm_button = ttk.Button(alarm_frame, text="Set Alarm", command=self.set_alarm)
        set_alarm_button.pack(pady=10)

        # Alarm Management
        alarm_management_frame = ttk.Frame(self.root, padding=(20, 20))
        alarm_management_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(alarm_management_frame, text="Manage Alarms", font=('Helvetica', 16)).pack()

        self.alarms_listbox = tk.Listbox(alarm_management_frame, height=6, font=('Helvetica', 12))
        self.alarms_listbox.pack(pady=10)

        toggle_alarm_button = ttk.Button(alarm_management_frame, text="Toggle Alarm", command=self.toggle_alarm)
        toggle_alarm_button.pack(pady=10)

    def update_current_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        self.current_time_var.set(current_time)
        self.current_date_var.set(current_date)
        self.root.after(1000, self.update_current_time)

    def set_alarm(self):
        alarm_time = self.alarm_time_var.get()
        alarm_tone = self.alarm_tone_var.get()
        self.alarms.append({'time': alarm_time, 'tone': alarm_tone, 'enabled': True})
        self.update_alarms_listbox()

    def update_alarms_listbox(self):
        self.alarms_listbox.delete(0, tk.END)
        for index, alarm in enumerate(self.alarms):
            self.alarms_listbox.insert(tk.END,
                                       f"Alarm {index + 1}: {alarm['time']} - {alarm['tone']} {'(Enabled)' if alarm['enabled'] else '(Disabled)'}")

    def toggle_alarm(self):
        selected_index = self.alarms_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.alarms[index]['enabled'] = not self.alarms[index]['enabled']
            self.update_alarms_listbox()

    def check_alarms(self):
        now = datetime.datetime.now().strftime("%H:%M")
        for alarm in self.alarms:
            if alarm['time'] == now and alarm['enabled']:
                threading.Thread(target=self.ring_alarm, args=(alarm['tone'],)).start()
        self.root.after(60000, self.check_alarms)  # Check alarms every minute

    def ring_alarm(self, tone):
        messagebox.showinfo("Alarm", f"Alarm is ringing with {tone} tone!")
        # Adjust path accordingly for your alarm tones
        if tone == 'Tone 1':
            winsound.PlaySound(r'C:\Users\vijay\OneDrive\Desktop\TASK_3\tone1.mp3',
                               winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif tone == 'Tone 2':
            winsound.PlaySound(r'C:\Users\vijay\OneDrive\Desktop\TASK_3\tone2.mp3',
                               winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif tone == 'Tone 3':
            winsound.PlaySound(r'C:\Users\vijay\OneDrive\Desktop\TASK_3\tone3.mp3',
                               winsound.SND_FILENAME | winsound.SND_ASYNC)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
