import requests
from bs4 import BeautifulSoup
import re

class SubstackScraper():

    def get_post_content(self, url: str) -> list[str]:
        parsed_html = self.get_url_html(url)
        extracted_text = self.scrape_post_content(parsed_html)
        print(f"Parsed post content from {url} successfully: {extracted_text}")
        return extracted_text

    def get_url_html(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {url}. Status code: {response.status_code}")

        parsed_html = BeautifulSoup(response.text, 'html.parser')

        # to inspect the data
        article_body = parsed_html.find('div', class_='single-post')
        prettified_article_body = str(article_body.prettify())
        with open('data/article_body.html', 'w', encoding='utf-8') as file:
            file.write(prettified_article_body)

        return parsed_html

    def scrape_post_content(self, parsed_html: BeautifulSoup) -> list[str]:
        """
        Includes footnotes but excludes comments
        """
        article_body = parsed_html.find('div', class_='single-post')
        paragraphs = list(article_body.find_all('p'))

        extracted_text = []
        for paragraph in paragraphs:
            paragraph_text = paragraph.get_text(separator=' ', strip=True)
            extracted_text.append(paragraph_text)
        
        return extracted_text
