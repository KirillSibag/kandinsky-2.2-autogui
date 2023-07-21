import pyautogui
from time import sleep
import pickle


try:
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
except Exception as ex:
    print("Error during unpickling object (Possibly unsupported):", ex)

diction = []

for i in data:
    a = str(i)
    diction.append(a[0:len(i)-1])


times = 100
m = ' '
d = ', '

# пауза и досрочное прекращение
pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True

# разрешение и позиция
pyautogui.size()
pyautogui.position()

def delay(time):
    sleep(time)
    
def ctrl(letter):
    pyautogui.hotkey('ctrl', letter)

def alt(lett):
    pyautogui.hotkey('alt', lett)

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




def main001():
    print("готов!")
    delay(6)
    for j in range(times):
        picture_names = []
        
        for i in range(10):
            ctrl('t')

            #перейти на сайт
            prnt('https://editor.fusionbrain.ai/')
            ent()
            delay(1.4)


            prompt = diction[0]
            diction.remove(diction[0])

            vb = random.randint(0, 2)
            
            if vb > 1:
                picture_names.append("a " + prompt + ", anime")
                #выбрать стиль
                mouse(150, 965)
                mouse(150, 400)
            else:
                picture_names.append("a " + prompt)
                

            mouse(800, 970)
            

            
            
            #ввести промпт
            prnt(prompt)
                 

            
            delay(0.2)

            #начать генерацию
            ctrl("enter")
            delay(0.2)

            

        ctrl('tab')
        file = open("fni.txt", "w+")
        for i in range(10):
            ctrl('w')
            #щелк по фотке
            mouse(950, 600)
            
            #загрузить
            
            mouse(860, 970)
            delay(0.4)
            
            #по сохранению
            mouse(1709, 167) 
            delay(0.3)

            h = 360
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
               

                #имя
                file.write(picture_names[i] + "\n")
                prnt(picture_names[i])
                
                ent()
                delay(0.3)
                
            mouse(1895, 10)
            delay(0.4)

        file.close()
        mouse(251, 1060)
        delay(0.1)
        mouse(251, 950)
        delay(0.3)
        ctrl('n')
        delay(0.5)

main001()
