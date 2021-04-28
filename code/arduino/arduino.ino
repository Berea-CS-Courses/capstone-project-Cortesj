/*
Arduino Code for Wifi Connection & Sensor Readout

Built with Arduino Nano 33 IoT & DHT22 Sensor
 */

// Import Libraries
#include <SPI.h>
#include <WiFiNINA.h>
#include "DHT.h"

// Import Settings for Wifi, etc...
#include "settings.h"

// Import WiFi Credentials from "Settings.h"
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int status = WL_IDLE_STATUS;     // the WiFi radio's status

// Initialize DHTxx Sensor Class
DHT dht(DHTPIN, DHTTYPE);

// Initialize Temperature & Humidity Data
float humidityData;
float temperatureData;

// Declare Connection Client | (WifiNINA Client)
WiFiClient client;

// PHP Server Address
char server[] = PHP_ADDRESS;

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);

  // Check for WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  // Start Sensor Data Readings
  dht.begin();

  // Attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  // Connection Successful, so print out the data:
  Serial.print("You're connected to the network");
  printCurrentNet();
  printWifiData();
}

void loop() {
  // Delay main loop every 10 Seconds
  delay(10000);

  // Functions to execute
  printCurrentNet();
  read_sensor();
  php_connect();
  reconnect();
}

void read_sensor() {
  // Read Sensor and save to variable
  humidityData = dht.readHumidity();
  temperatureData = dht.readTemperature(true);

  // Print out to Serial for Debug
  Serial.print("Humidity Data: ");
  Serial.println(humidityData);
  Serial.print("Temperature Data: ");
  Serial.println(temperatureData);
  Serial.println("");
}

void reconnect() {
  // Check for Disconnect/Connection Lost status to reconnect WiFi
  int status;
  status = WiFi.status();

  if (status == WL_DISCONNECTED || status == WL_CONNECTION_LOST){
    while (status != WL_CONNECTED){
      status = WiFi.begin(ssid, pass);
      delay(10000);
    }
  }
}

void php_connect() {
  // Connect client to PHP script on localhost
  if (client.connect(server, 80)){
    Serial.print("Connection Successful!");
    Serial.println(" ");
    // HTTP Request
    Serial.print("GET /test/dht.php?humidity=");
    client.print("GET /test/dht.php?humidity=");     //YOUR URL
    Serial.print(humidityData);
    client.print(humidityData);
    client.print("&temperature=");
    Serial.print("&temperature=");
    client.print(temperatureData);
    Serial.print(temperatureData);
    client.print(" ");      //SPACE BEFORE HTTP/1.1
    client.print("HTTP/1.1");
    client.println();
    client.println("Host: 192.168.0.175");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Connection Failed!");
    Serial.println("");
  }
}

void printWifiData() {
  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print your MAC address:
  byte mac[6];
  WiFi.macAddress(mac);
  Serial.print("MAC address: ");
  printMacAddress(mac);
}

void printCurrentNet() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print the MAC address of the router you're attached to:
  byte bssid[6];
  WiFi.BSSID(bssid);
  Serial.print("BSSID: ");
  printMacAddress(bssid);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.println(rssi);

  // print the encryption type:
  byte encryption = WiFi.encryptionType();
  Serial.print("Encryption Type:");
  Serial.println(encryption, HEX);
  Serial.println();
}

void printMacAddress(byte mac[]) {
  for (int i = 5; i >= 0; i--) {
    if (mac[i] < 16) {
      Serial.print("0");
    }
    Serial.print(mac[i], HEX);
    if (i > 0) {
      Serial.print(":");
    }
  }
  Serial.println();
}
