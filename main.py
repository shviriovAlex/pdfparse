from compare_pdf import compare_pdfs
from parse_pdf import get_pdf_data, transform_pdf_data_to_list, convert_pdf_data_list_to_dict


if __name__ == "__main__":
    pdf_str = get_pdf_data("test_task.pdf")
    pdf_list = transform_pdf_data_to_list(pdf_str)
    pdf_dict = convert_pdf_data_list_to_dict(pdf_list)
    compare_result = compare_pdfs("test_task.pdf", pdf_dict)