# main.py
# -------------------------------------------------------------------

# Main file for Engine Digital Twin Interface program.
# Written by Rodrigo Murillo Tapia, Alejandro Martinez Licon and Alejandro Gaviria Ramirez.
# 2023

from app import App     # The only object called in main is an instance of the App class.

### Note: Run main from path ending on EDTI directory to avoid errors

# Set interface size and appearance mode: "Dark", "Light"
window_size = "1300x600"
appearance_mode = "Light"

if __name__ == "__main__":      # Condition to only run this code if ran as the main program
    app = App(appearance_mode, window_size)     # Initializes app
    app.mainloop()                              # Runs the customtkinter mainloop of app

