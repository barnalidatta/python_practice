# main.py
from my_lib import MathUtils, TextProcessor

# --- 1. Calling the Stateless Utility ---
# Because of @staticmethod, we DO NOT instantiate. 
# We call methods directly on the class container name.
sum_result = MathUtils.add(10, 25)
is_valid = MathUtils.is_positive(sum_result)

print(f"Stateless Math Result: {sum_result} (Positive: {is_valid})")
# Output: Stateless Math Result: 35 (Positive: True)


# --- 2. Calling the Stateful Utility ---
# Because it uses 'self', we MUST instantiate it with initial data first.
# Then, we can chain the utility methods together.
processor = TextProcessor("   initial raw text data   ")
clean_text = processor.remove_whitespace().uppercase().get_result()

print(f"Stateful Text Result: '{clean_text}'")
# Output: Stateful Text Result: 'INITIAL RAW TEXT DATA'