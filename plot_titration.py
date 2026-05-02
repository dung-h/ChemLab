import numpy as np
import matplotlib.pyplot as plt

# Exact data points from the textbook image
V_data = np.array([0, 2, 4, 6, 8, 9, 9.2, 9.4, 9.6, 9.8, 10, 11, 12, 13])
pH_data = np.array([0.96, 1.14, 1.33, 1.59, 1.98, 2.38, 2.56, 2.73, 3.36, 7.26, 10.56, 11.70, 11.97, 12.01])

# For a smooth monotonic curve, we must use PchipInterpolator to avoid overshoot/wiggles
from scipy.interpolate import PchipInterpolator
pchip = PchipInterpolator(V_data, pH_data)
V_smooth = np.linspace(V_data.min(), V_data.max(), 500)
pH_smooth = pchip(V_smooth)

# Very wide figure
plt.figure(figsize=(15, 7))
plt.plot(V_smooth, pH_smooth, linestyle='-', color='darkblue', linewidth=2.5, label='Đường cong chuẩn độ')
plt.scatter(V_data, pH_data, color='blue', s=40, zorder=5)

# Equivalence point (exactly 9.8, 7.26 per table)
plt.plot(9.8, 7.26, marker='o', color='red', markersize=10, zorder=10)
plt.annotate(f'Điểm tương đương\n(9.8, 7.26)', (10.0, 7.0), color='red', fontweight='bold', fontsize=12)

# Tangent lines (True tangent method: extending the flat regions of the curve)
# Lower tangent: fit a line through V=4, 6, 8
slope_lower = (1.98 - 1.33) / (8 - 4)
intercept_lower = 1.98 - slope_lower * 8
x_lower = np.array([3, 11])
y_lower = slope_lower * x_lower + intercept_lower
plt.plot(x_lower, y_lower, color='gray', linestyle='-', linewidth=2, label='Đường tiếp tuyến')

# Upper tangent: fit a line through V=11, 12, 13
slope_upper = (12.01 - 11.70) / (13 - 11)
intercept_upper = 12.01 - slope_upper * 13
x_upper = np.array([8, 14])
y_upper = slope_upper * x_upper + intercept_upper
plt.plot(x_upper, y_upper, color='gray', linestyle='-', linewidth=2)

# Vertical line showing pH jump (Bước nhảy pH)
plt.vlines(x=9.8, ymin=slope_lower*9.8+intercept_lower, ymax=slope_upper*9.8+intercept_upper, color='darkgreen', linestyle=':', linewidth=2, label='Bước nhảy pH')
plt.annotate('Bước nhảy pH', (9.6, 6.5), ha='right', va='center', color='darkgreen', fontsize=11)

# Annotate key points
plt.annotate('(9.6, 3.36)', (9.6, 3.36), textcoords="offset points", xytext=(-30, -15), ha='center', fontsize=10, arrowprops=dict(arrowstyle='->'))
plt.annotate('(10.0, 10.56)', (10.0, 10.56), textcoords="offset points", xytext=(30, 15), ha='center', fontsize=10, arrowprops=dict(arrowstyle='->'))

plt.title('Đường cong chuẩn độ HCl bằng NaOH (Dữ liệu thực nghiệm)', fontsize=18, pad=20)
plt.xlabel('Thể tích NaOH (mL)', fontsize=14)
plt.ylabel('pH', fontsize=14)
plt.grid(True, which='major', linestyle='-', alpha=0.3)
plt.xlim(0, 15) # Match data range
plt.ylim(0, 14)
plt.xticks(np.arange(0, 16, 1))
plt.yticks(np.arange(0, 15, 1))
plt.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.savefig('titration_curve.png', dpi=300)
print("Saved titration_curve.png")
