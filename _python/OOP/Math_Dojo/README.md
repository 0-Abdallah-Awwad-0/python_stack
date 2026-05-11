# MathDojo Assignment

This assignment practices Object-Oriented Programming, method chaining, and flexible arguments.

## Main Idea

The MathDojo class keeps track of a result and allows adding or subtracting numbers.

## Attribute

### result
Stores the current calculation result.
It starts at 0.

## Methods

### add(num, *nums)
Adds one or more numbers to result.

The first number is required.
Extra numbers are stored inside *nums.

Example:
add(2, 5, 1)

### subtract(num, *nums)
Subtracts one or more numbers from result.

Example:
subtract(3, 2)

## Method Chaining

Each method returns self so methods can be chained together.

Example:
md.add(2).add(2, 5, 1).subtract(3, 2)

## Purpose

This assignment practices:
- Classes
- Objects
- Attributes
- Methods
- return self
- Method chaining
- Flexible arguments using *nums
