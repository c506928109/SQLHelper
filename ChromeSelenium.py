from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import re

class ChromeSelenium:
    def __init__(self, ImplicitylyWait):
        self.Browser = webdriver.Chrome()
        # self.Browser.implicitly_wait(ImplicitylyWait) 隐式等待 ajax的存在导致页面加载的概念模糊 废弃

    def __del__(self):
        self.Browser.quit()

    def RequestURL(self, URL):
        self.Browser.get(URL)

    def GetBrowser(self):
        return self.Browser
    
    def GetElementByXPath(self, XPath):
        return self.Browser.find_element_by_xpath(XPath).text
    
    def GetFloatElementByXPath(self, XPath):
        return [float(Item) for Item in re.findall(r'-?\d+\.?\d*e?-?\d*?', self.GetElementByXPath(XPath))]

#Begin ExplicitWaiting Condition
    #等待页面中出现某一元素
    def SetExplicitWaiting_ExistTarget(self, XPath, WaitTime):
        WebDriverWait(self.Browser, WaitTime).until(EC.presence_of_element_located((By.XPATH, XPath)))

#End ExplicitWaiting Condition

#Begin Action
    def CreateActionChains(self):
        return ActionChains(self.Browser)

    def GetActionChains(self):
        if not hasattr(self, 'ActionChains'):
            self.ActionChains = ActionChains(self.Browser)
        return self.ActionChains
    
    def MoveToElementByXPath(self, XPath):
        return self.GetActionChains().move_to_element(self.Browser.find_element_by_xpath(XPath))
#End Action
