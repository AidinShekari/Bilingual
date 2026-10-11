# Week 5: Uncertainty in Estimates and Fitting Multiple Participants · هفته‌ی 5: عدم قطعیت برآوردها و برازش برای چند شرکت‌کننده

> **Chapter 2: Parameter estimation methods** · Lecture 1 h · Lab 2 h
> **Running data:** the Week 2–4 forgetting data (how certain are our estimates?) and a new simulated **practice** experiment with 20 participants (the power law of practice).

<div dir="rtl">

> **فصل 2: روش‌های برآورد پارامتر** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** داده‌های فراموشی هفته‌های 2–4 (برآوردهای ما چقدر قطعی‌اند؟) و یک آزمایش **تمرین** (practice) شبیه‌سازی‌شده‌ی جدید با 20 شرکت‌کننده (قانون توانی تمرین).

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| power law of practice | قانون توانی تمرین | کاهش توانی زمان واکنش با تمرین |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| sampling distribution | توزیع نمونه‌گیری | توزیع برآورد در تکرارهای فرضی آزمایش |
| standard error (SE) | خطای استاندارد | پراکندگی برآورد در تکرارهای فرضی آزمایش |
| confidence interval (CI) | بازه‌ی اطمینان | بازه‌ای که با روش مشخص پارامتر واقعی را در بر می‌گیرد |
| Hessian | ماتریس Hessian | ماتریس مشتق‌های دوم؛ انحنای درست‌نمایی |
| log-likelihood / NLL | لگاریتم درست‌نمایی / منفی آن | مقداری که بهینه‌سازها کمینه یا بیشینه می‌کنند |
| Wald interval | بازه‌ی Wald | برآورد ± 1.96 SE |
| profile likelihood | درست‌نمایی نیم‌رخ (profile) | درست‌نمایی یک پارامتر با بهینه کردن بقیه |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| bootstrap | bootstrap (بازنمونه‌گیری) | تخمین عدم قطعیت با شبیه‌سازی یا بازنمونه‌گیری |
| parameter trade-off | بده‌بستان پارامترها | تغییر یک پارامتر که با پارامتر دیگر جبران می‌شود |
| aggregation artifact | خطای ناشی از میانگین‌گیری | الگویی در میانگین که در هیچ فردی نیست |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| bounds / constraints | کران‌ها / قیدها | محدودیت‌های مجاز برای مقدار پارامترها |
| accuracy | دقت | نسبت پاسخ‌های درست |
| complete / no / partial pooling | ادغام کامل / بدون ادغام / ادغام جزئی (pooling) | یک پارامتر برای همه / جدا برای هر فرد / سلسله‌مراتبی |
| individual differences | تفاوت‌های فردی | فرق پارامترها بین افراد |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| benchmark | benchmark (مجموعه‌آزمون استاندارد) | مجموعه سؤال برای مقایسه‌ی مدل‌های هوش مصنوعی |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Explain** the sampling distribution of an estimator and **distinguish** a standard error from a standard deviation of the data.
2. **Compute** standard errors and confidence intervals for model parameters in three ways: from the Hessian of the NLL (Wald), from the profile likelihood, and by parametric bootstrap. **Compare** these three methods.
3. **Diagnose** parameter trade-offs from the estimated correlation between parameters.
4. **Demonstrate** by simulation that averaging individual curves can produce a functional form (a "power law") that no individual follows.
5. **Choose** between aggregate, individual and (preview) hierarchical fitting, and **justify** the choice.

<div dir="rtl">

1. توزیع نمونه‌گیری (sampling distribution) یک برآوردگر را **توضیح دهند** و خطای استاندارد (SE) را از انحراف معیار داده‌ها **متمایز کنند**.
2. خطاهای استاندارد و بازه‌های اطمینان پارامترهای مدل را به سه روش **حساب کنند**: از Hessian تابع NLL (روش Wald)، از profile likelihood و با bootstrap پارامتری؛ و این سه روش را **مقایسه کنند**.
3. trade-off پارامترها را از همبستگی برآوردشده بین پارامترها **تشخیص دهند**.
4. با شبیه‌سازی **نشان دهند** که میانگین‌گیری از منحنی‌های فردی می‌تواند شکل تابعی‌ای (یک «قانون توانی») بسازد که هیچ فردی از آن پیروی نمی‌کند.
5. بین برازش تجمیعی، فردی و (پیش‌نمایش) سلسله‌مراتبی **انتخاب کنند** و انتخابشان را **توجیه کنند**.

</div>

---

## Motivation & big picture · مقدمه

**"$\hat d = 0.42$" is half a result.** Last week the power model's MLE for the Week 2 data was $\hat d = 0.42$ (true value 0.5). Is 0.42 compatible with 0.5? With 0.3? With 0.6? Without a measure of uncertainty we cannot say whether two participants, two groups or two conditions really differ. Every parameter estimate we report from now on comes with a confidence interval.

<div dir="rtl">

**«$\hat d = 0.42$» نصف یک نتیجه است.** هفته‌ی قبل MLE مدل توانی برای داده‌های هفته‌ی 2 برابر $\hat d = 0.42$ بود (مقدار واقعی 0.5). آیا 0.42 با 0.5 سازگار است؟ با 0.3؟ با 0.6؟ بدون یک معیار عدم قطعیت نمی‌توانیم بگوییم دو شرکت‌کننده، دو گروه یا دو شرط واقعاً با هم فرق دارند یا نه. از این به بعد هر برآورد پارامتری که گزارش می‌کنیم با یک بازه‌ی اطمینان همراه است.

</div>

**The law that nobody obeys.** The *power law of practice* is one of the most cited regularities in cognitive psychology: response times fall with practice approximately as a power function of the number of trials. Some researchers have argued that the power shape can arise from **averaging** over people (or items) who each improve *exponentially* but at different rates (see Further reading). If so, the "law" describes the average but no single learner, and a theory built to explain a power function in each individual mind would be explaining an artifact. This week we demonstrate the effect with simulated data and learn when to fit individuals rather than group averages.

<div dir="rtl">

**قانونی که هیچ‌کس از آن پیروی نمی‌کند.** *قانون توانی تمرین* (power law of practice) یکی از پرارجاع‌ترین یافته‌ها در روان‌شناسی شناختی است: زمان واکنش با تمرین تقریباً به شکل تابع توانی از تعداد trialها کم می‌شود. بعضی پژوهشگران استدلال کرده‌اند که شکل توانی می‌تواند از **میانگین‌گیری** روی افرادی (یا آیتم‌هایی) بیاید که هرکدام به‌طور *نمایی* ولی با نرخ‌های متفاوت بهتر می‌شوند (مطالعه‌ی بیشتر را ببینید). اگر این‌طور باشد، «قانون» میانگین را توصیف می‌کند ولی هیچ یادگیرنده‌ی تکی را نه، و نظریه‌ای که برای توضیح یک تابع توانی در ذهن هر فرد ساخته شود در واقع یک خطای ناشی از میانگین‌گیری را توضیح می‌دهد. این هفته این اثر را با داده‌ی شبیه‌سازی‌شده نشان می‌دهیم و یاد می‌گیریم کی باید افراد را برازش کرد نه میانگین گروه را.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Any claim of a difference** ("patients forget faster than controls", "training improved sensitivity") needs uncertainty estimates. Without them a difference of 0.05 in a parameter may be pure noise.
- **Clinical assessment of individuals**: to say that one patient's memory decay is abnormal, you need the standard error of *that patient's* estimate, not only the group average.
- **Learning and skill research**: the "power law of practice" was long treated as a universal law. This week's aggregation artifact shows why researchers now fit individual learners (and why the same caution applies to group-averaged curves in education, sports science and human factors).
- **Replication and meta-analysis** combine estimates from many studies by weighting each one by its precision (1/SE²).

<div dir="rtl">

- **هر ادعای تفاوت** («بیماران سریع‌تر از گروه کنترل فراموش می‌کنند»، «آموزش حساسیت را بالا برد») به برآورد عدم قطعیت نیاز دارد. بدون آن، تفاوت 0.05 در یک پارامتر ممکن است فقط نویز باشد.
- **ارزیابی بالینی یک فرد:** برای اینکه بگوییم سرعت فراموشی یک بیمار غیرعادی است، به خطای استاندارد برآورد *همان بیمار* نیاز داریم، نه فقط میانگین گروه.
- **پژوهش یادگیری و مهارت:** «قانون توانی تمرین» مدت‌ها یک قانون همگانی حساب می‌شد. خطای ناشی از میانگین‌گیری این هفته نشان می‌دهد چرا امروز پژوهشگرها یادگیرنده‌ها را جداگانه برازش می‌کنند (و چرا همین احتیاط درباره‌ی منحنی‌های میانگین گروه در آموزش، علوم ورزشی و ارگونومی هم لازم است).
- **تکرار پژوهش و فراتحلیل (meta-analysis)** برآوردهای چند مطالعه را با وزن دادن به هر کدام بر اساس دقتش (1/SE²) ترکیب می‌کنند.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

If you ran the same experiment again on the same person, you would get slightly different data and therefore a slightly different parameter estimate. The **standard error (SE)** says how much the estimate would jump around between such repetitions; a **confidence interval** is a range built from it (roughly estimate ± 2 SE). We cannot repeat the experiment many times, so we estimate this jumping in three ways: (1) from how sharply peaked the likelihood is (a sharp peak means the data pin the parameter down; this is the **Wald** method using the **Hessian**), (2) by tracing how fast the fit gets worse as we move one parameter (**profile likelihood**), and (3) by simulating many fake experiments from the fitted model and refitting each (**bootstrap**). The second half of the week warns about a trap: averaging data across people can create a curve shape that **no single person** has. If every learner improves exponentially but at a different speed, the group average looks like a power law.

<div dir="rtl">

اگر همان آزمایش را دوباره روی همان آدم اجرا کنید، داده‌ی کمی متفاوت و در نتیجه برآورد پارامتر کمی متفاوتی می‌گیرید. **خطای استاندارد (SE)** می‌گوید برآورد بین چنین تکرارهایی چقدر بالا و پایین می‌پرد؛ **بازه‌ی اطمینان** محدوده‌ای است که از روی آن ساخته می‌شود (تقریباً برآورد ± 2 SE). نمی‌توانیم آزمایش را بارها تکرار کنیم، پس این پرش را به سه روش تخمین می‌زنیم: (1) از اینکه قله‌ی درست‌نمایی چقدر تیز است (قله‌ی تیز یعنی داده پارامتر را دقیق تعیین می‌کند؛ این روش **Wald** با استفاده از **Hessian** است)، (2) با دنبال کردن اینکه وقتی یک پارامتر را جابه‌جا می‌کنیم برازش با چه سرعتی بدتر می‌شود (**profile likelihood**)، و (3) با شبیه‌سازی تعداد زیادی آزمایش ساختگی از مدل برازش‌شده و برازش دوباره‌ی هرکدام (**bootstrap**). نیمه‌ی دوم هفته درباره‌ی یک دام هشدار می‌دهد: میانگین گرفتن داده‌ها روی افراد می‌تواند شکلی از منحنی بسازد که **هیچ فردی** آن را ندارد. اگر هر یادگیرنده به‌طور نمایی ولی با سرعتی متفاوت بهتر شود، میانگین گروه شبیه قانون توانی می‌شود.

</div>

**Suggested timing (60 min):** sampling distributions 10 · Hessian standard errors 15 · profile likelihood 8 · bootstrap 10 · multiple participants and aggregation 17.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** توزیع‌های نمونه‌گیری 10 · خطای استاندارد از Hessian 15 · profile likelihood 8 · bootstrap 10 · چند شرکت‌کننده و میانگین‌گیری 17.

</div>

### 1. Estimates have sampling distributions · 1. برآوردها توزیع نمونه‌گیری دارند

If we reran the same experiment on the same participant (same true $\boldsymbol\theta^\ast$), we would get different data and therefore a different $\hat{\boldsymbol\theta}$. The distribution of $\hat{\boldsymbol\theta}$ over hypothetical replications is its **sampling distribution**.

<div dir="rtl">

اگر همان آزمایش را روی همان شرکت‌کننده (با همان $\boldsymbol\theta^\ast$ واقعی) تکرار می‌کردیم، داده‌ی متفاوت و در نتیجه $\hat{\boldsymbol\theta}$ متفاوتی می‌گرفتیم. توزیع $\hat{\boldsymbol\theta}$ روی تکرارهای فرضی، **توزیع نمونه‌گیری** آن است.

</div>

- The **standard error** (SE) of a parameter is the SD of its sampling distribution: how much the *estimate* would vary across replications.
- A **95% confidence interval** is constructed by a procedure that, across replications, contains $\theta^\ast$ in 95% of cases. (It is *not* "a 95% probability that $\theta^\ast$ is in this particular interval"; that is a Bayesian credible interval, Week 9.)

<div dir="rtl">

- **خطای استاندارد** (SE) یک پارامتر، انحراف معیار توزیع نمونه‌گیری‌اش است: اینکه *برآورد* بین تکرارها چقدر تغییر می‌کند.
- یک **بازه‌ی اطمینان 95%** با رویه‌ای ساخته می‌شود که در تکرارها، در 95% موارد $\theta^\ast$ را در بر می‌گیرد. (این *نه* به معنای «احتمال 95% که $\theta^\ast$ در همین بازه‌ی مشخص باشد» است؛ آن یک credible interval بیزی است، هفته‌ی 9.)

</div>

We cannot rerun the experiment many times, so we approximate the sampling distribution in three ways.

<div dir="rtl">

نمی‌توانیم آزمایش را بارها تکرار کنیم، پس توزیع نمونه‌گیری را به سه روش تقریب می‌زنیم.

</div>

### 2. Standard errors from the curvature of the likelihood (Wald) · 2. خطای استاندارد از انحنای درست‌نمایی (Wald)

**Intuition.** If the NLL has a sharp, narrow minimum, small changes in $\boldsymbol\theta$ make the data much less likely, so the data pin $\boldsymbol\theta$ down precisely. A flat, wide minimum means many values fit almost equally well, so the uncertainty is large. Curvature is measured by second derivatives.

<div dir="rtl">

**شهود.** اگر NLL یک کمینه‌ی تیز و باریک داشته باشد، تغییرات کوچک در $\boldsymbol\theta$ داده‌ها را خیلی کم‌احتمال‌تر می‌کنند، پس داده‌ها $\boldsymbol\theta$ را دقیق تعیین می‌کنند. یک کمینه‌ی پهن و تخت یعنی مقادیر زیادی تقریباً به یک اندازه خوب برازش می‌شوند، پس عدم قطعیت زیاد است. انحنا با مشتق‌های دوم اندازه‌گیری می‌شود.

</div>

**Formalism.** The **Hessian** of the NLL at the MLE is the matrix of second derivatives,

<div dir="rtl">

**صورت‌بندی.** **Hessian** تابع NLL در نقطه‌ی MLE ماتریس مشتق‌های دوم است،

</div>

$$
\mathbf{H}_{mn} = \frac{\partial^2\, \mathrm{NLL}(\boldsymbol\theta)}{\partial\theta_m\,\partial\theta_n}\bigg|_{\boldsymbol\theta = \hat{\boldsymbol\theta}},
$$

also called the **observed Fisher information**. For large samples,

<div dir="rtl">

که به آن **اطلاع فیشر مشاهده‌شده** (observed Fisher information) هم می‌گویند. برای نمونه‌های بزرگ:

</div>

$$
\widehat{\mathrm{Cov}}(\hat{\boldsymbol\theta}) \approx \mathbf{H}^{-1}, \qquad
\mathrm{SE}(\hat\theta_m) = \sqrt{[\mathbf{H}^{-1}]_{mm}}, \qquad
\text{95\% Wald CI: } \hat\theta_m \pm 1.96\,\mathrm{SE}(\hat\theta_m).
$$

The off-diagonal elements of $\mathbf{H}^{-1}$, rescaled to correlations, show **parameter trade-offs**: a correlation of −0.9 between two estimates means their errors largely compensate each other (the tilted valley of Week 3).

<div dir="rtl">

عناصر غیرقطری $\mathbf{H}^{-1}$، وقتی به همبستگی تبدیل شوند، **trade-off پارامترها** را نشان می‌دهند: همبستگی 0.9− بین دو برآورد یعنی خطاهایشان تا حد زیادی همدیگر را جبران می‌کنند (همان دره‌ی مورب هفته‌ی 3).

</div>

**Sanity check (binomial).** For one proportion, $\mathrm{NLL}''(\theta) = y/\theta^2 + (n-y)/(1-\theta)^2$. At $\hat\theta = y/n$ this equals $n / [\hat\theta(1-\hat\theta)]$, so $\mathrm{SE} = \sqrt{\hat\theta(1-\hat\theta)/n}$, the familiar textbook formula.

<div dir="rtl">

**بررسی درستی (دوجمله‌ای).** برای یک نسبت، $\mathrm{NLL}''(\theta) = y/\theta^2 + (n-y)/(1-\theta)^2$. در $\hat\theta = y/n$ این برابر $n / [\hat\theta(1-\hat\theta)]$ است، پس $\mathrm{SE} = \sqrt{\hat\theta(1-\hat\theta)/n}$؛ همان فرمول آشنای کتاب‌های درسی.

</div>

**In practice:** compute $\mathbf{H}$ numerically by finite differences (lab Part A). The `hess_inv` returned by BFGS is only a rough approximation, so do not use it for SEs.

<div dir="rtl">

**در عمل:** $\mathbf{H}$ را عددی با تفاضل‌های متناهی حساب کنید (بخش A lab). `hess_inv` که BFGS برمی‌گرداند فقط یک تقریب خام است، پس برای SE از آن استفاده نکنید.

</div>

**When Wald fails:** small samples, estimates near a bound (e.g., a recall level $\hat A$ close to 1), strongly non-quadratic likelihoods, or parameters with skewed sampling distributions (rates, variances). Then the symmetric $\pm 1.96$ SE interval can extend into impossible values.

<div dir="rtl">

**وقتی Wald جواب نمی‌دهد:** نمونه‌های کوچک، برآوردهای نزدیک یک کران (مثلاً سطح یادآوری $\hat A$ نزدیک 1)، درست‌نمایی‌هایی که شدیداً غیرمربعی‌اند، یا پارامترهایی با توزیع نمونه‌گیری چوله (نرخ‌ها، واریانس‌ها). در این حالت‌ها بازه‌ی متقارن $\pm 1.96$ SE ممکن است تا مقادیر ناممکن کشیده شود.

</div>

> **Advanced: why this works.** Near its minimum, any smooth NLL is approximately quadratic (second-order Taylor expansion). A quadratic NLL is exactly the NLL of a multivariate normal distribution whose inverse covariance is the Hessian. Combined with the asymptotic normality of the MLE (Week 4), this gives the result. The same quadratic approximation, called the *Laplace approximation*, reappears in Bayesian model comparison (Week 10).

<div dir="rtl">

> **پیشرفته: چرا این کار می‌کند.** نزدیک کمینه، هر NLL همواری تقریباً مربعی است (بسط تیلور مرتبه‌ی دوم). یک NLL مربعی دقیقاً NLL یک توزیع نرمال چندمتغیره است که معکوس کوواریانسش همان Hessian است. همراه با نرمال بودن مجانبی MLE (هفته‌ی 4)، این نتیجه را می‌دهد. همین تقریب مربعی، به نام *تقریب Laplace*، در مقایسه‌ی بیزی مدل‌ها (هفته‌ی 10) دوباره ظاهر می‌شود.

</div>

#### Reading the math · خواندن ریاضی

- $\mathbf{H}_{mn} = \partial^2 \mathrm{NLL}/\partial\theta_m\partial\theta_n$ at $\hat{\boldsymbol\theta}$: the matrix of second derivatives, i.e. the **curvature** of the NLL bowl at its bottom. Diagonal entries: how steep the bowl is along each parameter. Off-diagonal entries: whether the bowl is tilted (parameters trade off).
- $\widehat{\mathrm{Cov}}(\hat{\boldsymbol\theta}) \approx \mathbf{H}^{-1}$: a sharply curved bowl (large $\mathbf{H}$) gives a small covariance, i.e. precise estimates. Taking the inverse is what turns "steepness" into "uncertainty".
- $\mathrm{SE}(\hat\theta_m) = \sqrt{[\mathbf{H}^{-1}]_{mm}}$: take the $m$-th diagonal entry of the inverse and its square root.
- **One-parameter check:** for a proportion, $\mathrm{NLL}'' = n/[\hat\theta(1-\hat\theta)]$, so $\mathrm{SE} = \sqrt{\hat\theta(1-\hat\theta)/n}$. With 30 of 50 recalled: $\sqrt{0.6 \times 0.4/50} = 0.069$, and the 95% interval is $0.60 \pm 1.96 \times 0.069 = [0.46, 0.74]$.
- **Correlation from the covariance:** $\mathrm{corr} = \mathrm{Cov}_{12}/(\mathrm{SE}_1\mathrm{SE}_2)$. A value like −0.9 means the two estimates are strongly traded off.

<div dir="rtl">

- $\mathbf{H}_{mn} = \partial^2 \mathrm{NLL}/\partial\theta_m\partial\theta_n$ در نقطه‌ی $\hat{\boldsymbol\theta}$: ماتریس مشتق‌های دوم، یعنی **انحنای** کاسه‌ی NLL در کف آن. درایه‌های قطری: کاسه در امتداد هر پارامتر چقدر شیب‌دار است. درایه‌های غیرقطری: آیا کاسه کج است (پارامترها trade-off دارند).
- $\widehat{\mathrm{Cov}}(\hat{\boldsymbol\theta}) \approx \mathbf{H}^{-1}$: کاسه‌ی خیلی خمیده ($\mathbf{H}$ بزرگ) کوواریانس کوچک می‌دهد، یعنی برآورد دقیق. معکوس گرفتن همان چیزی است که «شیب‌داری» را به «عدم قطعیت» تبدیل می‌کند.
- $\mathrm{SE}(\hat\theta_m) = \sqrt{[\mathbf{H}^{-1}]_{mm}}$: درایه‌ی قطری $m$ام ماتریس معکوس را بردارید و از آن جذر بگیرید.
- **بررسی با یک پارامتر:** برای یک نسبت، $\mathrm{NLL}'' = n/[\hat\theta(1-\hat\theta)]$، پس $\mathrm{SE} = \sqrt{\hat\theta(1-\hat\theta)/n}$. با 30 از 50: $\sqrt{0.6 \times 0.4/50} = 0.069$ و بازه‌ی 95% برابر $0.60 \pm 1.96 \times 0.069 = [0.46, 0.74]$ است.
- **همبستگی از کوواریانس:** $\mathrm{corr} = \mathrm{Cov}_{12}/(\mathrm{SE}_1\mathrm{SE}_2)$. مقداری مثل −0.9 یعنی دو برآورد به‌شدت trade-off دارند.

</div>

### 3. Profile likelihood intervals · 3. بازه‌های profile likelihood

For a parameter of interest $\psi$ (say $d$), the **profile NLL** is obtained by fixing $\psi$ on a grid and minimizing the NLL over all *other* parameters at each grid value:

<div dir="rtl">

برای پارامتر مورد نظر $\psi$ (مثلاً $d$)، **NLL profile** با ثابت گرفتن $\psi$ روی یک شبکه و کمینه کردن NLL روی همه‌ی پارامترهای *دیگر* در هر نقطه‌ی شبکه به دست می‌آید:

</div>

$$
\mathrm{NLL}_{\text{prof}}(\psi) = \min_{\text{other params}} \mathrm{NLL}(\psi, \text{others}).
$$

The 95% **likelihood-ratio (profile) interval** is the set of $\psi$ values that are not much worse than the best:

<div dir="rtl">

**بازه‌ی نسبت درست‌نمایی (profile)** 95%، مجموعه‌ی مقادیری از $\psi$ است که خیلی بدتر از بهترین نیستند:

</div>

$$
\big\{\psi : 2\,[\mathrm{NLL}_{\text{prof}}(\psi) - \mathrm{NLL}_{\min}] \le 3.84\big\}, \qquad 3.84 = \chi^2_{1,\,0.95}.
$$

Profile intervals follow the actual shape of the likelihood, so they can be **asymmetric** and respect natural bounds. They are usually more accurate than Wald intervals in small samples.

<div dir="rtl">

بازه‌های profile شکل واقعی درست‌نمایی را دنبال می‌کنند، پس می‌توانند **نامتقارن** باشند و کران‌های طبیعی را رعایت کنند. در نمونه‌های کوچک معمولاً از بازه‌های Wald دقیق‌ترند.

</div>

#### Reading the math · خواندن ریاضی

- $\mathrm{NLL}_{\text{prof}}(\psi)$: fix the parameter of interest $\psi$ at one value, let the optimizer choose the best values of all *other* parameters, and record the resulting NLL. Repeat for many values of $\psi$. The result is a 1-D curve.
- The interval keeps every $\psi$ whose profile NLL is within $3.84/2 = 1.92$ units of the minimum. The number 3.84 is the 95% point of a $\chi^2$ distribution with 1 df; it comes from the likelihood-ratio test (Week 7).
- Unlike Wald, the curve is not forced to be a symmetric parabola, so the interval can be lopsided and never extends to impossible values.

<div dir="rtl">

- $\mathrm{NLL}_{\text{prof}}(\psi)$: پارامتر مورد نظر $\psi$ را روی یک مقدار ثابت کنید، بگذارید بهینه‌ساز بهترین مقدار همه‌ی پارامترهای *دیگر* را انتخاب کند، و NLL حاصل را ثبت کنید. برای مقدارهای زیادی از $\psi$ تکرار کنید. نتیجه یک منحنی یک‌بعدی است.
- بازه هر $\psi$ای را نگه می‌دارد که NLL نیم‌رخ آن حداکثر $3.84/2 = 1.92$ واحد بالاتر از کمینه باشد. عدد 3.84 نقطه‌ی 95% توزیع $\chi^2$ با 1 درجه‌ی آزادی است و از آزمون نسبت درست‌نمایی می‌آید (هفته‌ی 7).
- برخلاف Wald، این منحنی مجبور نیست سهمی متقارن باشد، پس بازه می‌تواند نامتقارن باشد و هیچ‌وقت تا مقدارهای ناممکن کشیده نمی‌شود.

</div>

### 4. The parametric bootstrap · 4. bootstrap پارامتری

A simulation answer to "what if we reran the experiment?":

<div dir="rtl">

جوابی شبیه‌سازی‌محور به «اگر آزمایش را تکرار می‌کردیم چه؟»:

</div>

1. Fit the model to the data: $\hat{\boldsymbol\theta}$.
2. Simulate $B$ new datasets from the model at $\hat{\boldsymbol\theta}$, with the same design as the real experiment.
3. Refit each dataset: $\hat{\boldsymbol\theta}^{*(1)}, \dots, \hat{\boldsymbol\theta}^{*(B)}$.
4. The SD of the bootstrap estimates approximates the SE. The 2.5th and 97.5th percentiles give a **percentile CI**.

<div dir="rtl">

1. مدل را روی داده برازش کنید: $\hat{\boldsymbol\theta}$.
2. $B$ مجموعه‌داده‌ی جدید از مدل با $\hat{\boldsymbol\theta}$ و با همان طرح آزمایش واقعی شبیه‌سازی کنید.
3. هر مجموعه‌داده را دوباره برازش کنید: $\hat{\boldsymbol\theta}^{*(1)}, \dots, \hat{\boldsymbol\theta}^{*(B)}$.
4. انحراف معیار برآوردهای bootstrap تقریب SE است. صدک‌های 2.5 و 97.5 یک **بازه‌ی اطمینان صدکی** (percentile CI) می‌دهند.

</div>

The bootstrap needs no derivatives, works for any statistic (e.g., a half-life, a difference between conditions), and shows the full shape and correlations of the sampling distribution. Its cost is $B$ refits ($B \approx 500$–$2000$). The **non-parametric** bootstrap resamples the observed trials with replacement instead of simulating from the model.

<div dir="rtl">

bootstrap به مشتق نیاز ندارد، برای هر آماره‌ای کار می‌کند (مثلاً نیمه‌عمر یا تفاوت دو شرط)، و شکل کامل و همبستگی‌های توزیع نمونه‌گیری را نشان می‌دهد. هزینه‌اش $B$ بار برازش است ($B \approx 500$ تا $2000$). bootstrap **ناپارامتری** به‌جای شبیه‌سازی از مدل، trialهای مشاهده‌شده را با جایگذاری بازنمونه‌گیری می‌کند.

</div>

**Comparison:**

<div dir="rtl">

**مقایسه:**

</div>

| Method | Cost | Symmetric? | Handles bounds? | Needs |
|---|---|---|---|---|
| Wald (Hessian) | One Hessian | Always | No | Smooth NLL, large $N$ |
| Profile likelihood | One fit per grid value | Can be asymmetric | Yes | A likelihood |
| Parametric bootstrap | $B$ fits | Can be asymmetric | Yes | A model you can simulate |

<div dir="rtl">

| روش | هزینه | متقارن؟ | کران را رعایت می‌کند؟ | نیاز دارد به |
|---|---|---|---|---|
| Wald (Hessian) | یک Hessian | همیشه | نه | NLL هموار، $N$ بزرگ |
| profile likelihood | یک برازش برای هر نقطه‌ی شبکه | می‌تواند نامتقارن باشد | بله | یک درست‌نمایی |
| bootstrap پارامتری | $B$ برازش | می‌تواند نامتقارن باشد | بله | مدلی که بتوانید شبیه‌سازی کنید |

</div>

### 5. Fitting multiple participants · 5. برازش برای چند شرکت‌کننده

Real experiments have $J$ participants (index $j$). There are three broad strategies:

<div dir="rtl">

آزمایش‌های واقعی $J$ شرکت‌کننده دارند (اندیس $j$). سه راهبرد کلی وجود دارد:

</div>

| Strategy | What is fitted | Pros | Cons |
|---|---|---|---|
| **Aggregate** (complete pooling) | One model to the averaged data | Stable; works with few trials per person | Assumes everyone is the same; **can distort the functional form** |
| **Individual** (no pooling) | One model per participant; then analyze the $J$ sets of estimates | Respects individual differences; standard practice | Noisy estimates with few trials; second-stage analysis ignores estimation uncertainty |
| **Hierarchical** (partial pooling) | Individual parameters drawn from a group distribution, estimated jointly | Best of both; principled shrinkage | More complex; usually Bayesian (Week 13) |

<div dir="rtl">

| راهبرد | چه چیزی برازش می‌شود | مزایا | معایب |
|---|---|---|---|
| **تجمیعی** (complete pooling) | یک مدل روی داده‌های میانگین‌گیری‌شده | پایدار؛ با trialهای کم برای هر نفر هم کار می‌کند | فرض می‌کند همه یکسان‌اند؛ **می‌تواند شکل تابعی را تحریف کند** |
| **فردی** (no pooling) | یک مدل برای هر شرکت‌کننده؛ بعد تحلیل $J$ مجموعه برآورد | تفاوت‌های فردی را رعایت می‌کند؛ روش استاندارد | با trial کم برآوردها پرنویزند؛ تحلیل مرحله‌ی دوم عدم قطعیت برآورد را نادیده می‌گیرد |
| **سلسله‌مراتبی** (partial pooling) | پارامترهای فردی از یک توزیع گروهی، که با هم برآورد می‌شوند | بهترینِ هر دو؛ shrinkage اصولی | پیچیده‌تر؛ معمولاً بیزی (هفته‌ی 13) |

</div>

**Aggregation artifacts.** The average of nonlinear curves is generally **not** a curve of the same family. For example, averaging exponential curves with different rates does not give an exponential: fast learners finish early, so the average's relative rate of change *slows down* over time, which is the defining property of a power function (Week 2, relative loss rate).

<div dir="rtl">

**خطاهای ناشی از میانگین‌گیری.** میانگین منحنی‌های غیرخطی معمولاً منحنی‌ای از همان خانواده **نیست**. مثلاً میانگین منحنی‌های نمایی با نرخ‌های متفاوت نمایی نمی‌شود: یادگیرنده‌های سریع زود به پایان می‌رسند، پس نرخ نسبی تغییر میانگین با گذشت زمان *کند می‌شود*؛ و این دقیقاً ویژگی تعریف‌کننده‌ی تابع توانی است (هفته‌ی 2، نرخ نسبی فراموشی).

</div>

> **Advanced: an exact result.** Suppose each participant follows $e^{-\lambda_j t}$ and the rates are Gamma-distributed across people, $\lambda_j \sim \mathrm{Gamma}(\text{shape } s, \text{rate } b)$. Then the group average curve is
> $$\mathbb{E}\big[e^{-\lambda t}\big] = \Big(1 + \frac{t}{b}\Big)^{-s},$$
> which is *exactly* a shifted power function (this is the moment-generating function of the Gamma distribution, evaluated at $-t$). Everyone forgets exponentially, yet the average forgets by a power law with exponent equal to the Gamma shape $s$. You verify this numerically in Exercise 4.

<div dir="rtl">

> **پیشرفته: یک نتیجه‌ی دقیق.** فرض کنید هر شرکت‌کننده از $e^{-\lambda_j t}$ پیروی کند و نرخ‌ها بین افراد توزیع Gamma داشته باشند، $\lambda_j \sim \mathrm{Gamma}(\text{shape } s, \text{rate } b)$. آن‌وقت منحنی میانگین گروه برابر است با
> $$\mathbb{E}\big[e^{-\lambda t}\big] = \Big(1 + \frac{t}{b}\Big)^{-s},$$
> که *دقیقاً* یک تابع توانی جابه‌جاشده است (این تابع مولد گشتاور توزیع Gamma در نقطه‌ی $-t$ است). همه به‌طور نمایی فراموش می‌کنند، ولی میانگین با یک قانون توانی با نمای برابر با پارامتر شکل Gamma یعنی $s$ فراموش می‌کند. این را در تمرین 4 عددی بررسی می‌کنید.

</div>

**Practical guideline.** Fit individuals whenever each participant has enough data to constrain the model; use the aggregate only as a summary, never as evidence about the *form* of an individual-level process. When individual data are sparse, use hierarchical models (Week 13).

<div dir="rtl">

**راهنمای عملی.** هر وقت هر شرکت‌کننده داده‌ی کافی برای مقید کردن مدل دارد، افراد را برازش کنید؛ داده‌ی تجمیعی را فقط به‌عنوان خلاصه به کار ببرید، هرگز به‌عنوان شاهدی درباره‌ی *شکل* یک فرایند در سطح فرد. وقتی داده‌های فردی کم است، از مدل‌های سلسله‌مراتبی استفاده کنید (هفته‌ی 13).

</div>

#### For an engineer · برای یک مهندس

- **Wald SE from the Hessian** = the inverse Fisher information, i.e. the **CRLB** evaluated at the estimate. MLE reaches the bound asymptotically, so for large $N$ the Wald interval is the CRLB-based interval.
- **The parametric bootstrap** is the Monte Carlo performance evaluation you do for an estimator or a receiver (e.g. simulating many noise realizations to get an estimator's variance or a BER curve), done at the fitted parameter values.
- **Profile likelihood** is what you do when you have *nuisance parameters*: optimize them out and look at the likelihood of the parameter you care about.
- **Aggregation artifact** = the difference between an **ensemble average** and a **single realization**. Averaging exponential decays with different time constants gives a slower, heavy-tailed decay, just as the average of many channel realizations does not look like any one realization. The process is not "ergodic across people": the group mean does not describe the individual.
- **Partial pooling** (preview of Week 13) is like estimating each user's SNR by combining their own few measurements with the distribution of SNRs in the whole cell: an empirical-Bayes estimate.

<div dir="rtl">

- **SE روش Wald از Hessian** = معکوس اطلاعات فیشر، یعنی همان **CRLB** که در نقطه‌ی برآورد محاسبه شده. MLE به‌طور مجانبی به این کران می‌رسد، پس برای $N$ بزرگ بازه‌ی Wald همان بازه‌ی مبتنی بر CRLB است.
- **bootstrap پارامتری** همان ارزیابی کارایی با Monte Carlo است که برای یک تخمین‌گر یا گیرنده انجام می‌دهید (مثلاً شبیه‌سازی تعداد زیادی تحقق نویز برای به دست آوردن واریانس تخمین‌گر یا منحنی BER)، فقط در مقدارهای برازش‌شده‌ی پارامتر.
- **profile likelihood** همان کاری است که با *پارامترهای مزاحم (nuisance parameters)* می‌کنید: آن‌ها را بهینه کنید و کنار بگذارید و به درست‌نمایی پارامتری که برایتان مهم است نگاه کنید.
- **خطای ناشی از میانگین‌گیری** = تفاوت **میانگین آنسامبل** و **یک تحقق تنها**. میانگین گرفتن از افت‌های نمایی با ثابت‌های زمانی مختلف یک افت کندتر با دنباله‌ی سنگین می‌دهد؛ همان‌طور که میانگین تعداد زیادی تحقق کانال شبیه هیچ تحقق تکی نیست. فرایند «بین افراد ارگودیک» نیست: میانگین گروه، فرد را توصیف نمی‌کند.
- **partial pooling** (پیش‌نمایش هفته‌ی 13) شبیه تخمین SNR هر کاربر با ترکیب چند اندازه‌گیری خودش و توزیع SNR در کل سلول است: یک برآورد empirical Bayes.

</div>

#### For the instructor · برای مدرس

- **Start with the question "is 0.42 different from 0.5?"** (Motivation). Students will want a yes/no; show that the answer depends entirely on the SE.
- **Show the three methods side by side** on the same data (lab Part C table). The message is not "which is correct" but "they agree when the likelihood is well-behaved, and differ near bounds or with little data".
- **The aggregation demo is the highlight.** Plot 5 individual exponential curves and their average on a log–log plot: the average is almost a straight line (power law), while each individual is curved. Ask the class what a researcher who only saw the average would conclude.
- **Typical questions.**
  - *"What is the difference between SD and SE?"* SD describes the spread of the *data*; SE describes the spread of an *estimate* across repeated experiments. SE shrinks with more data; SD does not.
  - *"Does a 95% CI contain the true value with probability 0.95?"* Not this particular interval; 95% of intervals built this way would. (The Bayesian credible interval of Week 9 does have the direct reading.)
  - *"Should I always fit individuals?"* Yes, if each person has enough data; otherwise use hierarchical models (Week 13).

<div dir="rtl">

- **با سؤال «آیا 0.42 با 0.5 فرق دارد؟» شروع کنید** (بخش مقدمه). دانشجوها جواب بله/نه می‌خواهند؛ نشان دهید جواب کاملاً به SE بستگی دارد.
- **سه روش را کنار هم نشان دهید** روی همان داده (جدول بخش C lab). پیام این نیست که «کدام درست است»، بلکه «وقتی درست‌نمایی خوش‌رفتار است با هم توافق دارند و نزدیک کران‌ها یا با داده‌ی کم فرق می‌کنند».
- **نمایش میانگین‌گیری نقطه‌ی اوج جلسه است.** 5 منحنی نمایی فردی و میانگین آن‌ها را روی نمودار لگاریتمی–لگاریتمی رسم کنید: میانگین تقریباً یک خط راست است (قانون توانی) در حالی که هر منحنی فردی خمیده است. از کلاس بپرسید پژوهشگری که فقط میانگین را دیده چه نتیجه‌ای می‌گیرد.
- **سؤال‌های رایج.**
  - *«فرق SD و SE چیست؟»* SD پراکندگی *داده‌ها* را توصیف می‌کند؛ SE پراکندگی یک *برآورد* در تکرارهای آزمایش را. SE با داده‌ی بیشتر کم می‌شود؛ SD نه.
  - *«آیا یک بازه‌ی اطمینان 95% با احتمال 0.95 مقدار واقعی را دارد؟»* این بازه‌ی مشخص نه؛ 95% بازه‌هایی که به این روش ساخته می‌شوند آن را دارند. (credible interval بیزی هفته‌ی 9 همین تفسیر مستقیم را دارد.)
  - *«آیا همیشه باید افراد را جداگانه برازش کنم؟»* بله، اگر هر نفر داده‌ی کافی دارد؛ وگرنه از مدل‌های سلسله‌مراتبی استفاده کنید (هفته‌ی 13).

</div>

---

## Worked example · مثال حل‌شده

### Part 1: three intervals for a recall probability · بخش 1: سه بازه برای یک احتمال یادآوری

A participant recalls $y = 30$ of $n = 50$ items; $\hat\theta = 0.60$.

<div dir="rtl">

یک شرکت‌کننده $y = 30$ از $n = 50$ آیتم را به یاد می‌آورد؛ $\hat\theta = 0.60$.

</div>

**Wald.** $\mathrm{SE} = \sqrt{0.6 \times 0.4 / 50} = 0.0693$, so the 95% CI is $0.60 \pm 1.96 \times 0.0693 = [0.464, 0.736]$.

<div dir="rtl">

**Wald.** $\mathrm{SE} = \sqrt{0.6 \times 0.4 / 50} = 0.0693$، پس بازه‌ی اطمینان 95% برابر $0.60 \pm 1.96 \times 0.0693 = [0.464, 0.736]$ است.

</div>

**Profile (likelihood ratio).** Solve $2[\ell(0.6) - \ell(\theta)] = 3.84$ numerically on both sides of 0.6. The 95% CI is $[0.462, 0.728]$, slightly **asymmetric**: it extends 0.138 below the estimate and 0.128 above, because the likelihood is skewed toward 0.5, where binomial variance is largest.

<div dir="rtl">

**profile (نسبت درست‌نمایی).** معادله‌ی $2[\ell(0.6) - \ell(\theta)] = 3.84$ را در دو طرف 0.6 عددی حل کنید. بازه‌ی 95% برابر $[0.462, 0.728]$ است که کمی **نامتقارن** است: 0.138 پایین‌تر از برآورد و 0.128 بالاتر از آن می‌رود، چون درست‌نمایی به سمت 0.5، جایی که واریانس دوجمله‌ای بیشینه است، چوله است.

</div>

**Interpretation.** With 50 items, a recall probability is only known to about ±0.13. A difference of 0.10 between two conditions of this size would not be convincing on its own.

<div dir="rtl">

**تفسیر.** با 50 آیتم، یک احتمال یادآوری فقط تا حدود ±0.13 معلوم است. تفاوت 0.10 بین دو شرط با این اندازه به‌تنهایی قانع‌کننده نیست.

</div>

### Part 2: averaging two exponential learners · بخش 2: میانگین‌گیری از دو یادگیرنده‌ی نمایی

Participant 1 forgets at $\lambda = 0.1$, participant 2 at $\lambda = 1.0$. The average curve $\bar f(t) = (e^{-0.1t} + e^{-t})/2$:

<div dir="rtl">

شرکت‌کننده‌ی 1 با $\lambda = 0.1$ و شرکت‌کننده‌ی 2 با $\lambda = 1.0$ فراموش می‌کند. منحنی میانگین $\bar f(t) = (e^{-0.1t} + e^{-t})/2$:

</div>

| $t$ | 0 | 1 | 2 | 5 | 10 |
|---|---|---|---|---|---|
| $\bar f(t)$ | 1.000 | 0.636 | 0.477 | 0.307 | 0.184 |
| Relative loss rate $-\bar f'(t)/\bar f(t)$ | 0.55 | 0.36 | 0.23 | 0.11 | 0.10 |

<div dir="rtl">

| $t$ | 0 | 1 | 2 | 5 | 10 |
|---|---|---|---|---|---|
| $\bar f(t)$ | 1.000 | 0.636 | 0.477 | 0.307 | 0.184 |
| نرخ نسبی فراموشی $-\bar f'(t)/\bar f(t)$ | 0.55 | 0.36 | 0.23 | 0.11 | 0.10 |

</div>

Each participant has a *constant* relative loss rate (0.1 and 1.0), but the average's rate **falls** from 0.55 to 0.10, the signature of a power-like curve. The reason: at later times the average is dominated by the slow forgetter, whose rate is low. **Interpretation:** a researcher fitting only the average would conclude that "memories become more resistant with age", a claim true of neither participant.

<div dir="rtl">

هر شرکت‌کننده یک نرخ نسبی *ثابت* دارد (0.1 و 1.0)، ولی نرخ میانگین از 0.55 به 0.10 **کاهش** می‌یابد؛ نشانه‌ی یک منحنی شبه‌توانی. دلیل: در زمان‌های بعدی، فراموش‌کننده‌ی کند که نرخش پایین است بر میانگین غالب است. **تفسیر:** پژوهشگری که فقط میانگین را برازش کند نتیجه می‌گیرد که «خاطره‌ها با بالا رفتن سن مقاوم‌تر می‌شوند»؛ ادعایی که درباره‌ی هیچ‌کدام از دو شرکت‌کننده درست نیست.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Compute Wald, profile and bootstrap intervals for the power model fitted to the Week 2 data, and compare them.
2. Visualize parameter trade-offs through the estimated correlation and the bootstrap cloud.
3. Simulate 20 exponential learners, fit exponential and power models to the **average** and to **each individual**, and interpret the contradiction.

<div dir="rtl">

1. محاسبه‌ی بازه‌های Wald، profile و bootstrap برای مدل توانی برازش‌شده روی داده‌های هفته‌ی 2 و مقایسه‌ی آن‌ها.
2. نمایش trade-off پارامترها از طریق همبستگی برآوردشده و ابر نقاط bootstrap.
3. شبیه‌سازی 20 یادگیرنده‌ی نمایی، برازش مدل‌های نمایی و توانی روی **میانگین** و روی **هر فرد**، و تفسیر تناقض.

</div>

**Timing:** Part A 20 min · Part B 15 min · Part C 25 min · Part D 40 min · Part E 20 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 20 دقیقه · بخش B 15 دقیقه · بخش C 25 دقیقه · بخش D 40 دقیقه · بخش E 20 دقیقه.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 1 · سلول 1

### Part A: Wald standard errors from a numerical Hessian (20 min) · بخش A: خطای استاندارد Wald از یک Hessian عددی (20 دقیقه)

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
   estimate      SE   lower   upper
A    0.8773  0.0626  0.7546  1.0000
d    0.4214  0.0532  0.3171  0.5257
Estimated correlation between A-hat and d-hat: 0.751
```

**Interpret:** both 95% intervals contain the true values ($A^\ast = 0.9$, $d^\ast = 0.5$), so the "miss" we worried about in Weeks 3–4 is well within sampling error. Note that the Wald interval for $A$ happens to end at 1.000, right at the boundary of possible values. With slightly noisier data, the symmetric Wald interval would include impossible values (probabilities above 1), whereas the bootstrap interval cannot. The positive correlation is the trade-off valley from Week 3: when the estimate of $A$ is too high, the estimate of $d$ tends to be too high as well.

<div dir="rtl">

**تفسیر:** هر دو بازه‌ی 95% مقادیر واقعی ($A^\ast = 0.9$، $d^\ast = 0.5$) را در بر دارند، پس «خطایی» که در هفته‌های 3–4 نگرانش بودیم کاملاً در حد خطای نمونه‌گیری است. دقت کنید که بازه‌ی Wald برای $A$ اتفاقاً درست روی 1.000، یعنی مرز مقادیر ممکن، تمام می‌شود. با داده‌ای کمی پرنویزتر، بازه‌ی متقارن Wald مقادیر ناممکن (احتمال بیشتر از 1) را هم شامل می‌شد، در حالی که بازه‌ی bootstrap نمی‌تواند. همبستگی مثبت همان دره‌ی trade-off هفته‌ی 3 است: وقتی برآورد $A$ زیادی بالاست، برآورد $d$ هم معمولاً زیادی بالاست.

</div>

### Part B: profile likelihood interval for $d$ (15 min) · بخش B: بازه‌ی profile likelihood برای $d$ (15 دقیقه)

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Profile 95% CI for d: [0.320, 0.525]  (grid step 0.005)
```

### Part C: parametric bootstrap (25 min) · بخش C: bootstrap پارامتری (25 دقیقه)

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 4 · سلول 4

**Expected output** (takes about 30–60 s):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 30 تا 60 ثانیه طول می‌کشد):

</div>

```text
   boot SE    2.5%  97.5%
A   0.0563  0.7724  1.000
d   0.0501  0.3304  0.528
Bootstrap correlation: 0.703
```

**Compare:** put the Wald, profile and bootstrap intervals for $d$ side by side. Are they similar? Which is asymmetric? With these data (8 cells × 50 items) all three methods should agree reasonably well. They diverge more with fewer items or with estimates near a bound (Exercise 5).

<div dir="rtl">

**مقایسه کنید:** بازه‌های Wald، profile و bootstrap برای $d$ را کنار هم بگذارید. شبیه هم‌اند؟ کدام نامتقارن است؟ با این داده‌ها (8 خانه × 50 آیتم) هر سه روش باید نسبتاً با هم توافق داشته باشند. با آیتم‌های کمتر یا برآوردهای نزدیک کران بیشتر از هم فاصله می‌گیرند (تمرین 5).

</div>

### Part D: the power law of practice as an aggregation artifact (40 min) · بخش D: قانون توانی تمرین به‌عنوان خطای میانگین‌گیری (40 دقیقه)

**Design.** $J = 20$ participants each complete 60 practice blocks of a visual-search task. Each participant improves **exponentially**:

<div dir="rtl">

**طرح.** $J = 20$ شرکت‌کننده هرکدام 60 بلوک تمرین در یک تکلیف جستجوی دیداری انجام می‌دهند. هر شرکت‌کننده به‌طور **نمایی** بهتر می‌شود:

</div>

$$
\mathrm{RT}_j(m) = E + B\,e^{-r_j (m-1)} + \varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, 40 \text{ ms}),
$$

with asymptote $E = 400$ ms, initial gain $B = 600$ ms, and individual learning rates $r_j \sim \mathrm{Gamma}(\text{shape} = 0.7, \text{scale} = 0.5)$ (mean 0.35 per block; a skewed distribution, with a few very fast learners and several very slow ones). Here $m$ is the practice block, and $\varepsilon$ is the noise of a block-mean RT.

<div dir="rtl">

با مجانب $E = 400$ ms، بهبود اولیه‌ی $B = 600$ ms و نرخ‌های یادگیری فردی $r_j \sim \mathrm{Gamma}(\text{shape} = 0.7, \text{scale} = 0.5)$ (میانگین 0.35 در هر بلوک؛ توزیعی چوله با چند یادگیرنده‌ی خیلی سریع و چند یادگیرنده‌ی خیلی کند). اینجا $m$ شماره‌ی بلوک تمرین و $\varepsilon$ نویز میانگین زمان واکنش هر بلوک است.

</div>

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
True learning rates: [1.000e-03 7.000e-03 7.000e-03 2.000e-02 3.000e-02 4.500e-02 1.220e-01
 1.490e-01 1.720e-01 2.360e-01 2.820e-01 3.260e-01 3.870e-01 3.950e-01
 5.340e-01 7.100e-01 7.900e-01 1.002e+00 1.869e+00 2.534e+00]
Average curve, exp: E = 507.5, B = 423.8, r = 0.205, RMSD = 19.26 ms
Average curve, pow: E = 419.2, B = 579.4, r = 0.529, RMSD = 10.16 ms
```

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 6 · سلول 6

**Expected output (summary line):**

<div dir="rtl">

**خروجی مورد انتظار (خط خلاصه):**

</div>

```text
Which model fits each participant better? {'exp': 20}
(with SciPy 1.18: {'exp': 19, 'pow': 1}; one participant with a near-zero learning rate is fitted differently)
```

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 7 · سلول 7

### Part E: interpret (20 min) · بخش E: تفسیر (20 دقیقه)

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 8 · سلول 8

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Mean of true individual rates:      0.481
Mean of estimated individual rates: 0.449 (SD 0.626)
Exponential rate fitted to the average curve: 0.205
Correlation of true and estimated individual rates: 0.971
(with SciPy 1.18: estimated mean 0.457 (SD 0.621), correlation 0.968, because of the same participant)
```

**Write 2–3 sentences for each:**
1. The average curve is better described by a power function (RMSD about 10 vs. 19 ms), yet all (or, depending on the SciPy version, 19) of the 20 individuals are better described by an exponential. Which statement about *learning* is justified, and which is not?
2. Why is the exponential rate fitted to the average curve smaller than the mean of the individual rates? (Hint: which participants dominate the average late in practice?)
3. Individual fits recover the true rates well here, with 60 blocks per person. What would change with only 10 blocks per person, and what would you do then? (Preview of Week 13.)

<div dir="rtl">

**برای هرکدام 2 تا 3 جمله بنویسید:**
1. منحنی میانگین با تابع توانی بهتر توصیف می‌شود (RMSD حدود 10 در برابر 19 ms)، ولی همه‌ی 20 فرد (یا بسته به نسخه‌ی SciPy، 19 نفر) با تابع نمایی بهتر توصیف می‌شوند. کدام گزاره درباره‌ی *یادگیری* موجه است و کدام نیست؟
2. چرا نرخ نمایی برازش‌شده روی منحنی میانگین از میانگین نرخ‌های فردی کوچک‌تر است؟ (راهنمایی: در اواخر تمرین کدام شرکت‌کننده‌ها بر میانگین غالب‌اند؟)
3. اینجا با 60 بلوک برای هر نفر، برازش‌های فردی نرخ‌های واقعی را خوب بازیابی می‌کنند. با فقط 10 بلوک برای هر نفر چه تغییر می‌کرد و آن‌وقت چه می‌کردید؟ (پیش‌نمایش هفته‌ی 13.)

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Compute Wald 95% CIs for the *exponential* model's MLE on the Week 2 data. Do they contain sensible values? Then compute them at the bogus "estimate" `(A, lam) = (1.0, 0.107)` from last week's bounded-Nelder–Mead warning. What happens to the Hessian at a point that is not a minimum?

<div dir="rtl">

**تمرین 1 ★.** بازه‌های اطمینان 95% Wald را برای MLE مدل *نمایی* روی داده‌های هفته‌ی 2 حساب کنید. آیا مقادیر معقولی در بر دارند؟ بعد آن‌ها را در «برآورد» ساختگی `(A, lam) = (1.0, 0.107)` از هشدار Nelder–Mead کران‌دار هفته‌ی قبل حساب کنید. در نقطه‌ای که کمینه نیست چه بر سر Hessian می‌آید؟

</div>

**Exercise 2 ★.** Rerun the bootstrap with $B = 50, 200, 1000$ and different seeds. How stable are the percentile limits? How large should $B$ be for a 95% CI?

<div dir="rtl">

**تمرین 2 ★.** bootstrap را با $B = 50, 200, 1000$ و seedهای مختلف دوباره اجرا کنید. حدود صدکی چقدر پایدارند؟ برای یک بازه‌ی 95%، $B$ چقدر باید بزرگ باشد؟

</div>

**Exercise 3 ★★ (a derived quantity).** Use the bootstrap samples from Part C to compute a 95% CI for the **half-life** of the power model, $t_{1/2} = 2^{1/d} - 1$. Why is this easy with the bootstrap and awkward with the Hessian?

<div dir="rtl">

**تمرین 3 ★★ (یک کمیت مشتق‌شده).** با نمونه‌های bootstrap بخش C یک بازه‌ی 95% برای **نیمه‌عمر** مدل توانی، $t_{1/2} = 2^{1/d} - 1$، حساب کنید. چرا این کار با bootstrap آسان و با Hessian دست‌وپاگیر است؟

</div>

**Exercise 4 ★★ (the Gamma–power result).** Draw 100 000 rates $\lambda \sim \mathrm{Gamma}(\text{shape } s = 0.8, \text{rate } b = 2)$, average $e^{-\lambda t}$ over them for $t \in [0, 30]$, and overlay the analytic curve $(1 + t/b)^{-s}$ (Lecture §5, Advanced box). Then fit exponential and power functions to the averaged curve.

<div dir="rtl">

**تمرین 4 ★★ (نتیجه‌ی Gamma–توانی).** 100 000 نرخ $\lambda \sim \mathrm{Gamma}(\text{shape } s = 0.8, \text{rate } b = 2)$ بکشید، $e^{-\lambda t}$ را روی آن‌ها برای $t \in [0, 30]$ میانگین بگیرید و منحنی تحلیلی $(1 + t/b)^{-s}$ را روی آن رسم کنید (کادر «پیشرفته» بخش 5 جزوه). بعد توابع نمایی و توانی را روی منحنی میانگین برازش کنید.

</div>

**Exercise 5 ★★★ (Advanced: coverage).** How often do 95% intervals actually contain the true value? Simulate 300 datasets from the power model ($A = 0.9$, $d = 0.5$) with $n = 10$ items per interval, and compute the Wald and profile CIs for $d$ for each. Report the coverage (proportion containing 0.5) of each method. Which is closer to 95%? Repeat with $n = 50$.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: پوشش).** بازه‌های 95% واقعاً چند وقت یک بار مقدار واقعی را در بر می‌گیرند؟ 300 مجموعه‌داده از مدل توانی ($A = 0.9$، $d = 0.5$) با $n = 10$ آیتم در هر فاصله شبیه‌سازی کنید و برای هرکدام بازه‌های Wald و profile $d$ را حساب کنید. پوشش (نسبت بازه‌هایی که 0.5 را در بر دارند) هر روش را گزارش کنید. کدام به 95% نزدیک‌تر است؟ با $n = 50$ تکرار کنید.

</div>

### Lab check-off · lab check-off

Show: (1) a table comparing the Wald, profile and bootstrap 95% CIs for $d$; (2) the bootstrap scatter plot with one sentence on the trade-off; (3) the individual-vs-average comparison and your answer to interpretation question 1.

<div dir="rtl">

نشان دهید: (1) جدولی که بازه‌های 95% Wald، profile و bootstrap برای $d$ را مقایسه می‌کند؛ (2) نمودار پراکنش bootstrap با یک جمله درباره‌ی trade-off؛ (3) مقایسه‌ی فردی در برابر میانگین و پاسخ شما به سؤال تفسیری 1.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Benchmark scores have standard errors.** AI models are compared on benchmarks, and leaderboards often rank models that differ by one or two percentage points. A benchmark is a *sample* of items, so its accuracy has sampling error just like a parameter estimate. Two lessons from this week apply directly:
1. **Report uncertainty.** A bootstrap over items gives a confidence interval for the accuracy and for the difference between two models.
2. **Respect the design.** Both models answered the *same* items, so the comparison is paired, like a within-participant design. Resampling the two models independently ignores the shared item difficulty and gives intervals that are too wide.

<div dir="rtl">

**نمره‌های benchmark هم خطای استاندارد دارند.** مدل‌های هوش مصنوعی روی benchmarkها مقایسه می‌شوند، و جدول‌های رتبه‌بندی (leaderboard) اغلب مدل‌هایی را رتبه‌بندی می‌کنند که یکی دو درصد با هم فرق دارند. یک benchmark یک *نمونه* از آیتم‌هاست، پس دقتش، درست مثل برآورد یک پارامتر، خطای نمونه‌گیری دارد. دو درس این هفته مستقیماً به کار می‌آیند:
1. **عدم قطعیت را گزارش کنید.** bootstrap روی آیتم‌ها یک بازه‌ی اطمینان برای دقت و برای تفاوت دو مدل می‌دهد.
2. **به طرح احترام بگذارید.** هر دو مدل به *همان* آیتم‌ها جواب داده‌اند، پس مقایسه جفتی است، مثل یک طرح درون‌آزمودنی. نمونه‌گیری مجدد مستقل از دو مدل، دشواری مشترک آیتم‌ها را نادیده می‌گیرد و بازه‌هایی بیش از حد پهن می‌دهد.

</div>

Item difficulty also varies a lot, which is the item-level version of the participant heterogeneity in Part D: a single average accuracy hides it.

<div dir="rtl">

دشواری آیتم‌ها هم خیلی متفاوت است، که نسخه‌ی سطح آیتمِ ناهمگنی شرکت‌کننده‌ها در بخش D است: یک دقت میانگین واحد آن را پنهان می‌کند.

</div>

> **Code · کد:** [`code/week05.py`](code/week05.py), cell 9 · سلول 9

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Accuracy A = 0.74, B = 0.67, difference = 0.07
95% CI, paired bootstrap:   [-0.03, 0.17]
95% CI, unpaired bootstrap: [-0.06, 0.20]
```

A 7-point lead on 100 items is not clearly different from zero. A leaderboard that ranks A above B without an interval is overconfident.

<div dir="rtl">

7 درصد برتری روی 100 آیتم به‌وضوح با صفر فرق ندارد. جدول رتبه‌بندی‌ای که A را بدون بازه بالای B می‌گذارد، بیش از حد مطمئن است.

</div>

**Try it (no API needed).**
- ★ How many items would the benchmark need for the paired interval to exclude 0, if the true difference stays the same? Find out by simulation.
- ★★ Compute the Wald SE of each accuracy, $\sqrt{p(1-p)/n}$, and compare it with the bootstrap SE.
- ★★ Discussion: a paper reports "Model A: 74%, Model B: 67%" with no interval and concludes that A "reasons better". List what you would ask the authors.

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ اگر تفاوت واقعی ثابت بماند، benchmark به چند آیتم نیاز دارد تا بازه‌ی جفتی 0 را شامل نشود؟ با شبیه‌سازی پیدا کنید.
- ★★ SE والد (Wald) هر دقت، $\sqrt{p(1-p)/n}$، را حساب کنید و با SE حاصل از bootstrap مقایسه کنید.
- ★★ بحث: مقاله‌ای «مدل A: 74%، مدل B: 67%» را بدون بازه گزارش می‌کند و نتیجه می‌گیرد که A «بهتر استدلال می‌کند». فهرست کنید از نویسندگان چه می‌پرسید.

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **Confusing SE with SD.** The SD describes the spread of the *data*; the SE describes the uncertainty of an *estimate* and shrinks as the data grow.
2. **"There is a 95% probability that the true value is in my CI."** For a frequentist CI, 95% refers to the long-run behavior of the procedure. The probability statement belongs to Bayesian credible intervals (Week 9).
3. **Using BFGS's `hess_inv` for standard errors.** It is a crude by-product of the optimizer. Compute the Hessian properly.
4. **Trusting Wald intervals near bounds.** If $\hat\theta$ is on or near a bound, or the interval crosses impossible values, use profile or bootstrap intervals.
5. **Reporting parameters without uncertainty.** Comparing two point estimates ("participant 1 has $d = 0.42$, participant 2 has $d = 0.51$") is meaningless without intervals.
6. **Inferring individual-level processes from averaged data.** Averages of nonlinear curves change functional form (Part D). This applies to items, trials and participants alike.
7. **Treating individual estimates as if they were data.** Second-stage t-tests on fitted parameters ignore that some estimates are much noisier than others. Hierarchical models fix this (Week 13).

<div dir="rtl">

1. **قاطی کردن SE با SD.** SD پراکندگی *داده‌ها* را توصیف می‌کند؛ SE عدم قطعیت یک *برآورد* را توصیف می‌کند و با بزرگ شدن داده‌ها کوچک می‌شود.
2. **«با احتمال 95% مقدار واقعی در بازه‌ی اطمینان من است.»** در بازه‌ی اطمینان فراوانی‌گرا، 95% به رفتار بلندمدت رویه برمی‌گردد. این گزاره‌ی احتمالاتی مال credible intervalهای بیزی است (هفته‌ی 9).
3. **استفاده از `hess_inv` در BFGS برای خطای استاندارد.** یک محصول جانبی خام بهینه‌ساز است. Hessian را درست حساب کنید.
4. **اعتماد به بازه‌های Wald نزدیک کران‌ها.** اگر $\hat\theta$ روی کران یا نزدیک آن است، یا بازه از مقادیر ناممکن عبور می‌کند، از بازه‌های profile یا bootstrap استفاده کنید.
5. **گزارش پارامترها بدون عدم قطعیت.** مقایسه‌ی دو برآورد نقطه‌ای («شرکت‌کننده‌ی 1 دارای $d = 0.42$ و شرکت‌کننده‌ی 2 دارای $d = 0.51$ است») بدون بازه بی‌معنی است.
6. **استنباط فرایندهای سطح فرد از داده‌های میانگین‌گیری‌شده.** میانگین منحنی‌های غیرخطی شکل تابعی را عوض می‌کند (بخش D). این برای آیتم‌ها، trialها و شرکت‌کننده‌ها یکسان صادق است.
7. **با برآوردهای فردی مثل داده رفتار کردن.** آزمون t مرحله‌ی دوم روی پارامترهای برازش‌شده نادیده می‌گیرد که بعضی برآوردها خیلی پرنویزتر از بقیه‌اند. مدل‌های سلسله‌مراتبی این را درست می‌کنند (هفته‌ی 13).

</div>

---

## Check your understanding · خودآزمایی

**1.** What is the sampling distribution of an estimator, and why can't we observe it directly?
<details><summary>Answer</summary>
The distribution of the estimates we would get across many hypothetical replications of the experiment with the same true parameters. We have only one dataset, so we approximate it with the Hessian (asymptotic theory), the profile likelihood, or simulation (bootstrap).
</details>

<div dir="rtl">

**1.** توزیع نمونه‌گیری یک برآوردگر چیست و چرا نمی‌توانیم مستقیماً آن را ببینیم؟
<details><summary>پاسخ</summary>
توزیع برآوردهایی که در تکرارهای فرضی بسیار زیاد آزمایش با همان پارامترهای واقعی می‌گرفتیم. فقط یک مجموعه‌داده داریم، پس آن را با Hessian (نظریه‌ی مجانبی)، profile likelihood یا شبیه‌سازی (bootstrap) تقریب می‌زنیم.
</details>

</div>

**2.** The NLL has a very flat minimum along one direction of the parameter space. What does that imply for the standard errors and the correlation of the estimates?
<details><summary>Answer</summary>
Low curvature means a small Hessian entry in that direction, so a large variance in $\mathbf{H}^{-1}$: large SEs. If the flat direction is diagonal, the estimates are strongly correlated (a trade-off).
</details>

<div dir="rtl">

**2.** NLL در یک جهت از فضای پارامتر کمینه‌ی خیلی تختی دارد. این درباره‌ی خطاهای استاندارد و همبستگی برآوردها چه می‌گوید؟
<details><summary>پاسخ</summary>
انحنای کم یعنی درایه‌ی کوچک Hessian در آن جهت، پس واریانس بزرگ در $\mathbf{H}^{-1}$: SEهای بزرگ. اگر جهت تخت مورب باشد، برآوردها به‌شدت همبسته‌اند (trade-off).
</details>

</div>

**3.** Derive the Wald SE for a binomial proportion from the second derivative of the NLL.
<details><summary>Answer</summary>
$\mathrm{NLL}''(\theta) = y/\theta^2 + (n-y)/(1-\theta)^2$. At $\hat\theta = y/n$ this is $n/\hat\theta + n/(1-\hat\theta) = n/[\hat\theta(1-\hat\theta)]$. Inverting and taking the square root gives $\mathrm{SE} = \sqrt{\hat\theta(1-\hat\theta)/n}$.
</details>

<div dir="rtl">

**3.** SE روش Wald را برای یک نسبت دوجمله‌ای از مشتق دوم NLL به دست آورید.
<details><summary>پاسخ</summary>
$\mathrm{NLL}''(\theta) = y/\theta^2 + (n-y)/(1-\theta)^2$. در $\hat\theta = y/n$ این برابر $n/\hat\theta + n/(1-\hat\theta) = n/[\hat\theta(1-\hat\theta)]$ است. معکوس کردن و جذر گرفتن می‌دهد $\mathrm{SE} = \sqrt{\hat\theta(1-\hat\theta)/n}$.
</details>

</div>

**4.** List the steps of a parametric bootstrap for a CI on a model parameter.
<details><summary>Answer</summary>
Fit the model to get $\hat{\boldsymbol\theta}$. Simulate $B$ datasets from the model at $\hat{\boldsymbol\theta}$ using the original design. Refit each one. Use the SD of the refitted estimates as the SE, and their 2.5th and 97.5th percentiles as the 95% CI.
</details>

<div dir="rtl">

**4.** مراحل یک bootstrap پارامتری برای بازه‌ی اطمینان یک پارامتر مدل را بنویسید.
<details><summary>پاسخ</summary>
مدل را برازش کنید تا $\hat{\boldsymbol\theta}$ به دست آید. $B$ مجموعه‌داده از مدل با $\hat{\boldsymbol\theta}$ و طرح آزمایش اصلی شبیه‌سازی کنید. هرکدام را دوباره برازش کنید. انحراف معیار برآوردهای جدید را SE و صدک‌های 2.5 و 97.5 آن‌ها را بازه‌ی 95% در نظر بگیرید.
</details>

</div>

**5.** Why can a profile-likelihood interval be asymmetric while a Wald interval cannot?
<details><summary>Answer</summary>
The Wald interval assumes a quadratic NLL (a normal sampling distribution), which is symmetric by construction. The profile interval uses the actual likelihood, which can be skewed, e.g., near a bound or for rate parameters.
</details>

<div dir="rtl">

**5.** چرا بازه‌ی profile likelihood می‌تواند نامتقارن باشد ولی بازه‌ی Wald نمی‌تواند؟
<details><summary>پاسخ</summary>
بازه‌ی Wald یک NLL مربعی (توزیع نمونه‌گیری نرمال) فرض می‌کند که ذاتاً متقارن است. بازه‌ی profile از درست‌نمایی واقعی استفاده می‌کند که ممکن است چوله باشد، مثلاً نزدیک یک کران یا برای پارامترهای نرخ.
</details>

</div>

**6.** Twenty participants each learn exponentially, with different rates. The averaged curve is fitted better by a power function. Should we conclude that learning follows a power law?
<details><summary>Answer</summary>
No. The power shape is an aggregation artifact: averaging exponentials with heterogeneous rates produces a curve whose relative rate of change decreases over time. Conclusions about the form of individual learning must come from individual (or hierarchical) fits.
</details>

<div dir="rtl">

**6.** بیست شرکت‌کننده هرکدام با نرخ متفاوت به‌طور نمایی یاد می‌گیرند. منحنی میانگین با تابع توانی بهتر برازش می‌شود. آیا باید نتیجه بگیریم که یادگیری از قانون توانی پیروی می‌کند؟
<details><summary>پاسخ</summary>
نه. شکل توانی خطای ناشی از میانگین‌گیری است: میانگین توابع نمایی با نرخ‌های ناهمگن منحنی‌ای می‌سازد که نرخ نسبی تغییرش با زمان کم می‌شود. نتیجه‌گیری درباره‌ی شکل یادگیری فردی باید از برازش‌های فردی (یا سلسله‌مراتبی) بیاید.
</details>

</div>

**7.** Give one advantage and one disadvantage of fitting each participant separately.
<details><summary>Answer</summary>
Advantage: respects individual differences and avoids aggregation artifacts. Disadvantage: with few trials per person, estimates are noisy (and sometimes extreme or on bounds), and analyzing them in a second stage ignores their different uncertainties.
</details>

<div dir="rtl">

**7.** یک مزیت و یک عیب برازش جداگانه‌ی هر شرکت‌کننده بگویید.
<details><summary>پاسخ</summary>
مزیت: تفاوت‌های فردی را رعایت می‌کند و از خطای میانگین‌گیری دوری می‌کند. عیب: با trialهای کم برای هر نفر، برآوردها پرنویزند (و گاهی حدی یا روی کران)، و تحلیل آن‌ها در مرحله‌ی دوم عدم قطعیت‌های متفاوتشان را نادیده می‌گیرد.
</details>

</div>

---

## Assignment · تکلیف

No new graded assignment this week. **A2 (LS vs. MLE) is due at the start of the Week 6 lecture.** Part A of today's lab shows how to add standard errors to your A2 estimates. Doing so is not required, but it will strengthen your interpretation.

<div dir="rtl">

این هفته تکلیف نمره‌دار جدیدی نداریم. **A2 (LS در برابر MLE) در ابتدای درس هفته‌ی 6 تحویل داده می‌شود.** بخش A lab امروز نشان می‌دهد چطور به برآوردهای A2 خود خطای استاندارد اضافه کنید. این کار الزامی نیست ولی تفسیرتان را قوی‌تر می‌کند.

</div>

**Optional practice (ungraded):** Exercise 5 (coverage) is the best preparation for Week 7's recovery studies.

<div dir="rtl">

**تمرین اختیاری (بدون نمره):** تمرین 5 (پوشش) بهترین آمادگی برای مطالعات بازیابی هفته‌ی 7 است.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018), chapter 5.** Combining information from multiple participants: aggregate vs. individual fitting and the dangers of averaging. *(Main reading.)*
- **Farrell & Lewandowsky (2018), chapter 4** (the sections on parameter uncertainty and the Hessian), revisited from last week.
- *Optional, outside the course list:* Heathcote, A., Brown, S., & Mewhort, D. J. K. (2000). The power law repealed: The case for an exponential law of practice. *Psychonomic Bulletin & Review, 7*, 185–207. The classic analysis of averaging artifacts in practice data.

<div dir="rtl">

- **Farrell & Lewandowsky (2018)، فصل 5.** ترکیب اطلاعات چند شرکت‌کننده: برازش تجمیعی در برابر فردی و خطرات میانگین‌گیری. *(منبع اصلی.)*
- **Farrell & Lewandowsky (2018)، فصل 4** (بخش‌های مربوط به عدم قطعیت پارامتر و Hessian)، مرور از هفته‌ی قبل.
- *اختیاری، خارج از فهرست درس:* Heathcote, A., Brown, S., & Mewhort, D. J. K. (2000). The power law repealed: The case for an exponential law of practice. *Psychonomic Bulletin & Review, 7*, 185–207. تحلیل کلاسیک خطاهای میانگین‌گیری در داده‌های تمرین.

</div>

*Preview for Week 6:* Exercise 4 of Week 3 showed a three-parameter model beating the true model on SSE. Next week we confront this directly: why good fit is not enough, and how cross-validation measures what we really want, which is prediction of new data.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 6:* تمرین 4 هفته‌ی 3 نشان داد که یک مدل سه‌پارامتری در SSE از مدل واقعی جلو می‌زند. هفته‌ی بعد مستقیماً با این روبه‌رو می‌شویم: چرا برازش خوب کافی نیست، و چطور cross-validation چیزی را که واقعاً می‌خواهیم، یعنی پیش‌بینی داده‌ی جدید، اندازه می‌گیرد.

</div>
