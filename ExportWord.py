import os
import re
import extract_msg

# === CONFIGURE THIS PATH ===
msg_folder_path = "extract.py"  # Change this to your actual folder name/path
# Example: "extract.py" if the folder is in the same directory as this script
# Or full path: r"C:\Users\YourName\Documents\extract.py"

# Pattern: one letter (A-Z or a-z) followed by exactly 6 digits
pattern = r'[A-Za-z]\d{6}'

matches = []

# Walk through the folder (and subfolders if any)
for root, dirs, files in os.walk(msg_folder_path):
    for file in files:
        if file.lower().endswith('.msg'):
            file_path = os.path.join(root, file)
            try:
                # Open and read the .msg file
                msg = extract_msg.Message(file_path)
                # Get body text (you can also use msg.htmlBody if emails are HTML)
                body = msg.body
                
                # Search for the pattern
                found = re.search(pattern, body)
                if found:
                    matches.append(found.group(0))
                
                msg.close()  # Important: close the message
            except Exception as e:
                print(f"Error reading {file}: {e}")

# Output results
if matches:
    print("Found codes:")
    print("\n".join(matches))
else:
    print("No codes found matching the pattern [Letter + 6 digits]")
