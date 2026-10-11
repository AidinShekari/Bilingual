# Week 3: Fitting Models by Least Squares: Error Surfaces and Optimization · هفته‌ی 3: برازش مدل با کمترین مربعات: سطح خطا و بهینه‌سازی

> **Chapter 2: Parameter estimation methods** · Lecture 1 h · Lab 2 h
> **This week's running data:** the simulated forgetting experiment from Week 2 (power model, $A^\ast = 0.9$, $d^\ast = 0.5$, $n = 50$ items at 8 intervals). We refit it properly and compare with last week's linearized fits.

<div dir="rtl">

> **فصل 2: روش‌های برآورد پارامتر** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی این هفته:** آزمایش فراموشی شبیه‌سازی‌شده از هفته‌ی 2 (مدل توانی، $A^\ast = 0.9$، $d^\ast = 0.5$، $n = 50$ آیتم در 8 فاصله). آن را درست برازش می‌کنیم و با برازش‌های خطی‌شده‌ی هفته‌ی قبل مقایسه می‌کنیم.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| least squares | کمترین مربعات | روش برازش با کمینه کردن مجموع مربع خطاها |
| error surface | سطح خطا | خطا به‌عنوان تابعی از پارامترها |
| optimizer | بهینه‌ساز | الگوریتمی که کمینه‌ی تابع را پیدا می‌کند |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| SSE / RMSD | مجموع مربعات خطا / ریشه‌ی میانگین مربع انحراف | معیارهای فاصله‌ی داده و پیش‌بینی |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| parameter trade-off | بده‌بستان پارامترها | تغییر یک پارامتر که با پارامتر دیگر جبران می‌شود |
| grid approximation | تقریب شبکه‌ای (grid) | محاسبه‌ی پسین روی شبکه‌ای از مقادیر |
| Nelder–Mead | روش Nelder–Mead | بهینه‌ساز بدون نیاز به مشتق |
| Bayes factor (BF) | عامل بیز (Bayes factor) | نسبت درست‌نمایی‌های حاشیه‌ای دو مدل |
| local minimum | کمینه‌ی محلی | نقطه‌ای پایین‌تر از اطراف ولی نه بهترین نقطه |
| bounds / constraints | کران‌ها / قیدها | محدودیت‌های مجاز برای مقدار پارامترها |
| reparameterization | بازپارامتری‌سازی | نوشتن پارامتر در مقیاس دیگر، مثلاً λ = e^η |
| multi-start | شروع چندگانه (multi-start) | اجرای بهینه‌ساز از چند نقطه‌ی شروع |
| maximum likelihood estimate (MLE) | برآورد بیشینه‌ی درست‌نمایی | پارامترهایی که داده را محتمل‌ترین می‌کنند |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| gradient | گرادیان | جهت و شیب تغییر تابع |
| convergence | همگرایی | رسیدن زنجیره‌ها به توزیع هدف |
| large language model (LLM) | مدل بزرگ زبانی | شبکه‌ی عصبی‌ای که کلمه‌ی بعدی متن را پیش‌بینی می‌کند |
| scaling law | قانون مقیاس | رابطه‌ی توانی بین اندازه‌ی مدل و خطا |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Define** SSE, MSE and RMSD as discrepancy functions and **explain** what minimizing them assumes about the noise.
2. **Visualize** an error surface for a two-parameter model and **interpret** its shape (minimum, valleys, plateaus) in terms of parameter trade-offs.
3. **Implement** least-squares fitting by grid search and with `scipy.optimize.minimize` (Nelder–Mead and L-BFGS-B), and **compare** the algorithms' strengths and failure modes.
4. **Diagnose** and **remedy** common fitting failures: bad starting values, plateaus, local minima, and out-of-range parameters (using bounds, reparameterization and multi-start).
5. **Evaluate** a least-squares fit with RMSD and residuals, and **interpret** the fitted parameters.

<div dir="rtl">

1. SSE، MSE و RMSD را به‌عنوان توابع ناهمخوانی (discrepancy functions) **تعریف کنند** و **توضیح دهند** که کمینه کردن آن‌ها چه فرضی درباره‌ی نویز دارد.
2. سطح خطای یک مدل دوپارامتری را **رسم کنند** و شکل آن (کمینه، دره، فلات) را بر حسب trade-off پارامترها **تفسیر کنند**.
3. برازش کمترین مربعات را با جستجوی شبکه‌ای و با `scipy.optimize.minimize` (Nelder–Mead و L-BFGS-B) **پیاده‌سازی کنند** و نقاط قوت و حالت‌های شکست الگوریتم‌ها را **مقایسه کنند**.
4. شکست‌های رایج برازش را **تشخیص دهند** و **رفع کنند**: مقدار شروع بد، فلات‌ها، کمینه‌های محلی، و پارامترهای خارج از دامنه (با کران، reparameterization و multi-start).
5. یک برازش کمترین مربعات را با RMSD و باقی‌مانده‌ها **ارزیابی کنند** و پارامترهای برازش‌شده را **تفسیر کنند**.

</div>

---

## Motivation & big picture · مقدمه

Last week we fitted forgetting curves by drawing a straight line through log-transformed proportions. The power model was the true model, yet its estimates were noticeably off ($\hat A = 0.80$, $\hat d = 0.37$ instead of $0.9$ and $0.5$). The method also breaks whenever a count is zero, and it minimizes errors on the wrong (log) scale.

<div dir="rtl">

هفته‌ی قبل منحنی‌های فراموشی را با کشیدن یک خط راست از میان نسبت‌های لگاریتمی‌شده برازش کردیم. مدل توانی مدل واقعی بود، ولی برآوردهایش آشکارا خطا داشتند ($\hat A = 0.80$، $\hat d = 0.37$ به‌جای $0.9$ و $0.5$). این روش هر وقت یک شمارش صفر باشد از کار می‌افتد، و خطاها را روی مقیاس غلط (لگاریتمی) کمینه می‌کند.

</div>

The fix is conceptually simple: **choose the parameters that make the model's predictions as close as possible to the data, on the data's own scale.** "As close as possible" needs a number, a *discrepancy function*. "Choose the parameters" needs a search procedure, an *optimization algorithm*. This week covers both.

<div dir="rtl">

راه‌حل از نظر مفهومی ساده است: **پارامترهایی را انتخاب کن که پیش‌بینی‌های مدل را، روی مقیاس خود داده، تا جای ممکن به داده نزدیک کنند.** «تا جای ممکن نزدیک» به یک عدد نیاز دارد: یک *تابع ناهمخوانی*. «پارامترها را انتخاب کن» به یک رویه‌ی جستجو نیاز دارد: یک *الگوریتم بهینه‌سازی*. این هفته هر دو را پوشش می‌دهد.

</div>

There is a deeper reason this matters for cognitive science. Model parameters are our *measurements* of latent constructs (decay rate, caution, sensitivity). A poor fitting procedure gives poor measurements, and every conclusion drawn from them (group differences, correlations with brain activity, model comparisons) inherits that error. Worse, as we will see, an optimizer can report "success" while returning nonsense.

<div dir="rtl">

دلیل عمیق‌تری هم هست که این برای علوم شناختی مهم است. پارامترهای مدل *اندازه‌گیری‌های* ما از سازه‌های پنهان‌اند (نرخ زوال، احتیاط، حساسیت). رویه‌ی برازش ضعیف اندازه‌گیری‌های ضعیف می‌دهد، و هر نتیجه‌ای که از آن‌ها گرفته شود (تفاوت گروه‌ها، همبستگی با فعالیت مغز، مقایسه‌ی مدل‌ها) آن خطا را به ارث می‌برد. بدتر اینکه، همان‌طور که خواهیم دید، یک بهینه‌ساز می‌تواند «موفقیت» گزارش کند در حالی که جواب بی‌معنی برمی‌گرداند.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Every model-based study in psychology** has a fitting step. Learning curves, forgetting curves, psychometric functions (how detection improves with stimulus strength) and dose–response curves in psychopharmacology are all fitted by minimizing a discrepancy.
- **Clinical and developmental research** compares fitted parameters between groups (e.g. the forgetting rate of patients vs. controls). If the fit is poor or stuck at a bound, the group comparison is wrong.
- **Neuroscience** fits tuning curves of neurons and hemodynamic response functions in fMRI with exactly these optimizers.
- **Machine learning** trains models by minimizing a loss with gradient methods; the vocabulary (loss surface, learning rate, local minima) is the same as this week's.

<div dir="rtl">

- **هر مطالعه‌ی مبتنی بر مدل در روان‌شناسی** یک مرحله‌ی برازش دارد. منحنی‌های یادگیری، منحنی‌های فراموشی، تابع‌های روان‌سنجی (psychometric function: اینکه تشخیص با قوی‌تر شدن محرک چطور بهتر می‌شود) و منحنی‌های دوز–پاسخ در روان‌داروشناسی همه با کمینه کردن یک معیار خطا برازش می‌شوند.
- **پژوهش‌های بالینی و رشدی** پارامترهای برازش‌شده را بین گروه‌ها مقایسه می‌کنند (مثلاً نرخ فراموشی بیماران در برابر گروه کنترل). اگر برازش بد باشد یا روی یک کران گیر کرده باشد، مقایسه‌ی گروه‌ها غلط است.
- **علوم اعصاب** منحنی‌های تنظیم (tuning curve) نورون‌ها و تابع پاسخ همودینامیک در fMRI را با همین بهینه‌سازها برازش می‌کند.
- **یادگیری ماشین** مدل‌ها را با کمینه کردن یک تابع زیان (loss) با روش‌های گرادیانی آموزش می‌دهد؛ واژه‌ها (سطح زیان، نرخ یادگیری، کمینه‌ی محلی) همان واژه‌های این هفته‌اند.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

A model has knobs (parameters). Fitting means turning the knobs until the model's curve passes as close as possible to the data points. To do this with a computer we need two things. First, a single number that says how bad the current fit is: the **sum of squared errors (SSE)**, the squared vertical distances between data points and the curve, added up. Second, a strategy to turn the knobs so that this number goes down: an **optimizer**. Think of the SSE as a landscape over all possible knob settings, with hills (bad fits) and valleys (good fits); the optimizer is a hiker looking for the lowest point. Problems arise when the landscape has a long flat valley (two knobs can compensate each other), a flat plateau (the hiker cannot tell which way is down), or several separate valleys (the hiker may stop in the wrong one). Most of this week is about recognizing those situations and protecting yourself against them.

<div dir="rtl">

مدل چند پیچ تنظیم (پارامتر) دارد. برازش یعنی چرخاندن پیچ‌ها تا منحنی مدل تا جای ممکن از نزدیک نقطه‌های داده بگذرد. برای اینکه کامپیوتر این کار را بکند دو چیز لازم داریم. اول، یک عدد که بگوید برازش فعلی چقدر بد است: **مجموع مربعات خطا (SSE)**، یعنی جمع مربع فاصله‌ی عمودی نقطه‌های داده از منحنی. دوم، روشی برای چرخاندن پیچ‌ها که این عدد را کم کند: یک **بهینه‌ساز (optimizer)**. SSE را مثل یک منظره روی همه‌ی تنظیم‌های ممکن پیچ‌ها تصور کنید، با تپه‌ها (برازش بد) و دره‌ها (برازش خوب)؛ بهینه‌ساز یک کوهنورد است که دنبال پایین‌ترین نقطه می‌گردد. مشکل وقتی پیش می‌آید که منظره یک دره‌ی دراز و صاف داشته باشد (دو پیچ می‌توانند اثر هم را جبران کنند)، یک فلات صاف (کوهنورد نمی‌فهمد کدام طرف سرازیری است)، یا چند دره‌ی جدا (کوهنورد ممکن است در دره‌ی اشتباه بایستد). بیشتر این هفته درباره‌ی تشخیص این موقعیت‌ها و محافظت از خودمان در برابر آن‌هاست.

</div>

**Suggested timing (60 min):** discrepancy functions 10 · error surfaces 10 · optimization algorithms 20 · practical problems and a fitting checklist 15 · preview 5.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** توابع ناهمخوانی 10 · سطح خطا 10 · الگوریتم‌های بهینه‌سازی 20 · مشکلات عملی و چک‌لیست برازش 15 · پیش‌نمایش 5.

</div>

### 1. Discrepancy functions · 1. توابع ناهمخوانی

For observations $y_i$ and model predictions $\hat y_i = f(x_i; \boldsymbol\theta)$, $i = 1, \dots, N$:

<div dir="rtl">

برای مشاهدات $y_i$ و پیش‌بینی‌های مدل $\hat y_i = f(x_i; \boldsymbol\theta)$، $i = 1, \dots, N$:

</div>

$$
\mathrm{SSE}(\boldsymbol\theta) = \sum_{i=1}^{N} \big(y_i - f(x_i;\boldsymbol\theta)\big)^2, \qquad
\mathrm{MSE} = \frac{\mathrm{SSE}}{N}, \qquad
\mathrm{RMSD} = \sqrt{\mathrm{MSE}}.
$$

- All three have the **same minimizer**: they are monotone transformations of each other. We *minimize* SSE and *report* RMSD, because RMSD is in the units of the data (here: proportion recalled), so "RMSD = 0.057" means predictions are off by about 0.06 on average.
- The **least-squares estimate** is
$$
\hat{\boldsymbol\theta}_{\text{LS}} = \arg\min_{\boldsymbol\theta} \mathrm{SSE}(\boldsymbol\theta).
$$

<div dir="rtl">

- هر سه **کمینه‌کننده‌ی یکسانی** دارند: تبدیل‌های یکنوای همدیگرند. SSE را *کمینه* و RMSD را *گزارش* می‌کنیم، چون RMSD بر حسب واحد داده است (اینجا: نسبت یادآوری)، پس «RMSD = 0.057» یعنی پیش‌بینی‌ها به‌طور میانگین حدود 0.06 خطا دارند.
- **برآورد کمترین مربعات** این است:
$$
\hat{\boldsymbol\theta}_{\text{LS}} = \arg\min_{\boldsymbol\theta} \mathrm{SSE}(\boldsymbol\theta).
$$

</div>

**Why squares?** Squaring makes all errors positive, penalizes large errors heavily, and gives a smooth (differentiable) function that optimizers handle well. More deeply, minimizing SSE is exactly maximum likelihood estimation **if** the noise is Gaussian with the same variance for every observation (Week 4). That "if" is the hidden assumption of least squares.

<div dir="rtl">

**چرا مربع؟** مربع کردن همه‌ی خطاها را مثبت می‌کند، خطاهای بزرگ را به‌شدت جریمه می‌کند، و تابعی هموار (مشتق‌پذیر) می‌دهد که بهینه‌سازها راحت با آن کار می‌کنند. در سطحی عمیق‌تر، کمینه کردن SSE دقیقاً همان برآورد بیشینه درست‌نمایی است، **اگر** نویز گاوسی و با واریانس یکسان برای همه‌ی مشاهدات باشد (هفته‌ی 4). این «اگر» فرض پنهان کمترین مربعات است.

</div>

**When the assumption fails.** Recall proportions are binomial: their variance $f(1-f)/n$ depends on $f$. Points near 0.5 are noisier than points near 0 or 1, but plain SSE treats them as equally reliable. **Weighted least squares** fixes this by weighting each squared error by the inverse of its variance:

<div dir="rtl">

**وقتی فرض برقرار نیست.** نسبت‌های یادآوری دوجمله‌ای‌اند: واریانسشان $f(1-f)/n$ به $f$ بستگی دارد. نقاط نزدیک 0.5 پرنویزتر از نقاط نزدیک 0 یا 1 هستند، ولی SSE ساده با همه‌شان مثل هم رفتار می‌کند. **کمترین مربعات وزنی** (weighted least squares) این را با وزن دادن به هر مربع خطا بر اساس معکوس واریانسش درست می‌کند:

</div>

$$
\mathrm{WSSE}(\boldsymbol\theta) = \sum_{i} \frac{\big(y_i - \hat y_i\big)^2}{\mathrm{Var}(y_i)}.
$$

You will try this in Exercise 3. Next week, maximum likelihood handles this issue more naturally.

<div dir="rtl">

این را در تمرین 3 امتحان می‌کنید. هفته‌ی بعد، بیشینه درست‌نمایی این مسئله را طبیعی‌تر حل می‌کند.

</div>

> **Note:** some textbooks call RMSD "RMSE". They are the same quantity.

<div dir="rtl">

> **نکته:** بعضی کتاب‌ها به RMSD می‌گویند «RMSE». هر دو یک کمیت‌اند.

</div>

#### Reading the math · خواندن ریاضی

- $\sum_{i=1}^{N}$ means "add up over all $N$ data points". $y_i - f(x_i;\boldsymbol\theta)$ is the **residual** of point $i$: observed minus predicted. Squaring and adding gives one number per parameter setting $\boldsymbol\theta$.
- $\arg\min_{\boldsymbol\theta} \mathrm{SSE}(\boldsymbol\theta)$ reads "the value of $\boldsymbol\theta$ at which SSE is smallest". Note the difference: $\min$ is the smallest *SSE value*, $\arg\min$ is the *parameter value* that achieves it. We want the $\arg\min$.
- **Small example.** Data $y = (0.62, 0.41)$, predictions $(0.66, 0.44)$: residuals $(-0.04, -0.03)$, SSE $= 0.0016 + 0.0009 = 0.0025$, MSE $= 0.00125$, RMSD $= 0.035$: the curve misses the points by about 3.5 percentage points on average.
- In WSSE each squared residual is divided by the variance of that point, so a noisy point counts less. With binomial data the variance is $f(1-f)/n$.

<div dir="rtl">

- $\sum_{i=1}^{N}$ یعنی «روی همه‌ی $N$ نقطه‌ی داده جمع بزن». $y_i - f(x_i;\boldsymbol\theta)$ **باقی‌مانده (residual)** نقطه‌ی $i$ است: مقدار مشاهده‌شده منهای مقدار پیش‌بینی‌شده. مربع کردن و جمع زدن برای هر تنظیم پارامتر $\boldsymbol\theta$ یک عدد می‌دهد.
- $\arg\min_{\boldsymbol\theta} \mathrm{SSE}(\boldsymbol\theta)$ این‌طور خوانده می‌شود: «مقداری از $\boldsymbol\theta$ که در آن SSE کمترین است». به تفاوت دقت کنید: $\min$ کوچک‌ترین *مقدار SSE* است و $\arg\min$ *مقدار پارامتری* که به آن می‌رسد. ما $\arg\min$ را می‌خواهیم.
- **مثال کوچک.** داده‌ی $y = (0.62, 0.41)$ و پیش‌بینی $(0.66, 0.44)$: باقی‌مانده‌ها $(-0.04, -0.03)$، SSE $= 0.0016 + 0.0009 = 0.0025$، MSE $= 0.00125$ و RMSD $= 0.035$: منحنی به‌طور میانگین حدود 3.5 درصد از نقطه‌ها فاصله دارد.
- در WSSE هر مربع باقی‌مانده بر واریانس همان نقطه تقسیم می‌شود، پس نقطه‌ی پرنویز وزن کمتری دارد. برای داده‌ی دوجمله‌ای واریانس برابر $f(1-f)/n$ است.

</div>

### 2. The error surface · 2. سطح خطا (error surface)

For a model with $k$ parameters, $\mathrm{SSE}(\boldsymbol\theta)$ is a surface over a $k$-dimensional parameter space. With $k = 2$ we can draw it as a contour map: the fitting problem becomes "find the lowest point of the landscape."

<div dir="rtl">

برای مدلی با $k$ پارامتر، $\mathrm{SSE}(\boldsymbol\theta)$ یک سطح روی فضای پارامتر $k$ بعدی است. با $k = 2$ می‌توانیم آن را به شکل نقشه‌ی تراز (contour map) رسم کنیم: مسئله‌ی برازش می‌شود «پایین‌ترین نقطه‌ی این منظره را پیدا کن.»

</div>

Features to recognize:

<div dir="rtl">

ویژگی‌هایی که باید بشناسید:

</div>

| Feature | What it looks like | What it means |
|---|---|---|
| **Single, round bowl** | Concentric, nearly circular contours | Parameters well determined and roughly independent; any decent algorithm finds the minimum |
| **Long, diagonal valley** | Elongated contours tilted at an angle | **Parameter trade-off**: increasing one parameter can be compensated by changing the other. Estimates will be correlated and uncertain along the valley (Week 5, Week 7) |
| **Plateau** | Very widely spaced contours | The model's predictions barely change with the parameters (e.g., a decay rate so large that the predicted curve is 0 everywhere). Gradient-based methods stall |
| **Several separate basins** | More than one closed set of contours | **Local minima**: the algorithm's answer depends on where it starts |

<div dir="rtl">

| ویژگی | ظاهرش | معنایش |
|---|---|---|
| **یک کاسه‌ی گرد** | خطوط تراز هم‌مرکز و تقریباً دایره‌ای | پارامترها به‌خوبی تعیین می‌شوند و تقریباً مستقل‌اند؛ هر الگوریتم معقولی کمینه را پیدا می‌کند |
| **دره‌ی بلند و مورب** | خطوط تراز کشیده و کج | **trade-off پارامترها**: افزایش یک پارامتر را می‌شود با تغییر دیگری جبران کرد. برآوردها در امتداد دره همبسته و نامطمئن خواهند بود (هفته‌ی 5، هفته‌ی 7) |
| **فلات (plateau)** | خطوط تراز خیلی دور از هم | پیش‌بینی‌های مدل با پارامترها تقریباً تغییر نمی‌کنند (مثلاً نرخ زوال آن‌قدر بزرگ که منحنی پیش‌بینی‌شده همه‌جا 0 است). روش‌های گرادیانی گیر می‌کنند |
| **چند حوضه‌ی جدا** | بیش از یک مجموعه‌ی بسته از خطوط تراز | **کمینه‌های محلی**: جواب الگوریتم به نقطه‌ی شروع بستگی دارد |

</div>

For exponential forgetting, $A$ and $\lambda$ trade off: a higher starting level with faster decay can predict nearly the same mid-range values as a lower level with slower decay. The valley is therefore tilted (you will see it in the lab).

<div dir="rtl">

در فراموشی نمایی، $A$ و $\lambda$ با هم trade-off دارند: سطح شروع بالاتر با زوال سریع‌تر می‌تواند تقریباً همان مقادیر میانی را پیش‌بینی کند که سطح پایین‌تر با زوال کندتر. به همین دلیل دره مورب است (در lab می‌بینید).

</div>

### 3. Optimization algorithms · 3. الگوریتم‌های بهینه‌سازی

All algorithms below start from initial values $\boldsymbol\theta^{(0)}$ and generate a sequence $\boldsymbol\theta^{(1)}, \boldsymbol\theta^{(2)}, \dots$ that (hopefully) descends to the minimum.

<div dir="rtl">

همه‌ی الگوریتم‌های زیر از مقادیر اولیه‌ی $\boldsymbol\theta^{(0)}$ شروع می‌کنند و دنباله‌ای $\boldsymbol\theta^{(1)}, \boldsymbol\theta^{(2)}, \dots$ می‌سازند که (امیدواریم) به کمینه پایین برود.

</div>

#### 3.1 Grid search · 3.1 جستجوی شبکه‌ای (grid search)

Evaluate the SSE at every point of a regular grid and keep the best.

<div dir="rtl">

SSE را در همه‌ی نقاط یک شبکه‌ی منظم حساب کنید و بهترین را نگه دارید.

</div>

- **Pros:** trivially simple; cannot be fooled by local minima *on the grid*; gives a picture of the whole surface.
- **Cons:** precision limited by grid spacing; cost grows **exponentially** with the number of parameters. With 100 values per parameter: $k = 2$ needs $10^4$ evaluations, $k = 5$ needs $10^{10}$. This is the **curse of dimensionality**.
- **Use it for:** visualizing 1–2-parameter surfaces, and for generating good starting values.

<div dir="rtl">

- **مزایا:** فوق‌العاده ساده؛ گول کمینه‌های محلی *روی شبکه* را نمی‌خورد؛ تصویری از کل سطح می‌دهد.
- **معایب:** دقت محدود به فاصله‌ی نقاط شبکه است؛ هزینه با تعداد پارامترها **به‌طور نمایی** بالا می‌رود. با 100 مقدار برای هر پارامتر: $k = 2$ به $10^4$ ارزیابی و $k = 5$ به $10^{10}$ ارزیابی نیاز دارد. این همان **نفرین ابعاد** (curse of dimensionality) است.
- **کاربرد:** رسم سطح‌های 1 یا 2 پارامتری، و تولید مقادیر شروع خوب.

</div>

#### 3.2 Nelder–Mead simplex (derivative-free) · 3.2 سیمپلکس Nelder–Mead (بدون مشتق)

A **simplex** is a set of $k+1$ points in a $k$-dimensional space (a triangle when $k = 2$). Each iteration tries to replace the **worst** vertex $\boldsymbol\theta_w$ by moving it through the centroid $\bar{\boldsymbol\theta}$ of the other vertices:

<div dir="rtl">

یک **سیمپلکس** مجموعه‌ای از $k+1$ نقطه در فضای $k$ بعدی است (برای $k = 2$ یک مثلث). هر تکرار سعی می‌کند **بدترین** رأس $\boldsymbol\theta_w$ را با حرکت دادنش از میان مرکز ثقل $\bar{\boldsymbol\theta}$ بقیه‌ی رأس‌ها جایگزین کند:

</div>

| Move | Formula (standard coefficients) | When |
|---|---|---|
| Reflect | $\boldsymbol\theta_r = \bar{\boldsymbol\theta} + (\bar{\boldsymbol\theta} - \boldsymbol\theta_w)$ | Always tried first |
| Expand | $\boldsymbol\theta_e = \bar{\boldsymbol\theta} + 2(\bar{\boldsymbol\theta} - \boldsymbol\theta_w)$ | The reflected point is better than the current best; try going further |
| Contract | $\boldsymbol\theta_c = \bar{\boldsymbol\theta} + \tfrac{1}{2}(\boldsymbol\theta_w - \bar{\boldsymbol\theta})$ (inside), or the same step on the reflected side (outside) | The reflected point is not better than the second-worst vertex |
| Shrink | Move all vertices halfway toward the best one | Contraction also failed |

<div dir="rtl">

| حرکت | فرمول (ضرایب استاندارد) | چه وقت |
|---|---|---|
| بازتاب (reflect) | $\boldsymbol\theta_r = \bar{\boldsymbol\theta} + (\bar{\boldsymbol\theta} - \boldsymbol\theta_w)$ | همیشه اول امتحان می‌شود |
| گسترش (expand) | $\boldsymbol\theta_e = \bar{\boldsymbol\theta} + 2(\bar{\boldsymbol\theta} - \boldsymbol\theta_w)$ | نقطه‌ی بازتاب‌شده از بهترین فعلی بهتر است؛ جلوتر برو |
| انقباض (contraction) | $\boldsymbol\theta_c = \bar{\boldsymbol\theta} + \tfrac{1}{2}(\boldsymbol\theta_w - \bar{\boldsymbol\theta})$ (داخلی)، یا همین گام در سمت بازتاب (خارجی) | نقطه‌ی بازتاب‌شده از دومین بدترین رأس بهتر نیست |
| جمع‌شدن (shrink) | همه‌ی رأس‌ها را تا نیمه به سمت بهترین ببر | انقباض هم شکست خورد |

</div>

The reflected point is **accepted** when it is better than the second-worst vertex but not better than the best. The simplex "tumbles" downhill, stretches along valleys, and shrinks around the minimum.

<div dir="rtl">

نقطه‌ی بازتاب‌شده **پذیرفته می‌شود** وقتی از دومین بدترین رأس بهتر باشد ولی از بهترین بهتر نباشد. سیمپلکس سرازیر «غلت می‌خورد»، در امتداد دره‌ها کشیده می‌شود و دور کمینه جمع می‌شود.

</div>

- **Pros:** needs only SSE values (no derivatives); robust to noisy or non-smooth objective functions; the default workhorse in cognitive modeling.
- **Cons:** can be slow in high dimensions; can stall in long narrow valleys; no guarantee of finding the global minimum.

<div dir="rtl">

- **مزایا:** فقط به مقادیر SSE نیاز دارد (بدون مشتق)؛ در برابر توابع هدف پرنویز یا ناهموار مقاوم است؛ ابزار پیش‌فرض و پرکاربرد در مدل‌سازی شناختی.
- **معایب:** در ابعاد بالا ممکن است کند باشد؛ در دره‌های بلند و باریک ممکن است گیر کند؛ هیچ تضمینی برای پیدا کردن کمینه‌ی سراسری ندارد.

</div>

> Direct-search methods like Nelder–Mead are treated in depth in Ghodousian's book on direct methods in nonlinear optimization (see Further reading).

<div dir="rtl">

> روش‌های جستجوی مستقیم مثل Nelder–Mead در کتاب قدوسیان درباره‌ی روش‌های مستقیم در بهینه‌سازی غیرخطی به‌تفصیل بررسی شده‌اند (مطالعه‌ی بیشتر را ببینید).

</div>

#### 3.3 Gradient-based methods · 3.3 روش‌های گرادیانی

The **gradient** $\nabla \mathrm{SSE}(\boldsymbol\theta)$ points uphill, so we step the other way:

<div dir="rtl">

**گرادیان** $\nabla \mathrm{SSE}(\boldsymbol\theta)$ به سمت سربالایی اشاره می‌کند، پس ما خلافش گام برمی‌داریم:

</div>

$$
\boldsymbol\theta^{(m+1)} = \boldsymbol\theta^{(m)} - \eta\,\nabla \mathrm{SSE}\big(\boldsymbol\theta^{(m)}\big),
\qquad
\frac{\partial\,\mathrm{SSE}}{\partial \theta} = -2 \sum_{i} \big(y_i - \hat y_i\big)\,\frac{\partial \hat y_i}{\partial \theta},
$$

with step size (learning rate) $\eta$. For the exponential model, $\partial \hat y/\partial A = e^{-\lambda t}$ and $\partial \hat y/\partial \lambda = -A\,t\,e^{-\lambda t}$.

<div dir="rtl">

با اندازه‌ی گام (نرخ یادگیری) $\eta$. برای مدل نمایی، $\partial \hat y/\partial A = e^{-\lambda t}$ و $\partial \hat y/\partial \lambda = -A\,t\,e^{-\lambda t}$.

</div>

In practice we use **quasi-Newton** methods such as **BFGS**. They also estimate the *curvature* of the surface and choose the step size automatically, so they converge much faster near a minimum. **L-BFGS-B** is the variant that accepts **bounds** on parameters. If you do not supply the gradient, scipy approximates it numerically by finite differences.

<div dir="rtl">

در عمل از روش‌های **شبه‌نیوتنی** (quasi-Newton) مثل **BFGS** استفاده می‌کنیم. این روش‌ها *انحنای* سطح را هم تخمین می‌زنند و اندازه‌ی گام را خودکار انتخاب می‌کنند، پس نزدیک کمینه خیلی سریع‌تر همگرا می‌شوند. **L-BFGS-B** نسخه‌ای است که **کران** پارامترها را می‌پذیرد. اگر گرادیان را ندهید، scipy آن را عددی با تفاضل‌های متناهی تقریب می‌زند.

</div>

- **Pros:** fast and precise on smooth surfaces; scale well to many parameters (this is how neural networks are trained).
- **Cons:** need a smooth objective; get stuck where the gradient is (nearly) zero, at plateaus as well as at minima; sensitive to starting values.

<div dir="rtl">

- **مزایا:** روی سطوح هموار سریع و دقیق‌اند؛ برای تعداد پارامتر زیاد خوب مقیاس‌پذیرند (شبکه‌های عصبی همین‌طور آموزش می‌بینند).
- **معایب:** به تابع هدف هموار نیاز دارند؛ هر جا گرادیان (تقریباً) صفر باشد گیر می‌کنند، هم در فلات‌ها و هم در کمینه‌ها؛ به مقدار شروع حساس‌اند.

</div>

> **Advanced: why plateaus trap gradient methods.** If $\lambda$ is very large, $e^{-\lambda t} \approx 0$ at every observed $t$, so both partial derivatives above are $\approx 0$. A gradient method sees a "flat floor" and stops, sometimes reporting successful convergence. Nelder–Mead compares function values at distant points and can step off the plateau. You will see both behaviors in lab Part D.

<div dir="rtl">

> **پیشرفته: چرا فلات‌ها روش‌های گرادیانی را به دام می‌اندازند.** اگر $\lambda$ خیلی بزرگ باشد، $e^{-\lambda t} \approx 0$ در همه‌ی $t$های مشاهده‌شده، پس هر دو مشتق جزئی بالا $\approx 0$ هستند. روش گرادیانی یک «کف صاف» می‌بیند و متوقف می‌شود و گاهی همگرایی موفق گزارش می‌کند. Nelder–Mead مقادیر تابع را در نقاط دور مقایسه می‌کند و می‌تواند از فلات بیرون بیاید. هر دو رفتار را در بخش D lab می‌بینید.

</div>

**Summary:**

<div dir="rtl">

**خلاصه:**

</div>

| Method | Needs derivatives | Bounds | Typical use |
|---|---|---|---|
| Grid search | No | Built in | Visualization, starting values, $k \le 2$ |
| Nelder–Mead | No | Yes (scipy ≥ 1.7) | Default for small cognitive models; noisy objectives |
| BFGS | Numerical or analytic | No | Smooth objectives, unconstrained parameters |
| L-BFGS-B | Numerical or analytic | Yes | Smooth objectives with bounded parameters |

<div dir="rtl">

| روش | نیاز به مشتق | کران | کاربرد معمول |
|---|---|---|---|
| جستجوی شبکه‌ای | ندارد | ذاتی | رسم، مقدار شروع، $k \le 2$ |
| Nelder–Mead | ندارد | دارد (scipy ≥ 1.7) | پیش‌فرض برای مدل‌های شناختی کوچک؛ توابع هدف پرنویز |
| BFGS | عددی یا تحلیلی | ندارد | توابع هدف هموار، پارامترهای بدون قید |
| L-BFGS-B | عددی یا تحلیلی | دارد | توابع هدف هموار با پارامترهای کران‌دار |

</div>

#### Reading the math · خواندن ریاضی

The gradient step $\boldsymbol\theta^{(m+1)} = \boldsymbol\theta^{(m)} - \eta\,\nabla \mathrm{SSE}(\boldsymbol\theta^{(m)})$ reads: *new guess = old guess − step size × slope*. The superscript $(m)$ is the iteration number, not a power. $\nabla \mathrm{SSE}$ is the vector of partial derivatives (one slope per parameter). The minus sign makes the step go downhill.

The derivative formula $\partial\,\mathrm{SSE}/\partial\theta = -2\sum_i (y_i - \hat y_i)\,\partial \hat y_i/\partial\theta$ follows from the chain rule. It says: points where the residual is large *and* where the prediction is sensitive to $\theta$ pull hardest on $\theta$. At the minimum these pulls cancel and the sum is zero.

<div dir="rtl">

گام گرادیانی $\boldsymbol\theta^{(m+1)} = \boldsymbol\theta^{(m)} - \eta\,\nabla \mathrm{SSE}(\boldsymbol\theta^{(m)})$ این‌طور خوانده می‌شود: *حدس جدید = حدس قبلی − اندازه‌ی گام × شیب*. بالانویس $(m)$ شماره‌ی تکرار است، نه توان. $\nabla \mathrm{SSE}$ بردار مشتق‌های جزئی است (برای هر پارامتر یک شیب). علامت منفی گام را به سمت سرازیری می‌برد.

فرمول مشتق $\partial\,\mathrm{SSE}/\partial\theta = -2\sum_i (y_i - \hat y_i)\,\partial \hat y_i/\partial\theta$ از قاعده‌ی زنجیره‌ای می‌آید. می‌گوید: نقطه‌هایی که باقی‌مانده‌شان بزرگ است *و* پیش‌بینی در آن‌ها به $\theta$ حساس است، $\theta$ را قوی‌تر از بقیه می‌کشند. در نقطه‌ی کمینه این کشش‌ها همدیگر را خنثی می‌کنند و جمع صفر می‌شود.

</div>

#### For an engineer · برای یک مهندس

- **Least squares** is the same criterion as in channel estimation and curve fitting; the difference here is that the models are **nonlinear** in the parameters ($e^{-\lambda t}$), so there is no closed-form normal-equation solution and we need iterative search.
- **Weighted least squares** is noise whitening: dividing by the variance is what you do before LS when the noise is not white (heteroscedastic noise).
- **Gradient descent with step size $\eta$** is the steepest-descent idea behind the LMS adaptive filter. BFGS is a quasi-Newton method (it builds an approximation of the Hessian), close to Gauss–Newton / Levenberg–Marquardt used in nonlinear LS.
- **A long diagonal valley** in the error surface is an **ill-conditioned** problem: the Hessian has a large eigenvalue ratio, as with strongly correlated regressors. Parameters are well determined along one direction and poorly along the other.
- **Reparameterization** ($\lambda = e^{\eta}$) is a change of variables that turns a constrained problem into an unconstrained one; it also often improves conditioning.
- **What is different from engineering practice:** data sets are small (8 points, 50 items each), the noise is large, and the parameters must be *interpreted* psychologically. So it is not enough that the predicted curve looks good: the individual parameter values must be trustworthy.

<div dir="rtl">

- **کمترین مربعات** همان معیار تخمین کانال و برازش منحنی است؛ تفاوت اینجا این است که مدل‌ها نسبت به پارامترها **غیرخطی**‌اند ($e^{-\lambda t}$)، پس جواب بسته‌ای از معادله‌های نرمال وجود ندارد و به جست‌وجوی تکراری نیاز داریم.
- **کمترین مربعات وزنی** همان سفید کردن نویز (noise whitening) است: تقسیم بر واریانس همان کاری است که وقتی نویز سفید نیست (نویز ناهمسان‌واریانس) پیش از LS انجام می‌دهید.
- **گرادیان نزولی با اندازه‌ی گام $\eta$** همان ایده‌ی steepest descent در فیلتر تطبیقی LMS است. BFGS یک روش شبه‌نیوتنی است (تقریبی از Hessian می‌سازد)، نزدیک به Gauss–Newton / Levenberg–Marquardt در LS غیرخطی.
- **یک دره‌ی دراز مورب** در سطح خطا یعنی مسئله **بدحالت (ill-conditioned)** است: نسبت مقدار ویژه‌های Hessian بزرگ است، مثل وقتی که رگرسورها به‌شدت همبسته‌اند. پارامترها در یک جهت خوب و در جهت دیگر بد تعیین می‌شوند.
- **reparameterization** ($\lambda = e^{\eta}$) یک تغییر متغیر است که مسئله‌ی مقید را به مسئله‌ی بدون قید تبدیل می‌کند و اغلب حالت (conditioning) مسئله را هم بهتر می‌کند.
- **تفاوت با کار مهندسی:** مجموعه داده‌ها کوچک‌اند (8 نقطه، هرکدام 50 آیتم)، نویز زیاد است، و پارامترها باید از نظر روان‌شناختی *تفسیر* شوند. پس کافی نیست منحنی پیش‌بینی‌شده خوب به نظر برسد؛ تک‌تک مقدارهای پارامتر باید قابل اعتماد باشند.

</div>

### 4. Practical problems and how to handle them · 4. مشکلات عملی و راه‌حل‌ها

**1. Starting values.** Use informed starts: read them off a plot, use a quick linearized fit (Week 2), or take the best point of a coarse grid.

<div dir="rtl">

**1. مقادیر شروع.** از شروع‌های آگاهانه استفاده کنید: از روی نمودار بخوانید، یک برازش خطی‌شده‌ی سریع (هفته‌ی 2) بگیرید، یا بهترین نقطه‌ی یک شبکه‌ی درشت را بردارید.

</div>

**2. Local minima → multi-start.** Run the optimizer from many random starting points and keep the best solution. If many starts agree on the same minimum, you can be reasonably confident it is the global one. Multi-start is cheap insurance; use it routinely for models with more than two parameters.

<div dir="rtl">

**2. کمینه‌های محلی ← multi-start.** بهینه‌ساز را از تعداد زیادی نقطه‌ی شروع تصادفی اجرا کنید و بهترین جواب را نگه دارید. اگر شروع‌های زیادی روی یک کمینه توافق کنند، می‌توانید نسبتاً مطمئن باشید که کمینه‌ی سراسری است. multi-start بیمه‌ی ارزانی است؛ برای مدل‌های بیش از دو پارامتر همیشه از آن استفاده کنید.

</div>

**3. Parameter bounds.** Many parameters have natural ranges ($0 \le A \le 1$, $\lambda > 0$). Without constraints, optimizers happily return $A = 29.6$. Three approaches:

<div dir="rtl">

**3. کران پارامترها.** بسیاری از پارامترها دامنه‌ی طبیعی دارند ($0 \le A \le 1$، $\lambda > 0$). بدون قید، بهینه‌سازها با خیال راحت $A = 29.6$ برمی‌گردانند. سه رویکرد:

</div>

| Approach | How | Comment |
|---|---|---|
| Bounded optimizer | `method="L-BFGS-B"` or `"Nelder-Mead"` with `bounds=` | Easiest; recommended default |
| **Reparameterization** | Optimize over unconstrained $\eta$ and transform: $\lambda = e^{\eta}$ (positive), $A = 1/(1 + e^{-\alpha_A})$ (between 0 and 1) | Works with any optimizer; also used in Bayesian modeling (Week 13) |
| Penalty | Return a huge SSE when parameters are out of range | Creates discontinuities; avoid |

<div dir="rtl">

| رویکرد | چطور | توضیح |
|---|---|---|
| بهینه‌ساز کران‌دار | `method="L-BFGS-B"` یا `"Nelder-Mead"` با `bounds=` | ساده‌ترین؛ پیش‌فرض توصیه‌شده |
| **reparameterization** | روی $\eta$ بدون قید بهینه کنید و تبدیل کنید: $\lambda = e^{\eta}$ (مثبت)، $A = 1/(1 + e^{-\alpha_A})$ (بین 0 و 1) | با هر بهینه‌سازی کار می‌کند؛ در مدل‌سازی بیزی هم استفاده می‌شود (هفته‌ی 13) |
| جریمه | وقتی پارامتر خارج از دامنه است یک SSE خیلی بزرگ برگردانید | ناپیوستگی می‌سازد؛ از آن پرهیز کنید |

</div>

**4. Non-identifiability.** Sometimes *several* parameter combinations fit equally well. An example is a two-component model whose two components can swap labels. This is a property of the model, not a failure of the optimizer, and multi-start reveals it (lab Part D).

<div dir="rtl">

**4. non-identifiability.** گاهی *چند* ترکیب پارامتر به یک اندازه خوب برازش می‌شوند. مثالش مدلی دوجزئی است که برچسب دو جزئش قابل جابه‌جایی است. این ویژگی خود مدل است، نه شکست بهینه‌ساز، و multi-start آن را آشکار می‌کند (بخش D lab).

</div>

**5. Trust, but verify.** `result.success == True` only means that the algorithm's stopping rule was met. Always (i) plot the fitted curve over the data, (ii) look at the residuals, and (iii) check that the estimates are within plausible ranges.

<div dir="rtl">

**5. اعتماد کن، ولی بررسی کن.** `result.success == True` فقط یعنی قاعده‌ی توقف الگوریتم برقرار شده است. همیشه (1) منحنی برازش‌شده را روی داده رسم کنید، (2) به باقی‌مانده‌ها نگاه کنید، و (3) بررسی کنید برآوردها در دامنه‌ی معقول باشند.

</div>

**A fitting checklist (use it in every lab from now on):**

<div dir="rtl">

**چک‌لیست برازش (از این به بعد در هر lab از آن استفاده کنید):**

</div>

1. Plot the data.
2. Write the model and the discrepancy function; test them on a few hand-picked parameter values.
3. Choose sensible bounds and starting values.
4. Optimize, preferably with multi-start.
5. Check the convergence message, the plot, the residuals and the parameter ranges.
6. Run a recovery check: simulate data from the fitted parameters, refit, and compare (Week 7 makes this systematic).

<div dir="rtl">

1. داده‌ها را رسم کنید.
2. مدل و تابع ناهمخوانی را بنویسید؛ آن‌ها را روی چند مقدار پارامتر دلخواه آزمون کنید.
3. کران‌ها و مقادیر شروع معقول انتخاب کنید.
4. بهینه کنید، ترجیحاً با multi-start.
5. پیام همگرایی، نمودار، باقی‌مانده‌ها و دامنه‌ی پارامترها را بررسی کنید.
6. یک بررسی بازیابی انجام دهید: از پارامترهای برازش‌شده داده شبیه‌سازی کنید، دوباره برازش کنید و مقایسه کنید (هفته‌ی 7 این را نظام‌مند می‌کند).

</div>

> **Advanced: conditionally linear parameters.** In $f(t) = A\,e^{-\lambda t}$, for any fixed $\lambda$ the best $A$ has a closed form, because the model is linear in $A$: $\hat A(\lambda) = \sum_i y_i g_i / \sum_i g_i^2$ with $g_i = e^{-\lambda t_i}$. Substituting it back gives a one-dimensional problem in $\lambda$ alone. This trick ("profiling out" linear parameters, or *variable projection*) makes fitting faster and more stable, and the resulting 1-D function is related to the *profile likelihood* of Week 5.

<div dir="rtl">

> **پیشرفته: پارامترهای شرطاً خطی.** در $f(t) = A\,e^{-\lambda t}$، برای هر $\lambda$ ثابت بهترین $A$ فرم بسته دارد، چون مدل نسبت به $A$ خطی است: $\hat A(\lambda) = \sum_i y_i g_i / \sum_i g_i^2$ با $g_i = e^{-\lambda t_i}$. جای‌گذاری آن مسئله را به یک مسئله‌ی یک‌بعدی فقط بر حسب $\lambda$ تبدیل می‌کند. این ترفند (حذف پارامترهای خطی یا *variable projection*) برازش را سریع‌تر و پایدارتر می‌کند، و تابع یک‌بعدی حاصل با *profile likelihood* هفته‌ی 5 مرتبط است.

</div>

#### For the instructor · برای مدرس

- **Show the landscape first.** A contour plot of SSE over $(A, \lambda)$ (lab Part B) makes every later idea concrete: the minimum, the diagonal valley, the plateau. Put it on the projector early and keep coming back to it.
- **Act out Nelder–Mead.** Draw a triangle on the contour plot and do one reflection by hand (worked example Step 2). Students remember the "tumbling triangle" much better than the table of moves.
- **Your strength:** you know gradient descent and least squares. Spend less time on the algorithms and more on the *failure modes* (Part D of the lab): an optimizer reporting success at $A = 29.6$ is the most memorable lesson of the week.
- **Typical questions.**
  - *"Which optimizer should I use?"* For small cognitive models: Nelder–Mead or L-BFGS-B with bounds, always with multi-start.
  - *"Why not always use a grid?"* The cost grows exponentially with the number of parameters.
  - *"Is SSE the right measure?"* Only if noise is Gaussian with equal variance; next week replaces it with the likelihood.

<div dir="rtl">

- **اول منظره را نشان دهید.** نمودار تراز SSE روی $(A, \lambda)$ (بخش B lab) همه‌ی ایده‌های بعدی را ملموس می‌کند: کمینه، دره‌ی مورب، فلات. آن را زود روی پروژکتور بیاورید و مدام به آن برگردید.
- **Nelder–Mead را اجرا کنید.** یک مثلث روی نمودار تراز بکشید و یک بازتاب (reflection) را با دست انجام دهید (قدم 2 مثال حل‌شده). دانشجوها «مثلثی که قل می‌خورد» را خیلی بهتر از جدول حرکت‌ها به خاطر می‌سپارند.
- **نقطه‌ی قوت شما:** شما gradient descent و کمترین مربعات را می‌شناسید. وقت کمتری روی الگوریتم‌ها و وقت بیشتری روی *حالت‌های شکست* بگذارید (بخش D lab): بهینه‌سازی که در $A = 29.6$ اعلام موفقیت می‌کند، به‌یادماندنی‌ترین درس این هفته است.
- **سؤال‌های رایج.**
  - *«از کدام بهینه‌ساز استفاده کنم؟»* برای مدل‌های شناختی کوچک: Nelder–Mead یا L-BFGS-B با کران، همیشه همراه با multi-start.
  - *«چرا همیشه از grid استفاده نکنیم؟»* هزینه با تعداد پارامترها به‌طور نمایی زیاد می‌شود.
  - *«آیا SSE معیار درستی است؟»* فقط اگر نویز گاوسی و با واریانس برابر باشد؛ هفته‌ی بعد درست‌نمایی جای آن را می‌گیرد.

</div>

---

## Worked example · مثال حل‌شده

**Data.** A participant recalls proportions $y = (0.62, 0.41, 0.19)$ at $t = (1, 3, 7)$ days. Model: $f(t) = A\,e^{-\lambda t}$.

<div dir="rtl">

**داده.** یک شرکت‌کننده نسبت‌های $y = (0.62, 0.41, 0.19)$ را در $t = (1, 3, 7)$ روز به یاد می‌آورد. مدل: $f(t) = A\,e^{-\lambda t}$.

</div>

### Step 1: a small grid search by hand · قدم 1: یک جستجوی شبکه‌ای کوچک با دست

For $(A, \lambda) = (0.8, 0.2)$: predictions $0.8e^{-0.2} = 0.655$, $0.8e^{-0.6} = 0.439$, $0.8e^{-1.4} = 0.197$, so

<div dir="rtl">

برای $(A, \lambda) = (0.8, 0.2)$: پیش‌بینی‌ها $0.8e^{-0.2} = 0.655$، $0.8e^{-0.6} = 0.439$، $0.8e^{-1.4} = 0.197$، پس

</div>

$$
\mathrm{SSE} = (0.62 - 0.655)^2 + (0.41 - 0.439)^2 + (0.19 - 0.197)^2 = 0.00123 + 0.00084 + 0.00005 \approx 0.00212.
$$

Repeating this for a 2 × 3 grid:

<div dir="rtl">

با تکرار این کار برای یک شبکه‌ی 2 × 3:

</div>

| | $\lambda = 0.15$ | $\lambda = 0.20$ | $\lambda = 0.25$ |
|---|---|---|---|
| $A = 0.8$ | 0.02281 | **0.00212** | 0.00364 |
| $A = 0.9$ | 0.06638 | 0.02172 | 0.00791 |

<div dir="rtl">

| | $\lambda = 0.15$ | $\lambda = 0.20$ | $\lambda = 0.25$ |
|---|---|---|---|
| $A = 0.8$ | 0.02281 | **0.00212** | 0.00364 |
| $A = 0.9$ | 0.06638 | 0.02172 | 0.00791 |

</div>

The grid's best point is $(0.8, 0.20)$. Note the tilt: $(0.9, 0.25)$ beats $(0.9, 0.15)$ by far. A larger $A$ "wants" a larger $\lambda$, which is the trade-off valley.

<div dir="rtl">

بهترین نقطه‌ی شبکه $(0.8, 0.20)$ است. به کجی دقت کنید: $(0.9, 0.25)$ خیلی بهتر از $(0.9, 0.15)$ است. $A$ بزرگ‌تر یک $\lambda$ بزرگ‌تر «می‌خواهد»؛ این همان دره‌ی trade-off است.

</div>

### Step 2: one Nelder–Mead iteration by hand · قدم 2: یک تکرار Nelder–Mead با دست

Start with the simplex (triangle) of three grid points:

<div dir="rtl">

با سیمپلکس (مثلث) سه نقطه‌ی شبکه شروع کنید:

</div>

| Vertex | $(A, \lambda)$ | SSE | Rank |
|---|---|---|---|
| $\boldsymbol\theta_b$ | (0.8, 0.25) | 0.00364 | best |
| $\boldsymbol\theta_g$ | (0.8, 0.15) | 0.02281 | second-worst |
| $\boldsymbol\theta_w$ | (0.9, 0.15) | 0.06638 | worst |

<div dir="rtl">

| رأس | $(A, \lambda)$ | SSE | رتبه |
|---|---|---|---|
| $\boldsymbol\theta_b$ | (0.8, 0.25) | 0.00364 | بهترین |
| $\boldsymbol\theta_g$ | (0.8, 0.15) | 0.02281 | دومین بدترین |
| $\boldsymbol\theta_w$ | (0.9, 0.15) | 0.06638 | بدترین |

</div>

1. **Centroid** of all vertices except the worst: $\bar{\boldsymbol\theta} = \big((0.8 + 0.8)/2,\ (0.25 + 0.15)/2\big) = (0.8, 0.20)$.
2. **Reflect** the worst vertex through the centroid: $\boldsymbol\theta_r = (0.8, 0.20) + \big((0.8, 0.20) - (0.9, 0.15)\big) = (0.7, 0.25)$.
3. **Evaluate:** predictions $(0.545, 0.331, 0.122)$, so $\mathrm{SSE}(\boldsymbol\theta_r) = 0.01657$.
4. **Decide:** $0.00364 \le 0.01657 < 0.02281$. The reflected point is better than the second-worst but not better than the best, so we **accept the reflection** (no expansion).
5. **New simplex:** $\{(0.8, 0.25),\ (0.7, 0.25),\ (0.8, 0.15)\}$, and the worst SSE has dropped from 0.066 to 0.023.

<div dir="rtl">

1. **مرکز ثقل** همه‌ی رأس‌ها جز بدترین: $\bar{\boldsymbol\theta} = \big((0.8 + 0.8)/2,\ (0.25 + 0.15)/2\big) = (0.8, 0.20)$.
2. **بازتاب** بدترین رأس از میان مرکز ثقل: $\boldsymbol\theta_r = (0.8, 0.20) + \big((0.8, 0.20) - (0.9, 0.15)\big) = (0.7, 0.25)$.
3. **ارزیابی:** پیش‌بینی‌ها $(0.545, 0.331, 0.122)$، پس $\mathrm{SSE}(\boldsymbol\theta_r) = 0.01657$.
4. **تصمیم:** $0.00364 \le 0.01657 < 0.02281$. نقطه‌ی بازتاب‌شده از دومین بدترین بهتر است ولی از بهترین بهتر نیست، پس **بازتاب را می‌پذیریم** (بدون گسترش).
5. **سیمپلکس جدید:** $\{(0.8, 0.25),\ (0.7, 0.25),\ (0.8, 0.15)\}$، و بدترین SSE از 0.066 به 0.023 کم شده است.

</div>

### Step 3: let the computer finish · قدم 3: بگذارید کامپیوتر تمامش کند

Running `scipy.optimize.minimize(..., method="Nelder-Mead")` from $(0.8, 0.2)$ converges to $\hat A = 0.754$, $\hat\lambda = 0.200$, with $\mathrm{SSE} = 3.7 \times 10^{-5}$ (RMSD $= 0.0035$).

<div dir="rtl">

اجرای `scipy.optimize.minimize(..., method="Nelder-Mead")` از $(0.8, 0.2)$ به $\hat A = 0.754$، $\hat\lambda = 0.200$ با $\mathrm{SSE} = 3.7 \times 10^{-5}$ (RMSD $= 0.0035$) همگرا می‌شود.

</div>

**Interpretation.** The fitted model says this participant would recall about 75% immediately after learning and loses about 18% of the remaining material per day ($1 - e^{-0.2} = 0.181$), with a half-life of $\ln 2 / 0.2 \approx 3.5$ days. With only three data points and two parameters, the near-perfect fit says very little about whether the exponential model is *right*. Any reasonable two-parameter decreasing curve would fit three points well (Week 6).

<div dir="rtl">

**تفسیر.** مدل برازش‌شده می‌گوید این شرکت‌کننده بلافاصله بعد از یادگیری حدود 75% را به یاد می‌آورد و هر روز حدود 18% از باقی‌مانده را از دست می‌دهد ($1 - e^{-0.2} = 0.181$)، با نیمه‌عمر $\ln 2 / 0.2 \approx 3.5$ روز. با فقط سه داده و دو پارامتر، برازش تقریباً کامل چیز زیادی درباره‌ی *درست بودن* مدل نمایی نمی‌گوید. هر منحنی نزولی دوپارامتری معقولی سه نقطه را خوب برازش می‌کند (هفته‌ی 6).

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Write an SSE function and explore the error surface of two forgetting models.
2. Fit by grid search, then with Nelder–Mead and L-BFGS-B; compare with last week's linearized fits.
3. Provoke and fix fitting failures: plateaus, local minima and out-of-range estimates.
4. **Evaluate** the fits (RMSD, residuals, comparison with the true values) and **interpret** the parameters.

<div dir="rtl">

1. نوشتن یک تابع SSE و بررسی سطح خطای دو مدل فراموشی.
2. برازش با جستجوی شبکه‌ای، سپس با Nelder–Mead و L-BFGS-B؛ مقایسه با برازش‌های خطی‌شده‌ی هفته‌ی قبل.
3. ایجاد و رفع شکست‌های برازش: فلات‌ها، کمینه‌های محلی و برآوردهای خارج از دامنه.
4. **ارزیابی** برازش‌ها (RMSD، باقی‌مانده‌ها، مقایسه با مقادیر واقعی) و **تفسیر** پارامترها.

</div>

**Timing:** Part A 15 min · Part B 25 min · Part C 25 min · Part D 35 min · Part E 20 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 15 دقیقه · بخش B 25 دقیقه · بخش C 25 دقیقه · بخش D 35 دقیقه · بخش E 20 دقیقه.

</div>

### Setup and data · آماده‌سازی و داده

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 1 · سلول 1

### Part A: Get a feel for the discrepancy function (15 min) · بخش A: آشنایی با تابع ناهمخوانی (15 دقیقه)

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
theta = (0.9, 0.5):  power SSE = 0.0349   exponential SSE = 0.4511
theta = (0.8, 0.4):  power SSE = 0.0328   exponential SSE = 0.4145
theta = (0.9, 0.1):  power SSE = 0.9047   exponential SSE = 0.2192
theta = (0.6, 0.05):  power SSE = 0.3303   exponential SSE = 0.1145
```

Before running the next parts, **predict**: which parameter values will give the smallest SSE for each model? Write your guess down.

<div dir="rtl">

پیش از اجرای بخش‌های بعد **پیش‌بینی کنید**: کدام مقادیر پارامتر کمترین SSE را برای هر مدل می‌دهند؟ حدستان را یادداشت کنید.

</div>

### Part B: Grid search and the error surface (25 min) · بخش B: جستجوی شبکه‌ای و سطح خطا (25 دقیقه)

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
exp: grid minimum A = 0.655, rate = 0.0560, SSE = 0.10607  (42300 evaluations)
pow: grid minimum A = 0.870, rate = 0.4239, SSE = 0.02592  (42300 evaluations)
```

**What to notice:** both surfaces have a single basin, but it is an **elongated, tilted valley**: higher $A$ goes with higher decay. That is the parameter trade-off. For the power model the true value (white ×) lies inside the valley but not at its bottom: with finite data, the best fit is never exactly the truth.

<div dir="rtl">

**به این دقت کنید:** هر دو سطح یک حوضه دارند، ولی یک **دره‌ی کشیده و مورب**: $A$ بالاتر با زوال بیشتر همراه است. این همان trade-off پارامترهاست. برای مدل توانی، مقدار واقعی (× سفید) داخل دره است ولی در ته آن نیست: با داده‌ی محدود، بهترین برازش هیچ‌وقت دقیقاً همان مقدار واقعی نیست.

</div>

### Part C: Fitting with an optimizer (25 min) · بخش C: برازش با یک بهینه‌ساز (25 دقیقه)

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
model            method      A   rate    SSE   RMSD  f_evals success
  exp          L-BFGS-B 0.6568 0.0566 0.1061 0.1151     39.0    True
  exp       Nelder-Mead 0.6568 0.0566 0.1061 0.1151     69.0    True
  exp              grid 0.6550 0.0560 0.1061 0.1151  42300.0    True
  exp linearized (Wk 2) 0.5500 0.0320 0.1373 0.1310      NaN     NaN
  pow          L-BFGS-B 0.8712 0.4251 0.0259 0.0569     36.0    True
  pow       Nelder-Mead 0.8711 0.4251 0.0259 0.0569     71.0    True
  pow              grid 0.8700 0.4239 0.0259 0.0569  42300.0    True
  pow linearized (Wk 2) 0.7970 0.3700 0.0315 0.0628      NaN     NaN
```

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 5 · سلول 5

**What to notice:**
- Nelder–Mead and L-BFGS-B agree to three or four decimals; the grid is within its spacing (0.005 for $A$) of them. The optimizers needed only 36–71 function evaluations instead of 42 300.
- Least squares gives a **lower SSE** than the linearized fits of Week 2 (it is minimizing exactly that quantity), and the power estimates are much closer to the truth.
- The path first heads quickly into the valley and then crawls along it, a typical pattern.

<div dir="rtl">

**به این‌ها دقت کنید:**
- Nelder–Mead و L-BFGS-B تا سه یا چهار رقم اعشار با هم توافق دارند؛ شبکه در حد فاصله‌ی نقاطش (0.005 برای $A$) با آن‌ها فرق دارد. بهینه‌سازها فقط 36 تا 71 ارزیابی تابع لازم داشتند، به‌جای 42 300.
- کمترین مربعات **SSE کمتری** از برازش‌های خطی‌شده‌ی هفته‌ی 2 می‌دهد (دقیقاً همین کمیت را کمینه می‌کند)، و برآوردهای مدل توانی خیلی به مقدار واقعی نزدیک‌ترند.
- مسیر اول سریع وارد دره می‌شود و بعد آرام در امتدادش می‌خزد؛ یک الگوی معمول.

</div>

### Part D: When fitting goes wrong (35 min) · بخش D: وقتی برازش خراب می‌شود (35 دقیقه)

**D1. A plateau and a false "success".** Start the exponential fit with an absurd decay rate, $\lambda = 20$ per day:

<div dir="rtl">

**D1. یک فلات و یک «موفقیت» کاذب.** برازش نمایی را با یک نرخ زوال بی‌معنی، $\lambda = 20$ در روز، شروع کنید:

</div>

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
BFGS         A =   29.571  lambda =  14.244  SSE = 1.1616  success = True  (Optimization terminated successfully.)
L-BFGS-B     A =   29.905  lambda =  14.289  SSE = 1.1616  success = True  (CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL)
Nelder-Mead  A =    0.657  lambda =   0.057  SSE = 0.1061  success = True  (Optimization terminated successfully.)
```

(The wording of the L-BFGS-B message varies slightly between SciPy versions.) The two gradient-based methods report **success** but return a nonsensical fit: $A$ is around 30 (a recall probability of 3000%!) and the predicted curve is essentially zero at every interval. They started on a plateau where the gradient is almost zero (Lecture §3.3, Advanced box). Nelder–Mead escaped. Lessons: (1) always check estimates and plots, not just `success`; (2) use bounds; (3) use sensible or multiple starting values.

<div dir="rtl">

(متن پیام L-BFGS-B بین نسخه‌های SciPy کمی فرق می‌کند.) دو روش گرادیانی **موفقیت** گزارش می‌کنند ولی برازشی بی‌معنی برمی‌گردانند: $A$ حدود 30 است (احتمال یادآوری 3000%!) و منحنی پیش‌بینی‌شده عملاً در همه‌ی فاصله‌ها صفر است. آن‌ها روی فلاتی شروع کردند که گرادیان در آن تقریباً صفر است (کادر «پیشرفته» بخش 3.3 جزوه). Nelder–Mead فرار کرد. درس‌ها: (1) همیشه برآوردها و نمودارها را بررسی کنید، نه فقط `success` را؛ (2) از کران استفاده کنید؛ (3) از مقادیر شروع معقول یا متعدد استفاده کنید.

</div>

**D2. Reparameterization.** Make the parameters unconstrained so that *any* optimizer respects the ranges $0 < A < 1$ and $\lambda > 0$:

<div dir="rtl">

**D2. reparameterization.** پارامترها را بدون قید کنید تا *هر* بهینه‌سازی دامنه‌های $0 < A < 1$ و $\lambda > 0$ را رعایت کند:

</div>

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 7 · سلول 7

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
BFGS on reparameterized power model: A = 0.8712, d = 0.4251, SSE = 0.02592
```

Same answer as in Part C, and the estimates are guaranteed to lie in range.

<div dir="rtl">

همان جواب بخش C، و تضمین می‌شود که برآوردها در دامنه باشند.

</div>

**D3. Local minima and multi-start.** A popular idea in memory research is that forgetting reflects two memory traces: a **fast** component that decays quickly and a **slow** one that lasts:

<div dir="rtl">

**D3. کمینه‌های محلی و multi-start.** یک ایده‌ی رایج در پژوهش‌های حافظه این است که فراموشی بازتاب دو رد حافظه (memory trace) است: یک جزء **سریع** که زود زوال پیدا می‌کند و یک جزء **کند** که می‌ماند:

</div>

$$
f(t) = A_1 e^{-\lambda_1 t} + A_2 e^{-\lambda_2 t}.
$$

This model has $k = 4$ parameters, and its error surface has several basins. Fit it from 50 random starting points:

<div dir="rtl">

این مدل $k = 4$ پارامتر دارد و سطح خطایش چند حوضه دارد. آن را از 50 نقطه‌ی شروع تصادفی برازش کنید:

</div>

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 8 · سلول 8

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Distinct final SSE values (rounded) and how often each was reached:
  SSE = 0.0201: 42 starts
  SSE = 0.0203: 1 starts
  SSE = 0.0337: 1 starts
  SSE = 0.0340: 1 starts
  SSE = 0.0359: 1 starts
  SSE = 0.1064: 1 starts
  SSE = 0.2010: 1 starts
  SSE = 0.2456: 1 starts
  SSE = 0.9092: 1 starts
Best 3 solutions (A1, lam1, A2, lam2):
   [0.58  0.36  0.264 0.   ] SSE = 0.02013
   [0.264 0.    0.58  0.36 ] SSE = 0.02013
   [0.264 0.    0.58  0.36 ] SSE = 0.02013
```

**What to notice:**
- About 40 of 50 starts end in the same best basin, but the rest (about 1 in 6) get stuck in **worse local minima**, some with an SSE many times larger. (The exact counts differ slightly between SciPy versions; with SciPy 1.18 it is 41 of 50.) A single run from an unlucky start would have given a wrong answer, and no warning.
- Among the best solutions, the fast and slow components may appear **with labels swapped** ($A_1, \lambda_1 \leftrightarrow A_2, \lambda_2$). Both describe the same curve. This is a non-identifiability built into the model, and a common fix is to impose an order constraint such as $\lambda_1 > \lambda_2$.
- In the best solution one component has a rate of exactly 0 (a flat, non-decaying component of 0.264). The fitted two-trace model has therefore collapsed into the exponential-with-asymptote model of Exercise 4, with the same SSE (0.0201). Is that a meaningful "permanent memory" or just the extra parameters absorbing noise? Remember that the data came from a *power* model. Fit alone cannot tell (Weeks 6–7).

<div dir="rtl">

**به این‌ها دقت کنید:**
- حدود 40 شروع از 50 در همان بهترین حوضه تمام می‌شوند، ولی بقیه (حدود 1 از 6) در **کمینه‌های محلی بدتر** گیر می‌کنند؛ بعضی با SSE چند برابر بزرگ‌تر. (تعداد دقیق بین نسخه‌های SciPy کمی فرق دارد؛ با SciPy 1.18 برابر 41 از 50 است.) یک اجرای تنها از یک شروع بدشانس جواب غلطی می‌داد، بدون هیچ هشداری.
- در میان بهترین جواب‌ها، اجزای سریع و کند ممکن است **با برچسب‌های جابه‌جا** ظاهر شوند ($A_1, \lambda_1 \leftrightarrow A_2, \lambda_2$). هر دو همان منحنی را توصیف می‌کنند. این یک non-identifiability ذاتی مدل است، و راه‌حل رایج اعمال قید ترتیبی مثل $\lambda_1 > \lambda_2$ است.
- در بهترین جواب، یکی از اجزا نرخ دقیقاً 0 دارد (یک جزء ثابت و بدون زوال به اندازه‌ی 0.264). پس مدل دوردی برازش‌شده به مدل نمایی با مجانب تمرین 4 تبدیل شده، با همان SSE (0.0201). آیا این یک «حافظه‌ی دائمی» معنادار است یا فقط پارامترهای اضافه نویز را جذب کرده‌اند؟ یادتان باشد داده‌ها از یک مدل *توانی* آمده‌اند. برازش به‌تنهایی نمی‌تواند جواب دهد (هفته‌های 6–7).

</div>

### Part E: Evaluate and interpret (20 min) · بخش E: ارزیابی و تفسیر (20 دقیقه)

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 9 · سلول 9

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Power model: relative loss rate at t =  1 days: 0.213 per day
Power model: relative loss rate at t = 20 days: 0.020 per day
Exponential model: constant relative loss rate 0.057 per day
```

**Interpret (write 2–3 sentences for each in your notebook):**

<div dir="rtl">

**تفسیر (برای هرکدام 2 تا 3 جمله در notebook بنویسید):**

</div>

1. Compare the residual patterns. Which model shows a systematic pattern, and what does that pattern say about the shape of forgetting in these data?
2. The power model's relative loss rate falls from about 0.21 per day after 1 day to about 0.02 per day after 20 days. Explain in plain language what this claims about memory.
3. The least-squares estimates ($\hat A \approx 0.87$, $\hat d \approx 0.43$) are closer to the truth than last week's linearized estimates but still not equal to it. Is this a failure of the method? (Hint: what would happen if you reran the experiment with a new random sample?)

<div dir="rtl">

1. الگوهای باقی‌مانده‌ها را مقایسه کنید. کدام مدل الگوی نظام‌مند نشان می‌دهد، و آن الگو درباره‌ی شکل فراموشی در این داده‌ها چه می‌گوید؟
2. نرخ نسبی فراموشی مدل توانی از حدود 0.21 در روز بعد از 1 روز به حدود 0.02 در روز بعد از 20 روز می‌رسد. به زبان ساده توضیح دهید این چه ادعایی درباره‌ی حافظه دارد.
3. برآوردهای کمترین مربعات ($\hat A \approx 0.87$، $\hat d \approx 0.43$) از برآوردهای خطی‌شده‌ی هفته‌ی قبل به مقدار واقعی نزدیک‌ترند ولی هنوز با آن برابر نیستند. آیا این شکست روش است؟ (راهنمایی: اگر آزمایش را با یک نمونه‌ی تصادفی جدید تکرار می‌کردید چه می‌شد؟)

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★ (same minimizer).** Fit the power model by minimizing SSE, MSE and RMSD in turn. Show that the estimates agree (up to optimizer tolerance). Why do we still prefer to *report* RMSD?

<div dir="rtl">

**تمرین 1 ★ (کمینه‌کننده‌ی یکسان).** مدل توانی را یک بار با کمینه کردن SSE، یک بار MSE و یک بار RMSD برازش کنید. نشان دهید برآوردها (در حد تلرانس بهینه‌ساز) یکسان‌اند. چرا باز هم ترجیح می‌دهیم RMSD را *گزارش* کنیم؟

</div>

**Exercise 2 ★ (Ebbinghaus by least squares).** Refit the Ebbinghaus savings data from Week 2, Exercise 3 (values marked [verify]) with least squares, for both models. Compare the parameters and RMSD with your linearized fits from Week 2.

<div dir="rtl">

**تمرین 2 ★ (ابینگهاوس با کمترین مربعات).** داده‌های savings ابینگهاوس از تمرین 3 هفته‌ی 2 (مقادیر با علامت [بررسی شود]) را برای هر دو مدل با کمترین مربعات دوباره برازش کنید. پارامترها و RMSD را با برازش‌های خطی‌شده‌ی هفته‌ی 2 مقایسه کنید.

</div>

**Exercise 3 ★★ (weighted least squares).** Binomial proportions have variance $f(1-f)/n$. Implement WSSE (Lecture §1) using the **predicted** $f$ in the variance, refit the power model and compare the estimates with plain least squares. Which data points gain influence and which lose it? (Next week you will see that maximum likelihood does this weighting automatically.)

<div dir="rtl">

**تمرین 3 ★★ (کمترین مربعات وزنی).** نسبت‌های دوجمله‌ای واریانس $f(1-f)/n$ دارند. WSSE (بخش 1 جزوه) را با استفاده از $f$ **پیش‌بینی‌شده** در واریانس پیاده‌سازی کنید، مدل توانی را دوباره برازش کنید و برآوردها را با کمترین مربعات ساده مقایسه کنید. کدام نقاط داده تأثیر بیشتری پیدا می‌کنند و کدام کمتر؟ (هفته‌ی بعد می‌بینید که بیشینه درست‌نمایی این وزن‌دهی را خودکار انجام می‌دهد.)

</div>

**Exercise 4 ★★ (more parameters, better fit?).** Fit the three-parameter **exponential-with-asymptote** model $f(t) = B + (A - B)e^{-\lambda t}$, where $B$ is the long-term asymptote, using bounds $0 \le B \le A \le 1$ (hint: reparameterize, or check the constraint after fitting). *Expected:* SSE ≈ 0.020, **lower** than the power model's ≈ 0.026, even though the data were generated by the power model! What does this tell you about using SSE to choose between models with different numbers of parameters? (We answer this properly in Weeks 6–7.)

<div dir="rtl">

**تمرین 4 ★★ (پارامتر بیشتر، برازش بهتر؟).** مدل سه‌پارامتری **نمایی با مجانب** $f(t) = B + (A - B)e^{-\lambda t}$ را که در آن $B$ مجانب بلندمدت است، با کران‌های $0 \le B \le A \le 1$ برازش کنید (راهنمایی: reparameterize کنید، یا قید را بعد از برازش بررسی کنید). *انتظار:* SSE ≈ 0.020 که **کمتر** از SSE ≈ 0.026 مدل توانی است، با اینکه داده‌ها از مدل توانی تولید شده‌اند! این درباره‌ی استفاده از SSE برای انتخاب بین مدل‌هایی با تعداد پارامتر متفاوت چه می‌گوید؟ (در هفته‌های 6–7 جواب درست این را می‌دهیم.)

</div>

**Exercise 5 ★★★ (Advanced: Nelder–Mead from scratch).** Implement Nelder–Mead for $k = 2$ using the moves in Lecture §3.2 (reflect, expand, inside/outside contract, shrink) and a stopping rule based on the spread of SSE values in the simplex. Run it on the power model from $(0.8, 0.2)$, plot the simplex every few iterations on the error surface, and compare the result and number of function evaluations with `scipy`.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: Nelder–Mead از صفر).** Nelder–Mead را برای $k = 2$ با حرکت‌های بخش 3.2 جزوه (بازتاب، گسترش، انقباض داخلی/خارجی، جمع‌شدن) و یک قاعده‌ی توقف بر اساس پراکندگی مقادیر SSE در سیمپلکس پیاده‌سازی کنید. آن را روی مدل توانی از $(0.8, 0.2)$ اجرا کنید، سیمپلکس را هر چند تکرار یک بار روی سطح خطا رسم کنید، و نتیجه و تعداد ارزیابی‌های تابع را با `scipy` مقایسه کنید.

</div>

### Lab check-off · lab check-off

Show the instructor or TA: (1) the error-surface plots with grid minima (Part B), (2) the comparison table from Part C, (3) your multi-start histogram (Part D3) with one sentence on what it shows, and (4) your answer to interpretation question 1 (Part E).

<div dir="rtl">

به مدرس یا دستیار آموزشی نشان دهید: (1) نمودارهای سطح خطا با کمینه‌های شبکه (بخش B)، (2) جدول مقایسه از بخش C، (3) هیستوگرام multi-start (بخش D3) با یک جمله درباره‌ی آنچه نشان می‌دهد، و (4) جوابتان به سؤال تفسیری 1 (بخش E).

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Scaling laws are curve fitting.** One of the most influential results in modern AI is that the test loss of language models falls smoothly with model size $N$, data size and compute, following a **power law** with an asymptote: $L(N) = E + B\,N^{-\alpha}$ (Kaplan et al., 2020; Hoffmann et al., 2022). Companies use such fits to decide how big the next model should be. Mathematically, this is the same problem as fitting a forgetting curve: a nonlinear model with three parameters, fitted by least squares with a numerical optimizer and multiple starting points. It has the same pitfalls too: extrapolation far beyond the data, and trade-offs between parameters (here $E$ and $\alpha$).

<div dir="rtl">

**قانون‌های مقیاس (scaling laws) همان برازش منحنی‌اند.** یکی از تأثیرگذارترین نتایج هوش مصنوعی امروز این است که خطای آزمون (test loss) مدل‌های زبانی با اندازه‌ی مدل $N$، اندازه‌ی داده و محاسبات به‌طور هموار کم می‌شود و از یک **قانون توانی** با مجانب پیروی می‌کند: $L(N) = E + B\,N^{-\alpha}$ (Kaplan et al., 2020; Hoffmann et al., 2022). شرکت‌ها از چنین برازش‌هایی استفاده می‌کنند تا تصمیم بگیرند مدل بعدی چقدر بزرگ باشد. از نظر ریاضی، این همان مسئله‌ی برازش منحنی فراموشی است: یک مدل غیرخطی با سه پارامتر که با کمترین مربعات، یک بهینه‌ساز عددی و چند نقطه‌ی شروع برازش می‌شود. دام‌هایش هم همان‌اند: برون‌یابی (extrapolation) خیلی دورتر از داده، و trade-off پارامترها (اینجا $E$ و $\alpha$).

</div>

> **Code · کد:** [`code/week03.py`](code/week03.py), cell 10 · سلول 10

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
E = 1.70, B = 3.22, alpha = 0.358, SSE = 0.00424
Extrapolated loss at N = 1e11: 1.754
```

**Try it (no API needed).**
- ★ Fit a pure power law without the asymptote ($E = 0$). Compare the SSE and the extrapolation to $N = 10^{11}$. Which conclusion about "bigger is better" changes?
- ★★ Fit only the four smallest models and extrapolate to the four largest. How far off is the prediction? Repeat with different seeds to see how stable the extrapolation is.
- ★★ Plot the SSE surface over $E$ and $\alpha$ (with $B$ at its best value for each pair). Is there a ridge, as in the Week 3 lab?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ یک قانون توانی خالص بدون مجانب ($E = 0$) برازش کنید. SSE و برون‌یابی تا $N = 10^{11}$ را مقایسه کنید. کدام نتیجه‌گیری درباره‌ی «بزرگ‌تر بهتر است» عوض می‌شود؟
- ★★ فقط چهار مدل کوچک‌تر را برازش کنید و تا چهار مدل بزرگ‌تر برون‌یابی کنید. پیش‌بینی چقدر خطا دارد؟ با seedهای مختلف تکرار کنید تا ببینید برون‌یابی چقدر پایدار است.
- ★★ سطح SSE را روی $E$ و $\alpha$ رسم کنید (با $B$ در بهترین مقدارش برای هر جفت). آیا مثل lab هفته‌ی 3 یک ridge وجود دارد؟

</div>

*Optional reading:* Kaplan, J., et al. (2020). Scaling laws for neural language models. *arXiv:2001.08361*. Hoffmann, J., et al. (2022). Training compute-optimal large language models. *arXiv:2203.15556*.

<div dir="rtl">

*مطالعه‌ی اختیاری:* Kaplan, J., et al. (2020). Scaling laws for neural language models. *arXiv:2001.08361*. Hoffmann, J., et al. (2022). Training compute-optimal large language models. *arXiv:2203.15556*.

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **"`success=True` means the fit is good."** It only means a stopping rule was met (Part D1). Always inspect estimates, plots and residuals.
2. **One start is enough.** For anything beyond simple two-parameter models, run multi-start. The cost is small; the risk of reporting a local minimum is not.
3. **Ignoring parameter ranges.** Unbounded optimizers can return impossible values (negative rates, probabilities above 1). Use bounds or reparameterization.
4. **Comparing SSE across models with different numbers of parameters.** The more flexible model almost always wins on SSE (Exercise 4). That is a question of model *evaluation*, not estimation (Weeks 6–7).
5. **Comparing SSE across datasets of different sizes.** SSE grows with $N$; use RMSD for comparisons.
6. **Treating the minimizer as the true value.** $\hat{\boldsymbol\theta}$ is an estimate with sampling error. A different sample would give a different estimate (Week 5 quantifies this).
7. **Forgetting what least squares assumes.** Plain SSE assumes equal, Gaussian noise for all observations. Proportions, counts and RTs usually violate this.
8. **Using grid search for many parameters.** The cost explodes ($100^k$ evaluations). Use grids only for visualization and starting values.

<div dir="rtl">

1. **«`success=True` یعنی برازش خوب است.»** فقط یعنی یک قاعده‌ی توقف برقرار شده است (بخش D1). همیشه برآوردها، نمودارها و باقی‌مانده‌ها را وارسی کنید.
2. **یک شروع کافی است.** برای هر مدلی فراتر از مدل‌های ساده‌ی دوپارامتری multi-start اجرا کنید. هزینه‌اش کم است؛ خطر گزارش یک کمینه‌ی محلی کم نیست.
3. **نادیده گرفتن دامنه‌ی پارامترها.** بهینه‌سازهای بدون کران می‌توانند مقادیر ناممکن برگردانند (نرخ منفی، احتمال بیشتر از 1). از کران یا reparameterization استفاده کنید.
4. **مقایسه‌ی SSE بین مدل‌هایی با تعداد پارامتر متفاوت.** مدل منعطف‌تر تقریباً همیشه در SSE برنده است (تمرین 4). این سؤالی درباره‌ی *ارزیابی* مدل است، نه برآورد (هفته‌های 6–7).
5. **مقایسه‌ی SSE بین مجموعه‌داده‌هایی با اندازه‌ی متفاوت.** SSE با $N$ بزرگ می‌شود؛ برای مقایسه از RMSD استفاده کنید.
6. **کمینه‌کننده را همان مقدار واقعی دانستن.** $\hat{\boldsymbol\theta}$ برآوردی با خطای نمونه‌گیری است. نمونه‌ی دیگر برآورد دیگری می‌دهد (هفته‌ی 5 این را کمّی می‌کند).
7. **فراموش کردن فرض کمترین مربعات.** SSE ساده نویز گاوسی و برابر برای همه‌ی مشاهدات فرض می‌کند. نسبت‌ها، شمارش‌ها و زمان‌های واکنش معمولاً این فرض را نقض می‌کنند.
8. **استفاده از جستجوی شبکه‌ای برای تعداد پارامتر زیاد.** هزینه منفجر می‌شود ($100^k$ ارزیابی). شبکه را فقط برای رسم و مقادیر شروع به کار ببرید.

</div>

---

## Check your understanding · خودآزمایی

**1.** Why do SSE, MSE and RMSD have the same minimizer? Which one would you report, and why?
<details><summary>Answer</summary>
MSE = SSE/N and RMSD = √MSE are strictly increasing transformations of SSE (N is fixed), so the same parameters minimize all three. Report RMSD, because it is in the units of the data and comparable across datasets of different sizes.
</details>

<div dir="rtl">

**1.** چرا SSE، MSE و RMSD کمینه‌کننده‌ی یکسانی دارند؟ کدام را گزارش می‌کنید و چرا؟
<details><summary>پاسخ</summary>
MSE = SSE/N و RMSD = √MSE تبدیل‌های اکیداً صعودی SSE هستند (N ثابت است)، پس همان پارامترها هر سه را کمینه می‌کنند. RMSD را گزارش کنید، چون بر حسب واحد داده است و بین مجموعه‌داده‌هایی با اندازه‌ی متفاوت قابل مقایسه است.
</details>

</div>

**2.** What is a parameter trade-off, and how does it appear on an error surface?
<details><summary>Answer</summary>
Changes in one parameter can be compensated by changes in another, leaving the predictions (and the SSE) almost unchanged. On the surface it appears as an elongated, tilted valley of low SSE. Estimates are then correlated and poorly determined along the valley direction.
</details>

<div dir="rtl">

**2.** trade-off پارامترها چیست و روی سطح خطا چگونه دیده می‌شود؟
<details><summary>پاسخ</summary>
تغییر یک پارامتر را می‌شود با تغییر پارامتر دیگری جبران کرد، طوری که پیش‌بینی‌ها (و SSE) تقریباً عوض نشوند. روی سطح به شکل یک دره‌ی کشیده و مورب با SSE پایین دیده می‌شود. در این حالت برآوردها همبسته‌اند و در جهت دره ضعیف تعیین می‌شوند.
</details>

</div>

**3.** With 50 grid values per parameter, how many SSE evaluations does a grid search need for a model with 6 parameters? What does this imply?
<details><summary>Answer</summary>
$50^6 \approx 1.56 \times 10^{10}$ evaluations. Grid search is infeasible beyond 2–3 parameters (the curse of dimensionality); we need iterative optimizers.
</details>

<div dir="rtl">

**3.** با 50 مقدار شبکه برای هر پارامتر، جستجوی شبکه‌ای برای یک مدل 6 پارامتری به چند ارزیابی SSE نیاز دارد؟ این یعنی چه؟
<details><summary>پاسخ</summary>
$50^6 \approx 1.56 \times 10^{10}$ ارزیابی. جستجوی شبکه‌ای فراتر از 2 تا 3 پارامتر عملی نیست (نفرین ابعاد)؛ به بهینه‌سازهای تکراری نیاز داریم.
</details>

</div>

**4.** In one Nelder–Mead iteration, the reflected point is better than the current best vertex. What does the algorithm do next?
<details><summary>Answer</summary>
It tries an expansion: a point twice as far from the centroid in the same direction. It keeps the expanded point if it is better than the reflected point, otherwise the reflected point.
</details>

<div dir="rtl">

**4.** در یک تکرار Nelder–Mead، نقطه‌ی بازتاب‌شده از بهترین رأس فعلی بهتر است. الگوریتم بعد چه می‌کند؟
<details><summary>پاسخ</summary>
یک گسترش امتحان می‌کند: نقطه‌ای در همان جهت با فاصله‌ی دو برابر از مرکز ثقل. اگر نقطه‌ی گسترش‌یافته از نقطه‌ی بازتاب‌شده بهتر باشد آن را نگه می‌دارد، وگرنه نقطه‌ی بازتاب‌شده را.
</details>

</div>

**5.** Why can a gradient-based optimizer stop on a plateau and report success?
<details><summary>Answer</summary>
Its stopping rule is based on the gradient (or step size) being nearly zero. On a plateau the gradient is close to zero even though the point is not a minimum, so the convergence criterion is met.
</details>

<div dir="rtl">

**5.** چرا یک بهینه‌ساز گرادیانی ممکن است روی فلات متوقف شود و موفقیت گزارش کند؟
<details><summary>پاسخ</summary>
قاعده‌ی توقفش بر اساس نزدیک به صفر بودن گرادیان (یا اندازه‌ی گام) است. روی فلات گرادیان نزدیک صفر است با اینکه آن نقطه کمینه نیست، پس معیار همگرایی برقرار می‌شود.
</details>

</div>

**6.** Give two ways to keep a decay-rate parameter positive during fitting.
<details><summary>Answer</summary>
(i) Use a bounded optimizer (e.g., L-BFGS-B or Nelder–Mead with `bounds=[(1e-6, None)]`). (ii) Reparameterize: optimize $\eta$ on the whole real line and set $\lambda = e^{\eta}$.
</details>

<div dir="rtl">

**6.** دو راه برای مثبت نگه داشتن یک پارامتر نرخ زوال در حین برازش بگویید.
<details><summary>پاسخ</summary>
(1) استفاده از بهینه‌ساز کران‌دار (مثلاً L-BFGS-B یا Nelder–Mead با `bounds=[(1e-6, None)]`). (2) reparameterization: $\eta$ را روی کل اعداد حقیقی بهینه کنید و قرار دهید $\lambda = e^{\eta}$.
</details>

</div>

**7.** Multi-start fits of the two-component model reach the same minimum SSE with $(A_1, \lambda_1, A_2, \lambda_2) = (0.58, 0.36, 0.26, 0.00)$ and $(0.26, 0.00, 0.58, 0.36)$. Is this a problem with the optimizer?
<details><summary>Answer</summary>
No. It is label switching: swapping the two components gives the identical curve, so the model is not identifiable without an ordering constraint (e.g., $\lambda_1 > \lambda_2$). The optimizer correctly found two equivalent global minima.
</details>

<div dir="rtl">

**7.** برازش‌های multi-start مدل دوجزئی با $(A_1, \lambda_1, A_2, \lambda_2) = (0.58, 0.36, 0.26, 0.00)$ و $(0.26, 0.00, 0.58, 0.36)$ به یک SSE کمینه‌ی یکسان می‌رسند. آیا این مشکل بهینه‌ساز است؟
<details><summary>پاسخ</summary>
نه. این جابه‌جایی برچسب (label switching) است: جابه‌جا کردن دو جزء دقیقاً همان منحنی را می‌دهد، پس مدل بدون یک قید ترتیبی (مثلاً $\lambda_1 > \lambda_2$) identifiable نیست. بهینه‌ساز به‌درستی دو کمینه‌ی سراسری معادل را پیدا کرده است.
</details>

</div>

---

## Assignment · تکلیف

No new graded assignment is released this week. **A1 (From verbal to formal) is due at the start of the Week 4 lecture.** Today's lab gives you everything needed for A1's calibration step if you want to check your closed-form derivation numerically.

<div dir="rtl">

این هفته تکلیف نمره‌دار جدیدی منتشر نمی‌شود. **A1 (از کلامی به فرمال) در ابتدای درس هفته‌ی 4 تحویل داده می‌شود.** lab امروز همه‌ی چیزهایی را که برای مرحله‌ی کالیبراسیون A1 لازم است به شما می‌دهد، اگر بخواهید استخراج بسته‌ی خود را عددی بررسی کنید.

</div>

**Optional practice (ungraded, recommended before Week 4):** complete lab Exercises 3 and 4. Exercise 3 (weighted least squares) is the bridge to maximum likelihood, and Exercise 4 previews the central problem of model evaluation. Solutions will be discussed briefly at the start of the Week 4 lab.

<div dir="rtl">

**تمرین اختیاری (بدون نمره، پیش از هفته‌ی 4 توصیه می‌شود):** تمرین‌های 3 و 4 lab را کامل کنید. تمرین 3 (کمترین مربعات وزنی) پلی به بیشینه درست‌نمایی است، و تمرین 4 پیش‌نمایشی از مسئله‌ی اصلی ارزیابی مدل است. راه‌حل‌ها در ابتدای lab هفته‌ی 4 به‌طور مختصر بحث می‌شوند.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018), chapter 3.** Basic parameter estimation: discrepancy functions, error surfaces, the simplex algorithm, and practical issues such as local minima and starting values. *(Main reading.)*
- **Ghodousian (1401)**, *Mabani-ye ravesh-haye mostaghim dar behine-sazi gheyr-khatti* (in Persian): direct search methods for nonlinear optimization, including simplex-type methods. Recommended for students who want the theory behind Nelder–Mead [verify chapter].
- **Verguts (2022)**: the chapter on optimization and gradient descent, useful for the gradient-based view that returns in Week 15 (learning models) [verify chapter].

<div dir="rtl">

- **Farrell & Lewandowsky (2018)، فصل 3.** برآورد پایه‌ی پارامتر: توابع ناهمخوانی، سطوح خطا، الگوریتم سیمپلکس و مسائل عملی مثل کمینه‌های محلی و مقادیر شروع. *(منبع اصلی.)*
- **قدوسیان (1401)**، *مبانی روش‌های مستقیم در بهینه‌سازی غیرخطی*: روش‌های جستجوی مستقیم برای بهینه‌سازی غیرخطی، از جمله روش‌های نوع سیمپلکس. برای دانشجویانی که نظریه‌ی پشت Nelder–Mead را می‌خواهند توصیه می‌شود [شماره‌ی فصل بررسی شود].
- **Verguts (2022)**: فصل بهینه‌سازی و گرادیان نزولی، مفید برای نگاه گرادیانی که در هفته‌ی 15 (مدل‌های یادگیری) برمی‌گردد [شماره‌ی فصل بررسی شود].

</div>

*Preview for Week 4:* instead of asking "which parameters minimize squared error?", we ask "which parameters make the observed data most probable?" This is maximum likelihood. It handles binomial data correctly, and it is the foundation for AIC/BIC (Week 7) and Bayesian inference (Weeks 9–13).

<div dir="rtl">

*پیش‌نمایش هفته‌ی 4:* به‌جای پرسیدن «کدام پارامترها مربع خطا را کمینه می‌کنند؟» می‌پرسیم «کدام پارامترها داده‌ی مشاهده‌شده را محتمل‌ترین می‌کنند؟» این بیشینه درست‌نمایی است. داده‌های دوجمله‌ای را درست مدیریت می‌کند و پایه‌ی AIC/BIC (هفته‌ی 7) و استنباط بیزی (هفته‌های 9–13) است.

</div>
