#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

#define LED D4 // Led in NodeMCU at pin GPIO16 (D0).


const char* ssid = "BRAIN_VALLEY01";
const char* password = "secret";
bool ledOn = false;
char indexPage[256];

IPAddress ip(192, 168, 1, 128);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

ESP8266WebServer server(80);

void switchOn() {
  digitalWrite(LED, HIGH);
  ledOn = true;
  server.send(200, "text/html", "Turning on LED<br/><a href='/'>Home</a>");
}

void switchOff() {
  digitalWrite(LED, LOW);
  ledOn = false;
  server.send(200, "text/html", "Turning off LED<br/><a href='/'>Home</a>");
}

void serveIndex() {
  sprintf(indexPage, "<p>Led is currently switched %s.</p><a href='/on'>on</a><br/><a href='/off'>off</a>", ledOn ? "on" : "off");
  server.send(200, "text/html", indexPage);
}

void setup() {
  WiFi.config(ip, gateway, subnet);
  WiFi.begin(ssid, password);


  pinMode(LED, OUTPUT);
  // off by default
  digitalWrite(LED, LOW);
  ledOn = false;

  Serial.begin(115200);

  while (WiFi.status() != WL_CONNECTED) {
    delay(2000);
    Serial.print("Waiting for WiFi");
  }

 
  Serial.println(WiFi.localIP());


  server.on("/", serveIndex);
  server.on("/on", switchOn);
  server.on("/off", switchOff);

  server.begin();
}
void loop() {
  server.handleClient();
}
