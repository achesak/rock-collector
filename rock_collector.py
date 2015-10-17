# -*- coding: utf-8 -*-


################################################################################

# Rock Collector
# Version 0.1

# Rock Collector is an application for managing a geology collection.

# Released under the MIT open source license:
license_text = """
Copyright (c) 2013-2015 Adam Chesak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

################################################################################


# Import any needed modules.
# Import Gtk and Gdk for the interface.
from gi.repository import Gtk, Gdk, GdkPixbuf
# Import json for parsing and saving the data.
import json
# Import sys for closing the application.
import sys
# Import webbrowser for opening the help in the user's web browser.
import webbrowser
# Import os for various things.
import os
# Import platform for getting the user's OS.
import platform

# Tell Python not to create bytecode files, as they mess with the git repo.
# This line can be removed be the user, if desired.
sys.dont_write_bytecode = True

# Import the application's UI data.
from resources.ui import VERSION, TITLE, MENU_DATA
# Import the functions for setting up the application.
import resources.launch as launch
# Import the functions for saving application data.
import resources.save as save
# Import the dialog for adding a rock to the collection.
from resources.dialogs.add_rock import AddRockDialog
# Import the dialog for adding a mineral to the collection.
from resources.dialogs.add_mineral import AddMineralDialog
# Import the dialog for adding a fossil to the collection.
from resources.dialogs.add_fossil import AddFossilDialog


class RockCollector(Gtk.Window):
    """Create the application class."""

    def __init__(self):
        """Create the application."""
        
        # Get the data and configuration directories.
        self.main_dir, self.conf_dir = launch.get_main_dir()
        launch.check_files_exist(self.main_dir, self.conf_dir)
        
        # Load the data and configuration variables.
        self.rocks, self.minerals, self.fossils = launch.load_data_files(self.main_dir)
        self.rocks_count, self.minerals_count, self.fossils_count = launch.load_counter_files(self.conf_dir)
        self.window_width, self.window_height = launch.load_conf_files(self.conf_dir)
        
        # Create the interface.
        self.create_interface()
    
    
    def create_interface(self):
        """Creates the application interface."""
        
        # Create the window.
        Gtk.Window.__init__(self, title = TITLE)
        self.set_default_size(self.window_width, self.window_height)
        self.set_icon_from_file("resources/images/icon.png")
        
        # Create the ListStores.
        self.rock_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str)
        self.mineral_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str)
        self.fossil_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str, str)
        
        # Create the notebook.
        notebook = Gtk.Notebook()
        notebook.set_tab_pos(Gtk.PositionType.TOP)
        rock_lbl = Gtk.Label("Rocks")
        mineral_lbl = Gtk.Label("Minerals")
        fossil_lbl = Gtk.Label("Fossils")
        
        # Create the TreeView for displaying the rock data
        self.rock_view = Gtk.TreeView(model = self.rock_list)
        rock_id_text = Gtk.CellRendererText()
        self.rock_id_col = Gtk.TreeViewColumn("ID", rock_id_text, text = 0)
        self.rock_view.append_column(self.rock_id_col)
        rock_date_text = Gtk.CellRendererText()
        self.rock_date_col = Gtk.TreeViewColumn("Date Collected", rock_date_text, text = 1)
        self.rock_view.append_column(self.rock_date_col)
        rock_loc_text = Gtk.CellRendererText()
        self.rock_loc_col = Gtk.TreeViewColumn("Location Found", rock_loc_text, text = 2)
        self.rock_view.append_column(self.rock_loc_col)
        rock_name_text = Gtk.CellRendererText()
        self.rock_name_col = Gtk.TreeViewColumn("Name", rock_name_text, text = 3)
        self.rock_view.append_column(self.rock_name_col)
        rock_type_text = Gtk.CellRendererText()
        self.rock_type_col = Gtk.TreeViewColumn("Type", rock_type_text, text = 4)
        self.rock_view.append_column(self.rock_type_col)
        rock_color_text = Gtk.CellRendererText()
        self.rock_color_col = Gtk.TreeViewColumn("Color", rock_color_text, text = 5)
        self.rock_view.append_column(self.rock_color_col)
        rock_tex_text = Gtk.CellRendererText()
        self.rock_tex_col = Gtk.TreeViewColumn("Texture", rock_tex_text, text = 6)
        self.rock_view.append_column(self.rock_tex_col)
        rock_struc_text = Gtk.CellRendererText()
        self.rock_struc_col = Gtk.TreeViewColumn("Structure", rock_struc_text, text = 7)
        self.rock_view.append_column(self.rock_struc_col)
        rock_hard_text = Gtk.CellRendererText()
        self.rock_hard_col = Gtk.TreeViewColumn("Hardness", rock_hard_text, text = 8)
        self.rock_view.append_column(self.rock_hard_col)
        rock_note_text = Gtk.CellRendererText()
        self.rock_note_col = Gtk.TreeViewColumn("Notes", rock_note_text, text = 9)
        self.rock_view.append_column(self.rock_note_col)
        
        # Add the rock list.
        rock_scroll = Gtk.ScrolledWindow()
        rock_scroll.set_hexpand(True)
        rock_scroll.set_vexpand(True)
        rock_scroll.add(self.rock_view)
        
        # Create the TreeView for displaying the mineral data
        self.mineral_view = Gtk.TreeView(model = self.mineral_list)
        mineral_id_text = Gtk.CellRendererText()
        self.mineral_id_col = Gtk.TreeViewColumn("ID", mineral_id_text, text = 0)
        self.mineral_view.append_column(self.mineral_id_col)
        mineral_date_text = Gtk.CellRendererText()
        self.mineral_date_col = Gtk.TreeViewColumn("Date Collected", mineral_date_text, text = 1)
        self.mineral_view.append_column(self.mineral_date_col)
        mineral_loc_text = Gtk.CellRendererText()
        self.mineral_loc_col = Gtk.TreeViewColumn("Location Found", mineral_loc_text, text = 2)
        self.mineral_view.append_column(self.mineral_loc_col)
        mineral_name_text = Gtk.CellRendererText()
        self.mineral_name_col = Gtk.TreeViewColumn("Name", mineral_name_text, text = 3)
        self.mineral_view.append_column(self.mineral_name_col)
        mineral_color_text = Gtk.CellRendererText()
        self.mineral_color_col = Gtk.TreeViewColumn("Color", mineral_color_text, text = 4)
        self.mineral_view.append_column(self.mineral_color_col)
        mineral_lus_text = Gtk.CellRendererText()
        self.mineral_lus_col = Gtk.TreeViewColumn("Luster", mineral_lus_text, text = 5)
        self.mineral_view.append_column(self.mineral_lus_col)
        mineral_str_text = Gtk.CellRendererText()
        self.mineral_str_col = Gtk.TreeViewColumn("Streak", mineral_str_text, text = 6)
        self.mineral_view.append_column(self.mineral_str_col)
        mineral_hard_text = Gtk.CellRendererText()
        self.mineral_hard_col = Gtk.TreeViewColumn("Hardness", mineral_hard_text, text = 7)
        self.mineral_view.append_column(self.mineral_hard_col)
        mineral_cry_text = Gtk.CellRendererText()
        self.mineral_cry_col = Gtk.TreeViewColumn("Crystal Structure", mineral_cry_text, text = 8)
        self.mineral_view.append_column(self.mineral_cry_col)
        mineral_note_text = Gtk.CellRendererText()
        self.mineral_note_col = Gtk.TreeViewColumn("Notes", mineral_note_text, text = 9)
        self.mineral_view.append_column(self.mineral_note_col)
        
        # Add the mineral list.
        mineral_scroll = Gtk.ScrolledWindow()
        mineral_scroll.set_hexpand(True)
        mineral_scroll.set_vexpand(True)
        mineral_scroll.add(self.mineral_view)
        
        # Create the TreeView for displaying the fossil data
        self.fossil_view = Gtk.TreeView(model = self.fossil_list)
        fossil_id_text = Gtk.CellRendererText()
        self.fossil_id_col = Gtk.TreeViewColumn("ID", fossil_id_text, text = 0)
        self.fossil_view.append_column(self.fossil_id_col)
        fossil_date_text = Gtk.CellRendererText()
        self.fossil_date_col = Gtk.TreeViewColumn("Date Collected", fossil_date_text, text = 1)
        self.fossil_view.append_column(self.fossil_date_col)
        fossil_loc_text = Gtk.CellRendererText()
        self.fossil_loc_col = Gtk.TreeViewColumn("Location Found", fossil_loc_text, text = 2)
        self.fossil_view.append_column(self.fossil_loc_col)
        fossil_spec_text = Gtk.CellRendererText()
        self.fossil_spec_col = Gtk.TreeViewColumn("Species", fossil_spec_text, text = 3)
        self.fossil_view.append_column(self.fossil_spec_col)
        fossil_genu_text = Gtk.CellRendererText()
        self.fossil_genu_col = Gtk.TreeViewColumn("Genus", fossil_genu_text, text = 4)
        self.fossil_view.append_column(self.fossil_genu_col)
        fossil_fam_text = Gtk.CellRendererText()
        self.fossil_fam_col = Gtk.TreeViewColumn("Family", fossil_fam_text, text = 5)
        self.fossil_view.append_column(self.fossil_fam_col)
        fossil_ord_text = Gtk.CellRendererText()
        self.fossil_ord_col = Gtk.TreeViewColumn("Order", fossil_ord_text, text = 6)
        self.fossil_view.append_column(self.fossil_ord_col)
        fossil_cla_text = Gtk.CellRendererText()
        self.fossil_cla_col = Gtk.TreeViewColumn("Class", fossil_cla_text, text = 7)
        self.fossil_view.append_column(self.fossil_cla_col)
        fossil_phy_text = Gtk.CellRendererText()
        self.fossil_phy_col = Gtk.TreeViewColumn("Phylum", fossil_phy_text, text = 8)
        self.fossil_view.append_column(self.fossil_phy_col)
        fossil_king_text = Gtk.CellRendererText()
        self.fossil_king_col = Gtk.TreeViewColumn("Kingdom", fossil_king_text, text = 9)
        self.fossil_view.append_column(self.fossil_king_col)
        fossil_note_text = Gtk.CellRendererText()
        self.fossil_note_col = Gtk.TreeViewColumn("Notes", fossil_note_text, text = 10)
        self.fossil_view.append_column(self.fossil_note_col)
        
        # Add the fossil list.
        fossil_scroll = Gtk.ScrolledWindow()
        fossil_scroll.set_hexpand(True)
        fossil_scroll.set_vexpand(True)
        fossil_scroll.add(self.fossil_view)
        
        # Add the tabs.
        notebook.append_page(rock_scroll, rock_lbl)
        notebook.append_page(mineral_scroll, mineral_lbl)
        notebook.append_page(fossil_scroll, fossil_lbl)
        
        # Create the menus.
        action_group = Gtk.ActionGroup("actions")
        action_group.add_actions([
            ("collection_menu", None, "_Collection"),
            ("add_rock", None, "Add _Rock...", "<Control>r", None, self.add_rock),
            ("add_mineral", None, "Add _Mineral...", "<Control>m", None, self.add_mineral),
            ("add_fossil", None, "Add _Fossil...", "<Control>f", None, self.add_fossil),
            ("remove", None, "_Remove...", "<Control>d", None, None),
            ("clear_rocks", None, "Clear Rocks...", None, None, None),
            ("clear_minerals", None, "Clear Minerals...", None, None, None),
            ("clear_fossils", None, "Clear Fossils...", None, None, None),
            ("clear_all", None, "Clear All...", None, None, None)
        ])
        action_export_group = Gtk.Action("export_menu", "E_xport", None, None)
        action_group.add_action(action_export_group)
        action_group.add_actions([
            ("export_rocks", None, "Export _Rocks...", None, None, None),
            ("export_minerals", None, "Export _Minerals...", None, None, None),
            ("export_fossils", None, "Export _Fossils...", None, None, None)
        ])
        action_import_group = Gtk.Action("import_menu", "_Import", None, None)
        action_group.add_action(action_import_group)
        action_group.add_actions([
            ("import_rocks", None, "Import _Rocks...", None, None, None),
            ("import_minerals", None, "Import _Minerals...", None, None, None),
            ("import_fossils", None, "Import _Fossils...", None, None, None),
            ("import_append_rocks", None, "_Import and Append Rocks...", None, None, None),
            ("import_append_minerals", None, "Import and _Append Minerals...", None, None, None),
            ("import_append_fossils", None, "Im_port and Append Fossils...", None, None, None),
            ("quit", None, "_Quit", "<Control>q", None, lambda x: self.exit("ignore", "this"))
        ])
        action_group.add_actions([
            ("info_menu", None, "_Info"),
            ("show_info", None, "Show _Info...", "<Control>i", None, None),
            ("show_rock_info", None, "Show _Rock Info...", "<Control><Shift>r", None, None),
            ("show_mineral_info", None, "Show _Mineral Info...", "<Control><Shift>m", None, None),
            ("show_fossil_info", None, "Show _Fossil Info...", "<Control><Shift>f", None, None)
        ])
        action_group.add_actions([
            ("options_menu", None, "_Options"),
            ("options", None, "_Options...", "F2", None, None)
        ])
        action_group.add_actions([
            ("help_menu", None, "_Help"),
            ("about", None, "_About...", "<Shift>F1", None, self.show_about),
            ("help", None, "_Help...", "F1", None, self.show_help)
        ])
        
        # Build the UI.
        ui_manager = Gtk.UIManager()
        ui_manager.add_ui_from_string(MENU_DATA)
        
        # Add the menus.
        accel_group = ui_manager.get_accel_group()
        self.add_accel_group(accel_group)
        ui_manager.insert_action_group(action_group)
        grid = Gtk.Grid()
        menubar = ui_manager.get_widget("/menubar")
        grid.add(menubar)

        # Add the notebook to the window.
        grid.attach_next_to(notebook, menubar, Gtk.PositionType.BOTTOM, 1, 1)
        
        # Add the grid to the main window.
        self.add(grid)
        self.show_all()
        
        # Bind events.
        self.connect("delete-event", self.delete_event)
    
    
    def delete_event(self, widget, event):
        """Saves the window size."""
        
        # Get the current window size.
        height, width = self.get_size()
        
        # Save the window size.
        save.save_window(self.conf_dir, width, height)
    
    
    def add_rock(self, event):
        """Adds a rock to the collection."""
        
        # Show the dialog.
        new_dlg = AddRockDialog(self)
        # Get the response.
        response = new_dlg.run()
        # Close the dialog.
        new_dlg.destroy()
    
    
    def add_mineral(self, event):
        """Adds a mineral to the collection."""
        
        # Show the dialog.
        new_dlg = AddMineralDialog(self)
        # Get the response.
        response = new_dlg.run()
        # Close the dialog.
        new_dlg.destroy()
    
    
    def add_fossil(self, event):
        """Adds a fossil  to the collection."""
        
        # Show the dialog.
        new_dlg = AddFossilDialog(self)
        # Get the response.
        response = new_dlg.run()
        # Close the dialog.
        new_dlg.destroy() 
    
    
    def show_about(self, event):
        """Shows the About dialog."""
        
        # Load the icon.
        img_file = open("resources/images/icon.png", "rb")
        img_bin = img_file.read()
        img_file.close()
        
        # Get the PixBuf.
        loader = GdkPixbuf.PixbufLoader.new_with_type("png")
        loader.write(img_bin)
        loader.close()
        pixbuf = loader.get_pixbuf()
        
        # Create the dialog.
        about_dlg = Gtk.AboutDialog()
        about_dlg.set_title("About Rock Collector")
        about_dlg.set_program_name(TITLE)
        about_dlg.set_logo(pixbuf)
        about_dlg.set_version(VERSION)
        about_dlg.set_comments("Rock Collector is an application for managing a geology collection.")
        about_dlg.set_copyright("Copyright (c) 2013-2015 Adam Chesak")
        about_dlg.set_authors(["Adam Chesak <achesak@yahoo.com>"])
        about_dlg.set_license(license_text)
        about_dlg.set_website("https://github.com/achesak/rock-collector")
        about_dlg.set_website_label("https://github.com/achesak/rock-collector")
        
        # Show the dialog.
        about_dlg.show_all()
        
        # Run then close the dialog.
        about_dlg.run()
        about_dlg.destroy()
    
    
    def show_help(self, event):
        """Shows the help in a web browser."""
        
        # Open the help file.
        webbrowser.open_new("resources/help/help.html")      
    
    
    def save(self):
        """Saves the data."""
        
        # Save the data files.
        save.save_data(self.main_dir, self.rocks, self.minerals, self.fossils)
        
        # Save the counters.
        save.save_counters(self.conf_dir, self.rocks_count, self.minerals_count, self.fossils_count)
    
    
    def exit(self, x, y):
        """Closes the application."""
        
        # Save the files.
        self.save()
        
        # Close the application.
        Gtk.main_quit()


if __name__ == "__main__":
    
    # Create the application.
    win = RockCollector()
    win.connect("delete-event", win.exit)
    win.show_all()
    Gtk.main()
