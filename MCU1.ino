#include <EEPROM.h>

unsigned int i = 0, k =0;

void setup() {
  Serial.begin(2400); // Set the baud rate to 2400 bps (bits per second)
}

void loop() {
// Example: receiving data
if(Serial.available()>0){
  char read_char_serial=Serial.read();
  if(i<1024){
    EEPROM.write(i,read_char_serial);
    i++;
  }
}
else{
  if(k<=i){
  char read_EEPROM_char=EEPROM.read(k);
  Serial.print(read_EEPROM_char);
  k++;
  }
}
}
  