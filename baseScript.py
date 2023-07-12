# THIS IS A SCRIPT BY AN AMATEUR SCRIPT KIDDIE TO SEND EMAILS USING GMAIL AND SELENIUM. 
# ANY COMMENTS OR CONSTRUCTIVE CRITICISM ARE WELCOME.


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
#from config import EMAIL, PASSWORD
import pandas as pd
import random
import datetime
import time


# Time Frame
start_time = datetime.time(8, 0)
end_time = datetime.time(21, 0)

# The Most Important Random

list_0 = [90, 120, 90, 120, 90]

r1 = random.choice(list_0)

list_1 = [10]

r2 = random.choice(list_1)

list_2 = [20, 10, 20]

r3 = random.choice(list_2)

cap_1 = [8]

############################################

url = 'https://www.gmail.com'

gmail_username = 'example@gmail.com'
gmail_password = "password123"

email_subject = "Big Kahuna Burger Network Inc. (Proposal)"
html_content = """ 
To whom it may concern:

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac enim neque. Nullam vel 
metus sit amet sem venenatis laoreet. Mauris consequat auctor lacus, a pretium lacus hendrerit eu. 
Duis eget arcu feugiat, ullamcorper ex ac, tristique arcu. Nullam eget nisl turpis. 
Vivamus gravida euismod enim. Integer auctor feugiat mauris eget lacinia. 
Phasellus volutpat eu metus et malesuada.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; 
Morbi ullamcorper massa a diam gravida varius. Nulla facilisi. Integer nec justo 
eget purus pharetra facilisis id in turpis. Aenean posuere sagittis ligula, 
sed fringilla quam. Morbi in bibendum orci. Pellentesque habitant morbi tristique 
senectus et netus et malesuada fames ac turpis egestas. Mauris tristique convallis quam sed facilisis.

Proin euismod efficitur eros, a eleifend mi dapibus id. 
Sed scelerisque lacinia elit, ac tristique elit elementum eu. 
Ut tincidunt est at cursus fringilla. Integer a mi non orci dapibus feugiat. 
Aenean iaculis turpis at suscipit efficitur. Curabitur dignissim, elit eget rutrum rutrum, 
nulla mi iaculis sem, id ullamcorper metus lectus vitae eros. 
Donec interdum ligula ac diam dignissim rhoncus.

Sincerely,

John Smith
Big Kahuna Burgers Network Inc.
311 E BlUE GROVE BLVD, RIVERSIDE, CA. 91104
(646) 809-1548

"""

dataframe = pd.read_excel('data.xlsx')

driver = webdriver.Chrome(executable_path='PATH TO CHROMEDRIVER EXEC')
# Example ('C:\\Users\\User01\Documents\\Content\\')

driver.get(url)

# LOGGING IN

driver.implicitly_wait(r2)
driver.find_element("id", 'identifierId').send_keys(gmail_username)
driver.find_element("id", 'identifierNext').click()

time.sleep(5)
driver.implicitly_wait(r2)
driver.find_element("xpath",'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(gmail_password)

time.sleep(3)
driver.find_element("id",'passwordNext').click()
driver.implicitly_wait(r2)

while True:
    now = datetime.datetime.now()

    for index, i in enumerate(dataframe.index):
        now = datetime.datetime.now()
        if start_time <= now.time() <= end_time:
            print("El Script se esta ejecutando")

            time.sleep(r3)

            print(dataframe.loc[i]['Email'], end='\n\n')    

# CREATING THE EMAIL

# COMPOSE EMAIL BOTTOM

            time.sleep(3)
            try:
                driver.implicitly_wait(r2)
                driver.find_element("xpath", '/html/body/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div').click()

            except NoSuchElementException:

                try:
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '/html/body/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div').click()

                except:
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '/html/body/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div').click()    

# EMAIL SPACE

            time.sleep(3)
            try:
                driver.implicitly_wait(r2)
                driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input').send_keys(dataframe.loc[i]['Email'])

            except NoSuchElementException:

                try:
                    driver.implicitly_wait(r2)    
                    driver.find_element("xpath", '//*[@id=":v9"]').send_keys(dataframe.loc[i]['Email'])
                except:
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/input').send_keys(dataframe.loc[i]['Email'])
    

# EMAIL SUBJECT
            
            time.sleep(3)
            try:
                driver.implicitly_wait(r2)
                driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/input').send_keys(email_subject)

            except NoSuchElementException:

                try:
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '//*[@id=":p4"]').send_keys(email_subject)
                except:
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/input').send_keys(email_subject)

# HTML CONTENT

            time.sleep(3)
            try:
                driver.implicitly_wait(r2)
                driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div').send_keys(html_content)

            except NoSuchElementException:

                    try:
                        driver.implicitly_wait(r2)
                        driver.find_element("xpath", '//*[@id=":qc"]').send_keys(html_content)
                    except:
                        driver.implicitly_wait(r2)
                        driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[3]/div/table/tbody/tr/td[2]/div[2]/div').send_keys(html_content)

# UPLOAD ATTACHMENTS

            time.sleep(r3)

            s = driver.find_element("xpath", "//input[@type='file']")
            s.send_keys("C:\\Users\\User01\Documents\\Content\\burger_plan.pdf")

            time.sleep(1)

            s = driver.find_element("xpath", "//input[@type='file']")
            s.send_keys("C:\\Users\\User01\Documents\\Content\\restaurant_services.pdf")

# SEND EMAIL

            time.sleep(3)
            try:
                driver.implicitly_wait(r2)
                driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click() 

            except NoSuchElementException:

                try:
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '//*[@id=":ou"]').click()
                except: 
                    driver.implicitly_wait(r2)
                    driver.find_element("xpath", '/html/body/div[21]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click() 

# THE SCRIPT DOES NOT RUN OUTSIDE THE TIME BOUNDARIES.
    else:
        print("The script is outside the allowed schedule.")  

    now = datetime.datetime.now() 
    time.sleep(5)