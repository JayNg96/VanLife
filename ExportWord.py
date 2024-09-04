import os
import pandas as pd
from docx import Document

def extract_checkboxes_from_docx(doc_path):
    doc = Document(doc_path)
    yes_state = "Unchecked"
    no_state = "Unchecked"
    
    # Iterate through paragraphs to find the specific string
    for para in doc.paragraphs:
        if "Is the customer information public/anonymized/encrypted in a secure manner, such that the identities of customers cannot be readily inferred?" in para.text:
            # Check the next elements after the question to find the checkboxes
            next_para = para._element.getnext()
            while next_para is not None:
                next_text = next_para.text if hasattr(next_para, 'text') else ''
                if '☐Yes' in next_text or '☒Yes' in next_text:
                    yes_state = "Checked" if '☒Yes' in next_text else "Unchecked"
                if '☐No' in next_text or '☒No' in next_text:
                    no_state = "Checked" if '☒No' in next_text else "Unchecked"
                next_para = next_para.getnext()
            break

    return yes_state, no_state

def main():
    folder_path = r"C:\Your\Folder\Path"  # Update this with your folder path
    output_data = []

    # Iterate through all Word documents in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            yes_state, no_state = extract_checkboxes_from_docx(file_path)
            output_data.append({
                "File Name": filename,
                "Yes State": yes_state,
                "No State": no_state
            })

    # Export the results to an Excel file
    df = pd.DataFrame(output_data)
    df.to_excel("output.xlsx", index=False)

if __name__ == "__main__":
    main()
