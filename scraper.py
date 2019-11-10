from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import selenium

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        sleep(1)
        password.send_keys(self.password)
        sleep(1)
        password.send_keys(Keys.ENTER)
        sleep(3)

    def like_posts_in(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
        sleep(5)
        for i in range(2):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(2)
        
        """
            Algorithm:
            1. Find every post
            2. Click on it.
            3. Like it.
            4. Press escape
            5.Repeat procedure for next post.

        """
        posts = bot.find_elements_by_class_name('v1Nh3')
        print(type (posts))

        for post in posts:
            try:
                i = 1
                post.click()
                sleep(2)
                like_button = bot.find_element_by_class_name('fr66n').click()
                sleep(2)
                close_button = bot.find_element_by_class_name('ckWGn').click()
                sleep(2)
                i = i + 1
                if i == 29:
                    sleep(60 * 10)
                    i = 1
                    break
            except (selenium.common.exceptions.ElementClickInterceptedException):
                # Occurs when too many posts have been liked at a time interval. The 'Action Blocked' popup shows
                check_if_action_blocked = bot.find_element_by_class_name('RnEpo')
                if check_if_action_blocked != None:
                    click_ok = bot.find_element_by_class_name('RnEpo').click()
                    sleep(60 * 10)
                    break
            except (selenium.common.exceptions.ElementClickInterceptedException):
                # Occurs when too many posts have been liked at a time interval. The 'Action Blocked' popup shows
                check_if_action_blocked = bot.find_element_by_class_name('RnEpo')
                if check_if_action_blocked != None:
                    click_ok = bot.find_element_by_class_name('RnEpo').click()
                    sleep(60 * 10)
                    break
                
            except Exception as ex:
                print(ex)
            


# username = 'uname'
# password = '********'
# hashtags = ['cpp', 'c', 'java', 'python']

# if username != '' and password != '' and len(hashtags) > 0:
#     me = InstagramBot(username, password)
#     me.login()
#     print("Logged in as " + username)
#     for hashtag in hashtags:
#         me.like_posts_in(hashtag)
# else:
#     print("Enter all the relevant inputs")
