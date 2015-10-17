# -*- coding: utf-8 -*-


# This file defines the functions for saving the application data.


# Import json for saving the data.
import json


def save_data(main_dir, rocks, minerals, fossils):
    """Saves the main data."""
    
    try:
        # Save the data files.
        rocks_file = open("%s/rocks.json" % main_dir, "w")
        json.dump(rocks, rocks_file)
        rocks_file.close()
        minerals_file = open("%s/minerals.json" % main_dir, "w")
        json.dump(minerals, minerals_file)
        minerals_file.close()
        fossils_file = open("%s/fossils.json" % main_dir, "w")
        json.dump(fossils, fossils_file)
        fossils_file.close()
        
    except IOError:
        # Show the error message if something happened, but continue.
        # This one is shown if there was an error writing to the files.
        print("Error saving data files (IOError).")
    
    except (TypeError, ValueError):
        # Show the error message if something happened, but continue.
        # This one is shown if there was an error with the data types.
        print("Error saving data files (TypeError or ValueError).")


def save_counters(conf_dir, rocks_count, minerals_count, fossils_count):
    """Saves the counters."""
    
    try:
        # Save the counter files.
        rocks_count_file = open("%s/rocks_counter" % conf_dir, "w")
        minerals_count_file = open("%s/minerals_counter" % conf_dir, "w")
        fossils_count_file = open("%s/fossils_counter" % conf_dir, "w")
        rocks_count_file.write(str(rocks_count))
        minerals_count_file.write(str(minerals_count))
        fossils_count_file.write(str(fossils_count))
        rocks_count_file.close()
        minerals_count_file.close()
        fossils_count_file.close()
        
    except IOError:
        # Show the error message if something happened, but continue.
        # This one is shown if there was an error writing to the files.
        print("Error saving counter files (IOError).")
    
    except (TypeError, ValueError):
        # Show the error message if something happened, but continue.
        # This one is shown if there was an error with the data types.
        print("Error saving counter files (TypeError or ValueError).")


def save_window(conf_dir, width, height):
    """Saves the configuration data."""
    
    try:
        # Save the window size.
        wins_file = open("%s/window_size" % conf_dir, "w")
        wins_file.write("%d\n%d" % (height, width))
        wins_file.close()
    
    except IOError:
        # Show the error message if something happened, but continue.
        # This one is shown if there was an error writing to the file.
        print("Error saving window size file (IOError).")
