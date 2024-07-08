Phone Management System Project Description
Project Title: Phone Management System

Overview:
The Phone Management System is a console-based application written in Python that allows users to manage a list of contacts. Users can add new contacts, search for existing contacts by name, list all contacts, and save contacts to a file for persistence. The system provides an intuitive menu-driven interface for users to interact with the contact list.

Features:
Add Contact: Users can add new contacts by providing the contact's name and phone number. The new contact is saved both in memory and to a file for persistence.
Search Contact: Users can search for contacts by name. The search is case-insensitive and returns all matching contacts.
List All Contacts: Users can list all saved contacts. Each contact's name and phone number are displayed.
Persistent Storage: Contacts are saved to a file (contacts.txt). The system loads existing contacts from this file when the application starts.
User-Friendly Interface: The system provides a simple, menu-driven interface to guide users through the available operations.

Implementation Details:
Contact Class: Represents a single contact with attributes for the name and phone number.
ContactManager Class: Manages the list of contacts, including loading from and saving to a file, adding new contacts, searching for contacts, and listing all contacts.
Main Menu Function: Provides the user interface for interacting with the contact manager, handling user input for various operations.
Usage:
Start the Application: Run the script to start the application. The contact manager will load existing contacts from contacts.txt.
Main Menu: The main menu is displayed with options to add a contact, search for a contact, list all contacts, or exit the application.
Add Contact: Select the option to add a contact, enter the contact's name and phone number when prompted, and the contact will be added to the list and saved to the file.
Search Contact: Select the option to search for a contact, enter the contact's name to search for, and the system will display matching contacts if found.
List All Contacts: Select the option to list all contacts, and the system will display all saved contacts.
Exit: Select the exit option to close the application.
