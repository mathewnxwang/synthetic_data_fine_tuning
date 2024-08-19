import requests
from bs4 import BeautifulSoup
import re

class SubstackScraper():

    def get_post_content(self, url: str) -> list[str]:
        parsed_html = self.get_url_html(url)
        cleaned_text = self.scrape_post_content(parsed_html)
        print(f"Parsed post content from {url} successfully: {cleaned_text}")
        return cleaned_text

    def get_url_html(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {url}. Status code: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # article_body = parsed_html.find('div', class_='single-post')
        # prettified_article_body = article_body.prettify()

        # with open(output_file, 'w', encoding='utf-8') as file:
        #     file.write(str(prettified_article_body))

        return soup

    def scrape_post_content(self, parsed_html: BeautifulSoup) -> list[str]:
        """
        Includes footnotes but excludes comments
        """
        article_body = parsed_html.find('div', class_='single-post')
        p_tags = list(article_body.find_all('p'))

        cleaned_text = []
        for p_tag in p_tags:
            cleaned_passage = p_tag.get_text(separator=' ', strip=True)
            cleaned_text.append(cleaned_passage)
        
        return cleaned_text
