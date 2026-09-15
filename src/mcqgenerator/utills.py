# import os
# import PyPDF2
# import json
# import traceback

# def read_file():
#     if file.name.endswith('.pdf'):
#         try:
#             pdf_reader = PyPDF2.PdfReader(file)
#             text =""
#             for page in pdf_reader.pages:
#                 text += page.extract_text()
#             return text
#         except Exception as e:
            
#             raise Exception(f"Error reading PDF file: {e}")
    
#     elif file.name.endswith('.txt'):
#         return file.read().decode('utf-8')
#     else:
#         raise Exception("Unsupported file format. Please upload a PDF or TXT file.")

# def get_table_data():
#     return data



import PyPDF2
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)

            text = ""

            for page in pdf_reader.pages:
                extracted_text = page.extract_text()

                if extracted_text:
                    text += extracted_text

            return text

        except Exception as e:
            raise Exception(f"Error reading PDF file: {e}")

    elif file.name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")

        except Exception as e:
            raise Exception(f"Error reading TXT file: {e}")

    else:
        raise Exception("Unsupported file format. Please upload a PDF or TXT file.")


def get_table_data(quiz_str):
    try:
        quiz_dict = json.loads(quiz_str)

        quiz_table = []

        for key, value in quiz_dict.items():
            quiz_table.append({
                "Question": value.get("mcq", ""),
                "Option A": value.get("options", {}).get("a", ""),
                "Option B": value.get("options", {}).get("b", ""),
                "Option C": value.get("options", {}).get("c", ""),
                "Option D": value.get("options", {}).get("d", ""),
                "Correct": value.get("correct", "")
            })

        return quiz_table

    except Exception as e:
        traceback.print_exc()
        raise Exception(f"Error creating table data: {e}")


