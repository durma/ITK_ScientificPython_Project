import streamlit as st
import scipy.stats as stats

st.title("Probability Distribution Calculator")

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
elif dist_type == "Poisson distribution":
    λ = st.sidebar.number_input("λ (Rate Parameter)", value=5.0, step=0.1)
    k = st.sidebar.number_input("k (Number of Events)", value=5, step=1)
    result = stats.poisson.pmf(k, λ)
elif dist_type == "Geometric distribution":
    p = st.sidebar.number_input("p (Probability of Success)", value=0.5, min_value=0.0, max_value=1.0, step=0.01)
    k = st.sidebar.number_input("k (Number of Trials until First Success)", value=5, step=1)
    result = stats.geom.pmf(k, p)
elif dist_type == "Hypergeometric distribution":
    M = st.sidebar.number_input("M (Total Population)", value=20, step=1)
    n = st.sidebar.number_input("n (Number of Successes in Population)", value=7, step=1)
    N = st.sidebar.number_input("N (Number of Draws)", value=12, step=1)
    k = st.sidebar.number_input("k (Number of Successes in Draws)", value=5, step=1)
    result = stats.hypergeom.pmf(k, M, n, N)
elif dist_type == "Standard distribution":
    mu = st.sidebar.number_input("μ (Mean)", value=0.0, step=0.1)
    sigma = st.sidebar.number_input("σ (Standard Deviation)", value=1.0, step=0.1)
    x = st.sidebar.number_input("x (Value)", value=0.0, step=0.1)
    result = stats.norm.pdf(x, mu, sigma)

st.markdown(f"## {dist_type}")
st.markdown(descriptions[dist_type]["description"])
st.markdown(descriptions[dist_type]["equation"])
st.markdown(f"### Result: {result}")