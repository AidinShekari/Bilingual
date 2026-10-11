# Glossary · واژه‌نامه

Terms are listed alphabetically. The number in brackets is the week where the term is introduced or treated most fully. Notation follows the course-wide table in Week 1.

<div dir="rtl">

اصطلاحات به ترتیب الفبای انگلیسی آمده‌اند تا با متن‌های انگلیسی و کتاب‌ها راحت تطبیق داده شوند. عدد داخل کروشه هفته‌ای است که اصطلاح در آن معرفی شده یا کامل‌تر توضیح داده شده است. نمادگذاری مطابق جدول نمادهای هفته‌ی 1 است.

</div>

| Term | Definition |
|---|---|
| **Acceptance rate** [11] | Proportion of Metropolis proposals that are accepted. Very high: steps too small; very low: steps too large. A rough target is 0.2–0.5. |
| **Aggregation artifact** [5] | A pattern in averaged data that no individual shows, e.g., a power-law curve from averaging exponential learners. |
| **AIC / AICc** [7] | Akaike information criterion, $2\,\mathrm{NLL} + 2k$; estimates out-of-sample predictive accuracy. AICc adds a small-sample correction. |
| **Akaike weight** [7] | $w_i \propto \exp(-\Delta_i/2)$: relative support for model $i$ as the best predictor among the candidates. |
| **Attention weight** ($w_m$) [14] | GCM parameter: the share of attention given to stimulus dimension $m$ (weights sum to 1). |
| **Bayes factor** ($\mathrm{BF}_{12}$) [10] | Ratio of marginal likelihoods $p(\mathbf{y}\mid\mathcal{M}_1)/p(\mathbf{y}\mid\mathcal{M}_2)$: how much the data change the odds between two models. |
| **Bayesian data analysis** [9] | Using Bayes' rule to infer parameters and models from data; a method of the scientist, applicable to any model. |
| **Bayesian model of cognition** [15] | A hypothesis that the mind performs (approximately) Bayesian inference; a computational-level theory. |
| **Beta-binomial model** [9] | A binomial likelihood with a Beta prior; the posterior is again a Beta distribution (conjugacy). |
| **BIC** [7] | Bayesian information criterion, $2\,\mathrm{NLL} + k\ln N$; approximates $-2\ln p(\mathbf{y}\mid\mathcal{M})$ and favors simpler models than AIC. |
| **Bias–variance trade-off** [6] | Expected prediction error = noise + bias² + variance. Flexible models lower bias but raise variance. |
| **Bootstrap (parametric)** [5] | Simulate many datasets from the fitted model, refit each one, and use the spread of the estimates as their uncertainty. |
| **Boundary separation** ($a$) [1, 14] | Random walk / DDM parameter: the distance between the response boundaries. Represents caution. |
| **Burn-in (warm-up)** [11] | Initial MCMC iterations discarded because they still reflect the starting values. |
| **Centered / non-centered parameterization** [13] | Two equivalent ways to write a hierarchical model; the non-centered form ($d_j = \mu + \sigma z_j$) avoids funnel geometry and divergences. |
| **Complete / no / partial pooling** [5, 13] | One parameter set for everyone / independent parameters per person / individual parameters drawn from an estimated group distribution. |
| **Confusion matrix (model recovery)** [7] | $P(\text{selected model} \mid \text{generating model})$, estimated by simulation. |
| **Conjugate prior** [9, 12] | A prior that yields a posterior in the same family (e.g., Beta for binomial data); enables Gibbs sampling. |
| **Credible interval / HDI** [9] | An interval containing a stated posterior probability (e.g., 95%); the HDI is the narrowest such interval. |
| **Criterion** ($c$) [2] | SDT response-bias parameter: the criterion location relative to the midpoint between the noise and signal distributions. Positive values are conservative. |
| **Cross-validation (K-fold, LOO)** [6] | Fit on part of the data and score predictions on the held-out part, rotating through $K$ folds; LOO holds out one observation at a time. |
| **$d'$ (sensitivity)** [2] | SDT parameter: the distance between the signal and noise distributions in SD units. |
| **Delta rule / Rescorla–Wagner rule** [15] | Error-driven update $Q \leftarrow Q + \alpha(r - Q)$. |
| **Deterministic core** [2] | The part of a model that gives its average prediction, $f(x;\boldsymbol\theta)$. |
| **Deviance** ($G^2$) [4] | $2(\ell_{\text{sat}} - \hat\ell)$: misfit relative to the saturated model; approximately $\chi^2$ with df = cells − $k$. |
| **Divergent transition** [13] | A NUTS trajectory whose numerical integration broke down; it signals unreliable exploration of part of the posterior. |
| **Drift rate** ($v$) [1, 14] | Random walk / DDM parameter: the average rate of evidence accumulation. Represents evidence quality. |
| **Drift-diffusion model (DDM)** [14] | Continuous evidence accumulation with noise between two boundaries; predicts choices and RT distributions. |
| **Effective sample size (ESS)** [12] | The number of independent draws that would give the same precision as the autocorrelated MCMC draws. |
| **Error surface** [3] | The discrepancy (SSE or NLL) as a function of the parameters; its shape reveals minima, valleys (trade-offs) and plateaus. |
| **Evidence / marginal likelihood** [9, 10] | $p(\mathbf{y}\mid\mathcal{M}) = \int p(\mathbf{y}\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta$: how well the model predicted the data before fitting. |
| **EZ-diffusion** [14] | Closed-form estimates of drift, boundary and non-decision time from accuracy and the mean and variance of correct RTs. |
| **Flexibility (model complexity)** [6] | The range of data patterns a model can produce; it depends on the number of parameters *and* the functional form. |
| **Forward / inverse problem** [1] | Simulation (parameters → data) vs. estimation (data → parameters). |
| **Full conditional** [12] | The distribution of one parameter given all others and the data; Gibbs sampling draws from it. |
| **GCM (Generalized Context Model)** [14] | Exemplar model of categorization: classification by summed similarity to stored exemplars. |
| **Generalization criterion** [6] | Evaluating models by predicting new conditions (extrapolation) rather than new trials. |
| **Gibbs sampling** [12] | MCMC that updates each parameter by drawing from its full conditional; every draw is accepted. |
| **Grid approximation** [9] | Computing the posterior on a grid of parameter values; feasible for 1–2 parameters. |
| **Hamiltonian Monte Carlo (HMC) / NUTS** [13] | Gradient-based MCMC that simulates physical dynamics to make distant, high-acceptance proposals; NUTS tunes the trajectory length automatically. |
| **Hessian / observed Fisher information** [5] | Matrix of second derivatives of the NLL at the MLE; its inverse approximates the covariance of the estimates. |
| **Hierarchical (multilevel) model** [13] | A model with individual-level parameters drawn from group-level distributions. |
| **Identifiability (structural / practical)** [7] | Whether parameters can be uniquely determined, in principle (structural) or from the available data (practical). |
| **Ideal observer** [15] | A model of optimal inference given the available information, e.g., reliability-weighted cue combination. |
| **Inverse temperature** ($\beta$) [15] | Softmax parameter: the sensitivity of choices to value differences (exploration vs. exploitation). |
| **Inversion matrix (model recovery)** [7] | $P(\text{generating model} \mid \text{selected model})$: how much to trust a model-selection outcome. |
| **Learning rate** ($\alpha$) [15] | How strongly prediction errors update values. |
| **Likelihood** ($L$), **log-likelihood** ($\ell$), **NLL** [4] | $p(\mathbf{y}\mid\boldsymbol\theta)$ viewed as a function of $\boldsymbol\theta$; its log; and the negative log, which optimizers minimize. |
| **Likelihood-ratio test (LRT)** [7] | For nested models, $2\Delta\ell \sim \chi^2_{\Delta k}$ under the simpler model. |
| **Linking assumption** [2] | How model quantities map onto observable behavior. |
| **Local minimum** [3] | A point lower than its surroundings but not the global minimum; found by single-start optimization. Use multi-start. |
| **MAP** [9] | Maximum a posteriori estimate (posterior mode); equals the MLE under a flat prior. |
| **Markov chain Monte Carlo (MCMC)** [11] | Sampling from a posterior by simulating a Markov chain whose stationary distribution is the posterior. |
| **Maximum likelihood estimate (MLE)** [4] | The parameter values that maximize the likelihood. |
| **MCSE** [12] | Monte Carlo standard error, posterior SD/$\sqrt{\mathrm{ESS}}$: the simulation error of a posterior mean. |
| **Metropolis / Metropolis–Hastings** [11] | MCMC that proposes a move and accepts it with probability $\min(1, \text{ratio})$; Hastings adds a correction for asymmetric proposals. |
| **Model mimicry** [7] | One model producing data that look as if generated by another. |
| **Model recovery** [7] | Simulating from each candidate model and checking whether the comparison method selects the generating model. |
| **Monte Carlo integration** [11] | Approximating an expectation by the average over random draws; error ∝ $1/\sqrt{S}$. |
| **Multi-start** [3] | Running an optimizer from many starting values and keeping the best result. |
| **Nelder–Mead simplex** [3] | Derivative-free optimizer that moves a simplex by reflection, expansion, contraction and shrinkage. |
| **Nested models** [7] | One model is a special case of the other (obtained by fixing parameters). |
| **Noise model** [2] | The distribution of observations around the deterministic prediction (e.g., binomial, Gaussian). |
| **Non-decision time** ($t_0$, $T_{er}$) [1, 14] | The part of RT not spent accumulating evidence (encoding and motor execution). |
| **Overfitting** [6] | Fitting the noise of a sample, which improves fit but worsens prediction of new data. |
| **Parameter recovery** [7] | Simulating data from known parameters at the actual design and checking that fitting returns them. |
| **Parameter trade-off** [3, 5] | Changes in one parameter can be compensated by another, which shows up as a tilted valley in the error surface and correlated estimates. |
| **Posterior** [9] | $p(\boldsymbol\theta\mid\mathbf{y}) \propto p(\mathbf{y}\mid\boldsymbol\theta)p(\boldsymbol\theta)$. |
| **Posterior predictive check (PPC)** [10] | Comparing data simulated from the fitted model with the observed data, to check adequacy. |
| **Power / exponential forgetting** [2] | $A(1+t)^{-d}$ (decreasing relative loss rate) vs. $Ae^{-\lambda t}$ (constant relative loss rate). |
| **Prior / prior predictive check** [9] | The distribution of parameters before the data / simulating data from the prior to check that the prior is sensible. |
| **Profile likelihood** [5] | The NLL minimized over the other parameters for each value of the parameter of interest; gives likelihood-ratio intervals. |
| **Prototype model** [14] | Categorization by similarity to a single summary representation per category. |
| **R-hat** ($\hat R$) [12] | Ratio comparing between-chain and within-chain variance; ≈ 1 (< 1.01) when chains agree. |
| **Random walk model** [1] | Discrete-step evidence accumulation to a boundary; the precursor of the DDM. |
| **Relative loss rate (hazard)** [2] | $-f'(t)/f(t)$: the proportional rate of forgetting at time $t$. |
| **Reparameterization** [3, 13] | Optimizing or sampling on a transformed scale (e.g., $\lambda = e^{\eta}$) to enforce constraints or improve geometry. |
| **RMSD** [3] | Root mean squared deviation, $\sqrt{\mathrm{SSE}/N}$, in data units. |
| **ROC / zROC** [2] | Hit rate vs. false-alarm rate as the criterion varies / the same on $z$ (probit) axes. |
| **Saturated model** [4] | A model with one free parameter per data cell, which reproduces the data exactly. |
| **Savage–Dickey density ratio** [10] | For nested models, $\mathrm{BF}_{01}$ = posterior density / prior density at the null value. |
| **Shrinkage** [13] | The pull of individual estimates toward the group mean in hierarchical models, stronger for noisier data. |
| **Signal detection theory (SDT)** [2] | A model of detection decisions with noisy evidence and a criterion; separates sensitivity from bias. |
| **Softmax** [15] | $P(o) \propto \exp(\beta Q(o))$: turns values into choice probabilities. |
| **SSE / MSE** [3] | Sum / mean of squared errors between data and predictions. |
| **Standard error** [5] | The SD of an estimator's sampling distribution. |
| **Wald interval** [5] | $\hat\theta \pm 1.96\,\mathrm{SE}$, with the SE from the Hessian; assumes approximate normality. |
| **Weighted least squares** [3] | Squared errors weighted by the inverse of their variance. |

<div dir="rtl">

| اصطلاح (English) | معادل فارسی | تعریف |
|---|---|---|
| **Acceptance rate** [11] | نرخ پذیرش | نسبت پیشنهادهای (proposals) الگوریتم Metropolis که پذیرفته می‌شوند. خیلی بالا یعنی گام‌ها خیلی کوچک‌اند؛ خیلی پایین یعنی گام‌ها خیلی بزرگ‌اند. هدف تقریبی: 0.2 تا 0.5. |
| **Aggregation artifact** [5] | خطای ناشی از میانگین‌گیری | الگویی در داده‌های میانگین‌گیری‌شده که در هیچ فردی دیده نمی‌شود؛ مثلاً منحنی توانی که از میانگین‌گیری یادگیرنده‌های نمایی به دست می‌آید. |
| **AIC / AICc** [7] | معیار اطلاعاتی آکائیکه | $2\,\mathrm{NLL} + 2k$؛ دقت پیش‌بینی روی داده‌ی جدید را تخمین می‌زند. AICc یک تصحیح برای نمونه‌های کوچک اضافه می‌کند. |
| **Akaike weight** [7] | وزن آکائیکه | $w_i \propto \exp(-\Delta_i/2)$: پشتیبانی نسبی از مدل $i$ به‌عنوان بهترین پیش‌بینی‌کننده در میان مدل‌های رقیب. |
| **Attention weight** ($w_m$) [14] | وزن توجه | پارامتر GCM: سهمی از توجه که به بُعد $m$ محرک داده می‌شود (مجموع وزن‌ها 1 است). |
| **Bayes factor** ($\mathrm{BF}_{12}$) [10] | Bayes factor | نسبت درست‌نمایی‌های حاشیه‌ای $p(\mathbf{y}\mid\mathcal{M}_1)/p(\mathbf{y}\mid\mathcal{M}_2)$: داده‌ها چقدر نسبت بخت (odds) دو مدل را تغییر می‌دهند. |
| **Bayesian data analysis** [9] | تحلیل داده‌ی بیزی | استفاده از قاعده‌ی بیز برای استنباط پارامترها و مدل‌ها از داده؛ روشی که پژوهشگر به کار می‌برد و برای هر مدلی قابل استفاده است. |
| **Bayesian model of cognition** [15] | مدل بیزی شناخت | این فرضیه که ذهن (به‌طور تقریبی) استنباط بیزی انجام می‌دهد؛ نظریه‌ای در سطح محاسباتی. |
| **Beta-binomial model** [9] | مدل beta-binomial | درست‌نمایی دوجمله‌ای با پیشین Beta؛ پسین هم دوباره Beta است (conjugacy). |
| **BIC** [7] | معیار اطلاعاتی بیزی | $2\,\mathrm{NLL} + k\ln N$؛ تقریبی از $-2\ln p(\mathbf{y}\mid\mathcal{M})$ است و مدل‌های ساده‌تری از AIC را ترجیح می‌دهد. |
| **Bias–variance trade-off** [6] | trade-off سوگیری–واریانس | خطای مورد انتظار پیش‌بینی = نویز + مربع سوگیری + واریانس. مدل‌های منعطف سوگیری را کم و واریانس را زیاد می‌کنند. |
| **Bootstrap (parametric)** [5] | bootstrap پارامتری | از مدل برازش‌شده تعداد زیادی مجموعه‌داده شبیه‌سازی کنید، هرکدام را دوباره برازش کنید و پراکندگی برآوردها را به‌عنوان عدم قطعیت آن‌ها به کار ببرید. |
| **Boundary separation** ($a$) [1, 14] | فاصله‌ی مرزها | پارامتر random walk / DDM: فاصله‌ی بین دو مرز پاسخ. نماینده‌ی احتیاط (caution). |
| **Burn-in (warm-up)** [11] | دوره‌ی گرم‌شدن (burn-in) | تکرارهای اولیه‌ی MCMC که دور ریخته می‌شوند چون هنوز تحت تأثیر مقدار شروع‌اند. |
| **Centered / non-centered parameterization** [13] | پارامترسازی centered / non-centered | دو روش هم‌ارز برای نوشتن یک مدل سلسله‌مراتبی؛ شکل non-centered ($d_j = \mu + \sigma z_j$) از هندسه‌ی قیفی و divergence جلوگیری می‌کند. |
| **Complete / no / partial pooling** [5, 13] | complete pooling / no pooling / partial pooling | یک مجموعه پارامتر برای همه / پارامترهای مستقل برای هر فرد / پارامترهای فردی که از یک توزیع گروهی برآوردشده می‌آیند. |
| **Confusion matrix (model recovery)** [7] | confusion matrix (بازیابی مدل) | $P(\text{مدل انتخاب‌شده} \mid \text{مدل تولیدکننده})$ که با شبیه‌سازی تخمین زده می‌شود. |
| **Conjugate prior** [9, 12] | پیشین conjugate | پیشینی که پسینی از همان خانواده می‌دهد (مثلاً Beta برای داده‌ی دوجمله‌ای)؛ نمونه‌گیری Gibbs را ممکن می‌کند. |
| **Credible interval / HDI** [9] | credible interval / بازه‌ی بیشترین چگالی | بازه‌ای که احتمال پسین مشخصی (مثلاً 95%) را در بر دارد؛ HDI باریک‌ترین چنین بازه‌ای است. |
| **Criterion** ($c$) [2] | ملاک (criterion) | پارامتر سوگیری پاسخ در SDT: محل ملاک نسبت به نقطه‌ی میانی توزیع‌های نویز و علامت. مقدار مثبت یعنی محافظه‌کار. |
| **Cross-validation (K-fold, LOO)** [6] | cross-validation | مدل را روی بخشی از داده برازش کنید و پیش‌بینی‌هایش را روی بخش کنارگذاشته بسنجید و این کار را بین $K$ بخش (fold) بچرخانید؛ LOO هر بار یک مشاهده را کنار می‌گذارد. |
| **$d'$ (sensitivity)** [2] | حساسیت | پارامتر SDT: فاصله‌ی بین توزیع‌های علامت و نویز بر حسب واحد انحراف معیار. |
| **Delta rule / Rescorla–Wagner rule** [15] | قاعده‌ی دلتا / قاعده‌ی Rescorla–Wagner | به‌روزرسانی مبتنی بر خطا: $Q \leftarrow Q + \alpha(r - Q)$. |
| **Deterministic core** [2] | هسته‌ی قطعی | بخشی از مدل که پیش‌بینی میانگین را می‌دهد، $f(x;\boldsymbol\theta)$. |
| **Deviance** ($G^2$) [4] | انحراف (deviance) | $2(\ell_{\text{sat}} - \hat\ell)$: میزان عدم برازش نسبت به مدل اشباع‌شده؛ تقریباً $\chi^2$ با درجه‌ی آزادی = تعداد خانه‌ها − $k$. |
| **Divergent transition** [13] | divergence | مسیری در NUTS که انتگرال‌گیری عددی‌اش شکسته است؛ نشان می‌دهد بخشی از پسین به‌خوبی کاوش نشده است. |
| **Drift rate** ($v$) [1, 14] | drift rate | پارامتر random walk / DDM: نرخ میانگین انباشت شواهد. نماینده‌ی کیفیت شواهد. |
| **Drift-diffusion model (DDM)** [14] | مدل drift-diffusion | انباشت پیوسته و پرنویز شواهد بین دو مرز؛ انتخاب‌ها و توزیع زمان‌های واکنش را پیش‌بینی می‌کند. |
| **Effective sample size (ESS)** [12] | اندازه‌ی مؤثر نمونه | تعداد نمونه‌های مستقلی که همان دقت نمونه‌های خودهمبسته‌ی MCMC را می‌دهند. |
| **Error surface** [3] | سطح خطا | معیار ناهمخوانی (SSE یا NLL) به‌صورت تابعی از پارامترها؛ شکلش کمینه‌ها، دره‌ها (trade-off پارامترها) و فلات‌ها را نشان می‌دهد. |
| **Evidence / marginal likelihood** [9, 10] | شواهد / marginal likelihood | $p(\mathbf{y}\mid\mathcal{M}) = \int p(\mathbf{y}\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta$: مدل پیش از برازش، داده‌ها را چقدر خوب پیش‌بینی کرده بود. |
| **EZ-diffusion** [14] | EZ-diffusion | برآورد بسته (closed-form) drift rate، فاصله‌ی مرزها و non-decision time از دقت و میانگین و واریانس زمان واکنش پاسخ‌های درست. |
| **Flexibility (model complexity)** [6] | انعطاف‌پذیری (پیچیدگی مدل) | دامنه‌ی الگوهای داده‌ای که یک مدل می‌تواند تولید کند؛ به تعداد پارامترها *و* شکل تابعی بستگی دارد. |
| **Forward / inverse problem** [1] | مسئله‌ی مستقیم / معکوس | شبیه‌سازی (پارامتر ← داده) در برابر برآورد (داده ← پارامتر). |
| **Full conditional** [12] | full conditional | توزیع یک پارامتر به شرط همه‌ی پارامترهای دیگر و داده؛ Gibbs از آن نمونه می‌گیرد. |
| **GCM (Generalized Context Model)** [14] | مدل بافت تعمیم‌یافته | مدل exemplar دسته‌بندی: دسته‌بندی بر اساس مجموع شباهت به نمونه‌های ذخیره‌شده. |
| **Generalization criterion** [6] | معیار تعمیم | ارزیابی مدل‌ها با پیش‌بینی شرایط جدید (برون‌یابی) به‌جای trialهای جدید. |
| **Gibbs sampling** [12] | نمونه‌گیری Gibbs | نوعی MCMC که هر پارامتر را با نمونه‌گیری از full conditionalش به‌روز می‌کند؛ همه‌ی نمونه‌ها پذیرفته می‌شوند. |
| **Grid approximation** [9] | تقریب شبکه‌ای | محاسبه‌ی پسین روی شبکه‌ای از مقادیر پارامتر؛ برای 1 تا 2 پارامتر شدنی است. |
| **Hamiltonian Monte Carlo (HMC) / NUTS** [13] | Hamiltonian Monte Carlo / NUTS | MCMC مبتنی بر گرادیان که با شبیه‌سازی دینامیک فیزیکی پیشنهادهای دور با احتمال پذیرش بالا می‌سازد؛ NUTS طول مسیر را خودکار تنظیم می‌کند. |
| **Hessian / observed Fisher information** [5] | ماتریس Hessian / اطلاع فیشر مشاهده‌شده | ماتریس مشتق‌های دوم NLL در نقطه‌ی MLE؛ معکوسش تقریبی از کوواریانس برآوردهاست. |
| **Hierarchical (multilevel) model** [13] | مدل سلسله‌مراتبی (چندسطحی) | مدلی که پارامترهای سطح فرد از توزیع‌های سطح گروه می‌آیند. |
| **Identifiability (structural / practical)** [7] | identifiability (ساختاری / عملی) | آیا پارامترها به‌طور یکتا قابل تعیین‌اند؛ در اصل (ساختاری) یا با داده‌های موجود (عملی). |
| **Ideal observer** [15] | مشاهده‌گر ایده‌آل | مدل استنباط بهینه با توجه به اطلاعات موجود؛ مثلاً ترکیب سرنخ‌ها با وزن‌دهی بر اساس قابلیت اطمینان. |
| **Inverse temperature** ($\beta$) [15] | inverse temperature | پارامتر softmax: حساسیت انتخاب‌ها به تفاوت ارزش‌ها (اکتشاف در برابر بهره‌برداری). |
| **Inversion matrix (model recovery)** [7] | inversion matrix (بازیابی مدل) | $P(\text{مدل تولیدکننده} \mid \text{مدل انتخاب‌شده})$: چقدر می‌توان به نتیجه‌ی انتخاب مدل اعتماد کرد. |
| **Learning rate** ($\alpha$) [15] | نرخ یادگیری | میزان تأثیر خطای پیش‌بینی بر به‌روزرسانی ارزش‌ها. |
| **Likelihood** ($L$), **log-likelihood** ($\ell$), **NLL** [4] | درست‌نمایی، لگاریتم درست‌نمایی، منفی لگاریتم درست‌نمایی | $p(\mathbf{y}\mid\boldsymbol\theta)$ به‌عنوان تابعی از $\boldsymbol\theta$؛ لگاریتم آن؛ و منفی لگاریتم آن که بهینه‌سازها کمینه‌اش می‌کنند. |
| **Likelihood-ratio test (LRT)** [7] | آزمون نسبت درست‌نمایی | برای مدل‌های nested، تحت مدل ساده‌تر $2\Delta\ell \sim \chi^2_{\Delta k}$. |
| **Linking assumption** [2] | فرض پیوند | اینکه کمیت‌های مدل چگونه به رفتار قابل مشاهده نگاشت می‌شوند. |
| **Local minimum** [3] | کمینه‌ی محلی | نقطه‌ای پایین‌تر از اطرافش ولی نه کمینه‌ی سراسری؛ بهینه‌سازی تک‌شروعی ممکن است در آن گیر کند. از multi-start استفاده کنید. |
| **MAP** [9] | برآورد بیشینه‌ی پسین | مُد پسین؛ تحت پیشین تخت با MLE برابر است. |
| **Markov chain Monte Carlo (MCMC)** [11] | مونت‌کارلوی زنجیره‌ی مارکوف | نمونه‌گیری از پسین با شبیه‌سازی یک زنجیره‌ی مارکوف که توزیع ایستایش همان پسین است. |
| **Maximum likelihood estimate (MLE)** [4] | برآورد بیشینه درست‌نمایی | مقادیری از پارامترها که درست‌نمایی را بیشینه می‌کنند. |
| **MCSE** [12] | خطای استاندارد مونت‌کارلو | انحراف معیار پسین تقسیم بر $\sqrt{\mathrm{ESS}}$: خطای شبیه‌سازی در میانگین پسین. |
| **Metropolis / Metropolis–Hastings** [11] | Metropolis / Metropolis–Hastings | MCMC که یک حرکت پیشنهاد می‌دهد و آن را با احتمال $\min(1, \text{نسبت})$ می‌پذیرد؛ Hastings برای پیشنهادهای نامتقارن یک تصحیح اضافه می‌کند. |
| **Model mimicry** [7] | تقلید مدل | وقتی یک مدل داده‌هایی تولید می‌کند که انگار مدل دیگری تولیدشان کرده است. |
| **Model recovery** [7] | بازیابی مدل | شبیه‌سازی از هر مدل رقیب و بررسی اینکه آیا روش مقایسه، مدل تولیدکننده را انتخاب می‌کند. |
| **Monte Carlo integration** [11] | انتگرال‌گیری مونت‌کارلو | تقریب یک امید ریاضی با میانگین نمونه‌های تصادفی؛ خطا متناسب با $1/\sqrt{S}$. |
| **Multi-start** [3] | چندشروعی | اجرای بهینه‌ساز از تعداد زیادی مقدار شروع و نگه‌داشتن بهترین نتیجه. |
| **Nelder–Mead simplex** [3] | سیمپلکس Nelder–Mead | بهینه‌ساز بدون مشتق که یک سیمپلکس را با بازتاب، گسترش، انقباض و جمع‌شدن حرکت می‌دهد. |
| **Nested models** [7] | مدل‌های nested | یکی حالت خاصی از دیگری است (با ثابت کردن برخی پارامترها). |
| **Noise model** [2] | مدل نویز | توزیع مشاهدات حول پیش‌بینی قطعی (مثلاً دوجمله‌ای، گاوسی). |
| **Non-decision time** ($t_0$, $T_{er}$) [1, 14] | non-decision time | بخشی از زمان واکنش که صرف انباشت شواهد نمی‌شود (رمزگذاری و اجرای حرکتی). |
| **Overfitting** [6] | overfitting | برازش نویز یک نمونه، که برازش را بهتر و پیش‌بینی داده‌ی جدید را بدتر می‌کند. |
| **Parameter recovery** [7] | بازیابی پارامتر | شبیه‌سازی داده از پارامترهای معلوم با همان طرح آزمایش واقعی و بررسی اینکه آیا برازش همان‌ها را برمی‌گرداند. |
| **Parameter trade-off** [3, 5] | trade-off پارامترها | تغییر یک پارامتر با پارامتر دیگری جبران می‌شود؛ به شکل دره‌ی مورب در سطح خطا و برآوردهای همبسته دیده می‌شود. |
| **Posterior** [9] | پسین | $p(\boldsymbol\theta\mid\mathbf{y}) \propto p(\mathbf{y}\mid\boldsymbol\theta)p(\boldsymbol\theta)$. |
| **Posterior predictive check (PPC)** [10] | بررسی پیش‌بینی پسین | مقایسه‌ی داده‌های شبیه‌سازی‌شده از مدل برازش‌شده با داده‌های مشاهده‌شده برای بررسی کفایت مدل. |
| **Power / exponential forgetting** [2] | فراموشی توانی / نمایی | $A(1+t)^{-d}$ (نرخ نسبی فراموشی کاهشی) در برابر $Ae^{-\lambda t}$ (نرخ نسبی ثابت). |
| **Prior / prior predictive check** [9] | پیشین / بررسی پیش‌بینی پیشین | توزیع پارامترها پیش از داده / شبیه‌سازی داده از پیشین برای اطمینان از منطقی بودن پیشین. |
| **Profile likelihood** [5] | profile likelihood | NLL کمینه‌شده روی پارامترهای دیگر برای هر مقدار از پارامتر مورد نظر؛ بازه‌های نسبت درست‌نمایی را می‌دهد. |
| **Prototype model** [14] | مدل پیش‌نمونه (prototype) | دسته‌بندی بر اساس شباهت به یک بازنمایی خلاصه برای هر دسته. |
| **R-hat** ($\hat R$) [12] | R-hat | نسبتی که واریانس بین زنجیره‌ها و درون زنجیره‌ها را مقایسه می‌کند؛ وقتی زنجیره‌ها هم‌خوان‌اند ≈ 1 (کمتر از 1.01). |
| **Random walk model** [1] | مدل گام تصادفی | انباشت گسسته‌ی شواهد تا رسیدن به مرز؛ پیش‌درآمد DDM. |
| **Relative loss rate (hazard)** [2] | نرخ نسبی فراموشی (hazard) | $-f'(t)/f(t)$: نرخ تناسبی فراموشی در زمان $t$. |
| **Reparameterization** [3, 13] | reparameterization | بهینه‌سازی یا نمونه‌گیری روی مقیاس تبدیل‌شده (مثلاً $\lambda = e^{\eta}$) برای اعمال قیدها یا بهبود هندسه. |
| **RMSD** [3] | ریشه‌ی میانگین مربع انحراف | $\sqrt{\mathrm{SSE}/N}$، بر حسب واحد داده. |
| **ROC / zROC** [2] | منحنی ROC / zROC | نرخ hit در برابر نرخ false alarm با تغییر ملاک / همین منحنی روی محورهای $z$ (probit). |
| **Saturated model** [4] | مدل اشباع‌شده | مدلی با یک پارامتر آزاد برای هر خانه‌ی داده که داده‌ها را دقیقاً بازتولید می‌کند. |
| **Savage–Dickey density ratio** [10] | نسبت چگالی Savage–Dickey | برای مدل‌های nested، $\mathrm{BF}_{01}$ = چگالی پسین / چگالی پیشین در مقدار صفر (null). |
| **Shrinkage** [13] | shrinkage | کشیده شدن برآوردهای فردی به سمت میانگین گروه در مدل‌های سلسله‌مراتبی؛ برای داده‌های پرنویزتر قوی‌تر است. |
| **Signal detection theory (SDT)** [2] | نظریه‌ی تشخیص علامت | مدل تصمیم‌های تشخیص با شواهد پرنویز و یک ملاک؛ حساسیت را از سوگیری جدا می‌کند. |
| **Softmax** [15] | softmax | $P(o) \propto \exp(\beta Q(o))$: ارزش‌ها را به احتمال انتخاب تبدیل می‌کند. |
| **SSE / MSE** [3] | مجموع / میانگین مربعات خطا | مجموع یا میانگین مربع تفاوت‌های داده و پیش‌بینی. |
| **Standard error** [5] | خطای استاندارد | انحراف معیار توزیع نمونه‌گیری یک برآوردگر. |
| **Wald interval** [5] | بازه‌ی Wald | $\hat\theta \pm 1.96\,\mathrm{SE}$ با SE به‌دست‌آمده از Hessian؛ نرمال بودن تقریبی را فرض می‌کند. |
| **Weighted least squares** [3] | کمترین مربعات وزنی | مربع خطاها با وزن معکوس واریانسشان. |

</div>

## AI & LLM terms (from the "Connection to AI & LLMs" sections) · اصطلاحات هوش مصنوعی و LLM (از بخش‌های «ارتباط با هوش مصنوعی و LLMها»)

| Term | Definition |
|---|---|
| **Benchmark contamination** [6] | Test items (or their answers) that appeared in a model's training data; a form of data leakage that inflates scores. |
| **Bradley–Terry model** [15] | $P(i \succ j) = 1/(1 + e^{-(r_i - r_j)})$: choice model for paired comparisons; used for RLHF reward models. Equivalent to a two-option softmax with $\beta = 1$. |
| **Cross-entropy loss** [4] | The training loss of language models: the negative log-likelihood of the next token, averaged over tokens. |
| **Embedding** [14] | A vector that a model assigns to a word or text; distances between embeddings are often used as a proxy for similarity. |
| **In-context learning** [7] | An LLM's improvement on a task from examples given in the prompt, without changing its parameters. |
| **Large language model (LLM)** [1] | A neural network (usually a transformer) trained to predict the next token in very large text corpora. |
| **Perplexity** [4] | $\exp(\text{NLL per token})$: the effective number of equally likely next tokens; lower is better. |
| **RLHF** [15] | Reinforcement learning from human feedback: a reward model is fitted to human preference choices, and the language model is then trained to maximize that reward. |
| **Scaling law** [3] | An empirical (usually power-law) relation between model loss and model size, data size or compute. |
| **Self-consistency** [11] | Sampling several answers from a model and taking the majority vote. |
| **Temperature** [1] | Divides the logits before the softmax in an LLM; low temperature gives near-deterministic output, high temperature more random output ($\beta = 1/T$). |
| **Token** [1] | The unit a language model reads and predicts: a word or part of a word. |

<div dir="rtl">

| اصطلاح (English) | معادل فارسی | تعریف |
|---|---|---|
| **Benchmark contamination** [6] | آلودگی benchmark | آیتم‌های آزمون (یا جواب‌هایشان) که در داده‌ی آموزشی مدل بوده‌اند؛ نوعی نشت داده که نمره را بیش از واقع نشان می‌دهد. |
| **Bradley–Terry model** [15] | مدل Bradley–Terry | $P(i \succ j) = 1/(1 + e^{-(r_i - r_j)})$: مدل انتخاب برای مقایسه‌های جفتی؛ برای مدل‌های پاداش RLHF استفاده می‌شود. هم‌ارز softmax دوگزینه‌ای با $\beta = 1$. |
| **Cross-entropy loss** [4] | تابع زیان cross-entropy | تابع زیان آموزش مدل‌های زبانی: منفی لگاریتم درست‌نمایی token بعدی، میانگین‌گرفته روی tokenها. |
| **Embedding** [14] | بردار embedding (بازنمایی برداری) | برداری که یک مدل به یک کلمه یا متن نسبت می‌دهد؛ فاصله‌ی embeddingها اغلب به جای شباهت استفاده می‌شود. |
| **In-context learning** [7] | یادگیری درون‌بافتی | بهتر شدن یک LLM در یک تکلیف با مثال‌هایی که در prompt داده می‌شود، بدون تغییر پارامترهایش. |
| **Large language model (LLM)** [1] | مدل بزرگ زبانی | یک شبکه‌ی عصبی (معمولاً transformer) که برای پیش‌بینی token بعدی در corpusهای متنی خیلی بزرگ آموزش دیده. |
| **Perplexity** [4] | perplexity (سردرگمی) | $\exp(\text{NLL per token})$: تعداد مؤثر tokenهای بعدی هم‌احتمال؛ کمتر بهتر است. |
| **RLHF** [15] | یادگیری تقویتی از بازخورد انسانی | یک مدل پاداش روی انتخاب‌های ترجیحی انسان برازش می‌شود، و بعد مدل زبانی برای بیشینه کردن آن پاداش آموزش می‌بیند. |
| **Scaling law** [3] | قانون مقیاس | رابطه‌ای تجربی (معمولاً توانی) بین زیان مدل و اندازه‌ی مدل، اندازه‌ی داده یا محاسبات. |
| **Self-consistency** [11] | self-consistency (خودسازگاری) | نمونه‌گیری چند جواب از یک مدل و گرفتن رأی اکثریت. |
| **Temperature** [1] | دما | logitها را پیش از softmax در یک LLM تقسیم می‌کند؛ دمای پایین خروجی تقریباً قطعی و دمای بالا خروجی تصادفی‌تر می‌دهد ($\beta = 1/T$). |
| **Token** [1] | token | واحدی که مدل زبانی می‌خواند و پیش‌بینی می‌کند: یک کلمه یا بخشی از کلمه. |

</div>
