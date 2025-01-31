import sys
import os

def extract_logs_for_date(file_path, target_date):
    try:
        output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output')
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        output_file = os.path.join(output_folder, f"output_{target_date}.txt")
        
        with open(file_path, 'r') as file, open(output_file, 'w') as output:
            for line in file:
                if line.startswith(target_date):
                    output.write(line)
        
        print(f"Filtered logs saved to: {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <file_path> <YYYY-MM-DD>")
    else:
        file_path = sys.argv[1]
        target_date = sys.argv[2]
        extract_logs_for_date(file_path, target_date)