from src import CrawlGdistribReviews

if __name__ == "__main__":

	# auchan
	# carrefour
	# leclerc

	gdistrib_name = "leclerc"
	output_directory = "/usr/bases/crawl_gdistrib/data"
	nb_reviews = 400

	crawler = CrawlGdistribReviews(
		gdistrib_name=gdistrib_name,
		output_directory=output_directory,
		nb_reviews=nb_reviews
	)
	crawler.crawl()