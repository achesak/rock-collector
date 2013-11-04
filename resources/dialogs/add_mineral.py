# -*- coding: utf-8 -*-


# This file defines the Add Mineral dialog.


# Import GTK for the dialog.
from gi.repository import Gtk


class AddMineralDialog(Gtk.Dialog):
    """Shows the "Add Rock" dialog."""
    
    def __init__(self, parent):
        """Create the dialog."""
        
        # This window should be modal.
        Gtk.Dialog.__init__(self, "Add Mineral", parent, Gtk.DialogFlags.MODAL)
        # Don't allow the user to resize the window.
        self.set_resizable(False)
        
        # Add the buttons.
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.add_button("OK", Gtk.ResponseType.OK)
        
        # Create the grid.
        new_box = self.get_content_area()
        new_grid = Gtk.Grid()
        # Add the grid to the dialog's content area.
        new_box.add(new_grid)
        
        # Create the Date Collected label and calendar.
        date_lbl = Gtk.Label("Date Collected: ")
        date_lbl.set_alignment(0, 0.5)
        new_grid.add(date_lbl)
        self.date_cal = Gtk.Calendar()
        new_grid.attach_next_to(self.date_cal, date_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Location Found label and entry.
        loc_lbl = Gtk.Label("Location Found: ")
        loc_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(loc_lbl, date_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.loc_ent = Gtk.Entry()
        new_grid.attach_next_to(self.loc_ent, loc_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Name label and entry.
        name_lbl = Gtk.Label("Name: ")
        name_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(name_lbl, loc_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.name_ent = Gtk.Entry()
        new_grid.attach_next_to(self.name_ent, name_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Color label and entry.
        color_lbl = Gtk.Label("Color: ")
        color_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(color_lbl, name_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.color_ent = Gtk.Entry()
        new_grid.attach_next_to(self.color_ent, color_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Luster label and entry.
        lust_lbl = Gtk.Label("Luster: ")
        lust_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(lust_lbl, color_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.lust_ent = Gtk.Entry()
        new_grid.attach_next_to(self.lust_ent, lust_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Streak label and entry.
        streak_lbl = Gtk.Label("Streak: ")
        streak_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(streak_lbl, lust_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.streak_ent = Gtk.Entry()
        new_grid.attach_next_to(self.streak_ent, streak_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Hardness label and entry.
        hard_lbl = Gtk.Label("Hardness: ")
        hard_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(hard_lbl, streak_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        hard_adj = Gtk.Adjustment(lower = 0, upper = 10, step_increment = 1)
        self.hard_sbtn = Gtk.SpinButton(digits = 1, adjustment = hard_adj)
        self.hard_sbtn.set_numeric(False)
        self.hard_sbtn.set_value(0)
        new_grid.attach_next_to(self.hard_sbtn, hard_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Crystal Structure label and entry.
        struct_lbl = Gtk.Label("Crystal Structure: ")
        struct_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(struct_lbl, hard_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.struct_ent = Gtk.Entry()
        new_grid.attach_next_to(self.struct_ent, struct_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Specific Gravity label and entry.
        sgrav_lbl = Gtk.Label("Specific Gravity: ")
        sgrav_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(sgrav_lbl, struct_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        sgrav_adj = Gtk.Adjustment(lower = 0, upper = 50, step_increment = 1)
        self.sgrav_sbtn = Gtk.SpinButton(digits = 2, adjustment = sgrav_adj)
        self.sgrav_sbtn.set_numeric(False)
        self.sgrav_sbtn.set_value(0)
        new_grid.attach_next_to(self.sgrav_sbtn, sgrav_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Streak label and entry.
        cleav_lbl = Gtk.Label("Cleavage: ")
        cleav_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(cleav_lbl, sgrav_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.cleav_ent = Gtk.Entry()
        new_grid.attach_next_to(self.cleav_ent, cleav_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Notes label and entry.
        note_lbl = Gtk.Label("Notes: ")
        note_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(note_lbl, cleav_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.note_ent = Gtk.Entry()
        new_grid.attach_next_to(self.note_ent, note_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Show the dialog. The response gets handled by the function
        # in the main class.
        self.show_all()
