import requests
import threading

checked = []  # List to store URLs that have been checked

def check_urls(urls):
    """
    Function to check the status of each URL in the given list.
    if it doesn't return 404 (not found code),we retrieve it
    
    """
    for url in urls:
        response = requests.get(url)
        print('Trying: ' + url.split('/')[-1])
        if response.status_code != 404:
            checked.append(url)

def main():
    """
    Main function to divide URLs into groups and check them concurrently.
    """
    # Read URLs from the file and construct full URLs
    with open("dir_list.txt", "r") as file:
        urls = ["http://127.0.0.1:5000/" + i.strip() for i in file]

    # Divide the URLs into 3 groups
    chunk_size = len(urls) // 3
    urls_chunks = [urls[i:i+chunk_size] for i in range(0, len(urls), chunk_size)]

    threads = []
    # Create and start a thread for each group of URLs
    for chunk in urls_chunks:
        thread = threading.Thread(target=check_urls, args=(chunk,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the working links
    print('Found the following path :')
    for g in checked:
        print(g)

if __name__ == "__main__":
    main()
