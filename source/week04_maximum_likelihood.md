# Week 4: Maximum Likelihood Estimation · هفته‌ی 4: برآورد بیشینه درست‌نمایی (Maximum Likelihood)

> **Chapter 2: Parameter estimation methods** · Lecture 1 h · Lab 2 h
> **Running data:** the Week 2–3 forgetting experiment (binomial recall counts), plus a new SDT experiment with three payoff conditions.

<div dir="rtl">

> **فصل 2: روش‌های برآورد پارامتر** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** آزمایش فراموشی هفته‌های 2–3 (شمارش‌های یادآوری دوجمله‌ای)، به‌علاوه‌ی یک آزمایش SDT جدید با سه شرط پاداش (payoff).

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| binomial distribution | توزیع دوجمله‌ای | توزیع تعداد موفقیت در n کوشش |
| signal detection theory (SDT) | نظریه‌ی تشخیص علامت | مدلی که حساسیت را از سوگیری پاسخ جدا می‌کند |
| log-likelihood / NLL | لگاریتم درست‌نمایی / منفی آن | مقداری که بهینه‌سازها کمینه یا بیشینه می‌کنند |
| least squares | کمترین مربعات | روش برازش با کمینه کردن مجموع مربع خطاها |
| maximum likelihood estimate (MLE) | برآورد بیشینه‌ی درست‌نمایی | پارامترهایی که داده را محتمل‌ترین می‌کنند |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| deviance (G²) | انحراف (deviance) | معیار عدم برازش نسبت به مدل اشباع‌شده |
| bounds / constraints | کران‌ها / قیدها | محدودیت‌های مجاز برای مقدار پارامترها |
| response bias | سوگیری پاسخ | تمایل به یک پاسخ، مستقل از محرک |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| optimizer | بهینه‌ساز | الگوریتمی که کمینه‌ی تابع را پیدا می‌کند |
| SSE / RMSD | مجموع مربعات خطا / ریشه‌ی میانگین مربع انحراف | معیارهای فاصله‌ی داده و پیش‌بینی |
| saturated model | مدل اشباع‌شده | مدلی که داده را دقیقاً بازتولید می‌کند |
| likelihood-ratio test (LRT) | آزمون نسبت درست‌نمایی | مقایسه‌ی دو مدل تودرتو |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| liberal / conservative | آسان‌گیر / محافظه‌کار | تمایل به گفتن «بله» / «نه» |
| token | token (واحد متن) | کلمه یا بخشی از کلمه که مدل زبانی پیش‌بینی می‌کند |
| perplexity | perplexity (سردرگمی) | e به توان NLL هر token |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Distinguish** probability (data varying, parameters fixed) from likelihood (data fixed, parameters varying).
2. **Derive** the likelihood and log-likelihood for binomial (Bernoulli) and Gaussian data models, and **show** that least squares is maximum likelihood under equal-variance Gaussian noise.
3. **Implement** maximum likelihood estimation (MLE) by minimizing the negative log-likelihood (NLL) in Python, for forgetting curves and for a multi-condition SDT model.
4. **Evaluate** absolute goodness of fit with the deviance $G^2$ and **compare** MLE with least-squares estimates.
5. **Interpret** constrained models (e.g., "payoffs change bias, not sensitivity") as substantive psychological hypotheses.

<div dir="rtl">

1. احتمال (داده متغیر، پارامترها ثابت) را از درست‌نمایی (داده ثابت، پارامترها متغیر) **متمایز کنند**.
2. درست‌نمایی و لگاریتم درست‌نمایی را برای مدل‌های داده‌ی دوجمله‌ای (برنولی) و گاوسی **استخراج کنند** و **نشان دهند** که کمترین مربعات همان بیشینه درست‌نمایی تحت نویز گاوسی با واریانس برابر است.
3. برآورد بیشینه درست‌نمایی (MLE) را با کمینه کردن منفی لگاریتم درست‌نمایی (NLL) در Python، برای منحنی‌های فراموشی و یک مدل SDT چندشرطی، **پیاده‌سازی کنند**.
4. برازش مطلق را با انحراف (deviance) $G^2$ **ارزیابی کنند** و MLE را با برآوردهای کمترین مربعات **مقایسه کنند**.
5. مدل‌های مقیدشده (مثلاً «پاداش سوگیری را تغییر می‌دهد، نه حساسیت را») را به‌عنوان فرضیه‌های روان‌شناختی واقعی **تفسیر کنند**.

</div>

---

## Motivation & big picture · مقدمه

In Week 3, least squares treated every data point as equally reliable. But a recall proportion of 0.50 measured on 50 items is *noisier* than a proportion of 0.95: binomial variance $f(1-f)/n$ depends on $f$. Least squares also has nothing to say about data that are not continuous numbers, such as a single yes/no response, a choice among options, or a confidence rating.

<div dir="rtl">

در هفته‌ی 3، کمترین مربعات با همه‌ی نقاط داده به یک اندازه قابل اعتماد رفتار کرد. ولی نسبت یادآوری 0.50 که روی 50 آیتم اندازه‌گیری شده *پرنویزتر* از نسبت 0.95 است: واریانس دوجمله‌ای $f(1-f)/n$ به $f$ بستگی دارد. کمترین مربعات همچنین درباره‌ی داده‌هایی که اعداد پیوسته نیستند، مثل یک پاسخ بله/نه، یک انتخاب بین چند گزینه یا یک درجه‌ی اطمینان، حرفی برای گفتن ندارد.

</div>

Maximum likelihood replaces "make predictions close to data" with a sharper question:

<div dir="rtl">

بیشینه درست‌نمایی «پیش‌بینی‌ها را به داده نزدیک کن» را با سؤالی دقیق‌تر جایگزین می‌کند:

</div>

> **Which parameter values make the data we actually observed most probable?**

<div dir="rtl">

> **کدام مقادیر پارامتر داده‌ای را که واقعاً مشاهده کردیم محتمل‌ترین می‌کنند؟**

</div>

To answer it, the model must say how probable *any* possible dataset is, which is exactly the noise model (component 4 of Week 2's anatomy). Once we have it, MLE handles counts, choices, RTs and mixtures of these in the same way. It also gives us, for free, an absolute measure of misfit (the deviance), the basis for standard errors (Week 5), information criteria (Week 7), and the likelihood term in Bayes' rule (Weeks 9–13). **The likelihood is the single most important object in this course.**

<div dir="rtl">

برای جواب دادن، مدل باید بگوید *هر* مجموعه‌داده‌ی ممکن چقدر محتمل است، و این دقیقاً همان مدل نویز است (جزء 4 در کالبدشکافی هفته‌ی 2). وقتی آن را داشته باشیم، MLE با شمارش‌ها، انتخاب‌ها، زمان‌های واکنش و ترکیب‌هایشان به یک شکل کار می‌کند. همچنین بدون هزینه‌ی اضافه یک معیار مطلق عدم برازش (deviance)، پایه‌ی خطاهای استاندارد (هفته‌ی 5)، معیارهای اطلاعاتی (هفته‌ی 7) و جمله‌ی درست‌نمایی در قاعده‌ی بیز (هفته‌های 9–13) را به ما می‌دهد. **درست‌نمایی مهم‌ترین مفهوم این درس است.**

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Almost every published cognitive model** is fitted by maximum likelihood or by its Bayesian extension (Weeks 9–13). When a paper reports "model fits", "AIC" or "log-likelihood", MLE is underneath.
- **Choice data**: which option a person picks (in a memory test, a gamble, a learning task) is not a continuous number, so least squares does not apply. The likelihood handles choices naturally.
- **Psychophysics**: the psychometric function (probability of detecting a stimulus as a function of its strength) is fitted by binomial MLE in every vision and hearing lab.
- **Testing hypotheses inside a model**: "does the payoff change sensitivity or only bias?" becomes a comparison of two likelihoods (Section 6).
- **AI**: large language models are trained by maximizing the likelihood of text (see the AI & LLMs section).

<div dir="rtl">

- **تقریباً هر مدل شناختی منتشرشده** با بیشینه‌ی درست‌نمایی یا نسخه‌ی بیزی آن (هفته‌های 9 تا 13) برازش می‌شود. وقتی مقاله‌ای «برازش مدل»، «AIC» یا «log-likelihood» گزارش می‌کند، MLE پشت آن است.
- **داده‌ی انتخاب:** اینکه آدم کدام گزینه را انتخاب می‌کند (در آزمون حافظه، یک قمار، یک تکلیف یادگیری) یک عدد پیوسته نیست، پس کمترین مربعات کار نمی‌کند. درست‌نمایی به‌طور طبیعی با انتخاب‌ها کار می‌کند.
- **روان‌فیزیک (psychophysics):** تابع روان‌سنجی (احتمال تشخیص یک محرک بر حسب شدت آن) در هر آزمایشگاه بینایی و شنوایی با MLE دوجمله‌ای برازش می‌شود.
- **آزمودن فرضیه‌ها داخل یک مدل:** «آیا پاداش حساسیت را عوض می‌کند یا فقط سوگیری را؟» به مقایسه‌ی دو درست‌نمایی تبدیل می‌شود (بخش 6).
- **هوش مصنوعی:** مدل‌های بزرگ زبانی با بیشینه کردن درست‌نمایی متن آموزش می‌بینند (بخش هوش مصنوعی و LLMها را ببینید).

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

Imagine trying different parameter values one by one. For each value, ask the model: "if this were the true value, how probable would the data I actually collected be?" That number is the **likelihood** of that parameter value. The **maximum likelihood estimate (MLE)** is the parameter value under which the observed data would have been most probable. Example: someone recalls 7 of 10 words. If their true recall probability were 0.5, getting exactly 7 would be fairly unlikely (0.117); if it were 0.7, it would be more likely (0.267). So 0.7 is the better explanation, and indeed the MLE is 7/10. In practice we work with the **logarithm** of the likelihood (so products become sums) and we let the computer *minimize* its negative (NLL), using the optimizers of Week 3. Two bonuses: least squares turns out to be a special case of MLE, and the likelihood gives an absolute test of misfit ($G^2$).

<div dir="rtl">

تصور کنید مقدارهای مختلف پارامتر را یکی‌یکی امتحان می‌کنید. برای هر مقدار از مدل بپرسید: «اگر این مقدار واقعی بود، داده‌ای که واقعاً جمع کرده‌ام چقدر محتمل بود؟» این عدد **درست‌نمایی (likelihood)** آن مقدار پارامتر است. **برآورد بیشینه‌ی درست‌نمایی (MLE)** مقداری از پارامتر است که تحت آن، داده‌ی مشاهده‌شده محتمل‌ترین بود. مثال: کسی 7 کلمه از 10 کلمه را به یاد می‌آورد. اگر احتمال واقعی یادآوری او 0.5 بود، به دست آمدن دقیقاً 7 نسبتاً بعید بود (0.117)؛ اگر 0.7 بود، محتمل‌تر بود (0.267). پس 0.7 توضیح بهتری است و در واقع MLE برابر 7/10 است. در عمل با **لگاریتم** درست‌نمایی کار می‌کنیم (تا ضرب‌ها به جمع تبدیل شوند) و از کامپیوتر می‌خواهیم منفی آن (NLL) را با بهینه‌سازهای هفته‌ی 3 *کمینه* کند. دو جایزه هم می‌گیریم: معلوم می‌شود کمترین مربعات حالت خاصی از MLE است، و درست‌نمایی یک آزمون مطلق برای عدم برازش ($G^2$) می‌دهد.

</div>

**Suggested timing (60 min):** probability vs. likelihood 10 · binomial MLE 15 · log-likelihood and NLL 10 · Gaussian case (LS = MLE) 10 · goodness of fit $G^2$ 10 · constrained models 5.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** احتمال در برابر درست‌نمایی 10 · MLE دوجمله‌ای 15 · لگاریتم درست‌نمایی و NLL 10 · حالت گاوسی (LS = MLE) 10 · برازش مطلق $G^2$ 10 · مدل‌های مقیدشده 5.

</div>

### 1. Probability vs. likelihood · 1. احتمال در برابر درست‌نمایی

The same function $p(\mathbf{y}\mid\boldsymbol\theta)$ can be read in two ways:

<div dir="rtl">

تابع یکسان $p(\mathbf{y}\mid\boldsymbol\theta)$ را می‌شود به دو شکل خواند:

</div>

| Reading | Fixed | Varies | Name | Sums/integrates to 1? |
|---|---|---|---|---|
| Before the experiment | $\boldsymbol\theta$ | $\mathbf{y}$ | Probability (mass/density) of data | Yes, over $\mathbf{y}$ |
| After the experiment | $\mathbf{y}$ (observed) | $\boldsymbol\theta$ | **Likelihood** $L(\boldsymbol\theta) = p(\mathbf{y}\mid\boldsymbol\theta,\mathcal{M})$ | **No**, not over $\boldsymbol\theta$ |

<div dir="rtl">

| خوانش | ثابت | متغیر | نام | جمع/انتگرالش 1 است؟ |
|---|---|---|---|---|
| پیش از آزمایش | $\boldsymbol\theta$ | $\mathbf{y}$ | احتمال (جرم/چگالی) داده | بله، روی $\mathbf{y}$ |
| پس از آزمایش | $\mathbf{y}$ (مشاهده‌شده) | $\boldsymbol\theta$ | **درست‌نمایی** $L(\boldsymbol\theta) = p(\mathbf{y}\mid\boldsymbol\theta,\mathcal{M})$ | **نه**، روی $\boldsymbol\theta$ نه |

</div>

The likelihood is **not** the probability that the parameters are correct. It is the probability of the data *under* each candidate parameter value. (Turning it into a probability distribution over $\boldsymbol\theta$ requires a prior: Bayes, Week 9.)

<div dir="rtl">

درست‌نمایی احتمال درست بودن پارامترها **نیست**. احتمال داده *تحت* هر مقدار ممکن پارامتر است. (تبدیل آن به یک توزیع احتمال روی $\boldsymbol\theta$ به یک پیشین نیاز دارد: بیز، هفته‌ی 9.)

</div>

**Example.** A participant recalls $y = 7$ of $n = 10$ items. Under a binomial model with recall probability $\theta$:

<div dir="rtl">

**مثال.** یک شرکت‌کننده $y = 7$ از $n = 10$ آیتم را به یاد می‌آورد. تحت یک مدل دوجمله‌ای با احتمال یادآوری $\theta$:

</div>

$$
L(\theta) = \binom{10}{7}\theta^{7}(1-\theta)^{3}.
$$

$L(0.5) = 0.117$, $L(0.7) = 0.267$: the observed data are about 2.3 times more probable if $\theta = 0.7$ than if $\theta = 0.5$.

<div dir="rtl">

$L(0.5) = 0.117$، $L(0.7) = 0.267$: داده‌های مشاهده‌شده اگر $\theta = 0.7$ باشد حدود 2.3 برابر محتمل‌ترند تا اگر $\theta = 0.5$ باشد.

</div>

#### Reading the math · خواندن ریاضی

$L(\theta) = \binom{10}{7}\theta^{7}(1-\theta)^{3}$:

- $\theta^7$: the probability that 7 specific items are recalled (each with probability $\theta$).
- $(1-\theta)^3$: the probability that the other 3 are forgotten.
- $\binom{10}{7} = 120$ ("10 choose 7"): the number of different ways to pick which 7 of the 10 items are the recalled ones. It does not depend on $\theta$, so it never changes *where* the maximum is.
- Plug in $\theta = 0.7$: $120 \times 0.7^7 \times 0.3^3 = 120 \times 0.0824 \times 0.027 = 0.267$.

The key mental switch: in probability, $\theta$ is fixed and we ask about different data; in likelihood, the data are fixed (we already have them) and we compare different $\theta$.

<div dir="rtl">

$L(\theta) = \binom{10}{7}\theta^{7}(1-\theta)^{3}$:

- $\theta^7$: احتمال اینکه 7 آیتم مشخص به یاد آورده شوند (هرکدام با احتمال $\theta$).
- $(1-\theta)^3$: احتمال اینکه 3 آیتم دیگر فراموش شوند.
- $\binom{10}{7} = 120$ («ترکیب 7 از 10»): تعداد راه‌های مختلف برای انتخاب اینکه کدام 7 آیتم از 10 آیتم به یاد آمده‌اند. به $\theta$ بستگی ندارد، پس هیچ‌وقت *محل* بیشینه را عوض نمی‌کند.
- با $\theta = 0.7$: $120 \times 0.7^7 \times 0.3^3 = 120 \times 0.0824 \times 0.027 = 0.267$.

تغییر نگاه اصلی: در احتمال، $\theta$ ثابت است و درباره‌ی داده‌های مختلف می‌پرسیم؛ در درست‌نمایی، داده ثابت است (آن را داریم) و $\theta$های مختلف را مقایسه می‌کنیم.

</div>

### 2. The maximum likelihood estimate · 2. برآورد بیشینه درست‌نمایی

$$
\hat{\boldsymbol\theta}_{\text{ML}} = \arg\max_{\boldsymbol\theta} L(\boldsymbol\theta) = \arg\max_{\boldsymbol\theta} \ell(\boldsymbol\theta),
\qquad \ell(\boldsymbol\theta) = \ln L(\boldsymbol\theta).
$$

**Why the log?**
1. With independent observations the likelihood is a **product**, $L = \prod_i p(y_i\mid\boldsymbol\theta)$, which underflows to 0 on a computer for even a few hundred trials. The log turns it into a **sum**, $\ell = \sum_i \ln p(y_i\mid\boldsymbol\theta)$.
2. The log is strictly increasing, so it has the same maximizer.
3. Sums are easier to differentiate.

<div dir="rtl">

**چرا لگاریتم؟**
1. با مشاهدات مستقل، درست‌نمایی یک **حاصل‌ضرب** است، $L = \prod_i p(y_i\mid\boldsymbol\theta)$، که در کامپیوتر حتی برای چند صد trial به 0 سرریز (underflow) می‌کند. لگاریتم آن را به یک **مجموع** تبدیل می‌کند، $\ell = \sum_i \ln p(y_i\mid\boldsymbol\theta)$.
2. لگاریتم اکیداً صعودی است، پس بیشینه‌کننده‌ی یکسانی دارد.
3. مشتق گرفتن از مجموع راحت‌تر است.

</div>

Optimizers *minimize*, so in code we minimize the **negative log-likelihood**, $\mathrm{NLL}(\boldsymbol\theta) = -\ell(\boldsymbol\theta)$.

<div dir="rtl">

بهینه‌سازها *کمینه* می‌کنند، پس در کد **منفی لگاریتم درست‌نمایی**، $\mathrm{NLL}(\boldsymbol\theta) = -\ell(\boldsymbol\theta)$، را کمینه می‌کنیم.

</div>

**Analytic example (binomial).** $\ell(\theta) = \text{const} + y\ln\theta + (n-y)\ln(1-\theta)$. Setting the derivative to zero:

<div dir="rtl">

**مثال تحلیلی (دوجمله‌ای).** $\ell(\theta) = \text{const} + y\ln\theta + (n-y)\ln(1-\theta)$. با صفر قرار دادن مشتق:

</div>

$$
\frac{d\ell}{d\theta} = \frac{y}{\theta} - \frac{n-y}{1-\theta} = 0 \quad\Rightarrow\quad \hat\theta = \frac{y}{n}.
$$

The MLE of a probability is the observed proportion, which is reassuring. For cognitive models the predicted probability is a *function* of the parameters, $\theta_i = f(x_i;\boldsymbol\theta)$, and we usually need a numerical optimizer.

<div dir="rtl">

MLE یک احتمال همان نسبت مشاهده‌شده است، که خیال‌مان را راحت می‌کند. در مدل‌های شناختی، احتمال پیش‌بینی‌شده *تابعی* از پارامترهاست، $\theta_i = f(x_i;\boldsymbol\theta)$، و معمولاً به یک بهینه‌ساز عددی نیاز داریم.

</div>

### 3. The binomial likelihood for forgetting curves · 3. درست‌نمایی دوجمله‌ای برای منحنی‌های فراموشی

With $y_i$ items recalled out of $n_i$ at interval $t_i$, and independent intervals:

<div dir="rtl">

با $y_i$ آیتم یادآوری‌شده از $n_i$ در فاصله‌ی $t_i$ و فاصله‌های مستقل:

</div>

$$
\ell(\boldsymbol\theta) = \sum_{i=1}^{N}\Big[\ln\binom{n_i}{y_i} + y_i \ln f(t_i;\boldsymbol\theta) + (n_i - y_i)\ln\big(1 - f(t_i;\boldsymbol\theta)\big)\Big].
$$

- The binomial coefficient does not depend on $\boldsymbol\theta$, so it does not affect the MLE (but keep it if you want to compare log-likelihoods across different data codings; `scipy.stats.binom.logpmf` includes it).
- Observations predicted to be near 0 or 1 have small variance, so a prediction that misses them is punished more heavily. MLE performs the variance weighting of Week 3's weighted least squares *automatically*.
- **Numerical safety:** if the model predicts $f = 0$ where $y > 0$, then $\ln 0 = -\infty$. Clip predictions to $[\epsilon, 1-\epsilon]$ with, e.g., $\epsilon = 10^{-10}$.

<div dir="rtl">

- ضریب دوجمله‌ای به $\boldsymbol\theta$ بستگی ندارد، پس روی MLE اثری ندارد (ولی اگر می‌خواهید لگاریتم درست‌نمایی را بین کدگذاری‌های مختلف داده مقایسه کنید نگهش دارید؛ `scipy.stats.binom.logpmf` آن را شامل می‌شود).
- مشاهداتی که پیش‌بینی می‌شود نزدیک 0 یا 1 باشند واریانس کمی دارند، پس پیش‌بینی‌ای که آن‌ها را از دست بدهد بیشتر جریمه می‌شود. MLE همان وزن‌دهی واریانسی کمترین مربعات وزنی هفته‌ی 3 را *خودکار* انجام می‌دهد.
- **ایمنی عددی:** اگر مدل جایی که $y > 0$ است $f = 0$ پیش‌بینی کند، $\ln 0 = -\infty$ می‌شود. پیش‌بینی‌ها را به $[\epsilon, 1-\epsilon]$ محدود (clip) کنید، مثلاً با $\epsilon = 10^{-10}$.

</div>

**Bernoulli vs. binomial.** If we keep the individual 0/1 responses, $\ell = \sum_{\text{trials}} [y\ln f + (1-y)\ln(1-f)]$. This differs from the binomial version only by the constant binomial coefficients, so it gives the same MLE.

<div dir="rtl">

**برنولی در برابر دوجمله‌ای.** اگر پاسخ‌های تکی 0/1 را نگه داریم، $\ell = \sum_{\text{trials}} [y\ln f + (1-y)\ln(1-f)]$. این فقط با ضرایب دوجمله‌ای ثابت با نسخه‌ی دوجمله‌ای فرق دارد، پس همان MLE را می‌دهد.

</div>

#### Reading the math · خواندن ریاضی

The forgetting log-likelihood is the single-proportion log-likelihood from Section 2, written once per retention interval and added up:

- for interval $i$: $y_i \ln f(t_i)$ rewards predicting a high recall probability where many items were recalled; $(n_i - y_i)\ln(1 - f(t_i))$ rewards predicting a low recall probability where many were forgotten.
- Adding over intervals is allowed because the intervals are assumed **independent**: the log of a product of probabilities is the sum of the logs.
- Why it weights points automatically: if the model predicts $f = 0.95$ but only 40 of 50 are recalled, the term $10 \ln(0.05) \approx -30$ is very costly. Near $f = 0.5$, the same absolute miss costs much less. Points that *should* be precise are trusted more.

<div dir="rtl">

لگاریتم درست‌نمایی فراموشی همان لگاریتم درست‌نمایی یک نسبت (بخش 2) است که برای هر فاصله‌ی زمانی یک بار نوشته و جمع شده است:

- برای فاصله‌ی $i$: جمله‌ی $y_i \ln f(t_i)$ به پیش‌بینی احتمال یادآوری بالا در جایی که آیتم‌های زیادی به یاد آمده‌اند پاداش می‌دهد؛ $(n_i - y_i)\ln(1 - f(t_i))$ به پیش‌بینی احتمال پایین در جایی که آیتم‌های زیادی فراموش شده‌اند پاداش می‌دهد.
- جمع زدن روی فاصله‌ها مجاز است چون فرض می‌کنیم فاصله‌ها **مستقل**‌اند: لگاریتم حاصل‌ضرب احتمال‌ها برابر جمع لگاریتم‌هاست.
- چرا وزن‌دهی خودکار است: اگر مدل $f = 0.95$ پیش‌بینی کند ولی فقط 40 از 50 به یاد آمده باشد، جمله‌ی $10 \ln(0.05) \approx -30$ خیلی پرهزینه است. نزدیک $f = 0.5$ همان مقدار خطا هزینه‌ی خیلی کمتری دارد. به نقطه‌هایی که *باید* دقیق باشند بیشتر اعتماد می‌شود.

</div>

### 4. The Gaussian case: least squares is maximum likelihood · 4. حالت گاوسی: کمترین مربعات همان بیشینه درست‌نمایی است

Suppose $y_i = f(x_i;\boldsymbol\theta) + \varepsilon_i$ with $\varepsilon_i \sim \mathcal{N}(0, \sigma)$, independent and with the **same** $\sigma$. Then

<div dir="rtl">

فرض کنید $y_i = f(x_i;\boldsymbol\theta) + \varepsilon_i$ با $\varepsilon_i \sim \mathcal{N}(0, \sigma)$، مستقل و با $\sigma$ **یکسان**. آن‌وقت

</div>

$$
\ell(\boldsymbol\theta, \sigma) = \sum_{i=1}^{N}\ln\left[\frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(y_i - f(x_i;\boldsymbol\theta))^2}{2\sigma^2}\right)\right]
= -\frac{N}{2}\ln(2\pi\sigma^2) - \frac{\mathrm{SSE}(\boldsymbol\theta)}{2\sigma^2}.
$$

For any fixed $\sigma$, maximizing $\ell$ over $\boldsymbol\theta$ means minimizing SSE. So **least squares = MLE under i.i.d. equal-variance Gaussian noise**. Maximizing over $\sigma$ as well gives $\hat\sigma^2 = \mathrm{SSE}/N$.

<div dir="rtl">

برای هر $\sigma$ ثابت، بیشینه کردن $\ell$ روی $\boldsymbol\theta$ یعنی کمینه کردن SSE. پس **کمترین مربعات = MLE تحت نویز گاوسی مستقل و با واریانس برابر**. بیشینه کردن روی $\sigma$ هم $\hat\sigma^2 = \mathrm{SSE}/N$ را می‌دهد.

</div>

This explains *when* least squares is appropriate (continuous, roughly symmetric noise with constant variance) and when it is not (counts, proportions, choices, skewed RTs).

<div dir="rtl">

این توضیح می‌دهد کمترین مربعات *کی* مناسب است (نویز پیوسته، تقریباً متقارن، با واریانس ثابت) و کی نیست (شمارش‌ها، نسبت‌ها، انتخاب‌ها، زمان‌های واکنش چوله).

</div>

> **Advanced: properties of the MLE.** Under regularity conditions (identifiable model, true parameters not on the boundary, $N$ large), the MLE is *consistent* (converges to the true value), *asymptotically normal*, and *asymptotically efficient* (no consistent estimator has smaller variance in the limit). Its sampling variance is approximated by the inverse of the **Fisher information**, the curvature of $-\ell$ at its minimum. Week 5 uses exactly this to compute standard errors. In small samples the MLE can be biased (e.g., $\hat\sigma^2 = \mathrm{SSE}/N$ underestimates $\sigma^2$).

<div dir="rtl">

> **پیشرفته: ویژگی‌های MLE.** تحت شرایط منظم بودن (مدل identifiable، پارامترهای واقعی نه روی مرز، $N$ بزرگ)، MLE *سازگار* (consistent: به مقدار واقعی همگرا می‌شود)، *به‌طور مجانبی نرمال* و *به‌طور مجانبی کارا* است (هیچ برآوردگر سازگاری در حد واریانس کمتری ندارد). واریانس نمونه‌گیری آن با معکوس **اطلاع فیشر** (Fisher information)، یعنی انحنای $-\ell$ در کمینه‌اش، تقریب زده می‌شود. هفته‌ی 5 دقیقاً از همین برای محاسبه‌ی خطاهای استاندارد استفاده می‌کند. در نمونه‌های کوچک MLE ممکن است سوگیری داشته باشد (مثلاً $\hat\sigma^2 = \mathrm{SSE}/N$ واریانس $\sigma^2$ را کمتر برآورد می‌کند).

</div>

### 5. Absolute goodness of fit: the deviance $G^2$ · 5. برازش مطلق: انحراف $G^2$

The log-likelihood value alone has no absolute meaning. To judge it, compare the model with the **saturated model**, which has one free probability per data cell and therefore reproduces every observed proportion exactly ($\hat f_i = y_i/n_i$). The **deviance** is

<div dir="rtl">

مقدار لگاریتم درست‌نمایی به‌تنهایی معنای مطلقی ندارد. برای قضاوت درباره‌اش، مدل را با **مدل اشباع‌شده** (saturated) مقایسه کنید که برای هر خانه‌ی داده یک احتمال آزاد دارد و بنابراین هر نسبت مشاهده‌شده را دقیقاً بازتولید می‌کند ($\hat f_i = y_i/n_i$). **انحراف** (deviance) برابر است با

</div>

$$
G^2 = 2\big[\ell_{\text{saturated}} - \ell(\hat{\boldsymbol\theta})\big]
= 2\sum_i \left[y_i \ln\frac{y_i}{n_i \hat f_i} + (n_i - y_i)\ln\frac{n_i - y_i}{n_i(1-\hat f_i)}\right],
$$

with $0 \ln 0 = 0$. If the model is correct and counts are not too small, $G^2$ approximately follows a $\chi^2$ distribution with $\text{df} = (\text{number of cells}) - k$. A large $G^2$ (small $p$) means the model misfits *more than sampling noise can explain*.

<div dir="rtl">

با $0 \ln 0 = 0$. اگر مدل درست باشد و شمارش‌ها خیلی کوچک نباشند، $G^2$ تقریباً توزیع $\chi^2$ با $\text{df} = (\text{تعداد خانه‌ها}) - k$ دارد. $G^2$ بزرگ ($p$ کوچک) یعنی عدم برازش مدل *بیش از آن است که نویز نمونه‌گیری بتواند توضیح دهد*.

</div>

Caveats: with very large $N$, any small misfit becomes "significant"; with small $N$, real misfit can go undetected. A non-significant $G^2$ does **not** prove the model is right (Week 6).

<div dir="rtl">

هشدارها: با $N$ خیلی بزرگ، هر عدم برازش کوچکی «معنادار» می‌شود؛ با $N$ کوچک، عدم برازش واقعی ممکن است دیده نشود. یک $G^2$ غیرمعنادار **ثابت نمی‌کند** که مدل درست است (هفته‌ی 6).

</div>

#### Reading the math · خواندن ریاضی

- The **saturated model** is the "cheating" model that predicts every observed proportion exactly. Its log-likelihood is the best any model could possibly achieve on these data.
- $G^2 = 2(\ell_{\text{saturated}} - \ell(\hat{\boldsymbol\theta}))$ measures how far our model falls short of that ceiling. $G^2 = 0$ would be a perfect fit.
- **Degrees of freedom** = number of data cells − number of fitted parameters. With 8 intervals and 2 parameters, df = 6.
- If the model is true, $G^2$ behaves like a $\chi^2$ variable with that df, whose average is df. So $G^2 \approx 6$ with df = 6 is a normal amount of misfit (just noise); $G^2 = 26$ with df = 6 ($p = .0002$) means the model systematically misses the data.

<div dir="rtl">

- **مدل اشباع‌شده (saturated)** مدل «تقلب‌کننده»‌ای است که هر نسبت مشاهده‌شده را دقیقاً پیش‌بینی می‌کند. لگاریتم درست‌نمایی آن بهترین مقداری است که هر مدلی ممکن است روی این داده به دست آورد.
- $G^2 = 2(\ell_{\text{saturated}} - \ell(\hat{\boldsymbol\theta}))$ اندازه می‌گیرد مدل ما چقدر از این سقف فاصله دارد. $G^2 = 0$ یعنی برازش کامل.
- **درجه‌ی آزادی (df)** = تعداد خانه‌های داده − تعداد پارامترهای برازش‌شده. با 8 فاصله و 2 پارامتر، df = 6.
- اگر مدل درست باشد، $G^2$ مثل یک متغیر $\chi^2$ با همان df رفتار می‌کند که میانگینش df است. پس $G^2 \approx 6$ با df = 6 مقدار عادی عدم برازش است (فقط نویز)؛ $G^2 = 26$ با df = 6 ($p = .0002$) یعنی مدل به‌طور نظام‌مند داده را از دست می‌دهد.

</div>

### 6. Constrained models as hypotheses · 6. مدل‌های مقیدشده به‌عنوان فرضیه

MLE makes it easy to fit **several conditions at once with some parameters shared**. Example: an SDT experiment with three payoff conditions (rewarding "yes" responses, neutral, rewarding "no").

<div dir="rtl">

MLE برازش **چند شرط هم‌زمان با بعضی پارامترهای مشترک** را آسان می‌کند. مثال: یک آزمایش SDT با سه شرط پاداش (پاداش برای پاسخ «بله»، خنثی، پاداش برای «نه»).

</div>

| Model | Free parameters | $k$ | Hypothesis |
|---|---|---|---|
| Shared sensitivity | $d'$; $c_1, c_2, c_3$ | 4 | Payoffs change *bias* only |
| Separate | $d'_1, d'_2, d'_3$; $c_1, c_2, c_3$ | 6 | Payoffs may also change *sensitivity* (this is the saturated model for 6 rates) |

<div dir="rtl">

| مدل | پارامترهای آزاد | $k$ | فرضیه |
|---|---|---|---|
| حساسیت مشترک | $d'$؛ $c_1, c_2, c_3$ | 4 | پاداش فقط *سوگیری* را تغییر می‌دهد |
| جداگانه | $d'_1, d'_2, d'_3$؛ $c_1, c_2, c_3$ | 6 | پاداش ممکن است *حساسیت* را هم تغییر دهد (این مدل اشباع‌شده برای 6 نرخ است) |

</div>

The joint log-likelihood is the sum over conditions of the binomial log-likelihoods of hits and false alarms. Comparing the two models' maximized log-likelihoods tests a substantive question. With nested models like these, $2(\ell_{6} - \ell_{4})$ is approximately $\chi^2$ with 2 df: the **likelihood-ratio test**, developed in Week 7.

<div dir="rtl">

لگاریتم درست‌نمایی مشترک، مجموع لگاریتم درست‌نمایی‌های دوجمله‌ای hitها و false alarmها در همه‌ی شرایط است. مقایسه‌ی لگاریتم درست‌نمایی بیشینه‌ی دو مدل یک سؤال واقعی را آزمون می‌کند. برای مدل‌های nested مثل این‌ها، $2(\ell_{6} - \ell_{4})$ تقریباً $\chi^2$ با 2 درجه‌ی آزادی است: **آزمون نسبت درست‌نمایی** که در هفته‌ی 7 کامل می‌شود.

</div>

> **Advanced: SDT MLE and the formulas.** For a single condition, the MLE of $(d', c)$ from counts is exactly what the Week 2 formulas give *without* correction, because the model is saturated (2 parameters, 2 rates) and the MLE reproduces the observed rates. The log-linear correction is *not* MLE; it is closer to a Bayesian estimate with a weak prior (Week 9).

<div dir="rtl">

> **پیشرفته: MLE در SDT و فرمول‌ها.** برای یک شرط تنها، MLE $(d', c)$ از شمارش‌ها دقیقاً همان چیزی است که فرمول‌های هفته‌ی 2 *بدون* تصحیح می‌دهند، چون مدل اشباع‌شده است (2 پارامتر، 2 نرخ) و MLE نرخ‌های مشاهده‌شده را بازتولید می‌کند. تصحیح log-linear، MLE *نیست*؛ بیشتر به یک برآورد بیزی با پیشین ضعیف شبیه است (هفته‌ی 9).

</div>

#### For an engineer · برای یک مهندس

- This is **maximum-likelihood estimation** exactly as in estimation theory (ML channel or frequency estimation, ML sequence detection). The only change is the noise model: binomial counts instead of AWGN.
- **LS = ML under AWGN** (Section 4) is a result you already use: with white Gaussian noise of known, equal variance, the ML estimator minimizes the squared error.
- The **Fisher information** and the asymptotic variance of the MLE (Advanced box) are the same quantities as in the **Cramér–Rao lower bound**. Week 5 uses them to compute standard errors.
- Comparing a constrained and a free model with $2(\ell_{\text{free}} - \ell_{\text{constrained}})$ is the **generalized likelihood-ratio test (GLRT)**: both hypotheses have unknown parameters that are replaced by their ML estimates.
- **Payoffs and criterion shifts**: in Bayesian detection the optimal threshold moves with the costs and priors. Section 6 tests whether *people* move only their threshold ($c$) when the payoffs change, while their "SNR" ($d'$) stays the same.

<div dir="rtl">

- این دقیقاً همان **تخمین بیشینه‌ی درست‌نمایی** در نظریه‌ی تخمین است (تخمین ML کانال یا فرکانس، آشکارسازی دنباله با ML). تنها تفاوت مدل نویز است: شمارش دوجمله‌ای به جای AWGN.
- **LS = ML تحت AWGN** (بخش 4) نتیجه‌ای است که قبلاً از آن استفاده کرده‌اید: با نویز سفید گاوسی با واریانس معلوم و برابر، تخمین‌گر ML خطای مربعی را کمینه می‌کند.
- **اطلاعات فیشر (Fisher information)** و واریانس مجانبی MLE (کادر پیشرفته) همان کمیت‌های **کران پایین Cramér–Rao** هستند. هفته‌ی 5 از آن‌ها برای محاسبه‌ی خطای استاندارد استفاده می‌کند.
- مقایسه‌ی یک مدل مقید و یک مدل آزاد با $2(\ell_{\text{free}} - \ell_{\text{constrained}})$ همان **آزمون نسبت درست‌نمایی تعمیم‌یافته (GLRT)** است: هر دو فرضیه پارامترهای مجهول دارند که با تخمین ML جایگزین می‌شوند.
- **پاداش‌ها و جابه‌جایی ملاک:** در آشکارسازی بیزی، آستانه‌ی بهینه با هزینه‌ها و احتمال‌های پیشین جابه‌جا می‌شود. بخش 6 می‌آزماید که آیا *آدم‌ها* وقتی پاداش‌ها عوض می‌شوند فقط آستانه‌شان ($c$) را جابه‌جا می‌کنند و «SNR»شان ($d'$) ثابت می‌ماند.

</div>

#### For the instructor · برای مدرس

- **The one sentence to repeat:** "the likelihood is the probability of the data we observed, as a function of the parameters". Write it on the board and leave it there all session.
- **Plot it.** Draw $L(\theta)$ for 7 of 10 (worked example, Part 1) as a curve over $\theta$ from 0 to 1. Ask: where is the peak? Does the area under the curve equal 1? (No.) Then draw it for 70 of 100: same peak, much narrower curve. That narrowness is precision, the topic of Week 5.
- **Use your background.** Many students find MLE abstract; you can present it as "the estimation method engineers use when the noise is not Gaussian".
- **Typical questions.**
  - *"Is the likelihood the probability that $\theta$ is correct?"* No. That needs a prior (Week 9).
  - *"Why minimize NLL instead of maximizing $L$?"* Same answer, but sums of logs avoid numerical underflow, and optimizers are written to minimize.
  - *"Is a non-significant $G^2$ proof the model is right?"* No: it only means the misfit is not larger than the noise, and with few data, real misfit can hide.
- **Time management.** Section 4 (Gaussian case) can be shown quickly as "LS is a special case". Spend the saved time on Section 5 ($G^2$).

<div dir="rtl">

- **جمله‌ای که باید تکرار کنید:** «درست‌نمایی احتمال داده‌ای است که مشاهده کرده‌ایم، به‌عنوان تابعی از پارامترها». آن را روی تخته بنویسید و تا آخر جلسه نگه دارید.
- **رسمش کنید.** $L(\theta)$ را برای 7 از 10 (مثال حل‌شده، بخش 1) به شکل منحنی روی $\theta$ از 0 تا 1 بکشید. بپرسید: قله کجاست؟ آیا مساحت زیر منحنی 1 است؟ (نه.) بعد آن را برای 70 از 100 بکشید: همان قله، منحنی خیلی باریک‌تر. این باریکی همان دقت (precision) است، موضوع هفته‌ی 5.
- **از پیش‌زمینه‌ی خودتان استفاده کنید.** خیلی از دانشجوها MLE را انتزاعی می‌دانند؛ شما می‌توانید آن را به‌عنوان «روش تخمینی که مهندس‌ها وقتی نویز گاوسی نیست به کار می‌برند» معرفی کنید.
- **سؤال‌های رایج.**
  - *«آیا درست‌نمایی احتمال درست بودن $\theta$ است؟»* نه. برای آن به prior نیاز داریم (هفته‌ی 9).
  - *«چرا NLL را کمینه می‌کنیم به جای اینکه $L$ را بیشینه کنیم؟»* جواب یکی است، ولی جمع لگاریتم‌ها از underflow عددی جلوگیری می‌کند و بهینه‌سازها برای کمینه کردن نوشته شده‌اند.
  - *«آیا $G^2$ غیرمعنادار ثابت می‌کند مدل درست است؟»* نه؛ فقط یعنی عدم برازش بیشتر از نویز نیست، و با داده‌ی کم ممکن است عدم برازش واقعی پنهان بماند.
- **مدیریت زمان.** بخش 4 (حالت گاوسی) را می‌شود سریع به‌عنوان «LS حالت خاصی است» نشان داد. وقت صرفه‌جویی‌شده را روی بخش 5 ($G^2$) بگذارید.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: likelihood of a single proportion · بخش 1: درست‌نمایی یک نسبت تنها

$y = 7$ recalled out of $n = 10$:

<div dir="rtl">

$y = 7$ یادآوری از $n = 10$:

</div>

| $\theta$ | 0.5 | 0.6 | **0.7** | 0.8 |
|---|---|---|---|---|
| $L(\theta) = \binom{10}{7}\theta^7(1-\theta)^3$ | 0.117 | 0.215 | **0.267** | 0.201 |
| $\ell(\theta)$ | −2.144 | −1.537 | **−1.321** | −1.603 |

<div dir="rtl">

| $\theta$ | 0.5 | 0.6 | **0.7** | 0.8 |
|---|---|---|---|---|
| $L(\theta) = \binom{10}{7}\theta^7(1-\theta)^3$ | 0.117 | 0.215 | **0.267** | 0.201 |
| $\ell(\theta)$ | −2.144 | −1.537 | **−1.321** | −1.603 |

</div>

The maximum is at $\hat\theta = 7/10 = 0.7$. Note that the likelihood values do not sum to 1 across $\theta$: likelihood is not a probability distribution over parameters.

<div dir="rtl">

بیشینه در $\hat\theta = 7/10 = 0.7$ است. دقت کنید که مقادیر درست‌نمایی روی $\theta$ جمعشان 1 نمی‌شود: درست‌نمایی توزیع احتمال روی پارامترها نیست.

</div>

### Part 2: a two-interval forgetting experiment · بخش 2: یک آزمایش فراموشی دوفاصله‌ای

$y = (30, 13)$ items recalled out of $n = 50$ at $t = (1, 7)$ days. Model: $f(t) = A e^{-\lambda t}$.

<div dir="rtl">

$y = (30, 13)$ آیتم یادآوری‌شده از $n = 50$ در $t = (1, 7)$ روز. مدل: $f(t) = A e^{-\lambda t}$.

</div>

**Step 1: NLL for a candidate.** For $(A, \lambda) = (0.70, 0.15)$: $f(1) = 0.7e^{-0.15} = 0.6025$, $f(7) = 0.7e^{-1.05} = 0.2450$.

<div dir="rtl">

**قدم 1: NLL برای یک نامزد.** برای $(A, \lambda) = (0.70, 0.15)$: $f(1) = 0.7e^{-0.15} = 0.6025$، $f(7) = 0.7e^{-1.05} = 0.2450$.

</div>

$$
\ell = \ln\mathrm{Binom}(30; 50, 0.6025) + \ln\mathrm{Binom}(13; 50, 0.2450) = -2.167 + (-2.088) = -4.255,
$$

so NLL $= 4.255$.

<div dir="rtl">

پس NLL $= 4.255$.

</div>

**Step 2: compare.** For $(0.70, 0.12)$: $f = (0.621, 0.302)$ and NLL $= 4.488$, which is worse. The first candidate makes the data more probable.

<div dir="rtl">

**قدم 2: مقایسه.** برای $(0.70, 0.12)$: $f = (0.621, 0.302)$ و NLL $= 4.488$ که بدتر است. نامزد اول داده‌ها را محتمل‌تر می‌کند.

</div>

**Step 3: the MLE.** With 2 parameters and 2 data points the model can match both observed proportions exactly: $A e^{-\lambda} = 0.60$ and $A e^{-7\lambda} = 0.26$. Dividing gives $e^{6\lambda} = 0.60/0.26$, so $\hat\lambda = \ln(2.308)/6 = 0.139$ and $\hat A = 0.60\,e^{0.139} = 0.690$, with NLL $= 4.225$ (the minimum). A numerical optimizer gives the same values.

<div dir="rtl">

**قدم 3: MLE.** با 2 پارامتر و 2 داده، مدل می‌تواند هر دو نسبت مشاهده‌شده را دقیقاً بازتولید کند: $A e^{-\lambda} = 0.60$ و $A e^{-7\lambda} = 0.26$. تقسیم این دو می‌دهد $e^{6\lambda} = 0.60/0.26$، پس $\hat\lambda = \ln(2.308)/6 = 0.139$ و $\hat A = 0.60\,e^{0.139} = 0.690$، با NLL $= 4.225$ (کمینه). یک بهینه‌ساز عددی همین مقادیر را می‌دهد.

</div>

**Interpretation.** The MLE says this participant recalls about 69% at the start and loses about 13% of what remains per day ($1 - e^{-0.139}$). Because $k = N$ here, $G^2 = 0$: the model *cannot* misfit, so the perfect fit carries no evidence for the exponential form. Only data with more cells than parameters can test a model.

<div dir="rtl">

**تفسیر.** MLE می‌گوید این شرکت‌کننده در شروع حدود 69% را به یاد می‌آورد و هر روز حدود 13% از باقی‌مانده را از دست می‌دهد ($1 - e^{-0.139}$). چون اینجا $k = N$ است، $G^2 = 0$: مدل *نمی‌تواند* بد برازش شود، پس این برازش کامل هیچ شاهدی برای شکل نمایی نیست. فقط داده‌هایی با تعداد خانه‌ی بیشتر از تعداد پارامترها می‌توانند یک مدل را آزمون کنند.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Plot a likelihood function and see why we work with log-likelihoods.
2. Fit exponential and power forgetting models by MLE; compare with least squares; evaluate with $G^2$.
3. Verify numerically that Gaussian MLE equals least squares.
4. Fit a constrained multi-condition SDT model and **interpret** what it says about payoffs.

<div dir="rtl">

1. رسم یک تابع درست‌نمایی و دیدن اینکه چرا با لگاریتم درست‌نمایی کار می‌کنیم.
2. برازش مدل‌های فراموشی نمایی و توانی با MLE؛ مقایسه با کمترین مربعات؛ ارزیابی با $G^2$.
3. وارسی عددی اینکه MLE گاوسی با کمترین مربعات برابر است.
4. برازش یک مدل SDT چندشرطی مقیدشده و **تفسیر** آنچه درباره‌ی پاداش‌ها می‌گوید.

</div>

**Timing:** Part A 15 min · Part B 35 min · Part C 15 min · Part D 35 min · Part E 20 min (exercises).

<div dir="rtl">

**زمان‌بندی:** بخش A 15 دقیقه · بخش B 35 دقیقه · بخش C 15 دقیقه · بخش D 35 دقیقه · بخش E 20 دقیقه (تمرین‌ها).

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 1 · سلول 1

### Part A: the likelihood function (15 min) · بخش A: تابع درست‌نمایی (15 دقیقه)

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Area under L(theta): 0.091 (not 1: L is not a distribution over theta)
Product of 2000 trial probabilities: 0.0
Sum of their logs: -1239.52
```

### Part B: MLE for forgetting curves (35 min) · بخش B: MLE برای منحنی‌های فراموشی (35 دقیقه)

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
model method      A   rate     NLL    SSE
  exp    MLE 0.6377 0.0458 29.8123 0.1100
  exp     LS 0.6568 0.0566 30.6983 0.1061
  pow    MLE 0.8773 0.4214 19.8303 0.0262
  pow     LS 0.8712 0.4251 19.8585 0.0259
True (power): A = 0.9, d = 0.5
```

**What to notice:**
- Each method wins on its *own* criterion: MLE has the lowest NLL, LS the lowest SSE.
- For the (true) power model the two methods agree closely.
- For the exponential model the two methods differ more (decay rate 0.046 vs. 0.057). The binomial likelihood gives more weight to the precisely measured points near the floor (long delays), so the ML curve decays more slowly in order to stay closer to them.

<div dir="rtl">

**به این‌ها دقت کنید:**
- هر روش در معیار *خودش* برنده است: MLE کمترین NLL و LS کمترین SSE را دارد.
- برای مدل توانی (مدل واقعی) دو روش خیلی به هم نزدیک‌اند.
- برای مدل نمایی دو روش بیشتر با هم فرق دارند (نرخ زوال 0.046 در برابر 0.057). درست‌نمایی دوجمله‌ای به نقاطی که نزدیک کف دقیق اندازه‌گیری شده‌اند (فاصله‌های طولانی) وزن بیشتری می‌دهد، پس منحنی ML کندتر زوال پیدا می‌کند تا به آن‌ها نزدیک‌تر بماند.

</div>

> **Warning: a real optimizer trap.** Replace `"L-BFGS-B"` with `"Nelder-Mead"` in the ML fit above (keeping `bounds=bounds`) and rerun. For the exponential model, scipy's bounded Nelder–Mead collapses against the bound `A = 1` and reports `success` with NLL = 79.5, far worse than the true minimum of 29.8 (it is even worse than the LS estimate's NLL). Bounded simplex methods can degenerate when vertices are pushed onto a bound. Two quick checks would catch this: an estimate sitting exactly on a bound, and a "MLE" whose NLL is *higher* than that of some other parameter values you have tried. Multi-start (Week 3) is the general cure.

<div dir="rtl">

> **هشدار: یک دام واقعی بهینه‌ساز.** در برازش ML بالا `"L-BFGS-B"` را با `"Nelder-Mead"` عوض کنید (با نگه داشتن `bounds=bounds`) و دوباره اجرا کنید. برای مدل نمایی، Nelder–Mead کران‌دار scipy روی کران `A = 1` فرو می‌ریزد و با NLL = 79.5 «`success`» گزارش می‌کند؛ خیلی بدتر از کمینه‌ی واقعی 29.8 (حتی بدتر از NLL برآورد LS). روش‌های سیمپلکس کران‌دار وقتی رأس‌ها روی یک کران فشرده شوند ممکن است تباهیده (degenerate) شوند. دو بررسی سریع این را لو می‌دهند: برآوردی که دقیقاً روی یک کران نشسته، و یک «MLE» که NLL آن از مقادیر پارامتر دیگری که امتحان کرده‌اید *بیشتر* است. multi-start (هفته‌ی 3) درمان کلی آن است.

</div>

Now evaluate absolute fit with the deviance:

<div dir="rtl">

حالا برازش مطلق را با انحراف ارزیابی کنید:

</div>

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
exp: G2 =  26.27, df = 6, p = 0.0002
pow: G2 =   6.31, df = 6, p = 0.3895
```

**Interpret:** the exponential model misfits far more than binomial noise allows ($p = .0002$): we can **reject** it as a description of these data. The power model's misfit is consistent with sampling noise. That does not prove it is the right model; it means these data give no reason to reject it.

<div dir="rtl">

**تفسیر:** عدم برازش مدل نمایی خیلی بیشتر از آن است که نویز دوجمله‌ای اجازه می‌دهد ($p = .0002$): می‌توانیم آن را به‌عنوان توصیف این داده‌ها **رد کنیم**. عدم برازش مدل توانی با نویز نمونه‌گیری سازگار است. این ثابت نمی‌کند که مدل درستی است؛ یعنی این داده‌ها دلیلی برای رد آن نمی‌دهند.

</div>

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 5 · سلول 5

### Part C: Gaussian MLE equals least squares (15 min) · بخش C: MLE گاوسی همان کمترین مربعات است (15 دقیقه)

Treat the proportions as continuous and assume Gaussian noise with a free $\sigma$ (a third parameter). The estimates of $A$ and $d$ should match least squares, and $\hat\sigma$ should equal $\sqrt{\mathrm{SSE}/N}$.

<div dir="rtl">

نسبت‌ها را پیوسته در نظر بگیرید و نویز گاوسی با $\sigma$ آزاد (پارامتر سوم) فرض کنید. برآوردهای $A$ و $d$ باید با کمترین مربعات یکی باشند و $\hat\sigma$ باید برابر $\sqrt{\mathrm{SSE}/N}$ باشد.

</div>

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Gaussian MLE: A = 0.8712, d = 0.4251, sigma = 0.0569
Least squares: A = 0.8711, d = 0.4251, sqrt(SSE/N) = 0.0569
```

### Part D: a constrained multi-condition SDT model (35 min) · بخش D: یک مدل SDT چندشرطی مقیدشده (35 دقیقه)

**The experiment.** Participants detect a faint tone under three payoff schemes: **liberal** (hits rewarded), **neutral**, and **conservative** (false alarms penalized). 80 signal and 80 noise trials per condition. We simulate one participant whose sensitivity is the same in all conditions and whose criterion shifts with the payoffs.

<div dir="rtl">

**آزمایش.** شرکت‌کننده‌ها یک صدای ضعیف را تحت سه طرح پاداش تشخیص می‌دهند: **liberal** (پاداش برای hit)، **خنثی** و **محافظه‌کار** (جریمه برای false alarm). در هر شرط 80 trial علامت و 80 trial نویز. یک شرکت‌کننده را شبیه‌سازی می‌کنیم که حساسیتش در همه‌ی شرایط یکسان است و ملاکش با پاداش جابه‌جا می‌شود.

</div>

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 7 · سلول 7

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
      condition  hits  n_signal  fas  n_noise
0       liberal    73        80   33       80
1       neutral    58        80   16       80
2  conservative    44        80    7       80

Shared d':   d' = 1.496, c = [-0.555  0.124  0.618], NLL = 13.134
Separate d': d' = [1.577 1.439 1.482], c = [-0.568  0.122  0.615], NLL = 13.043

Likelihood-ratio statistic = 0.18, df = 2, p = 0.913
```

Note that the estimated `d'` (about 1.5) is higher than the generating value of 1.2. With 80 trials per cell that is ordinary sampling error. Week 5 shows how to put a confidence interval around it.

<div dir="rtl">

دقت کنید که `d'` برآوردشده (حدود 1.5) از مقدار تولیدکننده‌ی 1.2 بیشتر است. با 80 trial در هر خانه این یک خطای نمونه‌گیری عادی است. هفته‌ی 5 نشان می‌دهد چطور دور آن بازه‌ی اطمینان بسازیم.

</div>

**Interpret (write in your notebook):**
1. Does constraining $d'$ to be equal across payoff conditions cost much likelihood? What do you conclude about the effect of payoffs?
2. The separate-$d'$ estimates differ from each other by a few tenths. Why is that not evidence that payoffs change sensitivity?
3. Check that the separate-$d'$ model reproduces the observed hit and false-alarm rates exactly. Why must it?

<div dir="rtl">

**تفسیر (در notebook بنویسید):**
1. آیا مقید کردن $d'$ به برابری در همه‌ی شرایط پاداش درست‌نمایی زیادی را هزینه می‌کند؟ درباره‌ی اثر پاداش‌ها چه نتیجه‌ای می‌گیرید؟
2. برآوردهای $d'$ جداگانه چند دهم با هم فرق دارند. چرا این شاهدی بر اینکه پاداش حساسیت را تغییر می‌دهد نیست؟
3. بررسی کنید که مدل $d'$ جداگانه نرخ‌های hit و false alarm مشاهده‌شده را دقیقاً بازتولید می‌کند. چرا باید این‌طور باشد؟

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Derive by hand the MLE of $\theta$ for a Bernoulli sequence with $y$ successes in $n$ trials, and check it numerically with `minimize_scalar` for $y = 13$, $n = 40$.

<div dir="rtl">

**تمرین 1 ★.** MLE $\theta$ را برای یک دنباله‌ی برنولی با $y$ موفقیت در $n$ trial با دست استخراج کنید و آن را برای $y = 13$، $n = 40$ با `minimize_scalar` عددی بررسی کنید.

</div>

**Exercise 2 ★.** In Part B, refit both models with the **Bernoulli** likelihood on item-level data (expand each count into 0/1 responses). Show that the estimates are identical to the binomial fits and that the NLLs differ by a constant. What is the constant?

<div dir="rtl">

**تمرین 2 ★.** در بخش B، هر دو مدل را با درست‌نمایی **برنولی** روی داده‌ی سطح آیتم دوباره برازش کنید (هر شمارش را به پاسخ‌های 0/1 باز کنید). نشان دهید برآوردها با برازش‌های دوجمله‌ای یکسان‌اند و NLLها به اندازه‌ی یک ثابت فرق دارند. آن ثابت چیست؟

</div>

**Exercise 3 ★★ (zero counts).** Set the last two counts to 0 (`recalled[-2:] = 0`). Which fitting methods from Weeks 2–4 still work? Fit both models by MLE and comment on what happens to the estimates and to $G^2$.

<div dir="rtl">

**تمرین 3 ★★ (شمارش صفر).** دو شمارش آخر را 0 کنید (`recalled[-2:] = 0`). کدام روش‌های برازش هفته‌های 2–4 هنوز کار می‌کنند؟ هر دو مدل را با MLE برازش کنید و درباره‌ی آنچه بر سر برآوردها و $G^2$ می‌آید توضیح دهید.

</div>

**Exercise 4 ★★ (a third SDT model).** Fit a model in which the criterion is the *same* in all conditions but $d'$ differs ($k = 4$). Compare its NLL with the shared-$d'$ model. Both have $k = 4$; why can you compare them directly by NLL here? Which one is psychologically more plausible for a payoff manipulation?

<div dir="rtl">

**تمرین 4 ★★ (یک مدل SDT سوم).** مدلی را برازش کنید که در آن ملاک در همه‌ی شرایط *یکسان* است ولی $d'$ فرق دارد ($k = 4$). NLL آن را با مدل $d'$ مشترک مقایسه کنید. هر دو $k = 4$ دارند؛ چرا اینجا می‌توانید مستقیماً با NLL مقایسه کنید؟ کدام برای یک دست‌کاری پاداش از نظر روان‌شناختی معقول‌تر است؟

</div>

**Exercise 5 ★★★ (Advanced: LS vs. MLE by simulation).** Simulate 500 datasets from the power model ($A = 0.9$, $d = 0.5$, the 8 intervals, $n = 50$), fit each by LS and by MLE, and compare the two estimators of $d$: mean (bias), SD, and root-mean-squared error. Which is better here? Repeat with $n = 10$. (This is good preparation for A2.)

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: LS در برابر MLE با شبیه‌سازی).** 500 مجموعه‌داده از مدل توانی ($A = 0.9$، $d = 0.5$، همان 8 فاصله، $n = 50$) شبیه‌سازی کنید، هرکدام را با LS و با MLE برازش کنید و دو برآوردگر $d$ را مقایسه کنید: میانگین (سوگیری)، انحراف معیار، و ریشه‌ی میانگین مربع خطا. کدام اینجا بهتر است؟ با $n = 10$ تکرار کنید. (آمادگی خوبی برای A2 است.)

</div>

### Lab check-off · lab check-off

Show: (1) the LS-vs-MLE table and $G^2$ results from Part B, (2) the Gaussian-vs-LS comparison from Part C, and (3) your answers to the interpretation questions of Part D.

<div dir="rtl">

نشان دهید: (1) جدول LS در برابر MLE و نتایج $G^2$ از بخش B، (2) مقایسه‌ی گاوسی در برابر LS از بخش C، و (3) پاسخ‌هایتان به سؤال‌های تفسیری بخش D.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**LLMs are trained by maximum likelihood.** The "cross-entropy loss" used to train every language model is the negative log-likelihood of the next token, averaged over a huge text corpus. Training an LLM is therefore an MLE problem with billions of parameters, solved by gradient descent instead of Nelder–Mead. Two quantities you meet in AI papers are this week's quantities in disguise: **loss** = NLL per token, and **perplexity** = $e^{\text{NLL per token}}$, the effective number of equally likely choices the model is "confused" between.

<div dir="rtl">

**LLMها با بیشینه‌ی درست‌نمایی آموزش می‌بینند.** «cross-entropy loss» که برای آموزش همه‌ی مدل‌های زبانی استفاده می‌شود، همان منفی لگاریتم درست‌نمایی token بعدی است که روی یک corpus متنی عظیم میانگین گرفته شده. پس آموزش یک LLM یک مسئله‌ی MLE با میلیاردها پارامتر است که به جای Nelder–Mead با gradient descent حل می‌شود. دو کمیتی که در مقاله‌های هوش مصنوعی می‌بینید همان کمیت‌های این هفته در لباس دیگرند: **loss** = NLL برای هر token، و **perplexity** = $e^{\text{NLL per token}}$، یعنی تعداد مؤثر گزینه‌های هم‌احتمالی که مدل بینشان «سردرگم» است.

</div>

The simplest language model, a **bigram model**, has a closed-form MLE: $P(w_2\mid w_1)$ = count($w_1 w_2$)/count($w_1$). It shows a familiar problem. Any word pair never seen in training gets probability 0, so a single new pair makes the likelihood of a whole sentence 0 (NLL = ∞). Smoothing solves this, in the same way that the log-linear correction of Week 2 solved hit rates of 1.

<div dir="rtl">

ساده‌ترین مدل زبانی، یعنی **مدل bigram**، یک MLE بسته دارد: $P(w_2\mid w_1)$ = count($w_1 w_2$)/count($w_1$). این مدل یک مشکل آشنا را نشان می‌دهد. هر جفت کلمه‌ای که در آموزش دیده نشده احتمال 0 می‌گیرد، پس فقط یک جفت تازه درست‌نمایی کل جمله را 0 می‌کند (NLL = ∞). هموارسازی (smoothing) این را حل می‌کند، همان‌طور که تصحیح log-linear هفته‌ی 2 مشکل نرخ hit 1 را حل کرد.

</div>

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 8 · سلول 8

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
P(cat | the) = 0.333
'the dog sat on the mat .'   MLE      NLL =  3.584  perplexity =   1.82
'the dog sat on the mat .'   add-one  NLL =  9.537  perplexity =   4.90
'the dog saw the cat .'      MLE      NLL =    inf  perplexity =    inf
'the dog saw the cat .'      add-one  NLL =  9.624  perplexity =   6.85
```

**Try it (no API needed).**
- ★ Which word pair in "the dog saw the cat ." was never seen in the corpus? Check by hand that the MLE of $P(\text{cat}\mid\text{the})$ is 1/3.
- ★★ Smoothing makes the *training* sentence less likely (NLL 3.6 → 9.5) but makes the new sentence possible. Replace add-one with add-$k$ and choose $k$ by leave-one-sentence-out cross-validation (a preview of Week 6).
- ★★ Discussion: the MLE of a bigram model reproduces the training corpus as closely as possible. Why is "maximizing likelihood on internet text" not the same as "learning to tell the truth"?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ کدام جفت کلمه در «the dog saw the cat .» هرگز در corpus دیده نشده؟ با دست بررسی کنید که MLE برای $P(\text{cat}\mid\text{the})$ برابر 1/3 است.
- ★★ هموارسازی جمله‌ی *آموزشی* را کم‌احتمال‌تر می‌کند (NLL از 3.6 به 9.5) ولی جمله‌ی تازه را ممکن می‌کند. add-one را با add-$k$ عوض کنید و $k$ را با cross-validation leave-one-sentence-out انتخاب کنید (پیش‌نمایشی از هفته‌ی 6).
- ★★ بحث: MLE یک مدل bigram corpus آموزشی را تا جای ممکن بازتولید می‌کند. چرا «بیشینه کردن درست‌نمایی روی متن اینترنت» با «یاد گرفتن راست‌گویی» یکی نیست؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **"The likelihood is the probability that the parameters are true."** It is the probability (density) of the *data* given the parameters. It does not integrate to 1 over $\boldsymbol\theta$.
2. **Multiplying probabilities instead of summing logs.** The product underflows to 0 for realistic numbers of trials (Part A).
3. **Maximizing when the optimizer minimizes.** `minimize` needs the **negative** log-likelihood. Forgetting the minus sign sends the optimizer to the *worst* parameters.
4. **Not clipping probabilities.** Predicted probabilities of exactly 0 or 1 produce $-\infty$ log-likelihoods and crash the optimizer.
5. **Comparing NLLs across different datasets or data codings.** NLL depends on the number of observations and on constants (e.g., binomial coefficients). Compare only models fitted to the same data, coded the same way.
6. **Using least squares for choices or counts by default.** It ignores the data's noise structure. Use the likelihood that matches how the data were generated.
7. **Reading a non-significant $G^2$ as proof the model is correct.** It only says the misfit is not detectably larger than sampling noise at this sample size.
8. **Forgetting that a saturated or exactly-determined model always fits perfectly** (worked example, Part D separate-$d'$ model). A perfect fit is then uninformative.

<div dir="rtl">

1. **«درست‌نمایی احتمال درست بودن پارامترهاست.»** احتمال (چگالی) *داده* به شرط پارامترهاست. انتگرالش روی $\boldsymbol\theta$ برابر 1 نیست.
2. **ضرب کردن احتمال‌ها به‌جای جمع کردن لگاریتم‌ها.** حاصل‌ضرب برای تعداد trial واقعی به 0 سرریز می‌کند (بخش A).
3. **بیشینه کردن وقتی بهینه‌ساز کمینه می‌کند.** `minimize` به **منفی** لگاریتم درست‌نمایی نیاز دارد. فراموش کردن علامت منفی بهینه‌ساز را به *بدترین* پارامترها می‌فرستد.
4. **محدود نکردن احتمال‌ها.** احتمال‌های پیش‌بینی‌شده‌ی دقیقاً 0 یا 1 لگاریتم درست‌نمایی $-\infty$ می‌دهند و بهینه‌ساز را از کار می‌اندازند.
5. **مقایسه‌ی NLL بین مجموعه‌داده‌ها یا کدگذاری‌های مختلف.** NLL به تعداد مشاهدات و ثابت‌ها (مثلاً ضرایب دوجمله‌ای) بستگی دارد. فقط مدل‌هایی را مقایسه کنید که روی همان داده با همان کدگذاری برازش شده‌اند.
6. **استفاده‌ی پیش‌فرض از کمترین مربعات برای انتخاب‌ها یا شمارش‌ها.** ساختار نویز داده را نادیده می‌گیرد. از درست‌نمایی‌ای استفاده کنید که با نحوه‌ی تولید داده جور باشد.
7. **خواندن $G^2$ غیرمعنادار به‌عنوان اثبات درستی مدل.** فقط می‌گوید عدم برازش با این حجم نمونه به‌طور قابل تشخیصی از نویز نمونه‌گیری بیشتر نیست.
8. **فراموش کردن اینکه مدل اشباع‌شده یا دقیقاً تعیین‌شده همیشه کامل برازش می‌شود** (مثال حل‌شده، مدل $d'$ جداگانه در بخش D). در این حالت برازش کامل بی‌اطلاع است.

</div>

---

## Check your understanding · خودآزمایی

**1.** In one sentence each: what varies and what is fixed in a probability distribution vs. a likelihood function?
<details><summary>Answer</summary>
Probability: parameters fixed, data vary, and it sums/integrates to 1 over data. Likelihood: data fixed at the observed values, parameters vary, and it need not integrate to 1 over parameters.
</details>

<div dir="rtl">

**1.** هرکدام در یک جمله: در یک توزیع احتمال در برابر یک تابع درست‌نمایی چه چیزی متغیر و چه چیزی ثابت است؟
<details><summary>پاسخ</summary>
احتمال: پارامترها ثابت، داده متغیر، و جمع/انتگرالش روی داده 1 است. درست‌نمایی: داده روی مقادیر مشاهده‌شده ثابت، پارامترها متغیر، و لازم نیست انتگرالش روی پارامترها 1 باشد.
</details>

</div>

**2.** Give two reasons for working with log-likelihoods.
<details><summary>Answer</summary>
(i) Numerical: products of many probabilities underflow, while sums of logs do not. (ii) The log is monotone, so the maximizer is unchanged, and sums are easier to differentiate and optimize.
</details>

<div dir="rtl">

**2.** دو دلیل برای کار با لگاریتم درست‌نمایی بیاورید.
<details><summary>پاسخ</summary>
(1) عددی: حاصل‌ضرب احتمال‌های زیاد سرریز می‌کند ولی مجموع لگاریتم‌ها نه. (2) لگاریتم monotone است، پس بیشینه‌کننده عوض نمی‌شود، و مشتق‌گیری و بهینه‌سازی مجموع‌ها راحت‌تر است.
</details>

</div>

**3.** Under what assumptions is least squares equivalent to maximum likelihood? Show the key step.
<details><summary>Answer</summary>
Independent Gaussian errors with equal variance $\sigma^2$. Then $\ell = -\tfrac{N}{2}\ln(2\pi\sigma^2) - \mathrm{SSE}/(2\sigma^2)$, so for any $\sigma$, maximizing $\ell$ over $\boldsymbol\theta$ is minimizing SSE.
</details>

<div dir="rtl">

**3.** تحت چه فرض‌هایی کمترین مربعات با بیشینه درست‌نمایی معادل است؟ گام کلیدی را نشان دهید.
<details><summary>پاسخ</summary>
خطاهای گاوسی مستقل با واریانس برابر $\sigma^2$. آن‌وقت $\ell = -\tfrac{N}{2}\ln(2\pi\sigma^2) - \mathrm{SSE}/(2\sigma^2)$، پس برای هر $\sigma$، بیشینه کردن $\ell$ روی $\boldsymbol\theta$ همان کمینه کردن SSE است.
</details>

</div>

**4.** A model with 2 parameters is fitted to 8 binomial cells and gives $G^2 = 4.1$. What are the df, and what do you conclude?
<details><summary>Answer</summary>
df = 8 − 2 = 6. A $\chi^2_6$ has mean 6, so 4.1 is well within the range expected from sampling noise ($p \approx 0.66$). There is no evidence of misfit, but that does not prove the model correct.
</details>

<div dir="rtl">

**4.** یک مدل 2 پارامتری روی 8 خانه‌ی دوجمله‌ای برازش شده و $G^2 = 4.1$ می‌دهد. درجه‌ی آزادی چند است و چه نتیجه‌ای می‌گیرید؟
<details><summary>پاسخ</summary>
df = 8 − 2 = 6. میانگین $\chi^2_6$ برابر 6 است، پس 4.1 کاملاً در دامنه‌ی مورد انتظار از نویز نمونه‌گیری است ($p \approx 0.66$). شاهدی بر عدم برازش نیست، ولی این درستی مدل را ثابت نمی‌کند.
</details>

</div>

**5.** Why does MLE with a binomial likelihood weight data points differently than plain least squares does?
<details><summary>Answer</summary>
The binomial log-likelihood reflects the variance $f(1-f)/n$: points predicted near 0 or 1 (small variance) are fitted more tightly, and points with larger $n$ count more. Plain least squares weights every squared error equally.
</details>

<div dir="rtl">

**5.** چرا MLE با درست‌نمایی دوجمله‌ای نقاط داده را متفاوت از کمترین مربعات ساده وزن می‌دهد؟
<details><summary>پاسخ</summary>
لگاریتم درست‌نمایی دوجمله‌ای واریانس $f(1-f)/n$ را منعکس می‌کند: نقاطی که پیش‌بینی می‌شود نزدیک 0 یا 1 باشند (واریانس کم) دقیق‌تر برازش می‌شوند، و نقاط با $n$ بزرگ‌تر بیشتر حساب می‌شوند. کمترین مربعات ساده همه‌ی مربع خطاها را یکسان وزن می‌دهد.
</details>

</div>

**6.** In the payoff experiment, what psychological hypothesis does the shared-$d'$ model express, and how would you test it?
<details><summary>Answer</summary>
That payoffs change only response bias (criterion), not perceptual sensitivity. Test it by comparing the maximized log-likelihood with the separate-$d'$ model: $2(\ell_6 - \ell_4) \sim \chi^2_2$ approximately (likelihood-ratio test), or with AIC/BIC (Week 7).
</details>

<div dir="rtl">

**6.** در آزمایش پاداش، مدل $d'$ مشترک چه فرضیه‌ی روان‌شناختی را بیان می‌کند و چطور آزمونش می‌کنید؟
<details><summary>پاسخ</summary>
اینکه پاداش‌ها فقط سوگیری پاسخ (ملاک) را تغییر می‌دهند، نه حساسیت ادراکی را. با مقایسه‌ی لگاریتم درست‌نمایی بیشینه با مدل $d'$ جداگانه آزمونش کنید: $2(\ell_6 - \ell_4) \sim \chi^2_2$ تقریبی (آزمون نسبت درست‌نمایی)، یا با AIC/BIC (هفته‌ی 7).
</details>

</div>

**7.** You fit a model and the optimizer returns NLL = −35.2 (negative). Is something wrong?
<details><summary>Answer</summary>
Not necessarily. For continuous data, densities can exceed 1 (e.g., a narrow Gaussian), so log-densities can be positive and the NLL negative. For discrete data (binomial), probabilities are ≤ 1, so the NLL must be ≥ 0, and a negative value would indicate a bug.
</details>

<div dir="rtl">

**7.** مدلی را برازش می‌کنید و بهینه‌ساز NLL = −35.2 (منفی) برمی‌گرداند. آیا اشکالی هست؟
<details><summary>پاسخ</summary>
نه لزوماً. برای داده‌ی پیوسته، چگالی‌ها می‌توانند از 1 بیشتر باشند (مثلاً یک گاوسی باریک)، پس لگاریتم چگالی می‌تواند مثبت و NLL منفی باشد. برای داده‌ی گسسته (دوجمله‌ای) احتمال‌ها ≤ 1 هستند، پس NLL باید ≥ 0 باشد و مقدار منفی نشانه‌ی باگ است.
</details>

</div>

---

## Assignment · تکلیف

### A2: Least squares vs. maximum likelihood (1.0 point of 20; released Week 4, due at the start of the Week 6 lecture) · A2: کمترین مربعات در برابر بیشینه درست‌نمایی (1.0 نمره از 20؛ انتشار هفته‌ی 4، موعد ابتدای درس هفته‌ی 6)

**Data.** Generate the dataset with exactly this code (everyone gets the same data):

<div dir="rtl">

**داده.** مجموعه‌داده را دقیقاً با این کد بسازید (همه داده‌ی یکسانی می‌گیرند):

</div>

> **Code · کد:** [`code/week04.py`](code/week04.py), cell 9 · سلول 9

**Tasks.**

<div dir="rtl">

**کارها.**

</div>

1. **Fit (2 pts).** Fit the exponential and power models to these data by (a) least squares on proportions and (b) binomial MLE. Report all estimates in one table with SSE and NLL.
2. **Evaluate (2 pts).** Compute $G^2$, df and $p$ for each model's MLE fit. Plot the data with 95% binomial intervals, both fitted curves, and residuals. Which model, if any, can be rejected?
3. **Simulation study (3 pts).** Treat the power model with $A = 0.95$, $d = 0.7$ as the truth. Simulate 500 datasets with the same design, fit each with LS and MLE, and report the bias, SD and RMSE of $\hat d$ for each method. Show histograms. Repeat with $n = 100$ items and describe what changes.
4. **Interpret (2 pts, max. 300 words).** Which estimator would you recommend for recall data, and why? Relate your answer to the noise structure of binomial data and to the near-floor counts (1–2 of 20) at the longest delays. What would happen to the Week 2 linearization method if one of those counts were 0?
5. **Code quality (1 pt).** Reproducible, commented notebook; seeds fixed; functions reused rather than copy-pasted.

<div dir="rtl">

1. **برازش (2 امتیاز).** مدل‌های نمایی و توانی را روی این داده‌ها با (الف) کمترین مربعات روی نسبت‌ها و (ب) MLE دوجمله‌ای برازش کنید. همه‌ی برآوردها را با SSE و NLL در یک جدول گزارش کنید.
2. **ارزیابی (2 امتیاز).** $G^2$، درجه‌ی آزادی و $p$ را برای برازش MLE هر مدل حساب کنید. داده‌ها را با بازه‌های 95% دوجمله‌ای، هر دو منحنی برازش‌شده، و باقی‌مانده‌ها رسم کنید. کدام مدل (اگر هست) قابل رد است؟
3. **مطالعه‌ی شبیه‌سازی (3 امتیاز).** مدل توانی با $A = 0.95$، $d = 0.7$ را مدل واقعی در نظر بگیرید. 500 مجموعه‌داده با همین طرح شبیه‌سازی کنید، هرکدام را با LS و MLE برازش کنید و سوگیری، انحراف معیار و RMSE برآورد $\hat d$ را برای هر روش گزارش کنید. هیستوگرام‌ها را نشان دهید. با $n = 100$ آیتم تکرار کنید و بگویید چه تغییر می‌کند.
4. **تفسیر (2 امتیاز، حداکثر 300 کلمه).** برای داده‌های یادآوری کدام برآوردگر را توصیه می‌کنید و چرا؟ جوابتان را به ساختار نویز داده‌های دوجمله‌ای و به شمارش‌های نزدیک به کف (1 تا 2 از 20) در طولانی‌ترین فاصله‌ها ربط دهید. اگر یکی از آن شمارش‌ها 0 بود، چه بر سر روش خطی‌سازی هفته‌ی 2 می‌آمد؟
5. **کیفیت کد (1 امتیاز).** notebook قابل بازتولید و با توضیح؛ seedها ثابت؛ توابع دوباره استفاده شوند نه کپی.

</div>

Late submissions lose 10% per day (max. 3 days).

<div dir="rtl">

برای تحویل با تأخیر، روزی 10% کسر می‌شود (حداکثر 3 روز).

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018), chapter 4.** Maximum likelihood parameter estimation: likelihood functions for common data types, log-likelihood, and fitting in practice. *(Main reading.)*
- **Azimifar & Ahmadi (1396)**, *Shenasayi-ye amari-ye olgu*, vol. 1 (in Persian): the section on maximum likelihood parameter estimation, with the statistical-learning view [verify chapter].
- **Lee & Wagenmakers (2014), chapter 3.** Inferences with binomials. Read it now for the binomial set-up; we revisit it from the Bayesian side in Week 9.

<div dir="rtl">

- **Farrell & Lewandowsky (2018)، فصل 4.** برآورد پارامتر با بیشینه درست‌نمایی: توابع درست‌نمایی برای انواع رایج داده، لگاریتم درست‌نمایی و برازش در عمل. *(منبع اصلی.)*
- **عظیمی‌فر و احمدی (1396)**، *شناسایی آماری الگو*، جلد 1: بخش برآورد پارامتر با بیشینه درست‌نمایی، با نگاه یادگیری آماری [شماره‌ی فصل بررسی شود].
- **Lee & Wagenmakers (2014)، فصل 3.** استنباط با توزیع دوجمله‌ای. الان برای چیدمان دوجمله‌ای بخوانید؛ در هفته‌ی 9 از سمت بیزی دوباره به آن برمی‌گردیم.

</div>

*Preview for Week 5:* an estimate without an uncertainty is half a result. We compute standard errors and confidence intervals from the curvature of the likelihood and by bootstrapping, and we discover how averaging participants can create a "law" that no individual follows.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 5:* برآورد بدون عدم قطعیت نصف یک نتیجه است. خطاهای استاندارد و بازه‌های اطمینان را از انحنای درست‌نمایی و با bootstrap حساب می‌کنیم، و کشف می‌کنیم که چطور میانگین‌گیری از شرکت‌کننده‌ها می‌تواند «قانونی» بسازد که هیچ فردی از آن پیروی نمی‌کند.

</div>
