## Github Activity Tracker

This is a simple Python script that fetches and displays recent GitHub activity for a given username. <br>
Github user activity project on https://roadmap.sh/projects/github-user-activity
### Features

- Retrieves the latest 100 GitHub events for a specified user.
- Formats the activity data into a readable list.
- Handles common errors, such as invalid usernames and API request failures.

### Usage

1. **Save the script:** Save the provided Python code as `github_activity.py`.
2. **Open your terminal:** Navigate to the directory where you saved the script.
3. **Run the script:** Execute the following command, replacing `<username>` with the desired GitHub username:

    python github_activity.py <username> <br>
    For example:
      ```bash

    python github_activity.py aizwal
    Example Output
    Recent Github activity for aizwal:
    - Pushed to aizwal/ProjectX on 2023-12-20 14:32:05 with 3 commits
    - Started watching aizwal/AwesomeRepo on 2023-12-19 10:15:22
    - Forked aizwal/AnotherRepo on 2023-12-18 16:48:31
    - Created branch in aizwal/NewProject on 2023-12-17 12:00:00
    ...
    ```
Dependencies
requests: Used for making HTTP requests to the GitHub API. Install it using pip: pip install requests<br>

Notes <br>
- The script retrieves data from the public GitHub API. <br>
- Rate limits apply to the GitHub API. If you exceed the limit, you may encounter errors. <br>
- The output format and displayed events may be adjusted by modifying the format_activity function in the script.
