from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = 'chromedriver_win32/chromedriver.exe'

url = input("Enter the URL of the first assignment:\n")
browser = webdriver.Chrome(chrome_path)
browser.get(url)
input('Okay to Proceed?')

while True:
    #checking to see if the page has loaded
    while True:
        try:
            section_title = browser.find_element_by_css_selector('div.section-header-row h1.zybook-section-title')
            break
        except:
            time.sleep(0.25)

    try:
        radio_payload = browser.find_element_by_css_selector('div.interactive-activity-container.multiple-choice-content-resource.participation.ember-view')
        browser.execute_script('arguments[0].scrollIntoView();', radio_payload)
    except:
        pass

    radio_buttons = browser.find_elements_by_css_selector('div.zb-radio-button.orange.ember-view label')
    for radio_button in radio_buttons:
        radio_button.click()

    try:
        short_answer_payload = browser.find_element_by_css_selector('div.interactive-activity-container.short-answer-content-resource.participation.ember-view')
        browser.execute_script('arguments[0].scrollIntoView();', short_answer_payload)
    except:
        pass


    show_answers = browser.find_elements_by_css_selector('button.show-answer-button.zb-button.secondary.ember-view')
    for show_answer in show_answers:
        show_answer.click()
        show_answer.click()

    answers = browser.find_elements_by_css_selector('div.answers')
    text_fields = browser.find_elements_by_css_selector('div.content-resource.short-answer-payload.ember-view textarea.zb-text-area.hide-scrollbar.ember-text-area.ember-view')
    for i in range(len(answers)):
        forfiet_answer = answers[i].find_element_by_css_selector('span.forfeit-answer')
        text_fields[i].send_keys(forfiet_answer.text)
        text_fields[i].send_keys(Keys.ENTER)

    animation_player_payloads = browser.find_elements_by_css_selector('div.interactive-activity-container.animation-player-content-resource.participation.ember-view')
    for animation_player_payload in animation_player_payloads:
        browser.execute_script('arguments[0].scrollIntoView();', animation_player_payload)
        twoTimes = animation_player_payload.find_element_by_css_selector('div.zb-checkbox.grey.label-present.right.ember-view')
        twoTimes.click()
        start = animation_player_payload.find_element_by_css_selector('div.animation-controls button.start-button.start-graphic.zb-button.primary.raised.ember-view')
        start.click()
        while True:
            try:
                rotated_play_button = animation_player_payload.find_element_by_css_selector(
                    'button.normalize-controls.zb-button.ember-view div.play-button.rotate-180')
                break
            except:
                pass
            try:
                play_button = animation_player_payload.find_element_by_css_selector(
                    'button.normalize-controls.zb-button.ember-view div.play-button')
                play_button.click()
            except:
                time.sleep(0.5)

    page_navigators = browser.find_elements_by_css_selector('nav.section-nav a.nav-link.ember-view')
    browser.get(page_navigators[1].get_attribute('href'))

    
