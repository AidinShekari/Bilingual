# Week 8: Midterm Review: The Whole Pipeline in One Case Study · هفته‌ی 8: مرور میان‌ترم: کل مسیر مدل‌سازی در یک مطالعه‌ی موردی

> **Chapters 1–3 review** · Lecture 1 h (integrated case study) · Lab slot: **midterm exam** (90 min) + project consultation (30 min)

<div dir="rtl">

> **مرور فصل‌های 1 تا 3** · درس 1 ساعت (مطالعه‌ی موردی یکپارچه) · زمان lab: **آزمون میان‌ترم** (90 دقیقه) + مشاوره‌ی پروژه (30 دقیقه)

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| formal model / formalize | مدل فرمال / فرمال کردن | نوشتن نظریه به شکل معادله یا الگوریتم |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| parameter recovery | بازیابی پارامتر | آیا برازش، پارامترهای معلوم شبیه‌سازی را برمی‌گرداند |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| criterion (c) | ملاک | آستانه‌ی تصمیم؛ نشان‌دهنده‌ی سوگیری پاسخ |
| least squares | کمترین مربعات | روش برازش با کمینه کردن مجموع مربع خطاها |
| cross-validation (CV) | اعتبارسنجی متقابل (cross-validation) | برازش روی بخشی از داده و آزمون روی بخش کنارگذاشته |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| SSE / RMSD | مجموع مربعات خطا / ریشه‌ی میانگین مربع انحراف | معیارهای فاصله‌ی داده و پیش‌بینی |
| log-likelihood / NLL | لگاریتم درست‌نمایی / منفی آن | مقداری که بهینه‌سازها کمینه یا بیشینه می‌کنند |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| deviance (G²) | انحراف (deviance) | معیار عدم برازش نسبت به مدل اشباع‌شده |
| AIC / BIC | معیار اطلاعاتی آکائیکه / بیزی | برازش به‌علاوه‌ی جریمه برای تعداد پارامتر |
| research design | طرح آزمایش | شرایط، تعداد کوشش‌ها و نمونه‌ها |
| confusion matrix | ماتریس درهم‌ریختگی (confusion matrix) | P(مدل انتخاب‌شده | مدل مولد) |
| hit | اصابت (hit) | پاسخ «بله» وقتی علامت وجود دارد |
| response time (RT) | زمان واکنش | فاصله‌ی ارائه‌ی محرک تا پاسخ |
| signal detection theory (SDT) | نظریه‌ی تشخیص علامت | مدلی که حساسیت را از سوگیری پاسخ جدا می‌کند |
| evidence | شواهد | اطلاعاتی که برای تصمیم جمع می‌شود |
| exponential / power function | تابع نمایی / توانی | دو شکل رایج برای منحنی فراموشی و یادگیری |
| training / test data | داده‌ی آموزش / آزمون | داده‌ی برازش / داده‌ی کنارگذاشته برای سنجش |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Execute** the complete modeling pipeline (formalize → simulate → fit → evaluate → recover → interpret) on a new problem without step-by-step guidance.
2. **Select** an appropriate likelihood, fitting method and evaluation method for a given dataset, and **justify** each choice.
3. **Interpret** a set of competing model fits, information criteria and recovery results, and **write** a defensible conclusion that states its limits.
4. **Recall** and **apply** the key formulas of Weeks 1–7 (the midterm formula sheet).

<div dir="rtl">

1. کل مسیر مدل‌سازی (فرمال‌سازی ← شبیه‌سازی ← برازش ← ارزیابی ← بازیابی ← تفسیر) را روی یک مسئله‌ی جدید بدون راهنمایی قدم‌به‌قدم **اجرا کنند**.
2. درست‌نمایی، روش برازش و روش ارزیابی مناسب برای یک مجموعه‌داده را **انتخاب کنند** و هر انتخاب را **توجیه کنند**.
3. مجموعه‌ای از برازش‌های مدل‌های رقیب، معیارهای اطلاعاتی و نتایج بازیابی را **تفسیر کنند** و یک نتیجه‌گیری قابل دفاع که محدودیت‌هایش را می‌گوید **بنویسند**.
4. فرمول‌های کلیدی هفته‌های 1 تا 7 (برگه‌ی فرمول میان‌ترم) را **به خاطر بیاورند** و **به کار ببرند**.

</div>

---

## Motivation & big picture · مقدمه

Over seven weeks we built a toolkit piece by piece: formal models (Weeks 1–2), least squares and optimization (Week 3), maximum likelihood (Week 4), uncertainty and multiple participants (Week 5), cross-validation (Week 6), information criteria and recovery (Week 7). Each lab practiced one or two pieces. Real research needs all of them at once, in the right order, with judgment about what matters.

<div dir="rtl">

در هفت هفته یک جعبه‌ابزار را تکه‌تکه ساختیم: مدل‌های فرمال (هفته‌های 1–2)، کمترین مربعات و بهینه‌سازی (هفته‌ی 3)، بیشینه درست‌نمایی (هفته‌ی 4)، عدم قطعیت و چند شرکت‌کننده (هفته‌ی 5)، cross-validation (هفته‌ی 6)، معیارهای اطلاعاتی و بازیابی (هفته‌ی 7). هر lab یکی دو تکه را تمرین کرد. پژوهش واقعی همه‌ی آن‌ها را هم‌زمان، به ترتیب درست و با قضاوت درباره‌ی اینکه چه چیزی مهم است، لازم دارد.

</div>

Today's lecture runs the entire pipeline on a **new** problem: does studying a word more often make it more *memorable* (higher sensitivity), and if so, how does sensitivity grow with repetitions? The case study is also the best preparation for the midterm, which asks you to make and justify the same kinds of decisions.

<div dir="rtl">

درس امروز کل مسیر را روی یک مسئله‌ی **جدید** اجرا می‌کند: آیا مطالعه‌ی بیشتر یک کلمه آن را *به‌یادماندنی‌تر* می‌کند (حساسیت بیشتر)، و اگر بله، حساسیت با تکرارها چطور رشد می‌کند؟ این مطالعه‌ی موردی بهترین آمادگی برای میان‌ترم هم هست که از شما می‌خواهد همین نوع تصمیم‌ها را بگیرید و توجیه کنید.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

This week puts all the pieces of the first half together on one new question: *does studying a word more often make it easier to recognize later?* We write the theory as an SDT model in which sensitivity $d'$ depends on the number of repetitions. We propose three versions of that dependence (no effect, a smooth increase, any pattern), fit all three by maximum likelihood, check whether each misfits ($G^2$), compare them (LRT, AIC, BIC), check that the method works at this design (recovery), and finally interpret the winner in plain psychological language, including what the data *cannot* tell us. If you can follow this one example from start to end, you understand the first half of the course.

<div dir="rtl">

این هفته همه‌ی تکه‌های نیمه‌ی اول درس را روی یک سؤال جدید کنار هم می‌گذارد: *آیا مطالعه‌ی بیشتر یک کلمه، بازشناسی بعدی آن را آسان‌تر می‌کند؟* نظریه را به شکل یک مدل SDT می‌نویسیم که در آن حساسیت $d'$ به تعداد تکرارها بستگی دارد. سه نسخه برای این وابستگی پیشنهاد می‌کنیم (بدون اثر، افزایش هموار، هر الگویی)، هر سه را با بیشینه‌ی درست‌نمایی برازش می‌کنیم، بررسی می‌کنیم که آیا هرکدام عدم برازش دارد ($G^2$)، آن‌ها را مقایسه می‌کنیم (LRT، AIC، BIC)، بررسی می‌کنیم که روش در این طرح آزمایش کار می‌کند (بازیابی)، و در پایان مدل برنده را به زبان ساده‌ی روان‌شناختی تفسیر می‌کنیم، از جمله اینکه داده چه چیزهایی را *نمی‌تواند* به ما بگوید. اگر بتوانید این یک مثال را از اول تا آخر دنبال کنید، نیمه‌ی اول درس را فهمیده‌اید.

</div>

**Suggested timing (60 min):** concept map 10 · case study 40 · exam briefing 10.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** نقشه‌ی مفهومی 10 · مطالعه‌ی موردی 40 · توضیح آزمون 10.

</div>

### 1. Concept map of Weeks 1–7 · 1. نقشه‌ی مفهومی هفته‌های 1 تا 7

| Pipeline step | Question | Tools | Week |
|---|---|---|---|
| Formalize | What exactly does the theory claim? | Five components of a model; parameters as psychological constructs | 1–2 |
| Simulate | What can (and can't) the model do? | Forward simulation, analytic checks, prediction plots | 1–2 |
| Fit | Which parameter values best account for the data? | SSE / least squares; NLL / MLE; grid, Nelder–Mead, L-BFGS-B; multi-start; bounds and reparameterization | 3–4 |
| Quantify uncertainty | How precise are the estimates? | Hessian (Wald) SEs, profile likelihood, bootstrap | 5 |
| Evaluate (absolute) | Does the model misfit beyond noise? | Residuals, $G^2$ | 2–4 |
| Evaluate (relative) | Which model generalizes best? | CV, LRT, AIC/AICc/BIC, weights | 6–7 |
| Recover | Can the method work at this design? | Parameter recovery, model recovery (confusion and inversion matrices) | 7 |
| Interpret | What does it mean psychologically, and what can't we conclude? | Parameter meaning, design limits, aggregation artifacts | all |

<div dir="rtl">

| مرحله | سؤال | ابزارها | هفته |
|---|---|---|---|
| فرمال‌سازی | نظریه دقیقاً چه ادعایی دارد؟ | پنج جزء یک مدل؛ پارامترها به‌عنوان سازه‌های روان‌شناختی | 1–2 |
| شبیه‌سازی | مدل چه کاری می‌تواند (و نمی‌تواند) بکند؟ | شبیه‌سازی مستقیم، بررسی‌های تحلیلی، نمودار پیش‌بینی‌ها | 1–2 |
| برازش | کدام مقادیر پارامتر داده‌ها را بهتر توضیح می‌دهند؟ | SSE / کمترین مربعات؛ NLL / MLE؛ شبکه، Nelder–Mead، L-BFGS-B؛ multi-start؛ کران‌ها و reparameterization | 3–4 |
| سنجش عدم قطعیت | برآوردها چقدر دقیق‌اند؟ | SE از Hessian (Wald)، profile likelihood، bootstrap | 5 |
| ارزیابی (مطلق) | آیا عدم برازش مدل از نویز بیشتر است؟ | باقی‌مانده‌ها، $G^2$ | 2–4 |
| ارزیابی (نسبی) | کدام مدل بهتر تعمیم پیدا می‌کند؟ | CV، LRT، AIC/AICc/BIC، وزن‌ها | 6–7 |
| بازیابی | آیا روش با این طرح آزمایش می‌تواند کار کند؟ | بازیابی پارامتر، بازیابی مدل (ماتریس‌های درهم‌ریختگی و معکوس) | 7 |
| تفسیر | از نظر روان‌شناختی چه معنایی دارد و چه چیزی را نمی‌توانیم نتیجه بگیریم؟ | معنای پارامترها، محدودیت‌های طرح آزمایش، خطاهای میانگین‌گیری | همه |

</div>

**Decision guide for the likelihood:**

<div dir="rtl">

**راهنمای انتخاب درست‌نمایی:**

</div>

| Data | Natural noise model | Week |
|---|---|---|
| Counts out of $n$ (recall, hits, false alarms) | Binomial | 2, 4 |
| Single binary choices | Bernoulli | 4 |
| Continuous, roughly symmetric, equal variance (e.g., block-mean RTs) | Gaussian (= least squares) | 4–5 |

<div dir="rtl">

| داده | مدل نویز طبیعی | هفته |
|---|---|---|
| شمارش از $n$ (یادآوری، hit، false alarm) | دوجمله‌ای | 2، 4 |
| انتخاب‌های دودویی تکی | برنولی | 4 |
| پیوسته، تقریباً متقارن، با واریانس برابر (مثلاً میانگین زمان واکنش بلوک‌ها) | گاوسی (= کمترین مربعات) | 4–5 |

</div>

### 2. Case study: does repetition increase memory sensitivity? · 2. مطالعه‌ی موردی: آیا تکرار حساسیت حافظه را بالا می‌برد؟

**Design.** In a recognition-memory experiment, words are studied 1, 2 or 4 times. At test, 100 old words per repetition condition and 100 new words (lures) are presented, and the participant says "old" or "new". Because lures were never studied, there is **one** false-alarm rate, shared by all conditions, and **three** hit rates.

<div dir="rtl">

**طرح آزمایش.** در یک آزمایش حافظه‌ی بازشناسی، کلمه‌ها 1، 2 یا 4 بار مطالعه می‌شوند. در آزمون، برای هر شرط تکرار 100 کلمه‌ی قدیمی و 100 کلمه‌ی جدید (فریبنده یا lure) ارائه می‌شود و شرکت‌کننده می‌گوید «قدیمی» یا «جدید». چون کلمه‌های فریبنده هرگز مطالعه نشده‌اند، **یک** نرخ false alarm مشترک برای همه‌ی شرایط و **سه** نرخ hit داریم.

</div>

**Formalization (SDT with an absolute criterion).** New words produce evidence $X \sim \mathcal{N}(0, 1)$; old words studied $r$ times produce $X \sim \mathcal{N}(d'_r, 1)$; the participant says "old" if $X > \kappa$, with one criterion $\kappa$ for all test items (they are intermixed, so the participant cannot know an item's condition). Then

<div dir="rtl">

**فرمال‌سازی (SDT با ملاک مطلق).** کلمه‌های جدید شواهد $X \sim \mathcal{N}(0, 1)$ و کلمه‌های قدیمی‌ای که $r$ بار مطالعه شده‌اند $X \sim \mathcal{N}(d'_r, 1)$ تولید می‌کنند؛ شرکت‌کننده اگر $X > \kappa$ باشد می‌گوید «قدیمی»، با یک ملاک $\kappa$ برای همه‌ی آیتم‌های آزمون (آیتم‌ها در هم آمیخته‌اند، پس شرکت‌کننده نمی‌داند هر آیتم از کدام شرط است). پس

</div>

$$
H_r = \Phi(d'_r - \kappa), \qquad F = \Phi(-\kappa).
$$

**Three candidate models of how $d'$ depends on repetitions:**

<div dir="rtl">

**سه مدل رقیب برای وابستگی $d'$ به تکرارها:**

</div>

| Model | $d'_r$ | $k$ | Claim |
|---|---|---|---|
| $\mathcal{M}_0$ (no effect) | $\delta_0$ | 2 | Repetition does not change sensitivity |
| $\mathcal{M}_1$ (log-linear) | $\delta_0 + \delta_1 \log_2 r$ | 3 | Each *doubling* of study adds the same sensitivity |
| $\mathcal{M}_2$ (free) | $d'_1, d'_2, d'_4$ | 4 | Any pattern (saturated: 4 parameters for 4 rates) |

<div dir="rtl">

| مدل | $d'_r$ | $k$ | ادعا |
|---|---|---|---|
| $\mathcal{M}_0$ (بی‌اثر) | $\delta_0$ | 2 | تکرار حساسیت را تغییر نمی‌دهد |
| $\mathcal{M}_1$ (خطی–لگاریتمی) | $\delta_0 + \delta_1 \log_2 r$ | 3 | هر *دو برابر شدن* مطالعه همان مقدار حساسیت اضافه می‌کند |
| $\mathcal{M}_2$ (آزاد) | $d'_1, d'_2, d'_4$ | 4 | هر الگویی (اشباع‌شده: 4 پارامتر برای 4 نرخ) |

</div>

$\mathcal{M}_0 \subset \mathcal{M}_1 \subset \mathcal{M}_2$, so all pairs are nested.

<div dir="rtl">

$\mathcal{M}_0 \subset \mathcal{M}_1 \subset \mathcal{M}_2$، پس همه‌ی جفت‌ها nested هستند.

</div>

**Likelihood.** Binomial for each of the four counts (three hit counts, one false-alarm count).

<div dir="rtl">

**درست‌نمایی.** دوجمله‌ای برای هر یک از چهار شمارش (سه شمارش hit، یک شمارش false alarm).

</div>

The lab code below runs every step. Students run it at home as exam preparation; the lecture walks through the outputs.

<div dir="rtl">

کد lab در ادامه همه‌ی مراحل را اجرا می‌کند. دانشجویان آن را برای آمادگی آزمون در خانه اجرا می‌کنند؛ در درس خروجی‌ها مرور می‌شوند.

</div>

#### Reading the math · خواندن ریاضی

- $H_r = \Phi(d'_r - \kappa)$ and $F = \Phi(-\kappa)$: the same SDT as Week 2, but the criterion is written as an **absolute** position $\kappa$ on the evidence axis (measured from the center of the "new word" curve) instead of relative to the midpoint. New words: curve at 0, so $F$ is the area right of $\kappa$, i.e. $\Phi(-\kappa)$. Old words studied $r$ times: curve at $d'_r$, so $H_r = \Phi(d'_r - \kappa)$.
- One $\kappa$ for all conditions: all test words are mixed together, so the participant cannot use a different threshold for words studied once and words studied four times.
- $\log_2 r$: the base-2 logarithm, so $\log_2 1 = 0$, $\log_2 2 = 1$, $\log_2 4 = 2$. In model $\mathcal{M}_1$, $d'_r = \delta_0 + \delta_1\log_2 r$ means: $\delta_0$ is the sensitivity after one study, and every *doubling* of study adds $\delta_1$.
- **Numbers from the worked example:** $\hat\kappa = 1.04$ gives $F = \Phi(-1.04) = 0.15$ ✓. With $\hat d'_1 = 0.82$: $H_1 = \Phi(0.82 - 1.04) = \Phi(-0.22) = 0.41$, close to the observed 0.40 ✓.

<div dir="rtl">

- $H_r = \Phi(d'_r - \kappa)$ و $F = \Phi(-\kappa)$: همان SDT هفته‌ی 2، ولی ملاک به‌صورت یک موقعیت **مطلق** $\kappa$ روی محور شواهد نوشته شده (از مرکز منحنی «کلمه‌ی جدید» سنجیده می‌شود) به جای اینکه نسبت به نقطه‌ی وسط سنجیده شود. کلمه‌های جدید: منحنی در 0، پس $F$ مساحت سمت راست $\kappa$ است، یعنی $\Phi(-\kappa)$. کلمه‌های قدیمی که $r$ بار مطالعه شده‌اند: منحنی در $d'_r$، پس $H_r = \Phi(d'_r - \kappa)$.
- یک $\kappa$ برای همه‌ی شرایط: همه‌ی کلمه‌های آزمون با هم مخلوط‌اند، پس شرکت‌کننده نمی‌تواند برای کلمه‌هایی که یک بار و کلمه‌هایی که چهار بار مطالعه شده‌اند آستانه‌ی متفاوتی به کار ببرد.
- $\log_2 r$: لگاریتم در پایه‌ی 2، پس $\log_2 1 = 0$، $\log_2 2 = 1$ و $\log_2 4 = 2$. در مدل $\mathcal{M}_1$، $d'_r = \delta_0 + \delta_1\log_2 r$ یعنی: $\delta_0$ حساسیت بعد از یک بار مطالعه است، و هر *دو برابر* شدن مطالعه $\delta_1$ اضافه می‌کند.
- **عددهای مثال حل‌شده:** $\hat\kappa = 1.04$ می‌دهد $F = \Phi(-1.04) = 0.15$ ✓. با $\hat d'_1 = 0.82$: $H_1 = \Phi(0.82 - 1.04) = \Phi(-0.22) = 0.41$، نزدیک مقدار مشاهده‌شده‌ی 0.40 ✓.

</div>

#### For an engineer · برای یک مهندس

The pipeline of the concept map is the **system identification** workflow you know: choose candidate model structures, estimate parameters (ML), validate (residual tests ≈ $G^2$), select the model order (LRT/AIC/BIC ≈ GLRT/AIC/MDL), and verify the procedure on simulated data with known truth (recovery). Two differences deserve emphasis in class: the "system" is a person whose parameters are themselves the scientific result, and the amount of data is tiny by engineering standards (400 binary responses), so uncertainty and recovery matter much more.

<div dir="rtl">

مسیر نقشه‌ی مفهومی همان روند **شناسایی سیستم (system identification)** است که می‌شناسید: ساختارهای مدل نامزد را انتخاب کن، پارامترها را تخمین بزن (ML)، اعتبارسنجی کن (آزمون باقی‌مانده‌ها ≈ $G^2$)، مرتبه‌ی مدل را انتخاب کن (LRT/AIC/BIC ≈ GLRT/AIC/MDL)، و روش را روی داده‌ی شبیه‌سازی‌شده با حقیقت معلوم وارسی کن (بازیابی). دو تفاوت ارزش تأکید در کلاس را دارند: «سیستم» یک آدم است که خود پارامترهایش نتیجه‌ی علمی‌اند، و مقدار داده با معیارهای مهندسی خیلی کم است (400 پاسخ دودویی)، پس عدم قطعیت و بازیابی خیلی مهم‌ترند.

</div>

#### For the instructor · برای مدرس

- **Use the concept-map table as the backbone of the session.** For each row, point to the corresponding output of the case study (e.g. "Evaluate (absolute)" → the $G^2$ column). Students see that every tool has a place.
- **Ask the class to interpret before you do.** Show the results table without the interpretation paragraph and let small groups write two sentences: "what do we conclude, and what can't we conclude?" Then compare with the text. This is exactly the skill the midterm tests.
- **Exam briefing:** tell students that the exam rewards *justified decisions* (which likelihood, which criterion, why recovery matters) more than computation. Show one past-style question from the "Check your understanding" section.
- **Project consultation (lab slot):** ask each team three questions: What is your cognitive question? Which parameter or model comparison answers it? Can your design recover it? Most weak proposals fail on the third.

<div dir="rtl">

- **جدول نقشه‌ی مفهومی را ستون اصلی جلسه کنید.** برای هر سطر، خروجی متناظر در مطالعه‌ی موردی را نشان دهید (مثلاً «ارزیابی مطلق» ← ستون $G^2$). دانشجوها می‌بینند هر ابزار جایی دارد.
- **پیش از خودتان از کلاس بخواهید تفسیر کند.** جدول نتایج را بدون پاراگراف تفسیر نشان دهید و بگذارید گروه‌های کوچک دو جمله بنویسند: «چه نتیجه‌ای می‌گیریم و چه نتیجه‌ای نمی‌توانیم بگیریم؟» بعد با متن مقایسه کنید. این دقیقاً مهارتی است که میان‌ترم می‌سنجد.
- **توضیح امتحان:** به دانشجوها بگویید امتحان به *تصمیم‌های مستدل* (کدام درست‌نمایی، کدام معیار، چرا بازیابی مهم است) بیشتر از محاسبه نمره می‌دهد. یک سؤال به سبک امتحان از بخش خودآزمایی نشان دهید.
- **مشاوره‌ی پروژه (وقت lab):** از هر تیم سه سؤال بپرسید: سؤال شناختی شما چیست؟ کدام پارامتر یا مقایسه‌ی مدل به آن جواب می‌دهد؟ آیا طرح آزمایش شما می‌تواند آن را بازیابی کند؟ بیشتر پیشنهادهای ضعیف در سؤال سوم شکست می‌خورند.

</div>

---

## Worked example · مثال حل‌شده

The case-study results for one simulated participant (true model $\mathcal{M}_1$ with $\delta_0 = 0.8$, $\delta_1 = 0.6$, $\kappa = 1.0$), from the code in the lab section. Numbers are rounded.

<div dir="rtl">

نتایج مطالعه‌ی موردی برای یک شرکت‌کننده‌ی شبیه‌سازی‌شده (مدل واقعی $\mathcal{M}_1$ با $\delta_0 = 0.8$، $\delta_1 = 0.6$، $\kappa = 1.0$)، از کد بخش lab. اعداد گرد شده‌اند.

</div>

**Step 1: data.**

<div dir="rtl">

**قدم 1: داده.**

</div>

| Condition | Old words | "Old" responses | Rate |
|---|---|---|---|
| $r = 1$ | 100 | 40 | 0.40 |
| $r = 2$ | 100 | 66 | 0.66 |
| $r = 4$ | 100 | 80 | 0.80 |
| New (lures) | 100 | 15 | 0.15 |

<div dir="rtl">

| شرط | کلمه‌های قدیمی | پاسخ «قدیمی» | نرخ |
|---|---|---|---|
| $r = 1$ | 100 | 40 | 0.40 |
| $r = 2$ | 100 | 66 | 0.66 |
| $r = 4$ | 100 | 80 | 0.80 |
| جدید (فریبنده) | 100 | 15 | 0.15 |

</div>

**Step 2: fit and evaluate** (MLE, $N = 400$ responses):

<div dir="rtl">

**قدم 2: برازش و ارزیابی** (MLE، $N = 400$ پاسخ):

</div>

| Model | $k$ | NLL | $G^2$ (df, $p$) | AIC | BIC | $w_{\text{AIC}}$ | $w_{\text{BIC}}$ | $\hat d'_{1,2,4}$ | $\hat\kappa$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mathcal{M}_0$ none | 2 | 27.27 | 35.55 (2, < .001) | 58.54 | 66.52 | 0.00 | 0.00 | 1.34, 1.34, 1.34 | 1.04 |
| $\mathcal{M}_1$ log-linear | 3 | 9.77 | 0.54 (1, .46) | **25.53** | **37.51** | **0.67** | **0.94** | 0.82, 1.37, 1.93 | 1.04 |
| $\mathcal{M}_2$ free | 4 | 9.50 | 0 (saturated) | 26.99 | 42.96 | 0.33 | 0.06 | 0.78, 1.45, 1.88 | 1.04 |

<div dir="rtl">

| مدل | $k$ | NLL | $G^2$ (df، $p$) | AIC | BIC | $w_{\text{AIC}}$ | $w_{\text{BIC}}$ | $\hat d'_{1,2,4}$ | $\hat\kappa$ |
|---|---|---|---|---|---|---|---|---|---|
| $\mathcal{M}_0$ بی‌اثر | 2 | 27.27 | 35.55 (2، < .001) | 58.54 | 66.52 | 0.00 | 0.00 | 1.34، 1.34، 1.34 | 1.04 |
| $\mathcal{M}_1$ خطی–لگاریتمی | 3 | 9.77 | 0.54 (1، .46) | **25.53** | **37.51** | **0.67** | **0.94** | 0.82، 1.37، 1.93 | 1.04 |
| $\mathcal{M}_2$ آزاد | 4 | 9.50 | 0 (اشباع‌شده) | 26.99 | 42.96 | 0.33 | 0.06 | 0.78، 1.45، 1.88 | 1.04 |

</div>

Likelihood-ratio tests: $\mathcal{M}_0$ vs. $\mathcal{M}_1$: $\Lambda = 35.01$, df = 1, $p < .001$; $\mathcal{M}_1$ vs. $\mathcal{M}_2$: $\Lambda = 0.54$, df = 1, $p = .46$.

<div dir="rtl">

آزمون‌های نسبت درست‌نمایی: $\mathcal{M}_0$ در برابر $\mathcal{M}_1$: $\Lambda = 35.01$، df = 1، $p < .001$؛ $\mathcal{M}_1$ در برابر $\mathcal{M}_2$: $\Lambda = 0.54$، df = 1، $p = .46$.

</div>

**Recovery at this design** (lab code, second block): $\mathcal{M}_1$'s parameters are well recovered ($r = 0.89$–$0.93$), and BIC identifies the generating model in 87–98% of simulations.

<div dir="rtl">

**بازیابی با این طرح آزمایش** (کد lab، بلوک دوم): پارامترهای $\mathcal{M}_1$ خوب بازیابی می‌شوند ($r = 0.89$ تا $0.93$) و BIC مدل تولیدکننده را در 87 تا 98 درصد شبیه‌سازی‌ها شناسایی می‌کند.

</div>

**Step 3: interpret.** Repetition clearly increases sensitivity: the no-effect model misfits badly ($G^2 = 35.5$, $p < .001$) and is rejected by every criterion. The log-linear model fits as well as the saturated model (LRT $p = .46$) with one parameter fewer, and both AIC and BIC prefer it. Its estimate $\hat\delta_1 \approx 0.55$ means each doubling of study adds roughly half a $d'$ unit. Recovery results show that, at this design, both the parameters and the model choice can be trusted. Caveats: this is one simulated participant; with only three repetition levels, a log-linear trend cannot be distinguished from many other increasing curves (e.g., a power function of $r$); and a single criterion $\kappa$ assumes the participant cannot tell how often an item was studied before responding.

<div dir="rtl">

**قدم 3: تفسیر.** تکرار به‌وضوح حساسیت را بالا می‌برد: مدل بی‌اثر به‌شدت بد برازش می‌شود ($G^2 = 35.5$، $p < .001$) و همه‌ی معیارها آن را رد می‌کنند. مدل خطی–لگاریتمی با یک پارامتر کمتر به خوبی مدل اشباع‌شده برازش می‌شود (LRT با $p = .46$) و هم AIC و هم BIC آن را ترجیح می‌دهند. برآورد $\hat\delta_1 \approx 0.55$ یعنی هر دو برابر شدن مطالعه تقریباً نیم واحد $d'$ اضافه می‌کند. نتایج بازیابی نشان می‌دهد که با این طرح آزمایش، هم به پارامترها و هم به انتخاب مدل می‌شود اعتماد کرد. هشدارها: این یک شرکت‌کننده‌ی شبیه‌سازی‌شده است؛ با فقط سه سطح تکرار، یک روند خطی–لگاریتمی را نمی‌شود از خیلی منحنی‌های صعودی دیگر (مثلاً یک تابع توانی از $r$) جدا کرد؛ و یک ملاک واحد $\kappa$ فرض می‌کند شرکت‌کننده پیش از پاسخ نمی‌داند یک آیتم چند بار مطالعه شده است.

</div>

---

## Lab (2 hours): midterm exam + project consultation · lab (2 ساعت): آزمون میان‌ترم + مشاوره‌ی پروژه

### Midterm exam (90 minutes, in the lab slot) · آزمون میان‌ترم (90 دقیقه، در زمان lab)

- **Format:** written, closed book. A **formula sheet** (below) is provided. No laptops: questions involve reading short code fragments and interpreting outputs, not writing code from scratch.
- **Coverage:** Weeks 1–7 (Chapters 1–3), with the emphasis on *understanding and interpretation* (the course's specific goal 2).
- **Question types:** (1) short conceptual questions; (2) one calculation by hand (e.g., $d'$ and $c$, a likelihood or NLL, AIC/BIC and weights); (3) reading code and predicting or explaining its output; (4) interpreting a fit table, a residual plot or a recovery/confusion matrix; (5) one short design question ("what would you change, and why?").
- **Weight:** 3 of 20 points.
- The midterm exam itself, with model answers, is in the course assessments (Stage 3 materials).

<div dir="rtl">

- **شکل:** کتبی، کتاب‌بسته. یک **برگه‌ی فرمول** (در ادامه) داده می‌شود. بدون لپ‌تاپ: سؤال‌ها شامل خواندن تکه‌کدهای کوتاه و تفسیر خروجی‌هاست، نه نوشتن کد از صفر.
- **محدوده:** هفته‌های 1 تا 7 (فصل‌های 1 تا 3)، با تأکید بر *فهم و تفسیر* (هدف ویژه‌ی 2 درس).
- **انواع سؤال:** (1) سؤال‌های مفهومی کوتاه؛ (2) یک محاسبه‌ی دستی (مثلاً $d'$ و $c$، یک درست‌نمایی یا NLL، AIC/BIC و وزن‌ها)؛ (3) خواندن کد و پیش‌بینی یا توضیح خروجی آن؛ (4) تفسیر یک جدول برازش، نمودار باقی‌مانده‌ها یا ماتریس بازیابی/درهم‌ریختگی؛ (5) یک سؤال کوتاه طراحی («چه چیزی را تغییر می‌دادید و چرا؟»).
- **وزن:** 3 نمره از 20.
- خود آزمون میان‌ترم با پاسخ‌های نمونه در مواد ارزشیابی درس آمده است.

</div>

**Formula sheet provided at the exam:**

<div dir="rtl">

**برگه‌ی فرمولی که در آزمون داده می‌شود:**

</div>

$$
\begin{aligned}
&d' = \Phi^{-1}(H) - \Phi^{-1}(F), \quad c = -\tfrac12[\Phi^{-1}(H) + \Phi^{-1}(F)], \quad H = \Phi(d'/2 - c), \quad F = \Phi(-d'/2 - c)\\
&f_{\exp}(t) = A e^{-\lambda t}, \quad f_{\text{pow}}(t) = A(1+t)^{-d}, \quad P_c^{\text{RW}} = \frac{1-r^z}{1-r^a},\ r = \frac{1-v}{1+v}, \quad \mathbb{E}[T] = \frac{aP_c - z}{v}\\
&\mathrm{SSE} = \textstyle\sum_i (y_i - \hat y_i)^2, \quad \mathrm{RMSD} = \sqrt{\mathrm{SSE}/N}\\
&\ell(\boldsymbol\theta) = \textstyle\sum_i \big[\ln\binom{n_i}{y_i} + y_i\ln f_i + (n_i - y_i)\ln(1-f_i)\big], \quad \mathrm{NLL} = -\ell\\
&G^2 = 2(\ell_{\text{sat}} - \hat\ell), \quad \Lambda = 2(\hat\ell_1 - \hat\ell_0) \sim \chi^2_{\Delta k}\\
&\mathrm{SE} \approx \sqrt{\mathrm{diag}(\mathbf{H}^{-1})}, \quad \text{Wald CI: } \hat\theta \pm 1.96\,\mathrm{SE}, \quad \text{profile CI: } 2(\mathrm{NLL}_{\text{prof}} - \mathrm{NLL}_{\min}) \le 3.84\\
&\mathrm{AIC} = 2\,\mathrm{NLL} + 2k, \quad \mathrm{AICc} = \mathrm{AIC} + \tfrac{2k(k+1)}{N-k-1}, \quad \mathrm{BIC} = 2\,\mathrm{NLL} + k\ln N, \quad w_i = \tfrac{e^{-\Delta_i/2}}{\sum_j e^{-\Delta_j/2}}
\end{aligned}
$$

Critical values: $\chi^2_{1,.95} = 3.84$, $\chi^2_{2,.95} = 5.99$, $\chi^2_{3,.95} = 7.81$. Quantiles: $\Phi^{-1}(0.84) \approx 1.0$, $\Phi^{-1}(0.975) = 1.96$. Logs: $\ln 2 = 0.693$, $\ln 10 = 2.303$, $\ln 100 = 4.605$, $\ln 400 = 5.991$.

<div dir="rtl">

مقادیر بحرانی: $\chi^2_{1,.95} = 3.84$، $\chi^2_{2,.95} = 5.99$، $\chi^2_{3,.95} = 7.81$. quantileها: $\Phi^{-1}(0.84) \approx 1.0$، $\Phi^{-1}(0.975) = 1.96$. لگاریتم‌ها: $\ln 2 = 0.693$، $\ln 10 = 2.303$، $\ln 100 = 4.605$، $\ln 400 = 5.991$.

</div>

### Project consultation (30 minutes, after the exam) · مشاوره‌ی پروژه (30 دقیقه، بعد از آزمون)

Teams meet the instructor or TA for 5–10 minutes each to discuss their project idea before the proposal deadline (start of Week 9). Bring a one-paragraph description of your question, model and data.

<div dir="rtl">

هر گروه 5 تا 10 دقیقه با مدرس یا دستیار آموزشی درباره‌ی ایده‌ی پروژه‌اش پیش از موعد پیشنهاد (ابتدای هفته‌ی 9) صحبت می‌کند. یک پاراگراف توصیف از سؤال، مدل و داده‌تان بیاورید.

</div>

### Self-study: the case study in code (run before the exam) · مطالعه‌ی شخصی: مطالعه‌ی موردی در کد (پیش از آزمون اجرا کنید)

> **Code · کد:** [`code/week08.py`](code/week08.py), cell 1 · سلول 1

> **Code · کد:** [`code/week08.py`](code/week08.py), cell 2 · سلول 2

**Expected output (first block):**

<div dir="rtl">

**خروجی مورد انتظار (بلوک اول):**

</div>

```text
hits per condition: [40 66 80]  false alarms: 15
           k     NLL      G2  df  p(G2)     AIC     BIC            d'_1,2,4  kappa  w_AIC  w_BIC
model
M0_none    2  27.269  35.549   2  0.000  58.538  66.521  [1.34, 1.34, 1.34]   1.04  0.000  0.000
M1_loglin  3   9.766   0.543   1  0.461  25.533  37.507  [0.82, 1.37, 1.93]   1.04  0.674  0.938
M2_free    4   9.495   0.000   0    NaN  26.990  42.956  [0.78, 1.45, 1.88]   1.04  0.326  0.062

LRT M0 vs M1: 35.01 (df 1, p = 0.0000);  M1 vs M2: 0.54 (df 1, p = 0.461)
```

**Expected output (second block, about 1 minute):**

<div dir="rtl">

**خروجی مورد انتظار (بلوک دوم، حدود 1 دقیقه):**

</div>

```text
M1 recovery delta0 : r = 0.895, RMSE = 0.181
M1 recovery delta1 : r = 0.930, RMSE = 0.113
M1 recovery kappa  : r = 0.887, RMSE = 0.142

BIC model recovery, P(selected | generated):
           M0_none  M1_loglin  M2_free
M0_none       0.98       0.02     0.00
M1_loglin     0.05       0.93     0.02
M2_free       0.10       0.03     0.87
```

Note on the $\mathcal{M}_2$ generator in model recovery: its three $d'$ values are drawn so that $d'_4$ lies *between* $d'_1$ and $d'_2$, a non-monotone pattern that $\mathcal{M}_1$ cannot produce. Otherwise $\mathcal{M}_2$ data would often be perfectly consistent with $\mathcal{M}_1$, and "confusions" would be meaningless.

<div dir="rtl">

یادداشت درباره‌ی مولد $\mathcal{M}_2$ در بازیابی مدل: سه مقدار $d'$ آن طوری کشیده می‌شوند که $d'_4$ *بین* $d'_1$ و $d'_2$ قرار بگیرد؛ یک الگوی غیریکنوا که $\mathcal{M}_1$ نمی‌تواند تولید کند. در غیر این صورت داده‌های $\mathcal{M}_2$ اغلب کاملاً با $\mathcal{M}_1$ سازگار می‌بودند و «اشتباه گرفتن‌ها» بی‌معنی می‌شد.

</div>

**Self-check questions on the case study** (discussed in the lecture):
1. Why is there only one false-alarm rate, and how does that change the SDT model compared with Week 2?
2. Which model does each criterion favor, and do the LRTs agree?
3. Is $\delta_1$ recoverable at this design? Is $\mathcal{M}_1$ distinguishable from $\mathcal{M}_0$ and $\mathcal{M}_2$?
4. Write the one-sentence psychological conclusion, with its main caveat.

<div dir="rtl">

**سؤال‌های خودسنجی درباره‌ی مطالعه‌ی موردی** (در درس بحث می‌شوند):
1. چرا فقط یک نرخ false alarm داریم، و این مدل SDT را در مقایسه با هفته‌ی 2 چطور تغییر می‌دهد؟
2. هر معیار کدام مدل را ترجیح می‌دهد، و آیا LRTها با آن موافق‌اند؟
3. آیا $\delta_1$ با این طرح آزمایش قابل بازیابی است؟ آیا $\mathcal{M}_1$ از $\mathcal{M}_0$ و $\mathcal{M}_2$ قابل تشخیص است؟
4. نتیجه‌ی روان‌شناختی را در یک جمله، همراه با مهم‌ترین هشدارش، بنویسید.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Chatbots as study partners: trust, but verify.** Many students use LLMs to explain concepts and check exam answers. That can help, but LLMs can produce fluent, confident and wrong calculations. Treat a chatbot's answer as you would a model's prediction: check it against something you can compute. The code below checks a pre-made chatbot answer to midterm question B3 (AIC for three models). The chatbot used $2\,\mathrm{NLL} + k$ instead of $2\,\mathrm{NLL} + 2k$.

<div dir="rtl">

**chatbot به‌عنوان هم‌درس: اعتماد کن، ولی بررسی کن.** بسیاری از دانشجوها از LLMها برای توضیح مفاهیم و بررسی جواب‌های امتحانی استفاده می‌کنند. این می‌تواند کمک کند، ولی LLMها می‌توانند محاسبه‌هایی روان، مطمئن و غلط تولید کنند. با جواب یک chatbot مثل پیش‌بینی یک مدل رفتار کنید: آن را با چیزی که خودتان می‌توانید حساب کنید بسنجید. کد پایین یک جواب ازپیش‌آماده‌ی chatbot به سؤال B3 میان‌ترم (AIC برای سه مدل) را بررسی می‌کند. chatbot به جای $2\,\mathrm{NLL} + 2k$ از $2\,\mathrm{NLL} + k$ استفاده کرده.

</div>

> **Code · کد:** [`code/week08.py`](code/week08.py), cell 3 · سلول 3

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
M1: chatbot 222.0, correct 224.0  WRONG
M2: chatbot 218.0, correct 221.0  WRONG
M3: chatbot 218.8, correct 223.8  WRONG
Akaike weights, chatbot: [0.07 0.55 0.37]  correct: [0.15 0.68 0.17]
```

The chatbot happens to pick the right winner ($\mathcal{M}_2$), but every number is wrong, and it doubles the support for the most complex model. A grader would give little credit, and in a real analysis the error would favor overfitting.

<div dir="rtl">

chatbot اتفاقاً برنده‌ی درست ($\mathcal{M}_2$) را انتخاب می‌کند، ولی همه‌ی عددها غلط‌اند و پشتیبانی از پیچیده‌ترین مدل را دو برابر می‌کند. مصحح نمره‌ی کمی می‌داد، و در یک تحلیل واقعی این خطا به نفع overfitting تمام می‌شد.

</div>

**Try it (no API needed).**
- ★ Which error in the formula produces exactly the chatbot's numbers? What would BIC look like with the same error?
- ★★ Write three small "test cases" (inputs with known answers) for the SDT formulas of Week 2 that you could use to check any answer, from a chatbot or a classmate.
- Reminder: no AI tools are allowed in the exam itself, and the course policy on AI use for assignments is in `assessments/README.md`.

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ کدام خطا در فرمول دقیقاً عددهای chatbot را تولید می‌کند؟ BIC با همین خطا چه شکلی می‌شد؟
- ★★ سه «مورد آزمون» (ورودی با جواب معلوم) کوچک برای فرمول‌های SDT هفته‌ی 2 بنویسید که بتوانید با آن هر جوابی را، چه از chatbot چه از هم‌کلاسی، بررسی کنید.
- یادآوری: در خود امتحان هیچ ابزار هوش مصنوعی مجاز نیست، و قانون درس درباره‌ی استفاده از هوش مصنوعی در تکلیف‌ها در `assessments/README.md` آمده است.

</div>

---

## Common mistakes & misconceptions (top 10 from Weeks 1–7) · اشتباهات رایج و برداشت‌های نادرست (10 مورد اول از هفته‌های 1 تا 7)

1. Treating a good fit as evidence that a model is true (Weeks 3, 6).
2. Forgetting the minus sign: optimizers minimize the **negative** log-likelihood (Week 4).
3. Not clipping probabilities, so $\ln 0$ crashes the fit (Week 4).
4. Trusting `success=True`, a single start, or a bounded Nelder–Mead that has collapsed against a bound (Weeks 3–4).
5. Least squares for counts or choices without thinking about the noise model (Weeks 3–4).
6. Reporting estimates without uncertainty, or using Wald intervals near bounds (Week 5).
7. Drawing conclusions about individuals from averaged curves (Week 5).
8. Leaking test data into training in cross-validation (Week 6).
9. Comparing non-nested models with an LRT, or reading AIC values on their own instead of as differences (Week 7).
10. Interpreting parameters or model comparisons without a recovery study at the actual design (Week 7).

<div dir="rtl">

1. برازش خوب را شاهد درستی مدل دانستن (هفته‌های 3، 6).
2. فراموش کردن علامت منفی: بهینه‌سازها **منفی** لگاریتم درست‌نمایی را کمینه می‌کنند (هفته‌ی 4).
3. محدود نکردن احتمال‌ها، که باعث می‌شود $\ln 0$ برازش را از کار بیندازد (هفته‌ی 4).
4. اعتماد به `success=True`، یک شروع تنها، یا Nelder–Mead کران‌داری که روی یک کران فرو ریخته است (هفته‌های 3–4).
5. کمترین مربعات برای شمارش‌ها یا انتخاب‌ها بدون فکر کردن به مدل نویز (هفته‌های 3–4).
6. گزارش برآوردها بدون عدم قطعیت، یا استفاده از بازه‌های Wald نزدیک کران‌ها (هفته‌ی 5).
7. نتیجه‌گیری درباره‌ی افراد از منحنی‌های میانگین‌گیری‌شده (هفته‌ی 5).
8. نشت داده‌ی آزمون به آموزش در cross-validation (هفته‌ی 6).
9. مقایسه‌ی مدل‌های non-nested با LRT، یا خواندن مقادیر AIC به‌تنهایی به‌جای تفاوت‌هایشان (هفته‌ی 7).
10. تفسیر پارامترها یا مقایسه‌ی مدل‌ها بدون مطالعه‌ی بازیابی با طرح آزمایش واقعی (هفته‌ی 7).

</div>

---

## Check your understanding (practice questions in exam style) · خودآزمایی (سؤال‌های تمرینی به سبک آزمون)

**1. (Concept)** Explain in three sentences why the exponential-with-asymptote model fitted the Week 2 data better than the power model, although the power model generated the data.
<details><summary>Answer</summary>
The asymptote model has an extra parameter, so it can adapt to the particular noise of the sample, here the flat-looking long-delay points. Better training fit is guaranteed for more flexible models and is not evidence of truth. Generalization measures (CV, AIC/BIC) and recovery studies are needed to judge it.
</details>

<div dir="rtl">

**1. (مفهومی)** در سه جمله توضیح دهید چرا مدل نمایی با مجانب داده‌های هفته‌ی 2 را بهتر از مدل توانی برازش کرد، با اینکه مدل توانی داده را تولید کرده بود.
<details><summary>پاسخ</summary>
مدل مجانبی یک پارامتر اضافه دارد، پس می‌تواند خودش را با نویز خاص نمونه، اینجا نقاط صاف‌نمای فاصله‌های طولانی، تطبیق دهد. برازش آموزش بهتر برای مدل‌های منعطف‌تر تضمین‌شده است و شاهد درستی نیست. برای قضاوت به معیارهای تعمیم (CV، AIC/BIC) و مطالعات بازیابی نیاز داریم.
</details>

</div>

**2. (Calculation)** An observer has $H = 0.84$ and $F = 0.16$. Compute $d'$ and $c$ (use $\Phi^{-1}(0.84) \approx 1.0$).
<details><summary>Answer</summary>
$d' = 1.0 - (-1.0) = 2.0$; $c = -\tfrac12(1.0 + (-1.0)) = 0$, so the observer is unbiased.
</details>

<div dir="rtl">

**2. (محاسبه)** یک مشاهده‌گر $H = 0.84$ و $F = 0.16$ دارد. $d'$ و $c$ را حساب کنید (از $\Phi^{-1}(0.84) \approx 1.0$ استفاده کنید).
<details><summary>پاسخ</summary>
$d' = 1.0 - (-1.0) = 2.0$؛ $c = -\tfrac12(1.0 + (-1.0)) = 0$، پس مشاهده‌گر بی‌سوگیری است.
</details>

</div>

**3. (Calculation)** Two models are fitted to $N = 100$ binary responses. Model A: $k = 2$, NLL = 60.0. Model B: $k = 4$, NLL = 57.5. Compute AIC and BIC for both. Which does each criterion prefer? ($\ln 100 = 4.605$)
<details><summary>Answer</summary>
AIC: A = 124.0, B = 123.0, so AIC prefers B (slightly). BIC: A = 120 + 9.21 = 129.21; B = 115 + 18.42 = 133.42, so BIC prefers A. The criteria disagree because BIC penalizes each parameter by 4.6 instead of 2.
</details>

<div dir="rtl">

**3. (محاسبه)** دو مدل روی $N = 100$ پاسخ دودویی برازش شده‌اند. مدل A: $k = 2$، NLL = 60.0. مدل B: $k = 4$، NLL = 57.5. AIC و BIC هر دو را حساب کنید. هر معیار کدام را ترجیح می‌دهد؟ ($\ln 100 = 4.605$)
<details><summary>پاسخ</summary>
AIC: A = 124.0، B = 123.0، پس AIC (کمی) B را ترجیح می‌دهد. BIC: A = 120 + 9.21 = 129.21؛ B = 115 + 18.42 = 133.42، پس BIC A را ترجیح می‌دهد. معیارها با هم مخالف‌اند چون BIC هر پارامتر را 4.6 به‌جای 2 جریمه می‌کند.
</details>

</div>

**4. (Code reading)** What is wrong with this NLL function, and what will the optimizer do?

<div dir="rtl">

**4. (خواندن کد)** این تابع NLL چه اشکالی دارد و بهینه‌ساز چه خواهد کرد؟

</div>

> **Code · کد:** [`code/week08.py`](code/week08.py), cell 4 · سلول 4

<details><summary>Answer</summary>
(i) It returns the log-likelihood, not its negative, so `minimize` will drive the parameters toward the *worst* fit (log-likelihood toward −∞). (ii) `p` is not clipped, so predicted values of 0 or above 1 give −inf or nan. Fix: `return -np.sum(binom.logpmf(y, n, np.clip(p, EPS, 1 - EPS)))`.
</details>

<div dir="rtl">

<details><summary>پاسخ</summary>
(1) لگاریتم درست‌نمایی را برمی‌گرداند نه منفی آن را، پس `minimize` پارامترها را به سمت *بدترین* برازش (لگاریتم درست‌نمایی به سمت −∞) می‌برد. (2) `p` محدود نشده، پس مقادیر پیش‌بینی‌شده‌ی 0 یا بیشتر از 1 مقدار −inf یا nan می‌دهند. اصلاح: `return -np.sum(binom.logpmf(y, n, np.clip(p, EPS, 1 - EPS)))`.
</details>

</div>

**5. (Interpretation)** A recovery study gives $r(\text{true}, \text{recovered}) = 0.95$ for parameter $A$ and $0.35$ for parameter $B$. What do you conclude about a paper reporting group differences in $B$ at this design?
<details><summary>Answer</summary>
$B$ is poorly recoverable at this design: estimates are dominated by noise or trade-offs, so group differences in estimated $B$ are not interpretable. The paper should improve the design or not interpret $B$.
</details>

<div dir="rtl">

**5. (تفسیر)** یک مطالعه‌ی بازیابی برای پارامتر $A$ مقدار $r(\text{true}, \text{recovered}) = 0.95$ و برای پارامتر $B$ مقدار $0.35$ می‌دهد. درباره‌ی مقاله‌ای که با این طرح آزمایش تفاوت گروه‌ها در $B$ را گزارش می‌کند چه نتیجه‌ای می‌گیرید؟
<details><summary>پاسخ</summary>
$B$ با این طرح آزمایش ضعیف بازیابی می‌شود: برآوردها تحت تأثیر نویز یا trade-off هستند، پس تفاوت گروه‌ها در $B$ برآوردشده قابل تفسیر نیست. مقاله باید طرح آزمایش را بهتر کند یا $B$ را تفسیر نکند.
</details>

</div>

**6. (Interpretation)** A BIC confusion matrix has P(selected = power | generated = asymptote) = 0.58. Your real data's BIC winner is the power model. What should you write?
<details><summary>Answer</summary>
That the power model is preferred by BIC but, at this design, BIC often selects the power model for data generated by the asymptote model, so the evidence does not discriminate between them well. Report the inversion probabilities, AIC/CV results, and recommend a design with longer delays.
</details>

<div dir="rtl">

**6. (تفسیر)** یک confusion matrix BIC دارای P(selected = power | generated = asymptote) = 0.58 است. برنده‌ی BIC در داده‌ی واقعی شما مدل توانی است. چه باید بنویسید؟
<details><summary>پاسخ</summary>
اینکه BIC مدل توانی را ترجیح می‌دهد، ولی با این طرح آزمایش BIC اغلب برای داده‌هایی که مدل مجانبی تولید کرده هم مدل توانی را انتخاب می‌کند، پس شواهد بین این دو به‌خوبی تمایز نمی‌گذارد. احتمال‌های معکوس و نتایج AIC/CV را گزارش کنید و طرحی با فاصله‌های طولانی‌تر پیشنهاد دهید.
</details>

</div>

**7. (Design)** You want to know whether a drug changes caution (boundary $a$) or evidence quality (drift $v$) in the random walk model. What data must you collect, and why is accuracy alone not enough?
<details><summary>Answer</summary>
Choices **and** RTs (ideally whole RT distributions) under drug and placebo. Both a larger $a$ and a larger $v$ raise accuracy, but $a$ slows responses while $v$ speeds them, so only the joint pattern separates them (Week 1).
</details>

<div dir="rtl">

**7. (طراحی)** می‌خواهید بدانید آیا یک دارو در مدل random walk احتیاط (مرز $a$) را تغییر می‌دهد یا کیفیت شواهد (drift $v$) را. چه داده‌ای باید جمع کنید و چرا دقت به‌تنهایی کافی نیست؟
<details><summary>پاسخ</summary>
انتخاب‌ها **و** زمان‌های واکنش (ترجیحاً کل توزیع زمان واکنش) تحت دارو و دارونما. هم $a$ بزرگ‌تر و هم $v$ بزرگ‌تر دقت را بالا می‌برند، ولی $a$ پاسخ‌ها را کند و $v$ سریع می‌کند، پس فقط الگوی مشترک آن‌ها را از هم جدا می‌کند (هفته‌ی 1).
</details>

</div>

**8. (Concept)** Why must cross-validation folds for the forgetting data be formed within intervals if we want to test prediction of new trials?
<details><summary>Answer</summary>
So that every training set contains all retention intervals (conditions), and the test asks about new items in known conditions. Leaving out whole intervals would test extrapolation to new conditions, which is a different generalization claim.
</details>

<div dir="rtl">

**8. (مفهومی)** اگر بخواهیم پیش‌بینی trialهای جدید را آزمون کنیم، چرا باید بخش‌های cross-validation برای داده‌های فراموشی داخل فاصله‌ها ساخته شوند؟
<details><summary>پاسخ</summary>
تا هر مجموعه‌ی آموزش همه‌ی فاصله‌های نگهداری (شرایط) را داشته باشد و آزمون درباره‌ی آیتم‌های جدید در شرایط معلوم باشد. کنار گذاشتن کل فاصله‌ها برون‌یابی به شرایط جدید را آزمون می‌کند که ادعای تعمیم دیگری است.
</details>

</div>

---

## Assignment · تکلیف

- **A3 (model comparison and recovery)** is due at the start of the Week 9 lecture.
- **Project proposal** is due at the start of the Week 9 lecture (max. 2 pages; see Week 7).
- No new assignment this week. Prepare for the midterm by running the case study above and answering the practice questions without looking at the answers.

<div dir="rtl">

- **A3 (مقایسه و بازیابی مدل)** در ابتدای درس هفته‌ی 9 تحویل داده می‌شود.
- **پیشنهاد پروژه** در ابتدای درس هفته‌ی 9 تحویل داده می‌شود (حداکثر 2 صفحه؛ هفته‌ی 7 را ببینید).
- این هفته تکلیف جدیدی نداریم. برای میان‌ترم با اجرای مطالعه‌ی موردی بالا و جواب دادن به سؤال‌های تمرینی بدون نگاه کردن به پاسخ‌ها آماده شوید.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018), chapters 2–5 and 10.** Reread the chapter summaries as a review of the whole first half of the course.
- **Lee & Wagenmakers (2014), chapter 11** (SDT). Read the model description as preparation for Week 9, where we start treating parameters as random variables with priors.

<div dir="rtl">

- **Farrell & Lewandowsky (2018)، فصل‌های 2 تا 5 و 10.** خلاصه‌ی فصل‌ها را به‌عنوان مرور کل نیمه‌ی اول درس دوباره بخوانید.
- **Lee & Wagenmakers (2014)، فصل 11** (SDT). توصیف مدل را برای آمادگی هفته‌ی 9 بخوانید، که در آن شروع می‌کنیم پارامترها را متغیرهای تصادفی با پیشین در نظر بگیریم.

</div>

*Preview for Week 9:* the second half of the course turns Bayesian. Instead of a single best estimate plus a confidence interval, we will compute the full probability distribution of the parameters given the data.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 9:* نیمه‌ی دوم درس بیزی می‌شود. به‌جای یک بهترین برآورد به‌علاوه‌ی یک بازه‌ی اطمینان، کل توزیع احتمال پارامترها به شرط داده را حساب می‌کنیم.

</div>
