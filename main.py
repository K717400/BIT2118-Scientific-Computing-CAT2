"""BIT 2118 Scientific Computing CAT 2 solutions.
Run with: python main.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import lu
from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

print("\nQUESTION 1")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def total_cost(self, quantity):
        return self.price * quantity

item = Product("Notebook", 30)
print(f"1.1 {item.name}: 5 units cost = {item.total_cost(5):.2f}")

def convert_price(value):
    try:
        return float(value)
    except ValueError:
        print(f"Invalid price: {value!r}. Enter a numeric value.")
        return None

print("1.2 Valid conversion:", convert_price("125.50"))
print("1.2 Invalid conversion:", convert_price("twelve"))

csv_path = ROOT / "sales.csv"
sales = pd.read_csv(csv_path)
print("\n1.3 Original sales data:\n", sales)
clean = sales.drop_duplicates().dropna(subset=["Sales"]).copy()
clean.to_csv(OUT / "clean_sales.csv", index=False)
print("Cleaned sales data:\n", clean)
product_a = clean[clean["Product"] == "Product A"]
plt.figure()
plt.plot(product_a["Day"], product_a["Sales"], marker="o")
plt.title("Product A Sales vs Day")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT / "product_a_sales.png")
plt.close()
print("Saved outputs/clean_sales.csv and outputs/product_a_sales.png")

print("\nQUESTION 2")
A = np.array([[4, 2], [8, 12]], dtype=float)
b = np.array([20, 72], dtype=float)
solution = np.linalg.solve(A, b)
print("2.1 In Ax=b, A is the coefficient matrix, x the unknown vector, and b the constants vector.")
print("2.2 Solution [x, y] =", solution)
P, L, U = lu(A)
print("2.3 P=\n", P, "\nL=\n", L, "\nU=\n", U)
print("Check P@A == L@U:", np.allclose(P @ A, L @ U))
B = np.array([[2, 1], [1, 2]], dtype=float)
eigenvalues, eigenvectors = np.linalg.eig(B)
print("2.4 Eigenvalues:", eigenvalues)
for i, value in enumerate(eigenvalues):
    v = eigenvectors[:, i]
    print(f"Av=lambda*v for lambda={value:.4f}:", np.allclose(B @ v, value * v))

print("\nQUESTION 3")
scores = [75, 53, 90, 87, 50, 85, 92, 75, 60, 95]
plt.figure()
plt.bar(range(1, 11), scores)
plt.title("Student Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.xticks(range(1, 11))
plt.tight_layout()
plt.savefig(OUT / "student_scores_bar.png")
plt.close()
print("3.1 Scores bar chart saved to outputs/student_scores_bar.png")
total = sum(r + 5 for r in range(0, 1001))
print("3.2 Sum from r=0 to 1000 of (r+5) =", total)
# Integral of x^3 + 2x + 5 from 1 to 2
area = ((2**4)/4 + 2**2 + 5*2) - ((1**4)/4 + 1**2 + 5*1)
print("3.3 Area under y=x^3+2x+5 from x=1 to x=2 =", area)

print("\nQUESTION 4")
V = 12.0
h = 1.0
for step in range(2):
    V = V + h * (-0.1 * V)
    print(f"4.1 Euler voltage after minute {step+1}: {V:.4f} V")

def decay(t, voltage):
    return -0.1 * voltage

times = np.arange(0, 21, 1)
result = solve_ivp(decay, (0, 20), [12.0], t_eval=times)
plt.figure()
plt.plot(result.t, result.y[0], marker="o")
plt.title("Battery Voltage Decay")
plt.xlabel("Time (minutes)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUT / "battery_voltage.png")
plt.close()
print("4.2 solve_ivp completed; plot saved to outputs/battery_voltage.png")
print("4.3 Ethical considerations: informed consent; privacy/confidentiality; honest reporting and transparency.")
print("4.4 Modelling challenges: incomplete data; measurement errors; simplifying assumptions; parameter uncertainty; computational limits.")

print("\nQUESTION 5")
quantity = 4
unit_price = 150
delivery_fee = 200
total_cost = unit_price * quantity + delivery_fee
print("5.1 Constants: 150 and 200; variable: quantity; total cost =", total_cost)
reading = 12.5
readings = [12.5, 13.0, 12.8]
frame = pd.DataFrame({"Reading": readings})
print("5.2 Single reading:", reading, "| List:", readings, "| DataFrame:\n", frame)
print("5.3 Floating-point calculations can have tiny representation/rounding errors; compare using a tolerance (e.g. np.isclose).")
masses_kg = np.array([2.2, 2.4, 2.6, 2.8])
masses_g = masses_kg * 1000
print("5.4 Masses in grams:", masses_g)
print("\nAll tasks completed. See DOCUMENTATION.md for explanations and interpretations.")
