> Change Algorithm $E$ (for the sake of efficiency) so that all trivial replacement operations such as $"m\leftarrow n"$ are avoided. Write this new algorithm in the style of Algorithm $E$, and call it Algorithm $F$.

---

The following algorithm avoids replacements.

1. Divide $m$ by $n$ and let $m$ be the remainder.
2. If $m=0$, the algorithm terminates; $n$ is the answer.
3. Divide $n$ by $m$ and let $n$ be the remainder.
4. If $n=0$, the algorithm terminates; $m$ is the answer.
5. Go to step $1$.
