# Monte Carlo Portfolio Analysis on TradingAgents

Distributed Monte Carlo portfolio simulation built on top of
[TradingAgents](https://github.com/TauricResearch/TradingAgents).

## Build order

Work through these in order. Each step should be tested standalone
before moving to the next — don't add infra (FastAPI, Ray) until the
core simulation logic is proven correct on one laptop.

1. **Environment & baseline** — get TradingAgents running, confirm a
   single `propagate()` call works. (`/`)
2. **Scenario generator** — perturbed price paths / seeds, no
   TradingAgents dependency yet. (`scenario_generator/`)
3. **Sequential integration loop** — wire scenarios into
   `propagate()`, save results to Parquet. (`worker/`)
4. **Concurrency + rate limiting** — asyncio/ThreadPoolExecutor with
   a semaphore. (`worker/`)
5. **Aggregation & stats** — VaR, Sharpe, drawdown from results.
   (`results/`)
6. **FastAPI backend** — `/simulate`, `/results/{id}` endpoints.
   (`api/`)
7. **Dashboard** — Streamlit reading from the results store.
   (`dashboard/`)
8. **Distribute across laptops** — Ray cluster, swap
   ThreadPoolExecutor for `@ray.remote`.

## Setup

```bash
conda create -n monte-carlo-trading python=3.12
conda activate monte-carlo-trading
pip install -r requirements.txt
cp .env.example .env  # add your LLM provider API key
```

## Team workflow

- Branch off `main` per feature (`git checkout -b scenario-generator`).
- Open a PR before merging to `main`.
- Keep `.env` out of git — it's already in `.gitignore`.
