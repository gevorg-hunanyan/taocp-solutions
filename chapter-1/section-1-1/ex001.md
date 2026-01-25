> The text showed how to interchange the values of variables $m$ and $n$, using the replacement notation, by setting $t\leftarrow m$, $m\leftarrow n$, $n\leftarrow t$. Show how the values of four variables $(a,b,c,d)$ can be rearranged to $(b,c,d,a)$ by a sequence of replacements. In other words, the new value of $a$ is to be the original value of $b$, etc. Try to use the minimum number of replacements.

---

Note that it is not possible to do so by four replacements. Indeed, assuming we have solved the problem with four replacements implies that each of the replacements is into one of the variables $a,b,c,d$. In other words, we cannot use another variable besides $a,b,c,d$, because otherwise the other three replacements would not suffice to rewrite all of $a,b,c,d$. If the first replacement is $x\leftarrow y$, where $x,y\in\\{a,b,c,d\\}$, then the value of $x$ will be lost and we will not be able to retrieve it anymore, reaching a contradiction. Therefore we need at least five replacements.

Doing it in five replacements is possible with the following sequence.

$$
\begin{gather}
  t\leftarrow a\\
  a\leftarrow b\\
  b\leftarrow c\\
  c\leftarrow d\\
  d\leftarrow t
\end{gather}
$$
