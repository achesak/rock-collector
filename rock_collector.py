#!/usr/bin/python
from gi.repository import Gtk


TITLE = "Rock Collector"


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

        # Add the notebook to the window.
        self.add(notebook)

if __name__ == "__main__":
    
    # Create the application.
    win = RockCollector()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
