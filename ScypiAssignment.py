import streamlit as st
import numpy as np
from scipy.stats import binom, poisson, geom, hypergeom, norm


def check_params(params):
    missing = [k for k, v in params.items() if v is None]
    return missing


st.title("Distribution Calculator")

col1, col2 = st.columns(2)

with col1:
    st.header("Inputs")
    n = st.number_input("n", value=None)
    p = st.number_input("p", value=None)
    k = st.number_input("k", value=None)
    K = st.number_input("K", value=None)
    l = st.number_input("l (lambda)", value=None)
    N = st.number_input("N", value=None)
    x = st.number_input("x", value=None)
    m = st.number_input("m (mean)", value=None)

with col2:
    st.header("Results")

    binom_params = {"Trials (n)": n, "Probability (p)": p}
    missing = check_params(binom_params)
    if missing:
        st.write(f"Binomial Distribution - Missing parameters: {', '.join(missing)}")
    else:
        sample = binom.rvs(n=int(n), p=p, size=1)
        st.write(f"Binomial Distribution: {sample}")

    poisson_params = {"Lambda (l)": l}
    missing = check_params(poisson_params)
    if missing:
        st.write(f"Poisson Distribution - Missing parameters: {', '.join(missing)}")
    else:
        sample = poisson.rvs(mu=l, size=1)
        st.write(f"Poisson Distribution: {sample}")

    geom_params = {"Probability (p)": p}
    missing = check_params(geom_params)
    if missing:
        st.write(f"Geometric Distribution - Missing parameters: {', '.join(missing)}")
    else:
        sample = geom.rvs(p=p, size=1)
        st.write(f"Geometric Distribution: {sample}")

    hypergeom_params = {"Total Population (N)": N, "Total Successes in Population (K)": K, "Sample Size (n)": n}
    missing = check_params(hypergeom_params)
    if missing:
        st.write(f"Hypergeometric Distribution - Missing parameters: {', '.join(missing)}")
    else:
        sample = hypergeom.rvs(M=N, n=K, N=n, size=1)
        st.write(f"Hypergeometric Distribution: {sample}")

    normal_params = {"Mean (m)": m, "Standard Deviation (x)": x}
    missing = check_params(normal_params)
    if missing:
        st.write(f"Normal Distribution - Missing parameters: {', '.join(missing)}")
    else:
        sample = norm.rvs(loc=m, scale=x, size=1)
        st.write(f"Normal Distribution: {sample}")
