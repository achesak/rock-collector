# -*- coding: utf-8 -*-


# This file defines the functions for launching and setting up the application.


# Import json for loading and saving the data.
import json
# Import platform for getting the user's operating system.
import platform
# Import os for creating a directory and other tasks.
import os
# Import os.path for seeing if a directory exists and other tasks.
import os.path
# Import sys for closing the application.
import sys


def get_main_dir():
    """Returns the main directory."""
    
    # The main directory is C:\.rock_collector on Windows,
    # and /home/[username]/.share/local/rock_collector for data files,
    # and /home/[username]/.config/rock_collector/ for configuration files on Linux.
    if platform.system().lower() == "windows":
        return "C:\\.rock_collector", "C:\\.rock_collector"
    else:
        base = os.path.expanduser("~")
        return base + "/.local/share/rock_collector", base + "/.config/rock_collector"


def check_files_exist(main_dir, conf_dir):
    """Checks to see if the base files exist, and create them if they don't."""
    
    # Check to see if the data directory exists, and create it if it doesn't.
    if not os.path.exists(main_dir) or not os.path.isdir(main_dir):
        
        # Create the directory.
        os.makedirs(main_dir)
        
        # Create the data files.
        init_file1 = open("%s/rocks.json" % main_dir, "w")
        init_file1.write("[]")
        init_file1.close()
        init_file2 = open("%s/minerals.json" % main_dir, "w")
        init_file2.write("[]")
        init_file2.close()
        init_file3 = open("%s/fossils.json" % main_dir, "w")
        init_file3.write("[]")
        init_file3.close()
    
    # Check to see if the configuration directory exists, and create it if it doesn't.
    if not os.path.exists(conf_dir) or not os.path.isdir(conf_dir):
        
        # Create the directory.
        os.makedirs(conf_dir)
        
        # Create the configuration files.
        init_file4 = open("%s/rocks_counter" % conf_dir, "w")
        init_file4.write("1")
        init_file4.close()
        init_file5 = open("%s/minerals_counter" % conf_dir, "w")
        init_file5.write("1")
        init_file5.close()
        init_file6 = open("%s/fossils_counter" % conf_dir, "w")
        init_file6.write("1")
        init_file6.close()
        init_file7 = open("%s/window_size" % conf_dir, "w")
        init_file7.write("1000\n500")
        init_file7.close()
    

def load_data_files(main_dir):
    """Loads the data files."""
    
    try:
        
        # Load the data files.
        rocks_file = open("%s/rocks.json" % main_dir, "r")
        rocks = json.load(rocks_file)
        rocks_file.close()
        minerals_file = open("%s/minerals.json" % main_dir, "r")
        minerals = json.load(minerals_file)
        minerals_file.close()
        fossils_file = open("%s/fossils.json" % main_dir, "r")
        fossils = json.load(fossils_file)
        fossils_file.close()    
        
    except IOError:
        # Show the error message, and close the application.
        # This one shows if there was a problem reading the file.
        print("Error reading data files (IOError).")
        sys.exit()
    
    return rocks, minerals, fossils


def load_counter_files(conf_dir):
    """Loads the counter files."""

    try:
        
        # Load the counters.
        rocks_count_file = open("%s/rocks_counter" % conf_dir, "r")
        rocks_count = int(rocks_count_file.read().rstrip())
        rocks_count_file.close()
        minerals_count_file = open("%s/minerals_counter" % conf_dir, "r")
        minerals_count = int(minerals_count_file.read().rstrip())
        minerals_count_file.close()
        fossils_count_file = open("%s/fossils_counter" % conf_dir, "r")
        fossils_count = int(fossils_count_file.read().rstrip())
        fossils_count_file.close()
        
    except IOError:
        # Show the error message, and close the application.
        # This one shows if there was a problem reading the file.
        print("Error reading counter files (IOError).")
        sys.exit()
    
    return rocks_count, minerals_count, fossils_count


def load_conf_files(conf_dir):
    """Loads the configuration files."""

    try:
        
        # Load the window size.
        window_size_file = open("%s/window_size" % conf_dir, "r")
        window_size = window_size_file.read().rstrip().split("\n")
        window_width = int(window_size[0])
        window_height = int(window_size[1])
        window_size_file.close()  
        
    except IOError:
        # Show the error message, and close the application.
        # This one shows if there was a problem reading the file.
        print("Error reading configuration files (IOError).")
        sys.exit()
    
    return window_width, window_height
