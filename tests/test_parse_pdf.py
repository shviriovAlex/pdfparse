from pytest import mark
from unittest.mock import patch

from parse_pdf import convert_pdf_data_list_to_dict, get_pdf_data
from compare_pdf import compare_pdfs


def test_get_pdf_data_path():
    ar = get_pdf_data("some_fake_path.pdf")
    er = {"error": "File not exist"}
    assert ar == er, "Exception wasn't caught"


@mark.parametrize(
    "test_list,er",
    [(['GRIFFON AVIATION SERVICES LLC', 'PN: tst SN: 123123'],
      {'GRIFFON AVIATION SERVICES LLC': '', 'PN': 'tst', 'SN': '123123'}),
     (['REMARK: LOT# : 1', 'TAGGED BY: '],
      {'REMARK': None, 'LOT#': '1', 'TAGGED BY': ''}),
     ([' ', 'Qty: 1NOTES:', 'inspection notes'],
      {'Qty: 1NOTES:': None, 'inspection notes': ''})]
)
def test_transform_pdf_data_to_dict(test_list, er):
    ar = convert_pdf_data_list_to_dict(test_list)
    assert ar == er, "Incorrect to dict"


@mark.parametrize(
    "mock_data,compare_dict,er",
    [("GRIFFON AVIATION SERVICES LLC PN: tst SN: 123123 DESCRIPTION: PART",
      {'GRIFFON AVIATION SERVICES LLC': '', 'PN': 'tst', 'SN': '123123', 'DESCRIPTION': 'PART', 'LOCATION': '111'},
      {"missing keys": ['LOCATION']}),
     ("GRIFFON AVIATION SERVICES LLC PN: tst SN: 123123 DESCRIPTION: PART",
      {'GRIFFON AVIATION SERVICES LLC': '', 'PN': 'tst', 'SN': '123123', 'DESCRIPTION': 'PART'},
      {"missing keys": []})]
)
@patch('compare_pdf.get_pdf_data')
def test_compare_pdfs(mock_method, mock_data, compare_dict, er):
    mock_method.return_value = mock_data
    ar = compare_pdfs("test_task.pdf", compare_dict)
    assert ar == er, "Incorrect compare data"
