
# LinkedIn Search Automation Script

This script automates the process of searching for names on LinkedIn, specifically filtering for people working at "Omicron". It reads names from a text file and opens LinkedIn search pages in your default web browser. The script waits for 20 seconds between searches or allows the user to press Enter to proceed to the next search immediately.

## Prerequisites

- Python 3.x
- `webbrowser` module (part of the Python Standard Library)
- `threading` module (part of the Python Standard Library)

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/yourusername/linkedin-search-automation.git
    cd linkedin-search-automation
    ```

2. **Create a `names.txt` file in the same directory as the script and list each name you want to search for on a new line:**

    ```txt
    John Doe
    Jane Smith
    ```

## Usage

1. **Run the script using Python:**

    ```bash
    python linkedin_search.py
    ```

2. **The script will open LinkedIn search pages for each name in your default web browser, filtering for people working at Omicron.**

3. **For each name, you will see the following message:**

    ```plaintext
    Searching for John Doe at Omicron. Press Enter to proceed to the next search or wait for 20 seconds.
    ```

    - **Press Enter** to skip the remaining time and proceed to the next search immediately.
    - **Wait for 20 seconds** to automatically proceed to the next search.

## Script Explanation

1. **Imports and Constants:**

    - `webbrowser`: To open web pages in the default browser.
    - `time`: To handle sleep intervals.
    - `threading`: To handle simultaneous waiting for user input and timer countdown.
    - `names_file_path`: Path to the file containing the names.

2. **Functions:**

    - `open_linkedin_search(name)`: Constructs the LinkedIn search URL for the given name and opens it in the default web browser.
    - `wait_for_input_or_timeout(timeout)`: Uses a threading timer to wait for user input or automatically proceed after a specified timeout.
    - `main()`: Reads names from the `names.txt` file, initiates the LinkedIn search for each name, and manages the waiting period between searches.

3. **Execution:**

    - The script reads names from the `names.txt` file.
    - For each name, it opens a LinkedIn search page filtered for people working at Omicron.
    - It waits for the user to press Enter or automatically proceeds after 20 seconds to the next search.

## Notes

- Ensure that you have an active internet connection and are logged into LinkedIn in your default browser.
- The script uses threading to manage user input and timeout simultaneously.

## License

This project is licensed under the MIT License.
