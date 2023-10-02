# # 🎄 🌊 🚁 🟩 🔥 🏥 💛 🪣 🏪 ☁️ ⚡ 🏆
import time
import os
from map import Map
from helicopter import Helicopter as Helio
import keyboard


# import keyboard
#
# # Установите обработчик событий клавиатуры
def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        print(f"Нажата клавиша: {e.name}")


#
# # Зарегистрируйте обработчик для всех клавиш
keyboard.hook(on_key_event)
#
# # Включите обработку клавиш
# keyboard.wait("esc")  # Ожидание нажатия клавиши "esc"


TICK_SLEEP = 0.05
TICK_UPDATE = 150
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    tmp = Map(MAP_W, MAP_H)
    tmp.generate_forest(3, 10)
    tmp.generate_river(10)

    helio = Helio(MAP_W, MAP_H)

    tick = 1
    while True:
        clear_console()
        print("TICK", tick)
        tmp.print_map(helio)
        tick += 1
        time.sleep(TICK_SLEEP)
        if tick % TICK_UPDATE == 0:
            tmp.generate_tree()
        if tick % FIRE_UPDATE == 0:
            tmp.update_fires()


if __name__ == "__main__":
    main()
