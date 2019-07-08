#include <SD.h>
#include <TMRpcm.h>

#define Chip_SD 4

TMRpcm tmrpcm;

char lectura;

void setup(){

  pinMode(led, OUTPUT);
  Serial.begin(9600);
  tmrpcm.speakerPin = 9;
  if (!SD.begin(Chip_SD)){
    return;
  }
}

void loop (){
  
  delay(2400);
  Serial.begin(9600);
  if(Serial.available() >= 1){
    lectura = Serial.read();
    Serial.end();
    
  if (lectura == 'a'){
    //delay(2400);
    tmrpcm.setVolume(5);
    tmrpcm.play("objverde.wav");
  }

  if (lectura == 'b'){
    //delay(2400);
    tmrpcm.setVolume(5);
    tmrpcm.play("objazul.wav");
  
  }
  
  if (lectura == 'c'){
    //delay(2400);
    tmrpcm.setVolume(5);
    tmrpcm.play("objrojo.wav");
  }
  }}
