# Week 10: Bayesian Modeling II: Posterior Predictive Checks and Bayes Factors · هفته‌ی 10: مدل‌سازی بیزی 2: بررسی پیش‌بینی پسین و Bayes factor

> **Chapter 4: Bayesian modeling** (with Chapter 3: evaluation) · Lecture 1 h · Lab 2 h
> **Running data:** the Week 2 forgetting data (exponential vs. power), and a weak-evidence SDT participant (is $d' = 0$?).

<div dir="rtl">

> **فصل 4: مدل‌سازی بیزی** (همراه با فصل 3: ارزیابی) · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** داده‌های فراموشی هفته‌ی 2 (نمایی در برابر توانی)، و یک شرکت‌کننده‌ی SDT با شواهد ضعیف (آیا $d' = 0$ است؟).

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| posterior | توزیع پسین (posterior) | باور درباره‌ی پارامتر بعد از دیدن داده |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| evidence | شواهد | اطلاعاتی که برای تصمیم جمع می‌شود |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| posterior predictive check (PPC) | بررسی پیش‌بینی پسین | مقایسه‌ی داده‌ی شبیه‌سازی‌شده از پسین با داده‌ی واقعی |
| marginal likelihood / evidence | درست‌نمایی حاشیه‌ای | احتمال داده تحت مدل، میانگین روی پیشین |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| Bayes factor (BF) | عامل بیز (Bayes factor) | نسبت درست‌نمایی‌های حاشیه‌ای دو مدل |
| model flexibility / complexity | انعطاف‌پذیری / پیچیدگی مدل | دامنه‌ی الگوهایی که مدل می‌تواند تولید کند |
| grid approximation | تقریب شبکه‌ای (grid) | محاسبه‌ی پسین روی شبکه‌ای از مقادیر |
| Savage–Dickey ratio | نسبت Savage–Dickey | BF از نسبت چگالی پسین به پیشین در مقدار صفر |
| AIC / BIC | معیار اطلاعاتی آکائیکه / بیزی | برازش به‌علاوه‌ی جریمه برای تعداد پارامتر |
| prior | توزیع پیشین (prior) | باور درباره‌ی پارامتر پیش از دیدن داده |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| posterior odds | بخت پسین (odds) | نسبت احتمال پسین دو مدل |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| adequacy check | بررسی کفایت مدل | آیا مدل ویژگی‌های اصلی داده را بازتولید می‌کند |
| nested models | مدل‌های تودرتو (nested) | یک مدل حالت خاص مدل دیگر است |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| accuracy | دقت | نسبت پاسخ‌های درست |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Generate** posterior predictive distributions and **conduct** graphical and numerical posterior predictive checks (PPCs).
2. **Define** the marginal likelihood and the Bayes factor, and **explain** why the marginal likelihood penalizes model flexibility automatically.
3. **Compute** Bayes factors by grid integration and with the Savage–Dickey density ratio, and **compare** them with the BIC approximation.
4. **Evaluate** the sensitivity of Bayes factors to the prior, and **contrast** it with the robustness of posterior estimates.
5. **Interpret** Bayes factors on a graded evidence scale and **combine** them with prior odds into posterior model probabilities.

<div dir="rtl">

1. توزیع‌های پیش‌بینی پسین را **تولید کنند** و بررسی‌های پیش‌بینی پسین (PPC) نموداری و عددی **انجام دهند**.
2. marginal likelihood و Bayes factor را **تعریف کنند** و **توضیح دهند** چرا marginal likelihood انعطاف مدل را خودکار جریمه می‌کند.
3. Bayes factor را با انتگرال‌گیری شبکه‌ای و با نسبت چگالی Savage–Dickey **حساب کنند** و با تقریب BIC **مقایسه کنند**.
4. حساسیت Bayes factor به پیشین را **ارزیابی کنند** و آن را با پایداری برآوردهای پسین **مقایسه کنند**.
5. Bayes factorها را روی یک مقیاس درجه‌بندی‌شده‌ی شواهد **تفسیر کنند** و با بخت‌های پیشین **ترکیب کنند** تا احتمال‌های پسین مدل‌ها به دست آید.

</div>

---

## Motivation & big picture · مقدمه

Last week gave us posteriors *within* a model. Two questions remain.

<div dir="rtl">

هفته‌ی قبل پسین‌ها را *درون* یک مدل به دست آوردیم. دو سؤال باقی مانده است.

</div>

**1. Is the model any good at all?** A posterior can be narrow and confident even when the model is badly wrong: the exponential model will happily give a precise posterior for $\lambda$ for the Week 2 data. The Bayesian answer is to ask the fitted model to **generate new data** and check whether they look like the real data. This is a *posterior predictive check*, the Bayesian counterpart of residual plots and $G^2$.

<div dir="rtl">

**1. آیا مدل اصلاً خوب است؟** یک پسین می‌تواند باریک و مطمئن باشد حتی وقتی مدل به‌شدت غلط است: مدل نمایی با کمال میل برای داده‌های هفته‌ی 2 یک پسین دقیق برای $\lambda$ می‌دهد. جواب بیزی این است که از مدل برازش‌شده بخواهیم **داده‌ی جدید تولید کند** و ببینیم شبیه داده‌ی واقعی است یا نه. این یک *بررسی پیش‌بینی پسین* (posterior predictive check) است؛ همتای بیزی نمودار باقی‌مانده‌ها و $G^2$.

</div>

**2. Which model do the data support more?** In Week 7 we compared models with AIC and BIC, which penalize parameter counts. Bayesian inference has a built-in answer: compute how well each model predicted the data *before* it was fitted, averaging over all parameter values its prior allows. That is the **marginal likelihood**, and the ratio of two marginal likelihoods is the **Bayes factor**. A flexible model spreads its predictions over many possible datasets, so it assigns less probability to any one of them. The Bayes factor thus implements Occam's razor automatically, and it responds to functional-form flexibility, not just to $k$.

<div dir="rtl">

**2. داده‌ها از کدام مدل بیشتر پشتیبانی می‌کنند؟** در هفته‌ی 7 مدل‌ها را با AIC و BIC مقایسه کردیم که تعداد پارامترها را جریمه می‌کنند. استنباط بیزی جوابی داخلی دارد: حساب کنیم هر مدل *پیش از* برازش داده‌ها را چقدر خوب پیش‌بینی کرده بود، با میانگین‌گیری روی همه‌ی مقادیر پارامتری که پیشینش اجازه می‌دهد. این **marginal likelihood** است، و نسبت دو marginal likelihood **Bayes factor** است. یک مدل منعطف پیش‌بینی‌هایش را روی مجموعه‌داده‌های ممکن زیادی پخش می‌کند، پس به هرکدام احتمال کمتری می‌دهد. بنابراین Bayes factor تیغ اوکام را خودکار اجرا می‌کند، و به انعطاف شکل تابعی پاسخ می‌دهد، نه فقط به $k$.

</div>

Bayes factors are also used to test null hypotheses ("is sensitivity zero?"). Unlike $p$-values, they can quantify evidence **for** the null.

<div dir="rtl">

Bayes factorها برای آزمون فرض صفر هم استفاده می‌شوند («آیا حساسیت صفر است؟»). برخلاف مقدار $p$، می‌توانند شواهد **به نفع** فرض صفر را هم کمّی کنند.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Evidence for "no effect".** Replication studies often ask whether an effect is absent. A $p$-value cannot support the null; a Bayes factor can ("the data are 8 times more likely under no effect").
- **Psychology journals and software**: Bayes factors are reported routinely with tools such as JASP and the R package BayesFactor, for t-tests, ANOVAs and correlations as well as for cognitive models.
- **Model checking in every Bayesian analysis**: posterior predictive checks are a standard step before any result is trusted (e.g. in clinical trials analyzed with Bayesian methods and in cognitive modeling papers).
- **Comparing theories with different flexibility**: when two models have the same number of parameters but one can produce many more data patterns, the Bayes factor is one of the few tools that notices.

<div dir="rtl">

- **شاهد برای «بدون اثر».** مطالعه‌های تکرار (replication) اغلب می‌پرسند آیا یک اثر وجود ندارد. $p$-value نمی‌تواند از فرض صفر پشتیبانی کند؛ Bayes factor می‌تواند («داده تحت فرض بدون اثر 8 برابر محتمل‌تر است»).
- **مجله‌ها و نرم‌افزارهای روان‌شناسی:** Bayes factorها با ابزارهایی مثل JASP و بسته‌ی BayesFactor در R به‌طور معمول گزارش می‌شوند؛ هم برای t-test، ANOVA و همبستگی و هم برای مدل‌های شناختی.
- **بررسی مدل در هر تحلیل بیزی:** posterior predictive check گامی استاندارد پیش از اعتماد به هر نتیجه است (مثلاً در کارآزمایی‌های بالینی که به روش بیزی تحلیل می‌شوند و در مقاله‌های مدل‌سازی شناختی).
- **مقایسه‌ی نظریه‌هایی با انعطاف متفاوت:** وقتی دو مدل تعداد پارامتر یکسانی دارند ولی یکی می‌تواند الگوهای داده‌ی خیلی بیشتری بسازد، Bayes factor یکی از معدود ابزارهایی است که این را می‌بیند.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

Two separate questions this week. **(1) Is my model good enough?** Let the fitted model *imagine* new data: take plausible parameter values from the posterior, simulate a new experiment, repeat many times. If the real data look like a typical imagined dataset, the model is adequate; if the real data sit outside the cloud of imagined data, the model is missing something. This is a **posterior predictive check**. **(2) Which of two models do the data support more?** Ask each model, *before fitting*, how probable it found the data we actually got, averaging over all the parameter values its prior allows. That number is the **marginal likelihood**, and the ratio for two models is the **Bayes factor**. A model that bets on everything (very flexible) must spread its bets thinly, so it wins less when the data fall where a simpler model bet. That is Occam's razor, built into probability theory. The catch: the Bayes factor depends on the prior, so you must report how it changes with reasonable priors.

<div dir="rtl">

این هفته دو سؤال جدا داریم. **(1) آیا مدل من به اندازه‌ی کافی خوب است؟** بگذارید مدل برازش‌شده داده‌ی تازه *تصور کند*: مقدارهای معقول پارامتر را از posterior بردارید، یک آزمایش تازه شبیه‌سازی کنید و این کار را بارها تکرار کنید. اگر داده‌ی واقعی شبیه یک داده‌ی تصوری معمولی باشد، مدل کافی است؛ اگر داده‌ی واقعی بیرون از ابر داده‌های تصوری باشد، مدل چیزی را از قلم انداخته است. این یک **posterior predictive check** است. **(2) داده از کدام‌یک از دو مدل بیشتر پشتیبانی می‌کند؟** از هر مدل بپرسید، *پیش از برازش*، داده‌ای را که واقعاً به دست آوردیم چقدر محتمل می‌دانست، با میانگین گرفتن روی همه‌ی مقدارهای پارامتری که prior آن اجازه می‌دهد. این عدد **marginal likelihood** است و نسبت آن برای دو مدل **Bayes factor** است. مدلی که روی همه‌چیز شرط می‌بندد (خیلی منعطف) باید شرط‌هایش را پخش کند، پس وقتی داده جایی می‌افتد که مدل ساده‌تر روی آن شرط بسته بود، کمتر برنده می‌شود. این همان تیغ اوکام است که در نظریه‌ی احتمال تعبیه شده. نکته‌ی مهم: Bayes factor به prior بستگی دارد، پس باید گزارش کنید که با priorهای معقول چطور تغییر می‌کند.

</div>

**Suggested timing (60 min):** posterior predictive checks 15 · marginal likelihood and Bayes factors 20 · computing BFs (grid, BIC, Savage–Dickey) 15 · prior sensitivity and comparison of methods 10.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** بررسی پیش‌بینی پسین 15 · marginal likelihood و Bayes factor 20 · محاسبه‌ی Bayes factor (شبکه، BIC، Savage–Dickey) 15 · حساسیت به پیشین و مقایسه‌ی روش‌ها 10.

</div>

### 1. Posterior predictive checks · 1. بررسی‌های پیش‌بینی پسین

The **posterior predictive distribution** describes new data $\mathbf{y}^{\text{rep}}$ that the fitted model expects:

<div dir="rtl">

**توزیع پیش‌بینی پسین** داده‌ی جدید $\mathbf{y}^{\text{rep}}$ را که مدل برازش‌شده انتظار دارد توصیف می‌کند:

</div>

$$
p(\mathbf{y}^{\text{rep}} \mid \mathbf{y}) = \int p(\mathbf{y}^{\text{rep}} \mid \boldsymbol\theta)\, p(\boldsymbol\theta \mid \mathbf{y})\, d\boldsymbol\theta.
$$

**Simulation recipe:** for $s = 1, \dots, S$, draw $\boldsymbol\theta^{(s)}$ from the posterior and simulate a dataset $\mathbf{y}^{\text{rep}(s)}$ from the model with the real design. This propagates *both* parameter uncertainty and sampling noise.

<div dir="rtl">

**دستور شبیه‌سازی:** برای $s = 1, \dots, S$، $\boldsymbol\theta^{(s)}$ را از پسین بکشید و یک مجموعه‌داده‌ی $\mathbf{y}^{\text{rep}(s)}$ از مدل با طرح آزمایش واقعی شبیه‌سازی کنید. این کار *هم* عدم قطعیت پارامترها و *هم* نویز نمونه‌گیری را منتقل می‌کند.

</div>

**Checks:**
- **Graphical:** plot the observed data on top of the predictive intervals (e.g., the central 95% of $y^{\text{rep}}$ per condition). Systematic departures (observed points repeatedly outside the bands, or on one side of them) show where the model fails.
- **Numerical:** choose a test statistic $T(\mathbf{y})$ that captures a feature you care about (e.g., recall at the longest delays, the steepness of the early drop). The **posterior predictive $p$-value** is $p_B = P\big(T(\mathbf{y}^{\text{rep}}) \ge T(\mathbf{y}) \mid \mathbf{y}\big)$. Values near 0 or 1 indicate that the model cannot reproduce this feature.

<div dir="rtl">

**بررسی‌ها:**
- **نموداری:** داده‌ی مشاهده‌شده را روی بازه‌های پیش‌بینی (مثلاً 95% مرکزی $y^{\text{rep}}$ در هر شرط) رسم کنید. انحراف‌های نظام‌مند (نقاط مشاهده‌شده که مرتب بیرون نوارها یا در یک سمتشان‌اند) نشان می‌دهند مدل کجا شکست می‌خورد.
- **عددی:** یک آماره‌ی آزمون $T(\mathbf{y})$ انتخاب کنید که ویژگی مورد نظرتان را نشان دهد (مثلاً یادآوری در طولانی‌ترین فاصله‌ها، تندی افت اولیه). **مقدار $p$ پیش‌بینی پسین** برابر است با $p_B = P\big(T(\mathbf{y}^{\text{rep}}) \ge T(\mathbf{y}) \mid \mathbf{y}\big)$. مقادیر نزدیک 0 یا 1 نشان می‌دهند مدل نمی‌تواند این ویژگی را بازتولید کند.

</div>

PPCs assess **absolute** adequacy, i.e., whether the model is good enough, not which of two models is better. They are a routine step of every Bayesian analysis (Week 13).

<div dir="rtl">

PPCها کفایت **مطلق** را می‌سنجند، یعنی اینکه مدل به اندازه‌ی کافی خوب است یا نه، نه اینکه کدام از دو مدل بهتر است. گام همیشگی هر تحلیل بیزی‌اند (هفته‌ی 13).

</div>

#### Reading the math · خواندن ریاضی

- $\mathbf{y}^{\text{rep}}$: "replicated" data, an imagined repetition of the experiment.
- $\int p(\mathbf{y}^{\text{rep}} \mid \boldsymbol\theta)\, p(\boldsymbol\theta \mid \mathbf{y})\, d\boldsymbol\theta$: average the model's predictions over all parameter values, each weighted by its posterior plausibility. In practice this integral is replaced by the two-step simulation recipe: draw $\boldsymbol\theta$ from the posterior, then simulate data with it.
- $p_B = P(T(\mathbf{y}^{\text{rep}}) \ge T(\mathbf{y}) \mid \mathbf{y})$: the fraction of imagined datasets whose summary $T$ is at least as large as the real one. If only 1% of imagined datasets show recall as high as observed at 30 days ($p_B = 0.01$), the model cannot produce that feature.

<div dir="rtl">

- $\mathbf{y}^{\text{rep}}$: داده‌ی «تکرارشده»، یک تکرار تصوری از آزمایش.
- $\int p(\mathbf{y}^{\text{rep}} \mid \boldsymbol\theta)\, p(\boldsymbol\theta \mid \mathbf{y})\, d\boldsymbol\theta$: پیش‌بینی‌های مدل را روی همه‌ی مقدارهای پارامتر میانگین بگیر، هرکدام با وزن معقول بودنش در posterior. در عمل این انتگرال با دستور شبیه‌سازی دومرحله‌ای جایگزین می‌شود: $\boldsymbol\theta$ را از posterior بکش و بعد با آن داده شبیه‌سازی کن.
- $p_B = P(T(\mathbf{y}^{\text{rep}}) \ge T(\mathbf{y}) \mid \mathbf{y})$: کسری از داده‌های تصوری که آماره‌ی خلاصه‌ی $T$ آن‌ها دست‌کم به اندازه‌ی داده‌ی واقعی بزرگ است. اگر فقط 1% داده‌های تصوری یادآوری‌ای به بالایی مقدار مشاهده‌شده در 30 روز نشان دهند ($p_B = 0.01$)، مدل نمی‌تواند این ویژگی را تولید کند.

</div>

### 2. The marginal likelihood and the Bayes factor · 2. marginal likelihood و Bayes factor

The **marginal likelihood** (evidence) of model $\mathcal{M}$ is the likelihood averaged over the prior:

<div dir="rtl">

**marginal likelihood** (شواهد) مدل $\mathcal{M}$ درست‌نمایی‌ای است که روی پیشین میانگین‌گیری شده است:

</div>

$$
p(\mathbf{y} \mid \mathcal{M}) = \int p(\mathbf{y} \mid \boldsymbol\theta, \mathcal{M})\, p(\boldsymbol\theta \mid \mathcal{M})\, d\boldsymbol\theta.
$$

It is the probability the model assigned to the observed data *before seeing them*. Bayes' rule at the level of models gives:

<div dir="rtl">

این احتمالی است که مدل *پیش از دیدن* داده‌ی مشاهده‌شده به آن داده بود. قاعده‌ی بیز در سطح مدل‌ها می‌دهد:

</div>

$$
\underbrace{\frac{p(\mathcal{M}_1 \mid \mathbf{y})}{p(\mathcal{M}_2 \mid \mathbf{y})}}_{\text{posterior odds}}
= \underbrace{\frac{p(\mathbf{y} \mid \mathcal{M}_1)}{p(\mathbf{y} \mid \mathcal{M}_2)}}_{\mathrm{BF}_{12}}
\times \underbrace{\frac{p(\mathcal{M}_1)}{p(\mathcal{M}_2)}}_{\text{prior odds}}.
$$

$\mathrm{BF}_{12}$ is the factor by which the data change the odds in favor of $\mathcal{M}_1$ over $\mathcal{M}_2$, and $\mathrm{BF}_{21} = 1/\mathrm{BF}_{12}$.

<div dir="rtl">

$\mathrm{BF}_{12}$ ضریبی است که داده‌ها با آن بخت $\mathcal{M}_1$ نسبت به $\mathcal{M}_2$ را تغییر می‌دهند، و $\mathrm{BF}_{21} = 1/\mathrm{BF}_{12}$.

</div>

**The automatic Occam's razor.** Both models must spread a total probability of 1 over all possible datasets. A simple model concentrates its predictions on a few datasets; a flexible model spreads them thin. If the data fall where the simple model predicted, the simple model gets the higher marginal likelihood, even though the flexible model can also fit them well after its parameters are tuned. Unlike AIC/BIC, this penalty depends on *how* flexible a model is (the prior predictive spread), not merely on $k$.

<div dir="rtl">

**تیغ خودکار اوکام.** هر دو مدل باید احتمال کل 1 را روی همه‌ی مجموعه‌داده‌های ممکن پخش کنند. یک مدل ساده پیش‌بینی‌هایش را روی چند مجموعه‌داده متمرکز می‌کند؛ یک مدل منعطف آن‌ها را نازک پخش می‌کند. اگر داده‌ها همان‌جایی بیفتند که مدل ساده پیش‌بینی کرده بود، مدل ساده marginal likelihood بالاتری می‌گیرد، حتی اگر مدل منعطف هم بعد از تنظیم پارامترهایش بتواند آن‌ها را خوب برازش کند. برخلاف AIC/BIC، این جریمه به *اینکه* مدل چقدر منعطف است (پراکندگی پیش‌بینی پیشین) بستگی دارد، نه فقط به $k$.

</div>

**A common evidence scale** (an adaptation of Jeffreys' classic categories, as used by Lee & Wagenmakers):

<div dir="rtl">

**یک مقیاس رایج شواهد** (برگرفته از دسته‌بندی کلاسیک Jeffreys، آن‌طور که Lee و Wagenmakers به کار می‌برند):

</div>

| $\mathrm{BF}_{12}$ | Evidence for $\mathcal{M}_1$ |
|---|---|
| 1–3 | Anecdotal |
| 3–10 | Moderate |
| 10–30 | Strong |
| 30–100 | Very strong |
| > 100 | Extreme |

<div dir="rtl">

| $\mathrm{BF}_{12}$ | شواهد به نفع $\mathcal{M}_1$ |
|---|---|
| 1–3 | حکایتی (anecdotal) |
| 3–10 | متوسط |
| 10–30 | قوی |
| 30–100 | خیلی قوی |
| > 100 | فوق‌العاده قوی |

</div>

(Values below 1 are read the same way for $\mathcal{M}_2$.) These labels are aids, not thresholds. Report the number.

<div dir="rtl">

(مقادیر کمتر از 1 به همین شکل برای $\mathcal{M}_2$ خوانده می‌شوند.) این برچسب‌ها کمک‌کننده‌اند، نه آستانه. خود عدد را گزارش کنید.

</div>

#### Reading the math · خواندن ریاضی

- $p(\mathbf{y} \mid \mathcal{M}) = \int p(\mathbf{y} \mid \boldsymbol\theta)\,p(\boldsymbol\theta)\,d\boldsymbol\theta$: the likelihood **averaged** over the prior, not maximized. Compare: MLE takes the *best* parameter value; the marginal likelihood takes the *prior-weighted average* over all of them. A model with many bad parameter values in its prior gets a low average.
- **Posterior odds = Bayes factor × prior odds.** Odds are probability ratios: odds of 3 mean 3:1, i.e. probability 0.75. If both models were equally plausible before (prior odds = 1) and $\mathrm{BF}_{12} = 3$, then afterwards $P(\mathcal{M}_1 \mid \mathbf{y}) = 3/(1+3) = 0.75$.
- **Worked example in one line:** with 7 of 10 correct, chance predicted the data with probability 0.117 and the "any accuracy" model with 0.091, so $\mathrm{BF}_{01} = 1.29$: the data hardly change the odds.

<div dir="rtl">

- $p(\mathbf{y} \mid \mathcal{M}) = \int p(\mathbf{y} \mid \boldsymbol\theta)\,p(\boldsymbol\theta)\,d\boldsymbol\theta$: درست‌نمایی که روی prior **میانگین** گرفته شده، نه بیشینه. مقایسه کنید: MLE *بهترین* مقدار پارامتر را برمی‌دارد؛ marginal likelihood *میانگین وزن‌دار با prior* روی همه‌ی مقدارها را. مدلی که prior آن مقدارهای بد زیادی دارد، میانگین پایینی می‌گیرد.
- **بخت پسین = Bayes factor × بخت پیشین.** بخت (odds) نسبت احتمال‌هاست: بخت 3 یعنی 3 به 1، یعنی احتمال 0.75. اگر دو مدل پیش از داده به یک اندازه معقول بودند (بخت پیشین = 1) و $\mathrm{BF}_{12} = 3$ باشد، بعد از داده $P(\mathcal{M}_1 \mid \mathbf{y}) = 3/(1+3) = 0.75$.
- **مثال حل‌شده در یک خط:** با 7 درست از 10، مدل شانس داده را با احتمال 0.117 و مدل «هر دقتی» با احتمال 0.091 پیش‌بینی کرده بودند، پس $\mathrm{BF}_{01} = 1.29$: داده بخت‌ها را تقریباً تغییر نمی‌دهد.

</div>

### 3. Computing Bayes factors · 3. محاسبه‌ی Bayes factor

**(a) Grid integration** (1–2 parameters): $p(\mathbf{y}\mid\mathcal{M}) \approx \sum_g p(\mathbf{y}\mid\boldsymbol\theta_g)\, p(\boldsymbol\theta_g)\, \Delta_g$, where $\Delta_g$ is the cell area. Do it in log space (log-sum-exp), and check that the prior mass inside the grid is ≈ 1.

<div dir="rtl">

**(الف) انتگرال‌گیری شبکه‌ای** (1 تا 2 پارامتر): $p(\mathbf{y}\mid\mathcal{M}) \approx \sum_g p(\mathbf{y}\mid\boldsymbol\theta_g)\, p(\boldsymbol\theta_g)\, \Delta_g$، که $\Delta_g$ مساحت هر خانه است. آن را در فضای لگاریتمی (log-sum-exp) انجام دهید و بررسی کنید که جرم پیشین داخل شبکه ≈ 1 باشد.

</div>

**(b) The BIC approximation.** For large $N$, $\ln p(\mathbf{y}\mid\mathcal{M}) \approx -\tfrac12\mathrm{BIC}$, so

<div dir="rtl">

**(ب) تقریب BIC.** برای $N$ بزرگ، $\ln p(\mathbf{y}\mid\mathcal{M}) \approx -\tfrac12\mathrm{BIC}$، پس

</div>

$$
\mathrm{BF}_{12} \approx \exp\big(-\tfrac12(\mathrm{BIC}_1 - \mathrm{BIC}_2)\big).
$$

It is quick but crude: it ignores the actual prior (it implicitly assumes a "unit-information" prior) and functional-form flexibility.

<div dir="rtl">

سریع ولی خام است: پیشین واقعی را نادیده می‌گیرد (به‌طور ضمنی یک پیشین «unit-information» فرض می‌کند) و انعطاف شکل تابعی را هم.

</div>

**(c) The Savage–Dickey density ratio** (nested models). If $\mathcal{M}_0$ fixes $\phi = \phi_0$ in $\mathcal{M}_1$, and the priors on the remaining parameters match, then

<div dir="rtl">

**(ج) نسبت چگالی Savage–Dickey** (مدل‌های nested). اگر $\mathcal{M}_0$ در $\mathcal{M}_1$ مقدار $\phi = \phi_0$ را ثابت کند و پیشین‌های بقیه‌ی پارامترها یکی باشند، آن‌وقت

</div>

$$
\mathrm{BF}_{01} = \frac{p(\phi = \phi_0 \mid \mathbf{y}, \mathcal{M}_1)}{p(\phi = \phi_0 \mid \mathcal{M}_1)}:
$$

the posterior density at the null value divided by the prior density at the null value, both under the larger model. If the data make $\phi_0$ more plausible than it was a priori, the evidence favors the null. One posterior from $\mathcal{M}_1$ is all we need.

<div dir="rtl">

چگالی پسین در مقدار صفر تقسیم بر چگالی پیشین در مقدار صفر، هر دو تحت مدل بزرگ‌تر. اگر داده‌ها $\phi_0$ را محتمل‌تر از قبل کنند، شواهد به نفع فرض صفر است. فقط یک پسین از $\mathcal{M}_1$ لازم داریم.

</div>

(Further methods, such as bridge sampling and thermodynamic integration, compute marginal likelihoods from MCMC output for complex models. They are beyond this course.)

<div dir="rtl">

(روش‌های دیگر، مثل bridge sampling و thermodynamic integration، marginal likelihood مدل‌های پیچیده را از خروجی MCMC حساب می‌کنند. این‌ها خارج از محدوده‌ی این درس‌اند.)

</div>

#### Reading the math · خواندن ریاضی

**Savage–Dickey** $\mathrm{BF}_{01} = p(\phi_0 \mid \mathbf{y}) / p(\phi_0)$: look at the height of the posterior and of the prior at the null value $\phi_0$ (e.g. $\theta = 0.5$). If the posterior is *higher* there than the prior was, the data made the null value more plausible, so the evidence favors the null. In the worked example the prior (flat) has height 1 at 0.5 and the posterior $\mathrm{Beta}(8,4)$ has height 1.29, so $\mathrm{BF}_{01} = 1.29$. A picture of two curves and one vertical line at $\phi_0$ is all you need to explain this.

<div dir="rtl">

**Savage–Dickey** $\mathrm{BF}_{01} = p(\phi_0 \mid \mathbf{y}) / p(\phi_0)$: به ارتفاع posterior و prior در مقدار صفر $\phi_0$ نگاه کنید (مثلاً $\theta = 0.5$). اگر posterior آنجا *بلندتر* از prior باشد، داده مقدار صفر را معقول‌تر کرده، پس شواهد به نفع فرض صفر است. در مثال حل‌شده prior (صاف) در 0.5 ارتفاع 1 دارد و posterior یعنی $\mathrm{Beta}(8,4)$ ارتفاع 1.29، پس $\mathrm{BF}_{01} = 1.29$. یک تصویر از دو منحنی و یک خط عمودی در $\phi_0$ تمام چیزی است که برای توضیح این لازم دارید.

</div>

### 4. Prior sensitivity: estimation vs. testing · 4. حساسیت به پیشین: برآورد در برابر آزمون

For **estimation**, a reasonable prior matters less and less as data accumulate. For **Bayes factors**, the prior on a tested parameter *never* stops mattering. Making the prior under $\mathcal{M}_1$ wider spreads its predictions more thinly, which lowers $p(\mathbf{y}\mid\mathcal{M}_1)$, so an arbitrarily vague prior makes the BF favor the null no matter what the data are (the Jeffreys–Lindley paradox). Consequences:
- Priors for model comparison must be chosen thoughtfully, ideally reflecting realistic effect sizes.
- Always report a **sensitivity analysis**: the BF over a range of reasonable prior widths.

<div dir="rtl">

برای **برآورد**، یک پیشین معقول با جمع شدن داده کم‌اهمیت‌تر می‌شود. برای **Bayes factor**، پیشین پارامتر آزمون‌شده *هرگز* بی‌اهمیت نمی‌شود. پهن‌تر کردن پیشین تحت $\mathcal{M}_1$ پیش‌بینی‌هایش را نازک‌تر پخش می‌کند و $p(\mathbf{y}\mid\mathcal{M}_1)$ را کم می‌کند، پس یک پیشین دلخواه مبهم Bayes factor را، هر داده‌ای که باشد، به نفع فرض صفر می‌کند (پارادوکس Jeffreys–Lindley). پیامدها:
- پیشین‌ها برای مقایسه‌ی مدل باید با دقت انتخاب شوند، ترجیحاً منعکس‌کننده‌ی اندازه‌ی اثرهای واقع‌بینانه.
- همیشه یک **تحلیل حساسیت** گزارش کنید: Bayes factor روی دامنه‌ای از پهنای معقول پیشین.

</div>

### 5. Comparison of model-evaluation methods · 5. مقایسه‌ی روش‌های ارزیابی مدل

| Method | Question | Penalizes | Prior needed? | Week |
|---|---|---|---|---|
| $G^2$, residuals, PPC | Is the model adequate? | — | PPC: yes | 4, 10 |
| LRT | Does the extra parameter improve fit beyond chance? (nested only) | $\Delta k$ via $\chi^2$ | No | 7 |
| AIC / CV | Which model predicts new data best? | Estimated over-fitting | No | 6–7 |
| BIC | Approximately: which model has the higher evidence? | $k \ln N$ | Implicit | 7 |
| Bayes factor | How much do the data change the odds between models? | Prior predictive spread (true flexibility) | **Yes, and the result depends on it** | 10 |

<div dir="rtl">

| روش | سؤال | چه چیزی را جریمه می‌کند | پیشین لازم است؟ | هفته |
|---|---|---|---|---|
| $G^2$، باقی‌مانده‌ها، PPC | آیا مدل کافی است؟ | — | PPC: بله | 4، 10 |
| LRT | آیا پارامتر اضافه برازش را بیش از شانس بهتر می‌کند؟ (فقط nested) | $\Delta k$ از راه $\chi^2$ | نه | 7 |
| AIC / CV | کدام مدل داده‌ی جدید را بهتر پیش‌بینی می‌کند؟ | overfitting تخمینی | نه | 6–7 |
| BIC | به‌طور تقریبی: کدام مدل شواهد بیشتری دارد؟ | $k \ln N$ | ضمنی | 7 |
| Bayes factor | داده‌ها بخت بین مدل‌ها را چقدر تغییر می‌دهند؟ | پراکندگی پیش‌بینی پیشین (انعطاف واقعی) | **بله، و نتیجه به آن بستگی دارد** | 10 |

</div>

> **Advanced: Bayes factors vs. predictive criteria.** The marginal likelihood can be written as a product of sequential predictions, $p(\mathbf{y}) = p(y_1)\,p(y_2\mid y_1)\cdots p(y_N\mid y_{1:N-1})$. It therefore scores how well the model predicts each data point from the earlier ones, *starting from the prior*. LOO-CV scores predictions from (almost) all the other data. This is why BFs depend on the prior and LOO hardly does, and why they can disagree on the same data.

<div dir="rtl">

> **پیشرفته: Bayes factor در برابر معیارهای پیش‌بینی.** marginal likelihood را می‌شود به شکل حاصل‌ضرب پیش‌بینی‌های ترتیبی نوشت، $p(\mathbf{y}) = p(y_1)\,p(y_2\mid y_1)\cdots p(y_N\mid y_{1:N-1})$. پس امتیاز می‌دهد که مدل هر نقطه‌ی داده را از روی نقاط قبلی، *با شروع از پیشین*، چقدر خوب پیش‌بینی می‌کند. LOO-CV پیش‌بینی‌ها را از روی (تقریباً) همه‌ی داده‌های دیگر امتیاز می‌دهد. به همین دلیل Bayes factor به پیشین وابسته است و LOO تقریباً نه، و به همین دلیل ممکن است روی داده‌ی یکسان با هم مخالف باشند.

</div>

#### For an engineer · برای یک مهندس

- **Posterior odds = BF × prior odds** is the **MAP (Bayes) detector** between two hypotheses, where the Bayes factor plays the role of the likelihood ratio.
- The difference from the **GLRT** (Week 4 and 7): with unknown parameters, the GLRT *maximizes* the likelihood over them; the Bayes factor *integrates* (averages) over them with a prior. Maximizing favors flexible hypotheses; averaging penalizes them automatically.
- The **Jeffreys–Lindley paradox** has an engineering flavor: if you let the alternative hypothesis allow absurdly large signal amplitudes (a very wide prior), almost any observation is better explained by "noise only".
- **Posterior predictive checks** are like validating a channel model by simulating received signals from the fitted model and comparing their statistics (histograms, autocorrelations, eye diagrams) with measured ones.

<div dir="rtl">

- **بخت پسین = BF × بخت پیشین** همان **آشکارساز MAP (بیز)** بین دو فرضیه است که در آن Bayes factor نقش نسبت درست‌نمایی را دارد.
- تفاوت با **GLRT** (هفته‌های 4 و 7): با پارامترهای مجهول، GLRT درست‌نمایی را روی آن‌ها *بیشینه* می‌کند؛ Bayes factor با یک prior روی آن‌ها *انتگرال* (میانگین) می‌گیرد. بیشینه کردن به فرضیه‌های منعطف امتیاز می‌دهد؛ میانگین گرفتن آن‌ها را خودکار جریمه می‌کند.
- **پارادوکس Jeffreys–Lindley** رنگ‌وبوی مهندسی دارد: اگر بگذارید فرضیه‌ی جایگزین دامنه‌های سیگنال به‌طور نامعقول بزرگ را مجاز بداند (prior خیلی پهن)، تقریباً هر مشاهده‌ای با «فقط نویز» بهتر توضیح داده می‌شود.
- **posterior predictive check** شبیه اعتبارسنجی یک مدل کانال است: سیگنال‌های دریافتی را از مدل برازش‌شده شبیه‌سازی کنید و آماره‌هایشان (هیستوگرام، خودهمبستگی، eye diagram) را با اندازه‌گیری‌ها مقایسه کنید.

</div>

#### For the instructor · برای مدرس

- **Explain Occam's razor with a betting story.** Two forecasters each have 100 chips to place on possible outcomes. One spreads them over everything; the other puts most chips on a narrow range. If the outcome lands in that narrow range, the focused forecaster wins more. The marginal likelihood is the payout.
- **Show prior sensitivity live.** In the lab code, change the width of the prior under $\mathcal{M}_1$ and watch the BF move. This is more convincing than any warning.
- **Keep the two questions apart.** Write "Is the model good enough? → PPC" and "Which model is better? → BF / CV / AIC" on the board. Students often use a BF to claim a model is *good*; it only says it is *better than the other*.
- **Typical questions.**
  - *"BF or $p$-value?"* They answer different questions. The BF compares two specific hypotheses and can support the null; the $p$-value only measures surprise under the null.
  - *"BF = 2.5, is that significant?"* There is no threshold; it is anecdotal evidence. Report the number.
  - *"Why do BF and AIC disagree?"* They aim at different targets (evidence vs. prediction) and the BF depends on the prior.

<div dir="rtl">

- **تیغ اوکام را با داستان شرط‌بندی توضیح دهید.** دو پیش‌بینی‌کننده هرکدام 100 ژتون دارند که باید روی نتیجه‌های ممکن بگذارند. یکی ژتون‌ها را روی همه‌چیز پخش می‌کند؛ دیگری بیشتر ژتون‌ها را روی یک محدوده‌ی باریک می‌گذارد. اگر نتیجه در آن محدوده‌ی باریک بیفتد، پیش‌بینی‌کننده‌ی متمرکز بیشتر می‌برد. marginal likelihood همان مبلغ برد است.
- **حساسیت به prior را زنده نشان دهید.** در کد lab پهنای prior تحت $\mathcal{M}_1$ را تغییر دهید و ببینید BF چطور جابه‌جا می‌شود. این از هر هشداری قانع‌کننده‌تر است.
- **دو سؤال را از هم جدا نگه دارید.** روی تخته بنویسید «آیا مدل کافی است؟ ← PPC» و «کدام مدل بهتر است؟ ← BF / CV / AIC». دانشجوها اغلب از BF برای ادعای *خوب* بودن یک مدل استفاده می‌کنند؛ BF فقط می‌گوید *از دیگری بهتر* است.
- **سؤال‌های رایج.**
  - *«BF یا $p$-value؟»* به سؤال‌های متفاوتی جواب می‌دهند. BF دو فرضیه‌ی مشخص را مقایسه می‌کند و می‌تواند از فرض صفر پشتیبانی کند؛ $p$-value فقط میزان غافلگیری تحت فرض صفر را می‌سنجد.
  - *«BF = 2.5 معنادار است؟»* آستانه‌ای وجود ندارد؛ شواهد حکایتی (anecdotal) است. عدد را گزارش کنید.
  - *«چرا BF و AIC با هم توافق ندارند؟»* هدف‌های متفاوتی دارند (شواهد در برابر پیش‌بینی) و BF به prior بستگی دارد.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: is recall at chance? A Bayes factor by hand · بخش 1: آیا یادآوری در حد شانس است؟ یک Bayes factor با دست

A participant chooses between two alternatives on $n = 10$ trials and is correct on $y = 7$. Is performance at chance?

<div dir="rtl">

یک شرکت‌کننده در $n = 10$ trial بین دو گزینه انتخاب می‌کند و در $y = 7$ trial درست جواب می‌دهد. آیا عملکرد در حد شانس است؟

</div>

- $\mathcal{M}_0$: $\theta = 0.5$ (no free parameters).
- $\mathcal{M}_1$: $\theta \sim \mathrm{Beta}(1, 1)$ (any accuracy equally plausible a priori).

<div dir="rtl">

- $\mathcal{M}_0$: $\theta = 0.5$ (بدون پارامتر آزاد).
- $\mathcal{M}_1$: $\theta \sim \mathrm{Beta}(1, 1)$ (هر دقتی از پیش به یک اندازه محتمل است).

</div>

**Step 1.** $p(y\mid\mathcal{M}_0) = \binom{10}{7} 0.5^{10} = 120/1024 = 0.1172$.

<div dir="rtl">

**قدم 1.** $p(y\mid\mathcal{M}_0) = \binom{10}{7} 0.5^{10} = 120/1024 = 0.1172$.

</div>

**Step 2.** Under a uniform prior, every count $0, \dots, n$ is equally likely a priori, so $p(y\mid\mathcal{M}_1) = \int_0^1 \binom{10}{7}\theta^7(1-\theta)^3\, d\theta = \frac{1}{n+1} = \frac{1}{11} = 0.0909$.

<div dir="rtl">

**قدم 2.** تحت پیشین یکنواخت، هر شمارش $0, \dots, n$ از پیش به یک اندازه محتمل است، پس $p(y\mid\mathcal{M}_1) = \int_0^1 \binom{10}{7}\theta^7(1-\theta)^3\, d\theta = \frac{1}{n+1} = \frac{1}{11} = 0.0909$.

</div>

**Step 3.** $\mathrm{BF}_{01} = 0.1172 / 0.0909 = 1.29$. The data slightly *favor chance*, which is anecdotal evidence either way.

<div dir="rtl">

**قدم 3.** $\mathrm{BF}_{01} = 0.1172 / 0.0909 = 1.29$. داده‌ها کمی *به نفع شانس*‌اند؛ شواهدی حکایتی در هر دو جهت.

</div>

**Step 4 (Savage–Dickey check).** The posterior under $\mathcal{M}_1$ is $\mathrm{Beta}(8, 4)$, whose density at 0.5 is 1.289. The prior density at 0.5 is 1. The ratio is 1.29, identical to Step 3.

<div dir="rtl">

**قدم 4 (بررسی Savage–Dickey).** پسین تحت $\mathcal{M}_1$ برابر $\mathrm{Beta}(8, 4)$ است که چگالی‌اش در 0.5 برابر 1.289 است. چگالی پیشین در 0.5 برابر 1 است. نسبت 1.29 است، دقیقاً همان قدم 3.

</div>

**More data:**

<div dir="rtl">

**داده‌ی بیشتر:**

</div>

| Data | $p$ (two-sided binomial test) | $\mathrm{BF}_{01}$ | Reading |
|---|---|---|---|
| 7/10 | 0.34 | 1.29 | Anecdotal, either way |
| 60/100 | ≈ 0.06 | 1.10 | Still anecdotal: the data barely distinguish chance from "some accuracy" |
| 70/100 | < 0.001 | 0.0023 ($\mathrm{BF}_{10} \approx 430$) | Extreme evidence against chance |

<div dir="rtl">

| داده | $p$ (آزمون دوجمله‌ای دوطرفه) | $\mathrm{BF}_{01}$ | خوانش |
|---|---|---|---|
| 7/10 | 0.34 | 1.29 | حکایتی، در هر دو جهت |
| 60/100 | ≈ 0.06 | 1.10 | هنوز حکایتی: داده‌ها به‌سختی شانس را از «کمی دقت» جدا می‌کنند |
| 70/100 | < 0.001 | 0.0023 ($\mathrm{BF}_{10} \approx 430$) | شواهد فوق‌العاده قوی علیه شانس |

</div>

**Interpretation.** With 60/100, a $p$-value near .05 tempts researchers to claim an effect, yet the Bayes factor says the data are about equally likely under both hypotheses. The reason: the alternative with a uniform prior "predicted" that accuracy could be anywhere from 0 to 1. An observed accuracy of 0.6 is only modestly better predicted by it than by exactly 0.5. A narrower, more realistic prior under $\mathcal{M}_1$ (e.g., accuracies between 0.5 and 0.8) would give a different BF, which is why prior sensitivity must be reported.

<div dir="rtl">

**تفسیر.** با 60/100، مقدار $p$ نزدیک .05 پژوهشگران را وسوسه می‌کند ادعای اثر کنند، ولی Bayes factor می‌گوید داده‌ها تحت هر دو فرضیه تقریباً به یک اندازه محتمل‌اند. دلیل: فرضیه‌ی جایگزین با پیشین یکنواخت «پیش‌بینی کرده بود» که دقت می‌تواند هر جایی بین 0 و 1 باشد. دقت مشاهده‌شده‌ی 0.6 فقط کمی بهتر با آن پیش‌بینی می‌شود تا با دقیقاً 0.5. یک پیشین باریک‌تر و واقع‌بینانه‌تر تحت $\mathcal{M}_1$ (مثلاً دقت‌های بین 0.5 و 0.8) Bayes factor متفاوتی می‌داد؛ به همین دلیل حساسیت به پیشین باید گزارش شود.

</div>

### Part 2: posterior model probabilities · بخش 2: احتمال‌های پسین مدل‌ها

For 7/10 with prior odds of 1: posterior odds $= 1.29$, so $P(\mathcal{M}_0 \mid y) = 1.29 / 2.29 = 0.56$. If a reviewer believes a priori that chance performance is 4 times less likely than above-chance performance (prior odds 1:4), then posterior odds $= 1.29 \times 0.25 = 0.32$, so $P(\mathcal{M}_0 \mid y) = 0.24$. The BF is the same for everyone; the posterior model probabilities depend on the prior odds.

<div dir="rtl">

برای 7/10 با بخت پیشین 1: بخت پسین $= 1.29$، پس $P(\mathcal{M}_0 \mid y) = 1.29 / 2.29 = 0.56$. اگر یک داور از پیش باور داشته باشد که عملکرد در حد شانس 4 برابر کمتر از عملکرد بالاتر از شانس محتمل است (بخت پیشین 1:4)، آن‌وقت بخت پسین $= 1.29 \times 0.25 = 0.32$، پس $P(\mathcal{M}_0 \mid y) = 0.24$. Bayes factor برای همه یکی است؛ احتمال‌های پسین مدل‌ها به بخت‌های پیشین بستگی دارند.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Run graphical and numerical posterior predictive checks for the exponential and power forgetting models.
2. Compute marginal likelihoods and the Bayes factor for power vs. exponential by grid integration; compare with BIC.
3. Test $d' = 0$ for a weak-evidence SDT participant with the Savage–Dickey ratio, and verify it by direct computation.
4. Map the sensitivity of the Bayes factor to the prior, and contrast it with the posterior estimate.

<div dir="rtl">

1. اجرای بررسی‌های پیش‌بینی پسین نموداری و عددی برای مدل‌های فراموشی نمایی و توانی.
2. محاسبه‌ی درست‌نمایی‌های حاشیه‌ای و Bayes factor توانی در برابر نمایی با انتگرال‌گیری شبکه‌ای؛ مقایسه با BIC.
3. آزمون $d' = 0$ برای یک شرکت‌کننده‌ی SDT با شواهد ضعیف با نسبت Savage–Dickey، و وارسی آن با محاسبه‌ی مستقیم.
4. ترسیم حساسیت Bayes factor به پیشین و مقایسه‌ی آن با برآورد پسین.

</div>

**Timing:** Part A 35 min · Part B 25 min · Part C 30 min · Part D 20 min · Part E 10 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 35 دقیقه · بخش B 25 دقیقه · بخش C 30 دقیقه · بخش D 20 دقیقه · بخش E 10 دقیقه.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week10.py`](code/week10.py), cell 1 · سلول 1

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
exp: posterior mean A = 0.655, rate = 0.049
pow: posterior mean A = 0.867, rate = 0.417
```

### Part A: posterior predictive checks (35 min) · بخش A: بررسی‌های پیش‌بینی پسین (35 دقیقه)

> **Code · کد:** [`code/week10.py`](code/week10.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
exp: T(observed) = 0.267, mean T(rep) = 0.240, posterior predictive p = 0.302
pow: T(observed) = 0.267, mean T(rep) = 0.243, posterior predictive p = 0.320
```

**Interpret:** look at the plots first. For the exponential model, the observed recall at the shortest delay (42/50) lies *above* the 95% band and recall at 7 days (13/50) lies *below* it. The exponential cannot drop steeply early and then level off. The power model's band contains every observed point.

<div dir="rtl">

**تفسیر:** اول به نمودارها نگاه کنید. برای مدل نمایی، یادآوری مشاهده‌شده در کوتاه‌ترین فاصله (42/50) *بالای* نوار 95% و یادآوری در 7 روز (13/50) *پایین* آن است. مدل نمایی نمی‌تواند اول تند افت کند و بعد ثابت شود. نوار مدل توانی همه‌ی نقاط مشاهده‌شده را در بر دارد.

</div>

Yet the numerical check with `T` = mean recall at the three longest delays gives unremarkable $p_B$ values for **both** models (about 0.3). The exponential's misfit is in the *shape* (early vs. middle delays), which this statistic does not look at. **A PPC can only detect the failures its test statistic is sensitive to.** Choose statistics that target the features that distinguish the theories; in Exercise 2 a "first drop" statistic exposes the exponential model ($p_B \approx 0.02$).

<div dir="rtl">

با این حال بررسی عددی با `T` = میانگین یادآوری در سه فاصله‌ی طولانی‌تر برای **هر دو** مدل مقادیر $p_B$ معمولی (حدود 0.3) می‌دهد. عدم برازش مدل نمایی در *شکل* است (فاصله‌های اولیه در برابر میانی)، که این آماره به آن نگاه نمی‌کند. **یک PPC فقط شکست‌هایی را تشخیص می‌دهد که آماره‌ی آزمونش به آن‌ها حساس است.** آماره‌هایی انتخاب کنید که ویژگی‌های متمایزکننده‌ی نظریه‌ها را هدف بگیرند؛ در تمرین 2 یک آماره‌ی «افت اول» مدل نمایی را لو می‌دهد ($p_B \approx 0.02$).

</div>

### Part B: Bayes factor by grid integration (25 min) · بخش B: Bayes factor با انتگرال‌گیری شبکه‌ای (25 دقیقه)

> **Code · کد:** [`code/week10.py`](code/week10.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
exp: log p(y|M) = -34.938   (prior mass inside grid = 0.9996)
pow: log p(y|M) = -22.872   (prior mass inside grid = 0.9991)

BF(pow vs exp) = exp(12.07) = 1.74e+05
BIC approximation: BF(pow vs exp) = exp(9.98) = 2.16e+04
```

**Interpret:** $\mathrm{BF} \approx 1.7 \times 10^5$ is extreme evidence for the power model over the exponential. BIC gives the same verdict but a different number ($2 \times 10^4$). Why do the grid BF and the BIC approximation differ? (Hint: which prior does each use, and are the two models equally flexible under our priors?)

<div dir="rtl">

**تفسیر:** $\mathrm{BF} \approx 1.7 \times 10^5$ شواهد فوق‌العاده قوی به نفع مدل توانی در برابر نمایی است. BIC همان حکم را می‌دهد ولی با عدد دیگری ($2 \times 10^4$). چرا Bayes factor شبکه‌ای و تقریب BIC با هم فرق دارند؟ (راهنمایی: هرکدام از کدام پیشین استفاده می‌کند، و آیا دو مدل تحت پیشین‌های ما به یک اندازه منعطف‌اند؟)

</div>

### Part C: Savage–Dickey: is this participant's sensitivity zero? (30 min) · بخش C: Savage–Dickey: آیا حساسیت این شرکت‌کننده صفر است؟ (30 دقیقه)

A participant in a hard detection task: 12 hits out of 20 signal trials, 8 false alarms out of 20 noise trials. $\mathcal{M}_1$: $d' \sim \mathcal{N}(0, 1)$, $c \sim \mathcal{N}(0, 1)$. $\mathcal{M}_0$: $d' = 0$, $c \sim \mathcal{N}(0, 1)$.

<div dir="rtl">

یک شرکت‌کننده در یک تکلیف تشخیص سخت: 12 hit از 20 trial علامت، 8 false alarm از 20 trial نویز. $\mathcal{M}_1$: $d' \sim \mathcal{N}(0, 1)$، $c \sim \mathcal{N}(0, 1)$. $\mathcal{M}_0$: $d' = 0$، $c \sim \mathcal{N}(0, 1)$.

</div>

> **Code · کد:** [`code/week10.py`](code/week10.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
BF01 Savage-Dickey = 1.328;  BF01 direct = 1.328;  posterior mean d' = 0.444
MLE d' = 0.507
```

The two computations agree, which is a useful check that both are implemented correctly.

<div dir="rtl">

دو محاسبه با هم توافق دارند؛ بررسی مفیدی برای اینکه هر دو درست پیاده‌سازی شده‌اند.

</div>

### Part D: prior sensitivity (20 min) · بخش D: حساسیت به پیشین (20 دقیقه)

> **Code · کد:** [`code/week10.py`](code/week10.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
 prior SD of d'   BF01  BF10  posterior mean d'
           0.25  0.938 1.066              0.144
           0.50  0.972 1.028              0.313
           1.00  1.328 0.753              0.444
           2.00  2.314 0.432              0.496
           5.00  5.541 0.180              0.513
          10.00 11.011 0.091              0.515
```

**What to notice:** as the prior on $d'$ widens, the posterior mean of $d'$ quickly stabilizes, but $\mathrm{BF}_{01}$ keeps growing in favor of the null. A very wide prior "predicts" huge sensitivities that did not occur, so the alternative is penalized. **For estimation the prior washes out; for testing it does not.**

<div dir="rtl">

**به این دقت کنید:** با پهن‌تر شدن پیشین $d'$، میانگین پسین $d'$ سریع ثابت می‌شود، ولی $\mathrm{BF}_{01}$ مدام به نفع فرض صفر بزرگ‌تر می‌شود. یک پیشین خیلی پهن حساسیت‌های بزرگی را «پیش‌بینی می‌کند» که اتفاق نیفتاده‌اند، پس فرضیه‌ی جایگزین جریمه می‌شود. **برای برآورد، پیشین کم‌رنگ می‌شود؛ برای آزمون، نه.**

</div>

### Part E: interpret (10 min) · بخش E: تفسیر (10 دقیقه)

Write 4–5 sentences: does this participant detect the signal? Report the BF with your chosen prior and justify the prior, mention the sensitivity analysis, and state what additional data would make the answer clearer.

<div dir="rtl">

4 تا 5 جمله بنویسید: آیا این شرکت‌کننده علامت را تشخیص می‌دهد؟ Bayes factor را با پیشین انتخابی‌تان گزارش کنید و پیشین را توجیه کنید، به تحلیل حساسیت اشاره کنید، و بگویید چه داده‌ی اضافه‌ای جواب را روشن‌تر می‌کرد.

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Verify by numerical integration (`scipy.integrate.quad`) that $\int_0^1 \binom{10}{7}\theta^7(1-\theta)^3 d\theta = 1/11$.

<div dir="rtl">

**تمرین 1 ★.** با انتگرال‌گیری عددی (`scipy.integrate.quad`) بررسی کنید که $\int_0^1 \binom{10}{7}\theta^7(1-\theta)^3 d\theta = 1/11$.

</div>

**Exercise 2 ★.** In Part A, use a different test statistic: the drop in recall from the first to the second interval. Which model, if any, fails this check? (Expected: the exponential, $p_B \approx 0.02$; the power model passes.)

<div dir="rtl">

**تمرین 2 ★.** در بخش A از یک آماره‌ی آزمون دیگر استفاده کنید: افت یادآوری از اولین به دومین فاصله. کدام مدل (اگر هست) در این بررسی شکست می‌خورد؟ (انتظار: مدل نمایی، $p_B \approx 0.02$؛ مدل توانی قبول می‌شود.)

</div>

**Exercise 3 ★★ (prior sensitivity of the forgetting BF).** Repeat Part B with the rate priors widened (scale × 3) and narrowed (scale ÷ 3). Does the conclusion "power ≫ exponential" survive? Why is it so robust here, unlike in Part D?

<div dir="rtl">

**تمرین 3 ★★ (حساسیت Bayes factor فراموشی به پیشین).** بخش B را با پیشین‌های نرخ پهن‌تر (مقیاس × 3) و باریک‌تر (مقیاس ÷ 3) تکرار کنید. آیا نتیجه‌ی «توانی ≫ نمایی» باقی می‌ماند؟ چرا اینجا، برخلاف بخش D، این‌قدر پایدار است؟

</div>

**Exercise 4 ★★ (an informed alternative).** In Part C, replace the prior on $d'$ by a half-normal $d' \sim \mathcal{N}^+(0, 1)$ (only positive values; remember to renormalize). Compute the Savage–Dickey BF. Why does a directional prior change the result?

<div dir="rtl">

**تمرین 4 ★★ (یک جایگزین آگاهانه).** در بخش C پیشین $d'$ را با یک نیم‌نرمال $d' \sim \mathcal{N}^+(0, 1)$ (فقط مقادیر مثبت؛ نرمال‌سازی دوباره را فراموش نکنید) جایگزین کنید. Bayes factor Savage–Dickey را حساب کنید. چرا یک پیشین جهت‌دار نتیجه را تغییر می‌دهد؟

</div>

**Exercise 5 ★★★ (Advanced: BF for the repetition study).** For the Week 8 case study ($\mathcal{M}_0$ vs. $\mathcal{M}_1$), choose priors for $\delta_0$, $\delta_1$ and $\kappa$, compute $\mathrm{BF}_{10}$ with the Savage–Dickey ratio at $\delta_1 = 0$ using a 3-D grid (keep it coarse), and compare it with the BIC approximation.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: Bayes factor برای مطالعه‌ی تکرار).** برای مطالعه‌ی موردی هفته‌ی 8 ($\mathcal{M}_0$ در برابر $\mathcal{M}_1$)، پیشین‌هایی برای $\delta_0$، $\delta_1$ و $\kappa$ انتخاب کنید، $\mathrm{BF}_{10}$ را با نسبت Savage–Dickey در $\delta_1 = 0$ با یک شبکه‌ی سه‌بعدی (درشت نگهش دارید) حساب کنید و با تقریب BIC مقایسه کنید.

</div>

### Lab check-off · lab check-off

Show: (1) the two PPC plots with $p_B$ values, (2) the grid BF for power vs. exponential and its BIC approximation, and (3) the prior-sensitivity table from Part D with one sentence of interpretation.

<div dir="rtl">

نشان دهید: (1) دو نمودار PPC با مقادیر $p_B$، (2) Bayes factor شبکه‌ای توانی در برابر نمایی و تقریب BIC آن، و (3) جدول حساسیت به پیشین از بخش D با یک جمله تفسیر.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Do LLMs have a "theory of mind"?** Some studies report that LLMs pass false-belief tasks, classic tests of whether one understands that others can hold false beliefs. Others show that small changes to the stories make performance collapse [verify: Kosinski, 2023/2024; Ullman, 2023]. Many such tests have two answer options, so chance is 50%, and the number of items is small. A Bayes factor answers the right first question: *do the data support above-chance performance at all, compared with chance?*

<div dir="rtl">

**آیا LLMها «نظریه‌ی ذهن» (theory of mind) دارند؟** بعضی مطالعه‌ها گزارش می‌دهند که LLMها تکلیف‌های باور نادرست (false belief) را با موفقیت انجام می‌دهند، یعنی آزمون‌های کلاسیکی که می‌سنجند آیا کسی می‌فهمد دیگران می‌توانند باورهای نادرست داشته باشند. بعضی دیگر نشان می‌دهند که تغییرهای کوچک در داستان‌ها عملکرد را فرو می‌ریزد [بررسی شود: Kosinski, 2023/2024; Ullman, 2023]. بسیاری از این آزمون‌ها دو گزینه‌ی جواب دارند، پس سطح شانس 50% است، و تعداد آیتم‌ها کم است. Bayes factor به اولین سؤال درست جواب می‌دهد: *آیا داده اصلاً از عملکرد بالاتر از شانس، در مقایسه با شانس، پشتیبانی می‌کند؟*

</div>

> **Code · کد:** [`code/week10.py`](code/week10.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
26/40 correct (65%): BF10 = 1.16
130/200 correct (65%): BF10 = 785.26
```

The same 65% is no evidence at all with 40 items, and overwhelming evidence with 200 items. Above-chance performance is also only the first step: the posterior predictive check of this week asks *how* the model succeeds and fails. For example, does it fail on exactly the altered stories, where a human would not?

<div dir="rtl">

همان 65% با 40 آیتم اصلاً شاهدی نیست، و با 200 آیتم شاهدی قاطع است. عملکرد بالاتر از شانس هم فقط قدم اول است: بررسی پیش‌بینی پسین این هفته می‌پرسد مدل *چطور* موفق می‌شود و شکست می‌خورد. مثلاً آیا دقیقاً روی داستان‌های تغییریافته شکست می‌خورد، جایی که یک انسان شکست نمی‌خورد؟

</div>

**Try it (no API needed).**
- ★ Repeat with a prior concentrated on above-chance values, e.g. Beta(5, 2) restricted to $\theta > 0.5$ (renormalize the density). How does $\mathrm{BF}_{10}$ for 26/40 change?
- ★★ Simulate a "shortcut" model that answers correctly on 90% of standard stories and 30% of altered stories (half of each). Its overall accuracy is 60%. Design a posterior predictive check that reveals the shortcut.
- ★★ Discussion: is "above chance on false-belief tasks" a claim at Marr's computational or algorithmic level?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ با یک پیشین متمرکز روی مقادیر بالاتر از شانس تکرار کنید، مثلاً Beta(5, 2) محدودشده به $\theta > 0.5$ (چگالی را دوباره نرمال کنید). $\mathrm{BF}_{10}$ برای 26/40 چطور تغییر می‌کند؟
- ★★ یک مدل «میان‌بُر» (shortcut) شبیه‌سازی کنید که 90% داستان‌های استاندارد و 30% داستان‌های تغییریافته را درست جواب می‌دهد (نیمی از هرکدام). دقت کلی‌اش 60% است. یک بررسی پیش‌بینی پسین طراحی کنید که میان‌بُر را آشکار کند.
- ★★ بحث: «بالاتر از شانس در تکلیف‌های باور نادرست» ادعایی در سطح محاسباتی Marr است یا الگوریتمی؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **"A narrow posterior means the model is right."** Precision is not adequacy. Always run a PPC.
2. **Using the posterior predictive check to choose between models.** PPCs check adequacy. Use BFs, CV or information criteria to compare.
3. **"The Bayes factor is the posterior probability of the model."** It is the *change* in odds. Posterior probabilities also need prior odds.
4. **Using very vague priors in Bayes-factor tests.** They bias the BF toward the null without limit (Part D). Use realistic priors and report the sensitivity.
5. **Savage–Dickey with mismatched priors.** The nuisance-parameter priors must be the same in both models, and the prior density must be evaluated *at the null value* in the larger model.
6. **Computing marginal likelihoods on a grid that cuts off prior mass.** Check that the prior mass inside the grid is close to 1.
7. **Treating "BF = 2.9" vs. "BF = 3.1" as qualitatively different.** The evidence scale is continuous; labels are aids, not decision thresholds.

<div dir="rtl">

1. **«پسین باریک یعنی مدل درست است.»** دقت همان کفایت نیست. همیشه یک PPC اجرا کنید.
2. **استفاده از بررسی پیش‌بینی پسین برای انتخاب بین مدل‌ها.** PPCها کفایت را بررسی می‌کنند. برای مقایسه از Bayes factor، CV یا معیارهای اطلاعاتی استفاده کنید.
3. **«Bayes factor احتمال پسین مدل است.»** Bayes factor *تغییر* بخت است. احتمال‌های پسین به بخت‌های پیشین هم نیاز دارند.
4. **استفاده از پیشین‌های خیلی مبهم در آزمون‌های Bayes factor.** بی‌حد و مرز Bayes factor را به سمت فرض صفر سوگیر می‌کنند (بخش D). از پیشین‌های واقع‌بینانه استفاده کنید و حساسیت را گزارش کنید.
5. **Savage–Dickey با پیشین‌های ناهمخوان.** پیشین‌های پارامترهای مزاحم (nuisance) باید در هر دو مدل یکی باشند، و چگالی پیشین باید *در مقدار صفر* تحت مدل بزرگ‌تر ارزیابی شود.
6. **محاسبه‌ی marginal likelihood روی شبکه‌ای که جرم پیشین را می‌بُرد.** بررسی کنید که جرم پیشین داخل شبکه نزدیک 1 باشد.
7. **«BF = 2.9» و «BF = 3.1» را کیفی متفاوت دانستن.** مقیاس شواهد پیوسته است؛ برچسب‌ها کمک‌کننده‌اند، نه آستانه‌ی تصمیم.

</div>

---

## Check your understanding · خودآزمایی

**1.** How is a posterior predictive distribution simulated, and what does it combine?
<details><summary>Answer</summary>
Draw parameters from the posterior, then simulate data from the model with those parameters (and the real design). It combines uncertainty about the parameters with the sampling noise of new data.
</details>

<div dir="rtl">

**1.** توزیع پیش‌بینی پسین چگونه شبیه‌سازی می‌شود و چه چیزهایی را ترکیب می‌کند؟
<details><summary>پاسخ</summary>
پارامترها را از پسین بکشید و بعد با آن پارامترها (و طرح آزمایش واقعی) از مدل داده شبیه‌سازی کنید. عدم قطعیت درباره‌ی پارامترها را با نویز نمونه‌گیری داده‌ی جدید ترکیب می‌کند.
</details>

</div>

**2.** Define the marginal likelihood in words.
<details><summary>Answer</summary>
The probability (density) of the observed data under the model, averaged over all parameter values weighted by the prior: how well the model predicted these data before it was fitted.
</details>

<div dir="rtl">

**2.** marginal likelihood را با کلمات تعریف کنید.
<details><summary>پاسخ</summary>
احتمال (چگالی) داده‌ی مشاهده‌شده تحت مدل، میانگین‌گیری‌شده روی همه‌ی مقادیر پارامتر با وزن پیشین: اینکه مدل پیش از برازش این داده‌ها را چقدر خوب پیش‌بینی کرده بود.
</details>

</div>

**3.** Why does the marginal likelihood penalize flexible models even without counting parameters?
<details><summary>Answer</summary>
Probability over possible datasets must sum to 1. A flexible model spreads its prior predictions over many datasets and so assigns each one, including the observed one, less probability, unless the data fall where only the flexible model predicts them.
</details>

<div dir="rtl">

**3.** چرا marginal likelihood حتی بدون شمردن پارامترها مدل‌های منعطف را جریمه می‌کند؟
<details><summary>پاسخ</summary>
احتمال روی مجموعه‌داده‌های ممکن باید جمعش 1 شود. یک مدل منعطف پیش‌بینی‌های پیشینش را روی مجموعه‌داده‌های زیادی پخش می‌کند و بنابراین به هرکدام، از جمله داده‌ی مشاهده‌شده، احتمال کمتری می‌دهد؛ مگر اینکه داده جایی بیفتد که فقط مدل منعطف پیش‌بینی‌اش می‌کند.
</details>

</div>

**4.** $\mathrm{BF}_{10} = 6$ and the prior odds are 1:3 (against $\mathcal{M}_1$). What are the posterior odds and $P(\mathcal{M}_1\mid\mathbf{y})$?
<details><summary>Answer</summary>
Posterior odds $= 6 \times 1/3 = 2$, so $P(\mathcal{M}_1\mid\mathbf{y}) = 2/3 \approx 0.67$.
</details>

<div dir="rtl">

**4.** $\mathrm{BF}_{10} = 6$ و بخت پیشین 1:3 (علیه $\mathcal{M}_1$) است. بخت پسین و $P(\mathcal{M}_1\mid\mathbf{y})$ چقدر است؟
<details><summary>پاسخ</summary>
بخت پسین $= 6 \times 1/3 = 2$، پس $P(\mathcal{M}_1\mid\mathbf{y}) = 2/3 \approx 0.67$.
</details>

</div>

**5.** State the Savage–Dickey ratio and the conditions for using it.
<details><summary>Answer</summary>
$\mathrm{BF}_{01} = p(\phi_0\mid\mathbf{y},\mathcal{M}_1)/p(\phi_0\mid\mathcal{M}_1)$: the posterior over the prior density at the null value under the larger model. It requires nested models (the null fixes $\phi = \phi_0$) and identical priors on the other parameters.
</details>

<div dir="rtl">

**5.** نسبت Savage–Dickey و شرایط استفاده از آن را بیان کنید.
<details><summary>پاسخ</summary>
$\mathrm{BF}_{01} = p(\phi_0\mid\mathbf{y},\mathcal{M}_1)/p(\phi_0\mid\mathcal{M}_1)$: چگالی پسین تقسیم بر چگالی پیشین در مقدار صفر تحت مدل بزرگ‌تر. به مدل‌های nested (فرض صفر $\phi = \phi_0$ را ثابت می‌کند) و پیشین‌های یکسان برای بقیه‌ی پارامترها نیاز دارد.
</details>

</div>

**6.** Why does widening the prior on the tested parameter increase $\mathrm{BF}_{01}$, even with fixed data?
<details><summary>Answer</summary>
A wider prior assigns more probability to large effects and less to the small effect sizes compatible with the data, so the alternative's marginal likelihood decreases while the null's does not change.
</details>

<div dir="rtl">

**6.** چرا پهن کردن پیشین پارامتر آزمون‌شده، حتی با داده‌ی ثابت، $\mathrm{BF}_{01}$ را افزایش می‌دهد؟
<details><summary>پاسخ</summary>
یک پیشین پهن‌تر احتمال بیشتری به اثرهای بزرگ و احتمال کمتری به اندازه‌ی اثرهای کوچک سازگار با داده می‌دهد، پس marginal likelihood فرضیه‌ی جایگزین کم می‌شود در حالی که درست‌نمایی فرض صفر تغییری نمی‌کند.
</details>

</div>

**7.** BIC gives $\mathrm{BF}_{12} \approx 20$, while the grid computation with your priors gives 3. Which do you report and why?
<details><summary>Answer</summary>
The grid BF, because it uses the actual priors and accounts for functional-form flexibility; BIC is a large-sample approximation with an implicit prior. Mention the discrepancy and, ideally, a prior sensitivity analysis.
</details>

<div dir="rtl">

**7.** BIC مقدار $\mathrm{BF}_{12} \approx 20$ می‌دهد، در حالی که محاسبه‌ی شبکه‌ای با پیشین‌های شما 3 می‌دهد. کدام را گزارش می‌کنید و چرا؟
<details><summary>پاسخ</summary>
Bayes factor شبکه‌ای را، چون از پیشین‌های واقعی استفاده می‌کند و انعطاف شکل تابعی را در نظر می‌گیرد؛ BIC تقریبی برای نمونه‌ی بزرگ با یک پیشین ضمنی است. به اختلاف اشاره کنید و، در صورت امکان، یک تحلیل حساسیت به پیشین بیاورید.
</details>

</div>

---

## Assignment · تکلیف

### A4: A Bayesian analysis by grid (1.0 point of 20; released Week 10, due at the start of the Week 12 lecture) · A4: یک تحلیل بیزی با شبکه (1.0 نمره از 20؛ انتشار هفته‌ی 10، موعد ابتدای درس هفته‌ی 12)

**Data:** the A2 dataset (`rng = np.random.default_rng(2024)`, 9 intervals, $n = 20$ items; see Week 4).

<div dir="rtl">

**داده:** مجموعه‌داده‌ی A2 (`rng = np.random.default_rng(2024)`، 9 فاصله، $n = 20$ آیتم؛ هفته‌ی 4 را ببینید).

</div>

**Tasks.**

<div dir="rtl">

**کارها.**

</div>

1. **Priors (1.5 pts).** Choose and justify priors for $(A, \lambda)$ of the exponential model and $(A, d)$ of the power model. Show prior predictive simulations of forgetting curves for both models and revise the priors if needed.
2. **Posterior (2 pts).** Compute the grid posteriors for both models. Report posterior means, SDs and 95% HDIs, and the posterior correlation of the two parameters. Plot the joint posteriors.
3. **Posterior predictive checks (2 pts).** Graphical PPC for both models, plus a numerical PPC with a test statistic you choose and justify.
4. **Bayes factor (2 pts).** Compute $\mathrm{BF}_{\text{pow,exp}}$ by grid integration (check the prior mass), compare it with the BIC approximation, and repeat with two alternative prior settings (sensitivity analysis).
5. **Comparison with A2 (1 pt).** Compare the posterior summaries with your A2 MLEs and their uncertainty.
6. **Interpretation (1.5 pts, max. 300 words).** What do you conclude about forgetting in these data, and how robust is the conclusion to the prior?

<div dir="rtl">

1. **پیشین‌ها (1.5 امتیاز).** پیشین‌هایی برای $(A, \lambda)$ مدل نمایی و $(A, d)$ مدل توانی انتخاب و توجیه کنید. شبیه‌سازی‌های پیش‌بینی پیشین منحنی‌های فراموشی را برای هر دو مدل نشان دهید و در صورت نیاز پیشین‌ها را اصلاح کنید.
2. **پسین (2 امتیاز).** پسین‌های شبکه‌ای را برای هر دو مدل حساب کنید. میانگین‌های پسین، انحراف معیارها و HDIهای 95%، و همبستگی پسین دو پارامتر را گزارش کنید. پسین‌های مشترک را رسم کنید.
3. **بررسی‌های پیش‌بینی پسین (2 امتیاز).** PPC نموداری برای هر دو مدل، به‌علاوه‌ی یک PPC عددی با آماره‌ی آزمونی که خودتان انتخاب و توجیه می‌کنید.
4. **Bayes factor (2 امتیاز).** $\mathrm{BF}_{\text{pow,exp}}$ را با انتگرال‌گیری شبکه‌ای حساب کنید (جرم پیشین را بررسی کنید)، با تقریب BIC مقایسه کنید، و با دو تنظیم پیشین دیگر تکرار کنید (تحلیل حساسیت).
5. **مقایسه با A2 (1 امتیاز).** خلاصه‌های پسین را با MLEهای A2 و عدم قطعیتشان مقایسه کنید.
6. **تفسیر (1.5 امتیاز، حداکثر 300 کلمه).** درباره‌ی فراموشی در این داده‌ها چه نتیجه‌ای می‌گیرید و این نتیجه‌گیری چقدر در برابر پیشین پایدار است؟

</div>

**Rubric:** points as above; within each task: correctness 60%, figures and tables 20%, interpretation 20%. Late submissions lose 10% per day (max. 3 days).

<div dir="rtl">

**روبریک:** امتیازها مطابق بالا؛ داخل هر کار: درستی 60%، نمودارها و جدول‌ها 20%، تفسیر 20%. برای تحویل با تأخیر، روزی 10% کسر می‌شود (حداکثر 3 روز).

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Lee & Wagenmakers (2014), chapter 7.** Bayesian model comparison: marginal likelihoods, Bayes factors and the Savage–Dickey method, with worked examples. *(Main reading.)*
- **Farrell & Lewandowsky (2018), chapter 11.** Bayesian model comparison using Bayes factors, in the context of cognitive models.
- **Kruschke (2014), chapter 10.** Model comparison and hierarchical modeling, a gentle introduction to Bayes factors and their prior sensitivity.
- **Martin, Kumar & Lao (2021), chapter 2.** Exploratory analysis of Bayesian models, including posterior predictive checks.

<div dir="rtl">

- **Lee & Wagenmakers (2014)، فصل 7.** مقایسه‌ی بیزی مدل‌ها: درست‌نمایی‌های حاشیه‌ای، Bayes factor و روش Savage–Dickey، با مثال‌های حل‌شده. *(منبع اصلی.)*
- **Farrell & Lewandowsky (2018)، فصل 11.** مقایسه‌ی بیزی مدل‌ها با Bayes factor، در بافت مدل‌های شناختی.
- **Kruschke (2014)، فصل 10.** مقایسه‌ی مدل‌ها و مدل‌سازی سلسله‌مراتبی؛ مقدمه‌ای ساده بر Bayes factor و حساسیتش به پیشین.
- **Martin, Kumar & Lao (2021)، فصل 2.** تحلیل اکتشافی مدل‌های بیزی، از جمله بررسی‌های پیش‌بینی پسین.

</div>

*Preview for Week 11:* our grids worked for two parameters. For five, ten or a hundred parameters we need a smarter way to explore the posterior: Markov chain Monte Carlo. You will build your first sampler from scratch.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 11:* شبکه‌های ما برای دو پارامتر کار کردند. برای پنج، ده یا صد پارامتر به راه هوشمندانه‌تری برای کاوش پسین نیاز داریم: Markov chain Monte Carlo. اولین نمونه‌گیر خود را از صفر می‌سازید.

</div>
