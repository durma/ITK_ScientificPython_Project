import streamlit as st
import numpy as np
import scipy.stats as stats

st.title("Probability Distribution Calculator")

dist_type = st.sidebar.selectbox("Select Distribution", ["Binomiális eloszlás", "Poisson eloszlás", "Geometriai eloszlás", "Hipergeometriai eloszlás", "Normális eloszlás"])

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
st.markdown(f"Result: {result}")
