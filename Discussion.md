**Solution Considered** <br>

Linear Search Approach

    Reading the entire log file line by line.
    Checking each line’s date and extracting logs matching the target date.

Binary Search on the Entire File

    Binary search is the most efficient solution since the logs are sorted, but i was not able to implement it under time.

**Steps to Run** <br>

    Ensure Python is Installed
        Run python --version to verify.

    Save the Script
        Copy the provided script and save it as extract_logs.py.

    Prepare the Log File
        Ensure you have a log file (logfile.log).
        
Run the Script

python extract_logs.py /path/to/logfile.log 2024-12-01

    Replace /path/to/logfile.log with the actual log file path.
    Replace 2024-12-01 with the date you want to extract logs for.

View the Output

    The filtered logs will be saved in the output/ folder as output_YYYY-MM-DD.txt.
