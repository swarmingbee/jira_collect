"""
Module responsible for report
"""

import csv


def project_export(complete_obj, project_name):
    """
    Def responsible for create the csv output
    """
    output_file = "/tmp/" + project_name + ".csv"
    print("Saving the file '{}'".format(output_file))
    with open(output_file, "w", encoding="utf-8") as file_ref:
        csv_file = csv.writer(file_ref)
        csv_file.writerows(complete_obj)
