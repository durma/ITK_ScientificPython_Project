import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

st.title("Probability Distribution Calculator")

# Description dictionary
descriptions = {
    "Binomial distribution": {
        "description": "The binomial distribution models the number of successes in a fixed number of trials, with each trial having a constant probability of success.",
        "equation": "$P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}$"
    },
    "Poisson distribution": {
        "description": "The Poisson distribution models the number of times an event occurs in a fixed interval of time or space.",
        "equation": "$P(X = k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}$"
    },
    "Geometric distribution": {
        "description": "The geometric distribution models the number of trials until the first success in independent and identically distributed Bernoulli trials.",
        "equation": "$P(X = k) = (1-p)^{k-1} p$"
    },
    "Hypergeometric distribution": {
        "description": "The hypergeometric distribution describes the probability of k successes in n draws, without replacement, from a finite population of size N that contains exactly M successes.",
        "equation": "$P(X = k) = \\frac{\\binom{M}{k} \\binom{N-M}{n-k}}{\\binom{N}{n}}$"
    },
    "Standard distribution": {
        "description": "The normal distribution is a continuous probability distribution characterized by its bell-shaped curve, symmetrical around the mean.",
        "equation": "$f(x) = \\frac{1}{\\sigma \\sqrt{2\\pi}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
    }
}

dist_type = st.sidebar.selectbox("Select Distribution", list(descriptions.keys()))
st.sidebar.markdown("### Input Parameters")
result = "Unknown"

if dist_type == "Binomial distribution":
    n = st.sidebar.number_input("n (Number of Trials)", value=10, step=1)
    p = st.sidebar.number_input("p (Probability of Success)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    k = st.sidebar.number_input("k (Number of Successes)", value=5, step=1)
    result = stats.binom.pmf(k, n, p)
    x = np.arange(0, n+1)
    y = stats.binom.pmf(x, n, p)
elif dist_type == "Poisson distribution":
    λ = st.sidebar.number_input("λ (Rate Parameter)", value=5.0, step=0.1)
    k = st.sidebar.number_input("k (Number of Events)", value=5, step=1)
    result = stats.poisson.pmf(k, λ)
    x = np.arange(0, 20)
    y = stats.poisson.pmf(x, λ)
elif dist_type == "Geometric distribution":
    p = st.sidebar.number_input("p (Probability of Success)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    k = st.sidebar.number_input("k (Number of Trials until First Success)", value=5, step=1)
    result = stats.geom.pmf(k, p)
    x = np.arange(1, 20)
    y = stats.geom.pmf(x, p)
elif dist_type == "Hypergeometric distribution":
    M = st.sidebar.number_input("M (Total Population)", value=20, step=1)
    n = st.sidebar.number_input("n (Number of Successes in Population)", value=7, step=1)
    N = st.sidebar.number_input("N (Number of Draws)", value=12, step=1)
    k = st.sidebar.number_input("k (Number of Successes in Draws)", value=5, step=1)
    result = stats.hypergeom.pmf(k, M, n, N)
    x = np.arange(max(0, n + N - M), min(n, N) + 1)
    y = stats.hypergeom.pmf(x, M, n, N)
elif dist_type == "Standard distribution":
    mu = st.sidebar.number_input("μ (Mean)", value=0.0, step=0.1)
    sigma = st.sidebar.number_input("σ (Standard Deviation)", value=1.0, step=0.1)
    x = st.sidebar.number_input("x (Value)", value=0.0, step=0.1)
    result = stats.norm.pdf(x, mu, sigma)
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)

st.markdown(f"## {dist_type}")
st.markdown(descriptions[dist_type]["description"])
st.markdown(descriptions[dist_type]["equation"])
st.markdown(f"### Result: {result}")

# Plotting the distribution
fig, ax = plt.subplots()
ax.plot(x, y, 'bo', ms=8, label='pmf' if 'discrete' in dist_type.lower() else 'pdf')
ax.vlines(x, 0, y, colors='b', lw=5, alpha=0.5)
st.pyplot(fig)