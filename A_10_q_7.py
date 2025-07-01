import matplotlib.pyplot as plt

#random data for the two semesters
subjects = ['Math', 'DSA', 'DBMS', 'CN', 'OS']
sem1_scores = [85, 78, 88, 90, 80]
sem2_scores = [82, 80, 85, 92, 83]

x = range(len(subjects))

# Plotting
plt.figure(figsize=(10, 6))
bar_width = 0.35

plt.bar(x, sem1_scores, width=bar_width, label='Semester 1', color='skyblue')
plt.bar([i + bar_width for i in x], sem2_scores, width=bar_width, label='Semester 2', color='lightgreen')

# Customizations
plt.xlabel('Subjects', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.title('Semester 1 vs Semester 2 Result Comparison', fontsize=14, fontweight='bold')
plt.xticks([i + bar_width/2 for i in x], subjects)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
