import bs4, requests, csv

def getData():
	r_one = requests.get('http://www.songfacts.com/category-type-about.php')
	b_soup_one = bs4.BeautifulSoup(r_one.text, "html.parser")
	data = ['song_category', 'song_name', 'by_name']

	# store headers
	with open('newfile.csv', 'w') as f1:
		writer = csv.DictWriter(f1, fieldnames=data)
		writer.writeheader()

	
	category_list = b_soup_one.select(".songullist-purple")
	anchor_list = category_list[0].find_all("a")

	for anchor in anchor_list:
		url = "http://www.songfacts.com" + anchor['href']
		r_two = requests.get(url)
		b_soup_two = bs4.BeautifulSoup(r_two.text, "html.parser")
		song_list = b_soup_two.select(".songullist-purple")
		song_li_list = song_list[0].find_all("li")
		with open('newfile.csv', 'a') as f2:
			writer = csv.DictWriter(f2, fieldnames=data)
			for li in song_li_list:
				s_anchor = li.select("a")
				writer.writerow({
					'song_category': anchor.string,
					'song_name': s_anchor[0].text,
					'by_name': li.contents[-1].strip()[2:]
					})

if __name__ == '__main__':
	getData()