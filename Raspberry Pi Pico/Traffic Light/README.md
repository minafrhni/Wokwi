# Raspberry Pi Pico Traffic Light with 7-Segment Countdown

This project simulates a real-world traffic light system using the Raspberry Pi Pico. It features:
- Red, yellow, and green LEDs
- A 7-segment display showing countdown timer for each light

### 🔧 Hardware Used
- Raspberry Pi Pico
- 3 LEDs (Red, Yellow, Green)
- 7-segment display (common cathode)
- Resistors and wires

### 🚦 Logic
- Red light: 5-second countdown
- Yellow light: 1 second
- Green light: 5-second countdown
- Yellow light: 1 second

### 🧠 How it works
The 7-segment display is controlled by 7 GPIO pins, using bitwise patterns for digits 0-9. LEDs are turned on/off based on the current phase of the traffic light.

### 📂 Files
- `main.py`: Contains the full code
- `diagram.json`: Contains diagram

### 🛠️ Future Improvements
- Add button input to pause/reset
- Add buzzer for sound alert
- Use I2C 7-segment display for fewer GPIOs

### ✅ Simulation
This project was tested using [Wokwi Simulator](https://wokwi.com), which supports Raspberry Pi Pico.
You can run the simulation directly in your browser: [Open Project in Wokwi](https://wokwi.com/projects/436000466121049089)
