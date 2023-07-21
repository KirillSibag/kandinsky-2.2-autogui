## импорт необходимых библиотек
import pyautogui
from time import sleep
import pickle

## открытие файла с запросами
try:
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
except Exception as ex:
    print("Error during unpickling object (Possibly unsupported):", ex)

diction = []
for i in data:
    a = str(i)
    diction.append(a[0:len(i)-1])

## циклов по 10 генераций
times = 100
m = ' '
d = ', '

# пауза и досрочное прекращение
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

# разрешение и позиция
pyautogui.size()
pyautogui.position()

## функция ожидания
def delay(time):
    sleep(time)

## горячие клавиши
def ctrl(letter):
    pyautogui.hotkey('ctrl', letter)

def alt(lett):
    pyautogui.hotkey('alt', lett)

## перемещение мыши, клик и энтер
def mouse(x, y):
    pyautogui.moveTo(x, y, duration=0)
    cl()

def cl():
    pyautogui.click()

def prnt(text):
    pyautogui.typewrite(text, interval=0.0)

def ent():
    pyautogui.press('enter')

def move(x, y):
    pyautogui.moveTo(x, y, duration=0)



##главная функция
def main001():
    print("готов!")
    ## ожидание 6 секунд
    delay(6)

    ## цикл циклов генерации
    for j in range(times):
        ## список для сохранения имён изображений
        picture_names = []

        ## 10 раз генерация. Пока происходит вбивание новых 
        ## запросов, старые генерации завершаются
        for i in range(10):
            ## новая вкладка
            ctrl('t')

            #перейти на сайт
            prnt('https://editor.fusionbrain.ai/')
            ent()
            delay(1.4)

            
            ## запрос
            prompt = diction[0]
            ## больше не используем
            diction.remove(diction[0])

            ## стиль: обычный или аниме
            vb = random.randint(0, 2)
            
            if vb > 1:
                picture_names.append("a " + prompt + ", anime")
                #выбрать стиль
                mouse(150, 965)
                mouse(150, 400)
            else:
                picture_names.append("a " + prompt)
                

            ## клик на поле запроса
            mouse(800, 970)
            
            #ввести промпт
            prnt(prompt)
            delay(0.2)

            #начать генерацию
            ctrl("enter")
            delay(0.2)

            
        ## переход на первую пустую вкладку и её закрытие
        ctrl('tab')
        ## здесь сохранятся все названия сохранённых изображений:
        file = open("fni.txt", "w+")
        for i in range(10):
            ctrl('w')
            #щелк по фотке
            mouse(950, 600)
            
            #загрузить (значок папки)
            mouse(860, 970)
            delay(0.4)
            
            #по сохранению (значок папки рядом с фоткой)
            mouse(1709, 167) 
            delay(0.3)

            ## пока не добрались до подсвеченного - идём вниз
            h = 354
            corr = 0
            count = 0
            while corr == 0 and count < 15:
                delay(0.2)
                h += 23
                move(395, h)
                x, y = pyautogui.position()
                px = pyautogui.pixel(x, y)
                if px[0] <= 217:
                    corr = 1
                count += 1

            if count < 15:
                #по названию
                cl()
                delay(0.6)
               

                # переименовываем и пишем в файл
                file.write(picture_names[i] + "\n")
                prnt(picture_names[i])
                
                ent()
                delay(0.3)

            ## зкрываем окно загрузок
            mouse(1895, 10)
            delay(0.4)

        ## тыкаем по иконке файрфокса
        file.close()
        mouse(251, 1060)
        delay(0.1)
        ## выбираем вкладку
        mouse(251, 950)
        delay(0.3)
        ## делаем новую вкладку
        ctrl('n')
        delay(0.5)

main001()
