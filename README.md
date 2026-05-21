<h1>MicroPython-OLED-temperature-sensor</h1>

<h2>Description</h2>
This is a small MicroPython project that reads the built-in temperature sensor on a microcontroller and shows the value on a 0.96” SSD1306 OLED screen. It continuously takes readings, converts the raw sensor data into degrees Celsius, and updates the display every couple of seconds so you can see the temperature in real time.

It uses the `machine` module to handle the ADC and I2C communication, and the OLED is driven using the SSD1306 library. The screen is cleared and refreshed each loop to keep the display clean and easy to read.

Overall, it’s a simple setup that combines basic sensor reading with a visual output, making it a good starting point for learning how to work with MicroPython hardware and small displays.
<br />


<h2>Technologies Used</h2>

- MicroPython
- Python (embedded systems)

<h2>Hardware Used</h2>

- Raspberry Pi Pico 
- 0.96” SSD1306 OLED Display 
- Built-in Temperature Sensor
- Breadboard and jumper wires
  
---

<h2>How It Works</h2>

<p>
The system continuously reads temperature data from the microcontroller’s built-in ADC sensor. This raw value is converted into degrees Celsius using a simple formula, then sent to the OLED display.
</p>

<p>
Every 2 seconds, the screen is cleared and updated with the latest temperature reading. This creates a real-time display that is easy to read and always up to date.
</p>

<p>
The MicroPython <b>machine</b> module handles both the ADC reading and I2C communication with the OLED screen, while the SSD1306 library is used to render text on the display.
</p>
<br/>

<h2>🔌 Wiring Connections (GPIO Pins)</h2>

<table>
  <tr>
    <th>OLED Pin</th>
    <th>Raspberry Pi Pico Pin</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>VCC</td>
    <td>3.3V</td>
    <td>Power supply</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>GND</td>
    <td>Ground connection</td>
  </tr>
  <tr>
    <td>SDA</td>
    <td>GP8</td>
    <td>I2C Data line</td>
  </tr>
  <tr>
    <td>SCL</td>
    <td>GP9</td>
    <td>I2C Clock line</td>
  </tr>
</table>
<br/>

---

<!--
```diff
- red text (errors)
+ green text (adds)
! orange text (warnings)
# gray text (notes)
@@ purple bold text (important)@@
