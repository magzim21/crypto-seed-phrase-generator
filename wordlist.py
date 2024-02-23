import requests

def get_wordlist_from_url(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Split the content by new lines to get individual words
        wordlist = response.text.split('\n')
        # Remove any empty strings in case there are extra new lines
        return [word for word in wordlist if word]
    else:
        # Handle error if the request was not successful
        return f"Failed to retrieve data: Status code {response.status_code}"

# URL containing the word list (replace with your specific URL)
url = 'https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt'

# Get the word list
WORDLIST = get_wordlist_from_url(url)