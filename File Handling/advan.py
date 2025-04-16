# Read server.log, count "ERROR" entries, and write error lines to errors_only.log
error_count = 0

with open("server.log", "r") as logfile, open("errors_only.log", "w") as errorfile:
    for line in logfile:
        if "error" in line:
            error_count += 1
            errorfile.write(line)
print(f"Total number of 'error' lines: {error_count}")


