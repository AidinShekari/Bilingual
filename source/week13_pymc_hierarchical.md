# Week 13: Probabilistic Programming and Hierarchical Models · هفته‌ی 13: برنامه‌نویسی احتمالاتی و مدل‌های سلسله‌مراتبی

> **Chapter 5: Parameter estimation with data-driven methods (MCMC)**, bridging to Chapter 6 · Lecture 1 h · Lab 2 h
> **Running data:** a recognition/detection experiment with 12 participants and only 50 + 50 trials each: hierarchical SDT in PyMC.

<div dir="rtl">

> **فصل 5: برآورد پارامتر با روش‌های داده‌محور (MCMC)**، پلی به فصل 6 · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** یک آزمایش بازشناسی/تشخیص با 12 شرکت‌کننده و فقط 50 + 50 trial برای هر نفر: SDT سلسله‌مراتبی در PyMC.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| hierarchical model | مدل سلسله‌مراتبی (چندسطحی) | پارامترهای فردی از یک توزیع گروهی می‌آیند |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| probabilistic programming | برنامه‌نویسی احتمالاتی | تعریف مدل با کد و نمونه‌گیری خودکار (PyMC) |
| prior | توزیع پیشین (prior) | باور درباره‌ی پارامتر پیش از دیدن داده |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| prior predictive check | بررسی پیش‌بینی پیشین | شبیه‌سازی داده از پیشین برای سنجش معقول بودن آن |
| posterior | توزیع پسین (posterior) | باور درباره‌ی پارامتر بعد از دیدن داده |
| posterior predictive check (PPC) | بررسی پیش‌بینی پسین | مقایسه‌ی داده‌ی شبیه‌سازی‌شده از پسین با داده‌ی واقعی |
| HMC / NUTS | Hamiltonian Monte Carlo / NUTS | MCMC مبتنی بر گرادیان |
| divergent transition | divergence (گذار واگرا) | هشدار NUTS برای ناحیه‌ای که درست کاوش نشده |
| complete / no / partial pooling | ادغام کامل / بدون ادغام / ادغام جزئی (pooling) | یک پارامتر برای همه / جدا برای هر فرد / سلسله‌مراتبی |
| shrinkage | انقباض به سمت میانگین (shrinkage) | کشیده شدن برآوردهای پرنویز به سمت میانگین گروه |
| centered / non-centered parameterization | پارامتری‌سازی centered / non-centered | دو شکل نوشتن مدل سلسله‌مراتبی |
| group-level parameter | پارامتر سطح گروه | میانگین و پراکندگی پارامترها در جمعیت |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| hit | اصابت (hit) | پاسخ «بله» وقتی علامت وجود دارد |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| gradient | گرادیان | جهت و شیب تغییر تابع |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| reparameterization | بازپارامتری‌سازی | نوشتن پارامتر در مقیاس دیگر، مثلاً λ = e^η |
| standard error (SE) | خطای استاندارد | پراکندگی برآورد در تکرارهای فرضی آزمایش |
| benchmark | benchmark (مجموعه‌آزمون استاندارد) | مجموعه سؤال برای مقایسه‌ی مدل‌های هوش مصنوعی |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Specify** a cognitive model in PyMC (priors, deterministic transformations, likelihood) and **run** a complete Bayesian workflow: prior predictive check, sampling, diagnostics, posterior predictive check.
2. **Explain** conceptually how Hamiltonian Monte Carlo / NUTS differs from random-walk Metropolis, and what a divergence signals.
3. **Formulate** a hierarchical (multilevel) model and **explain** partial pooling and shrinkage, contrasting it with the complete- and no-pooling approaches of Week 5.
4. **Implement** a non-centered parameterization and **justify** its use.
5. **Interpret** group-level and individual-level posteriors and **report** them according to the Week 12 checklist.

<div dir="rtl">

1. یک مدل شناختی را در PyMC **تعریف کنند** (پیشین‌ها، تبدیل‌های قطعی، درست‌نمایی) و یک گردش کار بیزی کامل را **اجرا کنند**: بررسی پیش‌بینی پیشین، نمونه‌گیری، تشخیص همگرایی، بررسی پیش‌بینی پسین.
2. به‌طور مفهومی **توضیح دهند** که Hamiltonian Monte Carlo / NUTS چه فرقی با Metropolis گام تصادفی دارد و یک divergence نشانه‌ی چیست.
3. یک مدل سلسله‌مراتبی (چندسطحی) را **صورت‌بندی کنند** و partial pooling و shrinkage را **توضیح دهند**، در مقایسه با رویکردهای complete pooling و no pooling هفته‌ی 5.
4. یک پارامترسازی non-centered را **پیاده‌سازی کنند** و استفاده‌اش را **توجیه کنند**.
5. پسین‌های سطح گروه و سطح فرد را **تفسیر کنند** و طبق چک‌لیست هفته‌ی 12 **گزارش کنند**.

</div>

---

## Motivation & big picture · مقدمه

In Week 5 we faced a dilemma. Fitting the **average** of all participants is stable but can distort the model (aggregation artifacts) and ignores individual differences. Fitting **each participant separately** respects differences, but with few trials per person the estimates are noisy. Some become extreme or infinite (a participant with 50/50 hits has $d' = \infty$ without a correction). The second-stage statistics on those estimates also ignore that some are much less certain than others.

<div dir="rtl">

در هفته‌ی 5 با یک دوراهی روبه‌رو شدیم. برازش **میانگین** همه‌ی شرکت‌کننده‌ها پایدار است ولی می‌تواند مدل را تحریف کند (خطای میانگین‌گیری) و تفاوت‌های فردی را نادیده می‌گیرد. برازش **هر شرکت‌کننده جداگانه** تفاوت‌ها را رعایت می‌کند، ولی با trialهای کم برای هر نفر برآوردها پرنویزند. بعضی‌شان حدی یا بی‌نهایت می‌شوند (شرکت‌کننده‌ای با 50/50 hit بدون تصحیح $d' = \infty$ دارد). آماره‌های مرحله‌ی دوم روی این برآوردها هم نادیده می‌گیرند که بعضی از بقیه خیلی نامطمئن‌ترند.

</div>

**Hierarchical models** dissolve the dilemma. They assume that each participant has their own parameter, *and* that these individual parameters come from a group-level distribution whose mean and spread are also estimated. Each individual estimate then borrows strength from the others: noisy, extreme estimates are pulled ("shrunk") toward the group mean, by exactly as much as their uncertainty warrants. The group-level parameters answer the population question ("what is the typical sensitivity, and how much do people differ?") with all sources of uncertainty included.

<div dir="rtl">

**مدل‌های سلسله‌مراتبی** این دوراهی را حل می‌کنند. فرض می‌کنند هر شرکت‌کننده پارامتر خودش را دارد، *و* این پارامترهای فردی از یک توزیع سطح گروه می‌آیند که میانگین و پراکندگی‌اش هم برآورد می‌شود. آن‌وقت هر برآورد فردی از بقیه نیرو قرض می‌گیرد: برآوردهای پرنویز و حدی دقیقاً به اندازه‌ای که عدم قطعیتشان ایجاب می‌کند به سمت میانگین گروه کشیده («shrink») می‌شوند. پارامترهای سطح گروه به سؤال جمعیت («حساسیت معمول چقدر است و آدم‌ها چقدر با هم فرق دارند؟») با در نظر گرفتن همه‌ی منابع عدم قطعیت جواب می‌دهند.

</div>

Writing samplers for such models by hand would be a research project. **Probabilistic programming languages** like PyMC let us *describe* the model in a few lines and use a state-of-the-art sampler, NUTS, automatically. The hand-built samplers of Weeks 11–12 are what make this black box transparent to you.

<div dir="rtl">

نوشتن نمونه‌گیر برای چنین مدل‌هایی با دست خودش یک پروژه‌ی پژوهشی است. **زبان‌های برنامه‌نویسی احتمالاتی** مثل PyMC به ما اجازه می‌دهند مدل را در چند خط *توصیف* کنیم و خودکار از یک نمونه‌گیر پیشرفته، NUTS، استفاده کنیم. نمونه‌گیرهای دست‌سازِ هفته‌های 11–12 همان چیزی‌اند که این جعبه‌ی سیاه را برایتان شفاف می‌کنند.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Most modern cognitive modeling studies with many participants** fit hierarchical models: hierarchical drift-diffusion models (the HDDM package), hierarchical reinforcement-learning models in computational psychiatry, hierarchical SDT in memory research.
- **Clinical and developmental studies with short sessions**: children and patients cannot do hundreds of trials, so individual estimates are noisy; partial pooling makes them usable.
- **Education and social science**: students within classes within schools (multilevel models) are the textbook example of hierarchical structure.
- **Sports analytics and medicine**: estimating a player's skill or a hospital's success rate from few observations by borrowing strength from the group is the same idea.

<div dir="rtl">

- **بیشتر مطالعه‌های امروزی مدل‌سازی شناختی با شرکت‌کننده‌های زیاد** مدل‌های سلسله‌مراتبی برازش می‌کنند: مدل‌های drift-diffusion سلسله‌مراتبی (بسته‌ی HDDM)، مدل‌های یادگیری تقویتی سلسله‌مراتبی در روان‌پزشکی محاسباتی، و SDT سلسله‌مراتبی در پژوهش حافظه.
- **مطالعه‌های بالینی و رشدی با جلسه‌های کوتاه:** کودکان و بیماران نمی‌توانند صدها trial انجام دهند، پس برآوردهای فردی پرنویزند؛ partial pooling آن‌ها را قابل استفاده می‌کند.
- **آموزش و علوم اجتماعی:** دانش‌آموزان درون کلاس‌ها درون مدرسه‌ها (مدل‌های چندسطحی) مثال کتاب‌درسی ساختار سلسله‌مراتبی است.
- **تحلیل ورزشی و پزشکی:** برآورد مهارت یک بازیکن یا نرخ موفقیت یک بیمارستان از چند مشاهده‌ی کم با کمک گرفتن از گروه، همین ایده است.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

When each person gives us only a little data, their individual estimates are noisy, and some come out absurd (a perfect score gives $d' = \infty$). A **hierarchical model** says: each person has their own parameter, *but* people are similar to each other, so their parameters come from a common group distribution, whose mean and spread we also estimate. The effect is sensible compromise: a person with little or extreme data is pulled toward the group average (**shrinkage**), and a person with plenty of data keeps an estimate close to their own. How strong the pull is depends on how different people turn out to be, which is learned from the data. Writing a sampler for such a model by hand is hard, so we use **PyMC**: we write the model almost like the math, and PyMC runs an advanced sampler (**NUTS**) for us. The last part of the week is a step-by-step **workflow** for doing this safely.

<div dir="rtl">

وقتی هر نفر فقط کمی داده به ما می‌دهد، برآوردهای فردی پرنویزند و بعضی‌شان بی‌معنی از آب درمی‌آیند (نمره‌ی کامل یعنی $d' = \infty$). یک **مدل سلسله‌مراتبی** می‌گوید: هر نفر پارامتر خودش را دارد، *ولی* آدم‌ها به هم شبیه‌اند، پس پارامترهایشان از یک توزیع گروهی مشترک می‌آیند که میانگین و پراکندگی آن را هم برآورد می‌کنیم. نتیجه یک مصالحه‌ی معقول است: کسی که داده‌ی کم یا حدی دارد به سمت میانگین گروه کشیده می‌شود (**shrinkage**)، و کسی که داده‌ی زیادی دارد برآوردی نزدیک به برآورد خودش نگه می‌دارد. شدت این کشش به این بستگی دارد که آدم‌ها چقدر با هم فرق دارند، و این از روی داده یاد گرفته می‌شود. نوشتن نمونه‌گیر برای چنین مدلی با دست سخت است، پس از **PyMC** استفاده می‌کنیم: مدل را تقریباً مثل ریاضی آن می‌نویسیم و PyMC یک نمونه‌گیر پیشرفته (**NUTS**) را برایمان اجرا می‌کند. بخش آخر هفته یک **گردش کار (workflow)** قدم‌به‌قدم برای انجام امن این کار است.

</div>

**Suggested timing (60 min):** probabilistic programming 10 · HMC/NUTS concepts 10 · hierarchical models 20 · parameterization and divergences 10 · the Bayesian workflow 10.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** برنامه‌نویسی احتمالاتی 10 · مفاهیم HMC/NUTS 10 · مدل‌های سلسله‌مراتبی 20 · پارامترسازی و divergenceها 10 · گردش کار بیزی 10.

</div>

### 1. Probabilistic programming with PyMC · 1. برنامه‌نویسی احتمالاتی با PyMC

A PyMC model is a direct transcription of the mathematical model:

<div dir="rtl">

یک مدل PyMC رونویسی مستقیم مدل ریاضی است:

</div>

| Math | PyMC |
|---|---|
| $\mu_{d} \sim \mathcal{N}(1, 1)$ | `mu_d = pm.Normal("mu_d", 1, 1)` |
| $\sigma_d \sim \mathcal{N}^{+}(0, 1)$ | `sigma_d = pm.HalfNormal("sigma_d", 1)` |
| $d'_j = \mu_d + \sigma_d z_j$ | `d = pm.Deterministic("d", mu_d + sigma_d * z_d)` |
| $H_j = \Phi(d'_j/2 - c_j)$ | `H = Phi(d / 2 - c)` (an expression, built with `pm.math`) |
| $\text{hits}_j \sim \mathrm{Binomial}(n_s, H_j)$ | `pm.Binomial("hits", n=n_s, p=H, observed=hits)` |

<div dir="rtl">

| ریاضی | PyMC |
|---|---|
| $\mu_{d} \sim \mathcal{N}(1, 1)$ | `mu_d = pm.Normal("mu_d", 1, 1)` |
| $\sigma_d \sim \mathcal{N}^{+}(0, 1)$ | `sigma_d = pm.HalfNormal("sigma_d", 1)` |
| $d'_j = \mu_d + \sigma_d z_j$ | `d = pm.Deterministic("d", mu_d + sigma_d * z_d)` |
| $H_j = \Phi(d'_j/2 - c_j)$ | `H = Phi(d / 2 - c)` (یک عبارت که با `pm.math` ساخته می‌شود) |
| $\text{hits}_j \sim \mathrm{Binomial}(n_s, H_j)$ | `pm.Binomial("hits", n=n_s, p=H, observed=hits)` |

</div>

Then `pm.sample()` compiles the model, computes gradients automatically, and runs NUTS. The result is an ArviZ `InferenceData`/`DataTree` object with groups such as `posterior`, `sample_stats`, `prior_predictive` and `posterior_predictive`, which ArviZ summarizes and diagnoses (Week 12).

<div dir="rtl">

بعد `pm.sample()` مدل را کامپایل می‌کند، گرادیان‌ها را خودکار حساب می‌کند و NUTS را اجرا می‌کند. نتیجه یک شیء `InferenceData`/`DataTree` در ArviZ است با گروه‌هایی مثل `posterior`، `sample_stats`، `prior_predictive` و `posterior_predictive` که ArviZ آن‌ها را خلاصه و تشخیص می‌کند (هفته‌ی 12).

</div>

**Practical notes:** use `cores=1` when running a plain `.py` script on Windows (or protect the code with `if __name__ == "__main__":`); give every variable a unique name; use `dims`/`coords` to label participants.

<div dir="rtl">

**نکته‌های عملی:** وقتی یک اسکریپت ساده‌ی `.py` را در Windows اجرا می‌کنید از `cores=1` استفاده کنید (یا کد را داخل `if __name__ == "__main__":` بگذارید)؛ به هر متغیر یک نام یکتا بدهید؛ برای برچسب زدن شرکت‌کننده‌ها از `dims`/`coords` استفاده کنید.

</div>

### 2. Hamiltonian Monte Carlo and NUTS (conceptually) · 2. Hamiltonian Monte Carlo و NUTS (به‌طور مفهومی)

Random-walk Metropolis proposes blind steps and wastes most of them in high dimensions or along correlated ridges (Weeks 11–12). **Hamiltonian Monte Carlo** (HMC) treats the negative log posterior as a landscape and the current parameter vector as a frictionless ball. Give the ball a random push (momentum), let it roll for a while following the landscape's gradient, and propose where it ends up. Proposals can be far away yet still in high-probability regions, so acceptance is high and autocorrelation low. **NUTS** (the No-U-Turn Sampler) tunes the rolling time automatically. HMC needs gradients, which PyMC computes for you.

<div dir="rtl">

Metropolis گام تصادفی گام‌های کورکورانه پیشنهاد می‌دهد و در ابعاد بالا یا در امتداد ridgeهای همبسته بیشترشان را هدر می‌دهد (هفته‌های 11–12). **Hamiltonian Monte Carlo** (HMC) منفی لگاریتم پسین را یک منظره و بردار فعلی پارامتر را یک توپ بدون اصطکاک در نظر می‌گیرد. به توپ یک ضربه‌ی تصادفی (تکانه) بدهید، بگذارید مدتی با دنبال کردن گرادیان منظره بغلتد، و جایی را که به آن می‌رسد پیشنهاد دهید. پیشنهادها می‌توانند دور باشند و هنوز در نواحی پراحتمال، پس پذیرش بالا و خودهمبستگی پایین است. **NUTS** (No-U-Turn Sampler) زمان غلتیدن را خودکار تنظیم می‌کند. HMC به گرادیان نیاز دارد که PyMC برایتان حساب می‌کند.

</div>

**Divergences.** The rolling is simulated numerically in small steps. Where the posterior's curvature changes abruptly (typically in "funnels", below), the simulation becomes inaccurate and NUTS flags a **divergent transition**. Even a few divergences mean the posterior is not being explored reliably there. Do not ignore them; reparameterize.

<div dir="rtl">

**Divergenceها.** غلتیدن به‌صورت عددی در گام‌های کوچک شبیه‌سازی می‌شود. جایی که انحنای پسین ناگهان تغییر می‌کند (معمولاً در «قیف‌ها»، در ادامه)، شبیه‌سازی نادقیق می‌شود و NUTS یک **divergence** (divergent transition) را علامت می‌زند. حتی چند divergence یعنی پسین آنجا به‌طور قابل اعتماد کاوش نمی‌شود. نادیده‌شان نگیرید؛ reparameterize کنید.

</div>

> **Advanced:** HMC simulates Hamiltonian dynamics with energy $H(\boldsymbol\theta, \mathbf{p}) = -\ln\tilde p(\boldsymbol\theta) + \tfrac12\mathbf{p}^\top M^{-1}\mathbf{p}$ using the leapfrog integrator. Exact dynamics conserve $H$, so proposals would always be accepted. The leapfrog error makes a Metropolis correction necessary, and a divergence is a trajectory whose energy error explodes.

<div dir="rtl">

> **پیشرفته:** HMC دینامیک هامیلتونی با انرژی $H(\boldsymbol\theta, \mathbf{p}) = -\ln\tilde p(\boldsymbol\theta) + \tfrac12\mathbf{p}^\top M^{-1}\mathbf{p}$ را با انتگرال‌گیر leapfrog شبیه‌سازی می‌کند. دینامیک دقیق $H$ را پایسته نگه می‌دارد، پس پیشنهادها همیشه پذیرفته می‌شدند. خطای leapfrog یک تصحیح Metropolis را لازم می‌کند، و یک divergence مسیری است که خطای انرژی‌اش منفجر می‌شود.

</div>

### 3. Hierarchical models · 3. مدل‌های سلسله‌مراتبی

**Structure (for SDT with $J$ participants):**

<div dir="rtl">

**ساختار (برای SDT با $J$ شرکت‌کننده):**

</div>

$$
\begin{aligned}
&\text{Group level:} && \mu_d \sim \mathcal{N}(1, 1),\ \ \sigma_d \sim \mathcal{N}^{+}(0, 1),\ \ \mu_c \sim \mathcal{N}(0, 1),\ \ \sigma_c \sim \mathcal{N}^{+}(0, 1)\\
&\text{Individual level:} && d'_j \sim \mathcal{N}(\mu_d, \sigma_d),\ \ c_j \sim \mathcal{N}(\mu_c, \sigma_c), \quad j = 1, \dots, J\\
&\text{Data:} && \text{hits}_j \sim \mathrm{Binomial}\big(n_s, \Phi(d'_j/2 - c_j)\big),\ \ \text{FAs}_j \sim \mathrm{Binomial}\big(n_n, \Phi(-d'_j/2 - c_j)\big)
\end{aligned}
$$

**Three ways to pool information (cf. Week 5):**

<div dir="rtl">

**سه راه ترکیب اطلاعات (مقایسه با هفته‌ی 5):**

</div>

| Approach | Model | What it assumes |
|---|---|---|
| Complete pooling | One $d'$ and one $c$ for everyone | $\sigma_d = \sigma_c = 0$: no individual differences |
| No pooling | Separate $d'_j$, $c_j$ with fixed, independent priors | $\sigma \to \infty$: participants tell us nothing about each other |
| **Partial pooling** | Hierarchical; $\sigma_d$, $\sigma_c$ *estimated* | The data decide how similar participants are |

<div dir="rtl">

| رویکرد | مدل | فرضش چیست |
|---|---|---|
| complete pooling | یک $d'$ و یک $c$ برای همه | $\sigma_d = \sigma_c = 0$: بدون تفاوت فردی |
| no pooling | $d'_j$ و $c_j$ جداگانه با پیشین‌های ثابت و مستقل | $\sigma \to \infty$: شرکت‌کننده‌ها هیچ چیزی درباره‌ی هم به ما نمی‌گویند |
| **partial pooling** | سلسله‌مراتبی؛ $\sigma_d$ و $\sigma_c$ *برآورد می‌شوند* | داده‌ها تصمیم می‌گیرند شرکت‌کننده‌ها چقدر شبیه هم‌اند |

</div>

**Shrinkage.** For a normal approximation, the hierarchical estimate of participant $j$ is a precision-weighted average of their own estimate $\hat d_j$ (with standard error $\mathrm{SE}_j$) and the group mean:

<div dir="rtl">

**shrinkage.** با یک تقریب نرمال، برآورد سلسله‌مراتبی شرکت‌کننده‌ی $j$ میانگین وزنی (با وزن دقت) برآورد خودش $\hat d_j$ (با خطای استاندارد $\mathrm{SE}_j$) و میانگین گروه است:

</div>

$$
\mathbb{E}[d'_j \mid \text{data}] \approx \frac{\hat d_j/\mathrm{SE}_j^2 + \mu_d/\sigma_d^2}{1/\mathrm{SE}_j^2 + 1/\sigma_d^2}.
$$

Participants with **noisier** data (larger $\mathrm{SE}_j$) are shrunk **more**. If people really differ a lot (large $\sigma_d$), shrinkage is weak; if they are similar, it is strong. This is learned from the data.

<div dir="rtl">

شرکت‌کننده‌هایی با داده‌ی **پرنویزتر** ($\mathrm{SE}_j$ بزرگ‌تر) **بیشتر** shrink می‌شوند. اگر آدم‌ها واقعاً خیلی با هم فرق داشته باشند ($\sigma_d$ بزرگ)، shrinkage ضعیف است؛ اگر شبیه هم باشند، قوی است. این از روی داده یاد گرفته می‌شود.

</div>

**Why shrinkage is good, not a distortion:** across participants, shrunken estimates are on average *closer to the true values* than the raw individual estimates. This is a famous result in statistics (Stein's paradox). Extreme raw estimates are partly extreme by chance, and shrinkage corrects for that regression to the mean.

<div dir="rtl">

**چرا shrinkage خوب است، نه تحریف:** در کل شرکت‌کننده‌ها، برآوردهای shrinkشده به‌طور میانگین *به مقادیر واقعی نزدیک‌ترند* تا برآوردهای فردی خام. این یک نتیجه‌ی معروف در آمار است (پارادوکس Stein). برآوردهای خام حدی تا حدی از روی شانس حدی‌اند، و shrinkage این بازگشت به میانگین را جبران می‌کند.

</div>

**Group-level questions** are answered directly by the posteriors of $\mu_d$ (typical sensitivity) and $\sigma_d$ (individual differences), and group comparisons are made by adding group or condition effects to the group level.

<div dir="rtl">

**سؤال‌های سطح گروه** مستقیماً با پسین‌های $\mu_d$ (حساسیت معمول) و $\sigma_d$ (تفاوت‌های فردی) جواب داده می‌شوند، و مقایسه‌ی گروه‌ها با افزودن اثرهای گروه یا شرط به سطح گروه انجام می‌شود.

</div>

#### Reading the math · خواندن ریاضی

- **Two levels.** Group level: $\mu_d$ (typical sensitivity) and $\sigma_d$ (how much people differ). Individual level: $d'_j \sim \mathcal{N}(\mu_d, \sigma_d)$, person $j$'s sensitivity is drawn from the group distribution. Data level: the hits and false alarms of person $j$ depend only on that person's $d'_j$ and $c_j$.
- $\mathcal{N}^{+}(0, 1)$: a "half-normal" distribution, a normal curve folded at 0 so only positive values remain (a standard deviation cannot be negative).
- **The shrinkage formula** is a precision-weighted average (as in Week 12): the person's own estimate $\hat d_j$ has precision $1/\mathrm{SE}_j^2$, the group distribution has precision $1/\sigma_d^2$. Example from the worked example: $\mathrm{SE} = 0.40$ gives precision 6.25, the group gives 4, so the estimate is $(6.25 \times 2.4 + 4 \times 1.3)/10.25 = 1.97$: the raw 2.4 moves 40% of the way toward the group mean 1.3.
- If people really differ a lot (large $\sigma_d$), the group precision is small and shrinkage is weak. If they are similar, shrinkage is strong.

<div dir="rtl">

- **دو سطح.** سطح گروه: $\mu_d$ (حساسیت معمول) و $\sigma_d$ (آدم‌ها چقدر با هم فرق دارند). سطح فرد: $d'_j \sim \mathcal{N}(\mu_d, \sigma_d)$، یعنی حساسیت نفر $j$ از توزیع گروه کشیده می‌شود. سطح داده: hitها و false alarmهای نفر $j$ فقط به $d'_j$ و $c_j$ همان نفر بستگی دارند.
- $\mathcal{N}^{+}(0, 1)$: توزیع «نیم‌نرمال» (half-normal)، یک منحنی نرمال که در 0 تا شده و فقط مقدارهای مثبت در آن مانده‌اند (انحراف معیار نمی‌تواند منفی باشد).
- **فرمول shrinkage** یک میانگین وزنی با دقت است (مثل هفته‌ی 12): برآورد خود فرد $\hat d_j$ دقت $1/\mathrm{SE}_j^2$ دارد و توزیع گروه دقت $1/\sigma_d^2$. مثال حل‌شده: $\mathrm{SE} = 0.40$ دقت 6.25 می‌دهد و گروه 4، پس برآورد $(6.25 \times 2.4 + 4 \times 1.3)/10.25 = 1.97$ است: مقدار خام 2.4، 40% راه را به سمت میانگین گروه یعنی 1.3 می‌رود.
- اگر آدم‌ها واقعاً خیلی با هم فرق داشته باشند ($\sigma_d$ بزرگ)، دقت گروه کم و shrinkage ضعیف است. اگر شبیه هم باشند، shrinkage قوی است.

</div>

### 4. Centered vs. non-centered parameterization · 4. پارامترسازی centered در برابر non-centered

Writing $d'_j \sim \mathcal{N}(\mu_d, \sigma_d)$ directly (the **centered** form) creates a "funnel" in the posterior: when $\sigma_d$ is small, all $d'_j$ must be squeezed close together, and when it is large they can spread out. NUTS struggles with this changing geometry and produces divergences, especially with few data per participant. The **non-centered** form samples standardized deviations and builds $d'_j$ deterministically:

<div dir="rtl">

نوشتن مستقیم $d'_j \sim \mathcal{N}(\mu_d, \sigma_d)$ (شکل **centered**) در پسین یک «قیف» می‌سازد: وقتی $\sigma_d$ کوچک است همه‌ی $d'_j$ها باید به هم فشرده شوند و وقتی بزرگ است می‌توانند پخش شوند. NUTS با این هندسه‌ی متغیر به زحمت می‌افتد و divergence تولید می‌کند، به‌خصوص با داده‌ی کم برای هر شرکت‌کننده. شکل **non-centered** انحراف‌های استانداردشده را نمونه‌گیری می‌کند و $d'_j$ را به‌طور قطعی می‌سازد:

</div>

$$
z_j \sim \mathcal{N}(0, 1), \qquad d'_j = \mu_d + \sigma_d z_j.
$$

It describes the same model but has a much friendlier geometry. Use it by default when data per participant are sparse.

<div dir="rtl">

همان مدل را توصیف می‌کند ولی هندسه‌ی خیلی دوستانه‌تری دارد. وقتی داده برای هر شرکت‌کننده کم است، به‌طور پیش‌فرض از آن استفاده کنید.

</div>

#### Reading the math · خواندن ریاضی

$z_j \sim \mathcal{N}(0, 1)$, $d'_j = \mu_d + \sigma_d z_j$: instead of sampling $d'_j$ directly, sample a standardized "how unusual is this person" score $z_j$ (in units of the group SD) and rebuild $d'_j$ from it. Both versions describe exactly the same model. The difference is only in what the sampler has to explore: in the centered form, the allowed range of every $d'_j$ shrinks to almost nothing when $\sigma_d$ is small (a funnel); in the non-centered form, the $z_j$ always live on the same scale, so the sampler's step size fits everywhere.

<div dir="rtl">

$z_j \sim \mathcal{N}(0, 1)$ و $d'_j = \mu_d + \sigma_d z_j$: به جای نمونه‌گیری مستقیم $d'_j$، یک نمره‌ی استانداردشده‌ی «این فرد چقدر غیرعادی است» یعنی $z_j$ (بر حسب انحراف معیار گروه) را نمونه بگیر و $d'_j$ را از روی آن بساز. هر دو نسخه دقیقاً یک مدل را توصیف می‌کنند. تفاوت فقط در چیزی است که نمونه‌گیر باید کاوش کند: در شکل centered، وقتی $\sigma_d$ کوچک است، محدوده‌ی مجاز هر $d'_j$ تقریباً به هیچ می‌رسد (یک قیف)؛ در شکل non-centered، $z_j$ها همیشه روی یک مقیاس‌اند، پس اندازه‌ی گام نمونه‌گیر همه‌جا مناسب است.

</div>

### 5. The Bayesian workflow · 5. گردش کار بیزی

1. **Specify** the model and priors (with justification).
2. **Prior predictive check** (Week 9): does the prior imply plausible data?
3. **Fit** with several chains.
4. **Diagnose:** $\hat R$, ESS, divergences, trace plots (Week 12).
5. **Posterior predictive check** (Week 10): can the fitted model reproduce the data?
6. **Compare** models if needed (LOO via ArviZ, Bayes factors; Weeks 6, 10).
7. **Interpret and report.**

<div dir="rtl">

1. مدل و پیشین‌ها را (با توجیه) **تعریف کنید**.
2. **بررسی پیش‌بینی پیشین** (هفته‌ی 9): آیا پیشین داده‌های معقولی نتیجه می‌دهد؟
3. با چند زنجیره **برازش کنید**.
4. **تشخیص دهید:** $\hat R$، ESS، divergenceها، trace plotها (هفته‌ی 12).
5. **بررسی پیش‌بینی پسین** (هفته‌ی 10): آیا مدل برازش‌شده می‌تواند داده‌ها را بازتولید کند؟
6. در صورت نیاز مدل‌ها را **مقایسه کنید** (LOO با ArviZ، Bayes factor؛ هفته‌های 6، 10).
7. **تفسیر و گزارش کنید.**

</div>

#### For an engineer · برای یک مهندس

- **Hierarchical model = estimation with a population prior.** It is like estimating each user's channel gain from a few pilots while also learning the distribution of gains in the cell, and using it as the prior: an **empirical-Bayes / MMSE** estimator. Shrinkage toward the group mean is the same phenomenon as the **James–Stein** estimator, which beats separate ML estimates in total squared error when there are three or more units.
- **HMC/NUTS** simulates Hamiltonian dynamics (a frictionless particle on the surface −log posterior) with a numerical integrator (leapfrog), as in physics simulations. A **divergence** is the integrator becoming unstable because the step size is too large for the local curvature, like a stiff ODE integrated with a too-large step.
- **Non-centered parameterization** is a change of variables that normalizes the variables to unit scale, i.e. it improves the conditioning of the problem, much like whitening or normalizing inputs before an adaptive algorithm.
- **PyMC** computes gradients automatically (automatic differentiation), the same technology that trains neural networks.

<div dir="rtl">

- **مدل سلسله‌مراتبی = تخمین با یک prior جمعیتی.** مثل این است که بهره‌ی کانال هر کاربر را از چند pilot تخمین بزنید و هم‌زمان توزیع بهره‌ها در سلول را یاد بگیرید و از آن به‌عنوان prior استفاده کنید: یک تخمین‌گر **empirical Bayes / MMSE**. shrinkage به سمت میانگین گروه همان پدیده‌ی تخمین‌گر **James–Stein** است که وقتی سه واحد یا بیشتر داریم، در مجموع خطای مربعی از تخمین‌های ML جداگانه بهتر است.
- **HMC/NUTS** دینامیک همیلتونی (یک ذره‌ی بدون اصطکاک روی سطح منفی لگاریتم posterior) را با یک انتگرال‌گیر عددی (leapfrog) شبیه‌سازی می‌کند، مثل شبیه‌سازی‌های فیزیکی. یک **divergence** یعنی انتگرال‌گیر ناپایدار شده چون اندازه‌ی گام برای انحنای محلی خیلی بزرگ است؛ مثل یک معادله‌ی دیفرانسیل سخت (stiff) که با گام خیلی بزرگ انتگرال‌گیری شود.
- **پارامتری‌سازی non-centered** یک تغییر متغیر است که متغیرها را به مقیاس واحد نرمال می‌کند، یعنی حالت (conditioning) مسئله را بهتر می‌کند؛ شبیه سفید کردن یا نرمال کردن ورودی‌ها پیش از یک الگوریتم تطبیقی.
- **PyMC** گرادیان‌ها را خودکار حساب می‌کند (automatic differentiation)، همان فناوری‌ای که شبکه‌های عصبی را آموزش می‌دهد.

</div>

#### For the instructor · برای مدرس

- **Introduce shrinkage with a sports or exam example.** A student who answered 3 of 3 questions correctly is probably not a "100% student"; a student with 95 of 100 probably is near 95%. Ask the class how they would combine individual and class information: they invent partial pooling themselves.
- **Show the shrinkage plot from lab Part D**: raw estimates, hierarchical estimates and the group mean on one figure, with arrows. It makes the idea stick.
- **Do not teach HMC mathematics in depth.** One picture (a ball rolling on the negative log posterior, given a random push) is enough; the important practical skill is reading the diagnostics (divergences, $\hat R$, ESS).
- **Running PyMC in class:** on Windows use `cores=1` in scripts, and start sampling early (Part C), since it can take a few minutes.
- **Typical questions.**
  - *"Isn't shrinkage biasing the results?"* Slightly, but it reduces the total error, so estimates are closer to the truth on average.
  - *"Is a hierarchical model always better?"* When individuals have enough data, results are similar to separate fits; the gain is largest with little data per person.
  - *"What does a divergence mean for my results?"* That part of the posterior was not explored reliably. Reparameterize and rerun until there are none.

<div dir="rtl">

- **shrinkage را با یک مثال ورزشی یا امتحانی معرفی کنید.** دانشجویی که 3 از 3 سؤال را درست جواب داده احتمالاً «دانشجوی 100%» نیست؛ دانشجویی با 95 از 100 احتمالاً نزدیک 95% است. از کلاس بپرسید اطلاعات فردی و کلاسی را چطور ترکیب می‌کنند: خودشان partial pooling را اختراع می‌کنند.
- **نمودار shrinkage بخش D lab را نشان دهید:** برآوردهای خام، برآوردهای سلسله‌مراتبی و میانگین گروه روی یک شکل، با پیکان. ایده را ماندگار می‌کند.
- **ریاضی HMC را عمیق درس ندهید.** یک تصویر (یک توپ که روی منفی لگاریتم posterior با یک ضربه‌ی تصادفی می‌غلتد) کافی است؛ مهارت عملی مهم، خواندن شاخص‌های تشخیصی است (divergence، $\hat R$، ESS).
- **اجرای PyMC در کلاس:** روی Windows در اسکریپت‌ها از `cores=1` استفاده کنید و نمونه‌گیری را زود شروع کنید (بخش C)، چون ممکن است چند دقیقه طول بکشد.
- **سؤال‌های رایج.**
  - *«آیا shrinkage نتایج را سوگیر نمی‌کند؟»* کمی، ولی خطای کل را کم می‌کند، پس برآوردها به‌طور میانگین به حقیقت نزدیک‌ترند.
  - *«آیا مدل سلسله‌مراتبی همیشه بهتر است؟»* وقتی افراد داده‌ی کافی دارند، نتایج شبیه برازش‌های جداگانه است؛ بیشترین سود وقتی است که برای هر نفر داده کم است.
  - *«divergence برای نتایجم یعنی چه؟»* یعنی بخشی از posterior به‌طور قابل اعتماد کاوش نشده. reparameterize کنید و دوباره اجرا کنید تا هیچ divergenceای نماند.

</div>

---

## Worked example · مثال حل‌شده

**Shrinkage by hand.** The group posterior has $\mu_d \approx 1.3$ and $\sigma_d \approx 0.5$ (group precision $1/0.5^2 = 4$). Two participants both have a raw estimate $\hat d_j = 2.4$.

<div dir="rtl">

**shrinkage با دست.** پسین گروه $\mu_d \approx 1.3$ و $\sigma_d \approx 0.5$ دارد (دقت گروه $1/0.5^2 = 4$). دو شرکت‌کننده هر دو برآورد خام $\hat d_j = 2.4$ دارند.

</div>

| Participant | $\mathrm{SE}_j$ | Individual precision $1/\mathrm{SE}_j^2$ | Hierarchical estimate | Posterior SD |
|---|---|---|---|---|
| P1 (few trials) | 0.40 | 6.25 | $(6.25 \times 2.4 + 4 \times 1.3)/(6.25 + 4) = 20.2/10.25 = \mathbf{1.97}$ | $1/\sqrt{10.25} = 0.31$ |
| P2 (many trials) | 0.20 | 25 | $(25 \times 2.4 + 4 \times 1.3)/(25 + 4) = 65.2/29 = \mathbf{2.25}$ | $1/\sqrt{29} = 0.19$ |

<div dir="rtl">

| شرکت‌کننده | $\mathrm{SE}_j$ | دقت فردی $1/\mathrm{SE}_j^2$ | برآورد سلسله‌مراتبی | انحراف معیار پسین |
|---|---|---|---|---|
| P1 (trial کم) | 0.40 | 6.25 | $(6.25 \times 2.4 + 4 \times 1.3)/(6.25 + 4) = 20.2/10.25 = \mathbf{1.97}$ | $1/\sqrt{10.25} = 0.31$ |
| P2 (trial زیاد) | 0.20 | 25 | $(25 \times 2.4 + 4 \times 1.3)/(25 + 4) = 65.2/29 = \mathbf{2.25}$ | $1/\sqrt{29} = 0.19$ |

</div>

**Interpretation.** Both participants *look* equally sensitive, but P1's estimate rests on less data, so the model trusts it less and moves it 0.43 toward the group mean. P2 moves only 0.15. Both posterior SDs are smaller than the raw SEs, because the group distribution adds information. (In the full model, $\mu_d$ and $\sigma_d$ are themselves uncertain and estimated jointly; this calculation fixes them for illustration.)

<div dir="rtl">

**تفسیر.** هر دو شرکت‌کننده *به نظر* به یک اندازه حساس‌اند، ولی برآورد P1 بر داده‌ی کمتری تکیه دارد، پس مدل کمتر به آن اعتماد می‌کند و آن را 0.43 به سمت میانگین گروه جابه‌جا می‌کند. P2 فقط 0.15 جابه‌جا می‌شود. هر دو انحراف معیار پسین از SEهای خام کوچک‌ترند، چون توزیع گروه اطلاعات اضافه می‌کند. (در مدل کامل، $\mu_d$ و $\sigma_d$ خودشان نامطمئن‌اند و هم‌زمان برآورد می‌شوند؛ این محاسبه برای توضیح آن‌ها را ثابت می‌گیرد.)

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Simulate a 12-participant experiment and compute individual (no-pooling) estimates.
2. Write the hierarchical SDT model in PyMC with a non-centered parameterization; run a prior predictive check.
3. Sample with NUTS; check $\hat R$, ESS and divergences.
4. Visualize shrinkage and compare the estimates with the true values.
5. Run a posterior predictive check and interpret the group-level parameters.

<div dir="rtl">

1. شبیه‌سازی یک آزمایش با 12 شرکت‌کننده و محاسبه‌ی برآوردهای فردی (no pooling).
2. نوشتن مدل SDT سلسله‌مراتبی در PyMC با پارامترسازی non-centered؛ اجرای یک بررسی پیش‌بینی پیشین.
3. نمونه‌گیری با NUTS؛ بررسی $\hat R$، ESS و divergenceها.
4. نمایش shrinkage و مقایسه‌ی برآوردها با مقادیر واقعی.
5. اجرای یک بررسی پیش‌بینی پسین و تفسیر پارامترهای سطح گروه.

</div>

**Timing:** Part A 10 min · Part B 20 min · Part C 25 min · Part D 30 min · Part E 20 min · Part F 15 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 10 دقیقه · بخش B 20 دقیقه · بخش C 25 دقیقه · بخش D 30 دقیقه · بخش E 20 دقیقه · بخش F 15 دقیقه.

</div>

> **Run time:** sampling takes from under a minute (conda-forge install with a compiler) up to about 2–3 minutes (no compiler). Start Part C early.

<div dir="rtl">

> **زمان اجرا:** نمونه‌گیری از کمتر از یک دقیقه (نصب conda-forge با compiler) تا حدود 2 تا 3 دقیقه (بدون compiler) طول می‌کشد. بخش C را زود شروع کنید.

</div>

### Part A: data and no-pooling estimates (10 min) · بخش A: داده و برآوردهای no pooling (10 دقیقه)

> **Code · کد:** [`code/week13.py`](code/week13.py), cell 1 · سلول 1

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
    hits  fas  d_true  d_indiv  c_true  c_indiv
0     46    2    2.21     3.01    0.13     0.15
1     16   25   -0.24    -0.46    0.42     0.23
2     28    6    1.78     1.29    0.41     0.50
3     40   11    1.33     1.57    0.05    -0.03
4     43    9    1.96     1.94    0.09    -0.08
5     43   17    1.49     1.45   -0.34    -0.32
6     31    0    2.21     2.63    0.70     1.02
7     35   11    1.32     1.27    0.13     0.12
8     24    8    1.04     0.92    0.60     0.51
9     39    8    1.59     1.72    0.33     0.11
10    27    3    1.52     1.58    0.78     0.69
11    21    9    1.12     0.69    0.66     0.54
```

### Part B: the model in PyMC, and a prior predictive check (20 min) · بخش B: مدل در PyMC، و یک بررسی پیش‌بینی پیشین (20 دقیقه)

> **Code · کد:** [`code/week13.py`](code/week13.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Share of prior-predictive rates exactly 0 or 1: 0.30
```

The prior implies a broad range of hit and false-alarm rates, mostly above the diagonal. About 30% of simulated participants have a hit or false-alarm count of exactly 0 or 50. These are mostly participants simulated with very high sensitivity and a strong bias, which produce zero false alarms. This is far better than the 96% of the "vague" prior in Week 9, but still on the generous side: tightening the priors on `sigma_d` and `sigma_c` (e.g., `HalfNormal(0.5)`) would remove most of them. Try it and check whether the posterior changes.

<div dir="rtl">

پیشین دامنه‌ی وسیعی از نرخ‌های hit و false alarm را نتیجه می‌دهد که بیشترشان بالای قطرند. حدود 30% شرکت‌کننده‌های شبیه‌سازی‌شده شمارش hit یا false alarm دقیقاً 0 یا 50 دارند. این‌ها بیشتر شرکت‌کننده‌هایی‌اند که با حساسیت خیلی بالا و سوگیری قوی شبیه‌سازی شده‌اند و false alarm صفر تولید می‌کنند. این خیلی بهتر از 96% پیشین «مبهم» هفته‌ی 9 است، ولی هنوز کمی دست‌ودل‌باز است: تنگ‌تر کردن پیشین‌های `sigma_d` و `sigma_c` (مثلاً `HalfNormal(0.5)`) بیشترشان را حذف می‌کند. امتحانش کنید و ببینید آیا پسین تغییر می‌کند.

</div>

### Part C: sampling and diagnostics (25 min) · بخش C: نمونه‌گیری و تشخیص همگرایی (25 دقیقه)

> **Code · کد:** [`code/week13.py`](code/week13.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
        ess_bulk ess_tail r_hat mcse_mean mcse_sd
mu_d        1303     1651  1.00    0.0075  0.0054
sigma_d     1639     2088  1.00    0.0055  0.0045
mu_c        1312     1474  1.00    0.0036   0.003
sigma_c     1203     1748  1.00    0.0034  0.0047
Number of divergent transitions: 0
Max R-hat over all individual d and c: 1.0023234826538692
```

### Part D: shrinkage and group-level inference (30 min) · بخش D: shrinkage و استنباط سطح گروه (30 دقیقه)

> **Code · کد:** [`code/week13.py`](code/week13.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
RMSE vs. true d':  no pooling = 0.339,  hierarchical = 0.279
mu_d     posterior mean = 1.45, 95% interval = [0.90, 1.95]
sigma_d  posterior mean = 0.90, 95% interval = [0.56, 1.42]
mu_c     posterior mean = 0.29, 95% interval = [0.04, 0.55]
sigma_c  posterior mean = 0.38, 95% interval = [0.22, 0.65]
P(mu_c > 0 | data) = 0.987
```

**Interpret (write in your notebook):**
1. Which participants are shrunk most, and why? Find one whose raw estimate is extreme and describe what the hierarchical model does with it.
2. Is the hierarchical estimate closer to the truth on average? Is it closer for *every* participant? Why is that not required?
3. What do $\mu_d$ and $\sigma_d$ tell you about this population? Compare $\sigma_d$ with the SD used to simulate the data (0.5) and explain the difference (hint: 12 participants).

<div dir="rtl">

**تفسیر (در notebook بنویسید):**
1. کدام شرکت‌کننده‌ها بیشتر shrink می‌شوند و چرا؟ یکی را که برآورد خامش حدی است پیدا کنید و توصیف کنید مدل سلسله‌مراتبی با آن چه می‌کند.
2. آیا برآورد سلسله‌مراتبی به‌طور میانگین به حقیقت نزدیک‌تر است؟ آیا برای *هر* شرکت‌کننده نزدیک‌تر است؟ چرا این لازم نیست؟
3. $\mu_d$ و $\sigma_d$ درباره‌ی این جمعیت چه می‌گویند؟ $\sigma_d$ را با انحراف معیاری که برای شبیه‌سازی داده استفاده شد (0.5) مقایسه کنید و تفاوت را توضیح دهید (راهنمایی: 12 شرکت‌کننده).

</div>

### Part E: posterior predictive check (20 min) · بخش E: بررسی پیش‌بینی پسین (20 دقیقه)

> **Code · کد:** [`code/week13.py`](code/week13.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Share of observed counts inside their 95% predictive interval: 1.00
```

### Part F: report (15 min) · بخش F: گزارش (15 دقیقه)

Write a methods-and-results paragraph following the Week 12 checklist: model and priors (in words and symbols), sampler and settings, diagnostics (max $\hat R$, min ESS, divergences), the PPC result, and the group-level conclusions ($\mu_d$, $\sigma_d$, $\mu_c$ with 95% intervals; $P(\mu_c > 0\mid\text{data})$).

<div dir="rtl">

یک پاراگراف روش‌ها و نتایج طبق چک‌لیست هفته‌ی 12 بنویسید: مدل و پیشین‌ها (با کلمات و نمادها)، نمونه‌گیر و تنظیمات، تشخیص‌ها (بیشترین $\hat R$، کمترین ESS، divergenceها)، نتیجه‌ی PPC، و نتیجه‌گیری‌های سطح گروه ($\mu_d$، $\sigma_d$، $\mu_c$ با بازه‌های 95%؛ $P(\mu_c > 0\mid\text{data})$).

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Fit the **complete-pooling** model (one $d'$ and one $c$ for everyone) in PyMC. Compare its estimate of $d'$ with $\mu_d$ from the hierarchical model, and its posterior predictive check with Part E. Which participants does it fail to predict?

<div dir="rtl">

**تمرین 1 ★.** مدل **complete pooling** (یک $d'$ و یک $c$ برای همه) را در PyMC برازش کنید. برآورد $d'$ آن را با $\mu_d$ مدل سلسله‌مراتبی، و بررسی پیش‌بینی پسینش را با بخش E مقایسه کنید. کدام شرکت‌کننده‌ها را نمی‌تواند پیش‌بینی کند؟

</div>

**Exercise 2 ★.** Rerun Part C with the **centered** parameterization (`d = pm.Normal("d", mu_d, sigma_d, dims="participant")`). Compare divergences, ESS and run time. Then reduce the data to 10 + 10 trials per participant and compare again.

<div dir="rtl">

**تمرین 2 ★.** بخش C را با پارامترسازی **متمرکز** (`d = pm.Normal("d", mu_d, sigma_d, dims="participant")`) دوباره اجرا کنید. divergenceها، ESS و زمان اجرا را مقایسه کنید. بعد داده را به 10 + 10 trial برای هر شرکت‌کننده کم کنید و دوباره مقایسه کنید.

</div>

**Exercise 3 ★★ (unequal trial numbers).** Give half of the participants 20 + 20 trials and the other half 200 + 200 (simulate new data). Show that shrinkage depends on the number of trials, as in the worked example.

<div dir="rtl">

**تمرین 3 ★★ (تعداد trial نابرابر).** به نیمی از شرکت‌کننده‌ها 20 + 20 trial و به نیمی دیگر 200 + 200 trial بدهید (داده‌ی جدید شبیه‌سازی کنید). نشان دهید shrinkage، مثل مثال حل‌شده، به تعداد trialها بستگی دارد.

</div>

**Exercise 4 ★★ (model comparison with LOO).** Compute the log-likelihood with `pm.compute_log_likelihood(idata)`. ArviZ's `loo` needs one pointwise log-likelihood per observation: add the `hits` and `fas` log-likelihood arrays into a single per-participant array (e.g., `idata.log_likelihood["obs"] = idata.log_likelihood["hits"] + idata.log_likelihood["fas"]`) and call `az.loo(idata, var_name="obs")`. Compare the hierarchical and complete-pooling models with `az.compare`. Check the Pareto-$k$ diagnostics and say what they mean for leave-one-participant-out prediction.

<div dir="rtl">

**تمرین 4 ★★ (مقایسه‌ی مدل با LOO).** لگاریتم درست‌نمایی را با `pm.compute_log_likelihood(idata)` حساب کنید. `loo` در ArviZ برای هر مشاهده به یک لگاریتم درست‌نمایی نقطه‌ای نیاز دارد: آرایه‌های لگاریتم درست‌نمایی `hits` و `fas` را در یک آرایه‌ی واحد برای هر شرکت‌کننده جمع کنید (مثلاً `idata.log_likelihood["obs"] = idata.log_likelihood["hits"] + idata.log_likelihood["fas"]`) و `az.loo(idata, var_name="obs")` را صدا بزنید. مدل‌های سلسله‌مراتبی و complete pooling را با `az.compare` مقایسه کنید. تشخیص‌های Pareto-$k$ را بررسی کنید و بگویید برای پیش‌بینی leave-one-participant-out چه معنایی دارند.

</div>

**Exercise 5 ★★★ (Advanced: a group effect).** Simulate two groups of 12 participants that differ in mean sensitivity by 0.4. Extend the model with a group effect $\beta$ on $\mu_d$ ($d'_j = \mu_d + \beta\cdot\text{group}_j + \sigma_d z_j$), estimate $\beta$, and report $P(\beta > 0\mid\text{data})$. Compare with a t-test on the individual $d'$ estimates.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: اثر گروه).** دو گروه 12 نفره شبیه‌سازی کنید که حساسیت میانگینشان 0.4 فرق دارد. مدل را با یک اثر گروه $\beta$ روی $\mu_d$ گسترش دهید ($d'_j = \mu_d + \beta\cdot\text{group}_j + \sigma_d z_j$)، $\beta$ را برآورد کنید و $P(\beta > 0\mid\text{data})$ را گزارش کنید. با یک آزمون t روی برآوردهای فردی $d'$ مقایسه کنید.

</div>

### Lab check-off · lab check-off

Show: (1) the diagnostics output (no divergences, $\hat R$, ESS), (2) the shrinkage plot with the RMSE comparison, and (3) the PPC plot with your Part F paragraph.

<div dir="rtl">

نشان دهید: (1) خروجی تشخیص‌ها (بدون divergence، $\hat R$، ESS)، (2) نمودار shrinkage با مقایسه‌ی RMSE، و (3) نمودار PPC همراه با پاراگراف بخش F.

</div>

**Project progress check (this week):** submit a one-page status report (what is done, a first fit or simulation figure, open problems). It is not graded; written feedback is returned within a week.

<div dir="rtl">

**گزارش پیشرفت پروژه (این هفته):** یک گزارش وضعیت یک‌صفحه‌ای تحویل دهید (چه کارهایی انجام شده، یک نمودار برازش یا شبیه‌سازی اولیه، مسائل باز). نمره ندارد؛ بازخورد کتبی ظرف یک هفته داده می‌شود.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Partial pooling for AI benchmarks.** Benchmarks are split into task categories, and some categories have only a handful of items. Reporting raw accuracy per category gives noisy, sometimes extreme numbers, just like individual SDT fits with few trials. A hierarchical model treats category accuracies as draws from a common distribution and shrinks small categories toward the overall mean. The code below uses a fast empirical-Bayes version, a beta-binomial model whose group parameters are estimated by maximizing the marginal likelihood on a grid. In the exercises you fit the full Bayesian version in PyMC.

<div dir="rtl">

**partial pooling برای benchmarkهای هوش مصنوعی.** benchmarkها به دسته‌های تکلیف تقسیم می‌شوند، و بعضی دسته‌ها فقط چند آیتم دارند. گزارش دقت خام برای هر دسته عددهای پرنویز و گاهی حدی می‌دهد، درست مثل برازش‌های فردی SDT با trialهای کم. یک مدل سلسله‌مراتبی دقت دسته‌ها را نمونه‌هایی از یک توزیع مشترک در نظر می‌گیرد و دسته‌های کوچک را به سمت میانگین کلی shrink می‌کند. کد پایین از یک نسخه‌ی سریع empirical-Bayes استفاده می‌کند: یک مدل beta-binomial که پارامترهای گروهش با بیشینه کردن marginal likelihood روی یک grid برآورد می‌شوند. در تمرین‌ها نسخه‌ی بیزی کامل را در PyMC برازش می‌کنید.

</div>

> **Code · کد:** [`code/week13.py`](code/week13.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
items   true    raw  shrunk
    5  0.72  0.80   0.71
    8  0.63  0.88   0.74
   10  0.64  0.50   0.63
   15  0.63  0.67   0.68
   25  0.76  0.88   0.80
   40  0.69  0.55   0.60
   60  0.80  0.78   0.76
   80  0.51  0.57   0.60
group mean = 0.69, concentration = 19.9;  RMSE raw = 0.125, shrunk = 0.066
```

The 8-item category (raw 0.88, true 0.63) is pulled down strongly, and the shrunken estimates are about twice as accurate overall (RMSE 0.066 vs. 0.125).

<div dir="rtl">

دسته‌ی 8آیتمی (خام 0.88، واقعی 0.63) به‌شدت پایین کشیده می‌شود، و برآوردهای shrinkشده در مجموع حدود دو برابر دقیق‌ترند (RMSE برابر 0.066 در برابر 0.125).

</div>

**Try it (no API needed).**
- ★ Which categories move most, and why? Relate your answer to the shrinkage formula in this week's lecture notes.
- ★★ Fit the same model in PyMC: `mu ~ Beta(2, 2)`, `kappa ~ Gamma(2, 0.1)` (shape and rate), `theta_j ~ Beta(mu * kappa, (1 - mu) * kappa)`, `y_j ~ Binomial(n_j, theta_j)`. Compare the posterior means with the empirical-Bayes estimates, and check the diagnostics.
- ★★ Discussion: a leaderboard highlights "the category where Model X is weakest", a category with 5 items. What would you tell the authors?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ کدام دسته‌ها بیشتر از همه جابه‌جا می‌شوند، و چرا؟ جوابتان را به فرمول shrinkage در جزوه‌ی درس این هفته ربط دهید.
- ★★ همین مدل را در PyMC برازش کنید: `mu ~ Beta(2, 2)`، `kappa ~ Gamma(2, 0.1)` (shape و rate)، `theta_j ~ Beta(mu * kappa, (1 - mu) * kappa)`، `y_j ~ Binomial(n_j, theta_j)`. میانگین‌های پسین را با برآوردهای empirical-Bayes مقایسه کنید و تشخیص‌ها را بررسی کنید.
- ★★ بحث: یک جدول رتبه‌بندی «دسته‌ای که مدل X در آن ضعیف‌ترین است» را برجسته می‌کند، که یک دسته‌ی 5آیتمی است. به نویسندگان چه می‌گویید؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **"Shrinkage biases the results."** It trades a little bias for a large reduction in variance and gives more accurate estimates on average. It is principled, not an ad-hoc correction.
2. **Ignoring divergences.** Even a handful indicate unreliable exploration. Reparameterize (non-centered), tighten priors on scale parameters, or increase `target_accept`.
3. **Centered parameterization with sparse data.** It invites funnels and divergences. Default to non-centered for hierarchical models with few trials per participant.
4. **Vague priors on group SDs.** Very wide priors on $\sigma$ can produce implausible prior predictions and sampling problems. Half-normal priors on a sensible scale are usually better.
5. **Treating the black box as magic.** PyMC samples whatever model you wrote, including wrong ones. The workflow (prior predictive check, diagnostics, PPC) still applies in full.
6. **Running multi-process sampling from a script on Windows without a main guard,** which causes cryptic multiprocessing errors. Use `cores=1` or `if __name__ == "__main__":`.
7. **Reporting only individual estimates.** The group-level parameters often answer the actual research question.

<div dir="rtl">

1. **«shrinkage نتایج را سوگیر می‌کند.»** کمی سوگیری را با کاهش زیاد واریانس معاوضه می‌کند و به‌طور میانگین برآوردهای دقیق‌تری می‌دهد. اصولی است، نه یک تصحیح موقت.
2. **نادیده گرفتن divergenceها.** حتی چندتایشان نشانه‌ی کاوش غیرقابل اعتماد است. reparameterize کنید (non-centered)، پیشین‌های پارامترهای مقیاس را تنگ‌تر کنید، یا `target_accept` را بالا ببرید.
3. **پارامترسازی centered با داده‌ی کم.** قیف و divergence می‌سازد. برای مدل‌های سلسله‌مراتبی با trialهای کم برای هر شرکت‌کننده، به‌طور پیش‌فرض از non-centered استفاده کنید.
4. **پیشین‌های مبهم برای انحراف معیارهای گروه.** پیشین‌های خیلی پهن روی $\sigma$ می‌توانند پیش‌بینی‌های پیشین نامعقول و مشکلات نمونه‌گیری بسازند. پیشین‌های نیم‌نرمال با مقیاس معقول معمولاً بهترند.
5. **جادو دانستن جعبه‌ی سیاه.** PyMC از هر مدلی که بنویسید، از جمله مدل‌های غلط، نمونه می‌گیرد. گردش کار (بررسی پیش‌بینی پیشین، تشخیص‌ها، PPC) همچنان کامل لازم است.
6. **اجرای نمونه‌گیری چندپردازشی از یک اسکریپت در Windows بدون main guard،** که خطاهای مبهم multiprocessing می‌دهد. از `cores=1` یا `if __name__ == "__main__":` استفاده کنید.
7. **گزارش فقط برآوردهای فردی.** پارامترهای سطح گروه اغلب به سؤال پژوهشی واقعی جواب می‌دهند.

</div>

---

## Check your understanding · خودآزمایی

**1.** What are the three ways to combine data across participants, and what does each assume about individual differences?
<details><summary>Answer</summary>
Complete pooling (everyone identical, $\sigma = 0$), no pooling (participants unrelated, so no information is shared), and partial pooling/hierarchical (participants come from a common distribution whose spread is estimated from the data).
</details>

<div dir="rtl">

**1.** سه راه ترکیب داده بین شرکت‌کننده‌ها کدام‌اند و هرکدام درباره‌ی تفاوت‌های فردی چه فرضی دارند؟
<details><summary>پاسخ</summary>
complete pooling (همه یکسان‌اند، $\sigma = 0$)، no pooling (شرکت‌کننده‌ها بی‌ارتباط‌اند، پس هیچ اطلاعاتی به اشتراک گذاشته نمی‌شود)، و partial pooling/سلسله‌مراتبی (شرکت‌کننده‌ها از یک توزیع مشترک می‌آیند که پراکندگی‌اش از داده برآورد می‌شود).
</details>

</div>

**2.** Two participants have the same raw $d'$ estimate. Why may the hierarchical model shrink one of them much more?
<details><summary>Answer</summary>
Shrinkage depends on the precision of each individual estimate. The participant with fewer trials (larger SE) carries less information and is pulled more strongly toward the group mean.
</details>

<div dir="rtl">

**2.** دو شرکت‌کننده برآورد خام $d'$ یکسانی دارند. چرا ممکن است مدل سلسله‌مراتبی یکی را خیلی بیشتر shrink کند؟
<details><summary>پاسخ</summary>
shrinkage به دقت هر برآورد فردی بستگی دارد. شرکت‌کننده‌ای که trial کمتری دارد (SE بزرگ‌تر) اطلاعات کمتری دارد و قوی‌تر به سمت میانگین گروه کشیده می‌شود.
</details>

</div>

**3.** Why is the non-centered parameterization often preferred?
<details><summary>Answer</summary>
The centered form creates a funnel-shaped posterior (individual parameters must collapse together when the group SD is small) that NUTS explores poorly, causing divergences. Sampling standardized $z_j$ and computing $d'_j = \mu + \sigma z_j$ gives a geometry that is much easier to explore.
</details>

<div dir="rtl">

**3.** چرا پارامترسازی non-centered اغلب ترجیح دارد؟
<details><summary>پاسخ</summary>
شکل centered پسینی قیفی‌شکل می‌سازد (پارامترهای فردی وقتی انحراف معیار گروه کوچک است باید به هم فشرده شوند) که NUTS بد کاوشش می‌کند و divergence می‌دهد. نمونه‌گیری $z_j$ استانداردشده و محاسبه‌ی $d'_j = \mu + \sigma z_j$ هندسه‌ای می‌دهد که کاوشش خیلی آسان‌تر است.
</details>

</div>

**4.** What is a divergent transition, and what should you do about it?
<details><summary>Answer</summary>
A NUTS trajectory whose numerical simulation broke down, usually in a region of high curvature; it signals that part of the posterior is not explored reliably. Reparameterize, use more informative priors for scale parameters, or increase `target_accept`, then check that the divergences disappear.
</details>

<div dir="rtl">

**4.** divergence چیست و باید با آن چه کرد؟
<details><summary>پاسخ</summary>
مسیری در NUTS که شبیه‌سازی عددی‌اش شکسته است، معمولاً در ناحیه‌ای با انحنای زیاد؛ نشان می‌دهد بخشی از پسین به‌طور قابل اعتماد کاوش نمی‌شود. reparameterize کنید، برای پارامترهای مقیاس از پیشین‌های آگاهی‌بخش‌تر استفاده کنید، یا `target_accept` را بالا ببرید، و بعد بررسی کنید که divergenceها ناپدید شده باشند.
</details>

</div>

**5.** Why does HMC usually mix much better than random-walk Metropolis in high dimensions?
<details><summary>Answer</summary>
It uses gradient information to make long, directed moves that follow the shape of the posterior, so distant proposals still have a high acceptance probability. Random-walk proposals become almost always rejected unless they are tiny.
</details>

<div dir="rtl">

**5.** چرا HMC معمولاً در ابعاد بالا خیلی بهتر از Metropolis گام تصادفی مخلوط می‌شود؟
<details><summary>پاسخ</summary>
از اطلاعات گرادیان برای حرکت‌های بلند و جهت‌دار که شکل پسین را دنبال می‌کنند استفاده می‌کند، پس پیشنهادهای دور هم هنوز احتمال پذیرش بالایی دارند. پیشنهادهای گام تصادفی، مگر اینکه خیلی ریز باشند، تقریباً همیشه رد می‌شوند.
</details>

</div>

**6.** In a hierarchical SDT model, which parameter answers "how much do people differ in sensitivity?", and which answers "what is the typical sensitivity?"
<details><summary>Answer</summary>
$\sigma_d$ (the group-level SD) and $\mu_d$ (the group-level mean), respectively.
</details>

<div dir="rtl">

**6.** در یک مدل SDT سلسله‌مراتبی، کدام پارامتر به «آدم‌ها چقدر در حساسیت با هم فرق دارند؟» و کدام به «حساسیت معمول چقدر است؟» جواب می‌دهد؟
<details><summary>پاسخ</summary>
به ترتیب $\sigma_d$ (انحراف معیار سطح گروه) و $\mu_d$ (میانگین سطح گروه).
</details>

</div>

**7.** List the steps of the Bayesian workflow.
<details><summary>Answer</summary>
Specify the model and priors → prior predictive check → fit with several chains → diagnose ($\hat R$, ESS, divergences, traces) → posterior predictive check → compare models if needed → interpret and report.
</details>

<div dir="rtl">

**7.** مراحل گردش کار بیزی را فهرست کنید.
<details><summary>پاسخ</summary>
تعریف مدل و پیشین‌ها ← بررسی پیش‌بینی پیشین ← برازش با چند زنجیره ← تشخیص ($\hat R$، ESS، divergenceها، traceها) ← بررسی پیش‌بینی پسین ← در صورت نیاز مقایسه‌ی مدل‌ها ← تفسیر و گزارش.
</details>

</div>

---

## Assignment · تکلیف

- **A5 (MCMC from scratch)** is due at the start of the Week 14 lecture.
- **Project progress check** this week (see above).
- No new graded assignment: the remaining weeks are reserved for the final project.

<div dir="rtl">

- **A5 (MCMC از صفر)** در ابتدای درس هفته‌ی 14 تحویل داده می‌شود.
- **گزارش پیشرفت پروژه** این هفته (بالا را ببینید).
- تکلیف نمره‌دار جدیدی نداریم: هفته‌های باقی‌مانده برای پروژه‌ی پایانی است.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Lee & Wagenmakers (2014), chapter 11.** Signal detection theory, including the hierarchical SDT model you implemented today. *(Main reading.)*
- **Kruschke (2014), chapter 9.** Hierarchical models: partial pooling and shrinkage explained step by step.
- **Farrell & Lewandowsky (2018), chapter 9.** Multilevel or hierarchical modeling of cognitive data.
- **Martin, Kumar & Lao (2021), chapters 2 and 10.** Diagnostics with ArviZ, and probabilistic programming languages (how PyMC works under the hood).

<div dir="rtl">

- **Lee & Wagenmakers (2014)، فصل 11.** نظریه‌ی تشخیص علامت، از جمله همان مدل SDT سلسله‌مراتبی‌ای که امروز پیاده‌سازی کردید. *(منبع اصلی.)*
- **Kruschke (2014)، فصل 9.** مدل‌های سلسله‌مراتبی: partial pooling و shrinkage، قدم‌به‌قدم.
- **Farrell & Lewandowsky (2018)، فصل 9.** مدل‌سازی چندسطحی یا سلسله‌مراتبی داده‌های شناختی.
- **Martin, Kumar & Lao (2021)، فصل‌های 2 و 10.** تشخیص با ArviZ، و زبان‌های برنامه‌نویسی احتمالاتی (PyMC در پشت صحنه چطور کار می‌کند).

</div>

*Preview for Week 14:* with the full toolkit in hand, we tour models from different areas of cognitive science, starting with categorization (the exemplar model GCM) and the speed–accuracy machinery of the drift-diffusion model.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 14:* با جعبه‌ابزار کامل، گشتی در مدل‌هایی از حوزه‌های مختلف علوم شناختی می‌زنیم؛ با دسته‌بندی (مدل exemplar یعنی GCM) و سازوکار سرعت–دقت مدل drift-diffusion شروع می‌کنیم.

</div>
