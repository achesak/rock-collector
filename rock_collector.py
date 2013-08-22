#!/usr/bin/python
from gi.repository import Gtk


TITLE = "Rock Collector"


class RockCollector(Gtk.Window):
    """Create the application class."""

    def __init__(self):
        """Create the application."""
        
        # Create the window.
        Gtk.Window.__init__(self, title = TITLE)
        
        # Create the ListStores.
        self.rock_list = Gtk.ListStore(int, str, str, str, str, str, str, str, str, str)
        
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
        
        # Add the tabs.
        notebook.append_page(rock_scroll, rock_lbl)

        # Add the notebook to the window.
        self.add(notebook)

if __name__ == "__main__":
    
    # Create the application.
    win = RockCollector()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
