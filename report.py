import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# reading csv file
file = pd.read_csv("data.csv")

# basic analysis
avg_marks = file["Marks"].mean()
max_marks = file["Marks"].max()
min_marks = file["Marks"].min()

# graph create
plt.bar(file["Student"], file["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks Report")
plt.savefig("marks_graph.png")
plt.close()

# pdf report
pdf = SimpleDocTemplate("student_report.pdf")

style = getSampleStyleSheet()
content = []

content.append(Paragraph("Student Marks Report", style['Title']))
content.append(Spacer(1,20))

content.append(Paragraph("Average Marks: " + str(avg_marks), style['Normal']))
content.append(Paragraph("Highest Marks: " + str(max_marks), style['Normal']))
content.append(Paragraph("Lowest Marks: " + str(min_marks), style['Normal']))

content.append(Spacer(1,20))
content.append(Image("marks_graph.png", width=400, height=250))

pdf.build(content)

print("PDF report created successfully")