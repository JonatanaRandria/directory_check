import requests

# Initialize an empty list to store checked URLs
checked = []

# Open the file containing directory paths for checking
with open("dir_list.txt", "r") as fichier:
    
    # Iterate over each line in the file
    for i in fichier:
        
        # Construct the URL by stripping whitespace and appending to the base URL
        url = "http://127.0.0.1:5000/" + i.strip() 
        
        # Print the current path being tested
        print('Testing : '+ i)
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # If the response status code is not 404 (Not Found), add the URL to the checked list
        if response.status_code != 404:
            checked.append(url)

# Print the list of found paths
print('Found the following path :')
for g in checked:
    print(g)
