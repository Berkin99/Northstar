
#include <SPI.h>
#include "RF24.h"

#include "ntrp.h"
#include "ntrp_router.h"

RF24 rfmodule(8,9);
NTRP_Router router(&Serial,&rfmodule);

void setup() {
  Serial.begin(115200);
  
  if(!rfmodule.begin())while(1);
  if(!router.sync()) while(1);

  delay(100);
  router.debug("NTRP Router Start v.5");
  
}

void loop() {
  router.task();
}
