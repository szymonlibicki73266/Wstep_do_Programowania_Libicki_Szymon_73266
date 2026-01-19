import math
import keyword

print("Functions in math module:")
math_functions = [name for name in dir(math) if callable(getattr(math, name)) and not name.startswith('_')]
for func in sorted(math_functions):
    print(f"  {func}")
print("\nFunctions in keyword module:")
keyword_functions = [name for name in dir(keyword) if callable(getattr(keyword, name)) and not name.startswith('_')]
for func in sorted(keyword_functions):
    print(f"  {func}")
tuple_methods = [name for name in dir(tuple) if not name.startswith('_')]
for method in sorted(tuple_methods):
    print(f"  {method}")