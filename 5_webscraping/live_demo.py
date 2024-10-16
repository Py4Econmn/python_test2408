# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()

# page = 5
# main_page = f"https://www.unegui.mn/l-hdlh/l-hdlh-zarna/oron-suuts-zarna/?page={page}&ordering=newest"
# driver.get(main_page)
# page_ads = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div")


# i = 5
# data = {}
# print(f'Ad number {i}')
# page_ads = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/section/div[2]/div[1]/div[2]/div[2]/div")
# i_ad = page_ads[i]
# ##1 access unegui.mn apartment sales ads: 
# try:
#     price    = i_ad.find_element(By.XPATH, "div[2]/div[2]/div[1]/a/span").text
#     # date_out = i_ad.find_element(By.XPATH, "div[2]/div[2]/div[3]/div[1]/div[1]").text
#     title    = i_ad.find_element(By.XPATH, "div[2]/div[2]/a").text
#     location = i_ad.find_element(By.XPATH, "div[2]/div/div[4]/div[1]/div[2]").text
# except:
#     price    = i_ad.find_element(By.XPATH, "div[2]/div[1]/div[1]/a/span").text
#     # date_out = i_ad.find_element(By.XPATH, "div[2]/div[1]/div[3]/div[1]/div[1]").text
#     title    = i_ad.find_element(By.XPATH, "div[2]/div[1]/a").text
#     location = i_ad.find_element(By.XPATH, "div[2]/div/div[4]/div[1]/div[2]").text


# i_ad.find_element(By.XPATH,'div[2]/a').click()


# date = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]").text
# id = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[2]/span").text
# try:
#     description = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[5]/div").text
# except:
#     description = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[6]/div").text

# attributes_el = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div/div[2]/div[1]/div[4]/ul/li")

# for i in range(len(attributes_el)):
#     try:
#         key   = attributes_el[i].find_element(By.XPATH, 'span[1]').text
#         value = attributes_el[i].find_element(By.XPATH, 'span[2]').text
#     except:
#         key   = attributes_el[i].find_element(By.XPATH, 'span[1]').text
#         value = attributes_el[i].find_element(By.XPATH, 'a').text
#     data[key] = value


# data['price'] = price
# data['title'] = title
# data['location'] = location
# data['date'] = date
# data['id'] = id
# data['description'] = description
# data['page'] = page 
# data['ad_num'] = i

# print(data)

# # print(f'Price: {price}')
# # print(f'Title: {title}')
# # print(f'Location: {location}')

# a = 5

import util
util.data_collection(5)