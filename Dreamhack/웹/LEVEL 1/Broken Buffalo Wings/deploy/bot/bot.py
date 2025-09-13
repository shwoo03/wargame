from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sys import argv

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "DH{{This_is_flag}}"


def read_url(paramters, cookie={"name": "name", "value": "value"}):
    
    # 인자 값을 받고 / 제거해서 /?a=b 이면 a=b로 최종 변경함 
    parameter = ""

    if paramters[1][0] == "/":
        parameter = paramters[1][1:]
    else : 
        parameter = paramters[1]


    # 쿠키에 flag 넣고 우리가 전송한 URL 접속 
    try:
        service = Service(executable_path="/chromedriver-linux64/chromedriver")
        options = webdriver.ChromeOptions()
        for _ in [
            "--headless",
            "--window-size=1920x1080",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ]:
            options.add_argument(_)

        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(3)
        driver.set_page_load_timeout(3)
        driver.get("http://127.0.0.1:8000/")

        driver.add_cookie(cookie)
        driver.get(f"http://127.0.0.1:8000/{parameter}")
    except Exception as e:
        driver.quit()
        return False
    driver.quit()
    return True


read_url(argv, {"name": "flag", "value": FLAG})
