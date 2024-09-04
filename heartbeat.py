import time
from max30102 import max30102
from max30102 import hrcalc

# Initialize the MAX30102 sensor
m = max30102.MAX30102()

# Record the start time
start_time = time.time()

try:
    while True:
    # Read the LED values
        red, ir = m.read_sequential()

    # Print the readings
    # print(red, ir)
    #print('\n\n')

    # Calculate and print heart rate and SpO2
        print(f'my heart rate -> {hrcalc.calc_hr_and_spo2(ir[:100], red[:100])}')



except KeyboardInterrupt:

    # Check if 30 seconds have passed
    # current_time = time.time()
    # print(current_time)
    # if current_time - start_time > 30:
    #     break

# Shutdown the sensor
    m.shutdown()
