
import RPi.GPIO as GPIO
import time

LED_PIN = 21        # BCM numbering
DELAY_SEC = 0.5     # seconds between toggles

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    print(f"LED connected to GPIO {LED_PIN}")

def loop():
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(DELAY_SEC)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(DELAY_SEC)

def cleanup():
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleaned up. Bye.")

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        cleanup()
