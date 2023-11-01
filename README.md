# democratic_failures_library

This library is designed to assist researchers with determining how often various democratic failures occur in various election systems.

Right now, I have written code that:

- Translates a preference from ranked to pairwise or vice versa
- Runs a set of social preferences on various election systems
- Can determine if a given election violates a particular democratic criteria

In the future, I plan to add:

- More democratic criteria
- More robust testing
- For monotonicity, a function that gives reliable results for elections with >3 candidates
- More election systems
- Make this into a library that can be installed using pip
