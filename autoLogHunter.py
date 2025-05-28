import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='AutoLogHunter - Simple log analysis tool.')
    parser.add_argument('-l', '--log', required=True, help='Path to the log file')
    parser.add_argument('-k', '--keywords', nargs='+', help='Keywords to search for (e.g., "Failed password")')
    return parser.parse_args()

def main():
    args = parse_arguments()
    print(f"[+] Log File: {args.log}")
    print(f"[+] Keywords: {args.keywords}")
    anomalies = []
    with open(args.log, 'r') as file:
        testLines = file.readlines()
        for line in testLines: 
            for keyword in args.keywords:
                if keyword in line: 
                    anomalies.append(line)
                    break
    
    print(f"\n[+] Found {len(anomalies)} anomalies with these keywords: {args.keywords}")
    for line in anomalies:
        print(f"    → {line.strip()}")

if __name__ == "__main__":
    main()
