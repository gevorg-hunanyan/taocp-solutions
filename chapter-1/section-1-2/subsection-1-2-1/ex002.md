> There must be something wrong with the following proof. What is it? "**Theorem.** Let $a$ be any positive number. For all positive integers $n$ we have $a^{n-1}=1$. *Proof.* If $n=1$, $a^{n-1}=a^{1-1}=a^0=1$. And by induction, assuming that the theorem is true for $1,2,\ldots,n$, we have
>
> $$ a^{(n+1)-1}=a^n=\frac{a^{n-1}\times a^{n-1}}{a^{(n-1)-1}}=\frac{1\times1}{1}=1; $$
>
> so the theorem is true for $n+1$ as well.

---

Inductive step is not valid for $n=1$, as we are assuming $a^{-1}=1$, which is not true.
