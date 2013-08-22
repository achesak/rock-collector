#!/usr/bin/python
from gi.repository import Gtk


TITLE = "Rock Collector"


class RockCollector(Gtk.Window):
    """Create the application class."""

    def __init__(self):
        """Create the application."""
        
        # Create the window.
        Gtk.Window.__init__(self, title = TITLE)
        
        # Create the notebook.
        notebook = Gtk.Notebook()
        # Set tab position to top.
        notebook.set_tab_pos(Gtk.PositionType.TOP)
        
        # Create the tab labels.
        rock_lbl = Gtk.Label("Rocks")
        mineral_lbl = Gtk.Label("Minerals")
        fossil_lbl = Gtk.Label("Fossils")
        
        button1 = Gtk.Button(label = "Button")
        button2 = Gtk.Button(label = "Button")
        button3 = Gtk.Button(label = "Button")
        notebook.append_page(button1, rock_lbl)
        notebook.append_page(button2, mineral_lbl)
        notebook.append_page(button3, fossil_lbl)
        
        # Add the notebook to the window.
        self.add(notebook)

if __name__ == "__main__":
    
    # Create the application.
    win = RockCollector()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
