#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

def get_filenames_from_index(url):
    """
    Given a directory-index URL (e.g. https://example.tld/path/images/),
    return a list of file names (with extensions) found on the page.
    Then download the images to the same directory as this script
    """
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    array = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if href in ("../", "..", "/") or href.endswith("/"):
            continue
        if href.startswith("?") or href.startswith("#") or href.startswith("mailto:"):
            continue

        filename = href.split("/")[-1]

        if "." in filename:
            array.append(filename)

    return array


def download_files(base_url, links):
    """
    Download each file in `links` from `base_url + link` and save it
    to the current directory using its filename.
    """
    for image in links:
        file_name = image.split('/')[-1]
        print(f"Filename: {file_name}")

        r = requests.get(base_url + image, stream=True)
        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            print(f"Broken Image: {file_name}")


if __name__ == "__main__":
    base_url = "https://example.tld/path/to/images/"

    array = get_filenames_from_index(base_url)
    print(array)

    download_files(base_url, array)
