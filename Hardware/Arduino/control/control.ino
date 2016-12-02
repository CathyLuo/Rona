int do_key = ;
int do_led = ;
int re_key = ;
int re_led = ; 
int mi_key = ;
int mi_led = ;
int fa_key = ;
int fa_led = ;
int so_key = ;
int so_led = ;
int la_key = ;
int la_led = ;
int si_key = ;
int si_led = ;
int high_do_key = ;
int high_do_led = ;

int high_key = ;
int high_led = ;
int mid_key = ;
int mid_led = ;
int low_key = ;
int low_led = ;

int piano_key = ;
int piano_led = ;
int guitar_key = ;
int guitar_led = ;
int xylophone_key = ;
int xylophone_led = ;

int teach_key = ;
int teach_led = ; 
int record_key = ;
int record_led = ;

typedef strcut _send_packet{
  unsigned char head;
  unsigned char key;
  unsigned char music_type;
  unsigned char function_mode;
  unsigned char action;
}send_packet;

void setup() {
  pinMode(do_key, INPUT);
  pinMode(re_key, INPUT);
  pinMode(mi_key, INPUT);
  pinMode(fa_key, INPUT);
  pinMode(so_key, INPUT);
  pinMode(la_key, INPUT);
  pinMode(si_key, INPUT);
  pinMode(high_do_key, INPUT);
  
  pinMode(high_key, INPUT);
  pinMode(mid_key, INPUT);
  pinMode(low_key, INPUT);
  
  pinMode(piano_key, INPUT);
  pinMode(guitar_key, INPUT);
  pinMode(xylophone_key, INPUT);
  
  pinMode(teach_key, INPUT);
  pinMode(record_key, INPUT);

  pinMode(do_led,OUTPUT);
  pinMode(re_led,OUTPUT);
  pinMode(mi_led,OUTPUT);
  pinMode(fa_led,OUTPUT);
  pinMode(so_led,OUTPUT);
  pinMode(la_led,OUTPUT);
  pinMode(si_led,OUTPUT);
  pinMode(high_do_led,OUTPUT);
  
  pinMode(high_led,OUTPUT);
  pinMode(mid_led,OUTPUT);
  pinMode(low_led,OUTPUT);
  
  pinMode(piano_led,OUTPUT);
  pinMode(guitar_led,OUTPUT);
  pinMode(xylophone_led,OUTPUT);
  
  pinMode(teach,OUTPUT);
  pinMode(record,OUTPUT);

  digitalWrite(do_led, LOW);
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  digitalWrite();
  
  Serial.begin(9600);
  
  send_packet pac = {0,0,0,0};

  unsigned char teach_flg = digitalRead(teach_key);
  unsigned char record_flg = digitalRead(record_key)
  unsigned char music_type_flg = 0;
  unsigned char music_region_flg = 0;
}



void loop() {
  while(Serial.available() > 0)
  {
      if(teach_flg != digitalRead(teach_key))
      {
        
      }
      if(record_flg != digitalRead(record_key))
      {
        
      }
      
  }
}
