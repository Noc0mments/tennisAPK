from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import requests

red = [1, 0, 0, 1]
blue = [0, 0, 1, 1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)

        btnR = Button(text="0",
                      background_color=red,
                      font_size=300
                         )
        btnR.background_down = btnR.background_disabled_normal
        btnR.bind(on_press=self.on_press_button)
        layout.add_widget(btnR)
        btnB = Button(text="0",
                      background_color=blue,
                      font_size=300,
                      )
        btnB.bind(on_press=self.on_press_button)
        layout.add_widget(btnB)
        return layout

    def on_press_button(self, instance):
        if instance.background_color==red:
            redScore=int(instance.text)
            redScore+=1
            instance.text=str(redScore)
            data={'c': 'r', 'd': redScore}
        elif instance.background_color==blue:
            blueScore = int(instance.text)
            blueScore += 1
            instance.text = str(blueScore)
            data={'c': 'b', 'd': blueScore}
        requests.post('http://172.16.5.240:4567/score', json=data)

    def on_press_button_blue(self, instance):
        print('Вы нажали на синюю кнопку!')


if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()