# -*- coding: utf-8 -*-


# This file defines variables used by the UI.


# Define the version and the title.
TITLE = "Rock Collector"
VERSION = "0.1"

# Define the menu XML.
MENU_DATA = """
<ui>
  <menubar name="menubar">
    <menu action="collection_menu">
      <menuitem action="add_rock" />
      <menuitem action="add_mineral" />
      <menuitem action="add_fossil" />
      <separator />
      <menuitem action="remove" />
      <separator />
      <menuitem action="clear_rocks" />
      <menuitem action="clear_minerals" />
      <menuitem action="clear_fossils" />
      <menuitem action="clear_all" />
      <separator />
      <menu action="export_menu">
        <menuitem action="export_rocks" />
        <menuitem action="export_minerals" />
        <menuitem action="export_fossils" />
      </menu>
      <menu action="import_menu">
        <menuitem action="import_rocks" />
        <menuitem action="import_minerals" />
        <menuitem action="import_fossils" />
        <separator />
        <menuitem action="import_append_rocks" />
        <menuitem action="import_append_minerals" />
        <menuitem action="import_append_fossils" />
      </menu>
      <separator />
      <menuitem action="quit" />
    </menu>
    <menu action="info_menu">
      <menuitem action="show_info" />
      <menuitem action="show_rock_info" />
      <menuitem action="show_mineral_info" />
      <menuitem action="show_fossil_info" />
    </menu>
    <menu action="options_menu">
      <menuitem action="options" />
    </menu>
    <menu action="help_menu">
      <menuitem action="about" />
      <separator />
      <menuitem action="help" />
    </menu>
  </menubar>
</ui>
"""
