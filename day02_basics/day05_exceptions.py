# Example 1: Handling division errors
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print("Result:", result)

except ValueError:
    print("❌ Please enter only numbers.")
except ZeroDivisionError:
    print("❌ You cannot divide by zero.")
except Exception as e:
    print("⚠️ Unexpected error:", e)
finally:
    print("✅ Program completed.")