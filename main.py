from src import CrawlGdistribReviews

if __name__ == "__main__":

	gdistrib_name = "auchan"
	save_directory = "/usr/bases/crawl_gdistrib/data"
	nb_reviews = 400

	crawler = CrawlGdistribReviews(
		gdistrib_name=gdistrib_name,
		save_directory=save_directory,
		nb_reviews=nb_reviews
	)
	crawler.crawl()