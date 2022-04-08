from selenium import  webdriver


url = 'https://music.163.com/#/discover/toplist?id=19723756'

def get_songs_name(browser):
    browser.get(url)
    browser.switch_to.frame('g_iframe');
    logo=browser.find_elements_by_class_name('txt')
    list=[]
    for i in logo:
        list.append(i.find_element_by_css_selector('b'))
    result=[]
    for i in list:
        result.append(i.get_attribute('title'))
    return result

def get_songs_id(browser):
    browser.get(url)
    browser.switch_to.frame('g_iframe');
    logo = browser.find_elements_by_class_name('txt')
    list = []
    for i in logo:
        list.append(i.find_element_by_css_selector('a'))
        result=[]
    for i in list:
        temp=i.get_attribute('href').split('=')[1]
        result.append(temp)
    return result