import RPi.GPIO as GPIO
import tkinter as tk

# Initialize GPIO using BOARD mode
GPIO.setmode(GPIO.BOARD)

# Set up GPIO for LEDs
Red_led = 35
Green_led = 38
Blue_led = 40

# Configure the pins as output
GPIO.setup(Red_led, GPIO.OUT)
GPIO.setup(Green_led, GPIO.OUT)
GPIO.setup(Blue_led, GPIO.OUT)

# Function to disable all LEDs
def switch_off_leds():
    GPIO.output(Red_led, GPIO.LOW)
    GPIO.output(Green_led, GPIO.LOW)
    GPIO.output(Blue_led, GPIO.LOW)

# Function to enable the selected LED
def switch_on_led(led_choice):
    switch_off_leds()
    if led_choice == 1:
        GPIO.output(Red_led, GPIO.HIGH)
    elif led_choice == 2:
        GPIO.output(Green_led, GPIO.HIGH)
    elif led_choice == 3:
        GPIO.output(Blue_led, GPIO.HIGH)

# Handle the LED selection
def control_led():
    selected_led = led_choice.get()
    switch_on_led(selected_led)

# Exit and clean up GPIO
def end_app():
    switch_off_leds()
    GPIO.cleanup()
    window.quit()

# Create the UI window
window = tk.Tk()
window.title("LED Controller")

# Variable to store the LED choice
led_choice = tk.IntVar()

# Create the UI elements
label = tk.Label(window, text="Control LED", font=("Arial", 20))
label.pack(pady=15)

# Creating radio buttons with corresponding LED colors
led_radio_c1 = tk.Radiobutton(window, text="Red LED", variable=led_choice, value=1, 
                              command=control_led, fg="red", selectcolor="red")
led_radio_c2 = tk.Radiobutton(window, text="Green LED", variable=led_choice, value=2, 
                              command=control_led, fg="green", selectcolor="green")
led_radio_c3 = tk.Radiobutton(window, text="Blue LED", variable=led_choice, value=3, 
                              command=control_led, fg="blue", selectcolor="blue")

led_radio_c1.pack(anchor=tk.W, padx=20)
led_radio_c2.pack(anchor=tk.W, padx=20)
led_radio_c3.pack(anchor=tk.W, padx=20)

reset_button = tk.Button(window, text="Turn Off All", command=switch_off_leds)
reset_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=end_app)
exit_button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
