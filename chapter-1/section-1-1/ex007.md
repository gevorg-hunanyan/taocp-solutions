> Suppose that $m$ is known and $n$ is allowed to range over all positive integers; let $U_m$ be the average number of times that step $E1$ is executed in Algorithm $E$. Show that $U_m$ is well defined. Is $U_m$ in any way related to $T_m$?

---

Solution taken from TAOCP:

> In all but a finite number of cases, $n>m$. And when $n>m$, the first iteration of Algorithm $E$ merely exchanges these numbers; so $U_m=T_m+1$.
