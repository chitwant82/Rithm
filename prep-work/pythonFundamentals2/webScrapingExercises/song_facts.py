import bs4, requests, csv

def getData():
	r_one = requests.get('http://www.songfacts.com/category-type-about.php')
	b_soup_one = bs4.BeautifulSoup(r_one.text, "html.parser")
	data = ['song_category', 'count', 'first_ten']

	# store headers
	with open('newfile.csv', 'w') as f1:
		writer = csv.DictWriter(f1, fieldnames=data)
		writer.writeheader()

	arr=[]
	category_list = b_soup_one.select(".songullist-purple")
	anchor_list = category_list[0].find_all("a")

	for anchor in anchor_list[:10]:
		url = "http://www.songfacts.com" + anchor['href']
		r_two = requests.get(url)
		b_soup_two = bs4.BeautifulSoup(r_two.text, "html.parser")
		song_list = b_soup_two.select(".songullist-purple")
		song_anchor_list = song_list[0].find_all("a")
		song_idx = 1
		for s_anchor in song_anchor_list[:10]:
			arr.append("Song" + str(song_idx) + " -> " + s_anchor.string)
			song_idx = song_idx + 1

		arr_str = ', '.join([str(x) for x in arr])

		with open('newfile.csv', 'a') as f2:
			writer = csv.DictWriter(f2, fieldnames=data)
			writer.writerow({
				'song_category': anchor.string,
				'count': len(song_anchor_list),
				'first_ten': arr_str
				})
		arr.clear()


if __name__ == '__main__':
	getData()