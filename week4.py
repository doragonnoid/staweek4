import streamlit as st
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

def calculate_z_score(value, mean, std_dev):
    return (value - mean) / std_dev

st.title("Normal Distribution Z-score Calculator")

# User Input
st.header("User Input")
mean = st.number_input("Enter mean:", value=10.0)
std_dev = st.number_input("Enter standard deviation:", value=0.5)
lower_limit = st.number_input("Enter lower limit:", value=9.5)
upper_limit = st.number_input("Enter upper limit:", value=10.5)

# Calculating Z-score
st.header("Z-score Calculation")
z_lower = calculate_z_score(lower_limit, mean, std_dev)
z_upper = calculate_z_score(upper_limit, mean, std_dev)
st.write(f'**Z-score for lower limit ({lower_limit} cm):** {z_lower:.2f}')
st.write(f'**Z-score for upper limit ({upper_limit} cm):** {z_upper:.2f}')

st.latex(r"""Z = \frac{x - \mu}{\sigma}""")
st.write(f"For lower limit: Z = ({lower_limit} - {mean}) / {std_dev} = {z_lower:.2f}")
st.write(f"For upper limit: Z = ({upper_limit} - {mean}) / {std_dev} = {z_upper:.2f}")

# Normal distribution graph and Z-score
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
y = stats.norm.pdf(x, mean, std_dev)

fig, ax = plt.subplots()
ax.plot(x, y, label='Normal Distribution')
ax.axvline(lower_limit, color='r', linestyle='dashed', label='Lower Limit')
ax.axvline(upper_limit, color='g', linestyle='dashed', label='Upper Limit')
ax.fill_between(x, y, where=(x >= lower_limit) & (x <= upper_limit), color='gray', alpha=0.5)
ax.legend()
st.pyplot(fig)

# Calculating probability within limits
st.header("Probability Within Range")
probability = stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower)
st.write(f'**Probability within this range:** {probability:.4f}')
st.latex(r"""P(a \leq X \leq b) = P(Z \leq Z_{upper}) - P(Z \leq Z_{lower})""")
st.write(f"P({lower_limit} ≤ X ≤ {upper_limit}) = P(Z ≤ {z_upper:.2f}) - P(Z ≤ {z_lower:.2f})")
st.write(f"= {stats.norm.cdf(z_upper):.4f} - {stats.norm.cdf(z_lower):.4f} = {probability:.4f}")

# Calculating defective proportion
st.header("Defective Bulb Proportion")
prop_defective = 1 - probability
st.write(f'**Proportion of defective bulbs in the manufacturing process:** {prop_defective:.4f}')
st.latex(r"""P_{defective} = 1 - P(a \leq X \leq b)""")
st.write(f"P_defective = 1 - {probability:.4f} = {prop_defective:.4f}")

# Defective proportion graph
fig, ax = plt.subplots()
ax.bar(['Within Range', 'Defective'], [probability, prop_defective], color=['blue', 'red'])
ax.set_ylabel('Proportion')
st.pyplot(fig)

# Quality Assurance Implications
st.header("Quality Assurance Implications")
if prop_defective > 0.10:
    st.write("The proportion of defective bulbs is very high (more than 10%). The company should immediately review the entire manufacturing process, including raw materials, production machinery, and quality control systems.")
elif prop_defective > 0.05:
    st.write("The proportion of defective bulbs is quite high (between 5% - 10%). It is recommended to increase supervision and adjust production parameters to reduce the number of defective products.")
else:
    st.write("The proportion of defective bulbs is still within an acceptable range (less than 5%). However, regular monitoring and continuous improvement are still necessary to maintain quality.")
