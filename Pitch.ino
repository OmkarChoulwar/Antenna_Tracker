#include <Servo.h>
Servo s1;
String t1;
int j=0;
float t2;
void setup()
{Serial.begin(9600);
s1.attach(9);
s1.writeMicroseconds(1210);
  }
  void loop()
  {
    while(Serial.available())
  {
   t1 = Serial.readStringUntil('\n');
    if (t1.toInt()>=0)
{Serial.print("forward");
    t2 = map(t1.toInt(),0,180,1250,1750);
     s1.writeMicroseconds(t2);
        Serial.println(t2);
      j++;
      }
      else if (t1.toInt()<0)
      {Serial.print("backward");
      
   t2 = map(t1.toInt(),-180,0,1750,1250);
     s1.writeMicroseconds(t2);
        Serial.println(t2);
        
        j++;
        }
        
    

     
      
        
    
  
  

  }
  }
