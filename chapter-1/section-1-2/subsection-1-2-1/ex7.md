> Formulate and prove by induction a rule for the sums $1^2$, $2^2-1^2$, $3^2-2^2+1^2$, $4^2-3^2+2^2-1^2$, $5^2-4^2+3^2-2^2+1^2$, etc.

---

Looking at this geometrically:

<p align="center">
  <img src="https://i.imgur.com/zAcU2Q5.png" style="width:50%; max-width:80%; height:auto;" />
</p>

we see that

$$\sum_{k=1}^n (-1)^{n-k}\cdot k^2 = \sum_{k=1}^n k = \frac{n(n+1)}{2}$$

Clearly $1^2=1$ and $2^2-1^2=3=\frac{2\cdot3}{2}$.

Assume $$\sum_{k=1}^n (-1)^{n-k}\cdot k^2 = \frac{n(n+1)}{2}$$ for $n=1,2,\ldots,m$. Then

$$
\begin{align}
  \sum_{k=1}^{m+1} (-1)^{(m+1)-k}\cdot k^2 &= (m+1)^2 - \sum_{k=1}^m (-1)^{m-k}\cdot k^2 \\\\&= (m+1)^2 - \frac{m(m+1)}{2} \\\\&= \frac{2(m+1)^2-m(m+1)}{2} \\\\&=\frac{(m+1)(2(m+1)-m)}{2} \\\\&=\frac{(m+1)(m+2)}{2}.
\end{align}
$$
