from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import scraper
import webdriverdownloader as wdd

# For Firefox gecko driver: 
gecko_dd = wdd.GeckoDriverDownloader()
gecko_dd.download_and_install()

# For Chrome driver:
# chrome_dd = wdd.ChromeDriverDownloader()
# chrome_dd.download_and_install()

# For Opera driver:
# opera_dd = wdd.OperaChromiumDriverDownloader()
# opera_dd.download_and_install()

class MyGrid(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    hashtags = ObjectProperty(None)
    
    def button(self):
        if self.username.text != '' and self.password.text != '' and len(self.hashtags.text) > 0:
            me = scraper.InstagramBot(self.username.text, self.password.text)
            me.login()
            print("Logged in as " + self.username.text)
            for hashtag in self.hashtags.text.split(','):
                me.like_posts_in(hashtag)
            else:
                print("Enter all the relevant inputs. Exiting program...")
                SystemExit()

        # me = scraper.InstagramBot(self.username.text, self.password.text, self.hashtags.text.split(','))
        
        

class IGBot(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    IGBot().run()

# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 1

#         self.inside = GridLayout()
#         self.inside.cols = 2
#         self.inside.add_widget(Label(text = "Username: "))
#         self.usernameIn = TextInput(multiline = False)
#         self.inside.add_widget(self.usernameIn)

#         self.inside.add_widget(Label(text = "Password: "))
#         self.passwordIn = TextInput(multiline = False)
#         self.inside.add_widget(self.passwordIn)

#         self.inside.add_widget(Label(text = "Hashtags: "))
#         self.hashtagsIn = TextInput(multiline = False)
#         self.inside.add_widget(self.hashtagsIn)

#         self.add_widget(self.inside)

#         self.submit = Button(text = "Submit", font_size = 40)
#         self.submit.bind(on_press = self.pressed)
#         self.add_widget(self.submit)

#     def pressed(self, instance):
#         uname = self.usernameIn.text
#         pwd = self.passwordIn.text
#         print(f"{uname}: {pwd}")
#         self.usernameIn.text = ''
#         self.passwordIn.text = ''
        

# class MyApp(App):
#     def build(self):
#         return MyGrid()
#         # return Label(text = "Label1")
    

# MyApp().run()