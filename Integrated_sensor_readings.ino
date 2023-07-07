#include "HX711.h"

//RIGHT LOAD: Ports 7, 6
//LEFT LOAD:  Ports 9, 8
//PL PRESSURE:  Ports 5, 4
//ABD PRESSURE: Ports 3, 2




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


float calibration_factor1 = -7800;
float calibration_factor2 = -7800;
float calibration_factor3 = -1000;
float calibration_factor4 = -1000;


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
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0


  scale2.begin(DOUT2, CLK2);
  scale2.set_scale(calibration_factor2); 
  scale2.tare(); 

  
  scale3.begin(DOUT3, CLK3);
  scale3.set_scale(calibration_factor3); 
  scale3.tare();

  scale4.begin(DOUT4, CLK4);
  scale4.set_scale(calibration_factor4); 
  scale4.tare();
  //Serial.println("Readings:");
}

void loop() {
 

  //Calibrated readings:

  reading_right = 0.0098*(scale.get_units()*35.94); //RIGHT LOAD CELL
  reading_left = 0.0098*(scale2.get_units()*34.91); //LEFT LOAD CELL
  
  pl_press = 0.129*scale3.get_units();               //PL PRESSURE
  ab_press = 0.130*scale4.get_units();              //ABD PRESSURE


  Serial.print(reading_right);
  Serial.print(" ");
  
  Serial.print(reading_left);
  Serial.print(" ");
  
  Serial.print(ab_press);
  Serial.print(" ");
  
  Serial.println(pl_press);
  
  
}
