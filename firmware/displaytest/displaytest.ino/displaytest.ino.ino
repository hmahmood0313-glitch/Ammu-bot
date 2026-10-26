#include <Arduino_GFX_Library.h>

// pins: DC=9, CS=10, SCK=12, MOSI=11, RST=8
Arduino_DataBus *bus = new Arduino_ESP32SPI(9, 10, 12, 11, GFX_NOT_DEFINED);
Arduino_GFX *gfx = new Arduino_GC9A01(bus, 8, 0, true);

void setup() {
  gfx->begin();
  gfx->fillScreen(0x0000);              // black
  gfx->fillCircle(80, 110, 25, 0x07FF); // left eye (cyan)
  gfx->fillCircle(160, 110, 25, 0x07FF);// right eye
  gfx->setTextColor(0xFFFF);            // white
  gfx->setTextSize(2);
  gfx->setCursor(65, 170);
  gfx->print("I am AI!");
}

void loop() {}