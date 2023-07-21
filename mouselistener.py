from pynput import mouse

# Действие при движении курсора


# Действие при нажатии кнопки мыши
def on_click(x, y, button, is_pressed):
    print(f'Была {"нажата" if is_pressed else "отпущена"} '
          f'{x} , {y} ')



# Прослушка мыши
mouse_listener = mouse.Listener(
  
   on_click=on_click
)
# Старт прослушки мыши
mouse_listener.start()
 
# Здесь может выполняться другой код
 
# Остановка прослушки мыши
