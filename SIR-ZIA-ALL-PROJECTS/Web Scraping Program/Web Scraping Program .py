import requests
from bs4 import BeautifulSoup

def get_github_avatar():
    print("GitHub Profile Image Scraper")
    username = input("Enter GitHub username: ")
    
    # Build GitHub profile URL
    url = f"https://github.com/{username}"
    
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the avatar image
        avatar = soup.find("img", {"alt": "Avatar"})["src"]
        
        # Handle relative URLs
        if avatar.startswith("/"):
            avatar = f"https://github.com{avatar}"
        
        print(f"\nProfile image URL: {avatar}")
    
    except requests.exceptions.RequestException:
        print("Error: Could not fetch GitHub profile. Check username and internet connection.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    get_github_avatar()