import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Since the exact raw data for each hypothesis isn't provided, we'll use the reported mean true effect sizes and significance levels directly from the summary provided earlier.

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


# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# One may want to adjust 'Mean True Effect Size' for visualization purposes, 
# e.g., taking the absolute value if you want to visualize the magnitude regardless of direction
# results_df_direct['Absolute Mean Effect Size'] = results_df_direct['Mean True Effect Size'].abs()

# Create a bar plot
plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    x='Mean True Effect Size', 
    y='Hypothesis', 
    data=results_df_direct,
    palette='coolwarm'  # This palette shows a good contrast for positive and negative values
)

plt.title('Mean True Effect Sizes by Hypothesis')
plt.xlabel('Mean True Effect Size')
plt.ylabel('Hypothesis')

# Optional: Adding the significance level as text on the bars
for index, row in results_df_direct.iterrows():
    barplot.text(
        row['Mean True Effect Size'], 
        index, 
        f"{row['Significance Level']}, I²={row['Heterogeneity (I^2)']}", 
        color='black',
        ha="center"
    )

plt.tight_layout()
plt.savefig("Results.png")

# Generate a README.md content with results and comments
readme_content = """
# Dissertation Statistical Analysis Results
## "How To Motivate Remote Employees: A Self-Determination Theory
Perspective"

This document summarizes the statistical analysis results from the dissertation.

## What is Meta-Analysis?
Meta-analysis is a statistical technique used to combine the findings from independent studies to identify patterns, discrepancies, and overall effects across numerous research studies. It goes beyond mere literature review by conducting secondary statistical analysis on the outcomes of relevant studies.
## Why Use Meta-Analysis?
The author chose meta-analysis to systematically review and synthesize existing research on how autonomy impacts remote employees' motivation. This method allows for a comprehensive examination of the collected data, identifying general consensus points, conflicts, and the reliability of the compared studies. It's particularly suited to the dissertation's goal due to the abundance of existing research on Self-Determination Theory (SDT) and its application to remote work environments.
## The Selected Approach
Among various meta-analysis methods, the dissertation utilizes the Hedges and colleagues method, which offers both fixed- and random-effects models. This approach was chosen for its ability to handle the nuances of the studies analyzed, especially considering the potential for diverse outcomes in studies related to autonomy and remote work.
## Statistical Implementation
*Fixed-Effects Meta-Analysis*: The method begins by converting effect sizes into a standard normal metric via Fisher’s r-to-Z transformation, then calculating a weighted average of these transformed scores.
*Calculating Homogeneity of Effect Sizes*: It involves assessing the consistency among study outcomes to ensure they are evaluating the same effect. Homogeneity tests such as Cochrane’s Q statistic and I^2 are employed to examine between-study variance.
*Random-Effects Meta-Analysis*: This part calculates the mean effect size, incorporating both within-study and between-study variances, to address the heterogeneity among studies.

## Hypotheses and Results

| Hypothesis | Mean True Effect Size | Significance Level | Heterogeneity (I^2) |
|------------|-----------------------|--------------------|---------------------|
"""

for index, row in results_df_direct.iterrows():
    readme_content += f"| {row['Hypothesis']} | {row['Mean True Effect Size']} | {row['Significance Level']} | {row['Heterogeneity (I^2)']} |\n"

readme_content += """

![Image Alt text](Results.png "Results")

## Comments

- The mean true effect sizes indicate the magnitude of the effect autonomy has on various outcomes related to remote work.
- Significance levels suggest the statistical confidence in these effects, with p<0.05 typically considered statistically significant.
- Heterogeneity (I^2) values provide insight into the variability among study results included in the meta-analysis.
"""

# Write README content to a file
readme_file_path = 'README.md'
with open(readme_file_path, 'w') as file:
    file.write(readme_content)