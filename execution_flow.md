# MDEA Execution Flow

This document describes the **runtime execution cycle** of the Multi-Domain Execution Architecture (MDEA).

MDEA acts as a **routing scheduler** that selects which domain expert evolves the system state at each update step.

The architecture enforces legality constraints and prevents theories from executing outside their valid regimes.

---

# Core Update Cycle

At each scheduler step the following sequence is executed.

```
Current State
    X_t
     │
     ▼
Compute Routing Signals
(G_health, σ, instability metrics)
     │
     ▼
Evaluate Hard Gates
(geometry failure / saturation)
     │
     ▼
If gate triggered → override expert
     │
     ▼
Otherwise compute expert validity
     │
     ▼
Select best legal expert
Ψ(X_t)
     │
     ▼
Execute reversible update
F_E
     │
     ▼
Next State
X_{t+1}
```

---

# Formal Update Rule

The system evolves according to

$$
X_{t+1} = F_{\Psi(X_t)}(X_t)
$$

where

* $X_t$ is the current state
* $\Psi(X_t)$ selects the active expert
* $F_E$ is the reversible update map for expert $E$.

---

# Execution Stages

## 1. Signal Evaluation

Diagnostic signals are computed from the current state:

* geometry health $G_{health}$
* saturation pressure $\sigma$
* instability metrics
* resolution convergence

These signals describe the **execution legality of each domain**.

---

## 2. Hard Gate Evaluation

Two conditions override normal routing.

### Geometry Failure

If

$$
G_{health}(X_t) < 0.3
$$

execution routes to

$$
E_{QPRCA}
$$

because geometric evolution is no longer valid.

---

### Saturation

If

$$
\sigma_{max}(X_t) > 1
$$

execution routes to

$$
E_{UHET}
$$

to handle saturation-regulated dynamics.

---

# 3. Validity Selection

If no hard gate fires, MDEA selects the highest-valid legal expert:


$\Psi(X_t)$
=========
$$
\mathrm{arg,max}^{geom}*{E \in \mathcal{E} : L*{HPF}(E,X_t)=1}
V_{HPF}(E,X_t)
$$

where

* $L_{HPF}$ enforces legality
* $V_{HPF}$ measures regime validity.

---

# 4. Expert Execution

The selected expert performs the reversible update

$$
X_{t+1} = F_E(X_t)
$$

This produces the next system state.

---

# Execution Guarantees

The MDEA architecture guarantees:

### Determinism

The routing functional returns a single expert for any state.

### Reversibility

All expert update maps are reversible.

### Finite Execution

Illegal execution domains are blocked by HPF legality gates.

---

# Conceptual Interpretation

MDEA converts informal **regime switching in physics** into an explicit execution architecture.

Instead of extending theories beyond their validity limits, MDEA:

* detects failure conditions
* routes execution to a valid domain
* continues evolution without singularities.

---

# Execution Loop

The entire system can be summarized as:

```
State → Signals → Router → Expert → State
```

or formally

$$
X_{t+1} = F_{\Psi(X_t)}(X_t)
$$

---

# File Relationships

| File               | Purpose                      |
| ------------------ | ---------------------------- |
| README.md          | Overview of MDEA             |
| routing_law.md     | Formal routing equation      |
| routing_signals.md | Diagnostic inputs to routing |
| execution_flow.md  | Runtime execution cycle      |
