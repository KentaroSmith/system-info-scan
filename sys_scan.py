import psutil
from tkinter import *
from tkinter import ttk
import datetime
import os, platform, subprocess, re
import sys
import cpuinfo

root = Tk()
root.geometry("800x500")
root.title("System Diagnostic")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tab_control = ttk.Notebook(mainframe)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Hardware Info")



computer_name = platform.node()
os_details = platform.platform()
architecture_details = platform.machine()
#memory_details = psutil.virtual_memory()
memory_details = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
network_info = psutil.net_if_addrs()
partition_info = psutil.disk_partitions()
processor_info = cpuinfo.cpuinfo.get_cpu_info()['brand_raw']

ethernet_info = network_info['Ethernet'][0]


tab_one_data = [
    [computer_name, "Computer Name: "],
    [os_details, "OS Information: "],
    [architecture_details, "Architecture Details: "],
    [processor_info, "Processor Details: "],
    [memory_details, "Memory Details: "],
    [partition_info, "Partition Info: "],
    [ethernet_info], "Ethernet Info: "
]

def LineItem(tab, row_num, item_data, description):
    variables = []
    for item in tab_one_data:
        num = str(tab_one_data.index(item))
        data = "info"
        data_label = "display"
        variables = [data+num, data_label+num]
        
    variables[0] = ttk.Label(tab, text=item_data)
    variables[1] = Label(tab, text = description)
    variables[1].grid(column = 2, row = row_num)
    variables[0].grid(column = 3, row = row_num)

row_number = 2
for data in tab_one_data:

    LineItem(tab1, row_number, data[0], data[1])
    row_number += 1
""" computer_name = platform.node()
computer_name_info = ttk.Label(tab1, text=computer_name)
computer_name_display = Label(tab1, text="Computer Name: ")
computer_name_display.grid(column=2, row=2)
computer_name_info.grid(column=3, row=2)

os_details = platform.platform()
os_details_info = ttk.Label(tab1, text=os_details)
os_details_display = Label(tab1, text="OS Information: ")
os_details_display.grid(column=2, row=3)
os_details_info.grid(column=3, row=3)

architecture_details = platform.machine()
architecture_details_info = ttk.Label(tab1, text=architecture_details)
architecture_details_display = Label(tab1, text="Architecture Details: ")
architecture_details_display.grid(column=2, row=4)
architecture_details_info.grid(column=3, row=4) """



print(platform.machine())
print(platform.platform())
print(platform.uname())
print(platform.processor())
print(platform.architecture())
print(sys.getwindowsversion())
print(sys.version_info)
print(psutil.users())
print(psutil.cpu_count())
print(psutil.virtual_memory())
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.net_if_addrs())
#print(psutil.sensors_temperatures())

tab_control.pack(expand=1, fill = 'both')
root.mainloop()