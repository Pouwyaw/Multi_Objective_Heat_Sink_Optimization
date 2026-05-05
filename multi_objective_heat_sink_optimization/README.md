# Multi-Objective Optimization of Heat Sink Design using NSGA-II

## 📌 Overview

This project focuses on the **multi-objective optimization of a heat sink design** using evolutionary algorithms. The goal is to simultaneously:

* Minimize the **steady-state temperature** of the system
* Minimize a **cost/size-related objective function (Z)**

The optimization is subject to **thermal, geometric, and mass constraints**, making it a realistic engineering design problem.

---

## 🧠 Problem Description

Heat sinks are widely used in electronic systems to dissipate heat. Their performance depends on several design variables:

* Fin thickness (`t`)
* Fin length (`L`)
* Number of fins (`n`)
* Base width (`W`)
* Total width (`Y`)

This project formulates the design as a **multi-objective optimization problem**:

### Objectives:

* Minimize temperature:
  `T(x)`
* Minimize cost/size:
  `Z(x)`

### Constraints:

* Maximum mass limit
* Geometric feasibility
* Fin spacing constraints

---

## 🔬 Mathematical Model

The thermal behavior is modeled using fin heat transfer theory.

### Heat Transfer from a Fin:

Q_{fin} = (T - T_{\infty}) \sqrt{hPkA_c} \cdot \frac{\sinh(mL) + \frac{h}{mk}\cosh(mL)}{\cosh(mL) + \frac{h}{mk}\sinh(mL)}

Where:

* (m = \sqrt{\frac{hP}{kA_c}})
* (h): convection coefficient
* (k): thermal conductivity
* (A_c): cross-sectional area
* (P): perimeter

### Total Heat Balance:

$$
n \cdot Q_{fin} + Q_{nofin} = P_{loss}
$$

This nonlinear equation is solved numerically to compute the temperature.

---

## ⚙️ Methods Used

This project combines numerical modeling with advanced optimization techniques:

### 🔹 Multi-objective Optimization

* **NSGA-II (Non-dominated Sorting Genetic Algorithm II)**
* Generates the **Pareto front**

### 🔹 Single-objective Optimization

* Weighted-sum method using **Genetic Algorithm (GA)**

### 🔹 Numerical Methods

* Root finding:

  * Brent’s method
  * Secant method (fallback)

### 🔹 Constraint Handling

* Mass constraint
* Fin spacing constraints
* Design variable bounds

---

## 📊 Results

The algorithm produces a **Pareto front** representing the trade-off between:

* Lower temperature (better cooling)
* Lower cost/size

### Key Points:

* **Ideal Point**: Best possible values for both objectives
* **Knee Point**: Best trade-off solution

Example visualization:

* Pareto front
* Highlighted ideal and knee points

---

## 🗂️ Project Structure

```
heat-sink-optimization/
│
├── main.py
├── model.py
├── optimization.py
├── utils.py
│
├── results/
│   ├── pareto.png
│   ├── weighted.png
│
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Install dependencies:

```bash
pip install numpy scipy matplotlib pymoo
```

### 2. Run the code:

```bash
python main.py
```

---

## 📌 Key Features

* Real-world engineering modeling
* Multi-objective optimization
* Constraint-aware design
* Pareto front analysis
* Automatic knee-point detection

---

## 🚀 Applications

* Thermal management in electronics
* Mechanical design optimization
* Engineering trade-off analysis

---

## 🧩 Future Improvements

* Surrogate modeling (e.g., Gaussian Process)
* Sensitivity analysis
* Mixed-integer optimization
* CFD-based validation

---

## 👤 Author

**Pouya Mirzaei**
Engineering Student | Optimization & AI Enthusiast

---

## ⭐ Notes

This project demonstrates how **physics-based modeling** can be combined with **evolutionary algorithms** to solve complex engineering problems with multiple competing objectives.
