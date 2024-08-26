import subprocess
import os


def compile_latex_to_pdf(tex_file):
    result = subprocess.run(["xelatex", tex_file], capture_output=True, text=True)
    
    # Print the output and errors for debugging
    print(result.stdout)
    print(result.stderr)

def generate_latex_file(template_path, output_path, context):
    with open(template_path, 'r', encoding='utf-8-sig') as file:
        latex_template = file.read()
    
    # Replace placeholders in the template
    for key, value in context.items():
        latex_template = latex_template.replace(f'<<{key}>>', str(value))
    
    with open(output_path, 'w', encoding='utf-8-sig') as file:
        file.write(latex_template)


# Define the LaTeX template
template_path = "report/report_template.tex"
output_tex_path = "report/generated_report.tex"
output_pdf_path = "bop_report_demo.pdf"

# generate input.tex with replaced
context_input = {
    "Date": "Тархаасан: 2024 оны 08 дугаар сарын 12",
}
generate_latex_file("report/input_template.tex", "report/input.tex", context_input)

data_dict = {
    "ca": -309.2,"ca_l1": 221.2,"ca_l2": 1360.8,"ca_diff": -530.3,"ca_diff_pct": "-",
    "cap": 78.3,"cap_l1": 59.9,"cap_l2": 54.6,"cap_diff": 18.4,"cap_diff_pct": 30.8,
    "fa": -720.6,"fa_l1": -58.3,"fa_l2": -925.8,"fa_diff": -662.4,"fa_diff_pct": 12.4,
    "eo": -547.1,"eo_l1": 134.4,"eo_l2": -677.5,"eo_diff": -681.5,"eo_diff_pct": "-",
    "res": -57.3,"res_l1": 473.7,"res_l2": 1058,"res_diff": -531.0,"res_diff_pct": "-"
}

context_input = {
    "ca": data_dict["ca"],"ca_l1": data_dict["ca_l1"],"ca_l2": data_dict["ca_l2"],"ca_diff": data_dict["ca_diff"],"ca_diff_pct": data_dict["ca_diff_pct"],
    "cap": data_dict["cap"],"cap_l1": data_dict["cap_l1"],"cap_l2": data_dict["cap_l2"],"cap_diff": data_dict["cap_diff"],"cap_diff_pct": data_dict["cap_diff_pct"],
    "fa": data_dict["fa"],"fa_l1": data_dict["fa_l1"],"fa_l2": data_dict["fa_l2"],"fa_diff": data_dict["fa_diff"],"fa_diff_pct": data_dict["fa_diff_pct"],
    "eo": data_dict["eo"],"eo_l1": data_dict["eo_l1"],"eo_l2": data_dict["eo_l2"],"eo_diff": data_dict["eo_diff"],"eo_diff_pct": data_dict["eo_diff_pct"],
    "res": data_dict["res"],"res_l1": data_dict["res_l1"],"res_l2": data_dict["res_l2"],"res_diff": data_dict["res_diff"],"res_diff_pct": data_dict["res_diff_pct"]
}
generate_latex_file("report/table_template.tex", "report/table.tex", context_input)


# Generate the report LaTeX file
context_rep = {
    "Logo": "report/company_logo.png",
}
generate_latex_file(template_path, output_tex_path, context_rep)

# Compile the LaTeX file to PDF
compile_latex_to_pdf(output_tex_path)

# Optionally, clean up auxiliary files
os.remove("generated_report.aux")
os.remove("generated_report.log")
