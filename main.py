from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random
from datetime import datetime

def generate_random_number():
    return "545" + ''.join([str(random.randint(0, 9)) for _ in range(7)])

def generate_random_two_digit_number():
    return str(random.randint(10, 99))

def generate_random_single_digit_number():
    return str(random.randint(1, 8))

def generate_current_date():
    return datetime.now().strftime("%d%m%Y")

def generate_current_time():
    return datetime.now().strftime("%H%M")

def perform_login(driver, wait):
    login_link_xpath = '//a[@id="lnkLogin" and contains(@href, "login.aspx")]'
    login_link = wait.until(EC.element_to_be_clickable((By.XPATH, login_link_xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", login_link)
    login_link.click()
    wait.until(EC.url_contains("login.aspx"))
    # Additional actions for login page if needed


# Function to generate a random user agent
def generate_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument(f"user-agent={generate_random_user_agent()}")

successful_completions = 0
failed_attempts = 0


# Initialize the Chrome driver
for _ in range(300):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.delete_all_cookies()

        # Get temporary email from temp-mail.io
        driver.get("https://temp-mail.io/tr")
        time.sleep(5)
        wait = WebDriverWait(driver, 5)
        mail = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))).get_attribute('value')

        # Sign up on tr.rateurvisit.com
        driver.get("https://tr.rateurvisit.com/#")
        # time.sleep(5)

        kaydol_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a_opensignup"]')))
        kaydol_button.click()

        wait.until(EC.visibility_of_element_located((By.NAME, 'txt_register_email'))).send_keys(mail)

        password = "Aykut123+-"
        wait.until(EC.visibility_of_element_located((By.NAME, 'txt_register_password'))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.NAME, 'txt_register_confirmpassword'))).send_keys(password)

        wait.until(EC.visibility_of_element_located((By.NAME, 'ddl_register_country'))).send_keys("Türkiye")

        # Rastgele bir mobil numara oluştur
        random_mobile_number = generate_random_number()
        wait.until(EC.visibility_of_element_located((By.NAME, 'txtMobileNumber'))).send_keys(random_mobile_number)

        checkbox_script = """
                    var checkbox = document.querySelector("#hypcheck");
                    if (checkbox) {
                        checkbox.click();
                    }
                """
        driver.execute_script(checkbox_script)

        kaydol_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lnkSubmit"]')))
        kaydol_button.click()

        time.sleep(8)

        # Confirm registration via temporary email
        driver.get("https://temp-mail.io/tr")
        time.sleep(5)

        mail_onay = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li')))
        mail_onay.click()

        driver.switch_to.window(driver.window_handles[-1])

        kutu_onay = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                 '//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/a')))
        kutu_onay.click()

        driver.switch_to.window(driver.window_handles[-1])

        driver.get("https://tr.rateurvisit.com/")

        wait.until(EC.visibility_of_element_located((By.NAME, 'txt_login_email'))).send_keys(mail)
        wait.until(EC.visibility_of_element_located((By.NAME, 'txt_login_password'))).send_keys(password)

        login_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lnkLogin"]')))
        login_gir.click()

        deneyim_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a_home"]/a[1]')))
        deneyim_gir.click()

        # Checkbox'a tıkla
        checkbox_script = """
                    var checkbox = document.querySelector("#divage > div > div:nth-child(2) > div > label > span > i");
                    if (checkbox) {
                        checkbox.click();
                    }
                """
        driver.execute_script(checkbox_script)

        hadi_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnDisabled"]')))
        hadi_gir.click()

        sonraki_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnstartorder"]')))
        sonraki_gir.click()

        wait.until(EC.visibility_of_element_located((By.NAME, 'txtrestaurantnumber'))).send_keys("1160260")

        time.sleep(2)

        cookies_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btncontinue"]')))
        cookies_gir.click()

        time.sleep(2)

        sonraki2_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnextrest"]')))
        sonraki2_gir.click()

        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.NAME, 'txtordernumbersplit'))).send_keys(
            generate_random_two_digit_number())
        wait.until(EC.visibility_of_element_located((By.NAME, 'txtregno'))).send_keys(
            generate_random_single_digit_number())

        sonraki3_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnextorder1"]')))
        sonraki3_gir.click()

        wait.until(EC.visibility_of_element_located((By.NAME, 'txtdateofvisit'))).send_keys(generate_current_date())
        wait.until(EC.visibility_of_element_located((By.NAME, 'txttime'))).send_keys(generate_current_time())

        sonraki4_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnextDate"]')))
        sonraki4_gir.click()

        checkbox_script = """
                    var checkbox = document.querySelector("#form1 > div.msections.msection7 > section:nth-child(2) > div > div > div.col-md-12.survey-answer-box > div:nth-child(1) > label > span > i");
                    if (checkbox) {
                        checkbox.click();
                    }
                """
        driver.execute_script(checkbox_script)

        sonraki5_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[1]/label')))
        sonraki5_gir.click()

        sonraki6_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[2]/label/div[1]')))
        sonraki6_gir.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="txtothers"]'))).send_keys("2")

        sonraki7_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki7_gir.click()
        time.sleep(1)

        sonraki8_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki8_gir.click()

        sonraki9_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki9_gir.click()

        time.sleep(1)

        sonraki10_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki10_gir.click()

        time.sleep(2)

        sonraki11_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki11_gir.click()

        time.sleep(1)

        sonraki12_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki12_gir.click()

        time.sleep(2)

        sonraki13_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki13_gir.click()

        time.sleep(1)

        sonraki14_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki14_gir.click()

        time.sleep(2)

        sonraki15_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki15_gir.click()

        time.sleep(1)

        sonraki16_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki16_gir.click()

        time.sleep(2)

        sonraki17_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[2]')))
        sonraki17_gir.click()

        time.sleep(1)

        sonraki18_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki18_gir.click()

        time.sleep(2)

        sonraki19_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki19_gir.click()

        time.sleep(1)

        sonraki20_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki20_gir.click()

        time.sleep(2)

        sonraki21_gir = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div/div[6]')))
        sonraki21_gir.click()

        time.sleep(1)

        sonraki22_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki22_gir.click()

        time.sleep(2)

        sonraki23_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="smily-btn"]/img')))
        sonraki23_gir.click()

        time.sleep(1)

        sonraki24_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki24_gir.click()

        time.sleep(2)

        sonraki25_gir_locator = (By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[1]/label/span/i')

        # Wait for the checkbox to be present in the DOM
        sonraki25_gir = wait.until(EC.presence_of_element_located(sonraki25_gir_locator))

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView();", sonraki25_gir)

        # Click the checkbox
        sonraki25_gir.click()

        sonraki40_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki40_gir.click()

        sonraki80_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]')))
        sonraki80_gir.click()

        comments = [
            "milkshake dondurma makinanız ne zaman gitsek çalışmıyordu",
            "hamburger malzemelerinde eksik malzemeler vardı",
            "ekmekler bayattı",
            "patatesler bayattı",
        ]

        wait.until(EC.visibility_of_element_located((By.NAME, 'controlValue'))).send_keys(random.choice(comments))

        time.sleep(3)

        sonraki26_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki26_gir.click()
        time.sleep(1)
        sonraki27_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]')))
        sonraki27_gir.click()

        comments = [
            "calısanlarınız daha ıyı olabılırdı",
            "mudurlerınız calısanlarınıza daha ıyı davranabılırdı",
            "ekmeklerınız bayattı ekmeklerınız bayat olmasaydı",
            "patataeslerı taze verebilirdiniz",
            "kısa ve kilolu bayan mudurunuz cok kabaydı",
            "kısa boyu bayan mudurunuz çalısanlarınıza nazik davranmadı bagırdı",
            "semiray hanım nazik davranmadı",
        ]

        wait.until(EC.visibility_of_element_located((By.NAME, 'controlValue'))).send_keys(random.choice(comments))

        sonraki26_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki26_gir.click()

        sonraki98_gir_locator = (By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[3]/label/span/i')

        # Wait for the checkbox to be present in the DOM
        sonraki98_gir = wait.until(EC.presence_of_element_located(sonraki98_gir_locator))

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView();", sonraki98_gir)

        # Click the checkbox
        sonraki98_gir.click()

        sonraki101_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki101_gir.click()

        time.sleep(2)

        sonraki99_gir_locator = (By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[2]/label/span/i')

        # Wait for the checkbox to be present in the DOM
        sonraki99_gir = wait.until(EC.presence_of_element_located(sonraki99_gir_locator))

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView();", sonraki99_gir)

        # Click the checkbox
        sonraki99_gir.click()

        sonraki103_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki103_gir.click()

        sonraki104_gir_locator = (By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[8]/label/span/i')

        # Wait for the checkbox to be present in the DOM
        sonraki104_gir = wait.until(EC.presence_of_element_located(sonraki104_gir_locator))

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView();", sonraki104_gir)

        # Click the checkbox
        sonraki104_gir.click()

        sonraki105_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki105_gir.click()

        sonraki106_gir_locator = (By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[2]/label/span/i')

        # Wait for the checkbox to be present in the DOM
        sonraki106_gir = wait.until(EC.presence_of_element_located(sonraki106_gir_locator))

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView();", sonraki106_gir)

        # Click the checkbox
        sonraki106_gir.click()

        sonraki107_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki107_gir.click()

        time.sleep(1)

        sonraki108_gir_locator = (By.XPATH, '//*[@id="dvBindSurveyQuestions"]/div[4]/label/span/i')

        # Wait for the checkbox to be present in the DOM
        sonraki108_gir = wait.until(EC.presence_of_element_located(sonraki108_gir_locator))

        # Scroll into view before clicking
        driver.execute_script("arguments[0].scrollIntoView();", sonraki108_gir)

        # Click the checkbox
        sonraki108_gir.click()

        sonraki109_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki109_gir.click()

        time.sleep(3)

        driver.execute_script(
            "document.querySelector('#dvBindSurveyQuestions > div:nth-child(3) > label > span.cr > i').click();")
        time.sleep(1)

        driver.execute_script(
            "document.querySelector('#dvBindSurveyQuestions > div:nth-child(6) > label > span > i').click();")

        sonraki110_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki110_gir.click()

        time.sleep(1)

        driver.execute_script(
            "document.querySelector('#dvBindSurveyQuestions > div:nth-child(4) > label > span').click();")

        sonraki111_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki111_gir.click()

        time.sleep(1)

        driver.execute_script(
            "document.querySelector('#dvBindSurveyQuestions > div:nth-child(9) > label > span > i').click();")

        sonraki112_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki112_gir.click()

        time.sleep(1)

        sonraki1110_gir = wait.until(EC.visibility_of_element_located((By.NAME, 'controlValue')))
        sonraki1110_gir.click()

        comments2 = [
            "big tasty sos yoktu",
            "big mac sos yoktu",
            "mayonez yoktu",
            "ekmek sıcak değildi",
            "ketçap yoktu",
            "domates yoktu",
            "Marul yoktu",
        ]

        wait.until(EC.visibility_of_element_located((By.NAME, 'controlValue'))).send_keys(random.choice(comments2))

        sonraki1000_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki1000_gir.click()



        sonraki114_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]')))
        sonraki114_gir.click()

        # Örnek bir isim listesi
        türkçe_isimler = [
            "Elif", "Burak", "Ayşe", "Emre", "Zeynep", "Can", "Nazlı", "Umut", "Damla", "Barış",
            "Yasmin", "Kerem", "Melis", "Deniz", "Selin", "Onur", "Ceren", "Kaan", "Ela", "Mert",
            "Dilara", "Tolga", "İrem", "Arda", "Yağmur", "Taylan", "Gizem", "Emir", "Selma", "Serkan",
            "Melisa", "Efe", "Ece", "Alp", "Elifnaz", "Burcu", "Oğuz", "İlayda", "Alper", "Beste",
            "Arif", "Şeyma", "Batuhan", "Zara", "Kaan", "Defne", "Berk", "Aslı", "Rüzgar", "Ezgi",
            "Uğur", "Cansu", "Çağan", "Hazal", "Baran", "Nehir", "Ömer", "Gözde", "Yiğit", "Pınar",
            "Hakan", "Ecem", "Alp", "Nur", "Kağan", "Özge", "Emirhan", "Buse", "Furkan", "Elifsu",
            "Deniz", "Yunus", "İlay", "Yavuz", "İpek", "Emircan", "Gamze", "Mehmet", "Elvan", "Caner",
            "Zara", "Yusuf", "Eylül", "Eray", "Asena", "Cem", "Duygu", "Arman", "Rüya", "Kağan",
            "Serap", "Selim", "Naz", "Orhan", "Damla", "Oktay", "Bengi", "Burhan", "Ayla", "Mehmet Can",
            "Elifnur", "Ahmet", "Melike", "Serdar", "Burcu", "Ufuk", "Sude", "Serdar", "Derin", "Oktay",
            "Rana", "Özgür", "Beyza", "Batu", "Ekin", "Ferit", "Yasemin", "Eren", "Aslıhan", "Baran",
            "Esra", "Murat", "Derya", "Volkan", "Cemre", "Berkay", "Selin", "Engin", "Ezgi", "Arif",
            "Özlem", "Talha", "Cansu", "Onur", "Sibel", "Ali", "Sevil", "Mete", "İrem", "Kaya",
            "Nurcan", "Mustafa", "Burcu", "Tuna", "Gamze", "Barış", "Aylin", "Cihan", "Yaren", "Umut",
            "İpek", "Alihan", "Zehra", "Burak", "Ayşenur", "Kerim", "Damla", "Rüzgar", "Sevim", "Alperen",
            "Melek", "Ulaş", "Pınar", "Alp", "Melis", "Emre", "Beste", "Utku", "Büşra", "Kaan",
            "Zara", "Hüseyin", "Ece", "Alara", "Murat", "Nazlı", "Ahmet", "Güneş", "Erkan", "Buse",
            "Kağan", "Sema", "Can", "Zeynep", "Alp", "Rüya", "Bilge", "Eren", "Dilara", "Alp",
            "İlay", "Yiğit", "Ecem", "Serkan", "İpek", "Yılmaz", "Kaya", "Demir", "Çelik", "Yıldırım", "Öztürk", "Koç", "Şahin", "Güneş", "Yalçın",
            "Türk", "Kurt", "Altın", "Kılıç", "Arslan", "Çetin", "Taş", "Özdemir", "Aydın", "Güzel",
            "Koçak", "Çakır", "Aslan", "Kara", "Erdoğan", "Yaman", "Özkan", "Polat", "Kaplan", "Sarı",
            "Uçar", "Yavuz", "Çetinkaya", "Yılmazer", "Akgül", "Ateş", "Karabulut", "Yorulmaz", "Aktaş", "Şen",
            "Güler", "Sönmez", "Başaran", "Yazıcı", "Avcı", "Ertaş", "Genç", "Özen", "Bulut", "Yüksel",
            "Durmaz", "Şeker", "Güngör", "Türkoğlu", "Yıldız", "Kapıcı", "Dinçer", "Bulut", "Koçyiğit", "Keskin",
            "Acar", "Doğan", "Şahbaz", "Küçük", "İpek", "Çalışkan", "Tunç", "Uzun", "Göktürk", "Gürbüz",
            "Duman", "Türkmen", "Ay", "Aslan", "Er", "Köse", "Güzel", "Demirtaş", "Gökalp", "Korkmaz",
            "Ekinci", "Çolak", "Yavuzer", "Budak", "Karakaş", "Gürsoy", "Çakmak", "Başar", "Şahin", "İşcan",
            "Bilgin", "Büyüktimkin", "Güler", "Demir", "Küçük", "Altay", "Bıyıklı", "Bostancı", "Günaydın",
            "Çağlar", "Güngör", "Dede", "Yıldız", "Kara", "Uzun", "Uyar", "Ateş", "Akın", "Çınar",
            "Yaman", "Kılıç", "Şahbaz", "Özdemir", "Arslan", "Uzun", "Yılmaz", "Erdoğan", "Göktürk", "Yücel",
            "Küçük", "Kaplan", "Aydın", "Uçar", "Çelik", "Özkan", "Sönmez", "Koçak", "Başaran", "Eroğlu",
            "Çetin", "Genç", "Güneş", "Avcı", "Gürbüz", "Şen", "Taş", "Aktaş", "Tunç", "Bulut",
            "Bulut", "Acar", "Şeker", "Çakır", "Güzel", "Doğan", "Türk", "Gürsoy", "Demirtaş", "Er",
            "Köse", "Gürsoy", "Demirtaş", "Er", "Köse", "Yorulmaz", "Dinçer", "Bulut", "Koçyiğit", "Keskin",
            "Acar", "Doğan", "Şahbaz", "Küçük", "İpek", "Çalışkan", "Tunç", "Uzun", "Göktürk", "Gürbüz",
            "Duman", "Türkmen", "Ay", "Aslan", "Er", "Köse", "Güzel", "Demirtaş", "Gökalp", "Korkmaz",
            "Ekinci", "Çolak", "Yavuzer", "Budak", "Karakaş", "Gürsoy", "Çakmak", "Başar", "Şahin", "İşcan",
            "Bilgin", "Büyüktimkin", "Güler", "Demir", "Küçük", "Altay", "Bıyıklı", "Bostancı", "Günaydın",
            "Çağlar", "Güngör", "Dede", "Yıldız", "Kara", "Uzun", "Uyar", "Ateş", "Akın", "Çınar"
        ]

        wait.until(EC.visibility_of_element_located((By.NAME, 'controlValuetext'))).send_keys(random.choice(türkçe_isimler))

        time.sleep(1)

        sonraki29_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki29_gir.click()

        sonraki114_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mobilenumber"]')))
        sonraki114_gir.click()

        wait.until(EC.visibility_of_element_located((By.ID, 'mobilenumber'))).send_keys(random_mobile_number)
        time.sleep(2)
        sonraki300_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki300_gir.click()

        time.sleep(1)

        driver.execute_script(
            "document.querySelector('#dvBindSurveyQuestions > div:nth-child(3) > label > span.cr > i').click();")

        sonraki31_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btnnext"]')))
        sonraki31_gir.click()

        time.sleep(1)


        sonraki155_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form1"]/div[12]/header/div/div[1]')))
        sonraki155_gir.click()

        time.sleep(1)

        sonraki156_gir = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form1"]/div[12]/header/div/div[1]')))
        sonraki156_gir.click()

        time.sleep(8)

        successful_completions += 1
        print(f"HATA.: {successful_completions}")

        try:
            driver.quit()
        except Exception as e:
            print("Tarayıcı kapatılırken bir hata oluştu:", str(e))
        finally:
            # Hata olsa da olmasa da çalışacak olan kısım
            print("Anket tamamlanamadı.")

        # ...
    except Exception as e:

        tebrik_mesaji = "Katılımınız için teşekkür ederiz."
        if tebrik_mesaji in driver.page_source:
            successful_completions += 1
            print("Anket tamamlandı. Toplam tamamlanan anket sayısı:", successful_completions)
        else:
            print("Anket tamamlanamadı.")

    # Print the final counts

print(f"Toplam başarılı tamamlanan anket sayısı: {successful_completions}")

print(f"Toplam başarısız deneme sayısı: {failed_attempts}")



