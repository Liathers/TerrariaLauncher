from instances_handler import *
from launcher_handler import *

from random import randint, seed
from tkscrolledframe import ScrolledFrame
from tktooltip import ToolTip
import tkinter.ttk as ttk
from os import listdir
from tkinter import *
import logging

def identify_button(button_id):
    log_message(logging.WARNING, f"Instance Manager: instance {button_id} clicked")

def tab_instances_window(parent):
    log_message(logging.INFO, "Setup: Initialised instances window")

    scrollable = ScrolledFrame(parent, scrollbars="vertical", relief=FLAT)
    scrollable.pack(side="top", expand=1, fill="both")
    main_frame = scrollable.display_widget(Frame)

    Label(main_frame, text="").pack()

    check_folder_created()
    for x in listdir("./instances/"):
        instance = load_instance(x)
        add_instance(main_frame, instance[0], instance[1]["instance_id"], instance[1]["version"], instance[1]["last_used"], False)

    Label(main_frame, text="").pack()

def add_instance(parent, name, instance_id, version, last_used, selected):
    selected = False

    highlight_colour = "black"
    highlight_thickness = 1
    if selected:
        highlight_colour = "red"
        highlight_thickness = 3

    instance_frame = Frame(parent, highlightbackground=highlight_colour, highlightthickness=highlight_thickness)
    instance_frame.pack(padx=25, pady=5, fill=X)

    left_frame = Frame(instance_frame, highlightthickness=0)
    left_frame.grid(column=0, row=0)

    Button(instance_frame, text=version, state="disabled", relief=GROOVE, width=7, height=3).grid(column=0, row=0, padx=2, pady=2, sticky=W)

    Label(instance_frame, text=f"ID: instance_{instance_id}\n", fg="#E0E0E0").grid(column=3, row=0, sticky=NE)

    button = ttk.Button(instance_frame, text="Select Instance", width=14, command=lambda id=instance_id: identify_button(id))
    button.grid(column=3, row=0, sticky=SE)
    ToolTip(button, msg="Switch to the selected version", delay=1)

    if selected:
        button.config(state="disabled", text="Selected")

    #Best method ever to make frame custom size, I'll change it if I find an alternative
    Label(left_frame, text="                                                                                               ").grid(column=1, row=0)
    Label(left_frame, text=f"{name}").grid(column=1, row=0, padx=63, sticky=W)
    Label(left_frame, text=f"\n{last_used}", fg="#8E8E8E").grid(column=1, row=1, padx=63, sticky=W)