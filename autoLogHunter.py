# Import the argparse module to handle command-line arguments
import argparse

# Function to define and parse expected command-line arguments
def parse_arguments():
    # Create an ArgumentParser object with a description of the tool
    parser = argparse.ArgumentParser(description='AutoLogHunter - Simple log analysis tool.')

    # Add a required argument for the path to the log file
    parser.add_argument('-l', '--log', required=True, help='Path to the log file')

    # Add an argument for a list of keywords to search for in the log file
    parser.add_argument('-k', '--keywords', nargs='+', help='Keywords to search for (e.g., "Failed password")')

    # Parse and return the arguments
    return parser.parse_args()

# Main function to coordinate the log scanning process
def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Print out the path to the log file and the keywords being used
    print(f"[+] Log File: {args.log}")
    print(f"[+] Keywords: {args.keywords}")

    # Initialize an empty list to store lines that match the given keywords
    anomalies = []

    # Open the log file in read mode
    with open(args.log, 'r') as file:
        # Read all lines in the log file into a list
        testLines = file.readlines()

        # Loop through each line in the file
        for line in testLines:
            # For each keyword, check if it appears in the current line
            for keyword in args.keywords:
                if keyword in line:
                    # If a keyword is found, add the line to the anomalies list
                    anomalies.append(line)
                    break  # Stop checking other keywords once a match is found

    # Print the total number of matching lines (anomalies) found
    print(f"\n[+] Found {len(anomalies)} anomalies with these keywords: {args.keywords}")

    # Print each anomalous line, stripped of leading/trailing whitespace
    for line in anomalies:
        print(f"    → {line.strip()}")

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
