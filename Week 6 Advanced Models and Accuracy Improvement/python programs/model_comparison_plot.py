import matplotlib.pyplot as plt
import os

# Correct path setup
current_dir = os.path.dirname(__file__)
week6_dir = os.path.abspath(os.path.join(current_dir, ".."))

# Data (replace later with real values if needed)
models = ["Linear Regression", "Random Forest"]
mae_scores = [5.2, 3.1]

# Plot
plt.figure()
plt.bar(models, mae_scores)

plt.title("Model Comparison (MAE)")
plt.xlabel("Models")
plt.ylabel("Error (MAE)")

# Save correctly
output_path = os.path.join(week6_dir, "outputs", "model_comparison.png")
plt.savefig(output_path)

print("✅ Graph saved at:", output_path)

plt.show()