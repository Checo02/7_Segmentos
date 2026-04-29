int seg[] = {3, 4, 5, 6, 7, 8, 9}; // A, B, C, D, E, F, G

byte numeros[10][7] = {
  {1,1,1,1,1,1,0}, // 0
  {0,1,1,0,0,0,0}, // 1
  {1,1,0,1,1,0,1}, // 2
  {1,1,1,1,0,0,1}, // 3
  {0,1,1,0,0,1,1}, // 4
  {1,0,1,1,0,1,1}, // 5
  {1,0,1,1,1,1,1}, // 6
  {1,1,1,0,0,0,0}, // 7
  {1,1,1,1,1,1,1}, // 8
  {1,1,1,1,0,1,1}  // 9
};

void mostrarNumero(int n) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(seg[i], numeros[n][i]);
  }
}

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 7; i++) {
    pinMode(seg[i], OUTPUT);
  }

  mostrarNumero(0);
}

void loop() {
  if (Serial.available() > 0) {
    char dato = Serial.read();

    if (dato >= '0' && dato <= '9') {
      int numero = dato - '0';
      mostrarNumero(numero);
    }
  }
}
