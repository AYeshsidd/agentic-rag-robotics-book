import xml.etree.ElementTree as ET
import sys

sitemap_content = sys.stdin.read()
root = ET.fromstring(sitemap_content)

namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
base_url_replace = "https://physical-ai-humanoid-robotics-book-sigma-eight.vercel.app/"

extracted_urls = []
for url_element in root.findall('sitemap:url', namespace):
    loc_element = url_element.find('sitemap:loc', namespace)
    if loc_element is not None:
        original_url = loc_element.text
        # Replace the placeholder base URL with the actual one
        if "https://your-docusaurus-site.example.com/" in original_url:
            corrected_url = original_url.replace("https://your-docusaurus-site.example.com/", base_url_replace)
            extracted_urls.append(corrected_url)
        else:
            extracted_urls.append(original_url)

# Filter for documentation pages and remove the homepage
filtered_urls = [url for url in extracted_urls if "/docs/" in url]

if filtered_urls:
    print("Extracted and Filtered URLs:")
    for url in filtered_urls:
        print(url)
    print("\nComma-separated for .env:")
    print(",".join(filtered_urls))
else:
    print("No relevant documentation URLs found in the sitemap.")
