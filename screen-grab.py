from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

#smtp import
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

options = webdriver.ChromeOptions()


#chrome headless option
options.add_argument('headless')


# set the window size
options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)


#to to url
driver.get('https://datastudio.google.com/u/0/reporting/0B_U5RNpwhcE6QXg4SXFBVGUwMjg/page/6zXD/preview')


#enter email address
email = driver.find_element_by_css_selector('input[type=email]')
email.send_keys('exaple@gmail.com')
email.send_keys(Keys.ENTER)

time.sleep(5)

#enter password
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

password.send_keys('password-here')
password.send_keys(Keys.ENTER)


# sleep up to 5 seconds for the elements to become available
time.sleep(5)


#take a screenshot of the page
driver.get_screenshot_as_file('./img/full-page.png')


time.sleep(2)

#smtp username details
email_user = 'example@gmail.com'
email_password = 'password-here'

#send email to
email_send = 'anthony_lekan@hotmail.com'


subject = 'Reading Headline'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

#send attached file
filename='./img/full-page.png'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)


driver.close()

