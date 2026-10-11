# Week 9: Bayesian Modeling I: Priors, Posteriors and Grid Approximation · هفته‌ی 9: مدل‌سازی بیزی 1: پیشین، پسین و تقریب شبکه‌ای

> **Chapter 4: Bayesian modeling** · Lecture 1 h · Lab 2 h
> **Running data:** a recall proportion (30 of 50) and the Week 2 SDT participant (68/100 hits, 11/100 false alarms).

<div dir="rtl">

> **فصل 4: مدل‌سازی بیزی** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** یک نسبت یادآوری (30 از 50) و شرکت‌کننده‌ی SDT هفته‌ی 2 (68/100 hit، 11/100 false alarm).

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| prior | توزیع پیشین (prior) | باور درباره‌ی پارامتر پیش از دیدن داده |
| posterior | توزیع پسین (posterior) | باور درباره‌ی پارامتر بعد از دیدن داده |
| grid approximation | تقریب شبکه‌ای (grid) | محاسبه‌ی پسین روی شبکه‌ای از مقادیر |
| signal detection theory (SDT) | نظریه‌ی تشخیص علامت | مدلی که حساسیت را از سوگیری پاسخ جدا می‌کند |
| hit | اصابت (hit) | پاسخ «بله» وقتی علامت وجود دارد |
| Bayes' rule | قاعده‌ی بیز | پسین ∝ درست‌نمایی × پیشین |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| evidence | شواهد | اطلاعاتی که برای تصمیم جمع می‌شود |
| beta-binomial model | مدل beta-binomial | پیشین Beta با داده‌ی دوجمله‌ای |
| binomial distribution | توزیع دوجمله‌ای | توزیع تعداد موفقیت در n کوشش |
| MAP estimate | برآورد MAP | مُد توزیع پسین |
| credible interval / HDI | بازه‌ی باورپذیر (credible interval) | بازه‌ای که با احتمال مشخص پارامتر را دارد |
| confidence interval (CI) | بازه‌ی اطمینان | بازه‌ای که با روش مشخص پارامتر واقعی را در بر می‌گیرد |
| prior predictive check | بررسی پیش‌بینی پیشین | شبیه‌سازی داده از پیشین برای سنجش معقول بودن آن |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| maximum likelihood estimate (MLE) | برآورد بیشینه‌ی درست‌نمایی | پارامترهایی که داده را محتمل‌ترین می‌کنند |
| cognitive model | مدل شناختی | توصیف دقیق و ریاضی یا محاسباتی از یک فرایند ذهنی |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| conjugate prior | پیشین مزدوج (conjugate) | پیشینی که پسین هم‌خانواده می‌دهد |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| accuracy | دقت | نسبت پاسخ‌های درست |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **State** Bayes' rule for parameters and **identify** the roles of prior, likelihood, evidence and posterior.
2. **Compute** posteriors analytically for the beta-binomial model and numerically by grid approximation, for one and two parameters.
3. **Summarize** a posterior (mean, median, MAP, SD, equal-tailed and highest-density intervals) and **distinguish** a credible interval from a confidence interval.
4. **Explain** how the prior and the amount of data jointly determine the posterior, and **use** prior predictive simulation to check whether a prior is sensible.
5. **Interpret** posterior probabilities of psychologically meaningful hypotheses (e.g., "$P(d' > 1 \mid \text{data})$").

<div dir="rtl">

1. قاعده‌ی بیز را برای پارامترها **بیان کنند** و نقش پیشین (prior)، درست‌نمایی، شواهد (evidence) و پسین (posterior) را **مشخص کنند**.
2. پسین را برای مدل beta-binomial به‌صورت تحلیلی و با تقریب شبکه‌ای به‌صورت عددی، برای یک و دو پارامتر، **حساب کنند**.
3. یک پسین را **خلاصه کنند** (میانگین، میانه، MAP، انحراف معیار، بازه‌های دم‌برابر و بیشترین چگالی) و credible interval را از بازه‌ی اطمینان **متمایز کنند**.
4. **توضیح دهند** که پیشین و مقدار داده با هم چطور پسین را تعیین می‌کنند، و با شبیه‌سازی پیش‌بینی پیشین **بررسی کنند** که پیشین معقول است یا نه.
5. احتمال‌های پسین فرضیه‌های معنادار روان‌شناختی را **تفسیر کنند** (مثلاً «$P(d' > 1 \mid \text{data})$»).

</div>

---

## Motivation & big picture · مقدمه

Since Week 3 we have asked: "which single parameter value best accounts for the data?" and then, in Week 5, "how much would that estimate vary across imaginary replications?" Researchers often want to say something more direct:

<div dir="rtl">

از هفته‌ی 3 پرسیده‌ایم: «کدام مقدار واحد پارامتر داده‌ها را بهتر توضیح می‌دهد؟» و بعد، در هفته‌ی 5، «این برآورد در تکرارهای خیالی چقدر تغییر می‌کرد؟» پژوهشگران اغلب می‌خواهند چیز مستقیم‌تری بگویند:

</div>

> *"Given these data, there is a 95% probability that this participant's sensitivity lies between 1.2 and 2.1."*
> *"The probability that the payoff manipulation made participants more liberal is 0.98."*

<div dir="rtl">

> *«با توجه به این داده‌ها، با احتمال 95% حساسیت این شرکت‌کننده بین 1.2 و 2.1 است.»*
> *«احتمال اینکه دست‌کاری پاداش شرکت‌کننده‌ها را liberalتر کرده باشد 0.98 است.»*

</div>

Frequentist confidence intervals do **not** license such statements (Week 5). Bayesian inference does, at a price: we must state what we believed about the parameters **before** seeing the data, in the form of a **prior distribution**. Bayes' rule then combines the prior with the likelihood (which we already know how to write) into a **posterior distribution**: everything the model and the data together say about the parameters.

<div dir="rtl">

بازه‌های اطمینان فراوانی‌گرا اجازه‌ی چنین جمله‌هایی را **نمی‌دهند** (هفته‌ی 5). استنباط بیزی می‌دهد، به یک قیمت: باید بگوییم **پیش از** دیدن داده درباره‌ی پارامترها چه باوری داشتیم، به شکل یک **توزیع پیشین**. بعد قاعده‌ی بیز پیشین را با درست‌نمایی (که بلدیم بنویسیم) ترکیب می‌کند و یک **توزیع پسین** می‌سازد: همه‌ی آنچه مدل و داده با هم درباره‌ی پارامترها می‌گویند.

</div>

Bayesian methods also make several of our earlier headaches easier: uncertainty comes for free (no Hessians or bootstraps), hierarchical models of many participants become natural (Week 13), and model comparison gets a principled answer (Week 10). The cost is computation, which is why Weeks 11–13 are about sampling.

<div dir="rtl">

روش‌های بیزی چند دردسر قبلی ما را هم آسان‌تر می‌کنند: عدم قطعیت مجانی به دست می‌آید (بدون Hessian یا bootstrap)، مدل‌های سلسله‌مراتبی چند شرکت‌کننده طبیعی می‌شوند (هفته‌ی 13)، و مقایسه‌ی مدل‌ها یک جواب اصولی پیدا می‌کند (هفته‌ی 10). هزینه‌اش محاسبه است، و برای همین هفته‌های 11 تا 13 درباره‌ی نمونه‌گیری‌اند.

</div>

> **Reminder (Week 1):** this week is about Bayesian **data analysis**, a method we as scientists use to estimate the parameters of *any* model. It makes no claim that the mind is Bayesian. Bayesian *models of cognition* come in Week 15.

<div dir="rtl">

> **یادآوری (هفته‌ی 1):** این هفته درباره‌ی **تحلیل داده‌ی بیزی** است؛ روشی که ما پژوهشگران برای برآورد پارامترهای *هر* مدلی به کار می‌بریم. هیچ ادعایی ندارد که ذهن بیزی است. *مدل‌های بیزی شناخت* در هفته‌ی 15 می‌آیند.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Small samples and individual cases.** Clinical neuropsychology often has one patient and a few dozen trials. A Bayesian analysis with a sensible prior gives usable, honest uncertainty where MLE is unstable.
- **Direct probability statements** that clinicians and policy makers understand: "there is a 97% probability that the new training improved memory".
- **Adaptive testing**: computerized tests (e.g. vision and hearing tests, adaptive exams) update a posterior after every response and choose the next item where it is most informative.
- **Combining evidence**: today's posterior is tomorrow's prior, so results of earlier studies can be built in formally.
- **Modern cognitive modeling software** (PyMC, Stan, JAGS) is Bayesian; most hierarchical models in recent papers are fitted this way (Week 13).

<div dir="rtl">

- **نمونه‌های کوچک و موردهای تکی.** در عصب‌روان‌شناسی بالینی اغلب یک بیمار و چند ده trial داریم. تحلیل بیزی با یک prior معقول، عدم قطعیت صادقانه و قابل استفاده‌ای می‌دهد، جایی که MLE ناپایدار است.
- **گزاره‌های احتمالی مستقیم** که پزشکان و سیاست‌گذاران می‌فهمند: «با احتمال 97% آموزش جدید حافظه را بهتر کرده».
- **آزمون‌های تطبیقی (adaptive testing):** آزمون‌های کامپیوتری (مثلاً آزمون‌های بینایی و شنوایی، امتحان‌های تطبیقی) بعد از هر پاسخ posterior را به‌روز می‌کنند و آیتم بعدی را جایی انتخاب می‌کنند که بیشترین اطلاعات را می‌دهد.
- **ترکیب شواهد:** posterior امروز prior فرداست، پس نتایج مطالعه‌های قبلی را می‌شود به‌طور رسمی وارد تحلیل کرد.
- **نرم‌افزارهای امروزی مدل‌سازی شناختی** (PyMC، Stan، JAGS) بیزی‌اند؛ بیشتر مدل‌های سلسله‌مراتبی در مقاله‌های اخیر به همین روش برازش می‌شوند (هفته‌ی 13).

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

So far we found *one* best parameter value and then asked how much it might vary. The Bayesian approach instead describes our knowledge about the parameter as a whole **probability distribution**. Before the data, the **prior** says which values we consider plausible (e.g. "recall probability is probably moderate, not 0 or 1"). The data then re-weight every possible value by its likelihood (Week 4). The result, the **posterior**, says how plausible each value is *after* seeing the data. In words: *posterior ∝ likelihood × prior*. From the posterior we can read off a best guess (its mean), an uncertainty (its spread), and direct statements such as "the probability that $d' > 1$ is 0.93". With little data the prior matters a lot; with much data the posterior is dominated by the likelihood and ends up close to the MLE. Computing the posterior is easy for one or two parameters (on a grid) and needs sampling methods beyond that (Weeks 11–13).

<div dir="rtl">

تا اینجا *یک* بهترین مقدار پارامتر پیدا می‌کردیم و بعد می‌پرسیدیم چقدر ممکن است تغییر کند. روش بیزی در عوض دانش ما درباره‌ی پارامتر را به شکل یک **توزیع احتمال** کامل توصیف می‌کند. پیش از داده، **prior (پیشین)** می‌گوید کدام مقدارها را معقول می‌دانیم (مثلاً «احتمال یادآوری احتمالاً متوسط است، نه 0 یا 1»). بعد داده‌ها به هر مقدار ممکن به اندازه‌ی درست‌نمایی‌اش (هفته‌ی 4) وزن تازه می‌دهند. نتیجه، **posterior (پسین)**، می‌گوید هر مقدار *بعد* از دیدن داده چقدر معقول است. به زبان ساده: *posterior ∝ likelihood × prior*. از posterior می‌توانیم یک بهترین حدس (میانگین آن)، یک عدم قطعیت (پراکندگی آن) و گزاره‌های مستقیمی مثل «احتمال اینکه $d' > 1$ باشد 0.93 است» بخوانیم. با داده‌ی کم prior اثر زیادی دارد؛ با داده‌ی زیاد posterior زیر سلطه‌ی درست‌نمایی است و به MLE نزدیک می‌شود. محاسبه‌ی posterior برای یک یا دو پارامتر آسان است (روی grid) و برای بیشتر از آن به روش‌های نمونه‌گیری نیاز دارد (هفته‌های 11 تا 13).

</div>

**Suggested timing (60 min):** Bayes' rule 10 · priors 10 · beta-binomial 12 · grid approximation 10 · summaries and credible intervals 12 · prior predictive checks 6.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** قاعده‌ی بیز 10 · پیشین‌ها 10 · beta-binomial 12 · تقریب شبکه‌ای 10 · خلاصه‌ها و credible intervalها 12 · بررسی پیش‌بینی پیشین 6.

</div>

### 1. Bayes' rule for parameters · 1. قاعده‌ی بیز برای پارامترها

$$
\underbrace{p(\boldsymbol\theta \mid \mathbf{y})}_{\text{posterior}}
= \frac{\overbrace{p(\mathbf{y} \mid \boldsymbol\theta)}^{\text{likelihood}}\;\overbrace{p(\boldsymbol\theta)}^{\text{prior}}}{\underbrace{p(\mathbf{y})}_{\text{evidence (marginal likelihood)}}},
\qquad
p(\mathbf{y}) = \int p(\mathbf{y}\mid\boldsymbol\theta)\,p(\boldsymbol\theta)\,d\boldsymbol\theta.
$$

(We suppress "$\mathcal{M}$" in the notation this week: everything is conditional on the model.)

<div dir="rtl">

(این هفته «$\mathcal{M}$» را در نمادگذاری نمی‌نویسیم: همه‌چیز مشروط به مدل است.)

</div>

- The **likelihood** is exactly the function from Week 4.
- The **prior** expresses what is known or plausible before the data.
- The **evidence** $p(\mathbf{y})$ does not depend on $\boldsymbol\theta$. For estimation it is just the normalizing constant that makes the posterior integrate to 1:

<div dir="rtl">

- **درست‌نمایی** دقیقاً همان تابع هفته‌ی 4 است.
- **پیشین** آنچه را پیش از داده معلوم یا محتمل است بیان می‌کند.
- **شواهد** $p(\mathbf{y})$ به $\boldsymbol\theta$ بستگی ندارد. برای برآورد، فقط ثابت نرمال‌ساز است که انتگرال پسین را 1 می‌کند:

</div>

$$
p(\boldsymbol\theta \mid \mathbf{y}) \propto p(\mathbf{y}\mid\boldsymbol\theta)\, p(\boldsymbol\theta).
$$

**Posterior ∝ likelihood × prior.** In Week 10 the evidence becomes the star of Bayesian model comparison.

<div dir="rtl">

**پسین ∝ درست‌نمایی × پیشین.** در هفته‌ی 10 شواهد ستاره‌ی مقایسه‌ی بیزی مدل‌ها می‌شود.

</div>

**Intuition.** The posterior is a compromise: it is high where the parameter values are both plausible *a priori* and make the data probable. With little data the prior matters; with a lot of data the likelihood dominates and the posterior concentrates around the MLE.

<div dir="rtl">

**شهود.** پسین یک مصالحه است: جایی بالاست که مقادیر پارامتر هم *از پیش* محتمل‌اند و هم داده را محتمل می‌کنند. با داده‌ی کم پیشین مهم است؛ با داده‌ی زیاد درست‌نمایی غالب می‌شود و پسین حول MLE متمرکز می‌شود.

</div>

#### Reading the math · خواندن ریاضی

- $p(\boldsymbol\theta \mid \mathbf{y})$: "probability (density) of the parameter value $\boldsymbol\theta$ *given* the data". This is what we want.
- $p(\mathbf{y} \mid \boldsymbol\theta)$: the likelihood, read as a function of $\boldsymbol\theta$ (Week 4).
- $p(\boldsymbol\theta)$: the prior, chosen before the data.
- $p(\mathbf{y}) = \int p(\mathbf{y}\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta$: the integral adds up "likelihood × prior" over *all* possible parameter values. It is one number, the same for every $\boldsymbol\theta$, so for estimation it only rescales the curve to total area 1.
- $\propto$ means "proportional to": equal up to a constant factor. In practice we compute likelihood × prior at many values and then divide by their sum, exactly as in the 4-point table of the worked example (0.0004479 / 0.0009574 = 0.468).

<div dir="rtl">

- $p(\boldsymbol\theta \mid \mathbf{y})$: «احتمال (چگالی) مقدار پارامتر $\boldsymbol\theta$ *به شرط* داده». این همان چیزی است که می‌خواهیم.
- $p(\mathbf{y} \mid \boldsymbol\theta)$: درست‌نمایی، که به‌عنوان تابعی از $\boldsymbol\theta$ خوانده می‌شود (هفته‌ی 4).
- $p(\boldsymbol\theta)$: prior که پیش از داده انتخاب می‌شود.
- $p(\mathbf{y}) = \int p(\mathbf{y}\mid\boldsymbol\theta)p(\boldsymbol\theta)\,d\boldsymbol\theta$: انتگرال، «درست‌نمایی × prior» را روی *همه‌ی* مقدارهای ممکن پارامتر جمع می‌کند. یک عدد است و برای همه‌ی $\boldsymbol\theta$ها یکسان است، پس در برآورد فقط منحنی را طوری مقیاس می‌کند که مساحت کل 1 شود.
- $\propto$ یعنی «متناسب با»: برابر، به‌جز یک ضریب ثابت. در عمل «درست‌نمایی × prior» را در مقدارهای زیادی حساب می‌کنیم و بعد بر جمعشان تقسیم می‌کنیم، دقیقاً مثل جدول چهارنقطه‌ای مثال حل‌شده (0.0004479 / 0.0009574 = 0.468).

</div>

### 2. Choosing priors · 2. انتخاب پیشین‌ها

| Kind | Example for a recall probability $\theta$ | When |
|---|---|---|
| Flat / uniform | $\mathrm{Beta}(1, 1)$ | When every value in the range is genuinely equally plausible (rarely true) |
| Weakly informative | $\mathrm{Beta}(2, 2)$: mild preference for moderate values | **Default for most cognitive models**: rules out absurd values, otherwise lets the data speak |
| Informative | $\mathrm{Beta}(20, 5)$: "recall after one day is around 0.8" | When previous studies or theory provide real knowledge |

<div dir="rtl">

| نوع | مثال برای احتمال یادآوری $\theta$ | چه وقت |
|---|---|---|
| تخت / یکنواخت | $\mathrm{Beta}(1, 1)$ | وقتی هر مقدار در دامنه واقعاً به یک اندازه محتمل است (به‌ندرت درست است) |
| ضعیف‌آگاهی‌بخش (weakly informative) | $\mathrm{Beta}(2, 2)$: ترجیح ملایم برای مقادیر میانی | **پیش‌فرض برای بیشتر مدل‌های شناختی**: مقادیر پوچ را کنار می‌گذارد و بقیه را به داده می‌سپارد |
| آگاهی‌بخش (informative) | $\mathrm{Beta}(20, 5)$: «یادآوری بعد از یک روز حدود 0.8 است» | وقتی مطالعات قبلی یا نظریه دانش واقعی می‌دهند |

</div>

Principles:
- Priors must be fixed **before** seeing the data.
- They should respect the parameter's range (e.g., no prior mass on negative decay rates).
- They should be checked by **prior predictive simulation** (§6): which *data* does the prior imply?
- A "vague" prior on one scale can be very informative on another scale (lab Part D).
- Report your priors and check the sensitivity of conclusions to reasonable alternatives (Week 10).

<div dir="rtl">

اصول:
- پیشین‌ها باید **پیش از** دیدن داده تعیین شوند.
- باید دامنه‌ی پارامتر را رعایت کنند (مثلاً هیچ جرم پیشینی روی نرخ زوال منفی نباشد).
- باید با **شبیه‌سازی پیش‌بینی پیشین** بررسی شوند (بخش 6): پیشین کدام *داده‌ها* را نتیجه می‌دهد؟
- یک پیشین «مبهم» روی یک مقیاس می‌تواند روی مقیاس دیگری خیلی آگاهی‌بخش باشد (بخش D lab).
- پیشین‌هایتان را گزارش کنید و حساسیت نتیجه‌گیری‌ها را به جایگزین‌های معقول بررسی کنید (هفته‌ی 10).

</div>

### 3. A closed-form case: the beta-binomial model · 3. یک حالت با جواب بسته: مدل beta-binomial

For $y$ successes in $n$ binomial trials with a $\mathrm{Beta}(a_0, b_0)$ prior on $\theta$:

<div dir="rtl">

برای $y$ موفقیت در $n$ trial دوجمله‌ای با پیشین $\mathrm{Beta}(a_0, b_0)$ روی $\theta$:

</div>

$$
p(\theta \mid y) \propto \underbrace{\theta^{y}(1-\theta)^{n-y}}_{\text{likelihood}} \cdot \underbrace{\theta^{a_0 - 1}(1-\theta)^{b_0 - 1}}_{\text{prior}}
= \theta^{a_0 + y - 1}(1-\theta)^{b_0 + n - y - 1},
$$

so the posterior is again a Beta distribution:

<div dir="rtl">

پس پسین دوباره یک توزیع Beta است:

</div>

$$
\theta \mid y \sim \mathrm{Beta}(a_0 + y,\; b_0 + n - y).
$$

When prior and posterior come from the same family, the prior is called **conjugate**.

<div dir="rtl">

وقتی پیشین و پسین از یک خانواده باشند، پیشین را **conjugate** می‌نامند.

</div>

- $a_0$ and $b_0$ act like **pseudo-counts** of prior successes and failures.
- Posterior mean: $\dfrac{a_0 + y}{a_0 + b_0 + n}$, a weighted average of the prior mean $\frac{a_0}{a_0 + b_0}$ and the observed proportion $y/n$, with weights $a_0 + b_0$ and $n$.
- **Connection to Weeks 2 and 4:** the log-linear correction $(y + 0.5)/(n + 1)$ is exactly the posterior mean under a $\mathrm{Beta}(0.5, 0.5)$ prior, the so-called *Jeffreys prior*. The "correction" was a Bayesian estimate in disguise.

<div dir="rtl">

- $a_0$ و $b_0$ مثل **شمارش‌های کاذب** (pseudo-counts) موفقیت‌ها و شکست‌های پیشین عمل می‌کنند.
- میانگین پسین: $\dfrac{a_0 + y}{a_0 + b_0 + n}$؛ میانگین وزنی میانگین پیشین $\frac{a_0}{a_0 + b_0}$ و نسبت مشاهده‌شده‌ی $y/n$، با وزن‌های $a_0 + b_0$ و $n$.
- **ارتباط با هفته‌های 2 و 4:** تصحیح log-linear $(y + 0.5)/(n + 1)$ دقیقاً میانگین پسین تحت پیشین $\mathrm{Beta}(0.5, 0.5)$، به نام *پیشین Jeffreys*، است. آن «تصحیح» یک برآورد بیزی در لباس مبدل بود.

</div>

#### Reading the math · خواندن ریاضی

- The **Beta distribution** $\mathrm{Beta}(a, b)$ is a flexible bell-like curve on the interval 0–1, ideal for describing beliefs about a probability. Its mean is $a/(a+b)$. $\mathrm{Beta}(1,1)$ is flat; $\mathrm{Beta}(20, 5)$ is a narrow bump around 0.8.
- The update rule $\mathrm{Beta}(a_0, b_0) \to \mathrm{Beta}(a_0 + y, b_0 + n - y)$ is just **counting**: add the observed successes to $a$ and the failures to $b$. The prior behaves as if we had already seen $a_0$ successes and $b_0$ failures (pseudo-counts).
- **Example:** prior $\mathrm{Beta}(2, 2)$ ("as if" 2 recalls and 2 failures), data 7 of 10 → $\mathrm{Beta}(9, 5)$, mean $9/14 = 0.643$. The prior pulls the observed 0.70 slightly toward 0.5, because it adds 4 pseudo-observations to 10 real ones.

<div dir="rtl">

- **توزیع Beta** $\mathrm{Beta}(a, b)$ یک منحنی زنگوله‌مانند انعطاف‌پذیر روی بازه‌ی 0 تا 1 است و برای توصیف باور درباره‌ی یک احتمال ایده‌آل است. میانگین آن $a/(a+b)$ است. $\mathrm{Beta}(1,1)$ صاف است؛ $\mathrm{Beta}(20, 5)$ یک برآمدگی باریک حول 0.8 است.
- قاعده‌ی به‌روزرسانی $\mathrm{Beta}(a_0, b_0) \to \mathrm{Beta}(a_0 + y, b_0 + n - y)$ فقط **شمردن** است: موفقیت‌های مشاهده‌شده را به $a$ و شکست‌ها را به $b$ اضافه کن. prior طوری رفتار می‌کند که انگار قبلاً $a_0$ موفقیت و $b_0$ شکست دیده‌ایم (شمارش‌های ساختگی یا pseudo-counts).
- **مثال:** prior برابر $\mathrm{Beta}(2, 2)$ («انگار» 2 یادآوری و 2 شکست)، داده 7 از 10 ← $\mathrm{Beta}(9, 5)$ با میانگین $9/14 = 0.643$. prior مقدار مشاهده‌شده‌ی 0.70 را کمی به سمت 0.5 می‌کشد، چون 4 مشاهده‌ی ساختگی به 10 مشاهده‌ی واقعی اضافه می‌کند.

</div>

### 4. Grid approximation · 4. تقریب شبکه‌ای (grid approximation)

Most cognitive models have no conjugate prior. If there are only one or two parameters, we can approximate the posterior on a grid:

<div dir="rtl">

بیشتر مدل‌های شناختی پیشین conjugate ندارند. اگر فقط یک یا دو پارامتر باشد، می‌توانیم پسین را روی یک شبکه تقریب بزنیم:

</div>

1. Define a grid of parameter values $\boldsymbol\theta_1, \dots, \boldsymbol\theta_G$ covering all plausible values.
2. At each grid point compute the **log** prior plus the **log** likelihood (logs avoid underflow, as in Week 4).
3. Subtract the maximum, exponentiate, and normalize so that the values sum to 1 (or integrate to 1).

<div dir="rtl">

1. شبکه‌ای از مقادیر پارامتر $\boldsymbol\theta_1, \dots, \boldsymbol\theta_G$ تعریف کنید که همه‌ی مقادیر معقول را بپوشاند.
2. در هر نقطه‌ی شبکه **لگاریتم** پیشین به‌علاوه‌ی **لگاریتم** درست‌نمایی را حساب کنید (لگاریتم‌ها، مثل هفته‌ی 4، از سرریز جلوگیری می‌کنند).
3. بیشینه را کم کنید، نمایی بگیرید و نرمال کنید تا جمع مقادیر 1 شود (یا انتگرالشان 1 شود).

</div>

The result is a discrete approximation of the posterior from which we can compute any summary. Grid approximation is exact up to the grid resolution and is ideal for building intuition. It fails beyond 2–3 parameters (the curse of dimensionality, Week 3), which motivates MCMC (Weeks 11–13).

<div dir="rtl">

نتیجه یک تقریب گسسته از پسین است که هر خلاصه‌ای را می‌شود از آن حساب کرد. تقریب شبکه‌ای تا حد دقت شبکه دقیق است و برای ساختن شهود ایده‌آل است. فراتر از 2 تا 3 پارامتر شکست می‌خورد (نفرین ابعاد، هفته‌ی 3)، و همین انگیزه‌ی MCMC است (هفته‌های 11–13).

</div>

### 5. Summarizing a posterior · 5. خلاصه کردن یک پسین

| Summary | Definition | Remark |
|---|---|---|
| Posterior mean | $\mathbb{E}[\theta \mid \mathbf{y}]$ | Minimizes expected squared error |
| Posterior median | 50th percentile | Robust to skew |
| MAP | $\arg\max_\theta p(\theta\mid\mathbf{y})$ | Equals the MLE under a flat prior |
| Posterior SD | $\sqrt{\mathrm{Var}[\theta\mid\mathbf{y}]}$ | The Bayesian counterpart of a SE |
| 95% equal-tailed interval | 2.5th to 97.5th percentiles | Easy to compute |
| 95% **HDI** (highest-density interval) | The narrowest interval containing 95% of the posterior; every value inside is more probable than every value outside | Preferred for skewed posteriors |

<div dir="rtl">

| خلاصه | تعریف | توضیح |
|---|---|---|
| میانگین پسین | $\mathbb{E}[\theta \mid \mathbf{y}]$ | خطای مربع مورد انتظار را کمینه می‌کند |
| میانه‌ی پسین | صدک 50 | در برابر چولگی مقاوم است |
| MAP | $\arg\max_\theta p(\theta\mid\mathbf{y})$ | تحت پیشین تخت با MLE برابر است |
| انحراف معیار پسین | $\sqrt{\mathrm{Var}[\theta\mid\mathbf{y}]}$ | همتای بیزی SE |
| بازه‌ی دم‌برابر 95% | صدک 2.5 تا 97.5 | محاسبه‌اش آسان است |
| **HDI** 95% (بازه‌ی بیشترین چگالی) | باریک‌ترین بازه‌ای که 95% پسین را در بر دارد؛ هر مقدار داخل آن از هر مقدار بیرونش محتمل‌تر است | برای پسین‌های چوله ترجیح دارد |

</div>

**Credible vs. confidence interval.** A 95% credible interval *does* mean "given the model, the prior and the data, the parameter lies in this interval with probability 0.95". A confidence interval is a statement about the long-run behavior of the procedure (Week 5). With weak priors and plenty of data, the two often coincide numerically, but their interpretations differ.

<div dir="rtl">

**credible interval در برابر بازه‌ی اطمینان.** credible interval 95% *واقعاً* یعنی «با توجه به مدل، پیشین و داده، پارامتر با احتمال 0.95 در این بازه است». بازه‌ی اطمینان گزاره‌ای درباره‌ی رفتار بلندمدت یک رویه است (هفته‌ی 5). با پیشین‌های ضعیف و داده‌ی کافی، این دو اغلب از نظر عددی یکی می‌شوند، ولی تفسیرشان فرق دارد.

</div>

**Posterior probabilities of hypotheses** come for free: $P(d' > 1 \mid \mathbf{y})$ is just the posterior mass above 1.

<div dir="rtl">

**احتمال پسین فرضیه‌ها** مجانی به دست می‌آید: $P(d' > 1 \mid \mathbf{y})$ فقط جرم پسین بالای 1 است.

</div>

### 6. Prior predictive checks · 6. بررسی‌های پیش‌بینی پیشین (prior predictive checks)

The **prior predictive distribution** describes the data the model expects *before* seeing any data:

<div dir="rtl">

**توزیع پیش‌بینی پیشین** داده‌هایی را توصیف می‌کند که مدل *پیش از* دیدن هر داده‌ای انتظار دارد:

</div>

$$
p(\mathbf{y}^{\text{rep}}) = \int p(\mathbf{y}^{\text{rep}}\mid\boldsymbol\theta)\, p(\boldsymbol\theta)\, d\boldsymbol\theta.
$$

To simulate from it: draw $\boldsymbol\theta$ from the prior, then simulate data from the model. If the simulated data look absurd (e.g., nearly all hit rates at exactly 0 or 1, or recall that *increases* over a month), the prior is unreasonable. Prior predictive checks are the Bayesian version of the "simulate before you fit" habit from Week 2.

<div dir="rtl">

برای شبیه‌سازی از آن: $\boldsymbol\theta$ را از پیشین بکشید و بعد از مدل داده شبیه‌سازی کنید. اگر داده‌های شبیه‌سازی‌شده پوچ به نظر برسند (مثلاً تقریباً همه‌ی نرخ‌های hit دقیقاً 0 یا 1، یا یادآوری‌ای که طی یک ماه *بیشتر* می‌شود)، پیشین نامعقول است. بررسی‌های پیش‌بینی پیشین نسخه‌ی بیزی عادت «پیش از برازش شبیه‌سازی کن» هفته‌ی 2 هستند.

</div>

> **Advanced: the posterior as updated prior.** Because $p(\boldsymbol\theta\mid\mathbf{y}_1, \mathbf{y}_2) \propto p(\mathbf{y}_2\mid\boldsymbol\theta)\, p(\boldsymbol\theta\mid\mathbf{y}_1)$ for independent data, today's posterior is tomorrow's prior. Bayesian updating is therefore naturally sequential, which is also why Bayesian inference is a popular normative model of *learning* (Week 15).

<div dir="rtl">

> **پیشرفته: پسین به‌عنوان پیشین به‌روزشده.** چون برای داده‌های مستقل $p(\boldsymbol\theta\mid\mathbf{y}_1, \mathbf{y}_2) \propto p(\mathbf{y}_2\mid\boldsymbol\theta)\, p(\boldsymbol\theta\mid\mathbf{y}_1)$، پسین امروز پیشین فرداست. پس به‌روزرسانی بیزی ذاتاً ترتیبی است، و به همین دلیل استنباط بیزی یک مدل هنجاری محبوب برای *یادگیری* است (هفته‌ی 15).

</div>

#### For an engineer · برای یک مهندس

- This is **Bayesian estimation** as in detection and estimation theory: the posterior is what an MAP or MMSE estimator works with. The posterior mean is the **MMSE estimate**; the posterior mode is the **MAP estimate**; with a flat prior MAP = ML.
- The **conjugate Beta–binomial update** is the same idea as conjugate Gaussian updating, the scalar core of the **Kalman filter** (prior mean and variance + measurement → posterior mean and variance), here for a probability instead of a Gaussian state.
- **Sequential updating** ("today's posterior is tomorrow's prior") is exactly recursive Bayesian filtering.
- What is different in psychology: the prior is usually **weak** and must be *justified to readers*, and the main output is not a decision but a description of uncertainty about a psychological parameter. Prior predictive checks are the habit that makes priors defensible.

<div dir="rtl">

- این همان **تخمین بیزی** در نظریه‌ی آشکارسازی و تخمین است: posterior چیزی است که تخمین‌گر MAP یا MMSE با آن کار می‌کند. میانگین posterior همان **تخمین MMSE** است؛ مد posterior **تخمین MAP** است؛ با prior صاف، MAP = ML.
- **به‌روزرسانی conjugate بتا–دوجمله‌ای** همان ایده‌ی به‌روزرسانی conjugate گاوسی است، یعنی هسته‌ی اسکالر **فیلتر کالمن** (میانگین و واریانس prior + اندازه‌گیری ← میانگین و واریانس posterior)، فقط اینجا برای یک احتمال به جای یک حالت گاوسی.
- **به‌روزرسانی ترتیبی** («posterior امروز prior فرداست») دقیقاً همان فیلترینگ بیزی بازگشتی است.
- تفاوت در روان‌شناسی: prior معمولاً **ضعیف** است و باید *برای خواننده توجیه شود*، و خروجی اصلی یک تصمیم نیست، بلکه توصیف عدم قطعیت درباره‌ی یک پارامتر روان‌شناختی است. بررسی پیش‌بینی پیشین (prior predictive check) عادتی است که priorها را قابل دفاع می‌کند.

</div>

#### For the instructor · برای مدرس

- **Do the 4-point grid on the board** (worked example, Part 1) with a column for prior, likelihood, product and posterior. It contains the whole of Bayesian inference in one table. Then change the prior to (0.1, 0.1, 0.4, 0.4) and recompute live: students see the prior at work.
- **Use the Beta pseudo-count story.** "A Beta(2, 2) prior is like having already seen 2 recalls and 2 failures." Students who find priors arbitrary relax once they see them as imaginary data.
- **Address the "subjectivity" worry directly.** Every analysis has assumptions (the likelihood is one too); Bayesian analysis makes one more of them explicit, and sensitivity analysis (Week 10) checks how much it matters.
- **Typical questions.**
  - *"Which prior is correct?"* None is uniquely correct. Use weakly informative priors, check them with prior predictive simulations, and report sensitivity.
  - *"Is a credible interval the same as a confidence interval?"* Often similar numerically with weak priors and enough data, but only the credible interval means "95% probability that the parameter is in here".
  - *"Is the brain Bayesian, then?"* That is a different question (Week 15). This week Bayes is a tool for the scientist.

<div dir="rtl">

- **grid چهارنقطه‌ای را روی تخته انجام دهید** (مثال حل‌شده، بخش 1) با ستون‌هایی برای prior، درست‌نمایی، حاصل‌ضرب و posterior. کل استنباط بیزی در همین یک جدول است. بعد prior را به (0.1، 0.1، 0.4، 0.4) تغییر دهید و زنده دوباره حساب کنید: دانشجوها اثر prior را می‌بینند.
- **از داستان شمارش‌های ساختگی Beta استفاده کنید.** «prior برابر Beta(2, 2) مثل این است که قبلاً 2 یادآوری و 2 شکست دیده باشیم.» دانشجوهایی که prior را دلبخواهی می‌دانند، وقتی آن را داده‌ی خیالی ببینند آرام می‌شوند.
- **مستقیماً به نگرانی «ذهنی بودن» جواب دهید.** هر تحلیلی فرض دارد (درست‌نمایی هم یک فرض است)؛ تحلیل بیزی یکی دیگر از فرض‌ها را صریح می‌کند، و تحلیل حساسیت (هفته‌ی 10) بررسی می‌کند که چقدر مهم است.
- **سؤال‌های رایج.**
  - *«کدام prior درست است؟»* هیچ‌کدام تنها جواب درست نیست. از priorهای weakly informative استفاده کنید، آن‌ها را با شبیه‌سازی پیش‌بینی پیشین بررسی کنید و حساسیت را گزارش کنید.
  - *«آیا credible interval همان بازه‌ی اطمینان است؟»* با prior ضعیف و داده‌ی کافی اغلب از نظر عددی شبیه‌اند، ولی فقط credible interval یعنی «با احتمال 95% پارامتر اینجاست».
  - *«پس مغز بیزی است؟»* این سؤال دیگری است (هفته‌ی 15). این هفته بیز ابزاری برای پژوهشگر است.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: a four-point grid by hand · بخش 1: یک شبکه‌ی چهارنقطه‌ای با دست

A participant recalls $y = 7$ of $n = 10$ items. To keep the arithmetic simple, suppose $\theta$ can only take the values 0.2, 0.4, 0.6 or 0.8, each with prior probability 1/4.

<div dir="rtl">

یک شرکت‌کننده $y = 7$ از $n = 10$ آیتم را به یاد می‌آورد. برای ساده نگه داشتن حساب، فرض کنید $\theta$ فقط می‌تواند مقادیر 0.2، 0.4، 0.6 یا 0.8 را بگیرد، هرکدام با احتمال پیشین 1/4.

</div>

| $\theta$ | Prior | Likelihood $\theta^7(1-\theta)^3$ (constant dropped) | Prior × likelihood | Posterior |
|---|---|---|---|---|
| 0.2 | 0.25 | 0.0000066 | 0.0000016 | **0.002** |
| 0.4 | 0.25 | 0.0003539 | 0.0000885 | **0.092** |
| 0.6 | 0.25 | 0.0017916 | 0.0004479 | **0.468** |
| 0.8 | 0.25 | 0.0016777 | 0.0004194 | **0.438** |
| Sum | 1 | | 0.0009574 | 1.000 |

<div dir="rtl">

| $\theta$ | پیشین | درست‌نمایی $\theta^7(1-\theta)^3$ (بدون ثابت) | پیشین × درست‌نمایی | پسین |
|---|---|---|---|---|
| 0.2 | 0.25 | 0.0000066 | 0.0000016 | **0.002** |
| 0.4 | 0.25 | 0.0003539 | 0.0000885 | **0.092** |
| 0.6 | 0.25 | 0.0017916 | 0.0004479 | **0.468** |
| 0.8 | 0.25 | 0.0016777 | 0.0004194 | **0.438** |
| جمع | 1 | | 0.0009574 | 1.000 |

</div>

Each posterior value = (prior × likelihood) / sum. The binomial coefficient was dropped because it cancels in the normalization. Interpretation: after the data, 0.6 and 0.8 are about equally plausible, and 0.2 is practically excluded.

<div dir="rtl">

هر مقدار پسین = (پیشین × درست‌نمایی) / جمع. ضریب دوجمله‌ای حذف شد چون در نرمال‌سازی ساده می‌شود. تفسیر: بعد از داده، 0.6 و 0.8 تقریباً به یک اندازه محتمل‌اند و 0.2 عملاً کنار گذاشته شده است.

</div>

### Part 2: the same data with a continuous Beta prior · بخش 2: همان داده با یک پیشین Beta پیوسته

Prior $\mathrm{Beta}(2, 2)$ (mean 0.5, mildly favoring moderate values). Posterior: $\mathrm{Beta}(2 + 7, 2 + 3) = \mathrm{Beta}(9, 5)$.

<div dir="rtl">

پیشین $\mathrm{Beta}(2, 2)$ (میانگین 0.5، با ترجیح ملایم برای مقادیر میانی). پسین: $\mathrm{Beta}(2 + 7, 2 + 3) = \mathrm{Beta}(9, 5)$.

</div>

- Posterior mean $= 9/14 = 0.643$: between the prior mean (0.5) and the observed proportion (0.7), closer to the data because $n = 10 > a_0 + b_0 = 4$.
- MAP (mode) $= (9 - 1)/(9 + 5 - 2) = 0.667$.
- 95% equal-tailed credible interval $= [0.386, 0.861]$.

<div dir="rtl">

- میانگین پسین $= 9/14 = 0.643$: بین میانگین پیشین (0.5) و نسبت مشاهده‌شده (0.7)، نزدیک‌تر به داده چون $n = 10 > a_0 + b_0 = 4$.
- MAP (مُد) $= (9 - 1)/(9 + 5 - 2) = 0.667$.
- credible interval دم‌برابر 95% $= [0.386, 0.861]$.

</div>

**Interpretation.** Given a mild prior and 10 items, the recall probability is probably around 0.64, but anything from about 0.39 to 0.86 remains credible. Ten items tell us little.

<div dir="rtl">

**تفسیر.** با یک پیشین ملایم و 10 آیتم، احتمال یادآوری احتمالاً حدود 0.64 است، ولی هر مقداری از حدود 0.39 تا 0.86 هنوز credible است. ده آیتم چیز زیادی به ما نمی‌گوید.

</div>

### Part 3: the prior matters less with more data · بخش 3: با داده‌ی بیشتر پیشین کمتر مهم است

With $y = 30$ of $n = 50$:

<div dir="rtl">

با $y = 30$ از $n = 50$:

</div>

| Prior | Posterior | Mean | 95% credible interval |
|---|---|---|---|
| $\mathrm{Beta}(1,1)$ (flat) | $\mathrm{Beta}(31, 21)$ | 0.596 | [0.461, 0.724] |
| $\mathrm{Beta}(0.5, 0.5)$ (Jeffreys) | $\mathrm{Beta}(30.5, 20.5)$ | 0.598 | [0.462, 0.727] |
| $\mathrm{Beta}(20, 5)$ (informative, "≈ 0.8") | $\mathrm{Beta}(50, 25)$ | 0.667 | [0.557, 0.768] |

<div dir="rtl">

| پیشین | پسین | میانگین | credible interval 95% |
|---|---|---|---|
| $\mathrm{Beta}(1,1)$ (تخت) | $\mathrm{Beta}(31, 21)$ | 0.596 | [0.461, 0.724] |
| $\mathrm{Beta}(0.5, 0.5)$ (Jeffreys) | $\mathrm{Beta}(30.5, 20.5)$ | 0.598 | [0.462, 0.727] |
| $\mathrm{Beta}(20, 5)$ (آگاهی‌بخش، «≈ 0.8») | $\mathrm{Beta}(50, 25)$ | 0.667 | [0.557, 0.768] |

</div>

The flat and Jeffreys priors give practically the same answer, also equal to the Week 5 profile-likelihood interval [0.462, 0.728]. The informative prior, which is worth 25 pseudo-observations, still pulls the estimate noticeably toward 0.8: 50 observations are not enough to overwhelm a strong prior. Whether that is good depends on whether the prior knowledge was right.

<div dir="rtl">

پیشین‌های تخت و Jeffreys عملاً یک جواب می‌دهند که با بازه‌ی profile likelihood هفته‌ی 5، [0.462, 0.728]، هم برابر است. پیشین آگاهی‌بخش، که ارزشش 25 مشاهده‌ی کاذب است، هنوز برآورد را به‌طور قابل توجهی به سمت 0.8 می‌کشد: 50 مشاهده برای غلبه بر یک پیشین قوی کافی نیست. اینکه این خوب است یا نه به درست بودن دانش پیشین بستگی دارد.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Compute beta-binomial posteriors analytically and by grid approximation, and see the prior–data compromise.
2. Watch the posterior sharpen with data (sequential updating).
3. Compute a 2-D grid posterior for SDT ($d'$, $c$); summarize it with means, HDIs and posterior probabilities.
4. Use prior predictive simulation to expose a bad "vague" prior.

<div dir="rtl">

1. محاسبه‌ی پسین‌های beta-binomial به‌صورت تحلیلی و با تقریب شبکه‌ای، و دیدن مصالحه‌ی پیشین و داده.
2. تماشای تیزتر شدن پسین با داده (به‌روزرسانی ترتیبی).
3. محاسبه‌ی پسین شبکه‌ای دوبعدی برای SDT ($d'$، $c$)؛ خلاصه کردن آن با میانگین‌ها، HDIها و احتمال‌های پسین.
4. استفاده از شبیه‌سازی پیش‌بینی پیشین برای افشای یک پیشین «مبهم» بد.

</div>

**Timing:** Part A 25 min · Part B 15 min · Part C 40 min · Part D 25 min · Part E 15 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 25 دقیقه · بخش B 15 دقیقه · بخش C 40 دقیقه · بخش D 25 دقیقه · بخش E 15 دقیقه.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week09.py`](code/week09.py), cell 1 · سلول 1

### Part A: beta-binomial, analytically and on a grid (25 min) · بخش A: beta-binomial، تحلیلی و روی شبکه (25 دقیقه)

> **Code · کد:** [`code/week09.py`](code/week09.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
flat Beta(1,1)           grid mean = 0.5962, exact mean = 0.5962, 95% CI = [0.461 0.724]
Jeffreys Beta(.5,.5)     grid mean = 0.5980, exact mean = 0.5980, 95% CI = [0.462 0.727]
informative Beta(20,5)   grid mean = 0.6667, exact mean = 0.6667, 95% CI = [0.557 0.768]
```

The grid and exact posteriors coincide. Look at where each posterior sits relative to its prior and the likelihood.

<div dir="rtl">

پسین‌های شبکه‌ای و دقیق بر هم منطبق‌اند. ببینید هر پسین نسبت به پیشین و درست‌نمایی خودش کجا قرار می‌گیرد.

</div>

### Part B: sequential updating (15 min) · بخش B: به‌روزرسانی ترتیبی (15 دقیقه)

> **Code · کد:** [`code/week09.py`](code/week09.py), cell 3 · سلول 3

**What to notice:** the posterior starts as the prior, narrows as items accumulate, and concentrates around the true value. Its width shrinks roughly like $1/\sqrt{n}$, as the SE did in Week 5.

<div dir="rtl">

**به این دقت کنید:** پسین از خود پیشین شروع می‌شود، با جمع شدن آیتم‌ها باریک می‌شود و حول مقدار واقعی متمرکز می‌شود. پهنایش تقریباً مثل $1/\sqrt{n}$ کم می‌شود، همان‌طور که SE در هفته‌ی 5 کم می‌شد.

</div>

### Part C: a two-parameter grid posterior for SDT (40 min) · بخش C: یک پسین شبکه‌ای دوپارامتری برای SDT (40 دقیقه)

The Week 2 participant: 68 hits out of 100 signal trials and 11 false alarms out of 100 noise trials. Priors: $d' \sim \mathcal{N}(1, 1.5)$ (sensitivity is usually positive, rarely above 4) and $c \sim \mathcal{N}(0, 1)$ (bias is usually modest).

<div dir="rtl">

شرکت‌کننده‌ی هفته‌ی 2: 68 hit از 100 trial علامت و 11 false alarm از 100 trial نویز. پیشین‌ها: $d' \sim \mathcal{N}(1, 1.5)$ (حساسیت معمولاً مثبت و به‌ندرت بالای 4 است) و $c \sim \mathcal{N}(0, 1)$ (سوگیری معمولاً متوسط است).

</div>

> **Code · کد:** [`code/week09.py`](code/week09.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
    post. mean  post. SD    MAP  95% HDI low  95% HDI high
d'       1.688     0.209  1.675        1.250         2.062
c        0.376     0.106  0.375        0.163         0.575
MLE (uncorrected formulas): d' = 1.694, c = 0.379
P(d' > 1 | data) = 1.000;  P(c > 0 | data) = 1.000
Posterior correlation of d' and c: 0.245
```

("1.000" means that none of the 20 000 posterior samples fell below the threshold, so the probability is > 0.9999. Report it as such, not as certainty.)

<div dir="rtl">

(«1.000» یعنی هیچ‌کدام از 20 000 نمونه‌ی پسین زیر آستانه نیفتادند، پس احتمال > 0.9999 است. آن را همین‌طور گزارش کنید، نه به‌عنوان قطعیت.)

</div>

**Interpret (write in your notebook):**
1. How do the posterior mean and MAP compare with the MLE? Why are they so close here?
2. Translate the HDI for $d'$ and $P(c > 0 \mid \text{data})$ into one plain-language sentence each about this participant.
3. Increase the prior SD on $d'$ to 10, then decrease it to 0.3 (centered at 1). Which summaries change, and by how much?

<div dir="rtl">

**تفسیر (در notebook بنویسید):**
1. میانگین پسین و MAP در مقایسه با MLE چطورند؟ چرا اینجا این‌قدر نزدیک‌اند؟
2. HDI مربوط به $d'$ و $P(c > 0 \mid \text{data})$ را هرکدام به یک جمله‌ی ساده درباره‌ی این شرکت‌کننده ترجمه کنید.
3. انحراف معیار پیشین $d'$ را به 10 افزایش دهید، بعد به 0.3 کم کنید (با مرکز 1). کدام خلاصه‌ها تغییر می‌کنند و چقدر؟

</div>

### Part D: prior predictive checks (25 min) · بخش D: بررسی‌های پیش‌بینی پیشین (25 دقیقه)

Before trusting a prior, look at the data it implies. Compare our prior with a "vague" one, $d' \sim \mathcal{N}(0, 10)$ and $c \sim \mathcal{N}(0, 10)$, which is sometimes used because it is "uninformative".

<div dir="rtl">

پیش از اعتماد به یک پیشین، به داده‌هایی که نتیجه می‌دهد نگاه کنید. پیشین ما را با یک پیشین «مبهم»، $d' \sim \mathcal{N}(0, 10)$ و $c \sim \mathcal{N}(0, 10)$، مقایسه کنید که گاهی به این دلیل استفاده می‌شود که «بی‌اطلاع» است.

</div>

> **Code · کد:** [`code/week09.py`](code/week09.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
our prior: d'~N(1,1.5), c~N(0,1): 14% of simulated datasets have a rate of exactly 0 or 1; 24% have H < F
'vague' prior: d'~N(0,10), c~N(0,10): 96% of simulated datasets have a rate of exactly 0 or 1; 23% have H < F
```

**What to notice:** the "vague" prior is not neutral at all. On the probability scale it puts 96% of simulated datasets at hit or false-alarm rates of exactly 0 or 1, which practically never happens in real detection experiments. It expresses a strong and absurd belief about the data. Vagueness on the parameter scale is not vagueness on the data scale.

<div dir="rtl">

**به این دقت کنید:** پیشین «مبهم» اصلاً خنثی نیست. روی مقیاس احتمال، 96% مجموعه‌داده‌های شبیه‌سازی‌شده را در نرخ hit یا false alarm دقیقاً 0 یا 1 قرار می‌دهد؛ چیزی که در آزمایش‌های تشخیص واقعی عملاً هرگز اتفاق نمی‌افتد. این پیشین باوری قوی و پوچ درباره‌ی داده بیان می‌کند. ابهام روی مقیاس پارامتر، ابهام روی مقیاس داده نیست.

</div>

Our own prior is not perfect either: about a quarter of its simulated datasets have $H < F$, because $\mathcal{N}(1, 1.5)$ puts about 25% of its mass on negative $d'$. For a task where participants are known to be above chance, a prior restricted to $d' > 0$ (e.g., a half-normal or a Gamma) would be more defensible. Try it, and check whether it changes the posterior for this participant. (Hint: with 200 informative trials, hardly at all.)

<div dir="rtl">

پیشین خود ما هم کامل نیست: حدود یک‌چهارم مجموعه‌داده‌های شبیه‌سازی‌شده‌اش $H < F$ دارند، چون $\mathcal{N}(1, 1.5)$ حدود 25% جرمش را روی $d'$ منفی می‌گذارد. برای تکلیفی که می‌دانیم شرکت‌کننده‌ها بالاتر از شانس عمل می‌کنند، پیشینی محدود به $d' > 0$ (مثلاً نیم‌نرمال یا Gamma) قابل دفاع‌تر است. امتحانش کنید و ببینید آیا پسین این شرکت‌کننده را تغییر می‌دهد. (راهنمایی: با 200 trial آگاهی‌بخش، تقریباً نه.)

</div>

### Part E: interpret (15 min) · بخش E: تفسیر (15 دقیقه)

Write a short "results paragraph" (4–6 sentences) for this participant as it would appear in a paper. Report the priors, the posterior means and 95% HDIs for $d'$ and $c$, $P(d' > 1 \mid \text{data})$, and one sentence on prior sensitivity (from Part C, question 3).

<div dir="rtl">

یک «پاراگراف نتایج» کوتاه (4 تا 6 جمله) برای این شرکت‌کننده بنویسید، طوری که در یک مقاله می‌آید. پیشین‌ها، میانگین‌های پسین و HDIهای 95% برای $d'$ و $c$، $P(d' > 1 \mid \text{data})$، و یک جمله درباره‌ی حساسیت به پیشین (از سؤال 3 بخش C) را گزارش کنید.

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Show algebraically that the posterior mean of the beta-binomial model is a weighted average of the prior mean and $y/n$. What are the weights?

<div dir="rtl">

**تمرین 1 ★.** به‌صورت جبری نشان دهید که میانگین پسین مدل beta-binomial میانگین وزنی میانگین پیشین و $y/n$ است. وزن‌ها چیستند؟

</div>

**Exercise 2 ★.** Using the Part A grid, compute the 95% HDI and the equal-tailed interval for $\mathrm{Beta}(1 + 2, 1 + 18)$ (2 successes out of 20). Why do they differ?

<div dir="rtl">

**تمرین 2 ★.** با شبکه‌ی بخش A، HDI 95% و بازه‌ی دم‌برابر را برای $\mathrm{Beta}(1 + 2, 1 + 18)$ (2 موفقیت از 20) حساب کنید. چرا با هم فرق دارند؟

</div>

**Exercise 3 ★★ (forgetting by grid).** Compute the grid posterior of $(A, d)$ for the power forgetting model with the Week 2 data, using priors $A \sim \mathrm{Beta}(8, 2)$ and $d \sim \mathrm{Gamma}(\text{shape } 2, \text{scale } 0.3)$. Compare the posterior means and 95% HDIs with the MLE and the Week 5 profile and bootstrap intervals.

<div dir="rtl">

**تمرین 3 ★★ (فراموشی با شبکه).** پسین شبکه‌ای $(A, d)$ را برای مدل فراموشی توانی با داده‌های هفته‌ی 2، با پیشین‌های $A \sim \mathrm{Beta}(8, 2)$ و $d \sim \mathrm{Gamma}(\text{shape } 2, \text{scale } 0.3)$ حساب کنید. میانگین‌های پسین و HDIهای 95% را با MLE و بازه‌های profile و bootstrap هفته‌ی 5 مقایسه کنید.

</div>

**Exercise 4 ★★ (equivalence of MAP and MLE).** In Part C, replace both priors by flat priors over the grid. Show that the MAP equals the MLE. Why is the posterior *mean* still slightly different?

<div dir="rtl">

**تمرین 4 ★★ (هم‌ارزی MAP و MLE).** در بخش C هر دو پیشین را با پیشین‌های تخت روی شبکه جایگزین کنید. نشان دهید MAP برابر MLE است. چرا *میانگین* پسین هنوز کمی فرق دارد؟

</div>

**Exercise 5 ★★★ (Advanced: sequential vs. batch).** For the SDT model, update the grid posterior trial by trial (each trial's posterior becomes the next trial's prior) through 200 simulated trials, and show that the final posterior is identical (up to numerical error) to the batch posterior from all trials at once. Plot the posterior SD of $d'$ against the number of trials.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: ترتیبی در برابر یکجا).** برای مدل SDT، پسین شبکه‌ای را trial به trial (پسین هر trial پیشین trial بعدی است) برای 200 trial شبیه‌سازی‌شده به‌روز کنید و نشان دهید پسین نهایی (تا حد خطای عددی) با پسین یکجای همه‌ی trialها یکی است. انحراف معیار پسین $d'$ را در برابر تعداد trialها رسم کنید.

</div>

### Lab check-off · lab check-off

Show: (1) the three-panel prior/likelihood/posterior plot from Part A, (2) the SDT summary table and joint posterior from Part C, and (3) the two prior predictive plots from Part D with one sentence on what is wrong with the vague prior.

<div dir="rtl">

نشان دهید: (1) نمودار سه‌قسمتی پیشین/درست‌نمایی/پسین از بخش A، (2) جدول خلاصه‌ی SDT و پسین مشترک از بخش C، و (3) دو نمودار پیش‌بینی پیشین از بخش D با یک جمله درباره‌ی اینکه پیشین مبهم چه مشکلی دارد.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**How good is the model, really? A Bayesian answer for small evaluations.** Researchers often test an LLM on a small set of items, for example 25 hand-written problems. The beta-binomial model of this week gives what such studies usually lack: a full posterior for the accuracy, direct probability statements ("the probability that accuracy exceeds 60%"), and a direct comparison of two models.

<div dir="rtl">

**مدل واقعاً چقدر خوب است؟ یک جواب بیزی برای ارزیابی‌های کوچک.** پژوهشگرها اغلب یک LLM را روی مجموعه‌ی کوچکی از آیتم‌ها، مثلاً 25 مسئله‌ی دست‌نویس، می‌آزمایند. مدل beta-binomial این هفته همان چیزی را می‌دهد که چنین مطالعه‌هایی معمولاً ندارند: یک پسین کامل برای دقت، گزاره‌های احتمالی مستقیم («احتمال اینکه دقت از 60% بیشتر باشد») و مقایسه‌ی مستقیم دو مدل.

</div>

> **Code · کد:** [`code/week09.py`](code/week09.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Model A: posterior mean = 0.704, 95% interval = [0.522, 0.857], P(accuracy > 0.6) = 0.878
Model B: posterior mean = 0.593, 95% interval = [0.406, 0.766], P(accuracy > 0.6) = 0.479
P(A more accurate than B | data) = 0.807
```

With 25 items, the posterior intervals are about 0.35 wide, and there is a 19% posterior probability that B is actually the better model.

<div dir="rtl">

با 25 آیتم، پهنای بازه‌های پسین حدود 0.35 است، و احتمال پسین 19% وجود دارد که در واقع B مدل بهتر باشد.

</div>

**Try it (no API needed).**
- ★ Use an informative prior from an earlier, larger evaluation (e.g., Beta(14, 6) for model A). How much do the conclusions change?
- ★★ The comparison above treats the two models as independent, although they answered the same items. Why is this a problem (see the Week 5 box)? Sketch a model that respects the pairing.
- ★★ Discussion: what prior would you use for the accuracy of a brand-new model on a four-choice test, and why should it not put much mass below 0.25?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ یک پیشین آگاهی‌بخش از یک ارزیابی قبلی و بزرگ‌تر استفاده کنید (مثلاً Beta(14, 6) برای مدل A). نتیجه‌گیری‌ها چقدر عوض می‌شوند؟
- ★★ مقایسه‌ی بالا دو مدل را مستقل در نظر می‌گیرد، با اینکه به همان آیتم‌ها جواب داده‌اند. چرا این مشکل است (کادر هفته‌ی 5 را ببینید)؟ طرح کلی مدلی را بکشید که جفت بودن را رعایت کند.
- ★★ بحث: برای دقت یک مدل کاملاً تازه روی یک آزمون چهارگزینه‌ای چه پیشینی استفاده می‌کنید، و چرا نباید جرم زیادی زیر 0.25 بگذارد؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **"The prior makes Bayesian inference subjective, so the results are arbitrary."** Priors are explicit assumptions, just like the choice of likelihood. Report them, justify them, and check sensitivity. With adequate data, reasonable priors lead to similar conclusions.
2. **"Flat or very wide priors are uninformative."** They can be strongly informative on the data scale (Part D). Use weakly informative priors and check them with prior predictive simulation.
3. **Choosing the prior after looking at the data.** That uses the data twice.
4. **Multiplying probabilities on a grid without logs,** which causes underflow (Week 4). Work with log-prior + log-likelihood, then subtract the maximum before exponentiating.
5. **Too coarse or too narrow a grid.** If the posterior is cut off at the grid edge, all summaries are wrong. Check that the posterior is near zero at the edges.
6. **Reading a credible interval as a confidence interval, or vice versa.** Only the credible interval supports "95% probability the parameter is in here" (given the model and prior).
7. **Reporting only the MAP.** The point of the posterior is the whole distribution. Report a central value *and* an interval, and probabilities for the hypotheses you care about.

<div dir="rtl">

1. **«پیشین استنباط بیزی را ذهنی و نتایج را دلبخواهی می‌کند.»** پیشین‌ها فرض‌های صریح‌اند، درست مثل انتخاب درست‌نمایی. گزارششان کنید، توجیهشان کنید و حساسیت را بررسی کنید. با داده‌ی کافی، پیشین‌های معقول به نتیجه‌گیری‌های مشابه می‌رسند.
2. **«پیشین‌های تخت یا خیلی پهن بی‌اطلاع‌اند.»** می‌توانند روی مقیاس داده به‌شدت آگاهی‌بخش باشند (بخش D). از پیشین‌های ضعیف‌آگاهی‌بخش استفاده کنید و با شبیه‌سازی پیش‌بینی پیشین بررسی‌شان کنید.
3. **انتخاب پیشین بعد از نگاه کردن به داده.** این یعنی دو بار استفاده از داده.
4. **ضرب احتمال‌ها روی شبکه بدون لگاریتم،** که سرریز می‌کند (هفته‌ی 4). با لگاریتم پیشین + لگاریتم درست‌نمایی کار کنید و پیش از نمایی گرفتن بیشینه را کم کنید.
5. **شبکه‌ی خیلی درشت یا خیلی باریک.** اگر پسین در لبه‌ی شبکه بریده شود، همه‌ی خلاصه‌ها غلط‌اند. بررسی کنید که پسین در لبه‌ها نزدیک صفر باشد.
6. **خواندن credible interval به جای بازه‌ی اطمینان یا برعکس.** فقط credible interval جمله‌ی «با احتمال 95% پارامتر اینجاست» (با توجه به مدل و پیشین) را پشتیبانی می‌کند.
7. **فقط گزارش MAP.** نکته‌ی پسین کل توزیع است. یک مقدار مرکزی *و* یک بازه، و احتمال فرضیه‌هایی را که برایتان مهم‌اند گزارش کنید.

</div>

---

## Check your understanding · خودآزمایی

**1.** Write Bayes' rule for a parameter $\theta$ and name each term.
<details><summary>Answer</summary>
$p(\theta\mid y) = p(y\mid\theta)p(\theta)/p(y)$: posterior = likelihood × prior / evidence (marginal likelihood). For estimation, $p(\theta\mid y) \propto p(y\mid\theta)p(\theta)$.
</details>

<div dir="rtl">

**1.** قاعده‌ی بیز را برای پارامتر $\theta$ بنویسید و هر جمله را نام ببرید.
<details><summary>پاسخ</summary>
$p(\theta\mid y) = p(y\mid\theta)p(\theta)/p(y)$: پسین = درست‌نمایی × پیشین / شواهد (marginal likelihood). برای برآورد، $p(\theta\mid y) \propto p(y\mid\theta)p(\theta)$.
</details>

</div>

**2.** Prior $\mathrm{Beta}(3, 3)$, data: 12 recalled out of 20. What is the posterior, and its mean?
<details><summary>Answer</summary>
$\mathrm{Beta}(3 + 12, 3 + 8) = \mathrm{Beta}(15, 11)$, with mean $15/26 = 0.577$.
</details>

<div dir="rtl">

**2.** پیشین $\mathrm{Beta}(3, 3)$، داده: 12 یادآوری از 20. پسین و میانگینش چیست؟
<details><summary>پاسخ</summary>
$\mathrm{Beta}(3 + 12, 3 + 8) = \mathrm{Beta}(15, 11)$، با میانگین $15/26 = 0.577$.
</details>

</div>

**3.** Why does the posterior get closer to the MLE as $n$ increases?
<details><summary>Answer</summary>
The log-likelihood is a sum over observations and grows with $n$, while the log-prior stays fixed. With much data the likelihood dominates the product, and the posterior concentrates around the likelihood's maximum.
</details>

<div dir="rtl">

**3.** چرا با افزایش $n$ پسین به MLE نزدیک‌تر می‌شود؟
<details><summary>پاسخ</summary>
لگاریتم درست‌نمایی مجموعی روی مشاهدات است و با $n$ بزرگ می‌شود، در حالی که لگاریتم پیشین ثابت می‌ماند. با داده‌ی زیاد درست‌نمایی بر حاصل‌ضرب غالب می‌شود و پسین حول بیشینه‌ی درست‌نمایی متمرکز می‌شود.
</details>

</div>

**4.** What is the difference between a 95% HDI and a 95% equal-tailed interval? When do they coincide?
<details><summary>Answer</summary>
The HDI is the narrowest interval containing 95% of the posterior mass, and every value inside has higher density than any value outside. The equal-tailed interval cuts 2.5% from each tail. They coincide for symmetric unimodal posteriors and differ for skewed ones.
</details>

<div dir="rtl">

**4.** تفاوت HDI 95% و بازه‌ی دم‌برابر 95% چیست؟ کی بر هم منطبق‌اند؟
<details><summary>پاسخ</summary>
HDI باریک‌ترین بازه‌ای است که 95% جرم پسین را در بر دارد و هر مقدار داخلش چگالی بیشتری از هر مقدار بیرونش دارد. بازه‌ی دم‌برابر از هر دم 2.5% را می‌بُرد. برای پسین‌های متقارن تک‌مُدی بر هم منطبق‌اند و برای پسین‌های چوله فرق دارند.
</details>

</div>

**5.** Why does grid approximation become impractical for models with many parameters?
<details><summary>Answer</summary>
The number of grid points grows exponentially with the number of parameters (e.g., 100 points per parameter means $100^k$ evaluations). That is the curse of dimensionality. MCMC sampling (Weeks 11–13) avoids it.
</details>

<div dir="rtl">

**5.** چرا تقریب شبکه‌ای برای مدل‌هایی با پارامترهای زیاد غیرعملی می‌شود؟
<details><summary>پاسخ</summary>
تعداد نقاط شبکه با تعداد پارامترها به‌طور نمایی رشد می‌کند (مثلاً 100 نقطه برای هر پارامتر یعنی $100^k$ ارزیابی). این نفرین ابعاد است. نمونه‌گیری MCMC (هفته‌های 11–13) از آن دوری می‌کند.
</details>

</div>

**6.** A colleague uses $d' \sim \mathcal{N}(0, 100)$ "to be safe". What would you do to convince them it is a bad idea?
<details><summary>Answer</summary>
A prior predictive simulation: show that this prior implies hit and false-alarm rates that are almost always exactly 0 or 1, an absurd belief about real detection data. Suggest a weakly informative prior instead.
</details>

<div dir="rtl">

**6.** همکاری «برای احتیاط» از $d' \sim \mathcal{N}(0, 100)$ استفاده می‌کند. برای قانع کردنش که این ایده‌ی بدی است چه می‌کنید؟
<details><summary>پاسخ</summary>
یک شبیه‌سازی پیش‌بینی پیشین: نشان دهید این پیشین نرخ‌های hit و false alarmی نتیجه می‌دهد که تقریباً همیشه دقیقاً 0 یا 1 هستند؛ باوری پوچ درباره‌ی داده‌ی تشخیص واقعی. به‌جایش یک پیشین ضعیف‌آگاهی‌بخش پیشنهاد کنید.
</details>

</div>

**7.** Explain the statement "the log-linear correction for extreme rates is a Bayesian estimate".
<details><summary>Answer</summary>
The corrected rate $(y + 0.5)/(n + 1)$ equals the posterior mean of $\theta$ under a $\mathrm{Beta}(0.5, 0.5)$ prior: $(0.5 + y)/(0.5 + 0.5 + n)$. The correction implicitly adds half a pseudo-observation of each type.
</details>

<div dir="rtl">

**7.** این جمله را توضیح دهید: «تصحیح log-linear برای نرخ‌های حدی یک برآورد بیزی است».
<details><summary>پاسخ</summary>
نرخ تصحیح‌شده‌ی $(y + 0.5)/(n + 1)$ برابر میانگین پسین $\theta$ تحت پیشین $\mathrm{Beta}(0.5, 0.5)$ است: $(0.5 + y)/(0.5 + 0.5 + n)$. این تصحیح به‌طور ضمنی از هر نوع نیم مشاهده‌ی کاذب اضافه می‌کند.
</details>

</div>

---

## Assignment · تکلیف

- **A3 (model comparison and recovery)** and the **project proposal** are due at the start of this week's lecture.
- No new graded assignment this week. **A4 (Bayesian analysis by grid)** is released in Week 10.
- **Optional practice (ungraded):** lab Exercise 3 (forgetting by grid) is the core of A4. Starting it now will save you time.

<div dir="rtl">

- **A3 (مقایسه و بازیابی مدل)** و **پیشنهاد پروژه** در ابتدای درس این هفته تحویل داده می‌شوند.
- این هفته تکلیف نمره‌دار جدیدی نداریم. **A4 (تحلیل بیزی با شبکه)** در هفته‌ی 10 منتشر می‌شود.
- **تمرین اختیاری (بدون نمره):** تمرین 3 lab (فراموشی با شبکه) هسته‌ی A4 است. اگر الان شروعش کنید در وقتتان صرفه‌جویی می‌شود.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Kruschke (2014), chapters 5–6.** Bayes' rule, and inferring a binomial probability via exact mathematical analysis (the beta-binomial model). Very gentle and visual. *(Main reading.)*
- **Lee & Wagenmakers (2014), chapters 1 and 3.** The basics of Bayesian analysis, and inferences with binomials.
- **Martin, Kumar & Lao (2021), chapter 1.** Bayesian inference: the components of a Bayesian model and prior/posterior predictive distributions, with Python code.
- **Farrell & Lewandowsky (2018), chapter 6.** Bayesian parameter estimation: basic concepts, linked to the likelihood framework of Week 4.
- **Azimifar & Ahmadi (1396)**, vol. 1 (in Persian): the section on Bayesian parameter estimation and its relation to ML estimation [verify chapter].

<div dir="rtl">

- **Kruschke (2014)، فصل‌های 5–6.** قاعده‌ی بیز، و استنباط یک احتمال دوجمله‌ای با تحلیل ریاضی دقیق (مدل beta-binomial). خیلی ساده و تصویری. *(منبع اصلی.)*
- **Lee & Wagenmakers (2014)، فصل‌های 1 و 3.** مبانی تحلیل بیزی، و استنباط با توزیع دوجمله‌ای.
- **Martin, Kumar & Lao (2021)، فصل 1.** استنباط بیزی: اجزای یک مدل بیزی و توزیع‌های پیش‌بینی پیشین/پسین، همراه با کد Python.
- **Farrell & Lewandowsky (2018)، فصل 6.** برآورد بیزی پارامتر: مفاهیم پایه، مرتبط با چارچوب درست‌نمایی هفته‌ی 4.
- **عظیمی‌فر و احمدی (1396)**، جلد 1: بخش برآورد بیزی پارامتر و ارتباطش با برآورد ML [شماره‌ی فصل بررسی شود].

</div>

*Preview for Week 10:* the posterior tells us about parameters *within* a model. Next week we ask how the data change our belief *between* models, using the evidence $p(\mathbf{y}\mid\mathcal{M})$ that we have been ignoring as a normalizing constant, and how to check whether a model's posterior predictions look like the real data.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 10:* پسین درباره‌ی پارامترها *درون* یک مدل حرف می‌زند. هفته‌ی بعد می‌پرسیم داده‌ها باور ما را *بین* مدل‌ها چطور تغییر می‌دهند، با استفاده از شواهد $p(\mathbf{y}\mid\mathcal{M})$ که تا حالا به‌عنوان ثابت نرمال‌ساز نادیده‌اش گرفته‌ایم، و چطور بررسی کنیم که پیش‌بینی‌های پسین یک مدل شبیه داده‌ی واقعی هستند یا نه.

</div>
