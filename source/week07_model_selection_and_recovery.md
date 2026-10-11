# Week 7: Evaluating Models II: Information Criteria, Parameter Recovery and Model Recovery · هفته‌ی 7: ارزیابی مدل‌ها 2: معیارهای اطلاعاتی، بازیابی پارامتر و بازیابی مدل

> **Chapter 3: Evaluation of cognitive models** · Lecture 1 h · Lab 2 h
> **Running data:** the Week 2–6 forgetting data and models, plus large simulation studies at the same design.

<div dir="rtl">

> **فصل 3: ارزیابی مدل‌های شناختی** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** داده‌ها و مدل‌های فراموشی هفته‌های 2–6، به‌علاوه‌ی مطالعات شبیه‌سازی بزرگ با همان طرح آزمایش.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| criterion (c) | ملاک | آستانه‌ی تصمیم؛ نشان‌دهنده‌ی سوگیری پاسخ |
| parameter recovery | بازیابی پارامتر | آیا برازش، پارامترهای معلوم شبیه‌سازی را برمی‌گرداند |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| model recovery | بازیابی مدل | آیا مقایسه‌ی مدل، مدل مولد را درست انتخاب می‌کند |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| research design | طرح آزمایش | شرایط، تعداد کوشش‌ها و نمونه‌ها |
| likelihood-ratio test (LRT) | آزمون نسبت درست‌نمایی | مقایسه‌ی دو مدل تودرتو |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| nested models | مدل‌های تودرتو (nested) | یک مدل حالت خاص مدل دیگر است |
| AIC / BIC | معیار اطلاعاتی آکائیکه / بیزی | برازش به‌علاوه‌ی جریمه برای تعداد پارامتر |
| response bias | سوگیری پاسخ | تمایل به یک پاسخ، مستقل از محرک |
| confusion matrix | ماتریس درهم‌ریختگی (confusion matrix) | P(مدل انتخاب‌شده | مدل مولد) |
| inversion matrix | ماتریس معکوس (inversion matrix) | P(مدل مولد | مدل انتخاب‌شده) |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| identifiability | شناسایی‌پذیری | آیا داده پارامترها را به‌طور یکتا تعیین می‌کند |
| parameter trade-off | بده‌بستان پارامترها | تغییر یک پارامتر که با پارامتر دیگر جبران می‌شود |
| log-likelihood / NLL | لگاریتم درست‌نمایی / منفی آن | مقداری که بهینه‌سازها کمینه یا بیشینه می‌کنند |
| Akaike weights | وزن‌های آکائیکه | پشتیبانی نسبی از هر مدل |
| cross-validation (CV) | اعتبارسنجی متقابل (cross-validation) | برازش روی بخشی از داده و آزمون روی بخش کنارگذاشته |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| model mimicry | تقلید مدل | تولید داده‌ای که شبیه داده‌ی مدل دیگر است |
| in-context learning | یادگیری درون‌متنی | یادگیری از مثال‌های داخل prompt |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Conduct** a likelihood-ratio test for nested models and **explain** why it cannot compare non-nested models.
2. **Compute** and **interpret** AIC, AICc, BIC and Akaike/BIC weights, and **explain** the different goals of AIC and BIC.
3. **Design** and **run** a parameter-recovery study, and **diagnose** biased, noisy or traded-off parameters.
4. **Design** and **run** a model-recovery study, and **interpret** the confusion and inversion matrices.
5. **Evaluate** whether a given experimental design and comparison method can support the conclusions a researcher wants to draw.

<div dir="rtl">

1. آزمون نسبت درست‌نمایی را برای مدل‌های nested **انجام دهند** و **توضیح دهند** چرا نمی‌تواند مدل‌های non-nested را مقایسه کند.
2. AIC، AICc، BIC و وزن‌های آکائیکه/BIC را **حساب و تفسیر کنند** و اهداف متفاوت AIC و BIC را **توضیح دهند**.
3. یک مطالعه‌ی بازیابی پارامتر را **طراحی و اجرا کنند** و پارامترهای سوگیر، پرنویز یا دارای trade-off را **تشخیص دهند**.
4. یک مطالعه‌ی بازیابی مدل را **طراحی و اجرا کنند** و ماتریس‌های درهم‌ریختگی و معکوس را **تفسیر کنند**.
5. **ارزیابی کنند** که آیا یک طرح آزمایش و روش مقایسه‌ی مشخص می‌تواند از نتیجه‌گیری‌هایی که پژوهشگر می‌خواهد بگیرد پشتیبانی کند.

</div>

---

## Motivation & big picture · مقدمه

Cross-validation (Week 6) is general but expensive: every fold means refitting, and refitting complex models with multi-start can take hours. **Information criteria** estimate out-of-sample performance from a *single* fit, by adding a complexity penalty to the training fit.

<div dir="rtl">

cross-validation (هفته‌ی 6) کلی ولی پرهزینه است: هر بخش یعنی یک برازش دوباره، و برازش دوباره‌ی مدل‌های پیچیده با multi-start ممکن است ساعت‌ها طول بکشد. **معیارهای اطلاعاتی** عملکرد خارج از نمونه را از یک برازش *واحد* تخمین می‌زنند؛ با افزودن یک جریمه‌ی پیچیدگی به برازش آموزش.

</div>

But there is a more fundamental question that no criterion answers on its own: **can our method even work at this design?** Suppose we conclude "participants forget by a power law, with decay exponent 0.42". Two things must be true for this to mean anything:

<div dir="rtl">

ولی سؤال بنیادی‌تری هست که هیچ معیاری به‌تنهایی به آن جواب نمی‌دهد: **آیا روش ما اصلاً با این طرح آزمایش می‌تواند کار کند؟** فرض کنید نتیجه بگیریم «شرکت‌کننده‌ها با یک قانون توانی با نمای زوال 0.42 فراموش می‌کنند». برای اینکه این حرف معنایی داشته باشد دو چیز باید درست باشد:

</div>

1. If the data had come from a power model with $d = 0.42$, our fitting procedure would have returned something close to 0.42 (**parameter recovery**).
2. If the data had come from an exponential model, our comparison method would have said "exponential", not "power" (**model recovery**).

<div dir="rtl">

1. اگر داده‌ها از یک مدل توانی با $d = 0.42$ آمده بودند، رویه‌ی برازش ما چیزی نزدیک به 0.42 برمی‌گرداند (**بازیابی پارامتر**).
2. اگر داده‌ها از یک مدل نمایی آمده بودند، روش مقایسه‌ی ما می‌گفت «نمایی»، نه «توانی» (**بازیابی مدل**).

</div>

Both can be checked by simulation, because we know the truth for simulated data. Modern guidelines for computational modeling treat these checks as essential; skipping them is like running an experiment without checking that the equipment works. This week completes the "simulate → fit → evaluate → **recover**" part of our pipeline.

<div dir="rtl">

هر دو را می‌شود با شبیه‌سازی بررسی کرد، چون برای داده‌ی شبیه‌سازی‌شده حقیقت را می‌دانیم. راهنماهای امروزی مدل‌سازی محاسباتی این بررسی‌ها را ضروری می‌دانند؛ نادیده گرفتنشان مثل اجرای آزمایش بدون وارسی سالم بودن تجهیزات است. این هفته بخش «شبیه‌سازی ← برازش ← ارزیابی ← **بازیابی**» مسیر مدل‌سازی ما را کامل می‌کند.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Model comparison tables with AIC/BIC** appear in almost every modeling paper in psychology, neuroscience, ecology and economics.
- **Computational psychiatry**: before claiming that patients have a lower learning rate, researchers must show by parameter recovery that the learning rate can be estimated at their design. Reviewers increasingly require this.
- **Designing experiments**: recovery simulations are run *before* collecting data, to choose the number of trials and conditions (a modeling version of power analysis).
- **Any study that says "model X explains the data best"** should report model recovery; otherwise the winner may only reflect a bias of the criterion.

<div dir="rtl">

- **جدول‌های مقایسه‌ی مدل با AIC/BIC** تقریباً در هر مقاله‌ی مدل‌سازی در روان‌شناسی، علوم اعصاب، بوم‌شناسی و اقتصاد دیده می‌شوند.
- **روان‌پزشکی محاسباتی:** پیش از ادعای اینکه بیماران نرخ یادگیری پایین‌تری دارند، پژوهشگرها باید با بازیابی پارامتر نشان دهند که نرخ یادگیری در طرح آزمایش آن‌ها قابل برآورد است. داوران مقاله‌ها روزبه‌روز بیشتر این را می‌خواهند.
- **طراحی آزمایش:** شبیه‌سازی‌های بازیابی *پیش از* جمع‌آوری داده اجرا می‌شوند تا تعداد trialها و شرایط انتخاب شود (نسخه‌ی مدل‌سازی تحلیل توان آماری یا power analysis).
- **هر مطالعه‌ای که می‌گوید «مدل X داده را بهتر از همه توضیح می‌دهد»** باید بازیابی مدل را گزارش کند؛ وگرنه ممکن است برنده فقط سوگیری معیار مقایسه را نشان دهد.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

Cross-validation is honest but slow. **Information criteria** (AIC, BIC) are quick formulas that take the fit of each model and subtract a penalty for every parameter, so that a model only wins if its extra parameters improve the fit by more than they "cost". AIC aims at the best predictor, BIC at the true model, and BIC's penalty is larger. The second, more important half of the week asks whether our methods work at all. We test them on fake data where we *know* the truth. **Parameter recovery**: simulate data with known parameter values, fit, and check that the fitted values come back close to the true ones. **Model recovery**: simulate data from each candidate model and check that the comparison method picks the model that actually generated them. If a method cannot find the truth in simulated data, its answer on real data means nothing.

<div dir="rtl">

cross-validation صادق ولی کند است. **معیارهای اطلاعاتی** (AIC و BIC) فرمول‌های سریعی‌اند که برازش هر مدل را می‌گیرند و برای هر پارامتر یک جریمه کم می‌کنند؛ پس مدلی برنده می‌شود که پارامترهای اضافه‌اش برازش را بیش از «هزینه‌شان» بهتر کنند. هدف AIC بهترین پیش‌بینی‌کننده و هدف BIC مدل درست است، و جریمه‌ی BIC بزرگ‌تر است. نیمه‌ی دوم هفته که مهم‌تر است می‌پرسد آیا روش‌های ما اصلاً کار می‌کنند. آن‌ها را روی داده‌ی ساختگی امتحان می‌کنیم که در آن حقیقت را *می‌دانیم*. **بازیابی پارامتر:** داده را با پارامترهای معلوم شبیه‌سازی کن، برازش کن، و بررسی کن که مقدارهای برازش‌شده نزدیک مقدارهای واقعی برگردند. **بازیابی مدل:** داده را از هر مدل نامزد شبیه‌سازی کن و بررسی کن که روش مقایسه همان مدلی را انتخاب کند که داده را تولید کرده. اگر روشی نتواند حقیقت را در داده‌ی شبیه‌سازی‌شده پیدا کند، جوابش روی داده‌ی واقعی بی‌معناست.

</div>

**Suggested timing (60 min):** likelihood-ratio test 8 · AIC and BIC 20 · parameter recovery 14 · model recovery 14 · identifiability 4.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** آزمون نسبت درست‌نمایی 8 · AIC و BIC 20 · بازیابی پارامتر 14 · بازیابی مدل 14 · identifiability 4.

</div>

### 1. The likelihood-ratio test (nested models) · 1. آزمون نسبت درست‌نمایی (مدل‌های nested)

Model $\mathcal{M}_0$ is **nested** in $\mathcal{M}_1$ if $\mathcal{M}_0$ is a special case of $\mathcal{M}_1$ obtained by fixing some parameters. Example: the exponential model is the exponential-with-asymptote model with $s = 0$ (asymptote at 0). Under the null hypothesis that $\mathcal{M}_0$ is true,

<div dir="rtl">

مدل $\mathcal{M}_0$ در $\mathcal{M}_1$ **nested** است اگر $\mathcal{M}_0$ حالت خاصی از $\mathcal{M}_1$ باشد که با ثابت کردن بعضی پارامترها به دست می‌آید. مثال: مدل نمایی همان مدل نمایی با مجانب با $s = 0$ (مجانب در 0) است. تحت فرض صفر که $\mathcal{M}_0$ درست است،

</div>

$$
\Lambda = 2\big[\ell_1(\hat{\boldsymbol\theta}_1) - \ell_0(\hat{\boldsymbol\theta}_0)\big] \;\dot\sim\; \chi^2_{\Delta k},
$$

where $\Delta k$ is the difference in the number of free parameters. A large $\Lambda$ means the extra parameters improve the fit more than chance would.

<div dir="rtl">

که در آن $\Delta k$ تفاوت تعداد پارامترهای آزاد است. $\Lambda$ بزرگ یعنی پارامترهای اضافه برازش را بیشتر از آنچه شانس توضیح می‌دهد بهتر کرده‌اند.

</div>

**Limitations:** it only works for **nested** models (power vs. exponential cannot be tested this way); it is a null-hypothesis test (it can reject the simpler model but never support it); and it is approximate when the fixed parameter value lies on the boundary of the parameter space (as $s = 0$ does).

<div dir="rtl">

**محدودیت‌ها:** فقط برای مدل‌های **nested** کار می‌کند (توانی در برابر نمایی را نمی‌شود این‌طور آزمون کرد)؛ آزمون فرض صفر است (می‌تواند مدل ساده‌تر را رد کند ولی هرگز از آن حمایت نمی‌کند)؛ و وقتی مقدار ثابت‌شده‌ی پارامتر روی مرز فضای پارامتر است (مثل $s = 0$) تقریبی است.

</div>

> **Advanced: boundary nulls.** When the null value is on the boundary (a variance of 0, an asymptote of 0, a mixture weight of 0), the null distribution of $\Lambda$ is a 50:50 mixture of $\chi^2_0$ (a point mass at 0) and $\chi^2_1$. Using $\chi^2_1$ is then conservative: the correct $p$-value is half of the naive one.

<div dir="rtl">

> **پیشرفته: فرض صفر روی مرز.** وقتی مقدار صفر روی مرز است (واریانس 0، مجانب 0، وزن آمیخته‌ی 0)، توزیع $\Lambda$ تحت فرض صفر آمیزه‌ای 50:50 از $\chi^2_0$ (یک جرم نقطه‌ای در 0) و $\chi^2_1$ است. در این حالت استفاده از $\chi^2_1$ محافظه‌کارانه است: مقدار $p$ درست نصف مقدار ساده است.

</div>

### 2. Information criteria · 2. معیارهای اطلاعاتی

Information criteria trade off fit against complexity. With maximized log-likelihood $\hat\ell$, $k$ free parameters and $N$ observations:

<div dir="rtl">

معیارهای اطلاعاتی بین برازش و پیچیدگی trade-off برقرار می‌کنند. با لگاریتم درست‌نمایی بیشینه $\hat\ell$، $k$ پارامتر آزاد و $N$ مشاهده:

</div>

$$
\mathrm{AIC} = -2\hat\ell + 2k, \qquad
\mathrm{AICc} = \mathrm{AIC} + \frac{2k(k+1)}{N - k - 1}, \qquad
\mathrm{BIC} = -2\hat\ell + k \ln N.
$$

**Lower is better.** Only **differences** between models fitted to the same data are meaningful.

<div dir="rtl">

**کمتر بهتر است.** فقط **تفاوت‌ها** بین مدل‌هایی که روی داده‌ی یکسان برازش شده‌اند معنادارند.

</div>

| | AIC (and AICc) | BIC |
|---|---|---|
| Goal | Best **prediction** of new data (minimize expected Kullback–Leibler divergence to the truth) | Pick the **true** model if it is among the candidates (consistency); approximates the Bayes factor |
| Penalty per parameter | 2 | $\ln N$ (bigger than 2 once $N \ge 8$) |
| As $N \to \infty$ | May keep choosing over-complex models | Chooses the true model with probability → 1 |
| Small-sample correction | AICc (use when $N/k < 40$) | — |

<div dir="rtl">

| | AIC (و AICc) | BIC |
|---|---|---|
| هدف | بهترین **پیش‌بینی** داده‌ی جدید (کمینه کردن واگرایی Kullback–Leibler مورد انتظار نسبت به حقیقت) | انتخاب مدل **واقعی** اگر میان نامزدها باشد (سازگاری)؛ تقریبی از Bayes factor |
| جریمه‌ی هر پارامتر | 2 | $\ln N$ (از $N \ge 8$ بیشتر از 2) |
| وقتی $N \to \infty$ | ممکن است همچنان مدل‌های بیش از حد پیچیده را انتخاب کند | مدل واقعی را با احتمال ← 1 انتخاب می‌کند |
| تصحیح نمونه‌ی کوچک | AICc (وقتی $N/k < 40$) | — |

</div>

**What is $N$?** The number of *independent observations* that enter the likelihood. For binomial recall data that is the number of item responses (here $8 \times 50 = 400$), not the number of cells (8). This choice affects BIC (through $\ln N$) and AICc. Report it.

<div dir="rtl">

**$N$ چیست؟** تعداد *مشاهدات مستقلی* که وارد درست‌نمایی می‌شوند. برای داده‌ی یادآوری دوجمله‌ای این تعداد پاسخ‌های آیتم است (اینجا $8 \times 50 = 400$)، نه تعداد خانه‌ها (8). این انتخاب روی BIC (از راه $\ln N$) و AICc اثر دارد. آن را گزارش کنید.

</div>

**Weights.** With $\Delta_i = \mathrm{IC}_i - \min_j \mathrm{IC}_j$,

<div dir="rtl">

**وزن‌ها.** با $\Delta_i = \mathrm{IC}_i - \min_j \mathrm{IC}_j$،

</div>

$$
w_i = \frac{\exp(-\Delta_i/2)}{\sum_j \exp(-\Delta_j/2)}.
$$

**Akaike weights** estimate the probability that model $i$ is the best predictor among the candidates. **BIC weights** approximate posterior model probabilities under equal prior odds (Week 10).

<div dir="rtl">

**وزن‌های آکائیکه** احتمال اینکه مدل $i$ بهترین پیش‌بینی‌کننده در میان نامزدها باشد را تخمین می‌زنند. **وزن‌های BIC** احتمال‌های پسین مدل‌ها را تحت بخت‌های پیشین برابر تقریب می‌زنند (هفته‌ی 10).

</div>

**Rules of thumb for $\Delta$:** 0–2, essentially equivalent support; 4–7, considerably less support; more than 10, essentially none. These are conventions, not laws.

<div dir="rtl">

**قواعد سرانگشتی برای $\Delta$:** 0 تا 2، پشتیبانی عملاً برابر؛ 4 تا 7، پشتیبانی به‌طور قابل توجهی کمتر؛ بیشتر از 10، عملاً بدون پشتیبانی. این‌ها قرارداد هستند، نه قانون.

</div>

**Limitation shared by AIC and BIC:** both count parameters, $k$, so they are blind to differences in **functional-form flexibility** between models with the same $k$ (Week 6). Cross-validation and Bayes factors (Week 10) are not.

<div dir="rtl">

**محدودیت مشترک AIC و BIC:** هر دو پارامترها ($k$) را می‌شمارند، پس به تفاوت **انعطاف شکل تابعی** بین مدل‌هایی با $k$ یکسان کورند (هفته‌ی 6). cross-validation و Bayes factor (هفته‌ی 10) این‌طور نیستند.

</div>

> **Advanced: where the AIC penalty comes from.** The maximized log-likelihood is an optimistically biased estimate of the expected log-likelihood of new data, because the same data were used to choose $\hat{\boldsymbol\theta}$. Akaike showed that, for regular models and large $N$, the bias is approximately $k$. Correcting for it gives $-2(\hat\ell - k) = \mathrm{AIC}$. That is also why AIC and LOO-CV agree asymptotically.

<div dir="rtl">

> **پیشرفته: جریمه‌ی AIC از کجا می‌آید.** لگاریتم درست‌نمایی بیشینه برآوردی خوش‌بینانه و سوگیر از لگاریتم درست‌نمایی مورد انتظار داده‌ی جدید است، چون همان داده برای انتخاب $\hat{\boldsymbol\theta}$ به کار رفته است. آکائیکه نشان داد که برای مدل‌های منظم و $N$ بزرگ، این سوگیری تقریباً $k$ است. تصحیحش $-2(\hat\ell - k) = \mathrm{AIC}$ را می‌دهد. به همین دلیل است که AIC و LOO-CV به‌طور مجانبی با هم توافق دارند.

</div>

#### Reading the math · خواندن ریاضی

- $-2\hat\ell$ is the **misfit** part (twice the minimized NLL); $2k$ or $k\ln N$ is the **penalty** part. Lower AIC/BIC is better.
- Each extra parameter must lower $-2\hat\ell$ by more than 2 (AIC) or more than $\ln N$ (BIC) to be worth it. With $N = 400$, $\ln N \approx 6$: a parameter must improve the NLL by about 3 units to pass BIC, but only by 1 unit to pass AIC.
- **Weights**: $\exp(-\Delta_i/2)$ converts a difference in AIC into a relative likelihood. $\Delta = 2$ gives $e^{-1} = 0.37$, so a model 2 AIC units worse is about a third as well supported. Dividing by the sum makes the weights add up to 1.
- **Worked numbers:** power model AIC $= 2(19.830) + 2(2) = 43.66$; exponential-with-asymptote $= 2(18.919) + 2(3) = 43.84$. The asymptote model fits better (lower NLL) but pays for one more parameter, so the two end up almost tied.

<div dir="rtl">

- $-2\hat\ell$ بخش **عدم برازش** است (دو برابر NLL کمینه‌شده)؛ $2k$ یا $k\ln N$ بخش **جریمه** است. AIC/BIC کمتر بهتر است.
- هر پارامتر اضافه باید $-2\hat\ell$ را بیش از 2 (برای AIC) یا بیش از $\ln N$ (برای BIC) کم کند تا ارزشش را داشته باشد. با $N = 400$، $\ln N \approx 6$: یک پارامتر باید NLL را حدود 3 واحد بهتر کند تا از BIC بگذرد، ولی برای AIC فقط 1 واحد.
- **وزن‌ها:** $\exp(-\Delta_i/2)$ تفاوت AIC را به درست‌نمایی نسبی تبدیل می‌کند. $\Delta = 2$ می‌دهد $e^{-1} = 0.37$، پس مدلی که 2 واحد AIC بدتر است حدود یک‌سوم پشتیبانی دارد. تقسیم بر جمع، وزن‌ها را طوری می‌کند که جمعشان 1 شود.
- **عددهای مثال حل‌شده:** AIC مدل توانی $= 2(19.830) + 2(2) = 43.66$؛ مدل نمایی با مجانب $= 2(18.919) + 2(3) = 43.84$. مدل مجانب بهتر برازش می‌شود (NLL کمتر) ولی هزینه‌ی یک پارامتر بیشتر را می‌دهد، پس دو مدل تقریباً مساوی می‌شوند.

</div>

### 3. Parameter recovery · 3. بازیابی پارامتر

**Question:** at this design, does the fitting procedure return the parameters that generated the data?

<div dir="rtl">

**سؤال:** با این طرح آزمایش، آیا رویه‌ی برازش پارامترهایی را که داده را تولید کرده‌اند برمی‌گرداند؟

</div>

**Procedure:**
1. Choose a set of true parameter values $\boldsymbol\theta^\ast$ covering the plausible range (a grid, or random draws from plausible ranges, e.g., around the estimates from real data).
2. For each $\boldsymbol\theta^\ast$, simulate a dataset with **exactly the real design** (same conditions, numbers of trials).
3. Fit the model with **exactly the real fitting procedure** (same optimizer, starts, bounds).
4. Compare $\hat{\boldsymbol\theta}$ with $\boldsymbol\theta^\ast$: scatter plots of true vs. recovered; correlation; bias (mean of $\hat\theta - \theta^\ast$); RMSE.
5. Also plot the recovered parameters **against each other**. A strong correlation between, say, $\hat\lambda$ and $\hat s$ that is absent in the true values reveals a **trade-off**.

<div dir="rtl">

**رویه:**
1. مجموعه‌ای از مقادیر واقعی پارامتر $\boldsymbol\theta^\ast$ انتخاب کنید که دامنه‌ی معقول را پوشش دهد (یک شبکه، یا نمونه‌های تصادفی از دامنه‌های معقول، مثلاً حول برآوردهای داده‌ی واقعی).
2. برای هر $\boldsymbol\theta^\ast$ یک مجموعه‌داده با **دقیقاً همان طرح واقعی** (همان شرایط، همان تعداد trial) شبیه‌سازی کنید.
3. مدل را با **دقیقاً همان رویه‌ی برازش واقعی** (همان بهینه‌ساز، شروع‌ها، کران‌ها) برازش کنید.
4. $\hat{\boldsymbol\theta}$ را با $\boldsymbol\theta^\ast$ مقایسه کنید: نمودار پراکنش واقعی در برابر بازیابی‌شده؛ همبستگی؛ سوگیری (میانگین $\hat\theta - \theta^\ast$)؛ RMSE.
5. پارامترهای بازیابی‌شده را **در برابر هم** هم رسم کنید. همبستگی قوی بین مثلاً $\hat\lambda$ و $\hat s$ که در مقادیر واقعی نیست، یک **trade-off** را آشکار می‌کند.

</div>

**Reading the results:** points on the identity line mean good recovery; a cloud parallel to the x-axis means the parameter is not recoverable at this design; a curve bending away at the extremes means bias near the bounds. If recovery fails, do not interpret that parameter. Change the design (more trials, other conditions) or simplify the model.

<div dir="rtl">

**خواندن نتایج:** نقاط روی خط همانی یعنی بازیابی خوب؛ ابری موازی با محور افقی یعنی پارامتر با این طرح قابل بازیابی نیست؛ منحنی‌ای که در دو انتها کج می‌شود یعنی سوگیری نزدیک کران‌ها. اگر بازیابی شکست بخورد، آن پارامتر را تفسیر نکنید. طرح آزمایش را عوض کنید (trial بیشتر، شرایط دیگر) یا مدل را ساده کنید.

</div>

### 4. Model recovery · 4. بازیابی مدل

**Question:** if model $\mathcal{M}_a$ generated the data, does our comparison method select $\mathcal{M}_a$?

<div dir="rtl">

**سؤال:** اگر مدل $\mathcal{M}_a$ داده را تولید کرده باشد، آیا روش مقایسه‌ی ما $\mathcal{M}_a$ را انتخاب می‌کند؟

</div>

**Procedure:**
1. For each candidate model $\mathcal{M}_a$: simulate many datasets at the real design, with parameters drawn from plausible ranges.
2. Fit **every** candidate model to every dataset.
3. Select a winner by the chosen criterion (AIC, BIC, CV, …).
4. Tabulate the **confusion matrix** $P(\text{selected} = b \mid \text{generated} = a)$.

<div dir="rtl">

**رویه:**
1. برای هر مدل نامزد $\mathcal{M}_a$: مجموعه‌داده‌های زیادی با طرح واقعی و با پارامترهایی از دامنه‌های معقول شبیه‌سازی کنید.
2. **همه‌ی** مدل‌های نامزد را روی هر مجموعه‌داده برازش کنید.
3. با معیار انتخاب‌شده (AIC، BIC، CV، …) یک برنده انتخاب کنید.
4. **confusion matrix** $P(\text{selected} = b \mid \text{generated} = a)$ را جدول کنید.

</div>

A good method gives a matrix with large diagonal entries. Off-diagonal mass shows **model mimicry**: one model can produce data that look like another's.

<div dir="rtl">

یک روش خوب ماتریسی با درایه‌های قطری بزرگ می‌دهد. جرم خارج از قطر **تقلید مدل** (model mimicry) را نشان می‌دهد: یک مدل می‌تواند داده‌هایی بسازد که شبیه داده‌های مدل دیگر است.

</div>

What we actually need when interpreting real data is the reverse: given that model $b$ won, how likely is it that $b$ generated the data? This is the **inversion matrix** $P(\text{generated} = a \mid \text{selected} = b)$, obtained by normalizing each *column* of the confusion counts (assuming equal prior frequency of the generating models).

<div dir="rtl">

چیزی که در تفسیر داده‌ی واقعی واقعاً لازم داریم برعکس است: با فرض اینکه مدل $b$ برنده شد، چقدر محتمل است که $b$ داده را تولید کرده باشد؟ این **inversion matrix** $P(\text{generated} = a \mid \text{selected} = b)$ است که با نرمال کردن هر *ستون* شمارش‌های درهم‌ریختگی به دست می‌آید (با فرض فراوانی پیشین برابر برای مدل‌های تولیدکننده).

</div>

> **Note:** model recovery also reveals **biases of criteria**: BIC tends to favor simpler models at small $N$, AIC more complex ones. The "best" criterion is the one that recovers your candidate models best *at your design*, which is exactly what this study measures.

<div dir="rtl">

> **نکته:** بازیابی مدل **سوگیری‌های معیارها** را هم آشکار می‌کند: BIC در $N$ کوچک به مدل‌های ساده‌تر و AIC به مدل‌های پیچیده‌تر تمایل دارد. «بهترین» معیار آن است که مدل‌های نامزد شما را *با طرح آزمایش شما* بهتر بازیابی کند، و این دقیقاً همان چیزی است که این مطالعه اندازه می‌گیرد.

</div>

#### Reading the math · خواندن ریاضی

- **Confusion matrix** $P(\text{selected} = b \mid \text{generated} = a)$: rows are the true (generating) models, columns the selected ones. Each row adds up to 1. Read a row as: "when the truth is $a$, how often do we pick each model?"
- **Inversion matrix** $P(\text{generated} = a \mid \text{selected} = b)$: the same counts, but each *column* is normalized to 1. Read a column as: "when we picked $b$, how often was $b$ really the truth?" This is the question that matters for a real dataset, where we only see the winner.
- **Small example.** 100 datasets from each of two models. From A: 90 select A, 10 select B. From B: 40 select A, 60 select B. Confusion row A = (0.90, 0.10). But among the 130 datasets that selected A, only 90 came from A: $P(\text{A true} \mid \text{A selected}) = 90/130 = 0.69$.

<div dir="rtl">

- **confusion matrix** $P(\text{selected} = b \mid \text{generated} = a)$: سطرها مدل‌های واقعی (مولد) و ستون‌ها مدل‌های انتخاب‌شده‌اند. جمع هر سطر 1 است. هر سطر را این‌طور بخوانید: «وقتی حقیقت $a$ است، چند بار هر مدل را انتخاب می‌کنیم؟»
- **inversion matrix** $P(\text{generated} = a \mid \text{selected} = b)$: همان شمارش‌ها، ولی هر *ستون* به 1 نرمال شده. هر ستون را این‌طور بخوانید: «وقتی $b$ را انتخاب کردیم، چند بار واقعاً $b$ حقیقت بود؟» این همان سؤالی است که برای داده‌ی واقعی اهمیت دارد، جایی که فقط برنده را می‌بینیم.
- **مثال کوچک.** از هر کدام از دو مدل 100 مجموعه داده. از A: 90 بار A و 10 بار B انتخاب می‌شود. از B: 40 بار A و 60 بار B. سطر A در confusion matrix برابر (0.90, 0.10) است. ولی از 130 مجموعه داده‌ای که A را انتخاب کردند، فقط 90 تا از A آمده بودند: $P(\text{A true} \mid \text{A selected}) = 90/130 = 0.69$.

</div>

### 5. Identifiability · 5. identifiability

- **Structurally non-identifiable:** different parameter values give *exactly* the same predictions, for any data. Examples: label switching in the two-trace model (Week 3), or the SDT location and scale (Week 2). The fix is a constraint or a reparameterization.
- **Practically non-identifiable:** parameters are identifiable in principle but not with the available data. Recovery is poor and estimates trade off. The fix is a better design or a simpler model.

<div dir="rtl">

- **non-identifiable ساختاری:** مقادیر مختلف پارامتر برای هر داده‌ای *دقیقاً* پیش‌بینی‌های یکسان می‌دهند. مثال‌ها: جابه‌جایی برچسب در مدل دوردی (هفته‌ی 3)، یا مکان و مقیاس در SDT (هفته‌ی 2). راه‌حل یک قید یا reparameterization است.
- **non-identifiable عملی:** پارامترها در اصل identifiable هستند ولی با داده‌های موجود نه. بازیابی ضعیف است و برآوردها trade-off دارند. راه‌حل طرح آزمایش بهتر یا مدل ساده‌تر است.

</div>

Parameter recovery is the practical test of identifiability.

<div dir="rtl">

بازیابی پارامتر آزمون عملی identifiability است.

</div>

#### For an engineer · برای یک مهندس

- **AIC and BIC** are the model-order selection criteria you may know from AR/ARMA modeling; **BIC** is essentially Rissanen's **MDL** criterion. The LRT for nested models is again the GLRT.
- **Parameter recovery** is testing an estimator on synthetic signals with known ground truth, at the real SNR and record length, before trusting it on measured data. Engineers do this routinely; in psychology it is often skipped, which is why the course insists on it.
- The **confusion matrix** is the channel transition matrix of a discrete channel: input = generating model, output = selected model. The **inversion matrix** is the matrix of *a posteriori* probabilities $P(\text{input} \mid \text{output})$, i.e. what an MAP decoder needs, assuming equal input priors.
- **Structural non-identifiability** is like an unobservable state or a rank-deficient system matrix: no amount of data helps. **Practical non-identifiability** is an ill-conditioned problem: identifiable in principle, but the noise is too large for the available record.

<div dir="rtl">

- **AIC و BIC** همان معیارهای انتخاب مرتبه‌ی مدل‌اند که شاید از مدل‌سازی AR/ARMA بشناسید؛ **BIC** اساساً همان معیار **MDL** ریسانن است. LRT برای مدل‌های nested دوباره همان GLRT است.
- **بازیابی پارامتر** یعنی آزمودن یک تخمین‌گر روی سیگنال‌های مصنوعی با حقیقت معلوم، با همان SNR و طول داده‌ی واقعی، پیش از اعتماد به آن روی داده‌ی اندازه‌گیری‌شده. مهندس‌ها این کار را مرتب انجام می‌دهند؛ در روان‌شناسی اغلب حذف می‌شود، و به همین دلیل این درس روی آن اصرار دارد.
- **confusion matrix** همان ماتریس احتمال انتقال یک کانال گسسته است: ورودی = مدل مولد، خروجی = مدل انتخاب‌شده. **inversion matrix** ماتریس احتمال‌های *پسین* $P(\text{input} \mid \text{output})$ است، یعنی چیزی که یک دیکدر MAP لازم دارد، با فرض احتمال‌های پیشین برابر برای ورودی‌ها.
- **non-identifiability ساختاری** مثل یک حالت مشاهده‌ناپذیر یا ماتریس سیستم با رتبه‌ی ناقص است: هیچ مقداری از داده کمک نمی‌کند. **non-identifiability عملی** یک مسئله‌ی بدحالت است: در اصل قابل شناسایی است ولی برای داده‌ی موجود نویز خیلی زیاد است.

</div>

#### For the instructor · برای مدرس

- **Frame recovery as "checking the equipment".** No one would trust a thermometer that was never tested in water of known temperature. Recovery is that test for a model.
- **Show one scatter plot of true vs. recovered values** (lab Part C) before any theory: good recovery (points on the diagonal) next to bad recovery (a flat cloud). The picture explains itself.
- **Teach confusion vs. inversion with the small 2×2 example above**; students confuse them in the exam more than anything else this week. The medical-test analogy helps: the sensitivity of a test is not the probability that a positive patient is ill.
- **Typical questions.**
  - *"AIC or BIC?"* Depends on the goal (prediction vs. finding the true model) and, practically, on which one recovers your models better at your design.
  - *"How many simulated datasets?"* 50–100 per condition is enough to see the pattern; more for publication.
  - *"Recovery failed, what now?"* Do not interpret that parameter. Change the design or simplify the model.

<div dir="rtl">

- **بازیابی را «آزمودن ابزار» معرفی کنید.** هیچ‌کس به دماسنجی که هیچ‌وقت در آبی با دمای معلوم امتحان نشده اعتماد نمی‌کند. بازیابی همان آزمون برای یک مدل است.
- **پیش از هر نظریه‌ای یک نمودار پراکندگی مقدار واقعی در برابر بازیابی‌شده نشان دهید** (بخش C lab): بازیابی خوب (نقطه‌ها روی قطر) کنار بازیابی بد (یک ابر صاف). تصویر خودش توضیح می‌دهد.
- **confusion و inversion را با مثال کوچک 2×2 بالا درس دهید**؛ دانشجوها در امتحان بیش از هر چیز دیگری در این هفته این دو را با هم قاطی می‌کنند. تشبیه تست پزشکی کمک می‌کند: sensitivity یک تست با احتمال بیمار بودن کسی که تستش مثبت شده یکی نیست.
- **سؤال‌های رایج.**
  - *«AIC یا BIC؟»* به هدف بستگی دارد (پیش‌بینی در برابر پیدا کردن مدل درست) و در عمل به اینکه کدام در طرح آزمایش شما مدل‌ها را بهتر بازیابی می‌کند.
  - *«چند مجموعه داده‌ی شبیه‌سازی‌شده؟»* برای دیدن الگو 50 تا 100 برای هر حالت کافی است؛ برای انتشار بیشتر.
  - *«بازیابی شکست خورد، حالا چه؟»* آن پارامتر را تفسیر نکنید. طرح آزمایش را تغییر دهید یا مدل را ساده‌تر کنید.

</div>

---

## Worked example · مثال حل‌شده

The four forgetting models fitted by MLE to the Week 2 data (training NLLs from Week 6), with $N = 400$ item responses:

<div dir="rtl">

چهار مدل فراموشی که با MLE روی داده‌های هفته‌ی 2 برازش شده‌اند (NLLهای آموزش از هفته‌ی 6)، با $N = 400$ پاسخ آیتم:

</div>

| Model | $k$ | NLL | AIC $= 2\,\mathrm{NLL} + 2k$ | BIC $= 2\,\mathrm{NLL} + k\ln 400$ |
|---|---|---|---|---|
| exp | 2 | 29.812 | 63.62 | 71.61 |
| pow | 2 | 19.830 | **43.66** | **51.64** |
| expasym | 3 | 18.919 | 43.84 | 55.81 |
| two | 4 | 18.919 | 45.84 | 61.80 |

<div dir="rtl">

| مدل | $k$ | NLL | AIC $= 2\,\mathrm{NLL} + 2k$ | BIC $= 2\,\mathrm{NLL} + k\ln 400$ |
|---|---|---|---|---|
| exp | 2 | 29.812 | 63.62 | 71.61 |
| pow | 2 | 19.830 | **43.66** | **51.64** |
| expasym | 3 | 18.919 | 43.84 | 55.81 |
| two | 4 | 18.919 | 45.84 | 61.80 |

</div>

**Step 1: AIC for the power model.** $2 \times 19.830 + 2 \times 2 = 43.66$.

<div dir="rtl">

**قدم 1: AIC برای مدل توانی.** $2 \times 19.830 + 2 \times 2 = 43.66$.

</div>

**Step 2: BIC for the power model.** $\ln 400 = 5.991$, so $2 \times 19.830 + 2 \times 5.991 = 51.64$.

<div dir="rtl">

**قدم 2: BIC برای مدل توانی.** $\ln 400 = 5.991$، پس $2 \times 19.830 + 2 \times 5.991 = 51.64$.

</div>

**Step 3: Akaike weights.** Differences from the best AIC: $\Delta = (19.96, 0, 0.18, 2.18)$. Then $e^{-\Delta/2} = (0.00005, 1, 0.914, 0.336)$, which sum to 2.250, so

<div dir="rtl">

**قدم 3: وزن‌های آکائیکه.** تفاوت‌ها با بهترین AIC: $\Delta = (19.96, 0, 0.18, 2.18)$. پس $e^{-\Delta/2} = (0.00005, 1, 0.914, 0.336)$ که جمعشان 2.250 است، بنابراین

</div>

$$
w^{\text{AIC}} = (0.000,\ 0.444,\ 0.406,\ 0.149).
$$

BIC weights computed the same way: $(0.000,\ 0.884,\ 0.110,\ 0.005)$.

<div dir="rtl">

وزن‌های BIC به همین روش: $(0.000,\ 0.884,\ 0.110,\ 0.005)$.

</div>

**Step 4: likelihood-ratio test**, exp nested in expasym: $\Lambda = 2(29.812 - 18.919) = 21.79$ on 1 df, $p \approx 3 \times 10^{-6}$. Adding an asymptote improves the exponential model significantly.

<div dir="rtl">

**قدم 4: آزمون نسبت درست‌نمایی**، exp nested در expasym: $\Lambda = 2(29.812 - 18.919) = 21.79$ با 1 درجه‌ی آزادی، $p \approx 3 \times 10^{-6}$. افزودن مجانب مدل نمایی را به‌طور معناداری بهتر می‌کند.

</div>

**Interpretation.** Both criteria reject the pure exponential decisively. AIC cannot separate the power and asymptote models (weights 0.44 vs. 0.41): for *prediction* they are about equally good, consistent with the Week 6 CV results. BIC's larger penalty favors the two-parameter power model (0.88). The two-trace model's extra parameter buys nothing: identical NLL to expasym, so it pays the penalty for nothing. Whether we should *trust* these preferences at this design is a question for model recovery (lab Part D).

<div dir="rtl">

**تفسیر.** هر دو معیار مدل نمایی خالص را قاطعانه رد می‌کنند. AIC نمی‌تواند مدل‌های توانی و مجانبی را از هم جدا کند (وزن‌های 0.44 در برابر 0.41): از نظر *پیش‌بینی* تقریباً به یک اندازه خوب‌اند، که با نتایج CV هفته‌ی 6 سازگار است. جریمه‌ی بزرگ‌تر BIC مدل توانی دوپارامتری را ترجیح می‌دهد (0.88). پارامتر اضافه‌ی مدل دوردی هیچ چیزی نمی‌خرد: NLL آن با expasym یکسان است، پس جریمه را بی‌دلیل می‌پردازد. اینکه آیا باید به این ترجیح‌ها با این طرح آزمایش *اعتماد* کنیم سؤالی برای بازیابی مدل است (بخش D lab).

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Run a likelihood-ratio test and compute AIC, AICc, BIC and weights for the forgetting models.
2. Run a parameter-recovery study for the power and exponential-with-asymptote models, and check for trade-offs.
3. Run a model-recovery study for three models with AIC and BIC; build confusion and inversion matrices.
4. **Interpret**: what can and cannot be concluded from the Week 2 data at this design?

<div dir="rtl">

1. اجرای آزمون نسبت درست‌نمایی و محاسبه‌ی AIC، AICc، BIC و وزن‌ها برای مدل‌های فراموشی.
2. اجرای یک مطالعه‌ی بازیابی پارامتر برای مدل‌های توانی و نمایی با مجانب و بررسی trade-offها.
3. اجرای یک مطالعه‌ی بازیابی مدل برای سه مدل با AIC و BIC؛ ساختن ماتریس‌های درهم‌ریختگی و معکوس.
4. **تفسیر**: با این طرح آزمایش، از داده‌های هفته‌ی 2 چه چیزی را می‌شود و چه چیزی را نمی‌شود نتیجه گرفت؟

</div>

**Timing:** Part A 15 min · Part B 15 min · Part C 35 min · Part D 40 min · Part E 15 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 15 دقیقه · بخش B 15 دقیقه · بخش C 35 دقیقه · بخش D 40 دقیقه · بخش E 15 دقیقه.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week07.py`](code/week07.py), cell 1 · سلول 1

### Part A: likelihood-ratio test (15 min) · بخش A: آزمون نسبت درست‌نمایی (15 دقیقه)

> **Code · کد:** [`code/week07.py`](code/week07.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
NLL exp = 29.812, NLL expasym = 18.919
LR statistic = 21.79, df = 1, naive p = 3.05e-06, boundary-corrected p = 1.52e-06
```

**Question:** why can't you use the same test to compare the power and exponential models?

<div dir="rtl">

**سؤال:** چرا نمی‌توانید از همین آزمون برای مقایسه‌ی مدل‌های توانی و نمایی استفاده کنید؟

</div>

### Part B: information criteria and weights (15 min) · بخش B: معیارهای اطلاعاتی و وزن‌ها (15 دقیقه)

> **Code · کد:** [`code/week07.py`](code/week07.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
         k     NLL     AIC    AICc     BIC  w_AIC  w_AICc  w_BIC
model
exp      2  29.812  63.625  63.655  71.608  0.000   0.000  0.000
pow      2  19.830  43.661  43.691  51.644  0.444   0.449  0.884
expasym  3  18.919  43.837  43.898  55.812  0.406   0.405  0.110
two      4  18.919  45.837  45.939  61.803  0.150   0.146  0.006
```

**Sensitivity check:** recompute BIC with $N = 8$ (the number of cells) instead of 400. Does the ranking change? Which choice of $N$ is defensible here, and why?

<div dir="rtl">

**بررسی حساسیت:** BIC را با $N = 8$ (تعداد خانه‌ها) به‌جای 400 دوباره حساب کنید. آیا رتبه‌بندی عوض می‌شود؟ کدام انتخاب $N$ اینجا قابل دفاع است و چرا؟

</div>

### Part C: parameter recovery (35 min) · بخش C: بازیابی پارامتر (35 دقیقه)

> **Code · کد:** [`code/week07.py`](code/week07.py), cell 4 · سلول 4

**Expected output** (about 1 minute):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 1 دقیقه):

</div>

```text
pow:
   r(true, rec)   bias   RMSE
A         0.888  0.005  0.055
d         0.965  0.003  0.070

expasym:
     r(true, rec)   bias   RMSE
A           0.802  0.008  0.077
lam         0.799  0.034  0.230
s           0.918 -0.008  0.060

expasym: corr(true lam, true s) = -0.08;  corr(recovered lam, recovered s) = 0.03
```

**Interpret:**
1. Which parameters are well recovered at this design? Which would you hesitate to interpret?
2. The expasym decay rate $\lambda$ has by far the largest RMSE (0.23 on a range of 0.05–1). Look at its panel: for which true values does recovery break down, and why? (Hint: if decay is very fast, most of the decline happens before the second test interval, so what do the data look like?) Here the recovered $\lambda$ and $s$ are *not* correlated (r = 0.03), so this is imprecision rather than a trade-off. Contrast this with the clear $A$–$d$ trade-off of the power model found in Week 5.
3. What design change would improve recovery of $\lambda$ and $s$? Test one idea in Exercise 3.

<div dir="rtl">

**تفسیر:**
1. با این طرح آزمایش، کدام پارامترها خوب بازیابی می‌شوند؟ تفسیر کدام را با تردید انجام می‌دهید؟
2. نرخ زوال $\lambda$ در expasym با فاصله‌ی زیاد بیشترین RMSE را دارد (0.23 روی دامنه‌ی 0.05 تا 1). به نمودارش نگاه کنید: بازیابی برای کدام مقادیر واقعی شکست می‌خورد و چرا؟ (راهنمایی: اگر زوال خیلی سریع باشد، بیشترِ افت پیش از دومین فاصله‌ی آزمون اتفاق می‌افتد؛ پس داده‌ها چه شکلی پیدا می‌کنند؟) اینجا $\lambda$ و $s$ بازیابی‌شده همبستگی *ندارند* (r = 0.03)، پس این عدم دقت است نه trade-off. این را با trade-off آشکار $A$–$d$ مدل توانی که در هفته‌ی 5 دیدیم مقایسه کنید.
3. چه تغییری در طرح آزمایش بازیابی $\lambda$ و $s$ را بهتر می‌کند؟ یک ایده را در تمرین 3 آزمون کنید.

</div>

### Part D: model recovery (40 min) · بخش D: بازیابی مدل (40 دقیقه)

> **Code · کد:** [`code/week07.py`](code/week07.py), cell 5 · سلول 5

**Expected output** (about 1–2 minutes):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 1 تا 2 دقیقه):

</div>

```text
AIC confusion matrix (rows = generating model, columns = selected model):
          exp   pow  expasym
exp      0.91  0.00     0.09
pow      0.03  0.82     0.15
expasym  0.06  0.25     0.69
AIC inversion matrix (rows = generating model, columns = selected model):
          exp   pow  expasym
exp      0.91  0.00     0.10
pow      0.03  0.77     0.16
expasym  0.06  0.23     0.74

BIC confusion matrix (rows = generating model, columns = selected model):
          exp   pow  expasym
exp      0.99  0.01     0.00
pow      0.05  0.94     0.01
expasym  0.09  0.58     0.33
BIC inversion matrix (rows = generating model, columns = selected model):
          exp   pow  expasym
exp      0.88  0.01     0.00
pow      0.04  0.61     0.03
expasym  0.08  0.38     0.97
```

**Interpret:**
1. Which model is most often confused with which? (With AIC, 25% of expasym datasets are labeled power; with BIC, 58%.) Explain the mimicry in terms of the curves' shapes.
2. Compare AIC and BIC. Which recovers the simpler models better, and which the more complex one?
3. In Part B, BIC selected the power model for the real data. Using the BIC **inversion** matrix, how confident should we be that the data were generated by a power model? (Only 61% of BIC's "power" verdicts came from power-generated data; 38% came from expasym.)

<div dir="rtl">

**تفسیر:**
1. کدام مدل بیشتر با کدام اشتباه گرفته می‌شود؟ (با AIC، 25% مجموعه‌داده‌های expasym برچسب توانی می‌گیرند؛ با BIC، 58%.) این تقلید را بر حسب شکل منحنی‌ها توضیح دهید.
2. AIC و BIC را مقایسه کنید. کدام مدل‌های ساده‌تر را بهتر بازیابی می‌کند و کدام مدل پیچیده‌تر را؟
3. در بخش B، BIC برای داده‌ی واقعی مدل توانی را انتخاب کرد. با استفاده از **inversion matrix** BIC، چقدر باید مطمئن باشیم که داده‌ها را یک مدل توانی تولید کرده است؟ (فقط 61% از حکم‌های «توانی» BIC از داده‌های تولیدشده با مدل توانی آمده‌اند؛ 38% از expasym.)

</div>

### Part E: conclusions about the Week 2 data (15 min) · بخش E: نتیجه‌گیری درباره‌ی داده‌های هفته‌ی 2 (15 دقیقه)

Write a paragraph (6–10 sentences) that a reviewer would accept, summarizing what the Week 2 data say about the form of forgetting. Use Parts A–D and your Week 6 CV results, and state what *cannot* be concluded at this design.

<div dir="rtl">

یک پاراگراف (6 تا 10 جمله) بنویسید که یک داور بپذیرد و خلاصه کند داده‌های هفته‌ی 2 درباره‌ی شکل فراموشی چه می‌گویند. از بخش‌های A تا D و نتایج CV هفته‌ی 6 استفاده کنید و بگویید با این طرح آزمایش چه چیزی را *نمی‌شود* نتیجه گرفت.

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Compute AIC and BIC weights for the worked example by hand (calculator) and check them against Part B.

<div dir="rtl">

**تمرین 1 ★.** وزن‌های AIC و BIC مثال حل‌شده را با دست (ماشین‌حساب) حساب کنید و با بخش B مقایسه کنید.

</div>

**Exercise 2 ★.** Repeat Part B with AICc. For which $N$ would AICc and AIC differ noticeably for the two-trace model?

<div dir="rtl">

**تمرین 2 ★.** بخش B را با AICc تکرار کنید. برای چه $N$ای AICc و AIC برای مدل دوردی به‌طور قابل توجهی فرق می‌کنند؟

</div>

**Exercise 3 ★★ (design for recovery).** Rerun the expasym recovery of Part C with intervals extended to $\{0.25, 1, 2, 4, 7, 14, 30, 60, 90\}$ days, and separately with $n = 200$ items. Which change helps $\lambda$ and $s$ recovery more?

<div dir="rtl">

**تمرین 3 ★★ (طراحی برای بازیابی).** بازیابی expasym بخش C را با فاصله‌های گسترش‌یافته به $\{0.25, 1, 2, 4, 7, 14, 30, 60, 90\}$ روز، و جداگانه با $n = 200$ آیتم، دوباره اجرا کنید. کدام تغییر بیشتر به بازیابی $\lambda$ و $s$ کمک می‌کند؟

</div>

**Exercise 4 ★★ (CV in model recovery).** Replace AIC/BIC in Part D by 5-fold CV (from Week 6) for 30 simulations per model. Is CV better or worse than AIC at recovering the models? Is it worth the computation time?

<div dir="rtl">

**تمرین 4 ★★ (CV در بازیابی مدل).** در بخش D، AIC/BIC را با CV پنج‌بخشی (از هفته‌ی 6) برای 30 شبیه‌سازی از هر مدل جایگزین کنید. آیا CV در بازیابی مدل‌ها از AIC بهتر است یا بدتر؟ آیا به زمان محاسبه‌اش می‌ارزد؟

</div>

**Exercise 5 ★★★ (Advanced: SDT recovery).** For the payoff experiment of Week 4 (three conditions, 80 + 80 trials per condition), run a model recovery for "shared $d'$" vs. "separate $d'$" using the likelihood-ratio test at $\alpha = .05$ and BIC. How often does each method wrongly claim that payoffs change sensitivity? How many trials per condition would you need to detect a true sensitivity difference of 0.3 in 80% of simulations?

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: بازیابی در SDT).** برای آزمایش پاداش هفته‌ی 4 (سه شرط، 80 + 80 trial در هر شرط)، یک بازیابی مدل برای «$d'$ مشترک» در برابر «$d'$ جداگانه» با آزمون نسبت درست‌نمایی در $\alpha = .05$ و با BIC اجرا کنید. هر روش چند بار به‌اشتباه ادعا می‌کند که پاداش حساسیت را تغییر می‌دهد؟ برای اینکه یک تفاوت واقعی حساسیت به اندازه‌ی 0.3 را در 80% شبیه‌سازی‌ها تشخیص دهید، در هر شرط چند trial لازم است؟

</div>

### Lab check-off · lab check-off

Show: (1) your IC table with weights (Part B), (2) the recovery scatter plots with one sentence on which parameter is least well recovered and why, (3) the AIC and BIC confusion matrices, and (4) your Part E paragraph.

<div dir="rtl">

نشان دهید: (1) جدول معیارهای اطلاعاتی با وزن‌ها (بخش B)، (2) نمودارهای پراکنش بازیابی با یک جمله درباره‌ی اینکه کدام پارامتر بدتر بازیابی می‌شود و چرا، (3) ماتریس‌های درهم‌ریختگی AIC و BIC، و (4) پاراگراف بخش E.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Comparing learning curves of an AI model.** LLMs can learn a new task from a few examples in the prompt ("in-context learning"). How the error falls with the number of examples $k$ is a learning curve, and the question "exponential or power?" is the same question as in this week's lab (and Week 2's forgetting curves). Information criteria, model recovery and identifiability apply unchanged. The design matters as much as before: with few values of $k$ and few test items, the two curves may be impossible to tell apart.

<div dir="rtl">

**مقایسه‌ی منحنی‌های یادگیری یک مدل هوش مصنوعی.** LLMها می‌توانند یک تکلیف تازه را از چند مثال در prompt یاد بگیرند («یادگیری درون‌بافتی» یا in-context learning). اینکه خطا با تعداد مثال‌ها $k$ چطور کم می‌شود یک منحنی یادگیری است، و سؤال «نمایی یا توانی؟» همان سؤال lab این هفته (و منحنی‌های فراموشی هفته‌ی 2) است. معیارهای اطلاعاتی، بازیابی مدل و identifiability بدون تغییر به کار می‌آیند. طرح هم به همان اندازه مهم است: با مقادیر کم $k$ و آیتم‌های آزمون کم، ممکن است دو منحنی اصلاً قابل تمیز نباشند.

</div>

> **Code · کد:** [`code/week07.py`](code/week07.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
{'exponential': 41.6, 'power': 40.4} Akaike weights: [0.362 0.638]
```

The data were generated by a power law, but the evidence is weak (weights 0.64 vs. 0.36).

<div dir="rtl">

داده از یک قانون توانی تولید شده، ولی شواهد ضعیف است (وزن‌های 0.64 در برابر 0.36).

</div>

**Try it (no API needed).**
- ★ Run a model recovery (Week 7, Part D) at this design: 50 datasets from each curve. Build the confusion matrix.
- ★★ Change the design: more values of $k$ (up to 128) or 200 test items per $k$. Which change improves model recovery more?
- ★★ Discussion: a paper concludes from one fitted curve that "in-context learning follows a power law, like human practice". What would you need to see before accepting the comparison with humans?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ در همین طرح یک بازیابی مدل (هفته‌ی 7، بخش D) اجرا کنید: 50 مجموعه داده از هر منحنی. confusion matrix را بسازید.
- ★★ طرح را عوض کنید: مقادیر بیشتری برای $k$ (تا 128) یا 200 آیتم آزمون برای هر $k$. کدام تغییر بازیابی مدل را بیشتر بهتر می‌کند؟
- ★★ بحث: مقاله‌ای از یک منحنی برازش‌شده نتیجه می‌گیرد که «یادگیری درون‌بافتی، مثل تمرین در انسان، از قانون توانی پیروی می‌کند». پیش از پذیرفتن این مقایسه با انسان، چه چیزی باید ببینید؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **Interpreting an AIC value on its own.** Only differences between models fitted to the same data mean anything.
2. **Using LRTs for non-nested models,** or reading a non-significant LRT as evidence *for* the simpler model.
3. **Thinking BIC is "Bayesian AIC" with the same goal.** BIC aims at identifying the data-generating model; AIC aims at prediction. They can disagree for good reasons.
4. **Unclear $N$.** Always report what counted as an observation; BIC and AICc depend on it.
5. **Skipping recovery.** A parameter that cannot be recovered at your design must not be interpreted, no matter how good the fit.
6. **Running recovery at a different design or with a different fitting procedure** than the real analysis. Recovery results are design-specific.
7. **Reading the confusion matrix as if it were the inversion matrix.** "Data from model A are recovered as A 90% of the time" is not the same as "when A wins, it is the true model 90% of the time".
8. **Choosing parameter ranges for recovery that are wider or narrower than plausible values.** Too wide inflates correlations; too narrow hides problems.

<div dir="rtl">

1. **تفسیر یک مقدار AIC به‌تنهایی.** فقط تفاوت بین مدل‌هایی که روی داده‌ی یکسان برازش شده‌اند معنا دارد.
2. **استفاده از LRT برای مدل‌های non-nested،** یا خواندن یک LRT غیرمعنادار به‌عنوان شاهدی *به نفع* مدل ساده‌تر.
3. **فکر کردن اینکه BIC همان «AIC بیزی» با همان هدف است.** BIC به دنبال شناسایی مدل تولیدکننده‌ی داده است؛ AIC به دنبال پیش‌بینی. می‌توانند به دلایل موجه با هم مخالف باشند.
4. **$N$ نامشخص.** همیشه گزارش کنید چه چیزی به‌عنوان یک مشاهده شمرده شده؛ BIC و AICc به آن بستگی دارند.
5. **نادیده گرفتن بازیابی.** پارامتری که با طرح آزمایش شما قابل بازیابی نیست نباید تفسیر شود، هر قدر هم برازش خوب باشد.
6. **اجرای بازیابی با طرح یا رویه‌ی برازشی متفاوت** از تحلیل واقعی. نتایج بازیابی وابسته به طرح آزمایش‌اند.
7. **خواندن confusion matrix به جای inversion matrix.** «داده‌های مدل A در 90% موارد به‌عنوان A بازیابی می‌شوند» با «وقتی A برنده می‌شود در 90% موارد مدل واقعی است» یکی نیست.
8. **انتخاب دامنه‌های پارامتر برای بازیابی که از مقادیر معقول پهن‌تر یا باریک‌ترند.** دامنه‌ی خیلی پهن همبستگی‌ها را باد می‌کند؛ دامنه‌ی خیلی باریک مشکلات را پنهان می‌کند.

</div>

---

## Check your understanding · خودآزمایی

**1.** Write the formulas for AIC and BIC. For which $N$ does BIC penalize each parameter more than AIC?
<details><summary>Answer</summary>
$\mathrm{AIC} = -2\hat\ell + 2k$; $\mathrm{BIC} = -2\hat\ell + k\ln N$. BIC's penalty exceeds AIC's when $\ln N > 2$, i.e., $N > e^2 \approx 7.4$, so for $N \ge 8$.
</details>

<div dir="rtl">

**1.** فرمول‌های AIC و BIC را بنویسید. برای چه $N$ای BIC هر پارامتر را بیشتر از AIC جریمه می‌کند؟
<details><summary>پاسخ</summary>
$\mathrm{AIC} = -2\hat\ell + 2k$؛ $\mathrm{BIC} = -2\hat\ell + k\ln N$. جریمه‌ی BIC وقتی از AIC بیشتر است که $\ln N > 2$، یعنی $N > e^2 \approx 7.4$، پس برای $N \ge 8$.
</details>

</div>

**2.** Model A has AIC = 210.4, model B has AIC = 212.9. Compute the Akaike weights and interpret them.
<details><summary>Answer</summary>
$\Delta = (0, 2.5)$, so $e^{-\Delta/2} = (1, 0.287)$ and $w = (0.777, 0.223)$. A is favored about 3.5:1 as the better predictor, but B retains non-negligible support.
</details>

<div dir="rtl">

**2.** مدل A دارای AIC = 210.4 و مدل B دارای AIC = 212.9 است. وزن‌های آکائیکه را حساب و تفسیر کنید.
<details><summary>پاسخ</summary>
$\Delta = (0, 2.5)$، پس $e^{-\Delta/2} = (1, 0.287)$ و $w = (0.777, 0.223)$. A حدود 3.5 به 1 به‌عنوان پیش‌بینی‌کننده‌ی بهتر ترجیح دارد، ولی B هنوز پشتیبانی قابل توجهی دارد.
</details>

</div>

**3.** Why can the likelihood-ratio test compare exponential and exponential-with-asymptote but not exponential and power?
<details><summary>Answer</summary>
The exponential is a special case of the asymptote model (fix $s = 0$), so the models are nested and $2\Delta\ell$ has a known $\chi^2$ distribution under the null. Exponential and power are not nested: neither is a special case of the other.
</details>

<div dir="rtl">

**3.** چرا آزمون نسبت درست‌نمایی می‌تواند نمایی و نمایی با مجانب را مقایسه کند ولی نمایی و توانی را نه؟
<details><summary>پاسخ</summary>
نمایی حالت خاصی از مدل مجانبی است ($s = 0$)، پس مدل‌ها nested هستند و $2\Delta\ell$ تحت فرض صفر توزیع $\chi^2$ معلومی دارد. نمایی و توانی nested نیستند: هیچ‌کدام حالت خاص دیگری نیست.
</details>

</div>

**4.** Describe the steps of a parameter-recovery study.
<details><summary>Answer</summary>
Choose plausible true parameter values; simulate data at the real design; fit with the real fitting procedure; compare recovered with true values (scatter plots, correlation, bias, RMSE); check correlations among the recovered parameters for trade-offs.
</details>

<div dir="rtl">

**4.** مراحل یک مطالعه‌ی بازیابی پارامتر را شرح دهید.
<details><summary>پاسخ</summary>
مقادیر واقعی معقول برای پارامترها انتخاب کنید؛ با طرح واقعی داده شبیه‌سازی کنید؛ با رویه‌ی برازش واقعی برازش کنید؛ مقادیر بازیابی‌شده را با واقعی مقایسه کنید (نمودار پراکنش، همبستگی، سوگیری، RMSE)؛ همبستگی بین پارامترهای بازیابی‌شده را برای یافتن trade-off بررسی کنید.
</details>

</div>

**5.** In a recovery study, the recovered $\lambda$ and $s$ correlate at $r = -0.8$, although the true values were drawn independently. What does that mean?
<details><summary>Answer</summary>
A trade-off: at this design, different combinations of decay rate and asymptote produce nearly the same predictions, so errors in one are compensated by the other. Individual values of $\lambda$ and $s$ should not be interpreted separately. A better design or a reparameterization is needed.
</details>

<div dir="rtl">

**5.** در یک مطالعه‌ی بازیابی، $\lambda$ و $s$ بازیابی‌شده با $r = -0.8$ همبسته‌اند، با اینکه مقادیر واقعی مستقل کشیده شده بودند. این یعنی چه؟
<details><summary>پاسخ</summary>
یک trade-off: با این طرح آزمایش، ترکیب‌های مختلف نرخ زوال و مجانب پیش‌بینی‌های تقریباً یکسانی می‌دهند، پس خطا در یکی با دیگری جبران می‌شود. مقادیر تکی $\lambda$ و $s$ نباید جداگانه تفسیر شوند. طرح آزمایش بهتر یا reparameterization لازم است.
</details>

</div>

**6.** Explain the difference between a confusion matrix and an inversion matrix in model recovery.
<details><summary>Answer</summary>
Confusion: $P(\text{selected} \mid \text{generated})$, with rows summing to 1, which describes the method's behavior for each true model. Inversion: $P(\text{generated} \mid \text{selected})$, with columns summing to 1 (assuming equal priors for the generating models), which tells us how much to trust a given winner when analyzing real data.
</details>

<div dir="rtl">

**6.** تفاوت confusion matrix و inversion matrix را در بازیابی مدل توضیح دهید.
<details><summary>پاسخ</summary>
درهم‌ریختگی: $P(\text{selected} \mid \text{generated})$ که سطرهایش جمع 1 دارند و رفتار روش را برای هر مدل واقعی توصیف می‌کند. معکوس: $P(\text{generated} \mid \text{selected})$ که ستون‌هایش جمع 1 دارند (با فرض پیشین برابر برای مدل‌های تولیدکننده) و به ما می‌گوید هنگام تحلیل داده‌ی واقعی چقدر به یک برنده‌ی مشخص اعتماد کنیم.
</details>

</div>

**7.** A model recovery shows that AIC selects the three-parameter model 40% of the time when the two-parameter model generated the data. What would you do?
<details><summary>Answer</summary>
Treat AIC wins for the complex model with caution at this design: check BIC or CV recovery, which may be more conservative, improve the design (more trials, more informative conditions), and report the recovery results alongside the real-data comparison.
</details>

<div dir="rtl">

**7.** یک بازیابی مدل نشان می‌دهد وقتی مدل دوپارامتری داده را تولید کرده، AIC در 40% موارد مدل سه‌پارامتری را انتخاب می‌کند. چه می‌کنید؟
<details><summary>پاسخ</summary>
با این طرح آزمایش، به برد AIC برای مدل پیچیده با احتیاط نگاه کنید: بازیابی BIC یا CV را بررسی کنید که ممکن است محافظه‌کارتر باشند، طرح آزمایش را بهتر کنید (trial بیشتر، شرایط آگاهی‌بخش‌تر)، و نتایج بازیابی را کنار مقایسه‌ی داده‌ی واقعی گزارش کنید.
</details>

</div>

---

## Assignment · تکلیف

### A3 continues (due at the start of the Week 9 lecture) · ادامه‌ی A3 (موعد ابتدای درس هفته‌ی 9)

Tasks 4 (information criteria) and 5 (parameter and model recovery) of A3 use this week's material. The full brief is in Week 6. Reuse today's `parameter_recovery` code and the model-recovery loop: they are designed to be adapted directly.

<div dir="rtl">

کارهای 4 (معیارهای اطلاعاتی) و 5 (بازیابی پارامتر و مدل) A3 از مطالب این هفته استفاده می‌کنند. شرح کامل در هفته‌ی 6 است. کد `parameter_recovery` امروز و حلقه‌ی بازیابی مدل را دوباره به کار ببرید: طوری طراحی شده‌اند که مستقیماً قابل تطبیق باشند.

</div>

### Final project: teams and proposal brief released · پروژه‌ی پایانی: تشکیل گروه‌ها و انتشار راهنمای پیشنهاد

- **Teams:** 1–2 students. Register your team with the TA by the end of this week.
- **Task:** choose a cognitive model and apply the full pipeline to a dataset (simulated, open, or your own): fit, evaluate (at least one model comparison with an alternative model), recover (at least one parameter-recovery analysis), interpret. **Pairs** also include a Bayesian/MCMC or hierarchical analysis and an individual contribution statement.
- **Proposal (due at the start of the Week 9 lecture, max. 2 pages):** research question, model(s) with equations, data source and design, planned comparison and recovery analyses, and a timeline. The full project brief and rubric are distributed separately (`project_brief.md`).
- **Not sure what to model?** The topics of Weeks 14–15 (exemplar categorization, drift-diffusion, reinforcement learning) all make good projects, as do extensions of the forgetting and SDT models from this course.

<div dir="rtl">

- **گروه‌ها:** 1 یا 2 نفر. تا پایان این هفته گروهتان را نزد دستیار آموزشی ثبت کنید.
- **کار:** یک مدل شناختی انتخاب کنید و کل مسیر مدل‌سازی را روی یک مجموعه‌داده (شبیه‌سازی‌شده، باز، یا داده‌ی خودتان) اجرا کنید: برازش، ارزیابی (دست‌کم یک مقایسه با یک مدل جایگزین)، بازیابی (دست‌کم یک تحلیل بازیابی پارامتر)، تفسیر. **گروه‌های دونفره** یک تحلیل بیزی/MCMC یا سلسله‌مراتبی و یک بیانیه‌ی سهم فردی هم اضافه می‌کنند.
- **پیشنهاد پروژه (موعد ابتدای درس هفته‌ی 9، حداکثر 2 صفحه):** سؤال پژوهش، مدل(ها) با معادلات، منبع داده و طرح آزمایش، تحلیل‌های مقایسه و بازیابی برنامه‌ریزی‌شده، و زمان‌بندی. شرح کامل پروژه و روبریک جداگانه توزیع می‌شود (`project_brief.md`).
- **مطمئن نیستید چه چیزی را مدل کنید؟** موضوعات هفته‌های 14–15 (دسته‌بندی exemplar، drift-diffusion، یادگیری تقویتی) همه پروژه‌های خوبی هستند، همین‌طور گسترش مدل‌های فراموشی و SDT این درس.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018), chapter 10.** Model comparison: likelihood-ratio tests, AIC, BIC and their weights; their assumptions and limitations. *(Main reading.)*
- **Lee & Wagenmakers (2014), chapter 7** (introduction). How the Bayesian approach to model comparison relates to the methods of this week, as preparation for Week 10.
- *Optional, outside the course list:* Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, e49547. A practical guide that treats parameter and model recovery as standard practice.

<div dir="rtl">

- **Farrell & Lewandowsky (2018)، فصل 10.** مقایسه‌ی مدل‌ها: آزمون نسبت درست‌نمایی، AIC، BIC و وزن‌هایشان؛ فرض‌ها و محدودیت‌هایشان. *(منبع اصلی.)*
- **Lee & Wagenmakers (2014)، فصل 7** (مقدمه). اینکه رویکرد بیزی به مقایسه‌ی مدل‌ها چه ارتباطی با روش‌های این هفته دارد؛ آمادگی برای هفته‌ی 10.
- *اختیاری، خارج از فهرست درس:* Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, e49547. راهنمایی عملی که بازیابی پارامتر و مدل را رویه‌ی استاندارد می‌داند.

</div>

*Preview for Week 8:* the midterm. The lecture is an integrated review in which we run the whole pipeline (simulate, fit, evaluate, recover, interpret) on a new dataset; the lab slot is the midterm exam.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 8:* میان‌ترم. درس یک مرور یکپارچه است که در آن کل مسیر (شبیه‌سازی، برازش، ارزیابی، بازیابی، تفسیر) را روی یک مجموعه‌داده‌ی جدید اجرا می‌کنیم؛ زمان lab به آزمون میان‌ترم اختصاص دارد.

</div>
