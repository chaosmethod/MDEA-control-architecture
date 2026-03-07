# MDEA–HPF Unified Update Law

**MDEA–HPF** is a concrete architectural realization of the **Holographic Projection Framework (HPF)**.

Its evolution law consists of a **regulated expert-selection rule** followed by a **reversible substrate update**.

---

# Operator Selection

The routing functional $\Psi(X_t)$ selects the active evolution operator.

Routing precedence is enforced as follows.

### Geometry Failure

If

$$
G_{health}(X_t) < 0.3
$$

then

$$
\Psi(X_t) = E_{QPRCA}
$$

Geometry is no longer a legal execution domain, so routing transitions to the substrate domain.

---

### Saturation

If

$$
\sigma_{max}(X_t) > 1
$$

then

$$
\Psi(X_t) = E_{UHET}
$$

This indicates bandwidth saturation or compactness collapse.

---

### Normal Routing

Otherwise,


$\Psi(X_t)$
=========
$$
\mathrm{arg,max}^{geom}*{E \in \mathcal{E} : L*{HPF}(E,X_t)=1}
V_{HPF}(E,X_t)
$$

This selects the **highest-valid legal expert**, with **geometry favored on ties**.

---

# State Update

The universe evolves according to

$$
X_{t+1} = F_{\Psi(X_t)}(X_t)
$$

where the selected expert performs the reversible update.

---

# Definitions

## $X_t$

Full universe state at discrete update step $t$.

---

## $\mathcal{E}$

Set of admissible evolution operators (**experts**) including:

* $E_{GR}$ — geometric regime
* $E_{QFT}$ — quantum field regime
* $E_{UHET}$ — ultra-high-energy regime
* $E_{QPRCA}$ — substrate-resolution regime

and related effective limits.

---

## $\Psi(X_t)$

HPF regulator routing functional selecting the active operator from $\mathcal{E}$.

Selection is determined by:

* failure-mode precedence
* legality constraints
* regime validity

---

## $F_E$

Reversible substrate update map associated with operator $E$.

Applying $F_E$ to the current state produces the next universe state.

---

## $L_{HPF}(E,X_t) \in {0,1}$

HPF **legality functional**.

This enforces hard admissibility constraints including:

* reversibility
* finite bandwidth
* entropy saturation compliance
* $\zeta$-stability

Operators with

$$
L_{HPF}(E,X_t) = 0
$$

are illegal and excluded from routing.

---

## $V_{HPF}(E,X_t)$

HPF **validity functional** measuring how well operator $E$ matches the local physical regime represented by $X_t$.

---

## $\mathrm{arg,max}^{geom}$

Validity maximization over legal operators with **ties resolved in favor of the geometric operator**.

---

## $G_{health}(X_t)$

Geometry-health functional measuring integrity of the geometric sector.

If

$$
G_{health}(X_t) < 0.3
$$

execution reroutes to $E_{QPRCA}$.

---

## $\sigma_{max}(X_t)$

Maximum local **saturation functional** measuring bandwidth or compactness saturation.

If

$$
\sigma_{max}(X_t) > 1
$$

execution reroutes to $E_{UHET}$ unless geometry failure has already taken precedence.

---

# Failure-Mode Precedence

Failure modes are **first-class execution signals**.

They may **not** be:

* ignored
* interpreted away
* patched by extending authority

Routing precedence:

```
Geometry Failure
      ↓
Saturation
      ↓
Ordinary legality / validity routing
```

If multiple failure conditions occur simultaneously, **geometry failure takes priority**.

---

# Operational Interpretation

The unified update law executes the following sequence:

1. Detect hard failure conditions.
2. Apply override routing if required.
3. Otherwise select the highest-valid legal expert.
4. Apply the reversible update map of the selected expert.

This yields a **single regulated evolution law on a reversible substrate** rather than a fixed single-regime equation.

---

# Notation

## Symbol Index

| Symbol                    | Meaning                                              |
| ------------------------- | ---------------------------------------------------- |
| $X_t$                     | Full universe state at discrete update step $t$.     |
| $X_{t+1}$                 | Universe state after one regulated substrate update. |
| $t$                       | Discrete update index.                               |
| $\Psi(X_t)$               | Routing functional selecting the active expert.      |
| $\mathcal{E}$             | Set of admissible evolution operators.               |
| $E$                       | Generic evolution operator.                          |
| $E_{GR}$                  | Geometric regime operator.                           |
| $E_{QFT}$                 | Quantum field regime operator.                       |
| $E_{UHET}$                | Ultra-high-energy override operator.                 |
| $E_{QPRCA}$               | Substrate-resolution override operator.              |
| $F_E$                     | Reversible update map associated with operator $E$.  |
| $L_{HPF}(E,X_t)$          | Legality functional.                                 |
| $V_{HPF}(E,X_t)$          | Validity functional.                                 |
| $\mathrm{arg,max}^{geom}$ | Validity maximization with geometry tie-break.       |
| $G_{health}(X_t)$         | Geometry-health functional.                          |
| $\sigma_{max}(X_t)$       | Saturation functional.                               |
| $\zeta$                   | HPF stability parameter.                             |

---

# Core Evolution Law

$$
X_{t+1} = F_{\Psi(X_t)}(X_t)
$$

---

# Conceptual Layers

| Layer     | Role                                           |
| --------- | ---------------------------------------------- |
| Substrate | State space represented by $X_t$.              |
| Regulator | Routing functional $\Psi(X_t)$.                |
| Experts   | Evolution operators in $\mathcal{E}$.          |
| Update    | Reversible map $F_E$ producing the next state. |
