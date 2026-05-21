import machine
import ssd1306
import utime

# Configure I2C communication pins (SCL and SDA)
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))

# Initialize the OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Function to read temperature from built-in sensor
def read_temperature():
    temp_sensor = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    raw_value = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (raw_value - 0.706) / 0.001721
    return round(temperature, 2)

# Main loop
while True:
    # Read temperature
    temperature = read_temperature()
    
    # Clear previous content
    oled.fill(0)
    
    # Write temperature to display
    oled.text("Temperature:", 0, 0)
    oled.text(str(temperature) + "C", 0, 20)
    
    # Update OLED display
    oled.show()
    
    # Wait for a moment before updating again
    utime.sleep(2)