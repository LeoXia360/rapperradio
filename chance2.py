from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, string

count = 0; 
limit = 100

while(True):
	try:
		driver = webdriver.Firefox()
		driver.get('https://ctt.ec/RbV0C')
		time.sleep(1)
		driver.find_element_by_id('username_or_email').send_keys('LeoXia5')
		driver.find_element_by_id('password').send_keys('chancetherapper')
		driver.find_element_by_xpath("//INPUT[@type='submit']").click()
		time.sleep(2)
		random_string = ''.join(random.choice(string.lowercase) for i in range(10))
		print random_string
		driver.find_element_by_xpath("//TEXTAREA[@id='status']").send_keys(" " + random_string)
		time.sleep(2)
		driver.find_element_by_xpath("(//INPUT[@type='submit'])[2]").click()
		driver.quit()
		count += 1
		print "number of tweets sent: " + str(count)
		if count >= limit:
			print "sleeping for an hour"
			time.sleep(3600)
			count = 0;
	except:
		pass
	finally:
		driver.quit()




# driver.get("http://rapperradio.com/")


# city_input = driver.find_element_by_id('theOneCities')
# city_input.send_keys('AUSTIN')
# hidden_austin = driver.find_element_by_class_name('tt-highlight')
# driver.execute_script("$(arguments[0]).click();", hidden_austin)
# station_input = driver.find_element_by_class_name('btn btn-whiteRounded station-link')
# station_input.click()
