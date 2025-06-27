import os
import pandas as pd
from fpdf import FPDF

# Folder and file paths
folder_path = r"C:\Users\satya\OneDrive\Desktop\Python Internship\TASK 2"
csv_file = os.path.join(folder_path, "data.csv")
pdf_file = os.path.join(folder_path, "formatted_report.pdf")

# Step 1: Create sample data.csv if it doesn't exist
if not os.path.isfile(csv_file):
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
        'Department': ['Sales', 'Marketing', 'Sales', 'Marketing', 'IT'],
        'Score': [85, 90, 78, 95, 88]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print(f"Sample data.csv created at {csv_file}")
else:
    print(f"data.csv already exists at {csv_file}")

# Step 2: Read data
data = pd.read_csv(csv_file)

# Step 3: Analyze data
avg_scores = data.groupby('Department')['Score'].mean().round(2)
top_performer = data.loc[data['Score'].idxmax()]

# Step 4: Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CODTECH Internship Report', 0, 1, 'C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, 'Task 2: Automated Report Generation', 0, 1, 'C')
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Step 5: Generate PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

pdf.cell(0, 10, 'Average Scores by Department:', ln=1)
for dept, avg in avg_scores.items():
    pdf.cell(0, 10, f'{dept}: {avg}', ln=1)

pdf.ln(10)
pdf.cell(0, 10, 'Top Performer:', ln=1)
pdf.cell(0, 10, f"Name: {top_performer['Name']}", ln=1)
pdf.cell(0, 10, f"Department: {top_performer['Department']}", ln=1)
pdf.cell(0, 10, f"Score: {top_performer['Score']}", ln=1)

pdf.output(pdf_file)

print(f"PDF report generated successfully at:\n{pdf_file}")