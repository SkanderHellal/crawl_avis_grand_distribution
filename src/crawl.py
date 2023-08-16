from typing import Optional
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import langdetect
import os
import time


class CrawlGdistribReviews:
	def __init__(self, gdistrib_name: str, output_directory: str, nb_reviews: Optional[int] = None):
		self.url = os.path.join("https://fr.custplace.com", f"{gdistrib_name}")
		self.gdistrib_name = gdistrib_name
		self.output_directory = output_directory
		self.nb_reviews = nb_reviews

	@staticmethod
	def detect_language(text: str) -> Optional[str]:
		"""
		Language detection method
		:param text: str
		:return: (`str` or `None`)
			text language
		"""
		try:
			language = langdetect.detect(text)
		except langdetect.LangDetectException:
			language = None
		return language

	@staticmethod
	def _instantiate_webdriver():
		"""Configure and instantiate Selenium web driver"""
		options = Options()
		options.add_argument("--headless")
		driver = webdriver.Chrome(options=options)

		return driver

	def crawl(self):
		"""Crawl Reviews and Ratings"""

		# Instantiate the driver
		driver = self._instantiate_webdriver()
		driver.get(self.url)
		time.sleep(5)

		# Pagination
		pagination = driver.find_element(By.XPATH, '//nav/ul')
		pages = pagination.find_elements(By.TAG_NAME, 'li')
		nb_last_page = int(pages[-2].text)

		# Extract reviews and ratings
		reviews_and_ratings = []
		for i in range(1, nb_last_page + 1):
			time.sleep(2)
			articles = driver.find_elements(By.TAG_NAME, 'article')
			for article in articles:

				# Extract rating
				try:
					rating = article.find_element(By.XPATH, 'div[contains(@class,"msg-heading")]/div')
					rating = rating.get_attribute("class").replace("inline-block mr-1.5 mb-2 aggregateRating s-", "")
				except:
					rating = "None"

				# Extract review
				try:
					review = article.find_element(By.XPATH, 'div[contains(@data-view,"message")]/p[@class="mb-3"]').text
					review = review.replace("\n", "")
				except:
					continue

				reviews_and_ratings.append(f"{review}|{rating}")

			if self.nb_reviews is not None and self.nb_reviews == len(reviews_and_ratings):
				break

			# Go to next page
			try:
				next_page = driver.find_elements(By.XPATH, '//nav/ul/li')[-1]
				print(next_page.find_element(By.TAG_NAME, 'a').get_attribute("href"))
				next_page.click()
			except:
				print("No page access")
				break

		driver.quit()

		# Save reviews
		with open(os.path.join(self.output_directory, f"{self.gdistrib_name}.txt"), "w") as f:
			for review in reviews_and_ratings:
				f.write(review)
				f.write("\n")