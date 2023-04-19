import os
import requests
from bs4 import BeautifulSoup

# Second Section: Declare important variables
# google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# Third Section: Build the main function
saved_folder = 'images'
sub_folders = ['kangaroo', 'lion']

search_urls = [
	[
		'https://www.google.com/search?q=kangroo+animal&tbm=isch&ved=2ahUKEwiIuN-P6qj-AhXxgeYKHa6MBzQQ2-cCegQIABAA&oq=kangroo+animal&gs_lcp=CgNpbWcQAzIFCAAQgAQyCQgAEBgQgAQQCjoECCMQJzoHCAAQigUQQzoGCAAQCBAeULEDWLcMYIEOaABwAHgAgAHNAYgBwQqSAQUwLjcuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=A_44ZMiqOvGDmgeumZ6gAw&bih=760&biw=1471&hl=en',
		'https://www.google.com/search?q=kangaroo+animal&tbm=isch&hl=en&chips=q:kangaroo+animal,g_1:australia:9xS9WlVZ-sw%3D&sa=X&ved=2ahUKEwj-zteU6qj-AhVZyXMBHfOiBSwQ4lYoAXoECAEQJw&biw=1471&bih=760',
		'https://www.google.com/search?q=kangaroo+animal&tbm=isch&hl=en&chips=q:kangaroo+animal,online_chips:wildlife:wRqu7xVPmlw%3D&sa=X&ved=2ahUKEwi_g7jm6qj-AhWWm2MGHVvlCuYQ3VYoAHoECAEQKA&biw=1471&bih=760',
		'https://www.google.com/search?q=kangaroo+animal&tbm=isch&hl=en&chips=q:kangaroo+animal,online_chips:red:1HbU8mIK04w%3D&sa=X&ved=2ahUKEwjErp2B66j-AhXPxKACHZk-CpgQ4VYoAHoECAEQJQ&biw=1471&bih=760',
	],
	[
		'https://www.google.com/search?q=lion&tbm=isch&hl=en&sa=X&ved=2ahUKEwilnPvR5aj-AhXGB7cAHZQfB4IQ3VYoAHoECAEQJQ&biw=1471&bih=760',
		'https://www.google.com/search?q=lion&tbm=isch&hl=en&chips=q:lion,g_1:animal:h8n1113FYDE%3D&sa=X&ved=2ahUKEwjdtf7S5aj-AhXO9XMBHQ72DCcQ4lYoE3oECAEQSw&biw=1471&bih=760',
		'https://www.google.com/search?q=lion&tbm=isch&hl=en&chips=q:lion,g_1:animal:h8n1113FYDE%3D,g_1:african:F1HXajgdwRM%3D&sa=X&ved=2ahUKEwji7o2d56j-AhW0mGMGHT-rDS8Q4lYoB3oECAEQNg&biw=1471&bih=760',
		'https://www.google.com/search?q=lion&tbm=isch&hl=en&chips=q:lion,g_1:animal:h8n1113FYDE%3D,g_1:zoo:VKZuAeZ3yno%3D&sa=X&ved=2ahUKEwiw3Oni6Kj-AhUaKLcAHXi7BtEQ3VYoAHoECAEQKw&biw=1471&bih=760',
	]
]


def download_images(i):
	
	for search_url in search_urls[i]:
		n_images = 30

		print('searching...')

		response = requests.get(search_url, headers=user_agent)

		html = response.text

		soup = BeautifulSoup(html, 'html.parser')

		results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

		count = 1
		links = []
		for result in results:
			try:
				link = result['data-src']
				links.append(link)
				count += 1
				if(count > n_images):
					break

			except KeyError:
				continue

		print(f"Downloading {len(links)} images...")
		
		folder_len = len(os.listdir(saved_folder + '/' + sub_folders[i]))
		for link in links:
			response = requests.get(link)

			image_name = saved_folder + '/'+ sub_folders[i] +'/' + str(folder_len) + '.jpg'

			with open(image_name, 'wb') as fh:
				fh.write(response.content)
			
			folder_len += 1

# os.rmdir('images/kangroo')
# os.rmdir('images/lion')
os.mkdir('images')
os.mkdir('images/kangaroo')
os.mkdir('images/lion')
download_images(0)
download_images(1)
