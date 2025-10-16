# Deep Learning for High-Dimensional PDEs & BSDEs

This repository contains the code for solving high-dimensional Partial Differential Equations (PDEs) and Backward Stochastic Differential Equations (BSDEs) using deep learning techniques, as presented in my Bachelor’s thesis.

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

## Introduction
This work explores the application of deep learning to solve high-dimensional PDEs and BSDEs, addressing the "curse of dimensionality." It leverages deep learning techniques to approximate solutions to complex equations, with particular focus on problems arising in finance and control theory.

The main contribution of this work is the implementation of the **Deep BSDE Solver**, which utilizes deep neural networks to estimate the gradient at each time step and solves the equations numerically using Monte Carlo simulations.

## Methodology
1. **High-Dimensional PDEs and BSDEs:**  
   The thesis provides an overview of high-dimensional problems and their applications, particularly in financial modeling and control theory. Key challenges, such as the curse of dimensionality, are discussed.

2. **Conversion to BSDEs:**  
   The work demonstrates how high-dimensional PDEs can be converted into Backward Stochastic Differential Equations (BSDEs) and how these equations are solved using deep learning methods.

3. **Deep BSDE Solver:**  
   A deep neural network is used to approximate gradients and solve the BSDEs. This method is validated on several examples, including pricing derivatives in a market with default risk and varying interest rates.

## Installation

To install and run the code, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   #pip install -r requirements.txt
   ```


## Results
The code is tested on several high-dimensional PDEs used in finance, including:
- Recursive pricing with default risk.
- Pricing in markets with different interest rates for borrowing and lending.
- The results include numerical simulations and visualizations showing the performance of the solver.

## Contributing
If you would like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request. Please ensure that your code follows the existing structure and includes appropriate tests.

## License: This project is licensed under the MIT License.

## References
- Darbon, J., Osher, S. (2016). Algorithms for overcoming the curse of dimensionality for certain Hamilton Jacobi equations arising in control theory and elsewhere. Research in the Mathematical Sciences, 3(1), 1-26.
- Henry-Labordere, P., Oudjane, N., Tan, X., Touzi, N., Warin, X. (2019). Branching diffusion representation of semilinear PDEs and Monte Carlo approximation. Annales de l’Institut Henri Poincaré.
- Han, J., Jentzen, A. (2017). Deep learning-based numerical methods for high-dimensional parabolic partial differential equations and backward stochastic differential equations. Communications in mathematics and statistics, 5(4), 349-380.
