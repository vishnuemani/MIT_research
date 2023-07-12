#include "HX711.h"

//PL PRESSURE: Ports 7, 6
//ABD PRESSURE:  Ports 9, 8
//LEFT LOAD:  Ports 5, 4
//RIGHT LOAD: Ports 3, 2




#define DOUT 7
#define CLK  6

#define DOUT2 9
#define CLK2  8

#define DOUT3 5
#define CLK3  4

#define DOUT4 3
#define CLK4  2


HX711 scale;
HX711 scale2;
HX711 scale3;
HX711 scale4;



float reading_right; 
float reading_left;
float pl_press;
float ab_press;


float calibration_factor1 = -1000;
float calibration_factor2 = -1000;
float calibration_factor3 = -7800;
float calibration_factor4 = -7800;


void setup() {
  Serial.begin(9600);

  pinMode(9, INPUT);
  pinMode(8, INPUT);
  
  pinMode(7, INPUT);
  pinMode(6, INPUT);

  pinMode(5, INPUT);
  pinMode(4, INPUT);
  
  pinMode(3, INPUT);
  pinMode(2, INPUT);

  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor1); //This value is obtained by using the SparkFun_HX711_Calibration sketch

  
  //scale.tare();


  scale2.begin(DOUT2, CLK2);
  scale2.set_scale(calibration_factor2); 
  //scale2.tare(); 

  
  scale3.begin(DOUT3, CLK3);
  scale3.set_scale(calibration_factor3); 
  //scale3.tare();

  scale4.begin(DOUT4, CLK4);
  scale4.set_scale(calibration_factor4); 
  //scale4.tare();
  
}

void loop() {


  /*
   * B VALUES:
   * 
   * PL PRESS (-70.3)
   * ABD PRESS (650)
   * RIGHT LOAD (-18.5)
   * LEFT LOAD (14.8)
   * 
  */

  


  
  
  Serial.print(0.129*(scale.get_units()-70.3)); //PL PRESS (yellow)

  Serial.print(" ");

  Serial.println(0.130*(scale2.get_units()+650)); //ABD PRESS

  Serial.print(" ");
  

  Serial.print(0.0098*((scale3.get_units()-18.50)*35.94)); //RIGHT LOAD

  Serial.print(" ");
  
  Serial.print(0.0098*((scale4.get_units()+14.8)*34.91)); //LEFT LOAD

  

  

  

  
  
  
  
}
