import webbrowser
import time
import threading

# Path to the file containing names
names_file_path = "names.txt"

def open_linkedin_search(name):
    query = f"https://www.linkedin.com/search/results/people/?keywords={name} Omicron"
    webbrowser.open(query)

def wait_for_input_or_timeout(timeout):
    timer = threading.Timer(timeout, lambda: None)
    timer.start()
    input("Press Enter to proceed to the next search or wait for 20 seconds...")
    timer.cancel()

def main():
    with open(names_file_path, 'r') as file:
        names = file.readlines()
    
    for name in names:
        name = name.strip()
        if name:
            open_linkedin_search(name)
            print(f"Searching for {name} at Omicron. Press Enter to proceed to the next search or wait for 20 seconds.")
            wait_for_input_or_timeout(20)

if __name__ == "__main__":
    main()
