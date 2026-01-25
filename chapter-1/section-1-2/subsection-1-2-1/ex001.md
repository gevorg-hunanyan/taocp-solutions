> Explain how to modify the idea of proof by mathematical induction, in case we want to prove some statement $P(n)$ for all nonnegative integers - that is, for $n=0,1,2,\ldots$ instead of for $n=1,2,3,\ldots$

---

First prove $P(0)$ instead of $P(1)$, then prove that if $P(0),P(1),\ldots,P(n)$, then $P(n+1)$ for all nonnegative integers $n$.

Or let $Q(n)$ be the statement $P(n-1)$ for all positive integers $n$, and proceed with ordinary induction for $Q(n)$.
