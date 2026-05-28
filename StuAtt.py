import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel(r"C:\Users\Sanjay\OneDrive\temp\attendance.xlsx")
df["attendance_percentage"]=(df["classes_Attended"]/df["total_classes"])*100
print("Attendance Report:")
print(df)
avg_attendance=np.mean(df["attendance_percentage"])
highest=df.loc[df["attendance_percentage"].idxmax()]
lowest=df.loc[df["attendance_percentage"].idxmin()]
low_attendance=df[df["attendance_percentage"]<75]
print("\nAverage Attendance:{:.2f}%".format(avg_attendance))
print("Highest Attendance:")
print(f"{highest['student']}-{highest['attendance_percentage']:.2f}%")
print("Lowest Attendance:")
print(f"{lowest['student']}-{lowest['attendance_percentage']:.2f}%")
df.to_excel("attendance_report.xlsx",index=False)
plt.figure(figsize=(10,9))
plt.bar(df['student'],df['attendance_percentage'])
plt.axhline(y=75,linestyle='--',label='Minimum Required(75%)')
plt.title("Attendance Analysis")
plt.xlabel("Students",fontweight='bold',fontsize=12)
plt.ylabel("Attendance Percentage",fontweight='bold',fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()
