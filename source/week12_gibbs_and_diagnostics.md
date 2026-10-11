# Week 12: Gibbs Sampling and Convergence Diagnostics · هفته‌ی 12: نمونه‌گیری Gibbs و تشخیص همگرایی

> **Chapter 5: Parameter estimation with data-driven methods (MCMC)** · Lecture 1 h · Lab 2 h
> **Running data:** log response times of one participant (a normal model with unknown mean and precision), and the power forgetting model sampled with last week's Metropolis sampler.

<div dir="rtl">

> **فصل 5: برآورد پارامتر با روش‌های داده‌محور (MCMC)** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** لگاریتم زمان‌های واکنش یک شرکت‌کننده (مدل نرمال با میانگین و دقت نامعلوم)، و مدل فراموشی توانی که با نمونه‌گیر Metropolis هفته‌ی قبل نمونه‌گیری می‌شود.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| Gibbs sampling | نمونه‌گیری Gibbs | به‌روزرسانی هر پارامتر از توزیع شرطی کاملش |
| convergence | همگرایی | رسیدن زنجیره‌ها به توزیع هدف |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| Markov chain Monte Carlo (MCMC) | زنجیره‌ی مارکوف Monte Carlo | نمونه‌گیری از پسین با یک زنجیره‌ی تصادفی |
| response time (RT) | زمان واکنش | فاصله‌ی ارائه‌ی محرک تا پاسخ |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| Metropolis algorithm | الگوریتم Metropolis | پیشنهاد یک حرکت و پذیرش یا رد آن |
| sampler | نمونه‌گیر (sampler) | الگوریتمی که از توزیع نمونه می‌گیرد |
| full conditional | توزیع شرطی کامل (full conditional) | توزیع یک پارامتر به شرط بقیه و داده |
| conjugate prior | پیشین مزدوج (conjugate) | پیشینی که پسین هم‌خانواده می‌دهد |
| R-hat | R-hat | مقایسه‌ی واریانس بین و درون زنجیره‌ها؛ باید ≈ 1 باشد |
| effective sample size (ESS) | اندازه‌ی مؤثر نمونه (ESS) | تعداد نمونه‌ی مستقل هم‌ارز |
| chain | زنجیره | دنباله‌ی نمونه‌های MCMC |
| trace plot | نمودار trace | مقدار نمونه‌ها در برابر شماره‌ی تکرار |
| Monte Carlo | Monte Carlo (مونت‌کارلو) | تقریب با میانگین نمونه‌های تصادفی |
| proposal | پیشنهاد (proposal) | مقدار جدیدی که الگوریتم امتحان می‌کند |
| posterior | توزیع پسین (posterior) | باور درباره‌ی پارامتر بعد از دیدن داده |
| MCSE | خطای استاندارد Monte Carlo | خطای شبیه‌سازی در میانگین پسین |
| prior | توزیع پیشین (prior) | باور درباره‌ی پارامتر پیش از دیدن داده |
| HMC / NUTS | Hamiltonian Monte Carlo / NUTS | MCMC مبتنی بر گرادیان |
| burn-in / warm-up | دوره‌ی گرم‌شدن (burn-in) | نمونه‌های اولیه که دور ریخته می‌شوند |
| autocorrelation | خودهمبستگی | وابستگی نمونه‌های پشت سر هم |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Derive** the full conditional distributions of a semi-conjugate normal model and **implement** a Gibbs sampler from scratch.
2. **Explain** when Gibbs sampling is efficient and when it mixes slowly (correlated parameters), and how Metropolis-within-Gibbs handles non-conjugate conditionals.
3. **Implement** split-$\hat R$ and the effective sample size (ESS), and **verify** them against ArviZ.
4. **Diagnose** non-convergence from multiple chains using trace plots, $\hat R$, ESS and the Monte Carlo standard error.
5. **Apply** a reporting checklist for MCMC results.

<div dir="rtl">

1. full conditionalها یک مدل نرمال semi-conjugate را **استخراج کنند** و یک نمونه‌گیر Gibbs را از صفر **پیاده‌سازی کنند**.
2. **توضیح دهند** که نمونه‌گیری Gibbs کی کاراست و کی کند مخلوط می‌شود (پارامترهای همبسته)، و Metropolis-within-Gibbs چطور full conditionalهای non-conjugate را مدیریت می‌کند.
3. split-$\hat R$ و اندازه‌ی مؤثر نمونه (ESS) را **پیاده‌سازی کنند** و با ArviZ **بررسی کنند**.
4. عدم همگرایی را از روی چند زنجیره با trace plot، $\hat R$، ESS و خطای استاندارد Monte Carlo **تشخیص دهند**.
5. یک چک‌لیست گزارش‌دهی برای نتایج MCMC را **به کار ببرند**.

</div>

---

## Motivation & big picture · مقدمه

Last week's Metropolis sampler had one tuning knob, the proposal SD, and a nagging question: *how do we know the chain has converged?* This week answers both concerns.

<div dir="rtl">

نمونه‌گیر Metropolis هفته‌ی قبل یک پیچ تنظیم داشت، یعنی انحراف معیار پیشنهادی، و یک سؤال آزاردهنده: *از کجا بدانیم زنجیره همگرا شده است؟* این هفته به هر دو نگرانی جواب می‌دهد.

</div>

**Gibbs sampling** removes the tuning problem for a large and important class of models. Instead of proposing a jump for all parameters and sometimes rejecting it, it updates **one parameter at a time**, drawing it *exactly* from its distribution given the current values of all the others. Every draw is accepted. Many classic Bayesian programs (BUGS, JAGS, used throughout Lee & Wagenmakers and Kruschke) are built on this idea.

<div dir="rtl">

**نمونه‌گیری Gibbs** مسئله‌ی تنظیم را برای دسته‌ی بزرگ و مهمی از مدل‌ها حذف می‌کند. به‌جای پیشنهاد یک پرش برای همه‌ی پارامترها و گاهی رد آن، هر بار **یک پارامتر** را به‌روز می‌کند و آن را *دقیقاً* از توزیعش به شرط مقادیر فعلی همه‌ی پارامترهای دیگر می‌کشد. هر نمونه‌ای پذیرفته می‌شود. بسیاری از برنامه‌های کلاسیک بیزی (BUGS، JAGS، که در سراسر کتاب‌های Lee & Wagenmakers و Kruschke استفاده می‌شوند) بر همین ایده ساخته شده‌اند.

</div>

**Convergence diagnostics** are the honest part of MCMC. A chain is only useful if it has (a) forgotten its starting point and (b) explored the whole posterior, and nothing in a single chain proves either. The standard remedy is to run **several chains from different starting points** and check that they agree. $\hat R$ quantifies "do the chains agree?", and the ESS quantifies "how much independent information do the correlated draws contain?". No MCMC result should be reported without them.

<div dir="rtl">

**تشخیص همگرایی** بخش صادقانه‌ی MCMC است. یک زنجیره فقط وقتی مفید است که (الف) نقطه‌ی شروعش را فراموش کرده باشد و (ب) کل پسین را کاوش کرده باشد، و هیچ چیزی در یک زنجیره‌ی تنها هیچ‌کدام را ثابت نمی‌کند. راه‌حل استاندارد اجرای **چند زنجیره از نقاط شروع مختلف** و بررسی توافق آن‌هاست. $\hat R$ این را کمّی می‌کند که «آیا زنجیره‌ها توافق دارند؟»، و ESS این را که «نمونه‌های همبسته چقدر اطلاعات مستقل دارند؟». هیچ نتیجه‌ی MCMC نباید بدون این‌ها گزارش شود.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Every published MCMC analysis** must report convergence diagnostics; reviewers in psychology and neuroscience now routinely ask for $\hat R$ and ESS.
- **Gibbs sampling** powers the classic Bayesian programs BUGS and JAGS, which are used in many cognitive modeling textbooks (Lee & Wagenmakers, Kruschke) and in ecology, epidemiology and education research.
- **Image processing and communications**: Gibbs samplers have been used for image restoration and for detection in multi-antenna (MIMO) receivers.
- **Topic models** (finding themes in large text collections) were classically fitted with Gibbs sampling.

<div dir="rtl">

- **هر تحلیل MCMC منتشرشده** باید شاخص‌های همگرایی را گزارش کند؛ داوران در روان‌شناسی و علوم اعصاب امروز به‌طور معمول $\hat R$ و ESS را می‌خواهند.
- **نمونه‌گیری Gibbs** پایه‌ی برنامه‌های بیزی کلاسیک BUGS و JAGS است که در بسیاری از کتاب‌های درسی مدل‌سازی شناختی (Lee & Wagenmakers، Kruschke) و در پژوهش‌های بوم‌شناسی، همه‌گیرشناسی و آموزش استفاده می‌شوند.
- **پردازش تصویر و مخابرات:** نمونه‌گیرهای Gibbs برای بازسازی تصویر و برای آشکارسازی در گیرنده‌های چندآنتنی (MIMO) به کار رفته‌اند.
- **مدل‌های موضوعی (topic models)** برای پیدا کردن موضوع‌ها در مجموعه‌های بزرگ متن، به‌طور کلاسیک با نمونه‌گیری Gibbs برازش می‌شدند.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

Metropolis needs a well-chosen step size. **Gibbs sampling** avoids that for many models by updating **one parameter at a time**: fix all the other parameters at their current values, and draw the chosen parameter directly from its exact distribution under those conditions (its **full conditional**). Then move to the next parameter, and so on. Nothing is ever rejected. The second half of the week answers the uncomfortable question "has my sampler actually worked?". We run **several chains** from very different starting points. If they all end up describing the same distribution, that is good evidence of convergence; $\hat R$ ("R-hat") is a single number that measures whether the chains agree (it should be below 1.01). Because neighboring draws are correlated, 4,000 draws may contain only the information of, say, 1,000 independent ones: that number is the **effective sample size (ESS)**, and it tells us how precise our averages are.

<div dir="rtl">

Metropolis به یک اندازه‌ی گام خوب‌انتخاب‌شده نیاز دارد. **نمونه‌گیری Gibbs** برای بسیاری از مدل‌ها از این مشکل دوری می‌کند، چون **هر بار یک پارامتر** را به‌روز می‌کند: همه‌ی پارامترهای دیگر را روی مقدار فعلی‌شان ثابت نگه دار و پارامتر انتخاب‌شده را مستقیم از توزیع دقیقش در همان شرایط بکش (**full conditional** آن). بعد سراغ پارامتر بعدی برو و همین‌طور ادامه بده. هیچ‌وقت چیزی رد نمی‌شود. نیمه‌ی دوم هفته به این سؤال ناخوشایند جواب می‌دهد: «آیا نمونه‌گیر من واقعاً کار کرده؟» **چند زنجیره** را از نقطه‌های شروع خیلی متفاوت اجرا می‌کنیم. اگر همه به توصیف یک توزیع برسند، شاهد خوبی برای همگرایی است؛ $\hat R$ («R-hat») یک عدد است که می‌سنجد زنجیره‌ها با هم توافق دارند یا نه (باید کمتر از 1.01 باشد). چون نمونه‌های پشت سر هم همبسته‌اند، 4,000 نمونه ممکن است فقط اطلاعات مثلاً 1,000 نمونه‌ی مستقل را داشته باشند: این عدد **اندازه‌ی مؤثر نمونه (ESS)** است و می‌گوید میانگین‌های ما چقدر دقیق‌اند.

</div>

**Suggested timing (60 min):** Gibbs sampling 20 · when Gibbs struggles 5 · convergence and multiple chains 8 · $\hat R$ 10 · ESS and MCSE 10 · reporting checklist 7.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** نمونه‌گیری Gibbs 20 · وقتی Gibbs به زحمت می‌افتد 5 · همگرایی و چند زنجیره 8 · $\hat R$ 10 · ESS و MCSE 10 · چک‌لیست گزارش‌دهی 7.

</div>

### 1. Gibbs sampling · 1. نمونه‌گیری Gibbs

For parameters $\boldsymbol\theta = (\theta_1, \dots, \theta_k)$, the **full conditional** of $\theta_m$ is its posterior given the data and *all other* parameters, $p(\theta_m \mid \boldsymbol\theta_{-m}, \mathbf{y})$. Gibbs sampling cycles through them:

<div dir="rtl">

برای پارامترهای $\boldsymbol\theta = (\theta_1, \dots, \theta_k)$، **full conditional** $\theta_m$ پسین آن به شرط داده و *همه‌ی* پارامترهای دیگر است، $p(\theta_m \mid \boldsymbol\theta_{-m}, \mathbf{y})$. نمونه‌گیری Gibbs بین آن‌ها می‌چرخد:

</div>

1. Start at $\boldsymbol\theta^{(0)}$.
2. For $s = 1, \dots, S$:
   - draw $\theta_1^{(s)} \sim p(\theta_1 \mid \theta_2^{(s-1)}, \dots, \theta_k^{(s-1)}, \mathbf{y})$
   - draw $\theta_2^{(s)} \sim p(\theta_2 \mid \theta_1^{(s)}, \theta_3^{(s-1)}, \dots, \mathbf{y})$
   - … (always using the newest values)
   - draw $\theta_k^{(s)} \sim p(\theta_k \mid \theta_1^{(s)}, \dots, \theta_{k-1}^{(s)}, \mathbf{y})$

<div dir="rtl">

1. از $\boldsymbol\theta^{(0)}$ شروع کنید.
2. برای $s = 1, \dots, S$:
   - بکشید $\theta_1^{(s)} \sim p(\theta_1 \mid \theta_2^{(s-1)}, \dots, \theta_k^{(s-1)}, \mathbf{y})$
   - بکشید $\theta_2^{(s)} \sim p(\theta_2 \mid \theta_1^{(s)}, \theta_3^{(s-1)}, \dots, \mathbf{y})$
   - … (همیشه با جدیدترین مقادیر)
   - بکشید $\theta_k^{(s)} \sim p(\theta_k \mid \theta_1^{(s)}, \dots, \theta_{k-1}^{(s)}, \mathbf{y})$

</div>

It is a special case of Metropolis–Hastings in which the proposal is the full conditional itself, so the acceptance probability is always 1.

<div dir="rtl">

این حالت خاصی از Metropolis–Hastings است که در آن پیشنهاد خود full conditional است، پس احتمال پذیرش همیشه 1 است.

</div>

**Finding full conditionals.** Write the joint density $p(\mathbf{y}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)$, keep only the factors that contain $\theta_m$, and recognize a known distribution. This works when priors are (conditionally) **conjugate**.

<div dir="rtl">

**پیدا کردن full conditionalها.** چگالی مشترک $p(\mathbf{y}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)$ را بنویسید، فقط ضرایبی را که $\theta_m$ دارند نگه دارید، و یک توزیع شناخته‌شده را تشخیص دهید. این وقتی کار می‌کند که پیشین‌ها (به‌طور شرطی) **conjugate** باشند.

</div>

**Example: a normal model for log RTs.** Let $y_i$ be log response times, $y_i \sim \mathcal{N}(\mu, 1/\sqrt{\tau})$, where $\tau = 1/\sigma^2$ is the **precision**. Priors: $\mu \sim \mathcal{N}(m_0, s_0)$ and $\tau \sim \mathrm{Gamma}(a_0, \text{rate } b_0)$, independent. Then:

<div dir="rtl">

**مثال: یک مدل نرمال برای لگاریتم زمان واکنش.** فرض کنید $y_i$ لگاریتم زمان‌های واکنش باشند، $y_i \sim \mathcal{N}(\mu, 1/\sqrt{\tau})$، که در آن $\tau = 1/\sigma^2$ **دقت** (precision) است. پیشین‌ها: $\mu \sim \mathcal{N}(m_0, s_0)$ و $\tau \sim \mathrm{Gamma}(a_0, \text{rate } b_0)$، مستقل. آن‌وقت:

</div>

$$
\mu \mid \tau, \mathbf{y} \sim \mathcal{N}\!\left(\frac{m_0/s_0^2 + \tau \sum_i y_i}{1/s_0^2 + N\tau},\ \ \frac{1}{\sqrt{1/s_0^2 + N\tau}}\right),
$$

$$
\tau \mid \mu, \mathbf{y} \sim \mathrm{Gamma}\!\left(a_0 + \frac{N}{2},\ \ \text{rate} = b_0 + \frac12\sum_i (y_i - \mu)^2\right).
$$

**Reading the formulas.** The conditional mean of $\mu$ is a precision-weighted average of the prior mean and the data mean (as in the beta-binomial of Week 9). The conditional distribution of $\tau$ adds half an observation to the shape and half a squared residual to the rate for each data point.

<div dir="rtl">

**خواندن فرمول‌ها.** میانگین شرطی $\mu$ میانگین وزنی (با وزن دقت) میانگین پیشین و میانگین داده است (مثل beta-binomial هفته‌ی 9). توزیع شرطی $\tau$ برای هر نقطه‌ی داده نیم مشاهده به پارامتر شکل و نیم مربع باقی‌مانده به rate اضافه می‌کند.

</div>

> **Note on parameterizations.** NumPy's `rng.gamma(shape, scale)` uses **scale** = 1/rate. Mixing up rate and scale is the most common bug in Gibbs samplers.

<div dir="rtl">

> **نکته درباره‌ی پارامترسازی‌ها.** `rng.gamma(shape, scale)` در NumPy از **scale** = 1/rate استفاده می‌کند. قاطی کردن rate و scale رایج‌ترین باگ در نمونه‌گیرهای Gibbs است.

</div>

#### Reading the math · خواندن ریاضی

- $\boldsymbol\theta_{-m}$: "all parameters except $\theta_m$".
- **Precision** $\tau = 1/\sigma^2$: the inverse of the variance. Large precision = small noise. Working with precisions makes combining information a simple addition.
- **The $\mu$ update:** the conditional mean $\dfrac{m_0/s_0^2 + \tau\sum y_i}{1/s_0^2 + N\tau}$ is a weighted average of the prior mean $m_0$ (weight $1/s_0^2$, the prior's precision) and the data mean (total weight $N\tau$, the data's precision). The conditional precision is the *sum* of the two precisions. Worked example: $1 + 4\times10 = 41$, so the data dominate.
- **The $\tau$ update:** a Gamma distribution whose shape grows by $1/2$ per observation and whose rate grows by half of each squared residual. Its mean, shape/rate, is roughly "1 / (average squared residual)", i.e. the precision suggested by the data.

<div dir="rtl">

- $\boldsymbol\theta_{-m}$: «همه‌ی پارامترها به‌جز $\theta_m$».
- **دقت (precision)** $\tau = 1/\sigma^2$: معکوس واریانس. دقت زیاد = نویز کم. کار کردن با دقت‌ها ترکیب اطلاعات را به یک جمع ساده تبدیل می‌کند.
- **به‌روزرسانی $\mu$:** میانگین شرطی $\dfrac{m_0/s_0^2 + \tau\sum y_i}{1/s_0^2 + N\tau}$ میانگین وزنی میانگین prior یعنی $m_0$ (با وزن $1/s_0^2$، دقت prior) و میانگین داده (با وزن کل $N\tau$، دقت داده) است. دقت شرطی *جمع* این دو دقت است. مثال حل‌شده: $1 + 4\times10 = 41$، پس داده غالب است.
- **به‌روزرسانی $\tau$:** یک توزیع Gamma که shape آن برای هر مشاهده $1/2$ و rate آن به اندازه‌ی نصف هر مربع باقی‌مانده بزرگ می‌شود. میانگین آن، shape/rate، تقریباً «1 / (میانگین مربع باقی‌مانده)» است، یعنی همان دقتی که داده نشان می‌دهد.

</div>

### 2. When Gibbs struggles, and Metropolis-within-Gibbs · 2. وقتی Gibbs به زحمت می‌افتد، و Metropolis-within-Gibbs

- **Strong posterior correlations.** Gibbs moves parallel to the coordinate axes. If the posterior is a narrow diagonal ridge (like the $A$–$d$ trade-off of the power model), each step can move only a tiny distance, and the chain zig-zags slowly along the ridge. Remedies: reparameterize, update correlated parameters jointly ("blocking"), or use gradient-based samplers (Week 13).
- **Non-conjugate conditionals.** Most cognitive models (forgetting curves, SDT, the GCM) have no closed-form conditionals. **Metropolis-within-Gibbs** updates each parameter with a one-dimensional Metropolis step targeting its full conditional, and uses exact Gibbs draws where available.

<div dir="rtl">

- **همبستگی‌های قوی پسین.** Gibbs موازی با محورهای مختصات حرکت می‌کند. اگر پسین یک ridge باریک مورب باشد (مثل trade-off $A$–$d$ مدل توانی)، هر گام فقط فاصله‌ی ریزی می‌تواند حرکت کند و زنجیره آرام در امتداد ridge زیگزاگ می‌زند. راه‌حل‌ها: reparameterization، به‌روزرسانی هم‌زمان پارامترهای همبسته («بلوک‌بندی»)، یا نمونه‌گیرهای گرادیانی (هفته‌ی 13).
- **full conditionalهای non-conjugate.** بیشتر مدل‌های شناختی (منحنی‌های فراموشی، SDT، GCM) توزیع شرطی بسته ندارند. **Metropolis-within-Gibbs** هر پارامتر را با یک گام Metropolis یک‌بعدی که full conditionalش را هدف می‌گیرد به‌روز می‌کند، و هر جا ممکن باشد از نمونه‌های دقیق Gibbs استفاده می‌کند.

</div>

> **Advanced:** JAGS and BUGS automatically pick a sampler for each parameter (conjugate Gibbs, slice sampling, adaptive Metropolis), which is why they run on almost any model. Modern Hamiltonian Monte Carlo (Stan, PyMC's NUTS) instead uses the gradient of the log posterior to move all parameters jointly along the posterior's geometry, and handles correlated posteriors far better (Week 13).

<div dir="rtl">

> **پیشرفته:** JAGS و BUGS برای هر پارامتر خودکار یک نمونه‌گیر انتخاب می‌کنند (Gibbs conjugate، slice sampling، Metropolis تطبیقی)، و به همین دلیل روی تقریباً هر مدلی اجرا می‌شوند. Hamiltonian Monte Carlo امروزی (Stan، NUTS در PyMC) در عوض از گرادیان لگاریتم پسین استفاده می‌کند تا همه‌ی پارامترها را هم‌زمان در امتداد هندسه‌ی پسین حرکت دهد، و پسین‌های همبسته را خیلی بهتر مدیریت می‌کند (هفته‌ی 13).

</div>

### 3. Convergence: the logic of multiple chains · 3. همگرایی: منطق چند زنجیره

An MCMC chain has converged when its draws are representative of the posterior. Two failure modes:
1. **Not yet stationary:** the chain still reflects the starting value.
2. **Stuck or slow:** the chain explores only part of the posterior (e.g., one of two modes, or one end of a long ridge).

<div dir="rtl">

یک زنجیره‌ی MCMC وقتی همگرا شده که نمونه‌هایش نماینده‌ی پسین باشند. دو حالت شکست:
1. **هنوز ایستا نشده:** زنجیره هنوز بازتاب مقدار شروع است.
2. **گیرکرده یا کند:** زنجیره فقط بخشی از پسین را کاوش می‌کند (مثلاً یکی از دو مُد، یا یک سر یک ridge طولانی).

</div>

Neither can be detected reliably from one chain, because a chain stuck in one region can look perfectly stable. Run $C \ge 4$ chains from **over-dispersed** starting points: if they all end up describing the same distribution, that is good (though never conclusive) evidence of convergence.

<div dir="rtl">

هیچ‌کدام را نمی‌شود با اطمینان از یک زنجیره تشخیص داد، چون زنجیره‌ای که در یک ناحیه گیر کرده می‌تواند کاملاً پایدار به نظر برسد. $C \ge 4$ زنجیره از نقاط شروع **بیش‌پراکنده** (over-dispersed) اجرا کنید: اگر همه به توصیف همان توزیع برسند، این شاهد خوبی (هرچند هرگز قطعی نیست) برای همگرایی است.

</div>

**Trace plots** of all chains overlaid should look like one well-mixed "hairy caterpillar", with no chain visibly separated or trending.

<div dir="rtl">

**trace plotهای** همه‌ی زنجیره‌ها روی هم باید مثل یک «کرم پشمالوی» خوب مخلوط‌شده باشند، بدون زنجیره‌ای که آشکارا جدا افتاده یا روند دارد.

</div>

### 4. The potential scale reduction factor $\hat R$ · 4. ضریب کاهش مقیاس بالقوه $\hat R$

Compare the variance **between** chains with the variance **within** chains. With $C$ chains of length $S$ (after burn-in), chain means $\bar\theta_c$ and within-chain variances $s_c^2$:

<div dir="rtl">

واریانس **بین** زنجیره‌ها را با واریانس **درون** زنجیره‌ها مقایسه کنید. با $C$ زنجیره به طول $S$ (بعد از burn-in)، میانگین زنجیره‌ها $\bar\theta_c$ و واریانس‌های درون‌زنجیره‌ای $s_c^2$:

</div>

$$
W = \frac{1}{C}\sum_c s_c^2, \qquad
B = \frac{S}{C-1}\sum_c (\bar\theta_c - \bar\theta)^2, \qquad
\widehat{\mathrm{var}}^{+} = \frac{S-1}{S}\,W + \frac{1}{S}\,B, \qquad
\hat R = \sqrt{\frac{\widehat{\mathrm{var}}^{+}}{W}}.
$$

If the chains have not mixed, $B$ is large relative to $W$ and $\hat R > 1$. As chains converge, $\hat R \to 1$.

<div dir="rtl">

اگر زنجیره‌ها مخلوط نشده باشند، $B$ نسبت به $W$ بزرگ است و $\hat R > 1$. با همگرا شدن زنجیره‌ها، $\hat R \to 1$.

</div>

- **Split-$\hat R$:** split each chain into a first and a second half and treat them as $2C$ chains. This also detects a single chain that is still drifting.
- **Threshold:** the classic rule was $\hat R < 1.1$; current recommendations (Vehtari et al., 2021) use $\hat R < 1.01$, computed after rank-normalization (as ArviZ does).

<div dir="rtl">

- **Split-$\hat R$:** هر زنجیره را به نیمه‌ی اول و دوم تقسیم کنید و با آن‌ها مثل $2C$ زنجیره رفتار کنید. این کار زنجیره‌ی تنهایی را هم که هنوز در حال drift است تشخیص می‌دهد.
- **آستانه:** قاعده‌ی کلاسیک $\hat R < 1.1$ بود؛ توصیه‌های امروزی (Vehtari و همکاران، 2021) $\hat R < 1.01$ است که بعد از نرمال‌سازی رتبه‌ای (rank-normalization) حساب می‌شود (همان کاری که ArviZ می‌کند).

</div>

### 5. Effective sample size and Monte Carlo standard error · 5. اندازه‌ی مؤثر نمونه و خطای استاندارد Monte Carlo

Autocorrelated draws carry less information than independent ones. The **effective sample size** is

<div dir="rtl">

نمونه‌های خودهمبسته اطلاعات کمتری از نمونه‌های مستقل دارند. **اندازه‌ی مؤثر نمونه** برابر است با

</div>

$$
\mathrm{ESS} = \frac{C\cdot S}{1 + 2\sum_{h=1}^{\infty}\rho_h},
$$

where $\rho_h$ is the lag-$h$ autocorrelation, estimated from all chains and truncated when the estimates become noise. ESS is the number of *independent* draws that would give the same precision.

<div dir="rtl">

که در آن $\rho_h$ خودهمبستگی با تأخیر $h$ است که از همه‌ی زنجیره‌ها تخمین زده و وقتی تخمین‌ها نویز می‌شوند بریده می‌شود. ESS تعداد نمونه‌های *مستقلی* است که همان دقت را می‌دادند.

</div>

- The **Monte Carlo standard error** of a posterior mean is $\mathrm{MCSE} = \text{posterior SD}/\sqrt{\mathrm{ESS}}$. It must be small relative to the precision you report (e.g., don't report 3 decimals if the MCSE is 0.01).
- **Rule of thumb:** bulk-ESS ≥ 400 (with 4 chains) for reliable posterior means and intervals; tail-ESS ≥ 400 for reliable extreme quantiles.

<div dir="rtl">

- **خطای استاندارد Monte Carlo** میانگین پسین برابر $\mathrm{MCSE} = \text{posterior SD}/\sqrt{\mathrm{ESS}}$ است. باید نسبت به دقتی که گزارش می‌کنید کوچک باشد (مثلاً اگر MCSE برابر 0.01 است 3 رقم اعشار گزارش نکنید).
- **قاعده‌ی سرانگشتی:** bulk-ESS ≥ 400 (با 4 زنجیره) برای میانگین‌ها و بازه‌های پسین قابل اعتماد؛ tail-ESS ≥ 400 برای quantileهای حدی قابل اعتماد.

</div>

#### Reading the math · خواندن ریاضی

- **$\hat R$:** $W$ is the average variance *inside* each chain; $B$ measures how far the chain *means* are from each other. $\widehat{\mathrm{var}}^{+}$ is an estimate of the total posterior variance that includes the disagreement between chains. If the chains agree, $B$ adds almost nothing and $\hat R = \sqrt{\widehat{\mathrm{var}}^{+}/W} \approx 1$. In the "not converged" worked example, the two chains sit around 1.0 and 2.0, $B$ is huge and $\hat R = 4.4$.
- **ESS:** $C \cdot S$ is the total number of draws; the denominator $1 + 2\sum\rho_h$ inflates for correlated draws. With $\rho_h = 0.5^h$, the sum is $0.5 + 0.25 + \dots = 1$, so the draws count only one third: 4,000 draws are worth 1,333 independent ones.
- **MCSE** $= \text{posterior SD}/\sqrt{\mathrm{ESS}}$ is the simulation error of the reported mean; decide the number of decimals from it.

<div dir="rtl">

- **$\hat R$:** $W$ میانگین واریانس *درون* هر زنجیره است؛ $B$ می‌سنجد *میانگین‌های* زنجیره‌ها چقدر از هم دورند. $\widehat{\mathrm{var}}^{+}$ تخمینی از کل واریانس posterior است که اختلاف بین زنجیره‌ها را هم در بر دارد. اگر زنجیره‌ها توافق داشته باشند، $B$ تقریباً چیزی اضافه نمی‌کند و $\hat R = \sqrt{\widehat{\mathrm{var}}^{+}/W} \approx 1$. در مثال حل‌شده‌ی «همگرا نشده»، دو زنجیره حول 1.0 و 2.0 هستند، $B$ خیلی بزرگ است و $\hat R = 4.4$.
- **ESS:** $C \cdot S$ کل تعداد نمونه‌هاست؛ مخرج $1 + 2\sum\rho_h$ برای نمونه‌های همبسته بزرگ می‌شود. با $\rho_h = 0.5^h$ جمع برابر $0.5 + 0.25 + \dots = 1$ است، پس نمونه‌ها فقط یک‌سوم حساب می‌شوند: 4,000 نمونه ارزش 1,333 نمونه‌ی مستقل را دارند.
- **MCSE** $= \text{posterior SD}/\sqrt{\mathrm{ESS}}$ خطای شبیه‌سازی میانگین گزارش‌شده است؛ تعداد رقم‌های اعشار را از روی آن تصمیم بگیرید.

</div>

### 6. MCMC reporting checklist · 6. چک‌لیست گزارش‌دهی MCMC

1. Sampler, number of chains, iterations, burn-in (warm-up), and any thinning.
2. Starting values (dispersed?).
3. $\hat R$ (which version) and ESS for **all** reported parameters, plus the maximum $\hat R$ and minimum ESS.
4. Trace plots (in a supplement) and a statement that they were inspected.
5. Priors, and the posterior summaries with MCSE-appropriate precision.
6. A posterior predictive check (Week 10).

<div dir="rtl">

1. نمونه‌گیر، تعداد زنجیره‌ها، تکرارها، burn-in (warm-up) و هر thinning.
2. مقادیر شروع (پراکنده؟).
3. $\hat R$ (کدام نسخه) و ESS برای **همه‌ی** پارامترهای گزارش‌شده، به‌علاوه‌ی بیشترین $\hat R$ و کمترین ESS.
4. trace plotها (در پیوست) و جمله‌ای که نشان دهد بررسی شده‌اند.
5. پیشین‌ها، و خلاصه‌های پسین با دقتی متناسب با MCSE.
6. یک بررسی پیش‌بینی پسین (هفته‌ی 10).

</div>

#### For an engineer · برای یک مهندس

- **Precision-weighted averaging** in the $\mu$ update is the same rule as **maximal-ratio combining** or the Kalman measurement update: combine estimates in proportion to their inverse noise variances.
- **Gibbs sampling** updates one variable given all the others, like coordinate-wise iterative algorithms (alternating optimization) and the iterative exchange of conditional information in turbo-style receivers; Gibbs samplers have been proposed for MIMO detection.
- **$\hat R$** is a one-way ANOVA (between-group vs. within-group variance) across independent simulation runs: the same check you would do by running a Monte Carlo simulation with several seeds and verifying that the runs agree.
- **ESS** $= N/(1 + 2\sum\rho_h)$ is the standard formula for the effective number of independent samples of a correlated random process: averaging $N$ correlated samples reduces the variance only as much as averaging ESS independent ones (related to the correlation time).

<div dir="rtl">

- **میانگین‌گیری وزن‌دار با دقت** در به‌روزرسانی $\mu$ همان قاعده‌ی **ترکیب با نسبت بیشینه (MRC)** یا گام به‌روزرسانی اندازه‌گیری در فیلتر کالمن است: تخمین‌ها را به نسبت معکوس واریانس نویزشان ترکیب کن.
- **نمونه‌گیری Gibbs** هر بار یک متغیر را به شرط بقیه به‌روز می‌کند؛ مثل الگوریتم‌های تکراری مختصات‌به‌مختصات (بهینه‌سازی متناوب) و تبادل تکراری اطلاعات شرطی در گیرنده‌های از نوع turbo. نمونه‌گیرهای Gibbs برای آشکارسازی MIMO هم پیشنهاد شده‌اند.
- **$\hat R$** یک ANOVA یک‌طرفه (واریانس بین گروه‌ها در برابر درون گروه‌ها) روی اجراهای مستقل شبیه‌سازی است: همان بررسی‌ای که با اجرای یک شبیه‌سازی Monte Carlo با چند seed مختلف و وارسی توافق اجراها انجام می‌دهید.
- **ESS** $= N/(1 + 2\sum\rho_h)$ فرمول استاندارد تعداد مؤثر نمونه‌های مستقل یک فرایند تصادفی همبسته است: میانگین گرفتن از $N$ نمونه‌ی همبسته واریانس را فقط به اندازه‌ی میانگین گرفتن از ESS نمونه‌ی مستقل کم می‌کند (مرتبط با زمان همبستگی).

</div>

#### For the instructor · برای مدرس

- **Draw Gibbs on a contour plot.** Two parameters, an elliptical posterior. Gibbs moves in horizontal and vertical steps only (a staircase). Then draw a narrow diagonal ellipse: the staircase steps become tiny. That one picture explains both how Gibbs works and when it struggles.
- **Make $\hat R$ visual first:** overlay four trace plots, once with chains that agree and once with one chain stuck elsewhere. Ask "do these chains describe the same distribution?" before showing any formula.
- **Teach the reporting checklist as a habit.** Ask students to apply it to their project and to every MCMC result in the lab.
- **Typical questions.**
  - *"$\hat R$ is 1.00, so my model is correct?"* No. $\hat R$ only checks that the chains agree; the model can still be wrong (check with a PPC) or the code can still be buggy.
  - *"Should I thin my chains?"* Not for correctness; it only saves memory.
  - *"Rate or scale?"* NumPy's Gamma uses scale = 1/rate; the most common bug in student Gibbs samplers.

<div dir="rtl">

- **Gibbs را روی یک نمودار تراز رسم کنید.** دو پارامتر، یک posterior بیضوی. Gibbs فقط با گام‌های افقی و عمودی حرکت می‌کند (یک پلکان). بعد یک بیضی مورب باریک بکشید: گام‌های پلکان خیلی ریز می‌شوند. همین یک تصویر هم نحوه‌ی کار Gibbs و هم زمان به زحمت افتادنش را توضیح می‌دهد.
- **$\hat R$ را اول تصویری کنید:** چهار trace plot را روی هم بکشید، یک بار با زنجیره‌هایی که توافق دارند و یک بار با یک زنجیره که جای دیگری گیر کرده. پیش از نشان دادن هر فرمولی بپرسید «آیا این زنجیره‌ها یک توزیع را توصیف می‌کنند؟»
- **چک‌لیست گزارش را به‌عنوان یک عادت درس دهید.** از دانشجوها بخواهید آن را روی پروژه‌شان و روی هر نتیجه‌ی MCMC در lab اعمال کنند.
- **سؤال‌های رایج.**
  - *«$\hat R$ برابر 1.00 است، پس مدلم درست است؟»* نه. $\hat R$ فقط بررسی می‌کند که زنجیره‌ها توافق دارند؛ مدل هنوز می‌تواند غلط باشد (با PPC بررسی کنید) یا کد هنوز می‌تواند باگ داشته باشد.
  - *«زنجیره‌ها را thin کنم؟»* برای درستی لازم نیست؛ فقط حافظه را صرفه‌جویی می‌کند.
  - *«rate یا scale؟»* توزیع Gamma در NumPy از scale = 1/rate استفاده می‌کند؛ رایج‌ترین باگ در نمونه‌گیرهای Gibbs دانشجوها.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: one Gibbs iteration by hand · بخش 1: یک تکرار Gibbs با دست

Data: $N = 4$ log RTs, $\mathbf{y} = (6.0, 6.3, 6.1, 6.4)$, so $\sum y_i = 24.8$. Priors: $m_0 = 6$, $s_0 = 1$, $a_0 = 2$, $b_0 = 0.1$. Current values: $\mu = 6.0$, $\tau = 10$.

<div dir="rtl">

داده: $N = 4$ لگاریتم زمان واکنش، $\mathbf{y} = (6.0, 6.3, 6.1, 6.4)$، پس $\sum y_i = 24.8$. پیشین‌ها: $m_0 = 6$، $s_0 = 1$، $a_0 = 2$، $b_0 = 0.1$. مقادیر فعلی: $\mu = 6.0$، $\tau = 10$.

</div>

**Update $\mu$.** Precision $= 1/1^2 + 4 \times 10 = 41$; mean $= (6/1 + 10 \times 24.8)/41 = (6 + 248)/41 = 6.195$; SD $= 1/\sqrt{41} = 0.156$. Draw, say, $\mu = 6.22$.

<div dir="rtl">

**به‌روزرسانی $\mu$.** دقت $= 1/1^2 + 4 \times 10 = 41$؛ میانگین $= (6/1 + 10 \times 24.8)/41 = (6 + 248)/41 = 6.195$؛ انحراف معیار $= 1/\sqrt{41} = 0.156$. مثلاً $\mu = 6.22$ کشیده می‌شود.

</div>

**Update $\tau$** given $\mu = 6.22$. Squared residuals: $0.0484 + 0.0064 + 0.0144 + 0.0324 = 0.1016$. Shape $= 2 + 4/2 = 4$; rate $= 0.1 + 0.1016/2 = 0.1508$. The conditional mean of $\tau$ is $4/0.1508 = 26.5$ (i.e., $\sigma \approx 0.19$). Draw, say, $\tau = 24.1$.

<div dir="rtl">

**به‌روزرسانی $\tau$** با $\mu = 6.22$. مربع باقی‌مانده‌ها: $0.0484 + 0.0064 + 0.0144 + 0.0324 = 0.1016$. شکل $= 2 + 4/2 = 4$؛ rate $= 0.1 + 0.1016/2 = 0.1508$. میانگین شرطی $\tau$ برابر $4/0.1508 = 26.5$ است (یعنی $\sigma \approx 0.19$). مثلاً $\tau = 24.1$ کشیده می‌شود.

</div>

New state: $(\mu, \tau) = (6.22, 24.1)$. No accept/reject step was needed.

<div dir="rtl">

حالت جدید: $(\mu, \tau) = (6.22, 24.1)$. هیچ گام پذیرش/ردی لازم نبود.

</div>

### Part 2: $\hat R$ by hand · بخش 2: $\hat R$ با دست

Two chains of $S = 4$ draws each.

<div dir="rtl">

دو زنجیره، هرکدام $S = 4$ نمونه.

</div>

**Not converged.** Chain 1: (1.0, 1.2, 0.8, 1.0); chain 2: (2.0, 2.2, 1.8, 2.0).
- Chain means: 1.0 and 2.0. Within-chain variances (ddof = 1): both $0.08/3 = 0.0267$, so $W = 0.0267$.
- $B = S \times \mathrm{var}(\text{means}) = 4 \times 0.5 = 2.0$.
- $\widehat{\mathrm{var}}^{+} = \tfrac34 \times 0.0267 + \tfrac14 \times 2.0 = 0.520$.
- $\hat R = \sqrt{0.520/0.0267} = 4.4$. The chains clearly disagree.

<div dir="rtl">

**همگرا نشده.** زنجیره‌ی 1: (1.0، 1.2، 0.8، 1.0)؛ زنجیره‌ی 2: (2.0، 2.2، 1.8، 2.0).
- میانگین زنجیره‌ها: 1.0 و 2.0. واریانس‌های درون‌زنجیره‌ای (ddof = 1): هر دو $0.08/3 = 0.0267$، پس $W = 0.0267$.
- $B = S \times \mathrm{var}(\text{means}) = 4 \times 0.5 = 2.0$.
- $\widehat{\mathrm{var}}^{+} = \tfrac34 \times 0.0267 + \tfrac14 \times 2.0 = 0.520$.
- $\hat R = \sqrt{0.520/0.0267} = 4.4$. زنجیره‌ها به‌وضوح با هم مخالف‌اند.

</div>

**Converged (realistic numbers).** $S = 1000$ draws per chain, $W = 0.05$, chain means 1.00 and 1.02: $B = 1000 \times \mathrm{var}(1.00, 1.02) = 1000 \times 0.0002 = 0.2$; $\widehat{\mathrm{var}}^{+} = 0.999 \times 0.05 + 0.2/1000 = 0.05015$; $\hat R = \sqrt{0.05015/0.05} = 1.0015$. Below 1.01: fine.

<div dir="rtl">

**همگرا شده (با اعداد واقع‌بینانه).** $S = 1000$ نمونه در هر زنجیره، $W = 0.05$، میانگین زنجیره‌ها 1.00 و 1.02: $B = 1000 \times \mathrm{var}(1.00, 1.02) = 1000 \times 0.0002 = 0.2$؛ $\widehat{\mathrm{var}}^{+} = 0.999 \times 0.05 + 0.2/1000 = 0.05015$؛ $\hat R = \sqrt{0.05015/0.05} = 1.0015$. کمتر از 1.01: خوب است.

</div>

### Part 3: ESS by hand · بخش 3: ESS با دست

$C \cdot S = 4000$ draws with autocorrelations $\rho_h = 0.5^h$. Then $\sum_{h\ge1}\rho_h = 1$, so $\mathrm{ESS} = 4000/(1 + 2) = 1333$. With a posterior SD of 0.2, MCSE $= 0.2/\sqrt{1333} = 0.0055$: report the posterior mean to two decimals.

<div dir="rtl">

$C \cdot S = 4000$ نمونه با خودهمبستگی‌های $\rho_h = 0.5^h$. آن‌وقت $\sum_{h\ge1}\rho_h = 1$، پس $\mathrm{ESS} = 4000/(1 + 2) = 1333$. با انحراف معیار پسین 0.2، MCSE $= 0.2/\sqrt{1333} = 0.0055$: میانگین پسین را با دو رقم اعشار گزارش کنید.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Implement a Gibbs sampler for the normal model of log RTs and validate it against a grid posterior.
2. Run four dispersed chains and inspect them.
3. Implement split-$\hat R$ and ESS; compare with ArviZ.
4. Break convergence on purpose (the power model with a bad Metropolis sampler) and watch the diagnostics catch it.

<div dir="rtl">

1. پیاده‌سازی یک نمونه‌گیر Gibbs برای مدل نرمال لگاریتم زمان واکنش و اعتبارسنجی آن با یک پسین شبکه‌ای.
2. اجرای چهار زنجیره‌ی پراکنده و وارسی آن‌ها.
3. پیاده‌سازی split-$\hat R$ و ESS؛ مقایسه با ArviZ.
4. خراب کردن عمدی همگرایی (مدل توانی با یک نمونه‌گیر Metropolis بد) و دیدن اینکه تشخیص‌ها آن را می‌گیرند.

</div>

**Timing:** Part A 30 min · Part B 15 min · Part C 30 min · Part D 30 min · Part E 15 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 30 دقیقه · بخش B 15 دقیقه · بخش C 30 دقیقه · بخش D 30 دقیقه · بخش E 15 دقیقه.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week12.py`](code/week12.py), cell 1 · سلول 1

### Part A: a Gibbs sampler (30 min) · بخش A: یک نمونه‌گیر Gibbs (30 دقیقه)

> **Code · کد:** [`code/week12.py`](code/week12.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
N = 40, sample mean = 6.200, sample SD = 0.225
Gibbs: mu = 6.1994 (SD 0.0358), sigma = 0.2283 (SD 0.0255)
Grid:  mu = 6.1996, sigma = 0.2287
```

### Part B: four dispersed chains (15 min) · بخش B: چهار زنجیره‌ی پراکنده (15 دقیقه)

> **Code · کد:** [`code/week12.py`](code/week12.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Chain means of mu: [6.2006 6.1988 6.1996 6.1992]
```

Gibbs forgets even absurd starting values within a few iterations here, because $\mu$ and $\tau$ are nearly uncorrelated in this posterior.

<div dir="rtl">

اینجا Gibbs حتی مقادیر شروع پوچ را در چند تکرار فراموش می‌کند، چون $\mu$ و $\tau$ در این پسین تقریباً ناهمبسته‌اند.

</div>

### Part C: $\hat R$ and ESS from scratch, checked against ArviZ (30 min) · بخش C: $\hat R$ و ESS از صفر، بررسی‌شده با ArviZ (30 دقیقه)

> **Code · کد:** [`code/week12.py`](code/week12.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
       R-hat (ours)  R-hat (ArviZ)  ESS (ours)  bulk-ESS (ArviZ)  MCSE of mean
param
mu           1.0002         1.0004   9980.4260        10032.6243        0.0004
sigma        0.9997         0.9998   8772.9605         8861.7940        0.0003
      ess_bulk ess_tail r_hat mcse_mean  mcse_sd
mu       10032     9427  1.00   0.00036  0.00027
sigma     8861     9714  1.00   0.00027  0.00021
```

(The exact column layout of `az.summary` differs slightly between ArviZ versions; the output above is from ArviZ 1.x.) Our simple estimators agree closely with ArviZ. With 4 × 2500 = 10 000 draws, ESS ≈ 9000–10 000 means the Gibbs draws are almost independent. ArviZ additionally **rank-normalizes** the draws (Vehtari et al., 2021), which makes its $\hat R$ and bulk-ESS robust to heavy tails, so small differences are expected. In practice use ArviZ; today's point is to know what it computes.

<div dir="rtl">

(چیدمان دقیق ستون‌های `az.summary` بین نسخه‌های ArviZ کمی فرق دارد؛ خروجی بالا از ArviZ 1.x است.) برآوردگرهای ساده‌ی ما با ArviZ خیلی نزدیک‌اند. با 4 × 2500 = 10 000 نمونه، ESS ≈ 9000 تا 10 000 یعنی نمونه‌های Gibbs تقریباً مستقل‌اند. ArviZ علاوه بر این نمونه‌ها را **نرمال‌سازی رتبه‌ای** می‌کند (Vehtari و همکاران، 2021)، که $\hat R$ و bulk-ESS آن را در برابر دنباله‌های سنگین مقاوم می‌کند، پس تفاوت‌های کوچک قابل انتظار است. در عمل از ArviZ استفاده کنید؛ نکته‌ی امروز این است که بدانید چه چیزی حساب می‌کند.

</div>

### Part D: catching non-convergence (30 min) · بخش D: گرفتن عدم همگرایی (30 دقیقه)

We reuse last week's Metropolis sampler on the power forgetting model, once badly tuned and short, once well tuned.

<div dir="rtl">

نمونه‌گیر Metropolis هفته‌ی قبل را روی مدل فراموشی توانی دوباره به کار می‌بریم؛ یک بار بد تنظیم‌شده و کوتاه، یک بار خوب تنظیم‌شده.

</div>

> **Code · کد:** [`code/week12.py`](code/week12.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
bad (tiny steps, short)   split-R-hat(d) = 3.583, ArviZ R-hat(d) = 3.424, ESS(d) = 4, chain means of d = [0.248 0.785 0.451 0.328]
good (tuned, longer)      split-R-hat(d) = 1.002, ArviZ R-hat(d) = 1.002, ESS(d) = 1025, chain means of d = [0.414 0.414 0.415 0.413]
```

**What to notice:** with tiny steps and short chains, each chain is still close to where it started. The traces are separate, $\hat R$ is far above 1.01 and the ESS is tiny. *Each chain on its own looks smooth and stable*, which is exactly why one chain is never enough. The tuned sampler gives overlapping traces, $\hat R = 1.002$ and an ESS of about 1000 from 20 000 draws. The Gibbs sampler of Part C, with almost uncorrelated draws, reached an ESS of about 9000–10 000 from 10 000 draws.

<div dir="rtl">

**به این دقت کنید:** با گام‌های ریز و زنجیره‌های کوتاه، هر زنجیره هنوز نزدیک جایی است که شروع کرده. traceها جدا از هم‌اند، $\hat R$ خیلی بالاتر از 1.01 است و ESS ناچیز است. *هر زنجیره به‌تنهایی صاف و پایدار به نظر می‌رسد*، و دقیقاً به همین دلیل یک زنجیره هرگز کافی نیست. نمونه‌گیر تنظیم‌شده traceهای روی هم افتاده، $\hat R = 1.002$ و ESS حدود 1000 از 20 000 نمونه می‌دهد. نمونه‌گیر Gibbs بخش C، با نمونه‌های تقریباً ناهمبسته، از 10 000 نمونه به ESS حدود 9000 تا 10 000 رسید.

</div>

### Part E: interpret and report (15 min) · بخش E: تفسیر و گزارش (15 دقیقه)

Write an MCMC methods-and-results paragraph for the log-RT model, following the checklist in Lecture §6: sampler, chains, iterations, burn-in, starting values, $\hat R$, ESS, posterior means and 95% intervals of $\mu$ and $\sigma$ (back-transform $\mu$ to milliseconds with $e^\mu$ and say what it represents).

<div dir="rtl">

یک پاراگراف روش‌ها و نتایج MCMC برای مدل لگاریتم زمان واکنش، طبق چک‌لیست بخش 6 جزوه، بنویسید: نمونه‌گیر، زنجیره‌ها، تکرارها، burn-in، مقادیر شروع، $\hat R$، ESS، میانگین‌های پسین و بازه‌های 95% $\mu$ و $\sigma$ (با $e^\mu$ مقدار $\mu$ را به میلی‌ثانیه برگردانید و بگویید نماینده‌ی چیست).

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Show by algebra that the full conditional of $\tau$ is a Gamma distribution: write $p(\tau\mid\mu,\mathbf{y}) \propto \tau^{N/2}\exp(-\tfrac{\tau}{2}\sum(y_i-\mu)^2)\cdot\tau^{a_0-1}e^{-b_0\tau}$ and read off the shape and rate.

<div dir="rtl">

**تمرین 1 ★.** به‌صورت جبری نشان دهید که full conditional $\tau$ یک توزیع Gamma است: $p(\tau\mid\mu,\mathbf{y}) \propto \tau^{N/2}\exp(-\tfrac{\tau}{2}\sum(y_i-\mu)^2)\cdot\tau^{a_0-1}e^{-b_0\tau}$ را بنویسید و شکل و rate را بخوانید.

</div>

**Exercise 2 ★.** Introduce the rate/scale bug (`scale=B0 + ...` instead of `1 / (...)`) into `gibbs_normal`. Do the diagnostics catch it? Does the validation against the grid? What does this tell you about the difference between *convergence* and *correctness*?

<div dir="rtl">

**تمرین 2 ★.** باگ rate/scale را (`scale=B0 + ...` به‌جای `1 / (...)`) وارد `gibbs_normal` کنید. آیا تشخیص‌ها آن را می‌گیرند؟ اعتبارسنجی با شبکه چطور؟ این درباره‌ی تفاوت *همگرایی* و *درستی* چه می‌گوید؟

</div>

**Exercise 3 ★★ (correlated Gibbs).** Write a Gibbs sampler for a bivariate normal "posterior" with correlation $\rho$ (full conditionals: $\theta_1\mid\theta_2 \sim \mathcal{N}(\rho\theta_2, \sqrt{1-\rho^2})$ and vice versa). Compare the ESS for $\rho = 0, 0.9, 0.99$ with 5000 iterations, and plot the zig-zag path for $\rho = 0.99$.

<div dir="rtl">

**تمرین 3 ★★ (Gibbs همبسته).** یک نمونه‌گیر Gibbs برای یک «پسین» نرمال دومتغیره با همبستگی $\rho$ بنویسید (full conditionalها: $\theta_1\mid\theta_2 \sim \mathcal{N}(\rho\theta_2, \sqrt{1-\rho^2})$ و برعکس). ESS را برای $\rho = 0, 0.9, 0.99$ با 5000 تکرار مقایسه کنید و مسیر زیگزاگ را برای $\rho = 0.99$ رسم کنید.

</div>

**Exercise 4 ★★ (Metropolis-within-Gibbs).** Sample the power forgetting model by updating $A$ and $d$ **one at a time**, each with a 1-D Metropolis step. Compare the ESS per second with the joint Metropolis sampler. Why might it be worse here? (Hint: the $A$–$d$ correlation.)

<div dir="rtl">

**تمرین 4 ★★ (Metropolis-within-Gibbs).** از مدل فراموشی توانی با به‌روزرسانی $A$ و $d$ **یکی‌یکی**، هرکدام با یک گام Metropolis یک‌بعدی، نمونه بگیرید. ESS در هر ثانیه را با نمونه‌گیر Metropolis مشترک مقایسه کنید. چرا ممکن است اینجا بدتر باشد؟ (راهنمایی: همبستگی $A$–$d$.)

</div>

**Exercise 5 ★★★ (Advanced: two conditions).** Extend the Gibbs sampler to log RTs from two conditions with separate means $\mu_1, \mu_2$ and a shared precision $\tau$. Simulate data with a true difference of 0.1, sample, and report the posterior of $\mu_2 - \mu_1$ and $P(\mu_2 > \mu_1\mid\mathbf{y})$ with diagnostics.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: دو شرط).** نمونه‌گیر Gibbs را برای لگاریتم زمان واکنش در دو شرط با میانگین‌های جداگانه‌ی $\mu_1, \mu_2$ و دقت مشترک $\tau$ گسترش دهید. داده‌ای با تفاوت واقعی 0.1 شبیه‌سازی کنید، نمونه بگیرید، و پسین $\mu_2 - \mu_1$ و $P(\mu_2 > \mu_1\mid\mathbf{y})$ را با تشخیص‌ها گزارش کنید.

</div>

### Lab check-off · lab check-off

Show: (1) the Gibbs-vs-grid validation (Part A), (2) your $\hat R$/ESS table next to ArviZ's (Part C), and (3) the bad-vs-good trace plots with their diagnostics (Part D).

<div dir="rtl">

نشان دهید: (1) اعتبارسنجی Gibbs در برابر شبکه (بخش A)، (2) جدول $\hat R$/ESS خودتان کنار جدول ArviZ (بخش C)، و (3) trace plotهای بد در برابر خوب با تشخیص‌هایشان (بخش D).

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Gibbs sampling from a masked language model.** Models like BERT are trained to fill in a masked word given all other words: they learn **full conditionals**, $P(w_i \mid \text{all other words})$. That is exactly what a Gibbs sampler needs. Repeatedly masking one position and resampling it generates whole sentences (Wang & Cho, 2019). The toy model below knows only the two full conditionals of a two-word "language", and Gibbs sampling recovers the joint distribution of sentences. Because the language is "sticky" (dog goes with barks, cat with meows), the chain mixes slowly, and $\hat R$ catches this in short runs.

<div dir="rtl">

**نمونه‌گیری Gibbs از یک مدل زبانی masked.** مدل‌هایی مثل BERT آموزش می‌بینند که یک کلمه‌ی پوشانده‌شده (masked) را با توجه به همه‌ی کلمه‌های دیگر پر کنند: آن‌ها **full conditionalها** $P(w_i \mid \text{all other words})$ را یاد می‌گیرند. این دقیقاً چیزی است که یک نمونه‌گیر Gibbs لازم دارد. پوشاندن مکرر یک موقعیت و نمونه‌گیری دوباره‌ی آن، جمله‌های کامل تولید می‌کند (Wang & Cho, 2019). مدل اسباب‌بازی پایین فقط دو full conditional یک «زبان» دوکلمه‌ای را می‌داند، و نمونه‌گیری Gibbs توزیع توأم جمله‌ها را بازیابی می‌کند. چون این زبان «چسبناک» است (dog با barks می‌آید، cat با meows)، زنجیره کند مخلوط می‌شود، و $\hat R$ این را در اجراهای کوتاه تشخیص می‌دهد.

</div>

> **Code · کد:** [`code/week12.py`](code/week12.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
  50 iterations: P(subject = dog) = 0.285 (exact 0.35), R-hat = 1.151
3000 iterations: P(subject = dog) = 0.354 (exact 0.35), R-hat = 1.000
```

**Try it (no API needed).**
- ★ Make the language even stickier (e.g., 0.33 on the diagonal and 0.001 elsewhere, renormalized). How many iterations do you now need for $\hat R < 1.01$? Compute the ESS (Week 12, Part C) of the `is_dog` chains.
- ★★ Real masked models are trained separately for each position, so their conditionals need not come from any single joint distribution. Perturb `p_v_given_s` slightly (without changing `p_s_given_v`) and check whether the Gibbs sampler still recovers `joint`. What does this tell you about trusting a sampler whose conditionals are learned?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ زبان را باز هم چسبناک‌تر کنید (مثلاً 0.33 روی قطر و 0.001 در بقیه، دوباره نرمال‌شده). حالا برای $\hat R < 1.01$ به چند تکرار نیاز دارید؟ ESS زنجیره‌های `is_dog` را حساب کنید (هفته‌ی 12، بخش C).
- ★★ مدل‌های masked واقعی برای هر موقعیت جداگانه آموزش می‌بینند، پس لازم نیست توزیع‌های شرطی‌شان از یک توزیع توأم واحد آمده باشند. `p_v_given_s` را کمی دست‌کاری کنید (بدون تغییر `p_s_given_v`) و بررسی کنید آیا نمونه‌گیر Gibbs هنوز `joint` را بازیابی می‌کند. این درباره‌ی اعتماد به نمونه‌گیری که توزیع‌های شرطی‌اش یادگرفته‌شده‌اند چه می‌گوید؟

</div>

*Optional reading:* Wang, A., & Cho, K. (2019). BERT has a mouth, and it must speak: BERT as a Markov random field language model. *arXiv:1902.04094*.

<div dir="rtl">

*مطالعه‌ی اختیاری:* Wang, A., & Cho, K. (2019). BERT has a mouth, and it must speak: BERT as a Markov random field language model. *arXiv:1902.04094*.

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **Rate vs. scale in the Gamma distribution.** NumPy and SciPy use scale = 1/rate. Write down which one your formula uses.
2. **Using old values within a Gibbs sweep.** Each conditional must use the *newest* values of the other parameters.
3. **"$\hat R \approx 1$, so the results are correct."** Diagnostics test agreement between chains, not correctness of the model or the code (Exercise 2). Validate new samplers on known cases.
4. **One long chain instead of several.** A stuck chain can look perfectly stable. Use $\ge 4$ dispersed chains.
5. **Reporting results with low ESS.** With ESS = 50, a posterior mean has an MCSE of about 14% of the posterior SD, and tail quantiles are unreliable.
6. **Thinning to "fix" autocorrelation.** Thinning lowers storage but does not increase the information. ESS already accounts for autocorrelation.
7. **Using the 1.1 threshold uncritically.** Modern guidance is $\hat R < 1.01$ with rank-normalized split-$\hat R$.
8. **Diagnosing only some parameters.** Check *all* reported parameters, including derived ones.

<div dir="rtl">

1. **rate در برابر scale در توزیع Gamma.** NumPy و SciPy از scale = 1/rate استفاده می‌کنند. بنویسید فرمولتان از کدام استفاده می‌کند.
2. **استفاده از مقادیر قدیمی داخل یک دور Gibbs.** هر توزیع شرطی باید از *جدیدترین* مقادیر پارامترهای دیگر استفاده کند.
3. **«$\hat R \approx 1$، پس نتایج درست‌اند.»** تشخیص‌ها توافق بین زنجیره‌ها را آزمون می‌کنند، نه درستی مدل یا کد را (تمرین 2). نمونه‌گیرهای جدید را روی حالت‌های معلوم اعتبارسنجی کنید.
4. **یک زنجیره‌ی بلند به‌جای چند زنجیره.** زنجیره‌ی گیرکرده می‌تواند کاملاً پایدار به نظر برسد. از ≥ 4 زنجیره‌ی پراکنده استفاده کنید.
5. **گزارش نتایج با ESS پایین.** با ESS = 50، MCSE میانگین پسین حدود 14% انحراف معیار پسین است و quantileهای دنباله غیرقابل اعتمادند.
6. **thinning برای «درست کردن» خودهمبستگی.** thinning حافظه را کم می‌کند ولی اطلاعات را زیاد نمی‌کند. ESS خودش خودهمبستگی را در نظر می‌گیرد.
7. **استفاده‌ی بی‌چون‌وچرا از آستانه‌ی 1.1.** راهنمایی امروزی $\hat R < 1.01$ با split-$\hat R$ نرمال‌شده‌ی رتبه‌ای است.
8. **تشخیص فقط برای بعضی پارامترها.** *همه‌ی* پارامترهای گزارش‌شده، از جمله مشتق‌شده‌ها، را بررسی کنید.

</div>

---

## Check your understanding · خودآزمایی

**1.** Why does Gibbs sampling never reject a draw?
<details><summary>Answer</summary>
Each draw comes exactly from the full conditional distribution. Viewed as Metropolis–Hastings with the full conditional as proposal, the acceptance ratio is always 1.
</details>

<div dir="rtl">

**1.** چرا نمونه‌گیری Gibbs هیچ‌وقت یک نمونه را رد نمی‌کند؟
<details><summary>پاسخ</summary>
هر نمونه دقیقاً از full conditional می‌آید. اگر آن را Metropolis–Hastings با full conditional به‌عنوان پیشنهاد ببینیم، نسبت پذیرش همیشه 1 است.
</details>

</div>

**2.** What do you need to be able to run a pure Gibbs sampler?
<details><summary>Answer</summary>
Full conditional distributions for every parameter (or block) that you can sample from directly, typically because the priors are conditionally conjugate.
</details>

<div dir="rtl">

**2.** برای اجرای یک نمونه‌گیر Gibbs خالص به چه چیزی نیاز دارید؟
<details><summary>پاسخ</summary>
full conditionalها برای هر پارامتر (یا بلوک) که بتوانید مستقیماً از آن‌ها نمونه بگیرید؛ معمولاً چون پیشین‌ها به‌طور شرطی conjugate هستند.
</details>

</div>

**3.** A Gibbs sampler for two strongly correlated parameters has a very low ESS. Why, and what could you do?
<details><summary>Answer</summary>
Gibbs updates one coordinate at a time, so on a narrow diagonal ridge every step is tiny and the chain zig-zags slowly. Remedies: reparameterize to reduce the correlation, update the correlated parameters jointly (blocking), or use HMC/NUTS.
</details>

<div dir="rtl">

**3.** یک نمونه‌گیر Gibbs برای دو پارامتر به‌شدت همبسته ESS خیلی پایینی دارد. چرا، و چه می‌توانید بکنید؟
<details><summary>پاسخ</summary>
Gibbs هر بار یک مختصه را به‌روز می‌کند، پس روی یک ridge باریک مورب هر گام ریز است و زنجیره آرام زیگزاگ می‌زند. راه‌حل‌ها: reparameterization برای کم کردن همبستگی، به‌روزرسانی هم‌زمان پارامترهای همبسته (بلوک‌بندی)، یا استفاده از HMC/NUTS.
</details>

</div>

**4.** Explain $\hat R$ in one sentence. Which value indicates convergence?
<details><summary>Answer</summary>
It compares the variance between chains with the variance within chains (it estimates how much the posterior spread could shrink if the chains ran forever); values near 1 (< 1.01 by current guidance) indicate that the chains agree.
</details>

<div dir="rtl">

**4.** $\hat R$ را در یک جمله توضیح دهید. کدام مقدار نشانه‌ی همگرایی است؟
<details><summary>پاسخ</summary>
واریانس بین زنجیره‌ها را با واریانس درون زنجیره‌ها مقایسه می‌کند (تخمین می‌زند اگر زنجیره‌ها تا ابد اجرا می‌شدند پراکندگی پسین چقدر می‌توانست کم شود)؛ مقادیر نزدیک 1 (طبق راهنمایی امروزی < 1.01) یعنی زنجیره‌ها توافق دارند.
</details>

</div>

**5.** You have 4000 draws and an ESS of 200 for a parameter with posterior SD 0.5. What is the MCSE of its posterior mean? How many decimals should you report?
<details><summary>Answer</summary>
MCSE $= 0.5/\sqrt{200} = 0.035$. Report the mean to one decimal (or two at most), because the third decimal is Monte Carlo noise.
</details>

<div dir="rtl">

**5.** 4000 نمونه و ESS برابر 200 برای پارامتری با انحراف معیار پسین 0.5 دارید. MCSE میانگین پسینش چقدر است؟ چند رقم اعشار باید گزارش کنید؟
<details><summary>پاسخ</summary>
MCSE $= 0.5/\sqrt{200} = 0.035$. میانگین را با یک رقم اعشار (یا حداکثر دو) گزارش کنید، چون رقم سوم نویز Monte Carlo است.
</details>

</div>

**6.** Why can't one chain demonstrate convergence?
<details><summary>Answer</summary>
A chain stuck in one region (one mode, or one part of a ridge) can look stationary and well mixed, and nothing in the chain itself reveals the unexplored regions. Only chains started elsewhere, which end up somewhere different, expose the problem.
</details>

<div dir="rtl">

**6.** چرا یک زنجیره نمی‌تواند همگرایی را نشان دهد؟
<details><summary>پاسخ</summary>
زنجیره‌ای که در یک ناحیه گیر کرده (یک مُد، یا بخشی از یک ridge) می‌تواند ایستا و خوب مخلوط‌شده به نظر برسد، و هیچ چیزی در خود زنجیره نواحی کاوش‌نشده را آشکار نمی‌کند. فقط زنجیره‌هایی که از جای دیگری شروع شده و به جای دیگری رسیده‌اند مشکل را لو می‌دهند.
</details>

</div>

**7.** Name four things a methods section should report about an MCMC analysis.
<details><summary>Answer</summary>
Any four of: sampler/software; number of chains; iterations and warm-up; starting values; $\hat R$ and ESS for all parameters; that trace plots were inspected; priors; a posterior predictive check.
</details>

<div dir="rtl">

**7.** چهار چیزی را که بخش روش‌ها باید درباره‌ی یک تحلیل MCMC گزارش کند نام ببرید.
<details><summary>پاسخ</summary>
هر چهار مورد از این‌ها: نمونه‌گیر/نرم‌افزار؛ تعداد زنجیره‌ها؛ تکرارها و warm-up؛ مقادیر شروع؛ $\hat R$ و ESS برای همه‌ی پارامترها؛ اینکه trace plotها بررسی شده‌اند؛ پیشین‌ها؛ یک بررسی پیش‌بینی پسین.
</details>

</div>

---

## Assignment · تکلیف

### A5: MCMC from scratch, with diagnostics (1.0 point of 20; released Week 12, due at the start of the Week 14 lecture) · A5: MCMC از صفر، همراه با تشخیص همگرایی (1.0 نمره از 20؛ انتشار هفته‌ی 12، موعد ابتدای درس هفته‌ی 14)

**Data:** the payoff SDT experiment from Week 4, Part D (regenerate it with the same seed: `np.random.default_rng(11)`), and the log-RT data from today's lab (`np.random.default_rng(12)`).

<div dir="rtl">

**داده:** آزمایش SDT پاداش از بخش D هفته‌ی 4 (با همان seed بازتولیدش کنید: `np.random.default_rng(11)`) و داده‌ی لگاریتم زمان واکنش lab امروز (`np.random.default_rng(12)`).

</div>

**Tasks.**

<div dir="rtl">

**کارها.**

</div>

1. **Metropolis for SDT (3 pts).** Implement a random-walk Metropolis sampler for the shared-$d'$ payoff model ($d'$, $c_1, c_2, c_3$) with priors $d' \sim \mathcal{N}(1, 1.5)$ and $c_m \sim \mathcal{N}(0, 1)$. Tune the proposal (report the acceptance rate), and run 4 dispersed chains.
2. **Diagnostics (2 pts).** Report split-$\hat R$ and ESS for all parameters with your own functions *and* with ArviZ; show trace plots. State whether you would trust the results and why.
3. **Inference (1.5 pts).** Report posterior means and 95% intervals; compute the posterior of $c_{\text{conservative}} - c_{\text{liberal}}$ and the probability that it is positive. Compare $d'$ with the Week 4 MLE.
4. **Gibbs (2 pts).** Implement the two-condition Gibbs sampler of Exercise 5 and report the posterior of the mean difference with diagnostics.
5. **Interpretation (1.5 pts, max. 300 words).** What do the payoffs do to sensitivity and bias, according to the posterior? Compare with the likelihood-ratio conclusion of Week 4.

<div dir="rtl">

1. **Metropolis برای SDT (3 امتیاز).** یک نمونه‌گیر Metropolis گام تصادفی برای مدل پاداش با $d'$ مشترک ($d'$، $c_1, c_2, c_3$) با پیشین‌های $d' \sim \mathcal{N}(1, 1.5)$ و $c_m \sim \mathcal{N}(0, 1)$ پیاده‌سازی کنید. پیشنهاد را تنظیم کنید (نرخ پذیرش را گزارش کنید) و 4 زنجیره‌ی پراکنده اجرا کنید.
2. **تشخیص همگرایی (2 امتیاز).** split-$\hat R$ و ESS را برای همه‌ی پارامترها با توابع خودتان *و* با ArviZ گزارش کنید؛ trace plotها را نشان دهید. بگویید آیا به نتایج اعتماد می‌کنید و چرا.
3. **استنباط (1.5 امتیاز).** میانگین‌های پسین و بازه‌های 95% را گزارش کنید؛ پسین $c_{\text{conservative}} - c_{\text{liberal}}$ و احتمال مثبت بودنش را حساب کنید. $d'$ را با MLE هفته‌ی 4 مقایسه کنید.
4. **Gibbs (2 امتیاز).** نمونه‌گیر Gibbs دوشرطی تمرین 5 را پیاده‌سازی کنید و پسین تفاوت میانگین‌ها را با تشخیص‌ها گزارش کنید.
5. **تفسیر (1.5 امتیاز، حداکثر 300 کلمه).** طبق پسین، پاداش‌ها با حساسیت و سوگیری چه می‌کنند؟ با نتیجه‌ی آزمون نسبت درست‌نمایی هفته‌ی 4 مقایسه کنید.

</div>

**Rubric:** points as above; within each task: correctness 60%, figures/tables 20%, interpretation 20%. Late submissions lose 10% per day (max. 3 days).

<div dir="rtl">

**روبریک:** امتیازها مطابق بالا؛ داخل هر کار: درستی 60%، نمودارها/جدول‌ها 20%، تفسیر 20%. برای تحویل با تأخیر، روزی 10% کسر می‌شود (حداکثر 3 روز).

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Kruschke (2014), chapter 7** (sections on Gibbs sampling and on MCMC representativeness, accuracy and efficiency): diagnostics, ESS and MCSE explained visually. *(Main reading.)*
- **Martin, Kumar & Lao (2021), chapter 2.** Exploratory analysis of Bayesian models: trace plots, $\hat R$, ESS and MCSE with ArviZ.
- **Lee & Wagenmakers (2014), chapter 4.** Inferences with Gaussians: the normal model whose Gibbs sampler you built today, in its Bayesian-modeling context.
- *Optional, outside the course list:* Vehtari, A., Gelman, A., Simpson, D., Carpenter, B., & Bürkner, P.-C. (2021). Rank-normalization, folding, and localization: An improved $\hat R$ for assessing convergence of MCMC. *Bayesian Analysis, 16*(2), 667–718.

<div dir="rtl">

- **Kruschke (2014)، فصل 7** (بخش‌های نمونه‌گیری Gibbs و نماینده بودن، دقت و کارایی MCMC): تشخیص همگرایی، ESS و MCSE به زبان تصویری. *(منبع اصلی.)*
- **Martin, Kumar & Lao (2021)، فصل 2.** تحلیل اکتشافی مدل‌های بیزی: trace plotها، $\hat R$، ESS و MCSE با ArviZ.
- **Lee & Wagenmakers (2014)، فصل 4.** استنباط با توزیع‌های گاوسی: همان مدل نرمالی که امروز نمونه‌گیر Gibbs آن را ساختید، در بافت مدل‌سازی بیزی.
- *اختیاری، خارج از فهرست درس:* Vehtari, A., Gelman, A., Simpson, D., Carpenter, B., & Bürkner, P.-C. (2021). Rank-normalization, folding, and localization: An improved $\hat R$ for assessing convergence of MCMC. *Bayesian Analysis, 16*(2), 667–718.

</div>

*Preview for Week 13:* writing samplers by hand teaches how they work, but it is slow and error-prone. Next week we describe models in PyMC, let its NUTS sampler do the work, and use the time we save for the most useful model class in cognitive science: hierarchical models of many participants.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 13:* نوشتن نمونه‌گیرها با دست یاد می‌دهد چطور کار می‌کنند، ولی کند و پراشتباه است. هفته‌ی بعد مدل‌ها را در PyMC توصیف می‌کنیم، می‌گذاریم نمونه‌گیر NUTS آن کار را بکند، و از وقتی که صرفه‌جویی می‌کنیم برای مفیدترین دسته‌ی مدل‌ها در علوم شناختی استفاده می‌کنیم: مدل‌های سلسله‌مراتبی چند شرکت‌کننده.

</div>
