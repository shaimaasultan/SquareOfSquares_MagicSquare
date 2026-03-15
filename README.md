# SquareOfSquares Project

## Overview
This repository contains code, documents, and resources related to the SquareOfSquares project, which appears to involve mathematical algorithms, algebraic equation solving, and AI verification.
## Project Analysis Summary

### Impossibility of a $3\times 3$ Magic Square of Distinct Squares

- The project develops a unified algebraic and geometric framework to analyze the problem of constructing a $3\times 3$ magic square using nine distinct perfect squares.
- By expressing each entry as $C^2 + r_i$, the eight non-central variables satisfy a homogeneous linear system of rank 3, yielding a 5-dimensional linear $r$-space.
- The perfect-square condition forces each $r_i$ onto a quadratic lattice, replacing linear freedom with discrete constraints.
- Algebraic and geometric arguments show that the intersection of this lattice with the magic subspace is empty, proving the impossibility of a true $3\times 3$ magic square of distinct squares.

### Near-Magic Squares and Relaxed Constraints

- Relaxing a single diagonal condition increases the degrees of freedom, allowing near-magic configurations.
- Quantitative bounds are provided for how close such configurations can come to satisfying all eight line-sum conditions.
- The framework clarifies the source of the obstruction and explains the abundance of near-magic examples.

### Linear and Quadratic Structure

- The linear $r$-system is universal for all magic squares, but the perfect-square requirement imposes quadratic constraints that are too rigid for a solution.
- The geometric incompatibility between the linear $r$-space and the quadratic lattice explains the impossibility.

---

For more details, see the documentation in `Documents/SquareOfSquares2.pdf`.

## Folder Structure

- **AI_Verfication/**
  - HTML files and resources for AI verification and algebraic equation solving.
- **Code/**
  - Python scripts for mathematical computations, grid relaxation, equation solving, and validation.
- **Documents/**
  - LaTeX files, auxiliary files, and documentation for the project.
  - Includes `SquareOfSquares2.tex` and its compiled output `SquareOfSquares2.pdf`.
- **images/**
  - Image resources (not detailed here).

## Key Files

- `Code/squareOfSquares.py`: Main script for square of squares computations.
- `Documents/SquareOfSquares2.tex`: LaTeX source for project documentation.
- `Documents/SquareOfSquares2.pdf`: Compiled PDF documentation.

## Usage

1. Clone the repository:
   ```sh
   git clone <repo-url>
   ```
2. Explore the Python scripts in the `Code` folder.
3. Review documentation in the `Documents` folder, especially `SquareOfSquares2.pdf`.

## Requirements

- Python 3.x
- (Optional) LaTeX for compiling `.tex` files

