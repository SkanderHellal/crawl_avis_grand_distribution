# Supermarket Reviews crawler

A simple crawler to extract customer reviews from on supermarkets from `fr.custplace.com`.

### Usage
```
git clone https://github.com/SkanderHellal/crawl_avis_grande_distribution.git
```
```
python3 -m venv venv
pip install -r requirements.txt
```
```python 
from src import CrawlGdistribReviews

crawler = CrawlGdistribReviews(
		gdistrib_name="auchan",
		nb_reviews=200
		output_directory=output_directory
	)
crawler.crawl()
```
`gdistrib_name: Supermarket name (Ex: "auchan", "carrefour")`

`nb_reviews: Number of reviews to extract`

`save_directory: Directory to save reviews`


