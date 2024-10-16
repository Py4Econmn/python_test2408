import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import datetime
import smtplib # to connect to email client - pip install secure-smtplib
from email.mime.multipart import MIMEMultipart # managing email msg
from email.mime.text import MIMEText           # managing email msg
from email.mime.application import MIMEApplication
import config


def date_out_parse(date_out):
    # phrases = ["Өнөөдөр", "Өчигдөр", "өмнө"]
    idate = date_out

    if 'Өнөөдөр' in idate or 'цагийн өмнө' in idate or 'минут' in idate:
        dtdate = datetime.date.today()
    elif 'Өчигдөр' in idate:
        dtdate = datetime.date.today() - datetime.timedelta(days=1)
    elif 'өдрийн өмнө' in idate:
        ilag = re.search(r'\d{1}', idate).group().strip()
        dtdate = datetime.date.today() - datetime.timedelta(days=int(ilag))
    elif 'долоо хоногийн өмнө' in idate:
        ilag = re.search(r'\d{1}', idate).group().strip()
        dtdate = datetime.date.today() - datetime.timedelta(days=int(ilag)*7)
    else:
        dtdate = idate
        (f'Date was not parsed: {date_out}')

    return dtdate

def find_last_page():
    driver = webdriver.Chrome() 
    today = datetime.date.today()
    date_first = today
    page = 12

    while date_first >= today:
        page += 1
        main_page = f"https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/?page={page}&ordering=newest"
        driver.get(main_page)
        first_ad = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div")

        try: 
            date_first = first_ad.find_element(By.XPATH, "div[2]/div/div[4]/div[1]/div[1]").text
        except:
            date_first = first_ad.find_element(By.XPATH, "div[2]/div[2]/div[4]/div[1]/div[1]").text

        date_first = date_out_parse(date_first)

        print(f'Page {page}, first date: {date_first}')

    return page

def data_collection(page):
    data_list = []

    print(f'Working on page number: {page}')
    driver = webdriver.Chrome()
    main_page = f"https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/?page={page}&ordering=newest"
    driver.get(main_page)
    page_ads = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div")

    for i in range(1): #len(page_ads)
        data = {}
        print(f'Ad number {i}')
        page_ads = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div")
        i_ad = page_ads[i]
        ##1 access unegui.mn apartment sales ads: 
        try:
            price    = i_ad.find_element(By.XPATH, "div[2]/div[2]/div[1]/a/span").text
            # date_out = i_ad.find_element(By.XPATH, "div[2]/div[2]/div[3]/div[1]/div[1]").text
            title    = i_ad.find_element(By.XPATH, "div[2]/div[2]/a").text
            location = i_ad.find_element(By.XPATH, "div[2]/div/div[4]/div[1]/div[2]").text
        except:
            price    = i_ad.find_element(By.XPATH, "div[2]/div[1]/div[1]/a/span").text
            # date_out = i_ad.find_element(By.XPATH, "div[2]/div[1]/div[3]/div[1]/div[1]").text
            title    = i_ad.find_element(By.XPATH, "div[2]/div[1]/a").text
            location = i_ad.find_element(By.XPATH, "div[2]/div/div[4]/div[1]/div[2]").text
        
        ##2 collect details of each ad: 
        i_ad.find_element(By.XPATH,'div[2]/a').click()

        date = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]").text
        # date = date_out_parse(date)
        id = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[2]/span").text
        try:
            description = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[5]/div").text
        except:
            description = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[6]/div").text
 
        attributes_el = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[4]/ul/li")

        for i in range(len(attributes_el)):
            try:
                key   = attributes_el[i].find_element(By.XPATH, 'span[1]').text
                value = attributes_el[i].find_element(By.XPATH, 'span[2]').text
            except:
                key   = attributes_el[i].find_element(By.XPATH, 'span[1]').text
                value = attributes_el[i].find_element(By.XPATH, 'a').text
            data[key] = value


        data['price'] = price
        data['title'] = title
        data['location'] = location
        data['date'] = date
        data['id'] = id
        data['description'] = description
        data['page'] = page 
        data['ad_num'] = i

        print(f'Price: {price}')
        print(f'Title: {title}')
        print(f'ID: {id}')
        print(f'Ad data all: {data}')
        
        data_list.append(data)

        driver.back()

    driver.quit()

    df = pd.DataFrame(data_list)
    df.to_csv(f'results/unegui_mn_ads_page{page}.csv', index=False, encoding='utf-8-sig') 


    return data_list


def send_email():
    # mail content
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello" 
    msg['From'] = config.FROM #'py4econ@gmail.com' 
    msg['To'] = config.TO #'sugarkhuu@gmail.com'
    password = config.PASSWORD

    text = "Hello, \n Sending the new ads added today. \n Best regards, \n Sugarkhuu"
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)

    today = datetime.datetime.today().strftime("%Y-%d-%m")

    attachment = MIMEApplication(open(f'results/results_{today}.csv', "rb").read(), _subtype="txt")
    attachment.add_header('Content-Disposition','attachment', filename=f'results_{today}.csv')
    msg.attach(attachment)


    # setup and login
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(msg['From'], password)

    # send email
    try:
        mail.sendmail('from', msg['To'],  msg.as_string())
    except Exception as e:
        print(e)

    mail.quit()

