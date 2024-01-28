from parse_pdf import get_pdf_data


def compare_pdfs(comparable_pdf_path: str, model_pdf_dict: dict[str, str]) -> dict:
    """
    Compare pdfs by key from ready etalon dict
    :param comparable_pdf_path: path to pdf file with will be compared
    :param model_pdf_dict: with which we will compare
    :return: dict {"missing keys": [keys]}
    """
    dict_result = {"missing keys": []}
    comparable_pdf_str = get_pdf_data(comparable_pdf_path)
    for key in model_pdf_dict:
        if key not in comparable_pdf_str:
            dict_result["missing keys"].append(key)
    return dict_result



