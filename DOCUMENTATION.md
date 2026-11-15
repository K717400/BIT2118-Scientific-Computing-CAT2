# BIT 2118 Scientific Computing CAT 2 — Documentation

## Question 1: Python objects, exceptions and data processing
A `Product` class groups product attributes and behaviour. The constructor stores a name and numeric price; `total_cost()` multiplies the price by the quantity. Converting user-entered prices with `float()` is protected by `try/except ValueError`, so invalid text is handled without abruptly stopping the program.

Pandas reads the CSV into a DataFrame. `drop_duplicates()` removes repeated rows, while `dropna(subset=['Sales'])` removes records whose Sales value is missing. The cleaned data is saved to a new CSV, and Product A sales are plotted against day.

**Critical evaluation:** Removing records from days affected by a system failure may make the dataset cleaner, but it can also hide a real operational problem and bias conclusions. Keep an untouched raw copy, flag failure-period records, document the reason for exclusion, and compare results with and without those records. Imputation or a separate missing-data category may be more appropriate depending on the analysis.

## Question 2: Linear algebra and SciPy
In `Ax=b`, A is the matrix of coefficients, x is the vector of unknown variables, and b is the vector of constants. NumPy solves the system `4x+2y=20` and `8x+12y=72`, giving x=3 and y=4.

SciPy's `lu()` returns permutation, lower-triangular and upper-triangular matrices. The program checks the factorisation using `P @ A == L @ U` with `numpy.allclose()` to allow for floating-point rounding.

An eigenvector v and eigenvalue λ satisfy `Av=λv`. The program calculates eigenvalues/eigenvectors of `[[2,1],[1,2]]` and verifies the relationship numerically.

## Question 3: Visualisation, summation and integration
A bar chart displays the ten student scores. The summation is evaluated by adding `r+5` for every integer r from 0 through 1000, giving 505505. The definite integral of `x^3+2x+5` from 1 to 2 is evaluated using the antiderivative `x^4/4 + x^2 + 5x`, giving an area of 11.75 square units.

High-level languages provide abstractions that make programs easier for people to read and maintain. Low-level languages are closer to machine instructions and hardware. MATLAB is generally considered a high-level, fourth-generation technical computing language because it provides matrix-oriented operations and specialised numerical libraries.

## Question 4: Numerical methods and modelling
For `dV/dt=-0.1V`, Euler's method uses `V(n+1)=V(n)+h(-0.1V(n))`. With h=1 minute and initial voltage 12 V, the two estimates are 10.8 V and 9.72 V. SciPy `solve_ivp` numerically solves the differential equation over 0–20 minutes and evaluates the solution at each whole minute.

Ethical considerations include informed consent where people provide data, privacy/confidentiality, and honest reporting of assumptions and limitations. Modelling challenges include incomplete data, measurement errors, simplifying assumptions, uncertain parameters and computational constraints.

## Question 5: Data and numerical representation
In `150*quantity+200`, 150 and 200 are fixed numeric values (constants in this calculation), while `quantity` is a variable. A single reading is one scalar value; a list stores a sequence of values; a Pandas DataFrame stores labelled tabular data.

Floating-point numbers are approximations in binary, so some decimal values cannot be represented exactly. Small rounding differences may occur; numerical comparisons should use a tolerance such as `numpy.isclose()` rather than exact equality.

The NumPy array of masses in kilograms is multiplied by 1000 to convert each value to grams: 2200, 2400, 2600 and 2800 g.

## AI-use acknowledgement
The assignment instructions ask students to acknowledge AI/LLM use. Edit the following statement so that it accurately describes your own use:

“An AI language model was used as a learning and drafting aid to help explain selected Python and scientific-computing concepts. I reviewed, tested and edited the submitted work and take responsibility for the final answers.”

## References (APA 6th edition style)
Harris, C. R., et al. (2020). Array programming with NumPy. *Nature, 585*, 357–362. https://doi.org/10.1038/s41586-020-2649-2

McKinney, W. (2010). Data structures for statistical computing in Python. In *Proceedings of the 9th Python in Science Conference* (pp. 51–56).

Virtanen, P., et al. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods, 17*, 261–272. https://doi.org/10.1038/s41592-019-0686-2

Python Software Foundation. (n.d.). *Python 3 documentation*. Retrieved from https://docs.python.org/3/
