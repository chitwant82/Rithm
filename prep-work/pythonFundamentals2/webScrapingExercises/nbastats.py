from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getData():
	data = None
	players = ['LeBron James', 'Russell Westbrook', 'James Harden',
	 'Kawhi Leonard', 'Stephen Curry']
	driver = webdriver.Firefox(executable_path=r'/path to file geckodriver')
	driver.get('http://stats.nba.com/players/traditional/#!?sort=PTS&dir=-1')
	try:
	    WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, ".nba-stat-table__overflow"))
	    )
	    data = driver.page_source

	finally:
	    driver.quit()

	b_soup_one = BeautifulSoup(data, "html.parser")

	data = ['PNAME', 'GP', 'W', 'PTS', 'FG%', '3P%', 'REB', 'AST', 'STL', 'BLK']

	# store headers
	with open('newfile.csv', 'w') as f1:
		writer = csv.DictWriter(f1, fieldnames=data)
		writer.writeheader()

	body_element_list = b_soup_one.select('div.nba-stat-table__overflow > table > tbody')

	all_tr = body_element_list[0].find_all("tr")


	for item in all_tr:
		p_name = item.select('td.player > a')[0].text
		if item.select('td.player > a')[0].text in players:
			all_td = item.find_all('td')
			with open('newfile.csv', 'a') as f2:
				writer = csv.DictWriter(f2, fieldnames=data)
				writer.writerow({
					'PNAME': p_name,
					'GP': all_td[4].text,
					'W': all_td[5].text,
					'PTS': all_td[8].text,
					'FG%': all_td[11].text,
					'3P%': all_td[14].text,
					'REB': all_td[20].text,
					'AST': all_td[21].text,
					'STL': all_td[23].text,
					'BLK': all_td[24].text
					})

if __name__ == '__main__':
	getData()