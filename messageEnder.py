###############################################
##                                           ##
##         WHATSAPP MESSAGE SENDER           ##
##        Created by Wesley Pinheiro         ##
##  Adapted by Naomi Lago and Tássio Souza   ##
##                                           ##
###############################################

'''
USEFUL LINKS:

Creator's repository: https://github.com/Wesley-Pinheiro
'''

# Required libraries. Run `$pip install` in case you don't have it installed.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome Browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') # Open Web WhatsApp
time.sleep(5) # Sleep timer (seconds) to scan the QR code

# Contact/Group list
contacts = ('Tia Eda', \
            "Habib's", \
            'Pernambucanas Homologação', \
            'Pernambucanas Produção', \
            'Peça Peças', \
            'Caixa ITX', \
            'Ragazzo Delivery', \
            'Ragazzo SAC', \
            'Enel-X', \
            'Funchal', \
            'Leve Saúde', \
            'Leve Clínica', \
            'Unimed Unimed', \
            'Unimed Rio Preto', \
            'Unimed Rio Rio', \
            'Unimed Farmácia', \
            'Unimed Atendimento', \
            'Unimed Testes', \
            'Zaplivery', \
            'Tendall Delivery', \
            'Tendall SAC', \
            'Basf SAC', \
            'Basf ATH', \
            'Even', \
            'Virbac', \
            'Cabesp', \
            'McDelivery SAC', \
            'Gamaltaly', \
            'Ameplan', \
            'Finandina', \
            )

# Message to be sent
message = '#fim'

# Media (whether be an image, a document or a video)
# PS.: For Windows path, we gotta use backslashes 
media = r''

# Search for contats or groups
def findContact(contact):
    searchField = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    # time.sleep(.5)
    searchField.click()
    searchField.send_keys(contact)
    searchField.send_keys(Keys.ENTER)

# Send the messages
def sendMessage(message):
    messageField = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    messageField[1].click()
    # time.sleep(.5)
    messageField[1].send_keys(str(message)) # + str(another_variable)
    messageField[1].send_keys(Keys.ENTER)

# Send the medias
def sendMedia(media):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(media)
    # time.sleep(.5)
    # send = driver.find_element_by_xpath("//div[contains(@class, '_3Git-')]")
    send = driver.find_element_by_xpath("//div[contains(@class, 'SncVf _3doiV')]")
    send.click()

# Loop to find receipts and send the messages
for contact in contacts:
    findContact(contact)
    sendMessage(message)       
    # sendMedia(media) 
    # time.sleep(.5)