# Bus Booking System - Go Student Bus: Massey Overnighter

A Python GUI application for booking bus transportation between Palmerston North and Auckland, designed for students travelling to/from Massey University events.

## Overview

This application provides a user-friendly interface for booking bus seats and bunks on overnight services between Palmerston North and Auckland. It features real-time availability tracking, comprehensive input validation, booking preview functionality, and automated booking confirmation with receipt generation.

## Features

### Core Functionality
- **Dual Route Booking**: Book one-way trips from Palmerston North to Auckland or Auckland to Palmerston North
- **Flexible Seating Options**: Choose between regular seats ($25) or bunks ($50) for overnight comfort
- **Real-time Availability**: Live tracking of remaining seats and bunks (20 seats, 15 bunks per service)
- **Multi-service Booking**: Book both directions in a single transaction

### User Interface
- **Professional Design**: Dark blue theme with yellow accents matching company branding
- **Intuitive Navigation**: Step-by-step booking process with clear visual feedback
- **Error Handling**: Comprehensive input validation with highlighted error fields
- **Responsive Layout**: Clean, organised layout with proper spacing and typography

### Booking Management
- **Input Validation**: Phone number format checking (9-11 digits, numbers only)
- **Availability Checking**: Prevents overbooking with real-time capacity updates
- **Booking Preview**: Detailed summary before confirmation, including itemised costs
- **Receipt Generation**: Automatic creation of booking confirmation files

### Financial Features
- **Transparent Pricing**: Clear pricing structure with GST calculation
- **Cost Breakdown**: Detailed invoice showing individual items, GST, and total
- **Multiple Payment Items**: Support for booking multiple seat/bunk combinations

## Technical Specifications

### Requirements
- Python 3.x
- tkinter (standard library)
- tkmacosx (for enhanced button styling on macOS)
- functools (standard library)
- re (regular expressions, standard library)

### Architecture
The application follows an object-oriented design with three main classes:

1. **Details Class**: Main entry form handling user information and route selection
2. **Booking Class**: Seat/bunk selection interface with availability management
3. **Preview Class**: Booking confirmation and payment processing

### File Structure
```
Bus Bookings/
├── app.py              # Main application file
├── booking1.txt        # Generated booking receipts
├── booking2.txt        # (created automatically)
└── ...                 # Additional booking files
```

## Installation

1. Ensure Python 3.x is installed on your system

2. Install required dependencies:
```bash
pip install tkmacosx
```

3. Download the application:
```bash
# Place app.py in your desired directory
```

4. Run the application:
```bash
python app.py
```

## Usage Guide

### Step 1: Personal Information
1. Enter your full name in the "Name" field
2. Enter your mobile number (9-11 digits, no spaces or special characters)
3. Select your desired route(s):
   - Palmerston North to Auckland
   - Auckland to Palmerston North
   - Both directions (round trip)

### Step 2: Seat Selection
1. Choose the number of regular seats needed (capacity: 20 per service)
2. Choose the number of bunks needed (capacity: 15 per service)
3. View real-time availability for each option
4. Click "Preview Booking" to continue

### Step 3: Booking Confirmation
1. Review your booking details and pricing
2. Verify personal information accuracy
3. Check the itemised cost breakdown, including GST
4. Choose "Edit" to make changes or "Confirm" to complete the booking

### Step 4: Receipt
- Booking confirmation file automatically generated
- File saved as "booking[number].txt" in application directory
- Contains complete booking details and payment information

## Pricing Structure

| Service Type | Route | Price |
|-------------|--------|-------|
| Regular Seat | Any direction | $25.00 |
| Bunk | Any direction | $50.00 |

*All prices include 15% GST*

## Capacity Limits

- **Seats**: 20 available per service direction
- **Bunks**: 15 available per service direction
- Real-time tracking prevents overbooking
- Availability updates automatically after each confirmed booking

## Input Validation

### Name Requirements
- Cannot be empty
- Any alphabetic characters accepted

### Phone Number Requirements
- Must be 9-11 digits long
- Numbers only (0-9)
- No spaces or special characters
- No international prefixes

### Booking Requirements
- At least one route must be selected
- At least one seat or bunk must be requested per selected route
- Cannot exceed available capacity
- Must be positive integers only

## Error Handling

The application provides comprehensive error feedback:

- **Visual Indicators**: Error fields highlighted in light red
- **Descriptive Messages**: Specific error descriptions displayed
- **Field Validation**: Real-time checking prevents invalid submissions
- **Capacity Warnings**: Clear notifications when services are full

## File Output

Confirmed bookings generate text files with the format:
```
booking[number]
Name: [Customer Name]
Phone: [Phone Number]

------------------------------------------------
[Service] SEATS/BUNKS $[price] x [quantity] = $[total]
------------------------------------------------

COST $[subtotal]
GST $[gst_amount]
TOTAL $[final_total]
```

## Version History

**Version 11**: Added functionality to update seat and bunk totals after booking confirmation, ensuring accurate availability tracking across multiple bookings.

## System Requirements

- **Operating System**: Windows, macOS, Linux
- **Python Version**: 3.6 or higher
- **Memory**: Minimum 64MB RAM
- **Storage**: 10MB free space for application and booking files
- **Display**: Minimum 800x600 resolution

## Support

For technical issues or booking inquiries, refer to the application's built-in validation messages and error handling system. All booking confirmations are automatically saved locally for record-keeping purposes.

## License

This application is designed for educational and internal use for Go Student Bus services between Palmerston North and Auckland for Massey University events.
