# Version 11: Added function to update seat and bunk totals

from tkinter import *
from functools import partial       # To prevent unwanted windows
from tkmacosx import Button
import re

class Details:
    def __init__(self, parent):

        # Formatting variables
        background_color = "#004B8D"        # dark blue
        text_color = "snow2"
        self.error = "RosyBrown1"
        self.is_yes_auckland = False
        self.is_yes_palmers = False
        self.counter = 0
        self.total_palmers_seats = 20
        self.total_palmers_bunks = 15
        self.total_auckland_seats = 20
        self.total_auckland_bunks = 15
    
        # Main Screen GUI
        self.details_frame = Frame (bg=background_color, width=300, height=300, pady=10)
        self.details_frame.grid()

        # Company Name (row 0)
        self.company_label = Label(self.details_frame, text="Go Student Bus: Massey Overnighter", 
                                          font=("Arial 19 bold"), 
                                          bg="#E4A024",         # yellow
                                          fg=background_color, 
                                          padx=10, pady=5)
        self.company_label.grid(row=0, pady=(12, 0))

        # Disclaimer (row 1)
        self.disclaimer_label = Label(self.details_frame, text="Note: there are only 15 bunks and "
                                          "20 seats available on each service", 
                                          font=("Arial 12"), 
                                          bg=background_color, fg=text_color, 
                                          padx=10, pady=5)
        self.disclaimer_label.grid(row=1, pady=5)

        # Set up Entry Frame
        self.entry_frame = Frame(self.details_frame, width=200, bg=background_color, pady=10)
        self.entry_frame.grid(row=2, pady=10)

        # Name Entry Text (row 0, column 0)
        self.name_entry_label = Label(self.entry_frame, text="Name:", 
                                          width=14,
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                          fg=text_color, padx=5,
                                          anchor="e")
        self.name_entry_label.grid(row=0, column=0)

        # Name Entry (row 0, column 1)
        self.name_entry = Entry(self.entry_frame, width=35, font="Arial 14 bold")
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Phone Entry Text (row 1, column 0)
        self.phone_entry_label = Label(self.entry_frame, text="Mobile Number:",
                                          width=14,                                             
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                          fg=text_color, padx=5,
                                          anchor="e")
        self.phone_entry_label.grid(row=1, column=0)

        # Phone Entry (row 1, column 1)
        self.phone_entry = Entry(self.entry_frame, width=35, font="Arial 14 bold")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)


        # Set up Journey Selection Frame
        self.journey_selection_frame = Frame(self.details_frame, width=200, bg=background_color, pady=10)
        self.journey_selection_frame.grid(row=3)

        # Palmers to Auckland Text (row 0, column 0)
        self.from_palmers_label = Label(self.journey_selection_frame, text="One way from Palmerston North to Auckland", 
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                           fg=text_color, padx=5)
        self.from_palmers_label.grid(row=0, column=0, padx=(5, 0))

        # Palmers to Auckland Button (row 0, column 1)
        self.from_palmers_button = Button(self.journey_selection_frame, text="No",
                                  font=("Arial 14"), 
                                  bg="light coral",
                                  command=self.button_change_palmers,
                                  padx=10, pady=10)
        self.from_palmers_button.grid(row=0, column=1, padx=12, pady=5)     



        # Auckland to Palmers Text (row 1, column 0)
        self.from_auckland_label = Label(self.journey_selection_frame, text="One way from Auckland to Palmerston North", 
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                           fg=text_color, padx=5)
        self.from_auckland_label.grid(row=1, column=0, padx=(5, 0))

        # Auckland to Palmers Button (row 1, column 1)
        self.from_auckland_button = Button(self.journey_selection_frame, text="No",
                                  font=("Arial 14"), 
                                  bg="light coral",
                                  command=self.button_change_auckland,
                                  padx=10, pady=10)
        self.from_auckland_button.grid(row=1, column=1, padx=12, pady=5)  



        # Instructions Text (row 4)
        self.instructions_label = Label(self.details_frame, text="", 
                                          font=("Arial 12"), 
                                          bg=background_color, 
                                           fg=text_color, padx=5)
        self.instructions_label.grid(row=4)


        # Next Button (row 5)
        self.next_button = Button(self.details_frame, text="Next",
                                  font=("Arial 14"), 
                                  bg="#E4A024",         # yellow
                                  padx=10, pady=10,
                                  command=lambda: self.details_check(background_color))
        self.next_button.grid(row=5, pady=(35, 15))



    def button_change_auckland(self):
        self.is_yes_auckland = not self.is_yes_auckland
        self.button_change(self.from_auckland_button, self.is_yes_auckland)

    def button_change_palmers(self):
        self.is_yes_palmers = not self.is_yes_palmers        
        self.button_change(self.from_palmers_button, self.is_yes_palmers)

    def button_change(self, button, is_yes):
        if is_yes:
            button.configure(text="Yes", bg="pale green")
        
        else:
            button.configure(text="No", bg="light coral")



    
    def details_check(self, background_color):

        self.name = self.name_entry.get()
        self.phone_number = self.phone_entry.get()

        details_error = False
        phone_error = False
    
        if len(self.phone_number) < 9 or len(self.phone_number) > 11:
            problem = "must be 9-11 digits long"
            phone_error = True

        valid_char = "[0-9]"
        for letter in self.phone_number:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "no spaces allowed"
            
            else:
                problem = ("no {}'s allowed".format(letter))
            phone_error = True


        if self.phone_number == "":
            problem = "can't be blank"
            phone_error = True


        if self.name == "": 
            self.phone_entry.configure(bg="white")            
            self.name_entry.configure(bg=self.error)

            # Display error message
            self.instructions_label.configure(text="You have not entered a name in the name entry box above", fg="black", bg=self.error)
            details_error = True

        elif phone_error == True:
            self.phone_entry.configure(bg=self.error)
            self.name_entry.configure(bg="white")

            # Display error message
            self.instructions_label.configure(text="You have entered an invalid phone number - {}".format(problem), fg="black", bg=self.error)
            details_error = True

        else:
            self.name_entry.configure(bg="white")
            self.phone_entry.configure(bg="white")

            self.instructions_label.configure(text="", bg=background_color)

        

        if self.is_yes_auckland == False and self.is_yes_palmers == False:
            # Display error message
            self.instructions_label.configure(text="You have not selected any bus services", fg="black", bg=self.error)
            self.name_entry.configure(bg="white")
            self.phone_entry.configure(bg="white")
            details_error = True
        

        if details_error == False:
            self.book_places(background_color)


    def book_places(self, background_color):
        Booking(self, background_color)


class Booking:
    def __init__(self, partner, background_color):

        self.name = partner.name
        self.phone_number = partner.phone_number

        self.is_yes_auckland = partner.is_yes_auckland
        self.is_yes_palmers = partner.is_yes_palmers

        self.partner = partner

        # Disable next button
        partner.next_button.config(state=DISABLED)

        # Set up child window (ie: places box)
        self.places_box = Toplevel()

        # If users press cross at top, closes Places and 'releases' next button
        self.places_box.protocol('WM_DELETE_WINDOW', partial(self.close_places, partner))

        # Set up Places Frame
        self.places_frame = Frame(self.places_box, bg=background_color, pady=10)
        self.places_frame.grid()

        # Create elements is Palmers button is Yes
        if self.is_yes_palmers:

            # Set up Palmers Heading Frame
            self.from_palmers_heading_frame = Frame(self.places_frame, width=200, bg=background_color, pady=10)
            self.from_palmers_heading_frame.grid(row=0, pady=(0,10)) 

            # Set up from Palmers heading (row 0)
            self.from_palmers_heading_label = Label(self.from_palmers_heading_frame, text="One way from Palmerston North to Auckland:", 
                                            font=("Arial 16 bold"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10)
            self.from_palmers_heading_label.grid(row=0, pady=(10,0))

            # Set up first seats/bunks frame
            self.from_palmers_places_frame = Frame(self.places_frame, width=200, bg=background_color, pady=10)
            self.from_palmers_places_frame.grid(row=1, pady=(0,20))  

            # Set up seats text (row 0, column 0)
            self.from_palmers_seats_label = Label(self.from_palmers_places_frame, text="Number of seats you would like to book:", 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_palmers_seats_label.grid(row=0, column=0)

            # Seats Entry (row 0, column 1)
            self.from_palmers_seats_entry = Entry(self.from_palmers_places_frame, width=15, font="Arial 14 bold")
            self.from_palmers_seats_entry.grid(row=0, column=1, padx=10, pady=5)   

            # Remaining seats text (row 0, column 2)
            self.from_palmers_remaining_seats_label = Label(self.from_palmers_places_frame, 
                                            text="({}/20 seats remaining)".format(partner.total_palmers_seats), 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_palmers_remaining_seats_label.grid(row=0, column=2) 

            # Set up bunks text (row 1, column 0)
            self.from_palmers_bunks_label = Label(self.from_palmers_places_frame, text="Number of bunks you would like to book:", 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_palmers_bunks_label.grid(row=1, column=0)

            # Bunks Entry (row 1, column 1)
            self.from_palmers_bunks_entry = Entry(self.from_palmers_places_frame, width=15, font="Arial 14 bold")
            self.from_palmers_bunks_entry.grid(row=1, column=1, padx=10, pady=5)   

            # Remaining seats text (row 1, column 2)
            self.from_palmers_remaining_bunks_label = Label(self.from_palmers_places_frame, 
                                            text="({}/15 bunks remaining)".format(partner.total_palmers_bunks), 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_palmers_remaining_bunks_label.grid(row=1, column=2) 


        # Create elements is Auckland button is Yes
        if self.is_yes_auckland:

            # Set up Auckland Heading Frame
            self.from_auckland_heading_frame = Frame(self.places_frame, width=200, bg=background_color, pady=10)
            self.from_auckland_heading_frame.grid(row=2, pady=(0,10)) 

            # Set up from Auckland heading (row 0)
            self.from_auckland_heading_label = Label(self.from_auckland_heading_frame, text="One way from Auckland to Palmerston North:", 
                                            font=("Arial 16 bold"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10)
            self.from_auckland_heading_label.grid(row=0, pady=(10,0))

            # Set up second seats/bunks frame
            self.from_auckland_places_frame = Frame(self.places_frame, width=200, bg=background_color, pady=10)
            self.from_auckland_places_frame.grid(row=3, pady=(0,10))  

            # Set up seats text (row 0, column 0)
            self.from_auckland_seats_label = Label(self.from_auckland_places_frame, text="Number of seats you would like to book:", 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_auckland_seats_label.grid(row=0, column=0)

            # Seats Entry (row 0, column 1)
            self.from_auckland_seats_entry = Entry(self.from_auckland_places_frame, width=15, font="Arial 14 bold")
            self.from_auckland_seats_entry.grid(row=0, column=1, padx=10, pady=5)   

            # Remaining seats text (row 0, column 2)
            self.from_auckland_remaining_seats_label = Label(self.from_auckland_places_frame,
                                            text="({}/20 seats remaining)".format(partner.total_auckland_seats), 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_auckland_remaining_seats_label.grid(row=0, column=2) 

            # Set up bunks text (row 1, column 0)
            self.from_auckland_bunks_label = Label(self.from_auckland_places_frame, text="Number of bunks you would like to book:", 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_auckland_bunks_label.grid(row=1, column=0)

            # Bunks Entry (row 1, column 1)
            self.from_auckland_bunks_entry = Entry(self.from_auckland_places_frame, width=15, font="Arial 14 bold")
            self.from_auckland_bunks_entry.grid(row=1, column=1, padx=10, pady=5)   

            # Remaining seats text (row 1, column 2)
            self.from_auckland_remaining_bunks_label = Label(self.from_auckland_places_frame, 
                                            text="({}/15 bunks remaining)".format(partner.total_auckland_bunks), 
                                            font=("Arial 14"), 
                                            bg=background_color, 
                                            fg="white",
                                            padx=10, pady=10)
            self.from_auckland_remaining_bunks_label.grid(row=1, column=2) 


        # Error text (row 4)
        self.error_label = Label(self.places_frame, text="Please enter a number", 
                                          font=("Arial 12"), 
                                          bg=background_color, 
                                          fg="white",
                                          padx=10)
        self.error_label.grid(row=4) 


        # Preview Booking Button (row 5)
        self.preview_button = Button(self.places_frame, text="Preview Booking",
                                  font=("Arial 14"), 
                                  bg="#E4A024",         # yellow
                                  padx=10, pady=10,
                                  command=lambda: self.seats_bunks_selection(partner, background_color))
        self.preview_button.grid(row=5, pady=15)
        
    

    def seats_bunks_selection(self, partner, background_color):
        self.error_label.configure(font=("Arial 12"), fg="white")
        
        if self.is_yes_palmers == True and self.is_yes_auckland == True:
            message = "(Palmerston North to Auckland)"
            valid_seats = self.seats_check(partner, self.from_palmers_seats_entry, message, partner.total_palmers_seats, background_color) 
            if valid_seats:
                valid_bunks = self.bunks_check(partner, self.from_palmers_bunks_entry, message, partner.total_palmers_bunks, background_color)
               
                if valid_seats and valid_bunks:
                    from_palmers_seats = int(float(self.from_palmers_seats_entry.get()))
                    from_palmers_bunks = int(float(self.from_palmers_bunks_entry.get()))

                    if partner.total_palmers_seats == 0 and partner.total_palmers_bunks == 0:
                        self.error_label.configure(text="There are no remaining seats or bunks {}".format(message), fg="black", bg=partner.error)
                    else:
                        if from_palmers_seats == 0 and from_palmers_bunks == 0:
                            self.error_label.configure(text="Please enter a number greater than zero for seats or bunks {}".format(message), fg="black", bg=partner.error)
                        else:
                            if valid_seats and valid_bunks:
                                    message = "(Auckland to Palmerston North)"
                                    valid_seats = self.seats_check(partner, self.from_auckland_seats_entry, message, partner.total_auckland_seats, background_color) 
                                    if valid_seats:
                                        valid_bunks = self.bunks_check(partner, self.from_auckland_bunks_entry, message, partner.total_auckland_bunks, background_color)

                                        from_auckland_seats = int(float(self.from_auckland_seats_entry.get()))
                                        from_auckland_bunks = int(float(self.from_auckland_bunks_entry.get()))

                                        if partner.total_auckland_seats == 0 and partner.total_auckland_bunks == 0:
                                            self.error_label.configure(text="There are no remaining seats or bunks {}".format(message), fg="black", bg=partner.error)
                                        else:
                                            if from_auckland_seats == 0 and from_auckland_bunks == 0:
                                                self.error_label.configure(text="Please enter a number greater than zero for seats or bunks {}".format(message), fg="black", bg=partner.error)
                                            else:
                                                if valid_seats and valid_bunks:
                                                    self.preview_booking(background_color)
                            

        elif self.is_yes_palmers == True:
            message = ""
            valid_seats = self.seats_check(partner, self.from_palmers_seats_entry, message, partner.total_palmers_seats, background_color)
            if valid_seats:
                valid_bunks = self.bunks_check(partner, self.from_palmers_bunks_entry, message, partner.total_palmers_bunks, background_color)
                
                if valid_seats and valid_bunks:
                    from_palmers_seats = int(float(self.from_palmers_seats_entry.get()))
                    from_palmers_bunks = int(float(self.from_palmers_bunks_entry.get()))

                    if partner.total_palmers_seats == 0 and partner.total_palmers_bunks == 0:
                        self.error_label.configure(text="There are no remaining seats or bunks {}".format(message), fg="black", bg=partner.error)
                    else:
                        if from_palmers_seats == 0 and from_palmers_bunks == 0:
                            self.error_label.configure(text="Please enter a number greater than zero for seats or bunks", fg="black", bg=partner.error)
                        else:
                            if valid_seats and valid_bunks:
                                self.preview_booking(background_color)


        elif self.is_yes_auckland == True:
            message = ""
            valid_seats = self.seats_check(partner, self.from_auckland_seats_entry, message, partner.total_auckland_seats, background_color)
            if valid_seats:
                valid_bunks = self.bunks_check(partner, self.from_auckland_bunks_entry, message, partner.total_auckland_bunks, background_color)
                
                if valid_seats and valid_bunks:
                    from_auckland_seats = int(float(self.from_auckland_seats_entry.get()))
                    from_auckland_bunks = int(float(self.from_auckland_bunks_entry.get()))

                    if partner.total_auckland_seats == 0 and partner.total_auckland_bunks == 0:
                        self.error_label.configure(text="There are no remaining seats or bunks {}".format(message), fg="black", bg=partner.error)
                    else:
                        if from_auckland_seats == 0 and from_auckland_bunks == 0:
                            self.error_label.configure(text="Please enter a number greater than zero for seats or bunks", fg="black", bg=partner.error)
                        else:
                            if valid_seats and valid_bunks:
                                self.preview_booking(background_color)

            


    def seats_check(self, partner, seats_entry, message, total_seats, background_color) -> bool:
        try:
            self.seats_booked = float(seats_entry.get())
            if self.seats_booked % 1 != 0:
                seats_entry.configure(bg=partner.error)
                self.error_label.configure(text="Please enter the number of seats as an integer {}".format(message), fg="black", bg=partner.error)
            elif self.seats_booked > total_seats:
                seats_entry.configure(bg=partner.error)
                self.error_label.configure(text="There are only {} seats available {}".format(total_seats, message), fg="black", bg=partner.error)
                if total_seats == 0:
                    self.error_label.configure(text="There are no more seats available {}".format(message), fg="black", bg=partner.error)
            elif self.seats_booked < 0:
                seats_entry.configure(bg=partner.error)
                self.error_label.configure(text="Please enter a positive number {}".format(message), fg="black", bg=partner.error)
            else:
                seats_entry.configure(bg="white")
                self.error_label.configure(text="", bg=background_color)
                return True
            return False
        except:
            seats_entry.configure(bg=partner.error)
            self.error_label.configure(text="Please enter the number of seats you would like using digits 0-9 {}".format(message), fg="black", bg=partner.error)
            return False



    def bunks_check(self, partner, bunks_entry, message, total_bunks, background_color) -> bool: 
        try:
            self.bunks_booked = float(bunks_entry.get())
            if self.bunks_booked % 1 != 0:
                bunks_entry.configure(bg=partner.error)
                self.error_label.configure(text="Please enter the number of bunks as an integer {}".format(message), fg="black", bg=partner.error)
            elif self.bunks_booked > total_bunks:
                bunks_entry.configure(bg=partner.error)
                self.error_label.configure(text="There are only {} seats available {}".format(total_bunks, message), fg="black", bg=partner.error)
                if total_bunks == 0:
                    self.error_label.configure(text="There are no more bunks available {}".format(message), fg="black", bg=partner.error)
            elif self.bunks_booked < 0:
                bunks_entry.configure(bg=partner.error)
                self.error_label.configure(text="Please enter a positive number {}".format(message), fg="black", bg=partner.error)
            else:
                bunks_entry.configure(bg="white")
                self.error_label.configure(text="", bg=background_color)
                return True
            return False
        except:
            bunks_entry.configure(bg=partner.error)
            self.error_label.configure(text="Please enter the number of bunks you would like using digits 0-9 {}".format(message), fg="black", bg=partner.error)
            return False



    def close_places(self, partner):
        # Put next button back to normal
        partner.next_button.config(state=NORMAL)
        self.places_box.destroy()


    def preview_booking(self, background_color):
        Preview(self, background_color)


class Preview:
    def __init__(self, partner, background_color):

        # Disable next button
        partner.preview_button.config(state=DISABLED)

        # Set up child window (ie: preview box)
        self.preview_box = Toplevel()

        # If users press cross at top, closes help and 'releases' next button
        self.preview_box.protocol('WM_DELETE_WINDOW', partial(self.close_preview, partner))

        # Set up Docket Frame
        self.preview_frame = Frame(self.preview_box, bg=background_color, pady=10)
        self.preview_frame.grid()

        # Set up Booking Preview heading (row 0)
        self.booking_preview_label = Label(self.preview_frame, text="Booking Preview", 
                                          font=("Arial 16 bold"), 
                                          bg=background_color, 
                                          fg="white",
                                          padx=10)
        self.booking_preview_label.grid(row=0, pady=(10,0))

        # Name / Phone Frame (row 1)
        self.name_phone_frame = Frame(self.preview_frame, bg=background_color, pady=10)
        self.name_phone_frame.grid(row=1, pady=(0,10)) 

        # Name text (row 0, column 0)
        self.name_label = Label(self.name_phone_frame, text="Name:", 
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                          fg="white",
                                          padx=10, pady=5)
        self.name_label.grid(row=0, column=0)

        # Phone text (row 0, column 1)
        self.phone_label = Label(self.name_phone_frame, text="Phone Number:", 
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                          fg="white",
                                          padx=10, pady=5)
        self.phone_label.grid(row=0, column=1)

        # Purchases text (row 2)
        self.purchases_label = Label(self.preview_frame, text="", 
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                          fg="white",
                                          padx=10, pady=5,
                                          justify=LEFT)
        self.purchases_label.grid(row=2)

        # Total cost text (row 3)
        self.total_label = Label(self.preview_frame, text="", 
                                          font=("Arial 14 bold"), 
                                          bg=background_color, 
                                          fg="white",
                                          padx=10, pady=5,
                                          justify=LEFT)
        self.total_label.grid(row=3, pady=10)

        # Edit / Confirm Frame (row 4)
        self.edit_confirm_frame = Frame(self.preview_frame, bg=background_color, pady=10)
        self.edit_confirm_frame.grid(row=4, pady=(0,10)) 

        # Edit Button (row 0, column 0)
        self.edit_button = Button(self.edit_confirm_frame, text="Edit",
                                  font=("Arial 14"), 
                                  bg="#E4A024",         # yellow
                                  padx=10, pady=10,
                                  command=partial(self.close_preview, partner))
        self.edit_button.grid(row=0, column=0, padx=5)

        # Confirm Button (row 0, column 1)
        self.confirm_button = Button(self.edit_confirm_frame, text="Confirm",
                                  font=("Arial 14"), 
                                  bg="#E4A024",         # yellow
                                  padx=10, pady=10,
                                  command=lambda: self.confirm_booking(partner, bookings))
        self.confirm_button.grid(row=0, column=1, padx=5)

        self.show_details(partner)
        bookings = self.show_bookings(partner)


    def show_details(self, partner):
        self.name_label.configure(text="Name: {}".format(partner.name))
        self.phone_label.configure(text="Phone: {}".format(partner.phone_number))


    def show_bookings(self, partner):
        self.total_cost = 0
        self.from_palmers_seats = 0
        self.from_palmers_bunks = 0
        self.from_auckland_seats = 0
        self.from_auckland_bunks = 0

        if partner.is_yes_palmers == True and partner.is_yes_auckland == True:
            self.from_palmers_seats = int(float(partner.from_palmers_seats_entry.get()))
            self.from_palmers_bunks = int(float(partner.from_palmers_bunks_entry.get()))
            self.from_auckland_seats = int(float(partner.from_auckland_seats_entry.get()))
            self.from_auckland_bunks = int(float(partner.from_auckland_bunks_entry.get()))

            bookings = []

            if self.from_palmers_seats > 0:
                price = 25
                cost = self.from_palmers_seats * price

                booking = "Palmerston North to Auckland SEATS ${} x {} = ${}".format(price, self.from_palmers_seats, cost)
                bookings.append(booking)
                self.total_cost += cost
                
            if self.from_palmers_bunks > 0:
                price = 50
                cost = self.from_palmers_bunks * price

                booking = "Palmerston North to Auckland BUNKS ${} x {} = ${}".format(price, self.from_palmers_bunks, cost)
                bookings.append(booking)
                self.total_cost += cost

            if self.from_auckland_seats > 0:
                price = 25
                cost = self.from_auckland_seats * price

                booking = "Auckland to Palmerston North SEATS ${} x {} = ${}".format(price, self.from_auckland_seats, cost)
                bookings.append(booking)
                self.total_cost += cost
                
            if self.from_auckland_bunks > 0:
                price = 50
                cost = self.from_auckland_bunks * price

                booking = "Auckland to Palmerston North BUNKS ${} x {} = ${}".format(price, self.from_auckland_bunks, cost)
                bookings.append(booking)
                self.total_cost += cost

            separator = "\n\n--------------------------------------------------------------------------\n\n"
            self.purchases_label.configure(text=separator.join(bookings))
            self.total_cost_calc()

            
        elif partner.is_yes_palmers == True:
            self.from_palmers_seats = int(float(partner.from_palmers_seats_entry.get()))
            self.from_palmers_bunks = int(float(partner.from_palmers_bunks_entry.get()))

            bookings = []

            if self.from_palmers_seats > 0:
                price = 25
                cost = self.from_palmers_seats * price

                booking = "Palmerston North to Auckland SEATS ${} x {} = ${}".format(price, self.from_palmers_seats, cost)
                bookings.append(booking)
                self.total_cost += cost
                
            if self.from_palmers_bunks > 0:
                price = 50
                cost = self.from_palmers_bunks * price

                booking = "Palmerston North to Auckland BUNKS ${} x {} = ${}".format(price, self.from_palmers_bunks, cost)
                bookings.append(booking)
                self.total_cost += cost

            separator = "\n\n--------------------------------------------------------------------------\n\n"
            self.purchases_label.configure(text=separator.join(bookings))
            self.total_cost_calc()


        elif partner.is_yes_auckland == True:
            self.from_auckland_seats = int(float(partner.from_auckland_seats_entry.get()))
            self.from_auckland_bunks = int(float(partner.from_auckland_bunks_entry.get()))

            bookings = []

            if self.from_auckland_seats > 0:
                price = 25
                cost = self.from_auckland_seats * price

                booking = "Auckland to Palmerston North SEATS ${} x {} = ${}".format(price, self.from_auckland_seats, cost)
                bookings.append(booking)
                self.total_cost += cost
                
            if self.from_auckland_bunks > 0:
                price = 50
                cost = self.from_auckland_bunks * price

                booking = "Auckland to Palmerston North BUNKS ${} x {} = ${}".format(price, self.from_auckland_bunks, cost)
                bookings.append(booking)
                self.total_cost += cost

            separator = "\n\n--------------------------------------------------------------------------\n\n"
            self.purchases_label.configure(text=separator.join(bookings))
            self.total_cost_calc()

        return bookings


    def total_cost_calc(self):
        self.gst = self.total_cost - (self.total_cost / 1.15)
        self.gst_ex_cost = self.total_cost - self.gst
        self.total_label.configure(text="COST ${:0.2f}\nGST ${:0.2f}\nTOTAL ${:0.2f}".format(self.gst_ex_cost,
                                                                                             self.gst, self.total_cost))

       
    def confirm_booking(self, partner, bookings):
        separator = "\n------------------------------------------------\n"
        partner.partner.counter += 1
        filename = "booking" + str(partner.partner.counter) + ".txt"

        # Create file to hold data
        f = open(filename, "w+")

        f.write("booking{}\nName: {}\nPhone: {}\n\n{}\n\nCOST ${:0.2f}\nGST ${:0.2f}\nTOTAL ${:0.2f}".format(str(partner.partner.counter), 
                partner.name, partner.phone_number, separator.join(bookings), self.gst_ex_cost, self.gst, self.total_cost))

        # Close file
        f.close()

        # Close dialogue
        self.close_preview(partner)
        partner.error_label.configure(text="Your booking has been confirmed!", font=("Arial 14 bold"))

        self.update_seats_bunks(partner)
    

    def update_seats_bunks(self, partner):
        partner.partner.total_palmers_seats -= self.from_palmers_seats
        partner.partner.total_palmers_bunks -= self.from_palmers_bunks
        partner.partner.total_auckland_seats -= self.from_auckland_seats
        partner.partner.total_auckland_bunks -= self.from_auckland_bunks

        if partner.is_yes_palmers:
            partner.from_palmers_remaining_seats_label.configure(text="({}/20 seats remaining)".format(partner.partner.total_palmers_seats))
            partner.from_palmers_remaining_bunks_label.configure(text="({}/15 bunks remaining)".format(partner.partner.total_palmers_bunks))

        if partner.is_yes_auckland:
            partner.from_auckland_remaining_seats_label.configure(text="({}/20 seats remaining)".format(partner.partner.total_auckland_seats))
            partner.from_auckland_remaining_bunks_label.configure(text="({}/15 bunks remaining)".format(partner.partner.total_auckland_bunks))


    def close_preview(self, partner):
        # Put preview button back to normal
        partner.preview_button.config(state=NORMAL)
        self.preview_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Bus Bookings")
    something = Details(root)
    root.mainloop()