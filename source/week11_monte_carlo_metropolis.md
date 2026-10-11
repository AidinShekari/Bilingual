# Week 11: Monte Carlo Methods and the Metropolis–Hastings Algorithm · هفته‌ی 11: روش‌های Monte Carlo و الگوریتم Metropolis–Hastings

> **Chapter 5: Parameter estimation with data-driven methods (MCMC)** · Lecture 1 h · Lab 2 h
> **Running data:** the Week 2 forgetting data with the Week 10 priors, so that we can check the sampler against the grid posterior we already have.

<div dir="rtl">

> **فصل 5: برآورد پارامتر با روش‌های داده‌محور (MCMC)** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** داده‌های فراموشی هفته‌ی 2 با پیشین‌های هفته‌ی 10، تا بتوانیم نمونه‌گیر را با پسین شبکه‌ای‌ای که از قبل داریم مقایسه کنیم.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| Monte Carlo | Monte Carlo (مونت‌کارلو) | تقریب با میانگین نمونه‌های تصادفی |
| Metropolis algorithm | الگوریتم Metropolis | پیشنهاد یک حرکت و پذیرش یا رد آن |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| Markov chain Monte Carlo (MCMC) | زنجیره‌ی مارکوف Monte Carlo | نمونه‌گیری از پسین با یک زنجیره‌ی تصادفی |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| prior | توزیع پیشین (prior) | باور درباره‌ی پارامتر پیش از دیدن داده |
| sampler | نمونه‌گیر (sampler) | الگوریتمی که از توزیع نمونه می‌گیرد |
| grid approximation | تقریب شبکه‌ای (grid) | محاسبه‌ی پسین روی شبکه‌ای از مقادیر |
| posterior | توزیع پسین (posterior) | باور درباره‌ی پارامتر بعد از دیدن داده |
| chain | زنجیره | دنباله‌ی نمونه‌های MCMC |
| proposal | پیشنهاد (proposal) | مقدار جدیدی که الگوریتم امتحان می‌کند |
| acceptance rate | نرخ پذیرش | نسبت پیشنهادهای پذیرفته‌شده |
| trace plot | نمودار trace | مقدار نمونه‌ها در برابر شماره‌ی تکرار |
| autocorrelation | خودهمبستگی | وابستگی نمونه‌های پشت سر هم |
| burn-in / warm-up | دوره‌ی گرم‌شدن (burn-in) | نمونه‌های اولیه که دور ریخته می‌شوند |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| starting point | نقطه‌ی شروع | سوگیری اولیه به سمت یکی از پاسخ‌ها |
| response bias | سوگیری پاسخ | تمایل به یک پاسخ، مستقل از محرک |
| large language model (LLM) | مدل بزرگ زبانی | شبکه‌ی عصبی‌ای که کلمه‌ی بعدی متن را پیش‌بینی می‌کند |
| self-consistency | self-consistency (رأی اکثریت) | چند بار نمونه‌گیری جواب و انتخاب رأی اکثریت |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| MCSE | خطای استاندارد Monte Carlo | خطای شبیه‌سازی در میانگین پسین |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Explain** why posterior quantities are integrals, and how Monte Carlo sampling turns integrals into averages, with an error that shrinks like $1/\sqrt{S}$.
2. **Describe** the logic of Markov chain Monte Carlo: a chain whose long-run distribution is the posterior, using only the *unnormalized* posterior.
3. **Implement** the Metropolis (and Metropolis–Hastings) algorithm from scratch for a one- and a two-parameter cognitive model.
4. **Tune** the proposal distribution using the acceptance rate, trace plots and autocorrelation, and **identify** burn-in.
5. **Compute** posterior summaries and derived quantities (e.g., a half-life) from samples, and **validate** a sampler against a known answer.

<div dir="rtl">

1. **توضیح دهند** چرا کمیت‌های پسین انتگرال‌اند، و چطور نمونه‌گیری Monte Carlo انتگرال‌ها را به میانگین تبدیل می‌کند، با خطایی که مثل $1/\sqrt{S}$ کم می‌شود.
2. منطق Markov chain Monte Carlo را **توصیف کنند**: زنجیره‌ای که توزیع بلندمدتش همان پسین است و فقط از پسین *نرمال‌نشده* استفاده می‌کند.
3. الگوریتم Metropolis (و Metropolis–Hastings) را برای یک مدل شناختی یک‌پارامتری و دوپارامتری از صفر **پیاده‌سازی کنند**.
4. توزیع پیشنهادی (proposal) را با استفاده از نرخ پذیرش، trace plot و خودهمبستگی **تنظیم کنند** و دوره‌ی burn-in را **مشخص کنند**.
5. خلاصه‌های پسین و کمیت‌های مشتق‌شده (مثلاً نیمه‌عمر) را از نمونه‌ها **حساب کنند** و نمونه‌گیر را با یک جواب معلوم **اعتبارسنجی کنند**.

</div>

---

## Motivation & big picture · مقدمه

Everything we want from a posterior is an **integral**: the posterior mean $\int \theta\, p(\theta\mid\mathbf{y})\,d\theta$, a marginal posterior (integrating out other parameters), $P(d' > 1\mid\mathbf{y})$, the posterior predictive distribution, the marginal likelihood. In Weeks 9–10 we did these integrals on grids. That worked for two parameters. A hierarchical SDT model for 20 participants (Week 13) has more than 40 parameters; a grid with only 10 points per parameter would need $10^{40}$ evaluations.

<div dir="rtl">

هر چیزی که از یک پسین می‌خواهیم یک **انتگرال** است: میانگین پسین $\int \theta\, p(\theta\mid\mathbf{y})\,d\theta$، پسین حاشیه‌ای (با انتگرال‌گیری روی بقیه‌ی پارامترها)، $P(d' > 1\mid\mathbf{y})$، توزیع پیش‌بینی پسین، و marginal likelihood. در هفته‌های 9–10 این انتگرال‌ها را روی شبکه حساب کردیم. این برای دو پارامتر کار کرد. یک مدل SDT سلسله‌مراتبی برای 20 شرکت‌کننده (هفته‌ی 13) بیش از 40 پارامتر دارد؛ شبکه‌ای با فقط 10 نقطه برای هر پارامتر به $10^{40}$ ارزیابی نیاز دارد.

</div>

**Monte Carlo** methods replace integration by **sampling**: if we could draw many values from the posterior, any integral becomes an average over the draws, and the accuracy depends on the number of draws, not on the number of parameters. The problem is that we cannot sample from a posterior directly; we usually cannot even compute its normalizing constant.

<div dir="rtl">

روش‌های **Monte Carlo** انتگرال‌گیری را با **نمونه‌گیری** جایگزین می‌کنند: اگر بتوانیم مقادیر زیادی از پسین بکشیم، هر انتگرالی به میانگین روی نمونه‌ها تبدیل می‌شود و دقت به تعداد نمونه‌ها بستگی دارد، نه به تعداد پارامترها. مشکل این است که نمی‌توانیم مستقیماً از پسین نمونه بگیریم؛ معمولاً حتی ثابت نرمال‌سازش را هم نمی‌توانیم حساب کنیم.

</div>

**Markov chain Monte Carlo (MCMC)** solves this with a beautifully simple trick: a random walk through parameter space that moves toward more probable values more often than toward less probable ones, in exactly the right proportions. After a while, the places the walker visits are draws from the posterior. The best-known version, the **Metropolis algorithm**, fits in 15 lines of Python, and you will write it today before using any library.

<div dir="rtl">

**Markov chain Monte Carlo (MCMC)** این مشکل را با ترفندی به‌طرز زیبایی ساده حل می‌کند: یک گام‌زنی تصادفی در فضای پارامتر که به سمت مقادیر محتمل‌تر بیشتر از مقادیر کم‌احتمال‌تر حرکت می‌کند، دقیقاً با نسبت‌های درست. بعد از مدتی، جاهایی که این گام‌زن به آن‌ها سر می‌زند نمونه‌هایی از پسین‌اند. شناخته‌شده‌ترین نسخه، یعنی **الگوریتم Metropolis**، در 15 خط Python جا می‌شود و امروز پیش از استفاده از هر کتابخانه‌ای خودتان آن را می‌نویسید.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **All modern Bayesian software** (PyMC, Stan, JAGS, BUGS) is built on MCMC. Every hierarchical model in recent psychology and neuroscience papers was fitted with some version of it.
- **Physics and chemistry** (where Metropolis was invented in 1953, to simulate particles), **epidemiology** (estimating infection parameters), **phylogenetics** (reconstructing evolutionary trees) and **finance** all rely on MCMC.
- **Cognitive science also uses sampling as a *theory of the mind***: some researchers propose that people approximate Bayesian inference by mentally sampling a few possibilities, which explains certain biases.
- **AI**: sampling answers from a language model is Monte Carlo (see the AI & LLMs section).

<div dir="rtl">

- **همه‌ی نرم‌افزارهای بیزی امروزی** (PyMC، Stan، JAGS، BUGS) روی MCMC ساخته شده‌اند. هر مدل سلسله‌مراتبی در مقاله‌های اخیر روان‌شناسی و علوم اعصاب با نسخه‌ای از آن برازش شده است.
- **فیزیک و شیمی** (جایی که الگوریتم Metropolis در سال 1953 برای شبیه‌سازی ذرات ابداع شد)، **همه‌گیرشناسی** (برآورد پارامترهای سرایت)، **تبارشناسی** (بازسازی درخت‌های تکاملی) و **مالی** همه به MCMC تکیه دارند.
- **علوم شناختی نمونه‌گیری را به‌عنوان *نظریه‌ای درباره‌ی ذهن* هم به کار می‌برد:** بعضی پژوهشگرها پیشنهاد می‌کنند آدم‌ها استنباط بیزی را با نمونه‌گیری ذهنی چند امکان تقریب می‌زنند، که بعضی سوگیری‌ها را توضیح می‌دهد.
- **هوش مصنوعی:** نمونه‌گیری جواب از یک مدل زبانی همان Monte Carlo است (بخش هوش مصنوعی و LLMها را ببینید).

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

Every question we ask a posterior ("what is the average value?", "what is the probability that $d' > 1$?") is an integral, and grids cannot compute integrals over many parameters. **Monte Carlo** replaces the integral with an average: if we had many random values *drawn from* the posterior, the average of those values would be the posterior mean, the fraction above 1 would be $P(d' > 1)$, and so on. The difficulty is getting those draws. The **Metropolis algorithm** gets them with a clever random walk. Stand at some parameter value, propose a small random step, and compare how plausible (likelihood × prior) the new spot is. If it is more plausible, move there. If it is less plausible, move there only *sometimes*, with probability equal to the ratio of plausibilities; otherwise stay where you are and record the current value again. Run this long enough and the places you have visited are a sample from the posterior. Remarkably, you never need the hard normalizing constant, because only ratios are used.

<div dir="rtl">

هر سؤالی که از posterior می‌پرسیم («مقدار میانگین چیست؟»، «احتمال اینکه $d' > 1$ باشد چقدر است؟») یک انتگرال است، و grid نمی‌تواند انتگرال روی پارامترهای زیاد را حساب کند. **Monte Carlo** انتگرال را با میانگین جایگزین می‌کند: اگر تعداد زیادی مقدار تصادفی *کشیده‌شده از* posterior داشتیم، میانگین آن‌ها میانگین posterior بود، کسری که بالای 1 است $P(d' > 1)$ بود، و الی آخر. مشکل به دست آوردن این نمونه‌هاست. **الگوریتم Metropolis** آن‌ها را با یک قدم‌زدن تصادفی هوشمندانه به دست می‌آورد. روی یک مقدار پارامتر بایستید، یک قدم تصادفی کوچک پیشنهاد کنید و مقایسه کنید جای جدید چقدر معقول است (درست‌نمایی × prior). اگر معقول‌تر است، به آنجا بروید. اگر کمتر معقول است، فقط *گاهی* بروید، با احتمالی برابر نسبت معقول بودن‌ها؛ وگرنه همان‌جا بمانید و مقدار فعلی را دوباره ثبت کنید. اگر این کار را به اندازه‌ی کافی ادامه دهید، جاهایی که رفته‌اید نمونه‌ای از posterior هستند. نکته‌ی جالب این است که هرگز به ثابت نرمال‌سازی سخت نیاز ندارید، چون فقط از نسبت‌ها استفاده می‌شود.

</div>

**Suggested timing (60 min):** Monte Carlo integration 12 · Markov chains 8 · the Metropolis algorithm 18 · Metropolis–Hastings 5 · tuning, burn-in and autocorrelation 12 · preview 5.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** انتگرال‌گیری Monte Carlo 12 · زنجیره‌های مارکوف 8 · الگوریتم Metropolis 18 · Metropolis–Hastings 5 · تنظیم، burn-in و خودهمبستگی 12 · پیش‌نمایش 5.

</div>

### 1. Monte Carlo integration · 1. انتگرال‌گیری Monte Carlo

If $\theta^{(1)}, \dots, \theta^{(S)}$ are independent draws from $p(\theta\mid\mathbf{y})$, then for any function $g$:

<div dir="rtl">

اگر $\theta^{(1)}, \dots, \theta^{(S)}$ نمونه‌های مستقلی از $p(\theta\mid\mathbf{y})$ باشند، برای هر تابع $g$:

</div>

$$
\mathbb{E}[g(\theta)\mid\mathbf{y}] = \int g(\theta)\, p(\theta\mid\mathbf{y})\, d\theta \;\approx\; \frac{1}{S}\sum_{s=1}^{S} g\big(\theta^{(s)}\big).
$$

| Want | Choose $g(\theta)$ | Monte Carlo estimate |
|---|---|---|
| Posterior mean | $\theta$ | Average of the draws |
| $P(\theta > 1 \mid \mathbf{y})$ | indicator $\mathbb{1}[\theta > 1]$ | Proportion of draws above 1 |
| Posterior of a derived quantity, e.g., half-life $2^{1/d} - 1$ | $g(d)$ | Apply $g$ to each draw, then summarize |
| Credible interval | — | Percentiles (or HDI) of the draws |
| Marginal posterior of $\theta_1$ | — | Simply ignore the other columns |

<div dir="rtl">

| آنچه می‌خواهیم | $g(\theta)$ را انتخاب کنید | برآورد Monte Carlo |
|---|---|---|
| میانگین پسین | $\theta$ | میانگین نمونه‌ها |
| $P(\theta > 1 \mid \mathbf{y})$ | شاخص $\mathbb{1}[\theta > 1]$ | نسبت نمونه‌های بالای 1 |
| پسین یک کمیت مشتق‌شده، مثلاً نیمه‌عمر $2^{1/d} - 1$ | $g(d)$ | $g$ را روی هر نمونه اعمال و بعد خلاصه کنید |
| credible interval | — | صدک‌ها (یا HDI) نمونه‌ها |
| پسین حاشیه‌ای $\theta_1$ | — | فقط ستون‌های دیگر را نادیده بگیرید |

</div>

The **Monte Carlo standard error** of the mean is $\mathrm{SD}(g)/\sqrt{S}$ for independent draws, independent of the number of parameters. That is why sampling beats grids in high dimensions.

<div dir="rtl">

**خطای استاندارد Monte Carlo** میانگین برای نمونه‌های مستقل $\mathrm{SD}(g)/\sqrt{S}$ است، مستقل از تعداد پارامترها. به همین دلیل نمونه‌گیری در ابعاد بالا بر شبکه برتری دارد.

</div>

#### Reading the math · خواندن ریاضی

- $\mathbb{E}[g(\theta)\mid\mathbf{y}] = \int g(\theta)\,p(\theta\mid\mathbf{y})\,d\theta$: the posterior average of some quantity $g(\theta)$. Choosing $g$ chooses the question (see the table).
- $\approx \frac{1}{S}\sum_{s} g(\theta^{(s)})$: replace the integral by the plain average over $S$ draws $\theta^{(1)}, \dots, \theta^{(S)}$. The superscript $(s)$ is the draw number.
- **Error:** $\mathrm{SD}(g)/\sqrt{S}$. To halve the error you need four times as many draws, whatever the number of parameters.
- **Example:** 10,000 draws from $\mathrm{Beta}(8,4)$; 9,000 of them are above 0.5, so $P(\theta > 0.5 \mid \mathbf{y}) \approx 0.90$, with Monte Carlo error $\sqrt{0.9 \times 0.1/10000} = 0.003$.

<div dir="rtl">

- $\mathbb{E}[g(\theta)\mid\mathbf{y}] = \int g(\theta)\,p(\theta\mid\mathbf{y})\,d\theta$: میانگین posterior یک کمیت $g(\theta)$. انتخاب $g$ یعنی انتخاب سؤال (جدول را ببینید).
- $\approx \frac{1}{S}\sum_{s} g(\theta^{(s)})$: انتگرال را با میانگین ساده روی $S$ نمونه‌ی $\theta^{(1)}, \dots, \theta^{(S)}$ جایگزین کن. بالانویس $(s)$ شماره‌ی نمونه است.
- **خطا:** $\mathrm{SD}(g)/\sqrt{S}$. برای نصف کردن خطا چهار برابر نمونه لازم است، هر تعداد پارامتری که داشته باشیم.
- **مثال:** 10,000 نمونه از $\mathrm{Beta}(8,4)$؛ 9,000 تای آن‌ها بالای 0.5 هستند، پس $P(\theta > 0.5 \mid \mathbf{y}) \approx 0.90$ با خطای Monte Carlo برابر $\sqrt{0.9 \times 0.1/10000} = 0.003$.

</div>

### 2. Markov chains in one paragraph · 2. زنجیره‌های مارکوف در یک پاراگراف

A **Markov chain** is a sequence $\theta^{(1)}, \theta^{(2)}, \dots$ in which each value is generated from the previous one only, by a fixed transition rule. Under mild conditions, a chain "forgets" its starting point and settles into a **stationary distribution**: the long-run proportion of time it spends in each region. MCMC constructs a transition rule whose stationary distribution is the posterior. Two consequences:
- The early part of the chain still reflects the starting point. It is discarded as **burn-in** (warm-up).
- Successive draws are **correlated**, so $S$ correlated draws carry less information than $S$ independent ones (the effective sample size, Week 12).

<div dir="rtl">

یک **زنجیره‌ی مارکوف** دنباله‌ای $\theta^{(1)}, \theta^{(2)}, \dots$ است که در آن هر مقدار فقط از مقدار قبلی، با یک قاعده‌ی گذار ثابت، تولید می‌شود. تحت شرایط ملایم، زنجیره نقطه‌ی شروعش را «فراموش می‌کند» و به یک **توزیع ایستا** (stationary) می‌رسد: نسبت بلندمدت زمانی که در هر ناحیه می‌گذراند. MCMC قاعده‌ی گذاری می‌سازد که توزیع ایستایش همان پسین است. دو پیامد:
- بخش اولیه‌ی زنجیره هنوز بازتاب نقطه‌ی شروع است. به‌عنوان **burn-in** (warm-up) دور ریخته می‌شود.
- نمونه‌های پشت‌سرهم **همبسته‌اند**، پس $S$ نمونه‌ی همبسته اطلاعات کمتری از $S$ نمونه‌ی مستقل دارند (اندازه‌ی مؤثر نمونه، هفته‌ی 12).

</div>

### 3. The Metropolis algorithm · 3. الگوریتم Metropolis

Let $\tilde p(\theta) = p(\mathbf{y}\mid\theta)\,p(\theta)$ be the **unnormalized** posterior (likelihood × prior). Choose a symmetric **proposal distribution**, usually a normal random walk $\theta' \sim \mathcal{N}(\theta, \sigma_{\text{prop}})$.

<div dir="rtl">

فرض کنید $\tilde p(\theta) = p(\mathbf{y}\mid\theta)\,p(\theta)$ پسین **نرمال‌نشده** (درست‌نمایی × پیشین) باشد. یک **توزیع پیشنهادی** متقارن انتخاب کنید، معمولاً یک گام تصادفی نرمال $\theta' \sim \mathcal{N}(\theta, \sigma_{\text{prop}})$.

</div>

1. Start at some $\theta^{(0)}$.
2. For $s = 1, 2, \dots, S$:
   - Propose $\theta' \sim \mathcal{N}(\theta^{(s-1)}, \sigma_{\text{prop}})$.
   - Compute the acceptance probability
     $$
     \alpha_{\text{acc}} = \min\left(1,\ \frac{\tilde p(\theta')}{\tilde p(\theta^{(s-1)})}\right).
     $$
   - Draw $u \sim \mathrm{Uniform}(0, 1)$. If $u < \alpha_{\text{acc}}$, **accept**: $\theta^{(s)} = \theta'$. Otherwise **reject**: $\theta^{(s)} = \theta^{(s-1)}$ (the current value is *repeated* in the chain).

<div dir="rtl">

1. از یک $\theta^{(0)}$ شروع کنید.
2. برای $s = 1, 2, \dots, S$:
   - پیشنهاد دهید $\theta' \sim \mathcal{N}(\theta^{(s-1)}, \sigma_{\text{prop}})$.
   - احتمال پذیرش را حساب کنید:
     $$
     \alpha_{\text{acc}} = \min\left(1,\ \frac{\tilde p(\theta')}{\tilde p(\theta^{(s-1)})}\right).
     $$
   - $u \sim \mathrm{Uniform}(0, 1)$ بکشید. اگر $u < \alpha_{\text{acc}}$، **بپذیرید**: $\theta^{(s)} = \theta'$. وگرنه **رد کنید**: $\theta^{(s)} = \theta^{(s-1)}$ (مقدار فعلی در زنجیره *تکرار* می‌شود).

</div>

**Why it works intuitively:** uphill moves are always accepted; downhill moves are accepted with probability equal to the density ratio. So the chain spends time in each region in proportion to its posterior probability.

<div dir="rtl">

**چرا به‌طور شهودی کار می‌کند:** حرکت‌های سربالا همیشه پذیرفته می‌شوند؛ حرکت‌های سرپایینی با احتمالی برابر نسبت چگالی‌ها پذیرفته می‌شوند. پس زنجیره در هر ناحیه به نسبت احتمال پسینش وقت می‌گذراند.

</div>

**Why only the unnormalized posterior is needed:** the evidence $p(\mathbf{y})$ appears in both numerator and denominator of the ratio and cancels. This is the key to MCMC's usefulness.

<div dir="rtl">

**چرا فقط پسین نرمال‌نشده لازم است:** شواهد $p(\mathbf{y})$ هم در صورت و هم در مخرج نسبت ظاهر می‌شود و ساده می‌شود. این کلید سودمندی MCMC است.

</div>

**Practical details:**
- Work in **logs**: accept if $\ln u < \ln\tilde p(\theta') - \ln\tilde p(\theta)$.
- **Bounded parameters:** if a proposal falls outside the support (e.g., $A > 1$), its prior is 0, so $\ln\tilde p = -\infty$ and the proposal is automatically rejected. (Alternatively, sample on a transformed, unbounded scale, as in Week 3; then the Jacobian must be added to the log posterior.)
- **Multiple parameters:** propose all parameters at once with a vector of proposal SDs, or update one parameter at a time (which leads to Gibbs sampling, Week 12).

<div dir="rtl">

**جزئیات عملی:**
- با **لگاریتم** کار کنید: اگر $\ln u < \ln\tilde p(\theta') - \ln\tilde p(\theta)$ بپذیرید.
- **پارامترهای کران‌دار:** اگر یک پیشنهاد خارج از تکیه‌گاه بیفتد (مثلاً $A > 1$)، پیشینش 0 است، پس $\ln\tilde p = -\infty$ و پیشنهاد خودکار رد می‌شود. (راه دیگر نمونه‌گیری روی یک مقیاس تبدیل‌شده و بی‌کران است، مثل هفته‌ی 3؛ در این صورت باید Jacobian را به لگاریتم پسین اضافه کرد.)
- **چند پارامتر:** همه‌ی پارامترها را هم‌زمان با برداری از انحراف معیارهای پیشنهادی پیشنهاد دهید، یا هر بار یک پارامتر را به‌روز کنید (که به نمونه‌گیری Gibbs می‌رسد، هفته‌ی 12).

</div>

> **Advanced: detailed balance.** A transition rule $T(\theta \to \theta')$ leaves $\pi$ stationary if $\pi(\theta)\,T(\theta \to \theta') = \pi(\theta')\,T(\theta' \to \theta)$ for all pairs. Check it for Metropolis with $\tilde p(\theta') < \tilde p(\theta)$: the left side is $\pi(\theta)\, q(\theta'\mid\theta)\, \tilde p(\theta')/\tilde p(\theta)$ and the right side is $\pi(\theta')\, q(\theta\mid\theta') \cdot 1$. With symmetric $q$ and $\pi \propto \tilde p$, the two are equal.

<div dir="rtl">

> **پیشرفته: تعادل جزئی (detailed balance).** یک قاعده‌ی گذار $T(\theta \to \theta')$ توزیع $\pi$ را ایستا نگه می‌دارد اگر برای همه‌ی جفت‌ها $\pi(\theta)\,T(\theta \to \theta') = \pi(\theta')\,T(\theta' \to \theta)$. این را برای Metropolis با $\tilde p(\theta') < \tilde p(\theta)$ بررسی کنید: سمت چپ $\pi(\theta)\, q(\theta'\mid\theta)\, \tilde p(\theta')/\tilde p(\theta)$ و سمت راست $\pi(\theta')\, q(\theta\mid\theta') \cdot 1$ است. با $q$ متقارن و $\pi \propto \tilde p$ این دو برابرند.

</div>

#### Reading the math · خواندن ریاضی

- $\tilde p(\theta) = p(\mathbf{y}\mid\theta)\,p(\theta)$: likelihood × prior, *without* dividing by the evidence. The tilde (~) marks "unnormalized".
- $\alpha_{\text{acc}} = \min(1, \tilde p(\theta')/\tilde p(\theta))$: if the proposal is more plausible, the ratio is > 1 and $\min$ caps it at 1 (always accept). If it is half as plausible, accept with probability 0.5.
- "Draw $u \sim \mathrm{Uniform}(0,1)$; accept if $u < \alpha$" is simply a way to make an event happen with probability $\alpha$ (a biased coin).
- **Worked example, step 3:** the proposal 0.95 is only 0.052 times as plausible as 0.80; $u = 0.30 > 0.052$, so it is rejected and 0.80 is written into the chain a second time.

<div dir="rtl">

- $\tilde p(\theta) = p(\mathbf{y}\mid\theta)\,p(\theta)$: درست‌نمایی × prior، *بدون* تقسیم بر evidence. علامت تیلدا (~) یعنی «نرمال‌نشده».
- $\alpha_{\text{acc}} = \min(1, \tilde p(\theta')/\tilde p(\theta))$: اگر پیشنهاد معقول‌تر باشد، نسبت بزرگ‌تر از 1 است و $\min$ آن را روی 1 نگه می‌دارد (همیشه پذیرش). اگر نصف معقول باشد، با احتمال 0.5 پذیرفته می‌شود.
- «$u \sim \mathrm{Uniform}(0,1)$ بکش؛ اگر $u < \alpha$ بود بپذیر» فقط راهی است برای اینکه یک رویداد با احتمال $\alpha$ اتفاق بیفتد (یک سکه‌ی نامتعادل).
- **مثال حل‌شده، قدم 3:** پیشنهاد 0.95 فقط 0.052 برابر 0.80 معقول است؛ $u = 0.30 > 0.052$، پس رد می‌شود و 0.80 بار دوم در زنجیره نوشته می‌شود.

</div>

### 4. Metropolis–Hastings: asymmetric proposals · 4. Metropolis–Hastings: پیشنهادهای نامتقارن

If the proposal is not symmetric, $q(\theta'\mid\theta) \ne q(\theta\mid\theta')$ (e.g., a log-normal proposal for a positive rate), the acceptance probability needs a correction:

<div dir="rtl">

اگر توزیع پیشنهادی متقارن نباشد، $q(\theta'\mid\theta) \ne q(\theta\mid\theta')$ (مثلاً پیشنهاد log-normal برای یک نرخ مثبت)، احتمال پذیرش به یک تصحیح نیاز دارد:

</div>

$$
\alpha_{\text{acc}} = \min\left(1,\ \frac{\tilde p(\theta')\, q(\theta \mid \theta')}{\tilde p(\theta)\, q(\theta' \mid \theta)}\right).
$$

Metropolis is the special case where the $q$ terms cancel. Gibbs sampling (Week 12) is another special case, in which every proposal is accepted.

<div dir="rtl">

Metropolis حالت خاصی است که جمله‌های $q$ ساده می‌شوند. نمونه‌گیری Gibbs (هفته‌ی 12) حالت خاص دیگری است که در آن هر پیشنهادی پذیرفته می‌شود.

</div>

### 5. Tuning and diagnosing a sampler · 5. تنظیم و تشخیص مشکلات یک نمونه‌گیر

The proposal SD $\sigma_{\text{prop}}$ controls efficiency:

<div dir="rtl">

انحراف معیار پیشنهادی $\sigma_{\text{prop}}$ کارایی را کنترل می‌کند:

</div>

| $\sigma_{\text{prop}}$ | Acceptance rate | Behavior | Trace plot looks like |
|---|---|---|---|
| Too small | Very high (> 0.9) | Tiny steps; explores slowly; strong autocorrelation | A slowly wandering line |
| Too large | Very low (< 0.1) | Most proposals land in low-probability regions and are rejected; the chain sticks | Flat steps with long plateaus |
| About right | ≈ 0.2–0.5 | Good mixing | A "fuzzy caterpillar" |

<div dir="rtl">

| $\sigma_{\text{prop}}$ | نرخ پذیرش | رفتار | trace plot چه شکلی است |
|---|---|---|---|
| خیلی کوچک | خیلی بالا (> 0.9) | گام‌های ریز؛ کاوش کند؛ خودهمبستگی قوی | خطی که آرام سرگردان است |
| خیلی بزرگ | خیلی پایین (< 0.1) | بیشتر پیشنهادها در نواحی کم‌احتمال می‌افتند و رد می‌شوند؛ زنجیره گیر می‌کند | پله‌های صاف با فلات‌های طولانی |
| تقریباً درست | ≈ 0.2 تا 0.5 | اختلاط (mixing) خوب | یک «کرم پشمالو» (fuzzy caterpillar) |

</div>

Classic theoretical results suggest an optimal acceptance rate of about 0.44 for one parameter, falling toward about 0.23 for many parameters. Treat these as targets, not laws. Tune $\sigma_{\text{prop}}$ during a preliminary run (not during the run you keep). Good proposal SDs are of the order of the posterior SDs, and correlated posteriors need correlated (or reparameterized) proposals.

<div dir="rtl">

نتایج نظری کلاسیک نرخ پذیرش بهینه‌ی حدود 0.44 را برای یک پارامتر پیشنهاد می‌کنند که برای پارامترهای زیاد به حدود 0.23 می‌رسد. این‌ها را هدف بدانید، نه قانون. $\sigma_{\text{prop}}$ را در یک اجرای مقدماتی تنظیم کنید (نه در اجرایی که نگه می‌دارید). انحراف معیارهای پیشنهادی خوب هم‌مرتبه با انحراف معیارهای پسین‌اند، و پسین‌های همبسته به پیشنهادهای همبسته (یا reparameterization) نیاز دارند.

</div>

**Burn-in.** Discard the initial part of the chain before it reaches the high-probability region; the trace plot shows where. **Thinning** (keeping every $m$-th draw) reduces storage but throws away information. It is not needed for correct inference.

<div dir="rtl">

**Burn-in.** بخش اولیه‌ی زنجیره را پیش از رسیدن به ناحیه‌ی پراحتمال دور بریزید؛ trace plot نشان می‌دهد کجا. **Thinning** (نگه داشتن هر $m$-امین نمونه) حافظه را کم می‌کند ولی اطلاعات را دور می‌ریزد. برای استنباط درست لازم نیست.

</div>

**Autocorrelation.** The lag-$h$ autocorrelation is the correlation between $\theta^{(s)}$ and $\theta^{(s+h)}$. High autocorrelation means slow exploration and fewer effectively independent draws.

<div dir="rtl">

**خودهمبستگی.** خودهمبستگی با تأخیر $h$ همبستگی بین $\theta^{(s)}$ و $\theta^{(s+h)}$ است. خودهمبستگی بالا یعنی کاوش کند و نمونه‌های مؤثراً مستقل کمتر.

</div>

**Always validate** a new sampler on a problem with a known answer (here, the conjugate beta-binomial and the Week 10 grid).

<div dir="rtl">

**همیشه یک نمونه‌گیر جدید را** روی مسئله‌ای با جواب معلوم **اعتبارسنجی کنید** (اینجا، beta-binomial conjugate و شبکه‌ی هفته‌ی 10).

</div>

#### For an engineer · برای یک مهندس

- **Monte Carlo integration** is what you do when you estimate a BER or an outage probability by simulation: average an indicator over many random realizations. The $1/\sqrt{S}$ error law is the same, and it is why low error rates need very long simulations.
- An MCMC chain is a **Markov process** whose stationary distribution is designed to be the posterior; burn-in is the transient, the stationary part is the steady state.
- **Autocorrelation** of the chain is exactly the autocorrelation of a random process. Correlated samples carry less information, just as correlated noise samples average out more slowly; Week 12 turns this into the "effective sample size".
- **Proposal tuning** is a step-size problem like choosing the step size of an adaptive filter: too small converges slowly, too large becomes unstable (here: most steps are rejected).
- The difference from ordinary simulation: we cannot generate independent samples from the target directly, so we build a process that converges to it.

<div dir="rtl">

- **انتگرال‌گیری Monte Carlo** همان کاری است که برای تخمین BER یا احتمال قطعی (outage) با شبیه‌سازی می‌کنید: میانگین یک تابع نشانگر روی تعداد زیادی تحقق تصادفی. قانون خطای $1/\sqrt{S}$ همان است، و به همین دلیل نرخ‌های خطای پایین شبیه‌سازی‌های خیلی طولانی لازم دارند.
- یک زنجیره‌ی MCMC یک **فرایند مارکوف** است که توزیع ایستای آن طوری طراحی شده که posterior باشد؛ burn-in همان حالت گذرا و بخش ایستا همان حالت ماندگار است.
- **خودهمبستگی** زنجیره دقیقاً همان خودهمبستگی یک فرایند تصادفی است. نمونه‌های همبسته اطلاعات کمتری دارند، همان‌طور که نمونه‌های نویز همبسته کندتر میانگین‌گیری می‌شوند؛ هفته‌ی 12 این را به «اندازه‌ی مؤثر نمونه» تبدیل می‌کند.
- **تنظیم پیشنهاد (proposal)** یک مسئله‌ی اندازه‌ی گام است، مثل انتخاب اندازه‌ی گام یک فیلتر تطبیقی: خیلی کوچک کند همگرا می‌شود، خیلی بزرگ ناپایدار می‌شود (اینجا: بیشتر قدم‌ها رد می‌شوند).
- تفاوت با شبیه‌سازی معمولی: نمی‌توانیم مستقیم از توزیع هدف نمونه‌ی مستقل تولید کنیم، پس فرایندی می‌سازیم که به آن همگرا شود.

</div>

#### For the instructor · برای مدرس

- **Walk the chain on the board.** Draw the curve $\theta^7(1-\theta)^3$ and run the four steps of the worked example with a student rolling the "$u$" values (a random number app works). The rejected step that *repeats* 0.80 is the key moment; ask why it must be recorded.
- **An analogy that works:** a tourist exploring a city at night who prefers lit streets. Brighter street: always go. Darker street: go only sometimes. After a long walk, the time spent on each street is proportional to its brightness.
- **Show the three trace plots** (too small, good, too large) from lab Part D side by side. Students learn to read trace plots in five minutes this way.
- **Typical questions.**
  - *"Why not just use a fine grid?"* With 40 parameters, a grid is impossible; sampling cost does not grow that way.
  - *"How do we know the chain has converged?"* That is Week 12 (multiple chains, $\hat R$).
  - *"Why throw away burn-in?"* Early draws still reflect the arbitrary starting point, not the posterior.

<div dir="rtl">

- **زنجیره را روی تخته اجرا کنید.** منحنی $\theta^7(1-\theta)^3$ را بکشید و چهار قدم مثال حل‌شده را اجرا کنید، در حالی که یک دانشجو مقدارهای «$u$» را تولید می‌کند (یک اپلیکیشن عدد تصادفی کافی است). قدم رد‌شده که 0.80 را *تکرار* می‌کند لحظه‌ی کلیدی است؛ بپرسید چرا باید ثبت شود.
- **تشبیهی که جواب می‌دهد:** گردشگری که شب در یک شهر می‌گردد و خیابان‌های روشن را ترجیح می‌دهد. خیابان روشن‌تر: همیشه برو. خیابان تاریک‌تر: فقط گاهی برو. بعد از یک پیاده‌روی طولانی، زمانی که در هر خیابان گذرانده متناسب با روشنایی آن است.
- **سه trace plot را** (خیلی کوچک، خوب، خیلی بزرگ) از بخش D lab کنار هم نشان دهید. دانشجوها این‌طوری در پنج دقیقه خواندن trace plot را یاد می‌گیرند.
- **سؤال‌های رایج.**
  - *«چرا فقط از یک grid ریز استفاده نکنیم؟»* با 40 پارامتر grid ناممکن است؛ هزینه‌ی نمونه‌گیری این‌طور رشد نمی‌کند.
  - *«از کجا بدانیم زنجیره همگرا شده؟»* این موضوع هفته‌ی 12 است (چند زنجیره، $\hat R$).
  - *«چرا burn-in را دور بریزیم؟»* نمونه‌های اولیه هنوز نقطه‌ی شروع دلبخواه را نشان می‌دهند، نه posterior را.

</div>

---

## Worked example · مثال حل‌شده

**Model:** recall $y = 7$ of $n = 10$ with a flat prior, so $\tilde p(\theta) = \theta^7(1-\theta)^3$ (constants dropped). Exact posterior: $\mathrm{Beta}(8, 4)$, mean 0.667. Proposal: $\theta' = \theta + \mathcal{N}(0, 0.1)$.

<div dir="rtl">

**مدل:** یادآوری $y = 7$ از $n = 10$ با پیشین تخت، پس $\tilde p(\theta) = \theta^7(1-\theta)^3$ (بدون ثابت‌ها). پسین دقیق: $\mathrm{Beta}(8, 4)$ با میانگین 0.667. پیشنهاد: $\theta' = \theta + \mathcal{N}(0, 0.1)$.

</div>

| Step | Current $\theta$ | Proposal $\theta'$ | $\tilde p(\theta)$ | $\tilde p(\theta')$ | Ratio | $u$ | Decision | New $\theta$ |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.50 | 0.58 | 0.000977 | 0.001636 | 1.675 | 0.42 | accept (uphill) | 0.58 |
| 2 | 0.58 | 0.80 | 0.001636 | 0.001678 | 1.026 | 0.71 | accept (uphill) | 0.80 |
| 3 | 0.80 | 0.95 | 0.001678 | 0.000087 | 0.052 | 0.30 | **reject**: $u > 0.052$ | 0.80 |
| 4 | 0.80 | 0.66 | 0.001678 | 0.002144 | 1.278 | 0.88 | accept (uphill) | 0.66 |

<div dir="rtl">

| گام | $\theta$ فعلی | پیشنهاد $\theta'$ | $\tilde p(\theta)$ | $\tilde p(\theta')$ | نسبت | $u$ | تصمیم | $\theta$ جدید |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.50 | 0.58 | 0.000977 | 0.001636 | 1.675 | 0.42 | پذیرش (سربالا) | 0.58 |
| 2 | 0.58 | 0.80 | 0.001636 | 0.001678 | 1.026 | 0.71 | پذیرش (سربالا) | 0.80 |
| 3 | 0.80 | 0.95 | 0.001678 | 0.000087 | 0.052 | 0.30 | **رد**: $u > 0.052$ | 0.80 |
| 4 | 0.80 | 0.66 | 0.001678 | 0.002144 | 1.278 | 0.88 | پذیرش (سربالا) | 0.66 |

</div>

**Chain so far:** 0.50, 0.58, 0.80, **0.80**, 0.66. The rejected step *repeats* 0.80 in the chain. That is essential: repeated values are how the chain records that 0.80 is more probable than 0.95. Dropping them would bias the sample.

<div dir="rtl">

**زنجیره تا اینجا:** 0.50، 0.58، 0.80، **0.80**، 0.66. گام ردشده مقدار 0.80 را در زنجیره *تکرار* می‌کند. این ضروری است: مقادیر تکراری راهی است که زنجیره ثبت می‌کند 0.80 از 0.95 محتمل‌تر است. حذف آن‌ها نمونه را سوگیر می‌کند.

</div>

**Interpretation.** In four steps the chain moved from the start into the region of high posterior density (0.6–0.8) and refused a jump into the tail. Over thousands of steps, the proportion of time spent near each value converges to $\mathrm{Beta}(8, 4)$.

<div dir="rtl">

**تفسیر.** در چهار گام، زنجیره از نقطه‌ی شروع به ناحیه‌ی چگالی پسین بالا (0.6 تا 0.8) رفت و از پرش به دنباله امتناع کرد. در طول هزاران گام، نسبت زمانی که نزدیک هر مقدار گذرانده می‌شود به $\mathrm{Beta}(8, 4)$ همگرا می‌شود.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Monte Carlo integration with independent draws: see the $1/\sqrt{S}$ error.
2. Write a Metropolis sampler and validate it on the beta-binomial model.
3. Sample the posterior of the power forgetting model, compare with the Week 10 grid, and compute a derived quantity.
4. Tune the proposal: compare too-small, good and too-large proposal SDs with trace plots, acceptance rates and autocorrelation.

<div dir="rtl">

1. انتگرال‌گیری Monte Carlo با نمونه‌های مستقل: دیدن خطای $1/\sqrt{S}$.
2. نوشتن یک نمونه‌گیر Metropolis و اعتبارسنجی آن روی مدل beta-binomial.
3. نمونه‌گیری از پسین مدل فراموشی توانی، مقایسه با شبکه‌ی هفته‌ی 10، و محاسبه‌ی یک کمیت مشتق‌شده.
4. تنظیم پیشنهاد: مقایسه‌ی انحراف معیارهای پیشنهادی خیلی کوچک، خوب و خیلی بزرگ با trace plot، نرخ پذیرش و خودهمبستگی.

</div>

**Timing:** Part A 15 min · Part B 25 min · Part C 35 min · Part D 30 min · Part E 15 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 15 دقیقه · بخش B 25 دقیقه · بخش C 35 دقیقه · بخش D 30 دقیقه · بخش E 15 دقیقه.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 1 · سلول 1

### Part A: Monte Carlo integration (15 min) · بخش A: انتگرال‌گیری Monte Carlo (15 دقیقه)

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Exact: mean = 0.5926, P(theta > 0.65) = 0.1967
S =    100: mean = 0.5865 (MC s.e. 0.0065), P(theta > 0.65) = 0.1800
S =   1000: mean = 0.5935 (MC s.e. 0.0021), P(theta > 0.65) = 0.2160
S =  10000: mean = 0.5937 (MC s.e. 0.0007), P(theta > 0.65) = 0.2022
S = 100000: mean = 0.5927 (MC s.e. 0.0002), P(theta > 0.65) = 0.1971
```

Ten times more draws gives about $\sqrt{10} \approx 3.2$ times less Monte Carlo error.

<div dir="rtl">

ده برابر نمونه‌ی بیشتر حدود $\sqrt{10} \approx 3.2$ برابر خطای Monte Carlo کمتر می‌دهد.

</div>

### Part B: a Metropolis sampler, validated (25 min) · بخش B: یک نمونه‌گیر Metropolis، اعتبارسنجی‌شده (25 دقیقه)

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Acceptance rate: 0.59
Metropolis: mean = 0.5930, SD = 0.0660, 95% interval = [0.458 0.718]
Exact:      mean = 0.5926, SD = 0.0663, 95% interval = [0.46  0.719]
```

### Part C: Metropolis for the power forgetting model (35 min) · بخش C: Metropolis برای مدل فراموشی توانی (35 دقیقه)

Same priors as in Week 10: $A \sim \mathrm{Beta}(8, 2)$, $d \sim \mathrm{Gamma}(2, \text{scale } 0.3)$.

<div dir="rtl">

همان پیشین‌های هفته‌ی 10: $A \sim \mathrm{Beta}(8, 2)$، $d \sim \mathrm{Gamma}(2, \text{scale } 0.3)$.

</div>

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Acceptance rate: 0.49
    mean     SD   2.5%  97.5%
A  0.868  0.052  0.762   0.96
d  0.418  0.048  0.325   0.51
Week 10 grid posterior means for comparison: A = 0.867, d = 0.417
```

**Derived quantities** come for free. Compute the posterior of the half-life $t_{1/2} = 2^{1/d} - 1$ (Week 2) and the predicted recall after 60 days:

<div dir="rtl">

**کمیت‌های مشتق‌شده** مجانی به دست می‌آیند. پسین نیمه‌عمر $t_{1/2} = 2^{1/d} - 1$ (هفته‌ی 2) و یادآوری پیش‌بینی‌شده بعد از 60 روز را حساب کنید:

</div>

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
half-life (days)       mean = 4.493, 95% interval = [2.889 7.443]
P(recall) at 60 days   mean = 0.158, 95% interval = [0.113 0.211]
P(half-life < 3 days | data) = 0.039
```

### Part D: tuning the proposal (30 min) · بخش D: تنظیم توزیع پیشنهادی (30 دقیقه)

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
too small    proposal SD = [0.002, 0.002]: acceptance = 0.97, lag-10 autocorrelation of d = 0.98, mean of d = 0.473
about right  proposal SD = [0.04, 0.05]: acceptance = 0.50, lag-10 autocorrelation of d = 0.26, mean of d = 0.416
too large    proposal SD = [0.5, 1.5]: acceptance = 0.00, lag-10 autocorrelation of d = 0.94, mean of d = 0.420
```

**What to notice:** the "too small" chain accepts almost everything but crawls (a slowly wandering trace with autocorrelation near 1 even at lag 60); the "too large" chain rejects almost everything and sits still for long stretches (flat steps). Both give unreliable estimates from 10 000 iterations: the "too small" chain's mean of $d$ (0.473) is far from the true posterior mean (0.417), and the "too large" chain's mean happens to be close only because it barely moved from its starting value (0.42). The well-tuned chain looks like a fuzzy caterpillar and its autocorrelation decays quickly.

<div dir="rtl">

**به این دقت کنید:** زنجیره‌ی «خیلی کوچک» تقریباً همه‌چیز را می‌پذیرد ولی می‌خزد (trace که آرام سرگردان است و خودهمبستگی‌اش حتی با تأخیر 60 نزدیک 1 است)؛ زنجیره‌ی «خیلی بزرگ» تقریباً همه‌چیز را رد می‌کند و مدت‌های طولانی ساکن می‌ماند (پله‌های صاف). هر دو با 10 000 تکرار برآوردهای غیرقابل اعتماد می‌دهند: میانگین $d$ زنجیره‌ی «خیلی کوچک» (0.473) از میانگین پسین واقعی (0.417) دور است، و میانگین زنجیره‌ی «خیلی بزرگ» فقط به این دلیل نزدیک است که تقریباً از مقدار شروعش (0.42) تکان نخورده است. زنجیره‌ی خوب تنظیم‌شده شبیه یک کرم پشمالوست و خودهمبستگی‌اش سریع کم می‌شود.

</div>

### Part E: interpret (15 min) · بخش E: تفسیر (15 دقیقه)

Answer in your notebook:
1. Do the Metropolis posterior summaries for $(A, d)$ agree with the Week 10 grid? What does that agreement establish?
2. How would you report the half-life of this participant's memory, with uncertainty, in one sentence?
3. Why must rejected proposals be recorded as repeated values in the chain?

<div dir="rtl">

در notebook جواب دهید:
1. آیا خلاصه‌های پسین Metropolis برای $(A, d)$ با شبکه‌ی هفته‌ی 10 توافق دارند؟ این توافق چه چیزی را ثابت می‌کند؟
2. نیمه‌عمر حافظه‌ی این شرکت‌کننده را، همراه با عدم قطعیت، در یک جمله چطور گزارش می‌کنید؟
3. چرا پیشنهادهای ردشده باید به‌صورت مقادیر تکراری در زنجیره ثبت شوند؟

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Using the Part B sampler, estimate $P(\theta > 0.65\mid\mathbf{y})$ for 30/50 and compare with the exact value from Part A. How many iterations do you need to get within ±0.01?

<div dir="rtl">

**تمرین 1 ★.** با نمونه‌گیر بخش B، $P(\theta > 0.65\mid\mathbf{y})$ را برای 30/50 برآورد کنید و با مقدار دقیق بخش A مقایسه کنید. برای رسیدن به دقت ±0.01 چند تکرار لازم است؟

</div>

**Exercise 2 ★.** Run the Part C sampler from four very different starting points, e.g., $(0.3, 0.05)$, $(0.99, 2.5)$, $(0.5, 1.0)$ and $(0.9, 0.1)$. Plot all traces together. After how many iterations do they become indistinguishable? (This is the idea behind R-hat, Week 12.)

<div dir="rtl">

**تمرین 2 ★.** نمونه‌گیر بخش C را از چهار نقطه‌ی شروع خیلی متفاوت اجرا کنید، مثلاً $(0.3, 0.05)$، $(0.99, 2.5)$، $(0.5, 1.0)$ و $(0.9, 0.1)$. همه‌ی traceها را با هم رسم کنید. بعد از چند تکرار از هم قابل تشخیص نیستند؟ (این ایده‌ی پشت R-hat است، هفته‌ی 12.)

</div>

**Exercise 3 ★★ (exponential model).** Write `log_post_exp` with the Week 10 priors, sample it, and compare the posterior with the grid. Then compute the posterior predictive distribution from your samples and reproduce the Week 10 PPC plot.

<div dir="rtl">

**تمرین 3 ★★ (مدل نمایی).** `log_post_exp` را با پیشین‌های هفته‌ی 10 بنویسید، از آن نمونه بگیرید و پسین را با شبکه مقایسه کنید. بعد توزیع پیش‌بینی پسین را از نمونه‌هایتان حساب کنید و نمودار PPC هفته‌ی 10 را بازتولید کنید.

</div>

**Exercise 4 ★★ (Metropolis–Hastings with an asymmetric proposal).** Sample $d$ with a **log-normal** random-walk proposal, $\ln d' \sim \mathcal{N}(\ln d, 0.1)$, which never proposes negative values. Derive the Hastings correction $q(d\mid d')/q(d'\mid d) = d'/d$ and include it. Show that omitting the correction biases the posterior.

<div dir="rtl">

**تمرین 4 ★★ (Metropolis–Hastings با پیشنهاد نامتقارن).** از $d$ با یک پیشنهاد گام تصادفی **log-normal**، $\ln d' \sim \mathcal{N}(\ln d, 0.1)$، که هرگز مقادیر منفی پیشنهاد نمی‌دهد، نمونه بگیرید. تصحیح Hastings یعنی $q(d\mid d')/q(d'\mid d) = d'/d$ را استخراج و اعمال کنید. نشان دهید حذف این تصحیح پسین را سوگیر می‌کند.

</div>

**Exercise 5 ★★★ (Advanced: adaptive tuning).** Write a warm-up phase that adjusts the proposal SDs every 500 iterations to push the acceptance rate toward 0.3 (e.g., multiply the SD by 1.2 if the rate is too high, by 0.8 if too low), then freezes them for the main run. Why must the adaptation stop before the samples you keep?

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: تنظیم تطبیقی).** یک مرحله‌ی warm-up بنویسید که هر 500 تکرار انحراف معیارهای پیشنهادی را تنظیم کند تا نرخ پذیرش به سمت 0.3 برود (مثلاً اگر نرخ خیلی بالاست SD را در 1.2 و اگر خیلی پایین است در 0.8 ضرب کنید)، و بعد آن‌ها را برای اجرای اصلی ثابت کند. چرا تطبیق باید پیش از نمونه‌هایی که نگه می‌دارید متوقف شود؟

</div>

### Lab check-off · lab check-off

Show: (1) the validation of your sampler against the exact Beta posterior (Part B), (2) the trace plots and summary for the power model with the comparison to the grid (Part C), and (3) the tuning figure with acceptance rates (Part D).

<div dir="rtl">

نشان دهید: (1) اعتبارسنجی نمونه‌گیرتان در برابر پسین دقیق Beta (بخش B)، (2) trace plotها و خلاصه برای مدل توانی همراه با مقایسه با شبکه (بخش C)، و (3) نمودار تنظیم با نرخ‌های پذیرش (بخش D).

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Sampling answers from an LLM is Monte Carlo.** Because an LLM samples its output (Week 1 box), asking the same question several times gives different answers. A popular trick called **self-consistency** samples $k$ answers and takes the majority vote [Wang et al., 2023, ICLR]. Does it help, and how much? This is a Monte Carlo question: we cannot compute the majority-vote accuracy easily in closed form, but we can simulate it and report the Monte Carlo standard error, as in this week's lab.

<div dir="rtl">

**نمونه‌گیری جواب از یک LLM همان Monte Carlo است.** چون یک LLM خروجی‌اش را نمونه‌گیری می‌کند (کادر هفته‌ی 1)، پرسیدن چندباره‌ی یک سؤال جواب‌های مختلفی می‌دهد. ترفند رایجی به نام **self-consistency** تعداد $k$ جواب نمونه‌گیری می‌کند و رأی اکثریت را می‌گیرد [Wang et al., 2023, ICLR]. آیا کمک می‌کند، و چقدر؟ این یک سؤال Monte Carlo است: دقت رأی اکثریت را به‌راحتی نمی‌توانیم به‌صورت بسته حساب کنیم، ولی می‌توانیم شبیه‌سازی‌اش کنیم و خطای استاندارد Monte Carlo را گزارش کنیم، مثل lab این هفته.

</div>

> **Code · کد:** [`code/week11.py`](code/week11.py), cell 7 · سلول 7

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
k =  1 samples: majority-vote accuracy = 0.406 (MCSE 0.003)
k =  5 samples: majority-vote accuracy = 0.506 (MCSE 0.004)
k = 15 samples: majority-vote accuracy = 0.671 (MCSE 0.003)
k = 45 samples: majority-vote accuracy = 0.873 (MCSE 0.002)
```

**Try it (no API needed).**
- ★ Change `p_answer` so that one *wrong* answer is the most likely (e.g., `[0.30, 0.35, 0.20, 0.15]`). What does majority voting do now? Why?
- ★★ How many simulated questions (`n_sim`) do you need for an MCSE of 0.001? Check your answer with the formula $\sqrt{p(1-p)/n}$.
- ★★ Connection to cognition: the "wisdom of the crowd within" idea says that averaging a person's repeated guesses improves accuracy. Which assumption of this simulation (independent samples) is unlikely to hold for repeated human guesses, or for an LLM at low temperature?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ `p_answer` را طوری عوض کنید که یک جواب *غلط* محتمل‌ترین باشد (مثلاً `[0.30, 0.35, 0.20, 0.15]`). حالا رأی اکثریت چه می‌کند؟ چرا؟
- ★★ برای MCSE برابر 0.001 به چند سؤال شبیه‌سازی‌شده (`n_sim`) نیاز دارید؟ جوابتان را با فرمول $\sqrt{p(1-p)/n}$ بررسی کنید.
- ★★ ارتباط با شناخت: ایده‌ی «خرد جمعی درون فرد» (wisdom of the crowd within) می‌گوید میانگین گرفتن از حدس‌های تکراری یک نفر دقت را بالا می‌برد. کدام فرض این شبیه‌سازی (نمونه‌های مستقل) احتمالاً برای حدس‌های تکراری انسان، یا برای یک LLM با دمای پایین، برقرار نیست؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **Dropping rejected steps** instead of repeating the current value. This biases the sample toward the tails.
2. **Using the normalized posterior.** Not needed and usually impossible; the evidence cancels in the ratio.
3. **Computing the ratio without logs.** Likelihoods underflow. Compare log densities.
4. **Forgetting the prior support.** Proposals outside the support must get $\ln\tilde p = -\infty$, otherwise the likelihood may be evaluated at impossible values (e.g., negative probabilities produce `nan`).
5. **Judging the sampler only by acceptance rate.** A 30% rate does not guarantee convergence. Look at traces and autocorrelation, and run several chains (Week 12).
6. **Keeping the burn-in** or tuning the proposal during the samples you keep. Both bias the results.
7. **"More iterations always fix it."** If the chain is stuck in one mode, or the proposal is badly scaled, more iterations of the same chain may not help in practical time. Diagnose first.
8. **Forgetting the Hastings correction** with asymmetric proposals.

<div dir="rtl">

1. **حذف گام‌های ردشده** به‌جای تکرار مقدار فعلی. این کار نمونه را به سمت دنباله‌ها سوگیر می‌کند.
2. **استفاده از پسین نرمال‌شده.** لازم نیست و معمولاً ممکن هم نیست؛ شواهد در نسبت ساده می‌شود.
3. **محاسبه‌ی نسبت بدون لگاریتم.** درست‌نمایی‌ها سرریز می‌کنند. لگاریتم چگالی‌ها را مقایسه کنید.
4. **فراموش کردن تکیه‌گاه پیشین.** پیشنهادهای خارج از تکیه‌گاه باید $\ln\tilde p = -\infty$ بگیرند، وگرنه ممکن است درست‌نمایی در مقادیر ناممکن ارزیابی شود (مثلاً احتمال‌های منفی `nan` تولید می‌کنند).
5. **قضاوت درباره‌ی نمونه‌گیر فقط با نرخ پذیرش.** نرخ 30% همگرایی را تضمین نمی‌کند. به traceها و خودهمبستگی نگاه کنید و چند زنجیره اجرا کنید (هفته‌ی 12).
6. **نگه داشتن burn-in** یا تنظیم پیشنهاد در طول نمونه‌هایی که نگه می‌دارید. هر دو نتایج را سوگیر می‌کنند.
7. **«تکرار بیشتر همیشه درستش می‌کند.»** اگر زنجیره در یک مُد گیر کرده یا مقیاس پیشنهاد بد است، تکرار بیشتر همان زنجیره ممکن است در زمان معقول کمکی نکند. اول تشخیص دهید.
8. **فراموش کردن تصحیح Hastings** با پیشنهادهای نامتقارن.

</div>

---

## Check your understanding · خودآزمایی

**1.** Why is the Monte Carlo error independent of the number of parameters, while grid approximation is not?
<details><summary>Answer</summary>
The MC estimate is an average of $S$ draws, and its standard error is $\mathrm{SD}/\sqrt{S}$ regardless of the dimension of $\theta$. A grid must cover the whole parameter space, so its size grows exponentially with the number of parameters.
</details>

<div dir="rtl">

**1.** چرا خطای Monte Carlo مستقل از تعداد پارامترهاست، ولی تقریب شبکه‌ای نه؟
<details><summary>پاسخ</summary>
برآورد MC میانگین $S$ نمونه است و خطای استانداردش $\mathrm{SD}/\sqrt{S}$ است، بدون توجه به بُعد $\theta$. یک شبکه باید کل فضای پارامتر را بپوشاند، پس اندازه‌اش با تعداد پارامترها به‌طور نمایی رشد می‌کند.
</details>

</div>

**2.** In the Metropolis algorithm, why do we not need the evidence $p(\mathbf{y})$?
<details><summary>Answer</summary>
Acceptance depends only on the *ratio* of posterior densities at the proposed and current values; $p(\mathbf{y})$ appears in both and cancels.
</details>

<div dir="rtl">

**2.** در الگوریتم Metropolis چرا به شواهد $p(\mathbf{y})$ نیاز نداریم؟
<details><summary>پاسخ</summary>
پذیرش فقط به *نسبت* چگالی‌های پسین در مقدار پیشنهادی و فعلی بستگی دارد؛ $p(\mathbf{y})$ در هر دو ظاهر می‌شود و ساده می‌شود.
</details>

</div>

**3.** Current $\tilde p(\theta) = 0.004$, proposed $\tilde p(\theta') = 0.001$, and $u = 0.18$. Accept or reject? What if $u = 0.31$?
<details><summary>Answer</summary>
The ratio is 0.25. With $u = 0.18 < 0.25$, accept; with $u = 0.31 > 0.25$, reject and repeat the current value.
</details>

<div dir="rtl">

**3.** $\tilde p(\theta) = 0.004$ فعلی، $\tilde p(\theta') = 0.001$ پیشنهادی و $u = 0.18$. پذیرش یا رد؟ اگر $u = 0.31$ باشد چه؟
<details><summary>پاسخ</summary>
نسبت 0.25 است. با $u = 0.18 < 0.25$ بپذیرید؛ با $u = 0.31 > 0.25$ رد کنید و مقدار فعلی را تکرار کنید.
</details>

</div>

**4.** A chain has acceptance rate 0.97. What is probably wrong, and how does its trace look?
<details><summary>Answer</summary>
The proposal SD is too small: almost every tiny step is accepted, the chain explores very slowly, and the trace looks like a slowly wandering line with high autocorrelation. Increase the proposal SD.
</details>

<div dir="rtl">

**4.** نرخ پذیرش یک زنجیره 0.97 است. احتمالاً چه مشکلی هست و trace آن چه شکلی دارد؟
<details><summary>پاسخ</summary>
انحراف معیار پیشنهادی خیلی کوچک است: تقریباً هر گام ریزی پذیرفته می‌شود، زنجیره خیلی آرام کاوش می‌کند و trace مثل خطی است که آرام سرگردان است و خودهمبستگی بالایی دارد. انحراف معیار پیشنهادی را بزرگ کنید.
</details>

</div>

**5.** What is burn-in, and how do you decide its length?
<details><summary>Answer</summary>
The initial iterations, before the chain has reached the high-probability region, which still reflect the arbitrary starting value. Choose the length from trace plots (and from several chains started at different points), and discard those iterations.
</details>

<div dir="rtl">

**5.** burn-in چیست و طولش را چطور تعیین می‌کنید؟
<details><summary>پاسخ</summary>
تکرارهای اولیه، پیش از رسیدن زنجیره به ناحیه‌ی پراحتمال، که هنوز بازتاب مقدار شروع دلخواه‌اند. طولش را از روی trace plotها (و از چند زنجیره که از نقاط مختلف شروع شده‌اند) انتخاب کنید و آن تکرارها را دور بریزید.
</details>

</div>

**6.** When is the Hastings correction needed? Give an example.
<details><summary>Answer</summary>
When the proposal is asymmetric, $q(\theta'\mid\theta) \ne q(\theta\mid\theta')$, e.g., a log-normal proposal for a positive rate, or a proposal that depends on the current value's position in a bounded interval.
</details>

<div dir="rtl">

**6.** تصحیح Hastings کی لازم است؟ یک مثال بزنید.
<details><summary>پاسخ</summary>
وقتی پیشنهاد نامتقارن است، $q(\theta'\mid\theta) \ne q(\theta\mid\theta')$؛ مثلاً پیشنهاد log-normal برای یک نرخ مثبت، یا پیشنهادی که به موقعیت مقدار فعلی در یک بازه‌ی کران‌دار بستگی دارد.
</details>

</div>

**7.** How do you obtain the posterior of the half-life $t_{1/2} = 2^{1/d} - 1$ from MCMC samples of $d$?
<details><summary>Answer</summary>
Transform every sample of $d$ into a half-life and summarize the transformed samples (mean, percentiles, HDI). No extra derivation is needed; this is one of the big practical advantages of sampling.
</details>

<div dir="rtl">

**7.** پسین نیمه‌عمر $t_{1/2} = 2^{1/d} - 1$ را از نمونه‌های MCMC $d$ چطور به دست می‌آورید؟
<details><summary>پاسخ</summary>
هر نمونه‌ی $d$ را به یک نیمه‌عمر تبدیل کنید و نمونه‌های تبدیل‌شده را خلاصه کنید (میانگین، صدک‌ها، HDI). هیچ استخراج اضافه‌ای لازم نیست؛ این یکی از مزیت‌های عملی بزرگ نمونه‌گیری است.
</details>

</div>

---

## Assignment · تکلیف

No new graded assignment this week. **A4 (Bayesian analysis by grid)** is due at the start of the Week 12 lecture. **A5 (MCMC from scratch)** is released in Week 12 and builds directly on today's `metropolis` function, so keep your lab notebook tidy.

<div dir="rtl">

این هفته تکلیف نمره‌دار جدیدی نداریم. **A4 (تحلیل بیزی با شبکه)** در ابتدای درس هفته‌ی 12 تحویل داده می‌شود. **A5 (MCMC از صفر)** در هفته‌ی 12 منتشر می‌شود و مستقیماً روی تابع `metropolis` امروز ساخته می‌شود، پس notebook lab را مرتب نگه دارید.

</div>

**Optional practice (ungraded):** Exercise 2 (multiple starting points) is the best preparation for Week 12.

<div dir="rtl">

**تمرین اختیاری (بدون نمره):** تمرین 2 (چند نقطه‌ی شروع) بهترین آمادگی برای هفته‌ی 12 است.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Kruschke (2014), chapter 7.** Markov chain Monte Carlo: an intuitive introduction to the Metropolis algorithm (the "politician" example), its logic and representativeness of samples. *(Main reading.)*
- **Farrell & Lewandowsky (2018), chapter 7.** Bayesian parameter estimation with MCMC, applied to cognitive models.
- **Martin, Kumar & Lao (2021)**: the sections on inference engines and MCMC [verify chapter].

<div dir="rtl">

- **Kruschke (2014)، فصل 7.** Markov chain Monte Carlo: مقدمه‌ای شهودی بر الگوریتم Metropolis (مثال «سیاستمدار»)، منطق آن و نماینده بودن نمونه‌ها. *(منبع اصلی.)*
- **Farrell & Lewandowsky (2018)، فصل 7.** برآورد بیزی پارامتر با MCMC، به‌کاررفته روی مدل‌های شناختی.
- **Martin, Kumar & Lao (2021)**: بخش‌های موتورهای استنباط و MCMC [شماره‌ی فصل بررسی شود].

</div>

*Preview for Week 12:* Gibbs sampling (no rejections at all), and the question every MCMC user must answer: has my chain converged? We will compute R-hat and the effective sample size ourselves, then check them against ArviZ.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 12:* نمونه‌گیری Gibbs (بدون هیچ ردی)، و سؤالی که هر کاربر MCMC باید جواب دهد: آیا زنجیره‌ام همگرا شده است؟ R-hat و اندازه‌ی مؤثر نمونه را خودمان حساب می‌کنیم و بعد با ArviZ بررسی می‌کنیم.

</div>
