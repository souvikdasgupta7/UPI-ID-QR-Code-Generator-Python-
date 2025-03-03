import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Function to generate QR codes
def generate_qr():
    # Get the UPI ID and Amount from the entry fields
    upi_id = upi_id_entry.get()
    amount = amount_entry.get()

    if not upi_id or not amount:
        messagebox.showerror("Input Error", "Please enter both UPI ID and amount.")
        return

    try:
        # Try converting amount to float to ensure it's a valid number
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
        return

    # Define the payment URLs based on the UPI ID and Amount
    phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu=INR&tn=Payment%20for%20services'
    paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu=INR&tn=Payment%20for%20services'
    google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu=INR&tn=Payment%20for%20services'

    # Create QR codes for each payment app
    phonepe_qr = qrcode.make(phonepe_url)
    paytm_qr = qrcode.make(paytm_url)
    google_pay_qr = qrcode.make(google_pay_url)

    # Get the dimensions of the window to set the QR code size
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    # Calculate the size of the QR code based on the window dimensions (keeping a margin)
    qr_size = min(window_width, window_height) // 3  # 1/3 of the smallest dimension

    # Resize the QR codes according to the window size using LANCZOS resampling
    phonepe_qr_resized = phonepe_qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    paytm_qr_resized = paytm_qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    google_pay_qr_resized = google_pay_qr.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    # Convert the resized QR codes to images that can be displayed with Tkinter
    phonepe_qr_image = ImageTk.PhotoImage(phonepe_qr_resized)
    paytm_qr_image = ImageTk.PhotoImage(paytm_qr_resized)
    google_pay_qr_image = ImageTk.PhotoImage(google_pay_qr_resized)

    # Display the QR codes in the Tkinter window
    phonepe_label.config(image=phonepe_qr_image)
    phonepe_label.image = phonepe_qr_image
    paytm_label.config(image=paytm_qr_image)
    paytm_label.image = paytm_qr_image
    google_pay_label.config(image=google_pay_qr_image)
    google_pay_label.image = google_pay_qr_image

    # Save the QR codes as image files
    phonepe_qr_resized.save('phonepe_qr.png')
    paytm_qr_resized.save('paytm_qr.png')
    google_pay_qr_resized.save('google_pay_qr.png')

    # Show Payment Success Message
    success_label.config(text=f"Payment of ₹{amount} Successful!", fg="#4CAF50")

# Create the main Tkinter window
root = tk.Tk()
root.title("UPI QR Code Generator")
root.geometry("600x750")
root.config(bg="#f1f1f1")  # Set background color to light grey

# Title label
title_label = tk.Label(root, text="Generate UPI QR Codes", font=("Arial", 20, "bold"), bg="#ff6347", fg="white", pady=10)
title_label.pack(fill="x")

# Label for UPI ID input
upi_id_label = tk.Label(root, text="Enter your UPI ID:", font=("Arial", 14), bg="#f1f1f1", fg="#333333")
upi_id_label.pack(pady=10)

# Entry field for UPI ID
upi_id_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief="solid", fg="#333333", bg="white", justify="center")
upi_id_entry.pack(pady=10)

# Label for Amount input
amount_label = tk.Label(root, text="Enter the Amount:", font=("Arial", 14), bg="#f1f1f1", fg="#333333")
amount_label.pack(pady=10)

# Entry field for Amount
amount_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief="solid", fg="#333333", bg="white", justify="center")
amount_entry.pack(pady=10)

# Generate Button with more attractive styling
generate_button = tk.Button(root, text="Generate QR Codes", font=("Arial", 14), bg="#4CAF50", fg="white", width=20, height=2, command=generate_qr, relief="solid")
generate_button.pack(pady=20)

# Divider line
divider = tk.Label(root, text="-------------------------------------------------", bg="#f1f1f1")
divider.pack(pady=10)

# Labels to display the QR codes
qr_frame = tk.Frame(root, bg="#f1f1f1")
qr_frame.pack(pady=20)

phonepe_label = tk.Label(qr_frame, bg="#f1f1f1")
phonepe_label.grid(row=0, column=0, padx=20, pady=10)

paytm_label = tk.Label(qr_frame, bg="#f1f1f1")
paytm_label.grid(row=0, column=1, padx=20, pady=10)

google_pay_label = tk.Label(qr_frame, bg="#f1f1f1")
google_pay_label.grid(row=1, column=0, padx=20, pady=10)

# Success label
success_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f1f1f1", fg="#4CAF50")
success_label.pack(pady=20)

# Footer with additional information or instructions
footer_label = tk.Label(root, text="Scan the QR codes to make payments", font=("Arial", 10), bg="#f1f1f1", fg="#666666")
footer_label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
