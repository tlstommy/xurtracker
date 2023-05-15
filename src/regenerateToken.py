#old token gen program to archive
#this is NOT reliable

import requests
from requests.structures import CaseInsensitiveDict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import *
import email
import time
import imaplib
import json


#prints the access token for oauth

url = "https://www.bungie.net/Platform/App/OAuth/Token/"

tokenAuthURL=f"https://www.bungie.net/en/OAuth/Authorize?client_id={OAUTH_CLIENT_ID}&response_type=code"

def grabNewBearerToken(OAUTH_CODE):

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = OAUTH_DATASTR + OAUTH_CODE


    resp = requests.post(url, headers=headers, data=data)

    jsonResponse = json.loads(resp.content)
    print(jsonResponse)
    print(jsonResponse["access_token"])
    return jsonResponse["access_token"]


def retriveEmailcode():
    #sleep to find new mail
    time.sleep(15)
    emailMessageData = None
    # connect to the server and go to its inbox
    mail = imaplib.IMAP4_SSL(EMAIL_SERVER)
    mail.login(EMAIL, EMAIL_PASSWORD)
    mail.select('inbox')
    _, microsoft_auth_emails = mail.search(None, '(FROM "account-security-noreply@accountprotection.microsoft.com")')
    #total number of mails from specific user

    #print("Total Messages:" , len(microsoft_auth_emails[0].split()))
    for num in microsoft_auth_emails[0].split():
        _, data = mail.fetch(num , '(RFC822)')
        _, bytes_data = data[0]

        #convert the byte data to message
        email_message = email.message_from_bytes(bytes_data)


        #access data
        for part in email_message.walk():
            if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                message = part.get_payload(decode=True)
                emailMessageData = str(message.decode())
                break
        mail.store(num, "+FLAGS", "\\Deleted")
    emailMessageData = emailMessageData.split("Security code: ")[-1].split("If you don't recognize the Microsoft")[0]
    emailMessageData.replace(" ","").replace("\r","").replace("\n","")
    emailCode = emailMessageData[0:7]
    print(f"[Retrieved Email Code - {emailCode}]")
    return emailCode

def generateNewOauthCode(useAuthApp):
    #https://understandingdata.com/install-google-chrome-selenium-ec2-aws/
    #cd tmp
    #sudo wget https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip
    #sudo unzip chromedriver_linux64.zip
    #sudo mv chromedriver /usr/bin/chromedriver
    #chromedriver --version

    print("USING AUTH APP: ",useAuthApp)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox") #bypass OS security model
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    print("[Driver Started]")
    driver.implicitly_wait(10)
    driver.get(tokenAuthURL)
    print(f"[Driver got - {tokenAuthURL}]")
    bngButton=driver.find_elements(By.CLASS_NAME,"provider-selector-btn")
    bngButton[0].click()
    driver.implicitly_wait(20)
    userEmailInput= driver.find_element(By.NAME,"loginfmt")
    userEmailInput.send_keys(seleniumUsername)
    userEmailInput.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    signinWithPassButton = driver.find_element(By.LINK_TEXT,"Other ways to sign in")
    signinWithPassButton.click()
    driver.implicitly_wait(10)
    usePassButton = driver.find_elements(By.CLASS_NAME,"tile-container")
    usePassButton[2].click()
    driver.implicitly_wait(10)
    userPassInput = driver.find_element(By.NAME,"passwd")
    userPassInput.send_keys(seleniumPassword)
    userPassInput.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    print("[Bypassing Microsoft Authenticator]")
    
    if useAuthApp == True:
        time.sleep(10)
        
    else:
        #sometimes this isnt need for some reason leave it commented just incase
        try:
            authButton = driver.find_element(By.LINK_TEXT,"I can't use my Microsoft Authenticator app right now")
            authButton.click()
            driver.implicitly_wait(20)
        except:
            pass

        useEmailButton = driver.find_elements(By.CLASS_NAME,"table")
        for i in range(len(useEmailButton)):
            if(useEmailButton[i].text == EMAIL_TARGET):
                print(f"[Found Target Email Server]")
                useEmailButton[i].click()
                break
        
        emailTextBox = driver.find_element(By.NAME,"ProofConfirmation")
        emailTextBox.send_keys(EMAIL)
        emailTextBox.send_keys(Keys.ENTER)
        emailCode = retriveEmailcode()
        otcInput = driver.find_element(By.NAME,"otc")
        otcInput.send_keys(emailCode)
        otcInput.send_keys(Keys.ENTER)


    XTUrl = driver.current_url
    OauthCode=XTUrl.split("https://xurtracker.com/?code=")[-1]
    print(f"[Oauth Code - {OauthCode}]")
    driver.close()
    return OauthCode

with open(OAUTH_ACCESS_TOKEN_LOCATION, 'w') as f:
    f.write(grabNewBearerToken(generateNewOauthCode(useAuthApp=False)))
    f.close()
