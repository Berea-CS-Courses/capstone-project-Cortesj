/*
 Settings File

 Defines all the external variables required for the code to fucntion. This is
 the area where you specify the Wifi credentials for a WPA connection. Also, the
 location to define the type of DHT sensor and set the digital pin to be used as input.
 */

// WiFi Credentials
#define SECRET_SSID "Bruh"
#define SECRET_PASS "F4nflove!$"

// Sensor Type & Sensor DIGITAL Pin
#define DHTPIN 2
#define DHTTYPE DHT22 // DHT11 & DHT22 are valid options

// Location & Sensor number
#define LOCATION "greenhouse_1"
#define SENSOR_NUM "1"

// PHP Server Address (Local Machine)
// Ensure IP is static in DCHP Server
#define PHP_ADDRESS "192.168.0.150"
