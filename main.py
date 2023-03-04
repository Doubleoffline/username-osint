import requests
import json

print("Made By Double")

def search_username(username):
    websites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Tumblr": f"https://{username}.tumblr.com/",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "Vimeo": f"https://vimeo.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "DeviantArt": f"https://{username}.deviantart.com/",
        "Stack Overflow": f"https://stackoverflow.com/users/{username}/",
        "Product Hunt": f"https://www.producthunt.com/@{username}",
        "AngelList": f"https://angel.co/u/{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "CodePen": f"https://codepen.io/{username}/",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}/",
        "Scribd": f"https://www.scribd.com/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}/",
        "Keybase": f"https://keybase.io/{username}",
        "Repl.it": f"https://repl.it/@{username}",
        "Kaggle": f"https://www.kaggle.com/{username}",
        "Academia.edu": f"https://{username}.academia.edu/",
        "ResearchGate": f"https://www.researchgate.net/profile/{username}",
        "Slideshare": f"https://www.slideshare.net/{username}",
        "StackExchange": f"https://stackexchange.com/users/{username}/"
    }

    results = []
    for site, url in websites.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found {username} on {site}: {url}")
                results.append({"site": site, "url": url})
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {site}: {e}")
    
    if results:
        with open(f"{username}.json", "w") as f:
            json.dump(results, f)
        print(f"Results saved in {username}.json")
    else:
        print("No results found")

if __name__ == "__main__":
    username = input("Enter a username to search: ")
    search_username(username)
