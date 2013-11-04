# -*- coding: utf-8 -*-


################################################################################

# Rock Collector
# Version 0.1

# Rock Collector is an application for managing a geology collection.

# Released under the MIT open source license:
license_text = """
Copyright (c) 2013 Adam Chesak

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
# Import sys for closing the application.
import sys
# Import webbrowser for opening the help in the user's web browser.
import webbrowser
# Import os for various things.
import os
# Import platform for getting the user's OS.
import platform

# Import the application's UI data.
from resources.ui import VERSION, TITLE, MENU_DATA
# Import the dialog for adding a rock to the collection.
from resources.dialogs.add_rock import AddRockDialog

# Tell Python not to create bytecode files, as they mess with the git repo.
# This line can be removed be the user, if desired.
sys.dont_write_bytecode = True


# Get the main directory.
if platform.system().lower() == "windows":
    main_dir = "C:\\.rockcollector"
else:
    main_dir = "%s/.rockcollector" % os.path.expanduser("~")

# Check to see if the directory exists, and create it if it doesn't.
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
    init_file4 = open("%s/rocks_counter" % main_dir, "w")
    init_file4.write("1")
    init_file4.close()
    init_file5 = open("%s/minerals_counter" % main_dir, "w")
    init_file5.write("1")
    init_file5.close()
    init_file6 = open("%s/fossils_counter" % main_dir, "w")
    init_file6.write("1")
    init_file6.close()


class RockCollector(Gtk.Window):
    """Create the application class."""

    def __init__(self):
        """Create the application."""
        
        # Create the window.
        Gtk.Window.__init__(self, title = TITLE)
        # Set the size.
        self.set_default_size(1000, 500)
        # Set the icon.
        self.set_icon_from_file("resources/images/icon.png")
        
        # Create the ListStores.
        self.rock_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str)
        self.mineral_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str)
        self.fossil_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str, str)
        
        # Create the notebook.
        notebook = Gtk.Notebook()
        # Set tab position to top.
        notebook.set_tab_pos(Gtk.PositionType.TOP)
        
        # Create the tab labels.
        rock_lbl = Gtk.Label("Rocks")
        mineral_lbl = Gtk.Label("Minerals")
        fossil_lbl = Gtk.Label("Fossils")
        
        # Create the TreeView for displaying the rock data
        self.rock_view = Gtk.TreeView(model = self.rock_list)
        
        # Create the rock ID column.
        rock_id_text = Gtk.CellRendererText()
        self.rock_id_col = Gtk.TreeViewColumn("ID", rock_id_text, text = 0)
        self.rock_view.append_column(self.rock_id_col)
        
        # Create the rock Date Collected column.
        rock_date_text = Gtk.CellRendererText()
        self.rock_date_col = Gtk.TreeViewColumn("Date Collected", rock_date_text, text = 1)
        self.rock_view.append_column(self.rock_date_col)
        
        # Create the rock Location Found column.
        rock_loc_text = Gtk.CellRendererText()
        self.rock_loc_col = Gtk.TreeViewColumn("Location Found", rock_loc_text, text = 2)
        self.rock_view.append_column(self.rock_loc_col)
        
        # Create the rock Name column.
        rock_name_text = Gtk.CellRendererText()
        self.rock_name_col = Gtk.TreeViewColumn("Name", rock_name_text, text = 3)
        self.rock_view.append_column(self.rock_name_col)
        
        # Create the rock Type column.
        rock_type_text = Gtk.CellRendererText()
        self.rock_type_col = Gtk.TreeViewColumn("Type", rock_type_text, text = 4)
        self.rock_view.append_column(self.rock_type_col)
        
        # Create the rock Color column.
        rock_color_text = Gtk.CellRendererText()
        self.rock_color_col = Gtk.TreeViewColumn("Color", rock_color_text, text = 5)
        self.rock_view.append_column(self.rock_color_col)
        
        # Create the rock Texture column.
        rock_tex_text = Gtk.CellRendererText()
        self.rock_tex_col = Gtk.TreeViewColumn("Texture", rock_tex_text, text = 6)
        self.rock_view.append_column(self.rock_tex_col)
        
        # Create the rock Structure column.
        rock_struc_text = Gtk.CellRendererText()
        self.rock_struc_col = Gtk.TreeViewColumn("Structure", rock_struc_text, text = 7)
        self.rock_view.append_column(self.rock_struc_col)
        
        # Create the rock Hardness column.
        rock_hard_text = Gtk.CellRendererText()
        self.rock_hard_col = Gtk.TreeViewColumn("Hardness", rock_hard_text, text = 8)
        self.rock_view.append_column(self.rock_hard_col)
        
        # Create the rock Notes column.
        rock_note_text = Gtk.CellRendererText()
        self.rock_note_col = Gtk.TreeViewColumn("Notes", rock_note_text, text = 9)
        self.rock_view.append_column(self.rock_note_col)
        
        # Create the ScrolledWindow for displaying the rock list with a scrollbar.
        rock_scroll = Gtk.ScrolledWindow()
        # The container should scroll both horizontally and vertically.
        rock_scroll.set_hexpand(True)
        rock_scroll.set_vexpand(True)
        
        # Display the rock TreeView.
        rock_scroll.add(self.rock_view)
        
        # Create the TreeView for displaying the mineral data
        self.mineral_view = Gtk.TreeView(model = self.mineral_list)
        
        # Create the mineral ID column.
        mineral_id_text = Gtk.CellRendererText()
        self.mineral_id_col = Gtk.TreeViewColumn("ID", mineral_id_text, text = 0)
        self.mineral_view.append_column(self.mineral_id_col)
        
        # Create the mineral Date Collected column.
        mineral_date_text = Gtk.CellRendererText()
        self.mineral_date_col = Gtk.TreeViewColumn("Date Collected", mineral_date_text, text = 1)
        self.mineral_view.append_column(self.mineral_date_col)
        
        # Create the mineral Location Found column.
        mineral_loc_text = Gtk.CellRendererText()
        self.mineral_loc_col = Gtk.TreeViewColumn("Location Found", mineral_loc_text, text = 2)
        self.mineral_view.append_column(self.mineral_loc_col)
        
        # Create the mineral Name column.
        mineral_name_text = Gtk.CellRendererText()
        self.mineral_name_col = Gtk.TreeViewColumn("Name", mineral_name_text, text = 3)
        self.mineral_view.append_column(self.mineral_name_col)
        
        # Create the mineral Color column.
        mineral_color_text = Gtk.CellRendererText()
        self.mineral_color_col = Gtk.TreeViewColumn("Color", mineral_color_text, text = 4)
        self.mineral_view.append_column(self.mineral_color_col)
        
        # Create the mineral Luster column.
        mineral_lus_text = Gtk.CellRendererText()
        self.mineral_lus_col = Gtk.TreeViewColumn("Luster", mineral_lus_text, text = 5)
        self.mineral_view.append_column(self.mineral_lus_col)
        
        # Create the mineral Streak column.
        mineral_str_text = Gtk.CellRendererText()
        self.mineral_str_col = Gtk.TreeViewColumn("Streak", mineral_str_text, text = 6)
        self.mineral_view.append_column(self.mineral_str_col)
        
        # Create the mineral Hardness column.
        mineral_hard_text = Gtk.CellRendererText()
        self.mineral_hard_col = Gtk.TreeViewColumn("Hardness", mineral_hard_text, text = 7)
        self.mineral_view.append_column(self.mineral_hard_col)
        
        # Create the mineral Crystal Structure column.
        mineral_cry_text = Gtk.CellRendererText()
        self.mineral_cry_col = Gtk.TreeViewColumn("Crystal Structure", mineral_cry_text, text = 8)
        self.mineral_view.append_column(self.mineral_cry_col)
        
        # Create the mineral Notes column.
        mineral_note_text = Gtk.CellRendererText()
        self.mineral_note_col = Gtk.TreeViewColumn("Notes", mineral_note_text, text = 9)
        self.mineral_view.append_column(self.mineral_note_col)
        
        # Create the ScrolledWindow for displaying the mineral list with a scrollbar.
        mineral_scroll = Gtk.ScrolledWindow()
        # The container should scroll both horizontally and vertically.
        mineral_scroll.set_hexpand(True)
        mineral_scroll.set_vexpand(True)
        
        # Display the mineral TreeView.
        mineral_scroll.add(self.mineral_view)
        
        # Create the TreeView for displaying the fossil data
        self.fossil_view = Gtk.TreeView(model = self.fossil_list)
        
        # Create the fossil ID column.
        fossil_id_text = Gtk.CellRendererText()
        self.fossil_id_col = Gtk.TreeViewColumn("ID", fossil_id_text, text = 0)
        self.fossil_view.append_column(self.fossil_id_col)
        
        # Create the fossil Date Collected column.
        fossil_date_text = Gtk.CellRendererText()
        self.fossil_date_col = Gtk.TreeViewColumn("Date Collected", fossil_date_text, text = 1)
        self.fossil_view.append_column(self.fossil_date_col)
        
        # Create the fossil Location Found column.
        fossil_loc_text = Gtk.CellRendererText()
        self.fossil_loc_col = Gtk.TreeViewColumn("Location Found", fossil_loc_text, text = 2)
        self.fossil_view.append_column(self.fossil_loc_col)
        
        # Create the fossil Species column.
        fossil_spec_text = Gtk.CellRendererText()
        self.fossil_spec_col = Gtk.TreeViewColumn("Species", fossil_spec_text, text = 3)
        self.fossil_view.append_column(self.fossil_spec_col)
        
        # Create the fossil Genus column.
        fossil_genu_text = Gtk.CellRendererText()
        self.fossil_genu_col = Gtk.TreeViewColumn("Genus", fossil_genu_text, text = 4)
        self.fossil_view.append_column(self.fossil_genu_col)
        
        # Create the fossil Family column.
        fossil_fam_text = Gtk.CellRendererText()
        self.fossil_fam_col = Gtk.TreeViewColumn("Family", fossil_fam_text, text = 5)
        self.fossil_view.append_column(self.fossil_fam_col)
        
        # Create the fossil Order column.
        fossil_ord_text = Gtk.CellRendererText()
        self.fossil_ord_col = Gtk.TreeViewColumn("Order", fossil_ord_text, text = 6)
        self.fossil_view.append_column(self.fossil_ord_col)
        
        # Create the fossil Class column.
        fossil_cla_text = Gtk.CellRendererText()
        self.fossil_cla_col = Gtk.TreeViewColumn("Class", fossil_cla_text, text = 7)
        self.fossil_view.append_column(self.fossil_cla_col)
        
        # Create the fossil Phylum column.
        fossil_phy_text = Gtk.CellRendererText()
        self.fossil_phy_col = Gtk.TreeViewColumn("Phylum", fossil_phy_text, text = 8)
        self.fossil_view.append_column(self.fossil_phy_col)
        
        # Create the fossil Kingdom column.
        fossil_king_text = Gtk.CellRendererText()
        self.fossil_king_col = Gtk.TreeViewColumn("Kingdom", fossil_king_text, text = 9)
        self.fossil_view.append_column(self.fossil_king_col)
        
        # Create the fossil Notes column.
        fossil_note_text = Gtk.CellRendererText()
        self.fossil_note_col = Gtk.TreeViewColumn("Notes", fossil_note_text, text = 10)
        self.fossil_view.append_column(self.fossil_note_col)
        
        # Create the ScrolledWindow for displaying the fossil list with a scrollbar.
        fossil_scroll = Gtk.ScrolledWindow()
        # The container should scroll both horizontally and vertically.
        fossil_scroll.set_hexpand(True)
        fossil_scroll.set_vexpand(True)
        
        # Display the fossil TreeView.
        fossil_scroll.add(self.fossil_view)
        
        # Add the tabs.
        notebook.append_page(rock_scroll, rock_lbl)
        notebook.append_page(mineral_scroll, mineral_lbl)
        notebook.append_page(fossil_scroll, fossil_lbl)
        
        # Create the action group for the menus.
        action_group = Gtk.ActionGroup("actions")
        
        # Create the Collection menu.
        action_group.add_actions([
            ("collection_menu", None, "_Collection"),
            ("add_rock", None, "Add _Rock...", "<Control>r", None, self.add_rock),
            ("add_mineral", None, "Add _Mineral...", "<Control>m", None, None),
            ("add_fossil", None, "Add _Fossil...", "<Control>f", None, None),
            ("remove", None, "_Remove...", "<Control>d", None, None),
            ("clear_rocks", None, "Clear Rocks...", None, None, None),
            ("clear_minerals", None, "Clear Minerals...", None, None, None),
            ("clear_fossils", None, "Clear Fossils...", None, None, None),
            ("clear_all", None, "Clear All...", None, None, None)
        ])
        
        # Create the Collection -> Export submenu
        action_export_group = Gtk.Action("export_menu", "E_xport", None, None)
        action_group.add_action(action_export_group)
        action_group.add_actions([
            ("export_rocks", None, "Export _Rocks...", None, None, None),
            ("export_minerals", None, "Export _Minerals...", None, None, None),
            ("export_fossils", None, "Export _Fossils...", None, None, None)
        ])
        
        # Create the Collection -> Import submenu
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
        
        # Create the Info menu.
        action_group.add_actions([
            ("info_menu", None, "_Info"),
            ("show_info", None, "Show _Info...", "<Control>i", None, None),
            ("show_rock_info", None, "Show _Rock Info...", "<Control><Shift>r", None, None),
            ("show_mineral_info", None, "Show _Mineral Info...", "<Control><Shift>m", None, None),
            ("show_fossil_info", None, "Show _Fossil Info...", "<Control><Shift>f", None, None)
        ])
        
        # Create the Options menu.
        action_group.add_actions([
            ("options_menu", None, "_Options"),
            ("options", None, "_Options...", "F2", None, None)
        ])
        
        # Create the Help menu.
        action_group.add_actions([
            ("help_menu", None, "_Help"),
            ("about", None, "_About...", "<Shift>F1", None, self.show_about),
            ("help", None, "_Help...", "F1", None, self.show_help)
        ])
        
        # Create the UI manager.
        ui_manager = Gtk.UIManager()
        ui_manager.add_ui_from_string(MENU_DATA)
        
        # Add the accelerator group to the toplevel window
        accel_group = ui_manager.get_accel_group()
        self.add_accel_group(accel_group)
        ui_manager.insert_action_group(action_group)
        
        # Create the grid for the UI.
        grid = Gtk.Grid()
        
        # Add the menubar to the window.
        menubar = ui_manager.get_widget("/menubar")
        grid.add(menubar)

        # Add the notebook to the window.
        grid.attach_next_to(notebook, menubar, Gtk.PositionType.BOTTOM, 1, 1)
        
        # Add the grid to the main window.
        self.add(grid)
        self.show_all()
    
    
    def add_rock(self, event):
        """Adds a rock to the collection."""
        
        # Show the dialog.
        new_dlg = AddRockDialog(self)
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
        
        # Set the title.
        about_dlg.set_title("About Rock Collector")
        # Set the program name.
        about_dlg.set_program_name(TITLE)
        # Set the program icon.
        about_dlg.set_logo(pixbuf)
        # Set the program version.
        about_dlg.set_version(VERSION)
        # Set the comments.
        about_dlg.set_comments("Rock Collector is an application for managing a geology collection.")
        # Set the copyright notice. Legal stuff, bleh.
        about_dlg.set_copyright("Copyright (c) 2013 Adam Chesak")
        # Set the authors.
        about_dlg.set_authors(["Adam Chesak <achesak@yahoo.com>"])
        # Set the license.
        about_dlg.set_license(license_text)
        # Set the website.
        about_dlg.set_website("http://poultryandprogramming.wordpress.com/")
        about_dlg.set_website_label("http://poultryandprogramming.wordpress.com/")
        
        # Show the dialog.
        about_dlg.show_all()
        
        # Run then close the dialog.
        about_dlg.run()
        about_dlg.destroy()
    
    
    def show_help(self, event):
        """Shows the help in a web browser."""
        
        # Open the help file.
        webbrowser.open_new("resources/help/help.html")      
    
    
    def exit(self, x, y):
        """Closes the application."""
        
        # Close the application.
        Gtk.main_quit()


if __name__ == "__main__":
    
    # Create the application.
    win = RockCollector()
    win.connect("delete-event", win.exit)
    win.show_all()
    Gtk.main()
