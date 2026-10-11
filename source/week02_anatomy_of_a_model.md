# Week 2: Anatomy of a Model: Signal Detection and Forgetting Curves · هفته‌ی 2: کالبدشکافی یک مدل: تشخیص علامت و منحنی‌های فراموشی

> **Chapter 1: Fundamentals of cognitive modeling** · Lecture 1 h · Lab 2 h
> **This week's running models:** equal-variance Gaussian signal detection theory (SDT); exponential and power forgetting curves. Both return in Weeks 3–13.

<div dir="rtl">

> **فصل 1: مبانی مدل‌سازی شناختی** · درس 1 ساعت · lab 2 ساعت
> **مدل‌های اصلی این هفته:** نظریه‌ی تشخیص علامت گاوسی با واریانس برابر (SDT)؛ منحنی‌های فراموشی نمایی و توانی. هر دو در هفته‌های 3 تا 13 دوباره می‌آیند.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| forgetting curve | منحنی فراموشی | کاهش یادآوری با گذشت زمان |
| signal detection theory (SDT) | نظریه‌ی تشخیص علامت | مدلی که حساسیت را از سوگیری پاسخ جدا می‌کند |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| deterministic core | هسته‌ی قطعی | بخش بدون تصادف مدل که پیش‌بینی میانگین را می‌دهد |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| linking assumption | فرض پیوند | اینکه کمیت‌های مدل چطور به رفتار قابل مشاهده وصل می‌شوند |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| hit | اصابت (hit) | پاسخ «بله» وقتی علامت وجود دارد |
| response bias | سوگیری پاسخ | تمایل به یک پاسخ، مستقل از محرک |
| binomial distribution | توزیع دوجمله‌ای | توزیع تعداد موفقیت در n کوشش |
| noise model | مدل نویز | توزیع داده حول پیش‌بینی مدل |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| ROC / zROC curve | منحنی ROC / zROC | نرخ hit در برابر نرخ false alarm با تغییر ملاک |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| criterion (c) | ملاک | آستانه‌ی تصمیم؛ نشان‌دهنده‌ی سوگیری پاسخ |
| formal model / formalize | مدل فرمال / فرمال کردن | نوشتن نظریه به شکل معادله یا الگوریتم |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| false alarm | هشدار کاذب (false alarm) | پاسخ «بله» وقتی علامت وجود ندارد |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| miss / correct rejection | از دست دادن / رد درست | پاسخ «نه» با وجود علامت / پاسخ «نه» بدون علامت |
| liberal / conservative | آسان‌گیر / محافظه‌کار | تمایل به گفتن «بله» / «نه» |
| free parameter | پارامتر آزاد | پارامتری که از روی داده برآورد می‌شود |
| verbal theory | نظریه‌ی کلامی | نظریه‌ای که فقط با کلمات بیان شده و پیش‌بینی دقیق نمی‌دهد |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Decompose** a cognitive model into its components: design, free and fixed parameters, deterministic core, noise (data) model, and linking assumptions.
2. **Compute** $d'$ and $c$ from a 2×2 table of counts, including a correction for hit or false-alarm rates of 0 or 1, and **explain** why $d'$ separates sensitivity from bias.
3. **Implement** exponential and power forgetting models with a binomial noise model, and **predict** qualitatively how each parameter changes the curves.
4. **Use** simulation and diagnostic plots (ROC/zROC, semi-log and log-log plots) to **evaluate** whether a model's qualitative signature appears in data.
5. **Interpret** fitted parameters in psychological terms and **identify** the limits of the "fit a straight line to transformed data" approach.

<div dir="rtl">

1. یک مدل شناختی را به اجزایش **تجزیه کنند**: طرح آزمایش، پارامترهای آزاد و ثابت، هسته‌ی قطعی، مدل نویز (داده)، و فرض‌های پیوند (linking assumptions).
2. $d'$ و $c$ را از یک جدول 2×2 شمارش‌ها **حساب کنند**، از جمله با تصحیح برای نرخ hit یا false alarm برابر 0 یا 1، و **توضیح دهند** چرا $d'$ حساسیت را از سوگیری جدا می‌کند.
3. مدل‌های فراموشی نمایی و توانی را با مدل نویز دوجمله‌ای **پیاده‌سازی کنند** و به‌طور کیفی **پیش‌بینی کنند** که هر پارامتر منحنی‌ها را چگونه تغییر می‌دهد.
4. با شبیه‌سازی و نمودارهای تشخیصی (ROC/zROC، نمودارهای نیمه‌لگاریتمی و لگاریتمی–لگاریتمی) **ارزیابی کنند** که آیا ردپای کیفی یک مدل در داده‌ها دیده می‌شود.
5. پارامترهای برازش‌شده را به زبان روان‌شناختی **تفسیر کنند** و محدودیت‌های روش «برازش خط راست روی داده‌ی تبدیل‌شده» را **شناسایی کنند**.

</div>

---

## Motivation & big picture · مقدمه

**Two radiologists.** Radiologist R1 flags 93% of scans that really contain a tumor, but also flags 31% of healthy scans. Radiologist R2 flags only 69% of tumors, but just 7% of healthy scans. Their percent correct is identical (81%). Who is the better diagnostician?

<div dir="rtl">

**دو رادیولوژیست.** رادیولوژیست R1 در 93% از تصویرهایی که واقعاً تومور دارند تومور گزارش می‌کند، ولی در 31% از تصویرهای سالم هم. رادیولوژیست R2 فقط 69% از تومورها را گزارش می‌کند، ولی فقط در 7% از تصویرهای سالم اشتباه می‌کند. درصد پاسخ درست هر دو یکسان است (81%). کدام تشخیص‌دهنده‌ی بهتری است؟

</div>

Percent correct cannot answer this, because it mixes two different things: **how well** a person can tell tumors from healthy tissue (*sensitivity*), and **how willing** they are to say "tumor" (*bias*). Signal detection theory is a small model with two parameters that pulls these apart. As the worked example will show, R1 and R2 have essentially the **same** sensitivity; they differ only in where they set their criterion. This is the first payoff of modeling: model parameters can **measure** latent constructs that raw scores conflate.

<div dir="rtl">

درصد پاسخ درست نمی‌تواند به این سؤال جواب دهد، چون دو چیز متفاوت را قاطی می‌کند: اینکه فرد **چقدر خوب** تومور را از بافت سالم تشخیص می‌دهد (*حساسیت*)، و اینکه **چقدر آمادگی** دارد بگوید «تومور هست» (*سوگیری*). نظریه‌ی تشخیص علامت یک مدل کوچک دوپارامتری است که این دو را از هم جدا می‌کند. همان‌طور که مثال حل‌شده نشان می‌دهد، R1 و R2 در واقع حساسیت **یکسانی** دارند؛ فقط ملاک‌شان را در جای متفاوتی گذاشته‌اند. این اولین ثمره‌ی مدل‌سازی است: پارامترهای مدل می‌توانند سازه‌های پنهانی را **اندازه بگیرند** که نمره‌های خام آن‌ها را قاطی می‌کنند.

</div>

**Ebbinghaus's curve.** Since Ebbinghaus's experiments on himself in the 1880s, we know that forgetting is fast at first and then slows down. "Fast, then slow" is a verbal description that both an **exponential** and a **power** function satisfy. Yet they imply different things: an exponential means a memory loses a *constant proportion* of its strength per day, at any age; a power function means older memories become *more resistant*. Choosing between them is a question about the nature of memory, and it requires a formal model.

<div dir="rtl">

**منحنی ابینگهاوس.** از زمان آزمایش‌هایی که ابینگهاوس در دهه‌ی 1880 روی خودش انجام داد می‌دانیم فراموشی اول سریع است و بعد کند می‌شود. «اول سریع، بعد کند» توصیفی کلامی است که هم تابع **نمایی** و هم تابع **توانی** با آن جور درمی‌آیند. ولی این دو معناهای متفاوتی دارند: نمایی یعنی یک خاطره در هر روز *نسبت ثابتی* از قدرتش را از دست می‌دهد، در هر سنی؛ توانی یعنی خاطره‌های قدیمی‌تر *مقاوم‌تر* می‌شوند. انتخاب بین این دو سؤالی درباره‌ی ماهیت حافظه است و به یک مدل فرمال نیاز دارد.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Medical diagnosis.** Radiologists, pathologists and screening programs are evaluated with SDT and ROC curves, so that a doctor who "sees better" can be told apart from a doctor who simply says "abnormal" more often.
- **Memory research.** In a recognition test, studied words are "signal" and new words are "noise". $d'$ measures memory strength separately from the tendency to say "old".
- **Eyewitness identification.** Police line-up procedures are compared with ROC analysis: some procedures do not improve accuracy, they only make witnesses more cautious.
- **Perception and hearing tests.** Thresholds for seeing or hearing faint stimuli are measured with SDT, so that a cautious listener is not mistaken for a hard-of-hearing one.
- **Machine learning.** Every binary classifier (spam filter, fraud detector, AI-text detector) has a hit rate and a false-alarm rate, and is evaluated with ROC curves and the area under the curve (AUC). This is the same theory.
- **Forgetting curves** are used to schedule learning: spaced-repetition apps (e.g. for vocabulary) decide when to show an item again from a model of how fast it is forgotten.

<div dir="rtl">

- **تشخیص پزشکی.** رادیولوژیست‌ها، پاتولوژیست‌ها و برنامه‌های غربالگری با SDT و منحنی ROC ارزیابی می‌شوند تا پزشکی که «بهتر می‌بیند» از پزشکی که فقط بیشتر می‌گوید «غیرطبیعی است» جدا شود.
- **پژوهش حافظه.** در آزمون بازشناسی، کلمه‌های مطالعه‌شده «علامت» و کلمه‌های جدید «نویز» هستند. $d'$ قدرت حافظه را جدا از تمایل به گفتن «قبلاً دیده‌ام» اندازه می‌گیرد.
- **شناسایی توسط شاهد عینی.** روش‌های مختلف صف شناسایی (line-up) در پلیس با تحلیل ROC مقایسه می‌شوند: بعضی روش‌ها دقت را بیشتر نمی‌کنند و فقط شاهد را محتاط‌تر می‌کنند.
- **آزمون‌های ادراک و شنوایی.** آستانه‌ی دیدن یا شنیدن محرک‌های ضعیف با SDT اندازه‌گیری می‌شود تا یک شنونده‌ی محتاط با کسی که کم‌شنواست اشتباه گرفته نشود.
- **یادگیری ماشین.** هر طبقه‌بند دودویی (فیلتر spam، آشکارساز تقلب، آشکارساز متن هوش مصنوعی) یک نرخ hit و یک نرخ false alarm دارد و با منحنی ROC و مساحت زیر آن (AUC) ارزیابی می‌شود. این همان نظریه است.
- **منحنی‌های فراموشی** برای زمان‌بندی یادگیری استفاده می‌شوند: اپلیکیشن‌های تکرار فاصله‌دار (مثلاً برای لغت) از روی مدلی از سرعت فراموشی تصمیم می‌گیرند کِی یک آیتم را دوباره نشان دهند.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

This week has one big idea: a model has **parts**, and each part is a separate assumption. We look at two small models. **Signal detection theory** explains yes/no decisions under uncertainty. Every trial gives the observer a noisy "feeling of signal". If the feeling is stronger than a personal threshold, the observer says "yes". Two numbers describe the observer: how far apart the "signal" and "no signal" feelings are on average (**sensitivity**, $d'$), and where the threshold is (**criterion**, $c$). Two people can have the same percent correct for completely different reasons, and SDT shows which. The **forgetting curve** describes how recall drops with time. Two formulas, exponential and power, both look like "fast drop, then slow", but they say different things about memory. Choosing between them is the kind of question the rest of the course teaches us to answer with data.

<div dir="rtl">

این هفته یک ایده‌ی اصلی دارد: هر مدل **اجزایی** دارد و هر جزء یک فرض جداست. دو مدل کوچک را می‌بینیم. **نظریه‌ی تشخیص علامت (SDT)** تصمیم‌های بله/نه در شرایط عدم قطعیت را توضیح می‌دهد. هر trial به مشاهده‌گر یک «حس وجود علامت» پرنویز می‌دهد. اگر این حس از یک آستانه‌ی شخصی قوی‌تر باشد، مشاهده‌گر می‌گوید «بله». دو عدد مشاهده‌گر را توصیف می‌کنند: حس «علامت هست» و «علامت نیست» به‌طور میانگین چقدر از هم فاصله دارند (**حساسیت**، $d'$)، و آستانه کجاست (**ملاک**، $c$). دو نفر می‌توانند درصد پاسخ درست یکسانی داشته باشند به دلایل کاملاً متفاوت، و SDT نشان می‌دهد کدام دلیل. **منحنی فراموشی** نشان می‌دهد یادآوری با گذشت زمان چطور کم می‌شود. دو فرمول، نمایی و توانی، هر دو شکل «اول سریع، بعد آهسته» دارند، ولی درباره‌ی حافظه حرف‌های متفاوتی می‌زنند. انتخاب بین آن‌ها از جنس سؤال‌هایی است که بقیه‌ی درس یاد می‌دهد با داده جواب دهیم.

</div>

#### Statistics words in plain language · واژه‌های آماری به زبان ساده

- **Distribution:** a description of which values a random quantity takes and how often. A histogram of many measurements approximates it.
- **Normal (Gaussian) distribution $\mathcal{N}(\mu, \sigma)$:** the bell curve, with mean $\mu$ (center) and standard deviation $\sigma$ (width). About 68% of values fall within $\mu \pm \sigma$ and 95% within $\mu \pm 1.96\sigma$.
- **Standard normal:** the normal distribution with $\mu = 0$, $\sigma = 1$. A value measured on this scale is called a **z-score**: "how many SDs above the mean".
- **$\Phi(x)$ (CDF):** the probability that a standard normal value is *below* $x$. $\Phi(0) = 0.5$, $\Phi(1) \approx 0.84$, $\Phi(1.96) \approx 0.975$. In Python: `norm.cdf(x)`.
- **$\Phi^{-1}(p)$ (inverse CDF, "z-transform"):** the opposite question: below which value lies a proportion $p$? $\Phi^{-1}(0.84) \approx 1$. In Python: `norm.ppf(p)`.
- **Binomial distribution $\mathrm{Binomial}(n, p)$:** the number of successes in $n$ independent tries, each with success probability $p$ (e.g. words recalled out of 50). Its mean is $np$ and its variance $np(1-p)$.
- **Proportion vs. probability:** a proportion is what we *observe* (30 of 50 recalled = 0.60); a probability is the model's *underlying* value that the proportion estimates.

<div dir="rtl">

- **توزیع (distribution):** توصیف اینکه یک کمیت تصادفی چه مقدارهایی می‌گیرد و هرکدام چقدر رایج است. هیستوگرام تعداد زیادی اندازه‌گیری تقریبی از آن است.
- **توزیع نرمال (گاوسی) $\mathcal{N}(\mu, \sigma)$:** منحنی زنگوله‌ای با میانگین $\mu$ (مرکز) و انحراف معیار $\sigma$ (پهنا). حدود 68% مقدارها در $\mu \pm \sigma$ و 95% در $\mu \pm 1.96\sigma$ قرار می‌گیرند.
- **نرمال استاندارد:** توزیع نرمال با $\mu = 0$ و $\sigma = 1$. مقداری که روی این مقیاس سنجیده شود **z-score** نام دارد: «چند انحراف معیار بالاتر از میانگین».
- **$\Phi(x)$ (تابع توزیع تجمعی یا CDF):** احتمال اینکه یک مقدار نرمال استاندارد *کمتر* از $x$ باشد. $\Phi(0) = 0.5$، $\Phi(1) \approx 0.84$، $\Phi(1.96) \approx 0.975$. در Python: `norm.cdf(x)`.
- **$\Phi^{-1}(p)$ (معکوس CDF، «تبدیل z»):** سؤال برعکس: نسبت $p$ از مقدارها زیر چه عددی هستند؟ $\Phi^{-1}(0.84) \approx 1$. در Python: `norm.ppf(p)`.
- **توزیع دوجمله‌ای $\mathrm{Binomial}(n, p)$:** تعداد موفقیت‌ها در $n$ تلاش مستقل که هرکدام با احتمال $p$ موفق است (مثلاً تعداد کلمه‌های به‌یادآمده از 50). میانگین آن $np$ و واریانس آن $np(1-p)$ است.
- **نسبت در برابر احتمال:** نسبت چیزی است که *مشاهده* می‌کنیم (30 از 50 = 0.60)؛ احتمال مقدار *زیربنایی* مدل است که نسبت آن را برآورد می‌کند.

</div>

**Suggested timing (60 min):** anatomy of a model 15 · SDT 20 · forgetting curves 15 · simulation as a thinking tool + preview 10.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** کالبدشکافی مدل 15 · SDT 20 · منحنی‌های فراموشی 15 · شبیه‌سازی به‌عنوان ابزار فکر کردن + پیش‌نمایش 10.

</div>

### 1. The anatomy of a model · 1. کالبدشکافی یک مدل

In Week 1 we wrote a model as a data-generating machine, $\mathbf{y} \sim p(\mathbf{y}\mid\boldsymbol\theta, \mathcal{M})$. In practice, almost every model you will meet in this course can be taken apart into five pieces:

<div dir="rtl">

در هفته‌ی 1 مدل را یک ماشین تولید داده نوشتیم، $\mathbf{y} \sim p(\mathbf{y}\mid\boldsymbol\theta, \mathcal{M})$. در عمل تقریباً هر مدلی که در این درس می‌بینید را می‌شود به پنج تکه تقسیم کرد:

</div>

| Component | Question | SDT | Forgetting (exponential) |
|---|---|---|---|
| **1. Design** $x_i$ | What is manipulated and measured? | Trial type (signal/noise); response yes/no | Retention interval $t_i$; number of items recalled out of $n$ |
| **2. Parameters** $\boldsymbol\theta$ | What is free to vary? What is fixed? | Free: $d'$, $c$. Fixed: both SDs = 1, noise mean = 0 | Free: $A$, $\lambda$. Fixed: $n$ |
| **3. Deterministic core** $f(x;\boldsymbol\theta)$ | What does the model predict on average? | $H = \Phi(d'/2 - c)$, $F = \Phi(-d'/2 - c)$ | $f(t) = A e^{-\lambda t}$ |
| **4. Noise model** | How do observations scatter around the prediction? | Hits $\sim \mathrm{Binomial}(n_s, H)$; false alarms $\sim \mathrm{Binomial}(n_n, F)$ | Recalled $\sim \mathrm{Binomial}(n, f(t))$ |
| **5. Linking assumptions** | How do model quantities map onto behavior? | "Yes" if internal evidence exceeds the criterion | Recall probability equals memory strength $f(t)$ |

<div dir="rtl">

| جزء | سؤال | SDT | فراموشی (نمایی) |
|---|---|---|---|
| **1. طرح آزمایش** $x_i$ | چه چیزی دست‌کاری و اندازه‌گیری می‌شود؟ | نوع trial (علامت/نویز)؛ پاسخ بله/نه | فاصله‌ی نگهداری $t_i$؛ تعداد آیتم‌های یادآوری‌شده از $n$ آیتم |
| **2. پارامترها** $\boldsymbol\theta$ | چه چیزی آزاد است؟ چه چیزی ثابت؟ | آزاد: $d'$، $c$. ثابت: هر دو انحراف معیار = 1، میانگین نویز = 0 | آزاد: $A$، $\lambda$. ثابت: $n$ |
| **3. هسته‌ی قطعی** $f(x;\boldsymbol\theta)$ | مدل به‌طور میانگین چه پیش‌بینی می‌کند؟ | $H = \Phi(d'/2 - c)$، $F = \Phi(-d'/2 - c)$ | $f(t) = A e^{-\lambda t}$ |
| **4. مدل نویز** | مشاهدات چگونه حول پیش‌بینی پراکنده می‌شوند؟ | hitها $\sim \mathrm{Binomial}(n_s, H)$؛ false alarmها $\sim \mathrm{Binomial}(n_n, F)$ | یادآوری‌شده‌ها $\sim \mathrm{Binomial}(n, f(t))$ |
| **5. فرض‌های پیوند** | کمیت‌های مدل چگونه به رفتار نگاشت می‌شوند؟ | اگر شواهد درونی از ملاک بیشتر باشد «بله» | احتمال یادآوری برابر قدرت حافظه $f(t)$ است |

</div>

Some points about each component:

<div dir="rtl">

چند نکته درباره‌ی هر جزء:

</div>

- **Free vs. fixed parameters.** Fixed parameters are not "unimportant". They are *assumptions*. In Week 1 we fixed $t_0 = 300$ ms. In SDT, fixing the noise mean at 0 and both standard deviations at 1 is what makes $d'$ and $c$ estimable at all: shifting or stretching the whole axis would not change any prediction. Such fixes are called **scaling constraints**.
- **Parameter ranges.** Every parameter has a meaningful range: $0 \le A \le 1$, $\lambda > 0$, $d' \ge 0$ for a non-perverse observer. Respecting these ranges matters when fitting (Week 3).
- **The noise model is part of the model.** Two researchers with the same $f(t)$ but different noise models (binomial vs. Gaussian) have *different* models and will get different parameter estimates (Week 4). The binomial is natural for counts: its variance $f(1-f)/n$ is largest at $f = 0.5$ and shrinks near 0 and 1.

<div dir="rtl">

- **پارامترهای آزاد در برابر ثابت.** پارامترهای ثابت «بی‌اهمیت» نیستند؛ آن‌ها *فرض* هستند. در هفته‌ی 1، $t_0 = 300$ ms را ثابت گرفتیم. در SDT، ثابت گرفتن میانگین نویز روی 0 و هر دو انحراف معیار روی 1 است که اصلاً برآورد $d'$ و $c$ را ممکن می‌کند: جابه‌جا کردن یا کشیدن کل محور هیچ پیش‌بینی‌ای را عوض نمی‌کند. به چنین ثابت‌هایی **قیدهای مقیاس** (scaling constraints) می‌گویند.
- **دامنه‌ی پارامترها.** هر پارامتر دامنه‌ی معناداری دارد: $0 \le A \le 1$، $\lambda > 0$، و برای مشاهده‌گری که برعکس پاسخ نمی‌دهد $d' \ge 0$. رعایت این دامنه‌ها در برازش مهم است (هفته‌ی 3).
- **مدل نویز جزئی از مدل است.** دو پژوهشگر با $f(t)$ یکسان ولی مدل نویز متفاوت (دوجمله‌ای در برابر گاوسی) مدل‌های *متفاوتی* دارند و برآوردهای پارامتر متفاوتی می‌گیرند (هفته‌ی 4). توزیع دوجمله‌ای برای شمارش‌ها طبیعی است: واریانسش $f(1-f)/n$ در $f = 0.5$ بیشینه است و نزدیک 0 و 1 کم می‌شود.

</div>

### 2. Signal detection theory (SDT) · 2. نظریه‌ی تشخیص علامت (SDT)

**The task.** On each trial a stimulus is either *signal* (e.g., a tumor, a studied word, a faint tone) or *noise*. The observer answers "yes" (signal) or "no". The outcomes form a 2×2 table:

<div dir="rtl">

**تکلیف آزمایشی.** در هر trial محرک یا *علامت* است (مثلاً یک تومور، یک کلمه‌ی مطالعه‌شده، یک صدای ضعیف) یا *نویز*. مشاهده‌گر پاسخ «بله» (علامت) یا «نه» می‌دهد. نتیجه‌ها یک جدول 2×2 می‌سازند:

</div>

| | Respond "yes" | Respond "no" |
|---|---|---|
| **Signal trial** | Hit | Miss |
| **Noise trial** | False alarm (FA) | Correct rejection (CR) |

<div dir="rtl">

| | پاسخ «بله» | پاسخ «نه» |
|---|---|---|
| **trial علامت** | hit | از دست دادن (miss) |
| **trial نویز** | false alarm (FA) | رد درست (correct rejection، CR) |

</div>

with hit rate $H = \frac{\text{hits}}{\text{hits} + \text{misses}}$ and false-alarm rate $F = \frac{\text{FAs}}{\text{FAs} + \text{CRs}}$.

<div dir="rtl">

با نرخ hit $H = \frac{\text{hits}}{\text{hits} + \text{misses}}$ و نرخ false alarm $F = \frac{\text{FAs}}{\text{FAs} + \text{CRs}}$.

</div>

**The model (intuition).** Each trial produces an internal **evidence** value. It is noisy: even pure noise trials sometimes feel signal-like. Signal trials produce, on average, more evidence. The observer says "yes" whenever the evidence exceeds a **criterion**.

<div dir="rtl">

**مدل (شهودی).** هر trial یک مقدار **شواهد** درونی تولید می‌کند. این مقدار پرنویز است: حتی trialهای نویز خالص هم گاهی شبیه علامت به نظر می‌رسند. trialهای علامت به‌طور میانگین شواهد بیشتری تولید می‌کنند. مشاهده‌گر هر وقت شواهد از یک **ملاک** (criterion) بیشتر باشد می‌گوید «بله».

</div>

**The model (formal), equal-variance Gaussian SDT:**

<div dir="rtl">

**مدل (فرمال)، SDT گاوسی با واریانس برابر:**

</div>

$$
\text{noise trials: } X \sim \mathcal{N}(0, 1), \qquad
\text{signal trials: } X \sim \mathcal{N}(d', 1), \qquad
\text{respond "yes" iff } X > k.
$$

- $d'$ is **sensitivity**: the distance between the two distributions in SD units.
- $k$ is the absolute criterion location. It is more convenient to measure the criterion relative to the midpoint between the distributions: $c = k - d'/2$. With $c = 0$ the observer is unbiased, $c < 0$ is **liberal** (says "yes" readily), and $c > 0$ is **conservative**.

<div dir="rtl">

- $d'$ **حساسیت** است: فاصله‌ی دو توزیع بر حسب واحد انحراف معیار.
- $k$ محل مطلق ملاک است. راحت‌تر است ملاک را نسبت به نقطه‌ی میانی دو توزیع بسنجیم: $c = k - d'/2$. با $c = 0$ مشاهده‌گر بی‌سوگیری است، $c < 0$ یعنی **liberal** (راحت «بله» می‌گوید)، و $c > 0$ یعنی **محافظه‌کار (conservative)**.

</div>

**Predictions.** Using the standard normal CDF $\Phi$:

<div dir="rtl">

**پیش‌بینی‌ها.** با استفاده از CDF نرمال استاندارد $\Phi$:

</div>

$$
H = P(X > k \mid \text{signal}) = \Phi\!\left(\tfrac{d'}{2} - c\right), \qquad
F = P(X > k \mid \text{noise}) = \Phi\!\left(-\tfrac{d'}{2} - c\right).
$$

**Inverting the model.** Applying $\Phi^{-1}$ (often written $z$) to both equations and solving gives the familiar formulas:

<div dir="rtl">

**معکوس کردن مدل.** با اعمال $\Phi^{-1}$ (که اغلب $z$ نوشته می‌شود) روی هر دو معادله و حل آن‌ها، فرمول‌های آشنا به دست می‌آیند:

</div>

$$
d' = \Phi^{-1}(H) - \Phi^{-1}(F), \qquad
c = -\tfrac{1}{2}\left[\Phi^{-1}(H) + \Phi^{-1}(F)\right].
$$

Notice what just happened: this is our first **parameter estimation**. There are two free parameters and two data points ($H$, $F$), so the model can be solved exactly. With more data points than parameters, an exact solution usually does not exist and we need the fitting methods of Weeks 3–4.

<div dir="rtl">

دقت کنید چه اتفاقی افتاد: این اولین **برآورد پارامتر** ماست. دو پارامتر آزاد و دو داده ($H$، $F$) داریم، پس مدل را می‌شود دقیقاً حل کرد. وقتی تعداد داده‌ها از تعداد پارامترها بیشتر باشد، معمولاً جواب دقیق وجود ندارد و به روش‌های برازش هفته‌های 3–4 نیاز داریم.

</div>

**The extreme-rate problem.** If $H = 1$ or $F = 0$, then $\Phi^{-1}$ is $\pm\infty$ and $d'$ is infinite. This happens often with few trials. A standard fix is the **log-linear correction**: add 0.5 to every cell count before computing the rates (i.e., add 0.5 to hits and FAs and 1 to the number of trials of each type). We use it by default in the lab.

<div dir="rtl">

**مشکل نرخ‌های حدی.** اگر $H = 1$ یا $F = 0$ باشد، $\Phi^{-1}$ برابر $\pm\infty$ و $d'$ بی‌نهایت می‌شود. با تعداد trial کم این اتفاق زیاد می‌افتد. راه‌حل استاندارد **تصحیح log-linear** است: پیش از محاسبه‌ی نرخ‌ها به هر خانه‌ی جدول 0.5 اضافه کنید (یعنی 0.5 به hitها و false alarmها و 1 به تعداد trialهای هر نوع). در lab به‌طور پیش‌فرض از آن استفاده می‌کنیم.

</div>

**The ROC curve: SDT's signature.** Hold $d'$ fixed and let $c$ vary. The pair $(F, H)$ traces a curve, the **receiver operating characteristic (ROC)**. Every point on one ROC has the same sensitivity but a different bias. Plotting $\Phi^{-1}(H)$ against $\Phi^{-1}(F)$ gives the **zROC**, which under equal-variance SDT is a straight line:

<div dir="rtl">

**منحنی ROC: نشانه‌ی اصلی SDT.** $d'$ را ثابت نگه دارید و بگذارید $c$ تغییر کند. جفت $(F, H)$ یک منحنی رسم می‌کند به نام **منحنی مشخصه‌ی عملکرد گیرنده (ROC)**. همه‌ی نقاط یک ROC حساسیت یکسان ولی سوگیری متفاوت دارند. رسم $\Phi^{-1}(H)$ در برابر $\Phi^{-1}(F)$ منحنی **zROC** را می‌دهد که در SDT با واریانس برابر یک خط راست است:

</div>

$$
\Phi^{-1}(H) = d' + 1 \cdot \Phi^{-1}(F).
$$

So the model makes a *testable* prediction: **the zROC is linear with slope 1**. ROCs can be measured with confidence ratings (each confidence level acts as a separate criterion). In recognition memory, zROC slopes are typically *below* 1, which motivates the unequal-variance model below.

<div dir="rtl">

پس مدل یک پیش‌بینی *قابل آزمون* دارد: **zROC خطی با شیب 1 است**. ROC را می‌شود با درجه‌بندی اطمینان (confidence ratings) اندازه گرفت (هر سطح اطمینان مثل یک ملاک جداگانه عمل می‌کند). در حافظه‌ی بازشناسی، شیب zROC معمولاً *کمتر* از 1 است و همین انگیزه‌ی مدل با واریانس نابرابر در ادامه است.

</div>

> **Advanced: unequal-variance SDT.** If signal trials have $X \sim \mathcal{N}(\mu_s, \sigma_s)$, the zROC is still linear but its slope is $1/\sigma_s$. In that case, $d'$ computed from a single $(H, F)$ pair *changes with the criterion*, so it is no longer a pure sensitivity measure. A common alternative index is $d_a = \mu_s \sqrt{2/(1+\sigma_s^2)}$. Estimating $\sigma_s$ requires more than one criterion, i.e., rating data. You will see this effect directly in lab Part B.

<div dir="rtl">

> **پیشرفته: SDT با واریانس نابرابر.** اگر در trialهای علامت $X \sim \mathcal{N}(\mu_s, \sigma_s)$ باشد، zROC هنوز خطی است ولی شیبش $1/\sigma_s$ است. در این حالت $d'$ که از یک جفت $(H, F)$ حساب می‌شود *با ملاک تغییر می‌کند*، پس دیگر یک معیار خالص حساسیت نیست. یک شاخص جایگزین رایج $d_a = \mu_s \sqrt{2/(1+\sigma_s^2)}$ است. برآورد $\sigma_s$ به بیش از یک ملاک، یعنی داده‌ی درجه‌بندی، نیاز دارد. این اثر را مستقیماً در بخش B lab می‌بینید.

</div>

#### Reading the math · خواندن ریاضی

**The two bell curves.** Draw two normal curves on one axis: the "noise" curve centered at 0 and the "signal" curve centered at $d'$. Both have width 1. Draw a vertical line at the criterion $k$. Everything to the right of the line is a "yes".

- $H$ = area of the **signal** curve to the right of the line. $F$ = area of the **noise** curve to the right of the line.
- Why $H = \Phi(d'/2 - c)$? The criterion sits at $k = d'/2 + c$ (the midpoint plus $c$). The signal curve is centered at $d'$, so the line is $k - d' = c - d'/2$ SDs from its center. The area to the right of that point is $1 - \Phi(c - d'/2) = \Phi(d'/2 - c)$, because the normal curve is symmetric.
- **Numerical example.** $d' = 2$, $c = 0$: $H = \Phi(1) = 0.84$ and $F = \Phi(-1) = 0.16$. Now make the observer liberal, $c = -0.5$: $H = \Phi(1.5) = 0.93$, $F = \Phi(-0.5) = 0.31$. Both rates went up, sensitivity is unchanged. This is radiologist R1 of the worked example.

**Inverting.** $d' = \Phi^{-1}(H) - \Phi^{-1}(F)$: convert each rate into a z-score and subtract. For R1: $1.476 - (-0.496) = 1.97$. $c$ is minus the average of the two z-scores: if both rates are high (both z-scores positive), $c$ is negative, i.e. liberal.

**The zROC line.** $\Phi^{-1}(H) = d' + \Phi^{-1}(F)$ is just the previous equation rearranged. In z-units, moving the criterion moves both z-scores by the same amount, so the points lie on a line with slope 1 and intercept $d'$.

<div dir="rtl">

**دو منحنی زنگوله‌ای.** دو منحنی نرمال را روی یک محور بکشید: منحنی «نویز» با مرکز 0 و منحنی «علامت» با مرکز $d'$. پهنای هر دو 1 است. یک خط عمودی در محل ملاک $k$ بکشید. هر چیزی سمت راست خط یعنی «بله».

- $H$ = مساحت منحنی **علامت** در سمت راست خط. $F$ = مساحت منحنی **نویز** در سمت راست خط.
- چرا $H = \Phi(d'/2 - c)$؟ ملاک در $k = d'/2 + c$ است (نقطه‌ی وسط به‌علاوه‌ی $c$). مرکز منحنی علامت $d'$ است، پس خط به اندازه‌ی $k - d' = c - d'/2$ انحراف معیار از مرکز آن فاصله دارد. مساحت سمت راست این نقطه $1 - \Phi(c - d'/2) = \Phi(d'/2 - c)$ است، چون منحنی نرمال متقارن است.
- **مثال عددی.** $d' = 2$ و $c = 0$: $H = \Phi(1) = 0.84$ و $F = \Phi(-1) = 0.16$. حالا مشاهده‌گر را آسان‌گیر (liberal) کنید، $c = -0.5$: $H = \Phi(1.5) = 0.93$ و $F = \Phi(-0.5) = 0.31$. هر دو نرخ بالا رفتند و حساسیت تغییر نکرد. این همان رادیولوژیست R1 در مثال حل‌شده است.

**معکوس کردن.** $d' = \Phi^{-1}(H) - \Phi^{-1}(F)$: هر نرخ را به z-score تبدیل کنید و از هم کم کنید. برای R1: $1.476 - (-0.496) = 1.97$. $c$ منفیِ میانگین دو z-score است: اگر هر دو نرخ بالا باشند (هر دو z-score مثبت)، $c$ منفی است، یعنی آسان‌گیر.

**خط zROC.** $\Phi^{-1}(H) = d' + \Phi^{-1}(F)$ همان معادله‌ی قبلی است که مرتب شده. در واحد z، جابه‌جا کردن ملاک هر دو z-score را به یک اندازه تغییر می‌دهد، پس نقطه‌ها روی خطی با شیب 1 و عرض از مبدأ $d'$ قرار می‌گیرند.

</div>

#### For an engineer · برای یک مهندس

SDT *is* the detection theory of radar and communications, imported into psychology in the 1950s.

| Psychology | Telecom / radar |
|---|---|
| noise trial / signal trial | hypothesis $H_0$ (noise only) / $H_1$ (signal + noise) |
| internal evidence $X$ | test statistic, e.g. matched-filter output |
| criterion $k$ (or $c$) | detection threshold |
| hit rate $H$ | probability of detection $P_D$ |
| false-alarm rate $F$ | probability of false alarm $P_{FA}$ |
| sensitivity $d'$ | deflection $(\mu_1 - \mu_0)/\sigma$; $d'^2$ plays the role of an SNR |
| ROC curve | receiver operating characteristic (same name, same plot) |
| liberal / conservative observer | low / high threshold (high / low $P_{FA}$) |

Differences in emphasis: an engineer usually *chooses* the threshold (e.g. Neyman–Pearson: fix $P_{FA}$, maximize $P_D$). A psychologist *observes* a person's $P_D$ and $P_{FA}$ and *infers* both the SNR ($d'$) and the threshold ($c$) the person used. The criterion $c$ is measured from the midpoint between the two means, so $c = 0$ means "no bias". The **optimal** threshold depends on prior probabilities and costs exactly as in Bayesian detection, and people often move their criterion in the right direction when payoffs change (Week 4).

<div dir="rtl">

SDT *همان* نظریه‌ی آشکارسازی رادار و مخابرات است که در دهه‌ی 1950 وارد روان‌شناسی شد.

| روان‌شناسی | مخابرات / رادار |
|---|---|
| trial نویز / trial علامت | فرضیه‌ی $H_0$ (فقط نویز) / $H_1$ (سیگنال + نویز) |
| شواهد درونی $X$ | آماره‌ی آزمون، مثلاً خروجی فیلتر منطبق (matched filter) |
| ملاک $k$ (یا $c$) | آستانه‌ی آشکارسازی |
| نرخ hit یعنی $H$ | احتمال آشکارسازی $P_D$ |
| نرخ false alarm یعنی $F$ | احتمال هشدار کاذب $P_{FA}$ |
| حساسیت $d'$ | انحراف (deflection) $(\mu_1 - \mu_0)/\sigma$؛ $d'^2$ نقش SNR را دارد |
| منحنی ROC | receiver operating characteristic (همان نام، همان نمودار) |
| مشاهده‌گر آسان‌گیر / محافظه‌کار | آستانه‌ی پایین / بالا ($P_{FA}$ بالا / پایین) |

تفاوت در تأکید: مهندس معمولاً آستانه را *انتخاب* می‌کند (مثلاً Neyman–Pearson: $P_{FA}$ را ثابت کن و $P_D$ را بیشینه کن). روان‌شناس $P_D$ و $P_{FA}$ یک آدم را *مشاهده* می‌کند و هم SNR ($d'$) و هم آستانه‌ای ($c$) را که آن فرد به کار برده *استنباط* می‌کند. ملاک $c$ از نقطه‌ی وسط دو میانگین سنجیده می‌شود، پس $c = 0$ یعنی «بدون سوگیری». آستانه‌ی **بهینه** دقیقاً مثل آشکارسازی بیزی به احتمال‌های پیشین و هزینه‌ها بستگی دارد، و آدم‌ها وقتی پاداش‌ها تغییر می‌کنند معمولاً ملاکشان را در جهت درست جابه‌جا می‌کنند (هفته‌ی 4).

</div>

### 3. Forgetting curves · 3. منحنی‌های فراموشی

**Data.** At each retention interval $t_i$ (e.g., in days), the participant is tested on $n$ items and recalls $y_i$ of them.

<div dir="rtl">

**داده.** در هر فاصله‌ی نگهداری $t_i$ (مثلاً به روز)، شرکت‌کننده با $n$ آیتم آزمون می‌شود و $y_i$ تا را به یاد می‌آورد.

</div>

**Two candidate deterministic cores:**

<div dir="rtl">

**دو هسته‌ی قطعی رقیب:**

</div>

| | Exponential | Power |
|---|---|---|
| Equation | $f(t) = A\,e^{-\lambda t}$ | $f(t) = A\,(1 + t)^{-d}$ |
| Parameters | $A$: initial level; $\lambda$: decay rate | $A$: initial level; $d$: decay exponent |
| Linearizing plot | $\ln f$ vs. $t$ is a straight line with slope $-\lambda$ | $\ln f$ vs. $\ln(1+t)$ is a straight line with slope $-d$ |
| Relative loss rate $-f'(t)/f(t)$ | $\lambda$ (constant) | $d/(1+t)$ (decreasing with age) |
| Psychological reading | A memory loses the same *proportion* of its strength per unit time, whatever its age | Older memories lose strength more slowly; they become more resistant |

<div dir="rtl">

| | نمایی | توانی |
|---|---|---|
| معادله | $f(t) = A\,e^{-\lambda t}$ | $f(t) = A\,(1 + t)^{-d}$ |
| پارامترها | $A$: سطح اولیه؛ $\lambda$: نرخ زوال | $A$: سطح اولیه؛ $d$: نمای زوال |
| نمودار خطی‌کننده | $\ln f$ در برابر $t$ خطی راست با شیب $-\lambda$ است | $\ln f$ در برابر $\ln(1+t)$ خطی راست با شیب $-d$ است |
| نرخ نسبی فراموشی $-f'(t)/f(t)$ | $\lambda$ (ثابت) | $d/(1+t)$ (با گذشت زمان کاهشی) |
| خوانش روان‌شناختی | خاطره در هر واحد زمان *نسبت* یکسانی از قدرتش را از دست می‌دهد، هر سنی که داشته باشد | خاطره‌های قدیمی‌تر کندتر قدرت از دست می‌دهند؛ مقاوم‌تر می‌شوند |

</div>

The **relative loss rate** (in survival analysis, the *hazard*) is the key interpretive difference. It is why the choice between the two functions is a theoretical question, not a curve-fitting detail.

<div dir="rtl">

**نرخ نسبی فراموشی** (که در تحلیل بقا به آن *hazard* می‌گویند) تفاوت کلیدی در تفسیر است. به همین دلیل انتخاب بین این دو تابع یک سؤال نظری است، نه یک جزئیات منحنی‌برازی.

</div>

**Noise model.** Recall counts are binomial:

<div dir="rtl">

**مدل نویز.** تعداد یادآوری‌ها دوجمله‌ای است:

</div>

$$
y_i \sim \mathrm{Binomial}\big(n, f(t_i; \boldsymbol\theta)\big).
$$

With $n = 50$ items and $f = 0.5$, the SD of the observed proportion is $\sqrt{0.5 \cdot 0.5 / 50} \approx 0.07$. That is large compared with the differences between models over short intervals, which is a first hint that **design** (which intervals, how many items) determines whether data can discriminate between models.

<div dir="rtl">

با $n = 50$ آیتم و $f = 0.5$، انحراف معیار نسبت مشاهده‌شده $\sqrt{0.5 \cdot 0.5 / 50} \approx 0.07$ است. این در مقایسه با تفاوت مدل‌ها در فاصله‌های کوتاه بزرگ است؛ اولین نشانه‌ی اینکه **طرح آزمایش** (کدام فاصله‌ها، چند آیتم) تعیین می‌کند داده‌ها می‌توانند بین مدل‌ها تمایز بگذارند یا نه.

</div>

> **Advanced: the "+1" in the power model is not innocent.** $A\,t^{-d}$ is infinite at $t = 0$, so a shift is added. But $(1 + t)$ depends on the **unit** of $t$: measuring in hours instead of days changes the shape of the curve, not just the scale of the axis. Some authors therefore write $A\,(1 + bt)^{-d}$ with a free scale parameter $b$, which adds a third parameter and raises the model comparison questions of Weeks 6–7. Keep the unit fixed (days) throughout this course.

<div dir="rtl">

> **پیشرفته: «+1» در مدل توانی بی‌خطر نیست.** $A\,t^{-d}$ در $t = 0$ بی‌نهایت است، پس یک جابه‌جایی اضافه می‌شود. ولی $(1 + t)$ به **واحد** $t$ بستگی دارد: اندازه‌گیری به ساعت به‌جای روز، شکل منحنی را عوض می‌کند، نه فقط مقیاس محور را. به همین دلیل بعضی نویسندگان $A\,(1 + bt)^{-d}$ را با پارامتر مقیاس آزاد $b$ می‌نویسند؛ این یک پارامتر سوم اضافه می‌کند و سؤال‌های مقایسه‌ی مدل هفته‌های 6–7 را پیش می‌آورد. در طول این درس واحد را ثابت (روز) نگه دارید.

</div>

#### Reading the math · خواندن ریاضی

- $f(t) = A e^{-\lambda t}$: $A$ is the recall level right after study ($t = 0$), and $\lambda$ says how fast it falls. With $\lambda = 0.1$ per day, recall is multiplied by $e^{-0.1} \approx 0.905$ every day: about 9.5% of what is left is lost each day, on day 1 and on day 100 alike.
- $f(t) = A(1+t)^{-d}$: going from day 0 to day 1 multiplies recall by $2^{-d}$; going from day 9 to day 10 multiplies it only by $(10/11)^{d}$, close to 1. Old memories hardly change any more.
- **Relative loss rate** $-f'(t)/f(t)$: "what fraction of the remaining memory is lost per day *right now*". Constant ($\lambda$) for the exponential, shrinking ($d/(1+t)$) for the power function. This single number is the psychological difference between the models.
- $y_i \sim \mathrm{Binomial}(n, f(t_i))$: at delay $t_i$ the participant recalls $y_i$ of $n$ items, and each item is recalled with probability $f(t_i)$. The observed proportion $y_i/n$ scatters around $f(t_i)$ with SD $\sqrt{f(1-f)/n}$, about 0.07 for $n = 50$.

<div dir="rtl">

- $f(t) = A e^{-\lambda t}$: $A$ میزان یادآوری درست بعد از مطالعه ($t = 0$) است و $\lambda$ می‌گوید با چه سرعتی کم می‌شود. با $\lambda = 0.1$ در روز، یادآوری هر روز در $e^{-0.1} \approx 0.905$ ضرب می‌شود: هر روز حدود 9.5% از آنچه مانده از دست می‌رود، چه روز اول و چه روز صدم.
- $f(t) = A(1+t)^{-d}$: رفتن از روز 0 به روز 1 یادآوری را در $2^{-d}$ ضرب می‌کند؛ رفتن از روز 9 به روز 10 فقط در $(10/11)^{d}$ که نزدیک 1 است. خاطره‌های قدیمی دیگر تقریباً تغییر نمی‌کنند.
- **نرخ نسبی فراموشی** $-f'(t)/f(t)$: «چه کسری از حافظه‌ی باقی‌مانده *همین الان* در هر روز از دست می‌رود». برای تابع نمایی ثابت است ($\lambda$) و برای تابع توانی کم می‌شود ($d/(1+t)$). همین یک عدد، تفاوت روان‌شناختی دو مدل است.
- $y_i \sim \mathrm{Binomial}(n, f(t_i))$: در تأخیر $t_i$، شرکت‌کننده $y_i$ آیتم از $n$ آیتم را به یاد می‌آورد و هر آیتم با احتمال $f(t_i)$ به یاد آورده می‌شود. نسبت مشاهده‌شده‌ی $y_i/n$ با انحراف معیار $\sqrt{f(1-f)/n}$ حول $f(t_i)$ پراکنده است؛ برای $n = 50$ حدود 0.07.

</div>

#### For an engineer · برای یک مهندس

- The **exponential** curve is the step response of a first-order system (an RC circuit discharging): one time constant $\tau = 1/\lambda$. A constant relative loss rate is the "memoryless" property you know from exponential lifetimes in reliability theory.
- The **power** curve has no single time constant. A useful picture: a sum of many exponentials with *different* time constants (fast and slow components) looks like a power law. Week 5 shows this exactly, and it is one candidate explanation of power-law forgetting.
- On a **log–log** plot a power law is a straight line; on a **semi-log** plot an exponential is a straight line. Engineers use the same trick to identify system orders and $1/f$ noise.
- The binomial noise model is the counting statistics of a detector: like counting bit errors out of $n$ bits, the uncertainty of a proportion shrinks with $1/\sqrt{n}$.

<div dir="rtl">

- منحنی **نمایی** همان پاسخ پله‌ی یک سیستم مرتبه‌ی اول است (دشارژ یک مدار RC): یک ثابت زمانی $\tau = 1/\lambda$. ثابت بودن نرخ نسبی فراموشی همان ویژگی «بی‌حافظگی» است که از طول عمر نمایی در نظریه‌ی قابلیت اطمینان می‌شناسید.
- منحنی **توانی** یک ثابت زمانی واحد ندارد. تصویر مفید: جمع تعداد زیادی منحنی نمایی با ثابت‌های زمانی *متفاوت* (مؤلفه‌های سریع و کند) شبیه یک قانون توانی می‌شود. هفته‌ی 5 این را دقیقاً نشان می‌دهد و این یکی از توضیح‌های ممکن برای فراموشی توانی است.
- روی نمودار **لگاریتمی–لگاریتمی** قانون توانی یک خط راست است؛ روی نمودار **نیمه‌لگاریتمی** تابع نمایی خط راست است. مهندس‌ها از همین ترفند برای تشخیص مرتبه‌ی سیستم و نویز $1/f$ استفاده می‌کنند.
- مدل نویز دوجمله‌ای همان آمار شمارش یک آشکارساز است: مثل شمردن خطاهای بیتی از $n$ بیت، عدم قطعیت یک نسبت با $1/\sqrt{n}$ کم می‌شود.

</div>

### 4. Simulation as a thinking tool · 4. شبیه‌سازی به‌عنوان ابزار فکر کردن

Before fitting anything, simulate. Simulation answers questions such as:

<div dir="rtl">

پیش از برازش هر چیزی، شبیه‌سازی کنید. شبیه‌سازی به سؤال‌هایی مثل این‌ها جواب می‌دهد:

</div>

- **What can the model produce, and what can it *not* produce?** Equal-variance SDT with $d' > 0$ can never produce $H < F$, and it can never produce a zROC slope different from 1. Both exponential and power curves are always decreasing, so they cannot capture *reminiscence* (recall improving over time). The set of things a model **cannot** do is what makes it testable.
- **Which parameters matter where?** $A$ moves the whole forgetting curve; $\lambda$ or $d$ controls the shape.
- **Can the design discriminate between models?** If two models make nearly identical predictions at the intervals we plan to test, no fitting method can tell them apart (lab Exercise 4; Assignment A1).

<div dir="rtl">

- **مدل چه چیزی را می‌تواند تولید کند، و چه چیزی را *نمی‌تواند*؟** SDT با واریانس برابر و $d' > 0$ هرگز نمی‌تواند $H < F$ تولید کند، و هرگز شیب zROC غیر از 1 نمی‌دهد. منحنی‌های نمایی و توانی هر دو همیشه نزولی‌اند، پس نمی‌توانند *بازیادآوری* (reminiscence، بهتر شدن یادآوری با گذشت زمان) را نشان دهند. مجموعه‌ی کارهایی که یک مدل **نمی‌تواند** انجام دهد همان چیزی است که آن را قابل آزمون می‌کند.
- **کدام پارامتر کجا اهمیت دارد؟** $A$ کل منحنی فراموشی را جابه‌جا می‌کند؛ $\lambda$ یا $d$ شکل را کنترل می‌کند.
- **آیا طرح آزمایش می‌تواند بین مدل‌ها تمایز بگذارد؟** اگر دو مدل در فاصله‌هایی که می‌خواهیم آزمون کنیم پیش‌بینی‌های تقریباً یکسانی بدهند، هیچ روش برازشی نمی‌تواند آن‌ها را از هم جدا کند (تمرین 4 lab؛ تکلیف A1).

</div>

### 5. Preview: estimation by linearization, and why it is not enough · 5. پیش‌نمایش: برآورد با خطی‌سازی، و چرا کافی نیست

A traditional way to fit forgetting curves is to log-transform the observed proportions and fit a straight line by ordinary regression. It is fast and intuitive, and we try it in the lab. It has three problems that motivate Weeks 3–4:

<div dir="rtl">

یک روش سنتی برای برازش منحنی فراموشی این است که از نسبت‌های مشاهده‌شده لگاریتم بگیریم و با رگرسیون معمولی یک خط راست برازش کنیم. سریع و شهودی است و در lab امتحانش می‌کنیم. سه مشکل دارد که انگیزه‌ی هفته‌های 3–4 است:

</div>

1. $\ln(0)$ is undefined, so an interval with zero recalls breaks the method.
2. The log transform distorts the noise: the scatter of $\ln \hat p$ is much larger for small proportions, but regression treats all points as equally reliable.
3. The line is fit on the log scale, but we care about errors on the original (proportion) scale.

<div dir="rtl">

1. $\ln(0)$ تعریف‌نشده است، پس فاصله‌ای با یادآوری صفر روش را از کار می‌اندازد.
2. تبدیل لگاریتمی نویز را تحریف می‌کند: پراکندگی $\ln \hat p$ برای نسبت‌های کوچک خیلی بیشتر است، ولی رگرسیون با همه‌ی نقاط مثل هم رفتار می‌کند.
3. خط روی مقیاس لگاریتمی برازش می‌شود، ولی ما به خطا روی مقیاس اصلی (نسبت) اهمیت می‌دهیم.

</div>

The principled alternative is to fit the model directly to the untransformed data, by minimizing squared error (Week 3) or maximizing the binomial likelihood (Week 4).

<div dir="rtl">

جایگزین اصولی این است که مدل را مستقیماً روی داده‌ی تبدیل‌نشده برازش کنیم: با کمینه کردن مربع خطا (هفته‌ی 3) یا بیشینه کردن درست‌نمایی دوجمله‌ای (هفته‌ی 4).

</div>

#### For the instructor · برای مدرس

- **Open with the radiologist puzzle** (Motivation) and let students vote on who is better before showing any math. Most will pick by percent correct, then realize it is identical.
- **Draw, don't derive.** The two overlapping bell curves with a movable vertical line explain $H$, $F$, $d'$ and $c$ better than any formula. Move the line left and right on the board and ask what happens to $H$ and $F$; then pull the curves apart and ask again.
- **Use $\Phi$ tables or Python live.** Compute R1's $d'$ with `norm.ppf` in front of the class. Students who are new to statistics need to see that $\Phi^{-1}$ is "just a lookup".
- **Connect to something they know:** a COVID or pregnancy test has a hit rate (sensitivity) and a false-alarm rate (1 − specificity). Medical "sensitivity" is the hit rate, *not* $d'$: point out this naming clash.
- **Typical questions.**
  - *"Why assume normal distributions?"* It is a convenient and often adequate assumption; the zROC test (slope 1) checks it, and the unequal-variance model relaxes it.
  - *"Is a liberal criterion bad?"* No: the best criterion depends on costs and base rates.
  - *"Exponential or power, which is right?"* For many datasets the power function fits better, but averaging over people can create a power shape (Week 5). Keep the question open.

<div dir="rtl">

- **با معمای رادیولوژیست‌ها شروع کنید** (بخش مقدمه) و پیش از نشان دادن هر فرمولی، بگذارید دانشجوها رأی بدهند کدام بهتر است. بیشترشان بر اساس درصد پاسخ درست انتخاب می‌کنند و بعد می‌فهمند که دو عدد یکسان است.
- **رسم کنید، اثبات نکنید.** دو منحنی زنگوله‌ای هم‌پوشان با یک خط عمودی متحرک، $H$، $F$، $d'$ و $c$ را بهتر از هر فرمولی توضیح می‌دهند. خط را روی تخته به چپ و راست ببرید و بپرسید $H$ و $F$ چه می‌شوند؛ بعد منحنی‌ها را از هم دور کنید و دوباره بپرسید.
- **از جدول $\Phi$ یا Python به‌طور زنده استفاده کنید.** $d'$ رادیولوژیست R1 را جلوی کلاس با `norm.ppf` حساب کنید. دانشجوهایی که آمار برایشان تازه است باید ببینند $\Phi^{-1}$ «فقط یک جدول‌خوانی» است.
- **به چیزی که می‌شناسند وصل کنید:** یک تست کرونا یا بارداری نرخ hit (sensitivity) و نرخ false alarm (یک منهای specificity) دارد. «sensitivity» در پزشکی همان نرخ hit است، *نه* $d'$: به این تشابه اسمی اشاره کنید.
- **سؤال‌های رایج.**
  - *«چرا توزیع نرمال فرض می‌کنیم؟»* فرضی راحت و اغلب کافی است؛ آزمون zROC (شیب 1) آن را بررسی می‌کند و مدل واریانس نابرابر آن را آزادتر می‌کند.
  - *«آیا ملاک آسان‌گیر بد است؟»* نه؛ بهترین ملاک به هزینه‌ها و نرخ‌های پایه بستگی دارد.
  - *«نمایی یا توانی، کدام درست است؟»* در بسیاری از داده‌ها تابع توانی بهتر برازش می‌شود، ولی میانگین‌گیری روی افراد می‌تواند شکل توانی بسازد (هفته‌ی 5). سؤال را باز نگه دارید.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: Two radiologists (and a third) · بخش 1: دو رادیولوژیست (و یک سومی)

Each radiologist reads 100 tumor scans and 100 healthy scans.

<div dir="rtl">

هر رادیولوژیست 100 تصویر با تومور و 100 تصویر سالم را می‌خواند.

</div>

| Observer | $H$ | $F$ | $\Phi^{-1}(H)$ | $\Phi^{-1}(F)$ | $d'$ | $c$ | Percent correct |
|---|---|---|---|---|---|---|---|
| R0 (neutral) | 0.84 | 0.16 | 0.994 | −0.994 | 1.99 | 0.00 | 84% |
| R1 (liberal) | 0.93 | 0.31 | 1.476 | −0.496 | 1.97 | −0.49 | 81% |
| R2 (conservative) | 0.69 | 0.07 | 0.496 | −1.476 | 1.97 | +0.49 | 81% |

<div dir="rtl">

| مشاهده‌گر | $H$ | $F$ | $\Phi^{-1}(H)$ | $\Phi^{-1}(F)$ | $d'$ | $c$ | درصد درست |
|---|---|---|---|---|---|---|---|
| R0 (خنثی) | 0.84 | 0.16 | 0.994 | −0.994 | 1.99 | 0.00 | 84% |
| R1 (liberal) | 0.93 | 0.31 | 1.476 | −0.496 | 1.97 | −0.49 | 81% |
| R2 (محافظه‌کار) | 0.69 | 0.07 | 0.496 | −1.476 | 1.97 | +0.49 | 81% |

</div>

**Step by step for R1:**
1. $\Phi^{-1}(0.93) = 1.476$ and $\Phi^{-1}(0.31) = -0.496$ (`scipy.stats.norm.ppf`).
2. $d' = 1.476 - (-0.496) = 1.972$.
3. $c = -\tfrac{1}{2}(1.476 + (-0.496)) = -0.490$, which is negative, so R1 is liberal.
4. Check by plugging back in: $H = \Phi(1.972/2 + 0.490) = \Phi(1.476) = 0.93$. ✓

<div dir="rtl">

**قدم‌به‌قدم برای R1:**
1. $\Phi^{-1}(0.93) = 1.476$ و $\Phi^{-1}(0.31) = -0.496$ (`scipy.stats.norm.ppf`).
2. $d' = 1.476 - (-0.496) = 1.972$.
3. $c = -\tfrac{1}{2}(1.476 + (-0.496)) = -0.490$، که منفی است، پس R1 liberal است.
4. بررسی با جای‌گذاری: $H = \Phi(1.972/2 + 0.490) = \Phi(1.476) = 0.93$. ✓

</div>

**Interpretation.** All three radiologists have essentially the same sensitivity ($d' \approx 2$). R1 and R2 have the *same* percent correct but *opposite* biases. Which bias is better is not a question of perception but of costs: missing a tumor is usually far worse than a false alarm, so a liberal criterion may be the *desirable* one. SDT lets us ask "can they see it?" and "how willing are they to say so?" separately.

<div dir="rtl">

**تفسیر.** هر سه رادیولوژیست در عمل حساسیت یکسانی دارند ($d' \approx 2$). R1 و R2 درصد درست *یکسان* ولی سوگیری *مخالف* دارند. اینکه کدام سوگیری بهتر است سؤالی درباره‌ی ادراک نیست، بلکه درباره‌ی هزینه‌هاست: از دست دادن یک تومور معمولاً خیلی بدتر از یک false alarm است، پس شاید ملاک liberal همان ملاک *مطلوب* باشد. SDT به ما اجازه می‌دهد «آیا می‌بینند؟» و «چقدر آماده‌اند بگویند؟» را جداگانه بپرسیم.

</div>

**The extreme-rate fix.** A participant scores 50/50 hits and 3/50 false alarms. Then $H = 1$ and $d' = \infty$. With the log-linear correction: $H = 50.5/51 = 0.990$, $F = 3.5/51 = 0.069$, so $d' = 2.33 - (-1.49) = 3.82$.

<div dir="rtl">

**تصحیح نرخ حدی.** یک شرکت‌کننده 50/50 hit و 3/50 false alarm دارد. پس $H = 1$ و $d' = \infty$. با تصحیح log-linear: $H = 50.5/51 = 0.990$، $F = 3.5/51 = 0.069$، پس $d' = 2.33 - (-1.49) = 3.82$.

</div>

### Part 2: Exponential vs. power forgetting · بخش 2: فراموشی نمایی در برابر توانی

Take $A = 0.95$ for both models, $\lambda = 0.25$/day for the exponential and $d = 0.6$ for the power model.

<div dir="rtl">

برای هر دو مدل $A = 0.95$ بگیرید، برای مدل نمایی $\lambda = 0.25$ در روز و برای مدل توانی $d = 0.6$.

</div>

| $t$ (days) | 0 | 1 | 2 | 7 | 14 | 30 |
|---|---|---|---|---|---|---|
| Exponential $0.95\,e^{-0.25t}$ | 0.950 | 0.740 | 0.576 | 0.165 | 0.029 | 0.001 |
| Power $0.95\,(1+t)^{-0.6}$ | 0.950 | 0.627 | 0.491 | 0.273 | 0.187 | 0.121 |

<div dir="rtl">

| $t$ (روز) | 0 | 1 | 2 | 7 | 14 | 30 |
|---|---|---|---|---|---|---|
| نمایی $0.95\,e^{-0.25t}$ | 0.950 | 0.740 | 0.576 | 0.165 | 0.029 | 0.001 |
| توانی $0.95\,(1+t)^{-0.6}$ | 0.950 | 0.627 | 0.491 | 0.273 | 0.187 | 0.121 |

</div>

**Half-life (time until recall halves from its initial level):**
- Exponential: $e^{-\lambda t} = 1/2 \Rightarrow t_{1/2} = \ln 2 / \lambda = 0.693/0.25 = 2.77$ days.
- Power: $(1+t)^{-d} = 1/2 \Rightarrow t_{1/2} = 2^{1/d} - 1 = 2^{1.667} - 1 = 2.17$ days.

<div dir="rtl">

**نیمه‌عمر (زمانی که یادآوری به نصف سطح اولیه می‌رسد):**
- نمایی: $e^{-\lambda t} = 1/2 \Rightarrow t_{1/2} = \ln 2 / \lambda = 0.693/0.25 = 2.77$ روز.
- توانی: $(1+t)^{-d} = 1/2 \Rightarrow t_{1/2} = 2^{1/d} - 1 = 2^{1.667} - 1 = 2.17$ روز.

</div>

**Interpretation.** Over the first two days the curves are fairly similar: they differ by about 0.1, which is only about 1.5 binomial SDs with $n = 50$ items. After a month they disagree completely: the exponential model says practically everything is forgotten (0.1%), while the power model says 12% is still retained. **Long retention intervals are where these models can be told apart**, a design lesson you will use in Assignment A1.

<div dir="rtl">

**تفسیر.** در دو روز اول منحنی‌ها نسبتاً شبیه‌اند: حدود 0.1 با هم فرق دارند که با $n = 50$ آیتم فقط حدود 1.5 انحراف معیار دوجمله‌ای است. بعد از یک ماه کاملاً با هم اختلاف دارند: مدل نمایی می‌گوید تقریباً همه چیز فراموش شده (0.1%)، در حالی که مدل توانی می‌گوید 12% هنوز باقی است. **فاصله‌های نگهداری طولانی جایی است که این مدل‌ها از هم تشخیص داده می‌شوند**؛ درسی درباره‌ی طراحی آزمایش که در تکلیف A1 از آن استفاده می‌کنید.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Implement SDT as a generative model, simulate yes/no experiments, and estimate $d'$ and $c$.
2. Use ROC and zROC plots to **evaluate** the equal-variance assumption.
3. Implement exponential and power forgetting with binomial noise, and explore their parameters.
4. **Fit** both forgetting models by linearization, **evaluate** them with residuals, and **interpret** the result.

<div dir="rtl">

1. پیاده‌سازی SDT به‌عنوان یک مدل مولد (generative)، شبیه‌سازی آزمایش‌های بله/نه، و برآورد $d'$ و $c$.
2. استفاده از نمودارهای ROC و zROC برای **ارزیابی** فرض واریانس برابر.
3. پیاده‌سازی فراموشی نمایی و توانی با نویز دوجمله‌ای و بررسی پارامترهایشان.
4. **برازش** هر دو مدل فراموشی با خطی‌سازی، **ارزیابی** آن‌ها با باقی‌مانده‌ها (residuals)، و **تفسیر** نتیجه.

</div>

**Timing:** Part A 30 min · Part B 25 min · Part C 30 min · Part D 25 min · remaining time: exercises.

<div dir="rtl">

**زمان‌بندی:** بخش A 30 دقیقه · بخش B 25 دقیقه · بخش C 30 دقیقه · بخش D 25 دقیقه · زمان باقی‌مانده: تمرین‌ها.

</div>

### Setup · آماده‌سازی

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 1 · سلول 1

### Part A: SDT as a generative model (30 min) · بخش A: SDT به‌عنوان یک مدل مولد (30 دقیقه)

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 2 · سلول 2

Simulate one participant and recover the parameters:

<div dir="rtl">

یک شرکت‌کننده را شبیه‌سازی کنید و پارامترها را بازیابی کنید:

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Counts: {'hits': 68, 'misses': 32, 'fas': 11, 'crs': 89}
Predicted H = 0.674, F = 0.147
Estimated d' = 1.67 (true 1.5),  c = 0.37 (true 0.3)
```

One simulated participant tells us little about how good the *estimator* is. Let's repeat the experiment many times: this is a preview of the **parameter recovery** logic of Week 7.

<div dir="rtl">

یک شرکت‌کننده‌ی شبیه‌سازی‌شده چیز زیادی درباره‌ی کیفیت *برآوردگر* نمی‌گوید. آزمایش را چندین بار تکرار کنیم: این پیش‌نمایشی از منطق **بازیابی پارامتر** در هفته‌ی 7 است.

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 4 · سلول 4

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
            d_hat         c_hat
             mean    std   mean    std
n_per_type
20          1.500  0.449  0.296  0.224
50          1.489  0.290  0.295  0.143
200         1.502  0.142  0.299  0.071
```

**What to notice:** the estimates scatter around the true values, and the scatter shrinks as the number of trials grows. With 20 trials per type, the SD of $\hat d'$ is about 0.45, so individual estimates are often off by ±0.5 or more, and roughly 4× more trials are needed to halve the scatter. On average the estimates are on target here. With higher $d'$ and few trials, however, extreme rates become common, and the correction then pulls estimates toward 0 (try `true_d = 3` with 20 trials). Keep this in mind whenever you compare $d'$ across groups tested with different numbers of trials.

<div dir="rtl">

**به این دقت کنید:** برآوردها حول مقادیر واقعی پراکنده‌اند و پراکندگی با افزایش تعداد trialها کم می‌شود. با 20 trial از هر نوع، انحراف معیار $\hat d'$ حدود 0.45 است، پس برآوردهای تکی اغلب ±0.5 یا بیشتر خطا دارند، و برای نصف کردن پراکندگی تقریباً 4 برابر trial لازم است. اینجا به‌طور میانگین برآوردها درست سر هدف‌اند. ولی با $d'$ بالاتر و trialهای کم، نرخ‌های حدی رایج می‌شوند و آن‌وقت تصحیح، برآوردها را به سمت 0 می‌کشد (`true_d = 3` را با 20 trial امتحان کنید). هر وقت $d'$ گروه‌هایی را مقایسه می‌کنید که با تعداد trial متفاوت آزمون شده‌اند، این را در نظر داشته باشید.

</div>

### Part B: ROC curves and the equal-variance assumption (25 min) · بخش B: منحنی‌های ROC و فرض واریانس برابر (25 دقیقه)

First, the model's predicted ROCs:

<div dir="rtl">

اول، ROCهای پیش‌بینی‌شده‌ی مدل:

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 5 · سلول 5

Now simulate a **confidence-rating** experiment. Responses are given on a 6-point scale (1 = "sure noise" … 6 = "sure signal"), which amounts to five criteria at once. We generate data from an equal-variance observer and from an **unequal-variance** observer whose signal distribution has SD 1.5.

<div dir="rtl">

حالا یک آزمایش **درجه‌بندی اطمینان** را شبیه‌سازی کنید. پاسخ‌ها روی یک مقیاس 6 درجه‌ای داده می‌شوند (1 = «مطمئنم نویز است» … 6 = «مطمئنم علامت است») که معادل پنج ملاک هم‌زمان است. داده‌ها را از یک مشاهده‌گر با واریانس برابر و از یک مشاهده‌گر با **واریانس نابرابر** که توزیع علامتش انحراف معیار 1.5 دارد تولید می‌کنیم.

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
sigma_signal = 1.0: zROC slope = 0.96 (predicted 1.00); d' at each criterion = [1.52 1.48 1.48 1.43 1.43]
sigma_signal = 1.5: zROC slope = 0.67 (predicted 0.67); d' at each criterion = [1.46 1.34 1.16 0.96 0.84]
```

**Evaluate and interpret.** For the equal-variance observer, the zROC slope is close to 1 and $d'$ is about the same at every criterion: the model's assumption holds. For the unequal-variance observer, the slope is close to $1/1.5 = 0.67$ and $d'$ **changes systematically with the criterion**. If we had collected only yes/no data from such an observer, a group difference in "$d'$" could be produced purely by a difference in bias. Checking a model's signature prediction (here: zROC slope = 1) is a basic form of **model evaluation**.

<div dir="rtl">

**ارزیابی و تفسیر.** برای مشاهده‌گر با واریانس برابر، شیب zROC نزدیک 1 است و $d'$ در همه‌ی ملاک‌ها تقریباً یکسان است: فرض مدل برقرار است. برای مشاهده‌گر با واریانس نابرابر، شیب نزدیک $1/1.5 = 0.67$ است و $d'$ **به‌طور نظام‌مند با ملاک تغییر می‌کند**. اگر از چنین مشاهده‌گری فقط داده‌ی بله/نه جمع کرده بودیم، تفاوت گروه‌ها در «$d'$» می‌توانست صرفاً از تفاوت در سوگیری بیاید. بررسی پیش‌بینی امضایی یک مدل (اینجا: شیب zROC = 1) شکل پایه‌ای از **ارزیابی مدل** است.

</div>

### Part C: Forgetting curves with binomial noise (30 min) · بخش C: منحنی‌های فراموشی با نویز دوجمله‌ای (30 دقیقه)

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 7 · سلول 7

Explore the parameters: how do $A$ and the decay parameter change each curve?

<div dir="rtl">

پارامترها را بررسی کنید: $A$ و پارامتر زوال هر منحنی را چگونه تغییر می‌دهند؟

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 8 · سلول 8

Now generate a **simulated experiment**. The data come from the *power* model, with 50 items tested at each of 8 retention intervals:

<div dir="rtl">

حالا یک **آزمایش شبیه‌سازی‌شده** بسازید. داده‌ها از مدل *توانی* می‌آیند، با 50 آیتم که در هر یک از 8 فاصله‌ی نگهداری آزمون می‌شوند:

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 9 · سلول 9

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
       t  recalled   n  p_obs
0   0.25        42  50   0.84
1   1.00        30  50   0.60
2   2.00        26  50   0.52
3   4.00        25  50   0.50
4   7.00        13  50   0.26
5  14.00        13  50   0.26
6  21.00        13  50   0.26
7  30.00        14  50   0.28
```

### Part D: Fit by linearization, evaluate, interpret (25 min) · بخش D: برازش با خطی‌سازی، ارزیابی، تفسیر (25 دقیقه)

**Fit.** Fit each model by a straight-line regression on the log scale (Lecture §5).

<div dir="rtl">

**برازش.** هر مدل را با رگرسیون خط راست روی مقیاس لگاریتمی برازش کنید (بخش 5 جزوه).

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 10 · سلول 10

**Evaluate.** Look at the fitted curves *and* the residuals. A good model leaves residuals that scatter randomly around zero; a systematic pattern means the model's *shape* is wrong.

<div dir="rtl">

**ارزیابی.** به منحنی‌های برازش‌شده *و* باقی‌مانده‌ها نگاه کنید. یک مدل خوب باقی‌مانده‌هایی به جا می‌گذارد که به‌طور تصادفی حول صفر پراکنده‌اند؛ یک الگوی نظام‌مند یعنی *شکل* مدل غلط است.

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 11 · سلول 11

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
exp: A = 0.550, rate = 0.032, RMSD = 0.1308
pow: A = 0.797, rate = 0.370, RMSD = 0.0628
true (power): A = 0.9, d = 0.5
```

**Interpret (write 2–3 sentences for each in your notebook):**

<div dir="rtl">

**تفسیر (برای هرکدام 2 تا 3 جمله در notebook بنویسید):**

</div>

1. Which model describes the data better, and what does the residual pattern of the *other* model look like? (Look for an inverted-U or U shape: the exponential overshoots at intermediate delays and undershoots at the long ones, or the reverse.)
2. Using the fitted parameters, what is each model's relative loss rate after 1 day and after 20 days? What does this mean for memory?
3. The power model is the true model here, yet its estimates ($\hat A \approx 0.80$, $\hat d \approx 0.37$) are noticeably off the true values ($A^\ast = 0.9$, $d^\ast = 0.5$). Name two reasons. (Hints: look at the last three data points; think about what the log transform does to the weights of small proportions.) In Week 3 we refit these same data on the original scale and compare.

<div dir="rtl">

1. کدام مدل داده‌ها را بهتر توصیف می‌کند، و الگوی باقی‌مانده‌های مدل *دیگر* چه شکلی دارد؟ (دنبال شکل U یا U وارونه بگردید: مدل نمایی در فاصله‌های میانی بیش‌برآورد و در فاصله‌های طولانی کم‌برآورد می‌کند، یا برعکس.)
2. با پارامترهای برازش‌شده، نرخ نسبی فراموشی هر مدل بعد از 1 روز و بعد از 20 روز چقدر است؟ این برای حافظه چه معنایی دارد؟
3. اینجا مدل توانی مدل واقعی است، ولی برآوردهایش ($\hat A \approx 0.80$، $\hat d \approx 0.37$) آشکارا با مقادیر واقعی ($A^\ast = 0.9$، $d^\ast = 0.5$) فاصله دارند. دو دلیل نام ببرید. (راهنمایی: به سه نقطه‌ی آخر نگاه کنید؛ فکر کنید تبدیل لگاریتمی با وزن نسبت‌های کوچک چه می‌کند.) در هفته‌ی 3 همین داده‌ها را روی مقیاس اصلی دوباره برازش و مقایسه می‌کنیم.

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★ (extreme rates).** A participant has 40/40 hits and 0/40 false alarms. Compute $d'$ without and with the log-linear correction. What does the corrected $d'$ represent, and why should you report the correction you used?

<div dir="rtl">

**تمرین 1 ★ (نرخ‌های حدی).** یک شرکت‌کننده 40/40 hit و 0/40 false alarm دارد. $d'$ را بدون تصحیح و با تصحیح log-linear حساب کنید. $d'$ تصحیح‌شده نماینده‌ی چیست، و چرا باید تصحیحی را که استفاده کرده‌اید گزارش کنید؟

</div>

**Exercise 2 ★ (half-lives).** Using your fitted parameters from Part D, compute each model's half-life. Then compute how long it takes recall to drop to 10% of its initial level. Where do the models disagree most?

<div dir="rtl">

**تمرین 2 ★ (نیمه‌عمرها).** با پارامترهای برازش‌شده از بخش D، نیمه‌عمر هر مدل را حساب کنید. بعد حساب کنید چقدر طول می‌کشد تا یادآوری به 10% سطح اولیه برسد. مدل‌ها کجا بیشترین اختلاف را دارند؟

</div>

**Exercise 3 ★★ (Ebbinghaus's data).** The classic savings data from Ebbinghaus's 1885 self-experiments are often reported as follows [verify against the original source before using them in class]:

<div dir="rtl">

**تمرین 3 ★★ (داده‌های ابینگهاوس).** داده‌های کلاسیک savings از آزمایش‌های ابینگهاوس روی خودش در 1885 اغلب این‌طور گزارش می‌شوند [پیش از استفاده در کلاس با منبع اصلی تطبیق داده شود]:

</div>

| Interval | 20 min | 1 h | 8.8 h | 1 day | 2 days | 6 days | 31 days |
|---|---|---|---|---|---|---|---|
| Savings (%) | 58.2 | 44.2 | 35.8 | 33.7 | 27.8 | 25.4 | 21.1 |

<div dir="rtl">

| فاصله | 20 دقیقه | 1 ساعت | 8.8 ساعت | 1 روز | 2 روز | 6 روز | 31 روز |
|---|---|---|---|---|---|---|---|
| Savings (%) | 58.2 | 44.2 | 35.8 | 33.7 | 27.8 | 25.4 | 21.1 |

</div>

Convert the intervals to days, fit both models by linearization, and compare their residuals. Which shape fits better? Then redo the analysis with time measured in **hours**. Does the power fit change? Explain, using the Advanced box in Lecture §3.

<div dir="rtl">

فاصله‌ها را به روز تبدیل کنید، هر دو مدل را با خطی‌سازی برازش کنید و باقی‌مانده‌هایشان را مقایسه کنید. کدام شکل بهتر برازش می‌شود؟ بعد تحلیل را با زمان بر حسب **ساعت** تکرار کنید. آیا برازش توانی تغییر می‌کند؟ با استفاده از کادر «پیشرفته» در بخش 3 جزوه توضیح دهید.

</div>

**Exercise 4 ★★ (which design can tell the models apart?).** Choose $(A, \lambda)$ and $(A, d)$ so that the two models predict the *same* recall at $t = 1$ and $t = 7$ days. (Hint: two equations in two unknowns per model; take logs.) Then plot both curves from $t = 0$ to $60$ days and mark where their difference exceeds 2 binomial SDs with $n = 50$. Which retention intervals would you test?

<div dir="rtl">

**تمرین 4 ★★ (کدام طرح آزمایش مدل‌ها را از هم جدا می‌کند؟).** $(A, \lambda)$ و $(A, d)$ را طوری انتخاب کنید که دو مدل در $t = 1$ و $t = 7$ روز یادآوری *یکسانی* پیش‌بینی کنند. (راهنمایی: برای هر مدل دو معادله و دو مجهول؛ لگاریتم بگیرید.) بعد هر دو منحنی را از $t = 0$ تا $60$ روز رسم کنید و جاهایی را که اختلافشان با $n = 50$ از 2 انحراف معیار دوجمله‌ای بیشتر است علامت بزنید. کدام فاصله‌های نگهداری را آزمون می‌کردید؟

</div>

**Exercise 5 ★★★ (Advanced: zero counts).** Generate data from the exponential model with $A = 0.9$, $\lambda = 0.3$ at the intervals in Part C, with $n = 20$ items. How often (out of 1000 simulated datasets) does at least one interval produce zero recalls, which breaks `fit_linearized`? Propose and implement a quick fix (e.g., adding 0.5 to counts) and check whether it biases the estimate of $\lambda$. Explain why this is a sign that we need a method that works on the original scale (Weeks 3–4).

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: شمارش صفر).** از مدل نمایی با $A = 0.9$، $\lambda = 0.3$ در فاصله‌های بخش C و با $n = 20$ آیتم داده تولید کنید. چند بار (از 1000 مجموعه‌داده‌ی شبیه‌سازی‌شده) دست‌کم یک فاصله یادآوری صفر دارد که `fit_linearized` را از کار می‌اندازد؟ یک راه‌حل سریع (مثلاً افزودن 0.5 به شمارش‌ها) پیشنهاد و پیاده‌سازی کنید و بررسی کنید آیا برآورد $\lambda$ را سوگیر می‌کند. توضیح دهید چرا این نشان می‌دهد به روشی نیاز داریم که روی مقیاس اصلی کار کند (هفته‌های 3–4).

</div>

### Lab check-off · lab check-off

Show the instructor or TA: (1) your SDT recovery table from Part A, (2) the two empirical zROCs with their slopes from Part B, and (3) the residual plot from Part D with a one-sentence interpretation.

<div dir="rtl">

به مدرس یا دستیار آموزشی نشان دهید: (1) جدول بازیابی SDT از بخش A، (2) دو zROC تجربی با شیب‌هایشان از بخش B، و (3) نمودار باقی‌مانده‌ها از بخش D با یک جمله تفسیر.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**AI-text detectors are observers in an SDT task.** Universities increasingly use tools that score a text for "how likely it was written by AI". Each text is either AI-written ("signal") or human-written ("noise"), and the tool says "AI" when its score exceeds a threshold. This is exactly the SDT setting of this week: the tool has a **sensitivity** $d'$ (how well the score separates the two kinds of texts) and a **criterion** $c$ (the threshold the user chooses). A false alarm means a student is wrongly accused, so the choice of criterion is an ethical decision, not only a technical one.

<div dir="rtl">

**آشکارسازهای متن هوش مصنوعی، مشاهده‌گرهایی در یک تکلیف SDT هستند.** دانشگاه‌ها روزبه‌روز بیشتر از ابزارهایی استفاده می‌کنند که به یک متن امتیاز «چقدر محتمل است که هوش مصنوعی نوشته باشد» می‌دهند. هر متن یا با هوش مصنوعی نوشته شده («علامت») یا با انسان («نویز»)، و ابزار وقتی امتیاز از یک آستانه بیشتر شود می‌گوید «هوش مصنوعی». این دقیقاً موقعیت SDT این هفته است: ابزار یک **حساسیت** $d'$ دارد (امتیاز چقدر خوب دو نوع متن را از هم جدا می‌کند) و یک **ملاک** $c$ (آستانه‌ای که کاربر انتخاب می‌کند). یک false alarm یعنی دانشجویی به‌اشتباه متهم شود، پس انتخاب ملاک یک تصمیم اخلاقی است، نه فقط فنی.

</div>

> **Code · کد:** [`code/week02.py`](code/week02.py), cell 12 · سلول 12

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
threshold 0.0: H = 0.84, F = 0.49, d' = 1.03, c = -0.50
threshold 0.6: H = 0.70, F = 0.28, d' = 1.11, c = 0.03
threshold 1.2: H = 0.51, F = 0.09, d' = 1.35, c = 0.66
```

Moving the threshold changes $c$ a lot (from −0.50 to 0.66), while $d'$ stays near its true value of 1.2. The variation in $d'$ is sampling noise from 200 texts per group.

<div dir="rtl">

جابه‌جا کردن آستانه $c$ را خیلی تغییر می‌دهد (از −0.50 تا 0.66)، در حالی که $d'$ نزدیک مقدار واقعی‌اش یعنی 1.2 می‌ماند. تغییرات $d'$ نویز نمونه‌گیری ناشی از 200 متن در هر گروه است.

</div>

**Try it (no API needed).**
- ★ Suppose 10% of submitted essays are AI-written. At threshold 1.2, what is $P(\text{AI-written} \mid \text{flagged})$? (Use Bayes' rule with $H$ and $F$.) Would you act on a flag?
- ★★ Plot the ROC of the detector (all thresholds from −2 to 3) and its zROC. Is the slope close to 1? Repeat with human-text scores of SD 1.5 (an unequal-variance detector).
- ★★ Discussion: detectors have been reported to flag texts by non-native English writers more often [verify: Liang et al., 2023, *Patterns*]. In SDT terms, what would that mean, and what should a university do?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ فرض کنید 10% مقاله‌های تحویلی با هوش مصنوعی نوشته شده‌اند. در آستانه‌ی 1.2، $P(\text{AI-written} \mid \text{flagged})$ چقدر است؟ (از قاعده‌ی بیز با $H$ و $F$ استفاده کنید.) آیا بر اساس یک هشدار اقدام می‌کنید؟
- ★★ ROC آشکارساز (همه‌ی آستانه‌ها از −2 تا 3) و zROC آن را رسم کنید. آیا شیب نزدیک 1 است؟ با امتیازهای متن انسانی با انحراف معیار 1.5 (آشکارسازی با واریانس نابرابر) تکرار کنید.
- ★★ بحث: گزارش شده که آشکارسازها متن‌های نویسندگان غیربومی انگلیسی را بیشتر علامت می‌زنند [بررسی شود: Liang et al., 2023, *Patterns*]. به زبان SDT این یعنی چه، و یک دانشگاه چه باید بکند؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **"Percent correct is good enough."** It confounds sensitivity and bias (see the radiologists). Use $d'$ and $c$ whenever responses can be biased.
2. **Computing $d'$ as $\Phi^{-1}(H - F)$ or from percentages.** The formula is $\Phi^{-1}(H) - \Phi^{-1}(F)$, with rates as proportions between 0 and 1.
3. **Forgetting the extreme-rate problem.** $H = 1$ or $F = 0$ gives an infinite $d'$; Python returns `inf` without an error. Always use (and report) a correction.
4. **Assuming $d'$ is bias-free no matter what.** It is criterion-independent only under the equal-variance model. If the zROC slope differs from 1, $d'$ from one $(H, F)$ pair depends on bias.
5. **"Exponential and power are just two curve shapes."** They make different claims about how forgetting works (constant vs. decreasing relative loss rate).
6. **Judging a model only by its fit statistic.** A small RMSD with a systematic residual pattern means the model's shape is wrong. Always plot the residuals.
7. **Ignoring the noise model.** A model is not just $f(x;\boldsymbol\theta)$. The binomial noise of recall proportions is part of the model, and it tells you which differences are meaningful.
8. **Changing the units of $t$ in the shifted power model** and expecting the same shape.

<div dir="rtl">

1. **«درصد پاسخ درست کافی است.»** حساسیت و سوگیری را قاطی می‌کند (رادیولوژیست‌ها را ببینید). هر وقت پاسخ‌ها ممکن است سوگیری داشته باشند از $d'$ و $c$ استفاده کنید.
2. **محاسبه‌ی $d'$ به شکل $\Phi^{-1}(H - F)$ یا از روی درصدها.** فرمول $\Phi^{-1}(H) - \Phi^{-1}(F)$ است، با نرخ‌ها به‌صورت نسبت بین 0 و 1.
3. **فراموش کردن مشکل نرخ‌های حدی.** $H = 1$ یا $F = 0$ یک $d'$ بی‌نهایت می‌دهد و Python بدون هیچ خطایی `inf` برمی‌گرداند. همیشه از یک تصحیح استفاده کنید (و آن را گزارش کنید).
4. **فرض اینکه $d'$ در هر حالتی مستقل از سوگیری است.** فقط تحت مدل واریانس برابر مستقل از ملاک است. اگر شیب zROC با 1 فرق کند، $d'$ یک جفت $(H, F)$ به سوگیری بستگی دارد.
5. **«نمایی و توانی فقط دو شکل منحنی‌اند.»** آن‌ها ادعاهای متفاوتی درباره‌ی چگونگی فراموشی دارند (نرخ نسبی ثابت در برابر کاهشی).
6. **قضاوت درباره‌ی مدل فقط با آماره‌ی برازش.** RMSD کوچک همراه با الگوی نظام‌مند در باقی‌مانده‌ها یعنی شکل مدل غلط است. همیشه باقی‌مانده‌ها را رسم کنید.
7. **نادیده گرفتن مدل نویز.** مدل فقط $f(x;\boldsymbol\theta)$ نیست. نویز دوجمله‌ای نسبت‌های یادآوری جزئی از مدل است و به شما می‌گوید کدام تفاوت‌ها معنادارند.
8. **تغییر واحد $t$ در مدل توانی جابه‌جاشده** و انتظار شکل یکسان.

</div>

---

## Check your understanding · خودآزمایی

**1.** Name the five components of a model and give the SDT version of each.
<details><summary>Answer</summary>
Design (signal vs. noise trials; yes/no responses); parameters (free: $d'$, $c$; fixed: noise mean 0, both SDs 1); deterministic core ($H = \Phi(d'/2 - c)$, $F = \Phi(-d'/2 - c)$); noise model (hit and FA counts are binomial); linking assumption (respond "yes" when the evidence exceeds the criterion).
</details>

<div dir="rtl">

**1.** پنج جزء یک مدل را نام ببرید و نسخه‌ی SDT هرکدام را بگویید.
<details><summary>پاسخ</summary>
طرح آزمایش (trialهای علامت در برابر نویز؛ پاسخ‌های بله/نه)؛ پارامترها (آزاد: $d'$، $c$؛ ثابت: میانگین نویز 0، هر دو انحراف معیار 1)؛ هسته‌ی قطعی ($H = \Phi(d'/2 - c)$، $F = \Phi(-d'/2 - c)$)؛ مدل نویز (شمارش hitها و false alarmها دوجمله‌ای است)؛ فرض پیوند (وقتی شواهد از ملاک بیشتر است پاسخ «بله»).
</details>

</div>

**2.** Why are the noise mean and the SDs in SDT fixed rather than free?
<details><summary>Answer</summary>
Because they are not identifiable: shifting both distributions and the criterion by the same amount, or stretching the whole axis, leaves every prediction unchanged. Fixing them (scaling constraints) defines the units in which $d'$ and $c$ are measured.
</details>

<div dir="rtl">

**2.** چرا میانگین نویز و انحراف معیارها در SDT ثابت‌اند و آزاد نیستند؟
<details><summary>پاسخ</summary>
چون identifiable نیستند: جابه‌جا کردن هر دو توزیع و ملاک به یک اندازه، یا کشیدن کل محور، هیچ پیش‌بینی‌ای را عوض نمی‌کند. ثابت کردن آن‌ها (قیدهای مقیاس) واحدهایی را تعریف می‌کند که $d'$ و $c$ با آن اندازه‌گیری می‌شوند.
</details>

</div>

**3.** An observer has $H = 0.80$ and $F = 0.20$. Compute $d'$ and $c$. ($\Phi^{-1}(0.80) = 0.842$)
<details><summary>Answer</summary>
$d' = 0.842 - (-0.842) = 1.68$; $c = -\tfrac{1}{2}(0.842 - 0.842) = 0$, so the observer is unbiased.
</details>

<div dir="rtl">

**3.** یک مشاهده‌گر $H = 0.80$ و $F = 0.20$ دارد. $d'$ و $c$ را حساب کنید. ($\Phi^{-1}(0.80) = 0.842$)
<details><summary>پاسخ</summary>
$d' = 0.842 - (-0.842) = 1.68$؛ $c = -\tfrac{1}{2}(0.842 - 0.842) = 0$، پس مشاهده‌گر بی‌سوگیری است.
</details>

</div>

**4.** What does equal-variance SDT predict about the zROC, and what does it mean if the empirical slope is 0.7?
<details><summary>Answer</summary>
A straight line with slope 1. A slope of 0.7 suggests the signal distribution is more variable than the noise distribution ($\sigma_s \approx 1/0.7 \approx 1.4$). Then single-point $d'$ depends on the criterion, and an unequal-variance model (or $d_a$) should be used.
</details>

<div dir="rtl">

**4.** SDT با واریانس برابر درباره‌ی zROC چه پیش‌بینی می‌کند، و اگر شیب تجربی 0.7 باشد یعنی چه؟
<details><summary>پاسخ</summary>
یک خط راست با شیب 1. شیب 0.7 نشان می‌دهد توزیع علامت از توزیع نویز متغیرتر است ($\sigma_s \approx 1/0.7 \approx 1.4$). در این صورت $d'$ تک‌نقطه‌ای به ملاک بستگی دارد و باید از مدل واریانس نابرابر (یا $d_a$) استفاده کرد.
</details>

</div>

**5.** What is the relative loss rate of each forgetting model, and why does it matter psychologically?
<details><summary>Answer</summary>
Exponential: $\lambda$, constant. Power: $d/(1+t)$, decreasing over time. The exponential says memories lose the same proportion of strength per day at every age; the power function says older memories become more resistant to further forgetting.
</details>

<div dir="rtl">

**5.** نرخ نسبی فراموشی هر مدل چیست، و چرا از نظر روان‌شناختی مهم است؟
<details><summary>پاسخ</summary>
نمایی: $\lambda$، ثابت. توانی: $d/(1+t)$، با گذشت زمان کاهشی. مدل نمایی می‌گوید خاطره‌ها در هر سنی روزانه نسبت یکسانی از قدرتشان را از دست می‌دهند؛ تابع توانی می‌گوید خاطره‌های قدیمی‌تر در برابر فراموشی بیشتر مقاوم‌تر می‌شوند.
</details>

</div>

**6.** Which plot would you make to check quickly whether forgetting data look exponential? And for power?
<details><summary>Answer</summary>
Exponential: $\ln(\text{recall})$ against $t$ (semi-log), which should be a straight line. Power: $\ln(\text{recall})$ against $\ln(1+t)$ (log-log), which should be a straight line.
</details>

<div dir="rtl">

**6.** برای اینکه سریع ببینید داده‌های فراموشی نمایی به نظر می‌رسند چه نموداری رسم می‌کنید؟ و برای توانی؟
<details><summary>پاسخ</summary>
نمایی: $\ln(\text{recall})$ در برابر $t$ (نیمه‌لگاریتمی) که باید خط راست باشد. توانی: $\ln(\text{recall})$ در برابر $\ln(1+t)$ (لگاریتمی–لگاریتمی) که باید خط راست باشد.
</details>

</div>

**7.** Give two reasons why fitting a straight line to log-transformed proportions is a poor estimation method.
<details><summary>Answer</summary>
(i) It breaks when an observed proportion is 0. (ii) It distorts the noise: small proportions become very variable on the log scale but are weighted equally, and the errors being minimized are on the wrong (log) scale. Fitting on the original scale with least squares or maximum likelihood avoids these problems.
</details>

<div dir="rtl">

**7.** دو دلیل بیاورید که چرا برازش خط راست روی نسبت‌های لگاریتمی‌شده روش برآورد ضعیفی است.
<details><summary>پاسخ</summary>
(1) وقتی یک نسبت مشاهده‌شده 0 باشد از کار می‌افتد. (2) نویز را تحریف می‌کند: نسبت‌های کوچک روی مقیاس لگاریتمی خیلی متغیر می‌شوند ولی با وزن برابر در نظر گرفته می‌شوند، و خطاهایی که کمینه می‌شوند روی مقیاس غلط (لگاریتمی) هستند. برازش روی مقیاس اصلی با کمترین مربعات یا بیشینه درست‌نمایی از این مشکلات جلوگیری می‌کند.
</details>

</div>

---

## Assignment · تکلیف

### A1: From verbal to formal (1.0 point of 20; released Week 2, due at the start of the Week 4 lecture) · A1: از کلامی به فرمال (1.0 نمره از 20؛ انتشار هفته‌ی 2، موعد ابتدای درس هفته‌ی 4)

**Scenario.** Two research groups study forgetting of vocabulary learned in a foreign-language course.
- **Group C** says: *"Memories decay at a constant rate."*
- **Group R** says: *"Memories become more resistant to forgetting as they age."*

<div dir="rtl">

**سناریو.** دو گروه پژوهشی فراموشی واژه‌هایی را که در یک کلاس زبان خارجی یاد گرفته شده‌اند مطالعه می‌کنند.
- **گروه C** می‌گوید: *«خاطره‌ها با نرخ ثابتی زوال پیدا می‌کنند.»*
- **گروه R** می‌گوید: *«خاطره‌ها با بالا رفتن سن در برابر فراموشی مقاوم‌تر می‌شوند.»*

</div>

Both groups claim that the published data (recall drops quickly and then levels off) support their view.

<div dir="rtl">

هر دو گروه ادعا می‌کنند داده‌های منتشرشده (یادآوری سریع افت می‌کند و بعد ثابت می‌شود) از دیدگاهشان حمایت می‌کند.

</div>

**Tasks.** Submit a Jupyter notebook plus a PDF export.

<div dir="rtl">

**کارها.** یک Jupyter notebook به‌همراه خروجی PDF آن تحویل دهید.

</div>

1. **Formalize (Group C and Group R).** Write each verbal claim as a formal model with all five components from Lecture §1: design, free/fixed parameters with ranges, deterministic core, binomial noise model, and linking assumption. Justify in 2–3 sentences why each equation captures its verbal claim (use the relative loss rate).
2. **Implement.** Write Python functions that (a) return predicted recall probabilities and (b) simulate binomial recall counts for given intervals and number of items $n$.
3. **Calibrate.** Both groups agree that recall is **0.60 after 1 day** and **0.35 after 7 days**. Derive, by hand and in closed form, the parameters of each model that reproduce these two values exactly. Show the derivation (take logs) and verify it numerically.
4. **Find where they diverge.** With the calibrated parameters, plot both predicted curves from 0 to 90 days. For $n = 40$ items, compute at each interval a *discriminability index* $D(t) = \big(f_C(t) - f_R(t)\big)^2 / \mathrm{Var}(t)$, where $\mathrm{Var}(t) = \bar f(1 - \bar f)/n$ and $\bar f$ is the average of the two predictions. Plot $D(t)$.
5. **Design an experiment.** You can test each participant at only **4** retention intervals, chosen from {0.5, 1, 2, 4, 7, 14, 30, 60, 90} days. Choose the set that maximizes the summed $D(t)$, explain why it makes sense, and simulate one dataset from *each* model at your design. Show the two datasets on one plot.
6. **Interpret (max. 300 words).** Which data would favor Group C and which Group R? What does your analysis say about why both groups can claim support from "the published data"? Name one assumption of your models that could be wrong, and how it would change your conclusions.

<div dir="rtl">

1. **فرمال‌سازی (گروه C و گروه R).** هر ادعای کلامی را به‌صورت یک مدل فرمال با هر پنج جزء بخش 1 جزوه بنویسید: طرح آزمایش، پارامترهای آزاد/ثابت با دامنه‌شان، هسته‌ی قطعی، مدل نویز دوجمله‌ای، و فرض پیوند. در 2 تا 3 جمله توجیه کنید چرا هر معادله ادعای کلامی‌اش را نشان می‌دهد (از نرخ نسبی فراموشی استفاده کنید).
2. **پیاده‌سازی.** توابع Python بنویسید که (الف) احتمال‌های یادآوری پیش‌بینی‌شده را برگردانند و (ب) برای فاصله‌ها و تعداد آیتم $n$ داده‌شده، شمارش‌های یادآوری دوجمله‌ای را شبیه‌سازی کنند.
3. **کالیبراسیون.** هر دو گروه قبول دارند که یادآوری **بعد از 1 روز 0.60** و **بعد از 7 روز 0.35** است. پارامترهای هر مدل را که دقیقاً این دو مقدار را بازتولید می‌کنند، دستی و به‌صورت بسته به دست آورید. محاسبه را نشان دهید (لگاریتم بگیرید) و آن را عددی بررسی کنید.
4. **پیدا کردن جای اختلاف.** با پارامترهای کالیبره‌شده، هر دو منحنی پیش‌بینی‌شده را از 0 تا 90 روز رسم کنید. برای $n = 40$ آیتم، در هر فاصله یک *شاخص تمایزپذیری* $D(t) = \big(f_C(t) - f_R(t)\big)^2 / \mathrm{Var}(t)$ حساب کنید که در آن $\mathrm{Var}(t) = \bar f(1 - \bar f)/n$ و $\bar f$ میانگین دو پیش‌بینی است. $D(t)$ را رسم کنید.
5. **طراحی آزمایش.** می‌توانید هر شرکت‌کننده را فقط در **4** فاصله‌ی نگهداری آزمون کنید که از میان {0.5، 1، 2، 4، 7، 14، 30، 60، 90} روز انتخاب می‌شوند. مجموعه‌ای را انتخاب کنید که مجموع $D(t)$ را بیشینه کند، توضیح دهید چرا منطقی است، و با طرح خود یک مجموعه‌داده از *هر* مدل شبیه‌سازی کنید. دو مجموعه‌داده را روی یک نمودار نشان دهید.
6. **تفسیر (حداکثر 300 کلمه).** کدام داده‌ها به نفع گروه C و کدام به نفع گروه R هستند؟ تحلیل شما درباره‌ی اینکه چرا هر دو گروه می‌توانند ادعا کنند «داده‌های منتشرشده» از آن‌ها حمایت می‌کند چه می‌گوید؟ یک فرض مدل‌هایتان را که ممکن است غلط باشد نام ببرید و بگویید چطور نتیجه‌گیری‌تان را تغییر می‌دهد.

</div>

**Grading rubric (10 points, scaled to 1.0 of the final grade):**

<div dir="rtl">

**روبریک نمره‌دهی (10 امتیاز، معادل 1.0 از نمره‌ی نهایی):**

</div>

| Criterion | Points | Full marks require |
|---|---|---|
| Formalization (Task 1) | 2 | All five components for both models; correct parameter ranges; the link between equation and verbal claim is explained via the relative loss rate |
| Code (Task 2) | 2 | Correct, commented, reproducible (fixed seeds); functions are vectorized or clearly looped |
| Calibration (Task 3) | 2 | Correct closed-form derivation and numerical check for both models |
| Divergence and design (Tasks 4–5) | 2.5 | Correct $D(t)$; the chosen design is justified and actually maximizes the criterion; clear plots |
| Interpretation (Task 6) | 1.5 | Clear, specific, refers to your own results; names a real limitation |

<div dir="rtl">

| معیار | امتیاز | شرط نمره‌ی کامل |
|---|---|---|
| فرمال‌سازی (کار 1) | 2 | هر پنج جزء برای هر دو مدل؛ دامنه‌ی درست پارامترها؛ ارتباط معادله و ادعای کلامی با نرخ نسبی فراموشی توضیح داده شده |
| کد (کار 2) | 2 | درست، با توضیح (comment)، قابل بازتولید (seed ثابت)؛ توابع برداری‌شده یا با حلقه‌ی روشن |
| کالیبراسیون (کار 3) | 2 | استخراج بسته‌ی درست و بررسی عددی برای هر دو مدل |
| اختلاف و طراحی (کارهای 4–5) | 2.5 | $D(t)$ درست؛ طرح انتخاب‌شده توجیه شده و واقعاً معیار را بیشینه می‌کند؛ نمودارهای روشن |
| تفسیر (کار 6) | 1.5 | روشن، مشخص، با ارجاع به نتایج خودتان؛ یک محدودیت واقعی را نام می‌برد |

</div>

Late submissions lose 10% per day (max. 3 days).

<div dir="rtl">

برای تحویل با تأخیر، روزی 10% کسر می‌شود (حداکثر 3 روز).

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018), chapter 2.** Building a model from a verbal theory; the components of a model and the role of parameters. *(Main reading.)*
- **Lee & Wagenmakers (2014), chapter 11.** Signal detection theory treated as a (Bayesian) cognitive model; we return to it in Weeks 9 and 13. Read the introductory part now, skip the code.
- **Verguts (2022)** and **Anderson (2014)**: the chapters on model building and parameters [verify chapter numbers].
- *Background on forgetting curves:* Lee & Wagenmakers (2014), chapter 10 (memory retention) uses a closely related exponential retention model; we will fit it in a Bayesian way in Weeks 9–11.

<div dir="rtl">

- **Farrell & Lewandowsky (2018)، فصل 2.** ساختن مدل از یک نظریه‌ی کلامی؛ اجزای مدل و نقش پارامترها. *(منبع اصلی.)*
- **Lee & Wagenmakers (2014)، فصل 11.** نظریه‌ی تشخیص علامت به‌عنوان یک مدل شناختی (بیزی)؛ در هفته‌های 9 و 13 به آن برمی‌گردیم. بخش مقدمه را الان بخوانید و از کد بگذرید.
- **Verguts (2022)** و **Anderson (2014)**: فصل‌های مربوط به ساختن مدل و پارامترها [شماره‌ی فصل‌ها بررسی شود].
- *پیش‌زمینه درباره‌ی منحنی‌های فراموشی:* Lee & Wagenmakers (2014)، فصل 10 (نگهداری حافظه) از یک مدل نگهداری نمایی نزدیک استفاده می‌کند که آن را در هفته‌های 9–11 به روش بیزی برازش می‌کنیم.

</div>

*Preview for Week 3:* we drop linearization and fit models directly by minimizing squared error, which means learning how optimization algorithms search a parameter space.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 3:* خطی‌سازی را کنار می‌گذاریم و مدل‌ها را مستقیماً با کمینه کردن مربع خطا برازش می‌کنیم؛ یعنی یاد می‌گیریم الگوریتم‌های بهینه‌سازی چطور فضای پارامتر را جستجو می‌کنند.

</div>
