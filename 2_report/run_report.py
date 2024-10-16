import subprocess
import os
import pandas as pd


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


df = pd.read_csv("data/bop_short.csv")
df.set_index('date', inplace=True)

# generate input.tex with replaced

value_change = round(df['ca'].diff(12).iloc[-1],2)
sign_change = "өсжээ" if df['ca'].diff(12).iloc[-1] > 0 else "бууржээ"

context_input = {
    "Date": "Тархаасан: 2024 оны 08 дугаар сарын 12",
    "value_change": value_change,
    "sign_change": sign_change
}
generate_latex_file("report/input_template.tex", "report/input.tex", context_input)


data_dict = {
    "ca": df.iloc[-1]['ca'],"ca_l1": df.iloc[-13]['ca'],"ca_l2": df.iloc[-25]['ca'],
    "ca_diff": df['ca'].diff(12).iloc[-1],"ca_diff_pct": df['ca'].diff(12).iloc[-1]/df['ca'].shift(12).iloc[-1],
    "cap": df.iloc[-1]['cap'],"cap_l1": df.iloc[-13]['cap'],"cap_l2": df.iloc[-25]['cap'],
    "cap_diff": df['cap'].diff(12).iloc[-1],"cap_diff_pct": df['cap'].diff(12).iloc[-1]/df['cap'].shift(12).iloc[-1],
    "fa": df.iloc[-1]['fa'],"fa_l1": df.iloc[-13]['fa'],"fa_l2": df.iloc[-25]['fa'],
    "fa_diff": df['fa'].diff(12).iloc[-1],"fa_diff_pct": df['fa'].diff(12).iloc[-1]/df['fa'].shift(12).iloc[-1],
    "eo": df.iloc[-1]['eo'],"eo_l1": df.iloc[-13]['eo'],"eo_l2": df.iloc[-25]['eo'],
    "eo_diff": df['eo'].diff(12).iloc[-1],"eo_diff_pct": df['eo'].diff(12).iloc[-1]/df['eo'].shift(12).iloc[-1],
    "res": df.iloc[-1]['res'],"res_l1": df.iloc[-13]['res'],"res_l2": df.iloc[-25]['res'],
    "res_diff": df['res'].diff(12).iloc[-1],"res_diff_pct": df['res'].diff(12).iloc[-1]/df['res'].shift(12).iloc[-1]
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
