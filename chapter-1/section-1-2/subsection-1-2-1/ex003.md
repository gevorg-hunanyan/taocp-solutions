> The following proof by induction seems correct, but for some reason the equation for $n=6$ gives $\frac12+\frac16+\frac{1}{12}+\frac{1}{20}+\frac{1}{30}=\frac56$ on the left-hand side, and $\frac32-\frac16=\frac43$ on the right-hand side. Can you find a mistake? "**Theorem.**
>
> $$ \frac{1}{1\times2}+\frac{1}{2\times3}+\cdots+\frac{1}{(n-1)\times n}=\frac{3}{2}-\frac{1}{n} $$
>
> *Proof.* We use induction on $n$. For $n=1$, clearly $\frac32-\frac1n=\frac{1}{1\times2}$; and, assuming that the theorem is true for $n$,
>
> $$\begin{multline}
  \frac{1}{1\times2}+\cdots+\frac{1}{(n-1)\times n}+\frac{1}{n\times(n+1)}\\\\=\frac32-\frac1n+\frac{1}{n(n+1)}=\frac32-\frac1n+\left(\frac1n-\frac{1}{n+1}\right)=\frac32-\frac{1}{n+1}."
\end{multline}$$

---

For $n=1$ the left-hand side of the equation is zero, as it has $n-1=0$ terms, therefore it is not equal to $\frac1{1\times2}$.
