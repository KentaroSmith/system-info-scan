from tkinter import *
from tkinter import ttk, Text
import os, platform, subprocess, re, socket, sys, cpuinfo, psutil, datetime, openpyxl

root = Tk()
root.geometry("800x500")
root.title("System Diagnostic")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
style = ttk.Style()
style.configure('tab.background', background = "white")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tab_control = ttk.Notebook(mainframe)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Hardware Info")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Log Entry")
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text = "Initial Setup")
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text = "Software")

wb = openpyxl.load_workbook("log.xlsx")



computer_name = platform.node()
os_details = platform.platform()
architecture_details = platform.machine()
#memory_details = psutil.virtual_memory()
memory_details = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
network_info = psutil.net_if_addrs()
partition_info = psutil.disk_partitions()
processor_info = cpuinfo.cpuinfo.get_cpu_info()['brand_raw']
today = datetime.date.today().__format__("%m-%d-%Y")
time = datetime.datetime.now().time().__format__("%H:%M")

if network_info.get('Ethernet') ==True:
    ethernet_info = network_info['Ethernet'][0]
else:
    ethernet_info = False
user = StringVar("")
notes = Text(tab2, height = 3, width = 50, wrap = WORD)
location = StringVar("")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
current_ip = s.getsockname()[0]
s.close()

#Initial setup items
arc_gis = IntVar()
foxit_phantom = IntVar()
cis_infinity = IntVar()
bluebeam = IntVar()
lansweeper_agent = IntVar()
arc_pro = IntVar()
autocad = IntVar()
lucity_desktop = IntVar()
serial_number = StringVar()
manufacturer = StringVar()
model = StringVar()
inventory_year = datetime.date.today().__format__("%Y")
inventory_year = datetime.date.today().__format__("%m")
description = StringVar()

tab_one_data = [
    [computer_name, "Computer Name: "],
    [os_details, "OS Information: "],
    [architecture_details, "Architecture Details: "],
    [processor_info, "Processor Details: "],
    [memory_details, "Memory Details: "],
    [partition_info, "Partition Info: "],
    [ethernet_info, "Ethernet Info: "],
    [current_ip, "Current Address"]
]

tab_two_data = [
    [computer_name, "Computer Name: "],
    [os_details, "OS Information: "],
    [processor_info, "Processor Details: "],
    [memory_details, "Memory Details: "],
    [current_ip, "Current Address"],
    [today, "Today's Date"],
    [time, "Time"],
    [user, "User"],
    [location, "Location"],
    [notes, "Notes"]
]

tab_three_data = [
    [serial_number, "Serial Number"],
    [manufacturer, "Manufacturer"],
    [model, "Model"],
    [description, "Description"]
]

tab_four_data = [
    [arc_gis, "Arc GIS"],
    [foxit_phantom, "Foxit Phantom"],
    [cis_infinity, "CIS Infinity"],
    [bluebeam, "Bluebeam"],
    [lansweeper_agent, "LAN Sweeper Agent"],
    [arc_pro, "ArcGIS Pro"],
    [autocad, "AutoCAD"],
    [lucity_desktop, "Lucity Desktop"]
]

for info in network_info:
    temp_list = [network_info[str(info)][1][1], info]
    tab_one_data.append(temp_list)
#Save function
def new_device(*args):
    ws = wb["new_inventory"]
    row = ws.max_row + 1
    for column in "A":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = computer_name
    for column in "B":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = "Y"
    for column in "C":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = manufacturer.get()#Manufacurer 
    for column in "D":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = model.get()#Model Type
    for column in "E":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = description.get()#Chasis type
    for column in "F":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = serial_number.get()#Serial number
    for column in "H":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = user.get()
    for column in "I":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = location.get()
    for column in "Q":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = str(arc_gis.get())
    for column in "U":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = str(foxit_phantom.get())
    for column in "X":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = str(bluebeam.get())
    for column in "Y":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = str(lansweeper_agent.get())
    wb.save(filename="log.xlsx")

def maint_log(*args):
    ws = wb["repair_notes"]
    row = ws.max_row + 1
    for column in "A":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = computer_name
    for column in "B":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = os_details
    for column in "C":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = processor_info
    for column in "D":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = memory_details
    for column in "E":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = current_ip
    for column in "F":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = today
    for column in "G":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = time
    for column in "H":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = location.get()
    for column in "I":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = notes.get("1.0", "end-1c")
    for column in "J":
        cell_name = "{}{}".format(column, row)
        ws[cell_name] = user.get()
    wb.save(filename="log.xlsx")

def LineItem(tab, tab_data, row_num, item_data, description):
    variables = []
    for item in tab_data:
        num = str(tab_data.index(item))
        data = "info"
        data_label = "display"
        variables = [data+num, data_label+num]
    if tab == tab1:    
        variables[0] = ttk.Label(tab, text=item_data)
        variables[1] = Label(tab, text = description)
        variables[1].grid(column = 2, row = row_num)
        variables[0].grid(column = 3, row = row_num)
    elif tab == tab2:
        if description == "Notes":
            variables[0] = notes
        else:
            variables[0] = ttk.Entry(tab, textvariable=item_data, width = 50)
        variables[1] = Label(tab, text = description, justify=RIGHT)
        variables[1].grid(column = 2, row = row_num)
        variables[0].grid(column = 3, row = row_num)
        if item_data == notes:
            pass
        else:
            variables[0].delete(0, END)
            variables[0].insert(0, item_data)
    elif tab == tab3:
        variables[0] = ttk.Entry(tab, textvariable=item_data, width = 50)
        variables[1] = Label(tab, text = description)
        variables[1].grid(column = 2, row = row_num)
        variables[0].grid(column = 3, row = row_num)
    else:
        variables[0] = ttk.Checkbutton(tab, variable=item_data, onvalue = 1, offvalue = 0 )
        variables[1] = Label(tab, text = description)
        variables[1].grid(column = 2, row = row_num)
        variables[0].grid(column = 3, row = row_num)


def tab_display(tab, tab_data):
    row_number = 2
    for data in tab_data:
        LineItem(tab, tab_data, row_number, data[0], data[1])
        row_number += 1

tab_display(tab1, tab_one_data)
tab_display(tab2, tab_two_data)
tab_display(tab3, tab_three_data)
tab_display(tab4, tab_four_data)
ttk.Button(tab2, text="Save Data", command=maint_log).grid(column = 2, row = 15, sticky = E)
ttk.Button(tab3, text="Save Data", command=new_device).grid(column = 2, row = 15, sticky = E)

""" print(platform.machine())
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
print(psutil.net_if_addrs()) """
#print(psutil.sensors_temperatures())

tab_control.pack(expand=1, fill = 'both')
root.mainloop()