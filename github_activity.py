import sys
import requests
import json
from datetime import datetime

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response =  requests.get(url)
        data = json.loads(response.text)
        return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"Error: Unable to fetch data. Status code: {e.code}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None



def format_activity(event):
    event_type = event['type']
    repo_name = event['repo']['name']
    created_at = datetime.fromisoformat(event['created_at'].replace('Z', '+00:00'))
    formatted_date = created_at.strftime("%Y-%m-%d %H:%M:%S")

    if event_type == 'PushEvent':
        commits = event['payload']['commits']
        return f"- Pushed to {repo_name} on {formatted_date} with {len(commits)} commits"
    elif event_type == 'PullRequestEvent':
        action = event['payload']['action']
        return f"- {action} a pull request in {repo_name} on {formatted_date}"
    elif event_type == 'WatchEvent':
        return f"- Started watching {repo_name} on {formatted_date}"
    elif event_type == 'ForkEvent':
        return f"- Forked {repo_name} on {formatted_date}"
    elif event_type == 'CreateEvent':
        ref_type = event['payload']['ref_type']
        return f"- Created {ref_type} in {repo_name} on {formatted_date}"
    else:
        return f"- {event_type} in {repo_name} on {formatted_date}"

def main():
    if len(sys.argv) !=2 :
        print("Usage: python github_activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    activity_data = fetch_github_activity(username)

    if activity_data:
        print(f"Recent Github activity for {username}:")
        for event in activity_data[:100]:
            formatted_event = format_activity(event)
            print(formatted_event)
    else:
        print(f"No activity found for {username}.")

if __name__ == "__main__":
    main()