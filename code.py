import board
import busio
import displayio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())




keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D3, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        # Fila 1: Control de Audio (Silenciar, Bajar Vol, Subir Vol)
        KC.MUTE,                 KC.VOLD,                KC.VOLU,
        
        # Fila 2: Reproducción (Anterior, Play/Pausa, Siguiente)
        KC.MEDIA_PREV_TRACK,     KC.MEDIA_PLAY_PAUSE,    KC.MEDIA_NEXT_TRACK,
        
        # Fila 3: Atajos del Sistema (Copiar, Pegar, Deshacer)
        KC.LCTL(KC.C),           KC.LCTL(KC.V),          KC.LCTL(KC.Z),
    ]
]
try:
    displayio.release_displays()
    i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
    
   
    display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    
   
    display.fill(0)
    display.text(" MACROPAD 3x3 ", 10, 5, 1)
    display.text("  KMK Ready!  ", 10, 20, 1)
    display.show()
except Exception as e:
    print("OLED no detectada o error de I2C:", e)

if __name__ == '__main__':
    keyboard.go()
