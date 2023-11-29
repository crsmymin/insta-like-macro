from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random

driver = webdriver.Chrome()

#필요한 변수 정의
insta_id = input('인스타그램 아이디 : ')
insta_pw = input('인스타그램 패스워드 : ')
# insta_tag = input('작업할 해시태그 : ')
insta_url = input('인스타 계정 : ')
insta_cnt = int(input('작업횟수(숫자만) : '))

driver.get('https://instagram.com')
driver.implicitly_wait(10)
print('로그인 진행중...')

inputbox = driver.find_element(By.XPATH, '//input[@aria-label="전화번호, 사용자 이름 또는 이메일"]')
inputbox.click()
inputbox.send_keys(insta_id)

inputbox = driver.find_element(By.XPATH, '//input[@aria-label="비밀번호"]')
inputbox.click()
inputbox.send_keys(insta_pw)

inputbox.send_keys(Keys.ENTER)
time.sleep(random.uniform(4.0, 6.0))

# driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))
driver.get('https://www.instagram.com/{}/'.format(insta_url))
time.sleep(random.uniform(4.0, 8.0))

new_feed = driver.find_elements(By.XPATH, '//article//img //ancestor :: div[2]')[9]
new_feed.click()

numoflike = 0
for i in range(insta_cnt): 
    time.sleep(random.uniform(4.0, 6.0))
    span = driver.find_element(By.XPATH, '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: span[2]')  
    like_btn = span.find_element(By.TAG_NAME, 'div')
    btn_svg = like_btn.find_element(By.TAG_NAME, 'svg') 
    svg = btn_svg.get_attribute('aria-label') 
    
    if svg == '좋아요' : 
        like_btn.click() 
        numoflike += 1
        print('좋아요를 {}번째 눌렀습니다.'.format(numoflike))
        time.sleep(random.uniform(4.0, 6.0))
    else :
        print('이미 작업한 피드입니다.')               
        time.sleep(random.uniform(4.0, 6.0))      

    if i < insta_cnt-1 : 
        next_feed_xpath = driver.find_element(By.XPATH, '//*[@aria-label="다음" and @height="16"]//ancestor :: div[2]')
        next_feed = next_feed_xpath.find_element(By.TAG_NAME, 
    'button') 
        next_feed.click() 
        time.sleep(random.uniform(3.0, 6.0))
        driver.implicitly_wait(15)

print("좋아요 작업이 끝났습니다. 프로그램을 종료합니다.")
driver.quit()