import PyPDF2
import re


def get_pdf_data(pdf_file_path: str) -> str | dict:
    """
    Get pdf file all pages
    :param pdf_file_path: path to pdf file
    :return: all pages data | dict as error
    """
    try:
        with open(pdf_file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

            for page in range(num_pages):
                page_obj = reader.pages[page]
                return page_obj.extract_text()
    except FileNotFoundError:
        return {"error": "File not exist"}


def transform_pdf_data_to_list(str_pdf: str) -> list:
    """
    Convert string data to list data
    :param str_pdf: pdf file data in str
    :return: list_pdf_data: list with pdf data
    """
    list_pdf_data = str_pdf.split("\n")
    return list_pdf_data


def convert_pdf_data_list_to_dict(pdf_list: list) -> dict[str, str or None]:
    """
    Transform data from list to dict.
    :param pdf_list:
    :return: dict
    """
    result = {}
    for row in pdf_list:
        if row == " ":
            pass
        elif ":" not in row:
            result[row.strip()] = ""
        else:
            if re.match(r'(\w+):\s*(\w+#)\s*:\s*(\w+)', row):
                matches = re.match(r'(\w+):\s*(\w+#)\s*:\s*(\w+)', row)
                result[matches.group(1)] = None
                result[matches.group(2)] = matches.group(3)
            elif re.match(r'(\b[^:\n]+:[^:\n]+)(?=\s|$)', row):
                matches = re.findall(r'(\b[^:\n]+:[^:\n]+)(?=\s|$)', row)
                for part in matches:
                    key, value = part.split(":", 1)
                    result[key.strip()] = value.strip()
            else:
                result[row] = None

    return result
