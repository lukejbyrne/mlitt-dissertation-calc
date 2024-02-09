# Adjusting the code to reflect the specific values provided in the dissertation
# Since the exact raw data for each hypothesis isn't provided, we'll use the reported mean true effect sizes
# and significance levels directly from the summary provided earlier.

# Hypothetical calculations will be replaced with direct inputs based on dissertation findings.

results_direct = {
    "Hypothesis": [
        "Performance (H1)",
        "Inter-role Conflict (H2a)",
        "Exhaustion (H2b)",
        "Life Satisfaction (H2c)",
        "Organizational Commitment (H3)",
        "Job Satisfaction (H4)"
    ],
    "Mean True Effect Size": [
        0.149,  # Mean effect size for Performance
        -0.072,  # Mean effect size for Inter-role Conflict
        -0.298,  # Mean effect size for Exhaustion
        0.314,  # Mean effect size for Life Satisfaction
        0.220,  # Mean effect size for Organizational Commitment
        0.188   # Mean effect size for Job Satisfaction
    ],
    "Significance Level": [
        "p<0.10",
        "p<0.01",
        "p<0.05",
        "p<0.10",
        "p<0.10",
        "p<0.01"
    ],
    "Heterogeneity (I^2)": [
        "63%",  # Heterogeneity for Performance
        "89%",  # Heterogeneity for Inter-role Conflict
        "79%",  # Heterogeneity for Exhaustion
        "Not Provided",  # Heterogeneity for Life Satisfaction
        "Not Provided",  # Heterogeneity for Organizational Commitment
        "90%"   # Heterogeneity for Job Satisfaction
    ]
}

# Convert the adjusted results into a DataFrame for presentation
results_df_direct = pd.DataFrame(results_direct)

# Generate a README.md content with results and comments
readme_content = """
# Dissertation Statistical Analysis Results

This document summarizes the statistical analysis results from the dissertation.

## Hypotheses and Results

| Hypothesis | Mean True Effect Size | Significance Level | Heterogeneity (I^2) |
|------------|-----------------------|--------------------|---------------------|
"""

for index, row in results_df_direct.iterrows():
    readme_content += f"| {row['Hypothesis']} | {row['Mean True Effect Size']} | {row['Significance Level']} | {row['Heterogeneity (I^2)']} |\n"

readme_content += """
## Comments

- The mean true effect sizes indicate the magnitude of the effect autonomy has on various outcomes related to remote work.
- Significance levels suggest the statistical confidence in these effects, with p<0.05 typically considered statistically significant.
- Heterogeneity (I^2) values provide insight into the variability among study results included in the meta-analysis.
"""

# Write README content to a file
readme_file_path = '/mnt/data/README_dissertation_results.md'
with open(readme_file_path, 'w') as file:
    file.write(readme_content)

readme_file_path
