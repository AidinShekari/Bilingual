# Mathematical notation

`latex/styles/math-notation.tex` defines reusable operators: `\Prob`, `\E`, `\Var`, `\Cov`, `\Normal`, `\Binomial`, `\BetaDist`, `\GammaDist`, `\argmax`, `\argmin`, `\MLE`, `\MAP`, `\NLL`, `\SSE`, `\RMSE`, `\AIC`, `\BIC`, `\ESS` and `\Rhat`.

The converter preserves the equations and parameter meanings of the supplied lessons. It converts a small set of Unicode mathematical symbols outside math mode to LaTeX commands so they cannot disappear from PDFs. New displayed equations should use `equation` or `align`, have unique `eq:` labels when referenced, and use `\eqref` or `\cref` for links. Never type mathematical expressions as screenshots.
