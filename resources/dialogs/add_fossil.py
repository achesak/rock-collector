# -*- coding: utf-8 -*-


# This file defines the Add Fossil dialog.


# Import GTK for the dialog.
from gi.repository import Gtk


class AddFossilDialog(Gtk.Dialog):
    """Shows the "Add Fossil" dialog."""
    
    def __init__(self, parent):
        """Create the dialog."""
        
        # This window should be modal.
        Gtk.Dialog.__init__(self, "Add Fossil", parent, Gtk.DialogFlags.MODAL)
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
        
        # Create the Age label and combobox.
        age_lbl = Gtk.Label("Age: ")
        age_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(age_lbl, loc_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.age_com = Gtk.ComboBoxText()
        for i in ["Unknown", "Archaean", "Proterozoic", "Cambrian", "Ordovician", "Silurian", "Devonian", "Carboniferous", "Permian", "Triassic", "Jurassic", "Cretaceous", "Paleogene", "Neogene", "Quaternary"]:
            self.age_com.append_text(i)
        self.age_com.set_active(0)
        new_grid.attach_next_to(self.age_com, age_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Species label and entry.
        spe_lbl = Gtk.Label("Species: ")
        spe_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(spe_lbl, age_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.spe_ent = Gtk.Entry()
        new_grid.attach_next_to(self.spe_ent, spe_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Genus label and entry.
        gen_lbl = Gtk.Label("Genus: ")
        gen_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(gen_lbl, spe_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.gen_ent = Gtk.Entry()
        new_grid.attach_next_to(self.gen_ent, gen_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Family label and entry.
        fam_lbl = Gtk.Label("Family: ")
        fam_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(fam_lbl, gen_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.fam_ent = Gtk.Entry()
        new_grid.attach_next_to(self.fam_ent, fam_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Order label and entry.
        ord_lbl = Gtk.Label("Order: ")
        ord_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(ord_lbl, fam_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.ord_ent = Gtk.Entry()
        new_grid.attach_next_to(self.ord_ent, ord_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Class label and entry.
        cla_lbl = Gtk.Label("Class: ")
        cla_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(cla_lbl, ord_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.cla_ent = Gtk.Entry()
        new_grid.attach_next_to(self.cla_ent, cla_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Phylum label and entry.
        phy_lbl = Gtk.Label("Phylum: ")
        phy_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(phy_lbl, cla_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.phy_ent = Gtk.Entry()
        new_grid.attach_next_to(self.phy_ent, phy_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Kingdom label and entry.
        kin_lbl = Gtk.Label("Kingdom: ")
        kin_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(kin_lbl, phy_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.kin_ent = Gtk.Entry()
        new_grid.attach_next_to(self.kin_ent, kin_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Create the Notes label and entry.
        note_lbl = Gtk.Label("Notes: ")
        note_lbl.set_alignment(0, 0.5)
        new_grid.attach_next_to(note_lbl, kin_lbl, Gtk.PositionType.BOTTOM, 1, 1)
        self.note_ent = Gtk.Entry()
        new_grid.attach_next_to(self.note_ent, note_lbl, Gtk.PositionType.RIGHT, 1, 1)
        
        # Show the dialog. The response gets handled by the function
        # in the main class.
        self.show_all()
