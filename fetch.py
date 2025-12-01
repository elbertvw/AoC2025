#!/usr/bin/env python3
import argparse
import getpass
import os
import sys
import urllib.request
import urllib.error

# Configuration
YEAR = 2025
USER_AGENT = "elbertvw (github.com/elbertvw) AoC2025 fetcher"
SESSION_FILE = os.path.expanduser("~/.aoc_session")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch Advent of Code input securely.")
    parser.add_argument("day", type=int, help="Day number (1-25)")
    parser.add_argument("output_file", nargs="?", help="Optional custom output file path")
    return parser.parse_args()

def validate_day(day):
    if not (1 <= day <= 25):
        sys.exit("Error: Day must be an integer between 1 and 25.")

def load_session_token_from_file():
    if not os.path.exists(SESSION_FILE):
        return None

    try:
        with open(SESSION_FILE, "r") as f:
            token = f.read().strip()
        return token if token else None
    except Exception as e:
        print(f"Warning: Could not read {SESSION_FILE}: {e}", file=sys.stderr)
        return None


def prompt_for_session_token():
    session_token = getpass.getpass("Enter AoC Session Token: ").strip()
    if not session_token:
        sys.exit("Error: Session token cannot be empty.")
    return session_token


def get_session_token():
    stored_token = load_session_token_from_file()
    if stored_token:
        print("Using stored session token from ~/.aoc_session")
        return stored_token
    return prompt_for_session_token()

def determine_output_path(day, custom_path):
    if custom_path:
        return custom_path
    day_padded = f"{day:02d}"
    return os.path.join(day_padded, "input")

def ensure_directory_exists(file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def build_request(url, session_token):
    req = urllib.request.Request(url)
    req.add_header("Cookie", f"session={session_token}")
    req.add_header("User-Agent", USER_AGENT)
    return req

def fetch_and_save_input(url, output_path, session_token):
    request = build_request(url, session_token)

    try:
        print(f"Fetching {url}...")
        with urllib.request.urlopen(request) as response:
            content = response.read()

        with open(output_path, "wb") as f:
            f.write(content)

        print(f"Success! Saved to {output_path}")
        return True

    except urllib.error.HTTPError as e:
        if e.code == 400:
            return False
        sys.exit(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        sys.exit(f"Network Error: {e.reason}")
    except Exception as e:
        sys.exit(f"Error: {e}")

def main():
    args = parse_arguments()
    validate_day(args.day)

    session_token = get_session_token()

    url = f"https://adventofcode.com/{YEAR}/day/{args.day}/input"
    output_path = determine_output_path(args.day, args.output_file)

    ensure_directory_exists(output_path)

    success = fetch_and_save_input(url, output_path, session_token)

    if not success:
        print("Stored token is invalid. Please enter a new token.", file=sys.stderr)
        session_token = prompt_for_session_token()
        fetch_and_save_input(url, output_path, session_token)

if __name__ == "__main__":
    main()