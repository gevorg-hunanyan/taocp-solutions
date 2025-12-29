> The text showed how to interchange the values of variables $m$ and $n$, using the replacement notation, by setting $t\leftarrow m$, $m\leftarrow n$, $n\leftarrow t$. Show how the values of four variables $(a,b,c,d)$ can be rearranged to $(b,c,d,a)$ by a sequence of replacements. In other words, the new value of $a$ is to be the original value of $b$, etc. Try to use the minimum number of replacements.

Note that it is not possible to do so by four replacements. Indeed, assuming the first replacement is $x\leftarrow y$, where $x,y\in\\{a,b,c,d\\}$, the value of $x$ will be lost and we will not be able to retrieve it anymore.

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
