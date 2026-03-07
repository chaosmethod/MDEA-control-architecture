# MDEA — Multi-Domain Execution Architecture

**MDEA** is a routing architecture that governs **which physical domain expert executes the next evolution step** of a system state.

It operates as a **mixture-of-experts scheduler** driven by computable legality and regime signals.

MDEA does **not define physics itself**.
Instead, it ensures that **each physical theory executes only within its valid regime**.

---

# What MDEA Does

At each step, MDEA:

1. Reads diagnostic signals describing the current state.
2. Detects illegal execution conditions.
3. Selects the most valid domain expert.
4. Executes that expert's reversible update.

The system evolution is therefore:

$$
X_{t+1} = F_{\Psi(X_t)}(X_t)
$$

where

* $X_t$ is the current state
* $F_E$ is the update map of expert $E$
* $\Psi(X_t)$ selects the active expert.

---

# Why Routing Is Necessary

Existing physical theories are **regime-limited**:

| Theory                | Limitation                 |
| --------------------- | -------------------------- |
| GR                    | singularities              |
| QFT                   | fixed background spacetime |
| semiclassical gravity | unstable backreaction      |
| EFT                   | finite cutoff              |

These limits are usually handled informally.

MDEA converts them into **explicit routing rules**.

When a theory's assumptions fail, execution **must transition** to another domain expert.

---

# Routing Functional

Under normal conditions MDEA selects the highest-valid expert:

$$
\Psi(X_t) =
\mathrm{arg,max}^{\mathrm{geom}}_{E \in \mathcal{E} : L(E,X_t)=1}
V(E,X_t)
$$

where

* $L(E,X_t)$ is a legality test
* $V(E,X_t)$ measures regime validity.

Geometry is favored on ties.

---

# Hard Routing Gates

Certain conditions override normal routing.

## Geometry Failure

If

$$
G_{\text{health}}(X_t) < G_{\text{crit}}
$$

execution routes to the **substrate domain**.

---

## Saturation

If

$$
\sigma_{\max}(X_t) > 1
$$

execution routes to the **saturation domain**.

---

# Routing Signals

MDEA operates on **domain-agnostic signals**:

| Signal       | Meaning                |
| ------------ | ---------------------- |
| $G_{health}$ | geometric validity     |
| $\sigma$     | saturation pressure    |
| $B$          | instability magnitude  |
| convergence  | refinement behavior    |
| migration    | instability relocation |

These signals allow routing without assuming any specific physical theory.

---

# Execution Flow

```
State X_t
   │
   ▼
Compute routing signals
   │
   ▼
Check hard routing gates
   │
   ▼
Select highest-valid legal expert
   │
   ▼
Execute reversible update
   │
   ▼
Next state X_{t+1}
```

---

# Design Principles

MDEA enforces three rules:

### 1. No Illegal Execution

A theory may not run outside its validity envelope.

### 2. Explicit Failure Handling

Failure modes trigger routing instead of patching.

### 3. Reversible Evolution

Every expert update must preserve information.

---

# Scope

MDEA does **not**:

* replace GR or QFT
* define fundamental physics
* impose new equations of motion

It provides the **execution architecture** for multi-regime physics.

---

# Status

The architecture is presented as an **inspectable theoretical scheduler** intended to formalize regime transitions in physics.

# Framework Location

MDEA is one component of the broader **Holographic Projection Framework ecosystem**.

The full framework stack is maintained in the primary repository:

**Framework repository:**
[https://github.com/chaosmethod/Holographic-Projection-Framework](https://github.com/chaosmethod/Holographic-Projection-Framework)

That repository contains the foundational components that MDEA routes between.

---

## Framework Layer Map

| Layer     | Role                                              | Location                                 |
| --------- | ------------------------------------------------- | ---------------------------------------- |
| **HPF**   | Legality constraints and regime-detection signals | `Holographic-Projection-Framework`       |
| **MDEA**  | Execution routing and control architecture        | *this repository*                        |
| **UHET**  | Saturation-regime phenomenology                   | `Holographic-Projection-Framework/UHET`  |
| **QPRCA** | Reversible computational substrate implementation | `Holographic-Projection-Framework/QPRCA` |

---

## Relationship Between Repositories

This repository focuses exclusively on the **control architecture**:

* how execution is routed
* how routing signals are interpreted
* how domain experts are selected

The **physical theories and substrate implementations** live in the main framework repository.

MDEA acts as the **execution scheduler** that determines which of those domains performs the next system update.

---

## Execution Context

The resulting execution model is:

```
HPF signals
     ↓
MDEA routing architecture
     ↓
Domain experts (GR / QFT / UHET / QPRCA)
     ↓
State evolution
```

Formally,

$[
X_{t+1} = F_{\Psi(X_t)}(X_t)
]$
