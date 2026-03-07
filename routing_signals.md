# Routing Signals

This document defines the **diagnostic signals used by MDEA** to determine which execution domain should handle the current system state.

These signals are **domain-agnostic** and are evaluated before expert selection.

Routing signals are provided by the HPF regulatory layer and interpreted by MDEA.

---

# Signal Categories

Routing signals fall into four groups:

| Category               | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| Geometry Health        | Detects when geometric descriptions fail  |
| Saturation Pressure    | Detects update bandwidth overload         |
| Instability Migration  | Detects persistent unresolved instability |
| Resolution Convergence | Detects successful refinement             |

These signals allow MDEA to route execution **without assuming any specific theory**.

---

# Geometry Health

### Definition

$G_{health}(X_t)$ measures the viability of geometric evolution.

Range:

$$
G_{health} \in [0,1]
$$

Interpretation:

| Value | Meaning              |
| ----- | -------------------- |
| 1     | Geometry fully valid |
| ~0.5  | Geometry strained    |
| <0.3  | Geometry failure     |

### Routing Condition

If

$$
G_{health}(X_t) < 0.3
$$

execution is routed to the **substrate domain**

$$
E_{QPRCA}
$$

because geometric descriptions are no longer legal.

---

# Saturation Pressure

### Definition

Saturation pressure measures local update demand relative to available capacity.

$$
\sigma(x) = \frac{\text{update demand}(x)}{\text{update capacity}(x)}
$$

Aggregate saturation:

$$
\sigma_{max} = \max_x \sigma(x)
$$

---

### Interpretation

| Value              | Meaning          |
| ------------------ | ---------------- |
| $\sigma \ll 1$     | uncongested      |
| $\sigma \approx 1$ | near saturation  |
| $\sigma > 1$       | illegal overload |

---

### Routing Condition

If

$$
\sigma_{max}(X_t) > 1
$$

execution is routed to the **saturation domain**

$$
E_{UHET}
$$

unless geometry failure has already occurred.

---

# Instability Migration

Instability migration occurs when refinement **fails to eliminate an instability and instead relocates it**.

Two conditions must hold:

### Persistence

$$
\frac{B_{ref}}{B_{base}} \ge \tau_P
$$

### Relocation

The instability location shifts beyond a defined tolerance.

---

### Interpretation

Migration indicates that the current domain **cannot resolve the instability internally**.

When migration persists, HPF activates routing constraints and MDEA selects a different expert.

---

# Resolution Convergence

Resolution convergence tests whether refinement removes instability.

Let

$$
B = \sum_x b(x)
$$

be the total instability magnitude.

Convergence occurs when

$$
\frac{B_{ref}}{B_{base}} \le \tau_C
$$

where

$$
\tau_C \approx 0.5
$$

---

### Interpretation

If convergence holds:

* the current expert remains valid
* HPF does not engage
* execution continues normally.

---

# Signal Evaluation Order

Signals are evaluated in the following order:

```
Geometry Health
      ↓
Saturation
      ↓
Instability Migration
      ↓
Resolution Convergence
```

Geometry failure always takes priority.

---

# Signal Role in Routing

The routing functional

$$
\Psi(X_t)
$$

uses these signals to determine whether:

1. execution must be forcibly rerouted, or
2. normal validity selection may proceed.

The resulting update law is

$$
X_{t+1} = F_{\Psi(X_t)}(X_t)
$$

---

# Design Principle

Routing signals must satisfy three conditions:

1. **Computable** from the system state
2. **Domain-independent**
3. **Finite-resolution compatible**

This ensures routing decisions are **operational rather than interpretive**.

---

# Relationship to HPF

HPF defines the **meaning and legality constraints** of routing signals.

MDEA interprets those signals to determine **which domain expert executes the next update**.
