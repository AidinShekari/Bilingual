# Week 16: Final Project Presentations and Good Modeling Practice · هفته‌ی 16: ارائه‌های پروژه‌ی پایانی و شیوه‌ی خوب مدل‌سازی

> **Course wrap-up** · Lecture slot: synthesis + first presentations · Lab slot: presentations and peer feedback

<div dir="rtl">

> **جمع‌بندی درس** · وقت درس: جمع‌بندی + اولین ارائه‌ها · وقت lab: ارائه‌ها و بازخورد همتایان

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| peer feedback | بازخورد همتا | نقد سازنده‌ی کار هم‌کلاسی‌ها |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| parameter recovery | بازیابی پارامتر | آیا برازش، پارامترهای معلوم شبیه‌سازی را برمی‌گرداند |
| reproducibility | بازتولیدپذیری | امکان به دست آوردن دوباره‌ی همان نتایج |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| Bayes factor (BF) | عامل بیز (Bayes factor) | نسبت درست‌نمایی‌های حاشیه‌ای دو مدل |
| bounds / constraints | کران‌ها / قیدها | محدودیت‌های مجاز برای مقدار پارامترها |
| posterior | توزیع پسین (posterior) | باور درباره‌ی پارامتر بعد از دیدن داده |
| hierarchical model | مدل سلسله‌مراتبی (چندسطحی) | پارامترهای فردی از یک توزیع گروهی می‌آیند |
| adequacy check | بررسی کفایت مدل | آیا مدل ویژگی‌های اصلی داده را بازتولید می‌کند |
| posterior predictive check (PPC) | بررسی پیش‌بینی پسین | مقایسه‌ی داده‌ی شبیه‌سازی‌شده از پسین با داده‌ی واقعی |
| cross-validation (CV) | اعتبارسنجی متقابل (cross-validation) | برازش روی بخشی از داده و آزمون روی بخش کنارگذاشته |
| AIC / BIC | معیار اطلاعاتی آکائیکه / بیزی | برازش به‌علاوه‌ی جریمه برای تعداد پارامتر |
| research design | طرح آزمایش | شرایط، تعداد کوشش‌ها و نمونه‌ها |
| model recovery | بازیابی مدل | آیا مقایسه‌ی مدل، مدل مولد را درست انتخاب می‌کند |
| drift-diffusion model (DDM) | مدل drift-diffusion (رانش–انتشار) | انباشت پیوسته‌ی شواهد بین دو مرز |
| preregistration | پیش‌ثبت (preregistration) | ثبت برنامه‌ی تحلیل پیش از دیدن داده |
| prior | توزیع پیشین (prior) | باور درباره‌ی پارامتر پیش از دیدن داده |
| random seed | seed تصادفی | عدد شروع مولد اعداد تصادفی برای تکرارپذیری |
| large language model (LLM) | مدل بزرگ زبانی | شبکه‌ی عصبی‌ای که کلمه‌ی بعدی متن را پیش‌بینی می‌کند |
| accuracy | دقت | نسبت پاسخ‌های درست |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Communicate** a complete modeling study (question, model, fitting, evaluation, recovery, interpretation) clearly and within a time limit.
2. **Critique** other modeling studies constructively, using the course's evaluation criteria.
3. **Apply** a checklist of good modeling practice (reproducibility, transparency, robustness) to their own project report.
4. **Integrate** the methods of the course into one coherent workflow and **explain** when to use which.

<div dir="rtl">

1. یک مطالعه‌ی مدل‌سازی کامل (سؤال، مدل، برازش، ارزیابی، بازیابی، تفسیر) را روشن و در محدوده‌ی زمانی **ارائه کنند**.
2. مطالعه‌های مدل‌سازی دیگران را با معیارهای ارزیابی درس، به شکلی سازنده **نقد کنند**.
3. یک چک‌لیست شیوه‌ی خوب مدل‌سازی (بازتولیدپذیری، شفافیت، استواری) را روی گزارش پروژه‌ی خودشان **اعمال کنند**.
4. روش‌های درس را در یک گردش کار منسجم **یکپارچه کنند** و **توضیح دهند** کِی از کدام استفاده کنند.

</div>

---

## Motivation & big picture · مقدمه

A model is only as useful as others' ability to understand, check and build on it. Over 15 weeks, every lab has followed the same arc: **formalize → simulate → fit → evaluate → recover → interpret.** This week you show that arc in your own project, and you practice the other half of scientific modeling: reading someone else's model critically but fairly. The session ends with the practices that make modeling work trustworthy and reusable: reproducible code, transparent reporting, honest statements of limitations.

<div dir="rtl">

یک مدل فقط به اندازه‌ی توانایی دیگران در فهمیدن، بررسی کردن و ساختن روی آن مفید است. در 15 هفته، همه‌ی labها یک مسیر را دنبال کرده‌اند: **صورت‌بندی ← شبیه‌سازی ← برازش ← ارزیابی ← بازیابی ← تفسیر.** این هفته این مسیر را در پروژه‌ی خودتان نشان می‌دهید، و نیمه‌ی دیگر مدل‌سازی علمی را تمرین می‌کنید: خواندن مدل دیگران به شکلی انتقادی ولی منصفانه. جلسه با شیوه‌هایی تمام می‌شود که کار مدل‌سازی را قابل اعتماد و قابل استفاده‌ی دوباره می‌کنند: کد بازتولیدپذیر، گزارش شفاف، بیان صادقانه‌ی محدودیت‌ها.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

The last week has no new method. Students present their projects, and the course is summarized as one workflow: **formalize** a theory as a model, **simulate** it to see what it predicts, **fit** it to data, **evaluate** it (does it fit, and does it beat alternatives?), check that the method can **recover** the truth at this design, and **interpret** the result in psychological terms, including what cannot be concluded. The checklist of good practice turns these steps into concrete things to verify in every report: reproducible code, reported uncertainty, adequacy checks, recovery and honest limitations.

<div dir="rtl">

هفته‌ی آخر روش جدیدی ندارد. دانشجوها پروژه‌هایشان را ارائه می‌دهند و کل درس به شکل یک گردش کار خلاصه می‌شود: نظریه را به شکل یک مدل **فرمال کن**، آن را **شبیه‌سازی کن** تا ببینی چه پیش‌بینی می‌کند، آن را روی داده **برازش کن**، **ارزیابی‌اش کن** (آیا برازش خوبی دارد و آیا از رقیب‌ها بهتر است؟)، بررسی کن که روش در این طرح آزمایش می‌تواند حقیقت را **بازیابی کند**، و نتیجه را به زبان روان‌شناختی **تفسیر کن**، از جمله اینکه چه نتیجه‌ای را نمی‌شود گرفت. چک‌لیست شیوه‌ی خوب این قدم‌ها را به چیزهای مشخصی تبدیل می‌کند که در هر گزارش باید بررسی شوند: کد بازتولیدپذیر، گزارش عدم قطعیت، بررسی کفایت مدل، بازیابی و بیان صادقانه‌ی محدودیت‌ها.

</div>

**Suggested timing (lecture slot, 60 min):** course synthesis 15 · good-practice checklist 15 · first presentations 30.

<div dir="rtl">

**زمان‌بندی پیشنهادی (وقت درس، 60 دقیقه):** جمع‌بندی درس 15 · چک‌لیست شیوه‌ی خوب 15 · اولین ارائه‌ها 30.

</div>

### 1. The course in one table · 1. کل درس در یک جدول

| Question you face | Tools | Week |
|---|---|---|
| How do I turn a theory into a model? | Five components; simulation; analytic checks | 1–2 |
| How do I estimate parameters? | Least squares; maximum likelihood; optimization (grid, Nelder–Mead, L-BFGS-B), multi-start, bounds | 3–4 |
| How certain are the estimates? | Hessian SEs, profile likelihood, bootstrap; posterior intervals | 5, 9 |
| How do I handle many participants? | Individual fits; aggregation artifacts; hierarchical models | 5, 13 |
| Is the model adequate? | Residuals, $G^2$, posterior predictive checks | 2–4, 10 |
| Which model is better? | CV, LRT, AIC/BIC, Bayes factors | 6–7, 10 |
| Can my design answer the question? | Parameter recovery, model recovery | 7 |
| How do I get a posterior for complex models? | Grid → Metropolis–Hastings → Gibbs → NUTS (PyMC); $\hat R$, ESS, divergences | 9–13 |
| What do models look like in different fields? | SDT, forgetting, practice, GCM, DDM/EZ, RL, ideal observers | 2, 5, 14–15 |

<div dir="rtl">

| سؤالی که با آن روبه‌رو هستید | ابزارها | هفته |
|---|---|---|
| چطور یک نظریه را به مدل تبدیل کنم؟ | پنج جزء؛ شبیه‌سازی؛ بررسی‌های تحلیلی | 1–2 |
| چطور پارامترها را برآورد کنم؟ | کمترین مربعات؛ بیشینه‌ی درست‌نمایی؛ بهینه‌سازی (grid، Nelder–Mead، L-BFGS-B)، multi-start، کران‌ها | 3–4 |
| برآوردها چقدر مطمئن‌اند؟ | SEهای Hessian، profile likelihood، bootstrap؛ بازه‌های پسین | 5، 9 |
| با شرکت‌کننده‌های زیاد چه کنم؟ | برازش‌های فردی؛ خطاهای میانگین‌گیری؛ مدل‌های سلسله‌مراتبی | 5، 13 |
| آیا مدل کفایت دارد؟ | باقی‌مانده‌ها، $G^2$، بررسی‌های پیش‌بینی پسین | 2–4، 10 |
| کدام مدل بهتر است؟ | CV، LRT، AIC/BIC، Bayes factor | 6–7، 10 |
| آیا طرح من می‌تواند به سؤال جواب دهد؟ | بازیابی پارامتر، بازیابی مدل | 7 |
| چطور برای مدل‌های پیچیده پسین به دست بیاورم؟ | Grid ← Metropolis–Hastings ← Gibbs ← NUTS (PyMC)؛ $\hat R$، ESS، divergenceها | 9–13 |
| مدل‌ها در حوزه‌های مختلف چه شکلی‌اند؟ | SDT، فراموشی، تمرین، GCM، DDM/EZ، RL، مشاهده‌گرهای ایده‌آل | 2، 5، 14–15 |

</div>

#### For an engineer · برای یک مهندس

Looking back, most of the course maps onto tools you already know, and the table below can serve as your own summary when answering students' questions:

| Course topic | Engineering counterpart |
|---|---|
| Random walk / DDM (Weeks 1, 14) | Sequential detection (SPRT), first-passage times |
| SDT, ROC (Week 2) | Binary detection, $P_D$ / $P_{FA}$, ROC |
| Least squares, optimizers (Week 3) | LS estimation, gradient methods, Gauss–Newton |
| Maximum likelihood, $G^2$, LRT (Weeks 4, 7) | ML estimation, goodness-of-fit tests, GLRT |
| Hessian SEs, bootstrap (Week 5) | Fisher information / CRLB, Monte Carlo performance evaluation |
| CV, AIC, BIC (Weeks 6–7) | Model-order selection (AIC, MDL), validation data |
| Parameter/model recovery (Week 7) | Testing estimators on synthetic data with known ground truth |
| Bayesian inference, BF (Weeks 9–10) | MAP/MMSE estimation, Bayesian detection |
| MCMC, $\hat R$, ESS (Weeks 11–12) | Monte Carlo simulation, Markov processes, correlated-sample statistics |
| Hierarchical models (Week 13) | Empirical Bayes, James–Stein shrinkage |
| Delta rule, cue combination (Week 15) | LMS adaptation, MRC / Kalman sensor fusion |

What is genuinely different in cognitive modeling: the "system" is a human being, the data are small and noisy, and the parameters themselves are the scientific findings, so interpretation, uncertainty and recovery matter more than raw performance.

<div dir="rtl">

با نگاه به عقب، بیشتر درس روی ابزارهایی که قبلاً می‌شناسید منطبق است، و جدول زیر می‌تواند خلاصه‌ی خودتان برای جواب دادن به سؤال‌های دانشجوها باشد:

| موضوع درس | معادل مهندسی |
|---|---|
| random walk / DDM (هفته‌های 1، 14) | آشکارسازی ترتیبی (SPRT)، زمان‌های اولین عبور |
| SDT، ROC (هفته‌ی 2) | آشکارسازی دودویی، $P_D$ / $P_{FA}$، ROC |
| کمترین مربعات، بهینه‌سازها (هفته‌ی 3) | تخمین LS، روش‌های گرادیانی، Gauss–Newton |
| بیشینه‌ی درست‌نمایی، $G^2$، LRT (هفته‌های 4، 7) | تخمین ML، آزمون‌های نیکویی برازش، GLRT |
| SE از Hessian، bootstrap (هفته‌ی 5) | اطلاعات فیشر / CRLB، ارزیابی کارایی با Monte Carlo |
| CV، AIC، BIC (هفته‌های 6–7) | انتخاب مرتبه‌ی مدل (AIC، MDL)، داده‌ی اعتبارسنجی |
| بازیابی پارامتر و مدل (هفته‌ی 7) | آزمودن تخمین‌گرها روی داده‌ی مصنوعی با حقیقت معلوم |
| استنباط بیزی، BF (هفته‌های 9–10) | تخمین MAP/MMSE، آشکارسازی بیزی |
| MCMC، $\hat R$، ESS (هفته‌های 11–12) | شبیه‌سازی Monte Carlo، فرایندهای مارکوف، آمار نمونه‌های همبسته |
| مدل‌های سلسله‌مراتبی (هفته‌ی 13) | empirical Bayes، shrinkage از نوع James–Stein |
| قاعده‌ی دلتا، ترکیب نشانه‌ها (هفته‌ی 15) | تطبیق LMS، MRC / ادغام حسگر در کالمن |

چیزی که در مدل‌سازی شناختی واقعاً متفاوت است: «سیستم» یک انسان است، داده کم و پرنویز است، و خود پارامترها یافته‌ی علمی‌اند؛ پس تفسیر، عدم قطعیت و بازیابی از کارایی خام مهم‌ترند.

</div>

### 2. A checklist of good modeling practice · 2. یک چک‌لیست شیوه‌ی خوب مدل‌سازی

**Before fitting**
- [ ] The research question is stated in terms of model parameters or model comparisons.
- [ ] Candidate models (including at least one simpler alternative) are specified *before* looking at the data, ideally preregistered.
- [ ] Priors (if Bayesian) are justified and checked with prior predictive simulation.
- [ ] Parameter and model recovery have been checked **at the actual design**.

<div dir="rtl">

**پیش از برازش**
- [ ] سؤال پژوهشی بر حسب پارامترهای مدل یا مقایسه‌ی مدل‌ها بیان شده است.
- [ ] مدل‌های نامزد (دست‌کم با یک جایگزین ساده‌تر) *پیش از* نگاه کردن به داده مشخص شده‌اند، ترجیحاً با پیش‌ثبت (preregistration).
- [ ] پیشین‌ها (اگر بیزی است) توجیه شده‌اند و با شبیه‌سازی پیش‌بینی پیشین بررسی شده‌اند.
- [ ] بازیابی پارامتر و مدل **در همان طرح واقعی** بررسی شده است.

</div>

**Fitting and evaluation**
- [ ] The likelihood matches the data type (binomial for counts, sequential for learning, …).
- [ ] Optimization uses multi-start and sensible bounds, and fits are checked visually; for MCMC, $\hat R$, ESS and divergences are reported.
- [ ] Absolute fit (residuals, $G^2$ or PPC) *and* relative fit (CV/IC/BF) are reported.
- [ ] Uncertainty is reported for every interpreted parameter.

<div dir="rtl">

**برازش و ارزیابی**
- [ ] درست‌نمایی با نوع داده جور است (دوجمله‌ای برای شمارش‌ها، ترتیبی برای یادگیری، …).
- [ ] بهینه‌سازی از multi-start و کران‌های معقول استفاده می‌کند و برازش‌ها به‌صورت تصویری بررسی شده‌اند؛ برای MCMC، $\hat R$، ESS و divergenceها گزارش شده‌اند.
- [ ] برازش مطلق (باقی‌مانده‌ها، $G^2$ یا PPC) *و* برازش نسبی (CV/IC/BF) گزارش شده‌اند.
- [ ] برای هر پارامتری که تفسیر می‌شود عدم قطعیت گزارش شده است.

</div>

**Reporting and reproducibility**
- [ ] All code and (where allowed) data are shared; random seeds are fixed.
- [ ] Software versions are recorded (e.g., `conda env export > environment.yml`).
- [ ] One command or notebook regenerates every number and figure in the report.
- [ ] Limitations are stated: what the design cannot distinguish, which parameters are not recoverable, which assumptions were not tested.

<div dir="rtl">

**گزارش و بازتولیدپذیری**
- [ ] همه‌ی کدها و (در صورت اجازه) داده‌ها به اشتراک گذاشته شده‌اند؛ seedهای تصادفی ثابت شده‌اند.
- [ ] نسخه‌های نرم‌افزار ثبت شده‌اند (مثلاً `conda env export > environment.yml`).
- [ ] یک دستور یا notebook همه‌ی عددها و نمودارهای گزارش را دوباره تولید می‌کند.
- [ ] محدودیت‌ها بیان شده‌اند: طرح چه چیزی را نمی‌تواند تمیز دهد، کدام پارامترها قابل بازیابی نیستند، کدام فرض‌ها آزموده نشده‌اند.

</div>

**Recording the computing environment** (include in every project notebook):

<div dir="rtl">

**ثبت محیط محاسباتی** (در هر notebook پروژه بگذارید):

</div>

> **Code · کد:** [`code/week16.py`](code/week16.py), cell 1 · سلول 1

### 3. Presentation format · 3. قالب ارائه

- **Length:** 8 minutes (individual) or 10 minutes (pairs), plus 4 minutes of questions. Strict timekeeping.
- **Suggested structure** (one slide each, roughly):
  1. The question and why it matters.
  2. The model(s): equations and the psychological meaning of every parameter.
  3. Data and design.
  4. Fitting method and a fit figure (data + predictions).
  5. Evaluation: model comparison *and* an adequacy check.
  6. Recovery: can the design answer the question?
  7. Interpretation and limitations.
- **Pairs:** both members present, and the Bayesian/MCMC or hierarchical component must be shown.
- **Schedule:** posted one week in advance; the order is drawn at random. Sessions run across the lecture and lab slots (about 15–18 presentations in 3 hours, depending on enrolment).

<div dir="rtl">

- **مدت:** 8 دقیقه (انفرادی) یا 10 دقیقه (دونفره)، به‌علاوه‌ی 4 دقیقه پرسش. زمان دقیق رعایت می‌شود.
- **ساختار پیشنهادی** (تقریباً هر مورد یک اسلاید):
  1. سؤال و اینکه چرا مهم است.
  2. مدل(ها): معادله‌ها و معنای روان‌شناختی هر پارامتر.
  3. داده و طرح.
  4. روش برازش و یک نمودار برازش (داده + پیش‌بینی‌ها).
  5. ارزیابی: مقایسه‌ی مدل *و* یک بررسی کفایت.
  6. بازیابی: آیا طرح می‌تواند به سؤال جواب دهد؟
  7. تفسیر و محدودیت‌ها.
- **تیم‌های دونفره:** هر دو عضو ارائه می‌دهند، و بخش بیزی/MCMC یا سلسله‌مراتبی باید نشان داده شود.
- **برنامه:** یک هفته زودتر اعلام می‌شود؛ ترتیب با قرعه تعیین می‌شود. جلسه‌ها در وقت درس و lab برگزار می‌شوند (حدود 15–18 ارائه در 3 ساعت، بسته به تعداد ثبت‌نام).

</div>

### 4. Giving and receiving feedback · 4. دادن و گرفتن بازخورد

Each student completes a **peer-feedback form** for three assigned presentations (below). Feedback is anonymous to the presenter, visible to the instructor, and counts toward participation (lab check-off). Good feedback is **specific** ("the recovery plot shows $\beta$ is not identifiable, so the group difference in $\beta$ should not be interpreted") rather than general ("nice talk"), and **constructive** (it suggests a concrete improvement).

<div dir="rtl">

هر دانشجو برای سه ارائه‌ی تعیین‌شده یک **فرم بازخورد همتا** پر می‌کند (پایین). بازخورد برای ارائه‌دهنده ناشناس و برای مدرس قابل مشاهده است و در نمره‌ی مشارکت (lab check-off) حساب می‌شود. بازخورد خوب **مشخص** است («نمودار بازیابی نشان می‌دهد $\beta$ identifiable نیست، پس تفاوت گروه‌ها در $\beta$ نباید تفسیر شود») نه کلی («ارائه‌ی خوبی بود»)، و **سازنده** است (یک بهبود مشخص پیشنهاد می‌کند).

</div>

**Peer-feedback form**

<div dir="rtl">

**فرم بازخورد همتا**

</div>

| Item | Rating (1–4) | Comment |
|---|---|---|
| The question was clear and the model matched it | | |
| The model's parameters were explained in psychological terms | | |
| The fit was shown and evaluated (adequacy + comparison) | | |
| Recovery or identifiability was addressed | | |
| Conclusions followed from the results, and limitations were stated | | |
| **One thing that was particularly well done** | | |
| **One concrete suggestion for the written report** | | |

<div dir="rtl">

| مورد | امتیاز (1–4) | توضیح |
|---|---|---|
| سؤال روشن بود و مدل با آن جور بود | | |
| پارامترهای مدل با زبان روان‌شناختی توضیح داده شدند | | |
| برازش نشان داده و ارزیابی شد (کفایت + مقایسه) | | |
| به بازیابی یا identifiability پرداخته شد | | |
| نتیجه‌گیری‌ها از نتایج بیرون آمدند و محدودیت‌ها بیان شدند | | |
| **یک چیزی که به‌خصوص خوب انجام شده بود** | | |
| **یک پیشنهاد مشخص برای گزارش کتبی** | | |

</div>

#### For the instructor · برای مدرس

- **Grade with the rubric, comment with the checklist.** During presentations, keep the good-practice checklist next to you and note one strength and one concrete improvement per team; this makes the written feedback fast and fair.
- **Questions to ask presenters** (they map onto the course): Which parameter answers your question? How do you know it is recoverable? Does the model fit in absolute terms, not only better than the alternative? What can your design *not* tell us?
- **Use the worked critique** (fictional Q-learning study) as a model for how students should give feedback: specific, tied to a week of the course, and constructive.
- **Close the course with the one-table summary.** Ask students which row they found hardest, and point them to the corresponding week for exam revision.

<div dir="rtl">

- **با rubric نمره بدهید و با چک‌لیست نظر بدهید.** در طول ارائه‌ها چک‌لیست شیوه‌ی خوب را کنارتان نگه دارید و برای هر تیم یک نقطه‌ی قوت و یک پیشنهاد مشخص یادداشت کنید؛ این کار بازخورد کتبی را سریع و منصفانه می‌کند.
- **سؤال‌هایی برای ارائه‌دهندگان** (منطبق بر درس): کدام پارامتر به سؤال شما جواب می‌دهد؟ از کجا می‌دانید قابل بازیابی است؟ آیا مدل به‌طور مطلق برازش خوبی دارد، نه فقط بهتر از رقیب؟ طرح آزمایش شما چه چیزی را *نمی‌تواند* به ما بگوید؟
- **از نقد حل‌شده** (مطالعه‌ی خیالی Q-learning) به‌عنوان الگوی بازخورد دادن دانشجوها استفاده کنید: مشخص، وصل به یکی از هفته‌های درس، و سازنده.
- **درس را با جدول خلاصه‌ی یک‌صفحه‌ای ببندید.** از دانشجوها بپرسید کدام سطر برایشان سخت‌تر بود و برای مرور امتحان آن‌ها را به هفته‌ی مربوط ارجاع دهید.

</div>

---

## Worked example: critiquing a modeling study · مثال حل‌شده: نقد یک مطالعه‌ی مدل‌سازی

**Summary of a (fictional) study.** *"We fitted a Q-learning model to 30 patients and 30 controls who performed 60 trials of a two-armed bandit task with stable reward probabilities. Each participant was fitted by MLE. Patients had significantly lower learning rates ($t(58) = 2.4$, $p = .02$). We conclude that the disorder impairs reward learning."*

<div dir="rtl">

**خلاصه‌ی یک مطالعه‌ی (خیالی).** *«یک مدل Q-learning را روی 30 بیمار و 30 فرد کنترل برازش کردیم که 60 trial از یک تکلیف bandit دوبازویی با احتمال‌های پاداش ثابت انجام دادند. هر شرکت‌کننده با MLE برازش شد. بیماران نرخ یادگیری به‌طور معنادار پایین‌تری داشتند ($t(58) = 2.4$، $p = .02$). نتیجه می‌گیریم که این اختلال یادگیری از پاداش را مختل می‌کند.»*

</div>

**Critique using the checklist.**

<div dir="rtl">

**نقد با استفاده از چک‌لیست.**

</div>

1. **Recovery at this design (Week 7, Week 15 lab).** With 60 trials and *stable* reward probabilities, the learning rate is weakly identifiable, and $\alpha$ and $\beta$ trade off. Without a recovery study, a difference in $\hat\alpha$ could reflect a difference in choice noise ($\beta$) or just estimation noise. *Suggestion:* report parameter recovery at this design, and include reversals.
2. **Model comparison (Week 15, Part D).** Did Q-learning beat simpler strategies (WSLS, perseveration) in both groups? If patients are better described by a different strategy, comparing their $\alpha$ with controls' is not meaningful. *Suggestion:* report AIC/BIC or CV per group, with model recovery.
3. **Second-stage t-test on point estimates (Weeks 5, 13).** It ignores the uncertainty of individual estimates, which is large with 60 trials. *Suggestion:* a hierarchical model with a group effect on $\alpha$, reporting its posterior.
4. **Adequacy (Weeks 4, 10).** No posterior predictive check or learning-curve plot is shown. Does the model reproduce each group's learning curve?
5. **Interpretation.** "Impairs reward learning" is a strong process claim. A lower $\hat\alpha$ is also compatible with more exploration, lower motivation (lower $\beta$), or different priors on initial values. *Suggestion:* temper the conclusion, or add a design that separates these accounts.

<div dir="rtl">

1. **بازیابی در این طرح (هفته‌ی 7، lab هفته‌ی 15).** با 60 trial و احتمال‌های پاداش *ثابت*، نرخ یادگیری ضعیف شناسایی می‌شود، و $\alpha$ و $\beta$ با هم trade-off دارند. بدون مطالعه‌ی بازیابی، تفاوت در $\hat\alpha$ ممکن است بازتاب تفاوت در نویز انتخاب ($\beta$) یا فقط نویز برآورد باشد. *پیشنهاد:* بازیابی پارامتر را در همین طرح گزارش کنید و وارونگی اضافه کنید.
2. **مقایسه‌ی مدل (هفته‌ی 15، بخش D).** آیا Q-learning در هر دو گروه از راهبردهای ساده‌تر (WSLS، پافشاری) بهتر بود؟ اگر بیماران با راهبرد دیگری بهتر توصیف شوند، مقایسه‌ی $\alpha$ آن‌ها با گروه کنترل معنادار نیست. *پیشنهاد:* AIC/BIC یا CV را برای هر گروه همراه با بازیابی مدل گزارش کنید.
3. **آزمون t مرحله‌ی دوم روی برآوردهای نقطه‌ای (هفته‌های 5، 13).** عدم قطعیت برآوردهای فردی را نادیده می‌گیرد، که با 60 trial بزرگ است. *پیشنهاد:* یک مدل سلسله‌مراتبی با اثر گروه روی $\alpha$، و گزارش پسین آن.
4. **کفایت (هفته‌های 4، 10).** هیچ بررسی پیش‌بینی پسین یا نمودار منحنی یادگیری نشان داده نشده. آیا مدل منحنی یادگیری هر گروه را بازتولید می‌کند؟
5. **تفسیر.** «یادگیری از پاداش را مختل می‌کند» یک ادعای فرایندی قوی است. $\hat\alpha$ پایین‌تر با کاوش بیشتر، انگیزه‌ی کمتر ($\beta$ پایین‌تر) یا پیشین‌های متفاوت روی ارزش‌های اولیه هم سازگار است. *پیشنهاد:* نتیجه‌گیری را تعدیل کنید، یا طرحی اضافه کنید که این تبیین‌ها را از هم جدا کند.

</div>

**Overall:** a reasonable first study whose conclusion is not yet supported. Three additions (recovery, model comparison, hierarchical estimation) would make it convincing. Notice that each point maps directly onto one week of this course.

<div dir="rtl">

**در مجموع:** یک مطالعه‌ی اول معقول که نتیجه‌گیری‌اش هنوز پشتوانه ندارد. سه افزوده (بازیابی، مقایسه‌ی مدل، برآورد سلسله‌مراتبی) آن را قانع‌کننده می‌کند. توجه کنید که هر نکته مستقیماً به یکی از هفته‌های این درس برمی‌گردد.

</div>

---

## Lab (2 hours): presentations and peer feedback · lab (2 ساعت): ارائه‌ها و بازخورد همتایان

**Goals:** present your project; give written feedback on three presentations; note the feedback you receive for your final report.

<div dir="rtl">

**اهداف:** پروژه‌تان را ارائه دهید؛ برای سه ارائه بازخورد کتبی بدهید؛ بازخوردهایی را که می‌گیرید برای گزارش پایانی یادداشت کنید.

</div>

**Logistics:**
- Upload slides (PDF) to the course page **before** the session starts.
- Bring your laptop with your project notebook in case of questions about the code.
- Fill in the peer-feedback forms during the session (paper or online form) and submit them by the end of the day.

<div dir="rtl">

**هماهنگی‌ها:**
- اسلایدها (PDF) را **پیش از** شروع جلسه در صفحه‌ی درس بارگذاری کنید.
- لپ‌تاپتان را با notebook پروژه بیاورید، برای پرسش‌هایی درباره‌ی کد.
- فرم‌های بازخورد همتا را در طول جلسه پر کنید (کاغذی یا فرم آنلاین) و تا پایان روز تحویل دهید.

</div>

**After the presentations:** the instructor gives brief oral feedback to each team. Written feedback (instructor + peers) is returned within 3 days so it can be used in the final report.

<div dir="rtl">

**بعد از ارائه‌ها:** مدرس به هر تیم بازخورد شفاهی کوتاهی می‌دهد. بازخورد کتبی (مدرس + همتایان) ظرف 3 روز برگردانده می‌شود تا در گزارش پایانی استفاده شود.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Good practice when AI is part of your modeling work.** AI tools now enter cognitive modeling in three roles, and each needs the course's habits of checking:
1. **As a coding assistant.** Generated code can look right and be wrong. Test it the modeling way: simulate data with known parameters and check that the code recovers them (parameter recovery as a unit test).
2. **As a "simulated participant".** Some studies give LLMs psychology experiments and compare the answers with human data, or even propose LLM-based models of human behavior (e.g., Binz & Schulz, 2023; Dillion et al., 2023 [verify]). Evaluate such claims like any model: generalization to new tasks, comparison with simpler cognitive models, mimicry, and interpretability (Week 15).
3. **As an object of study.** If you test an LLM, record the model name and version, the date, the exact prompts, the temperature and the number of samples. Without these, the study cannot be reproduced.

<div dir="rtl">

**شیوه‌ی خوب وقتی هوش مصنوعی بخشی از کار مدل‌سازی شماست.** ابزارهای هوش مصنوعی امروز با سه نقش وارد مدل‌سازی شناختی می‌شوند، و هر نقش به عادت‌های بررسی این درس نیاز دارد:
1. **به‌عنوان دستیار کدنویسی.** کد تولیدشده می‌تواند درست به نظر برسد و غلط باشد. آن را به روش مدل‌سازی بیازمایید: داده را با پارامترهای معلوم شبیه‌سازی کنید و بررسی کنید که کد آن‌ها را بازیابی می‌کند (بازیابی پارامتر به‌عنوان unit test).
2. **به‌عنوان «شرکت‌کننده‌ی شبیه‌سازی‌شده».** بعضی مطالعه‌ها آزمایش‌های روان‌شناسی را به LLMها می‌دهند و جواب‌ها را با داده‌ی انسانی مقایسه می‌کنند، یا حتی مدل‌هایی مبتنی بر LLM برای رفتار انسان پیشنهاد می‌کنند (مثلاً Binz & Schulz, 2023; Dillion et al., 2023 [بررسی شود]). چنین ادعاهایی را مثل هر مدل دیگری ارزیابی کنید: تعمیم به تکلیف‌های تازه، مقایسه با مدل‌های شناختی ساده‌تر، تقلید (mimicry) و تفسیرپذیری (هفته‌ی 15).
3. **به‌عنوان موضوع مطالعه.** اگر یک LLM را می‌آزمایید، نام و نسخه‌ی مدل، تاریخ، promptهای دقیق، دما و تعداد نمونه‌ها را ثبت کنید. بدون این‌ها مطالعه قابل بازتولید نیست.

</div>

The code below tests a pre-made SDT function "written by an assistant". It looks plausible, and it even passes the case $c = 0$, but a recovery test shows that it gets the sign of $c$ wrong.

<div dir="rtl">

کد پایین یک تابع SDT ازپیش‌آماده را که «یک دستیار نوشته» می‌آزماید. معقول به نظر می‌رسد و حتی حالت $c = 0$ را درست جواب می‌دهد، ولی یک آزمون بازیابی نشان می‌دهد که علامت $c$ را غلط حساب می‌کند.

</div>

> **Code · کد:** [`code/week16.py`](code/week16.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
true (d', c) = (1.5, 0.3) -> recovered (1.50, -0.30)  FAIL
true (d', c) = (1.0, -0.4) -> recovered (1.00, 0.40)  FAIL
true (d', c) = (2.0, 0.0) -> recovered (2.00, 0.00)  OK
```

A liberal observer would be reported as conservative, which would reverse the conclusion of a bias study. The test with $c = 0$ alone would not have caught it.

<div dir="rtl">

یک مشاهده‌گر liberal، محافظه‌کار گزارش می‌شد، که نتیجه‌گیری یک مطالعه‌ی سوگیری را برعکس می‌کرد. آزمونی که فقط $c = 0$ را بسنجد این را پیدا نمی‌کرد.

</div>

**Try it (no API needed).**
- ★ Fix the function and rerun the tests.
- ★★ Write a similar recovery test for the EZ-diffusion function of Week 14, using the simulator from the same lab.
- ★★ For your own project: add one paragraph to the reproducibility statement that describes how AI tools were used and how their output was verified (see `assessments/project_brief.md`, section 6).

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ تابع را اصلاح کنید و آزمون‌ها را دوباره اجرا کنید.
- ★★ یک آزمون بازیابی مشابه برای تابع EZ-diffusion هفته‌ی 14 بنویسید، با استفاده از شبیه‌ساز همان lab.
- ★★ برای پروژه‌ی خودتان: یک پاراگراف به بیانیه‌ی بازتولیدپذیری اضافه کنید که توضیح دهد ابزارهای هوش مصنوعی چطور استفاده شدند و خروجی‌شان چطور بررسی شد (`assessments/project_brief.md`، بخش 6 را ببینید).

</div>

*Optional reading:* Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *PNAS, 120*(6), e2218523120. Dillion, D., Tandon, N., Gu, Y., & Gray, K. (2023). Can AI language models replace human participants? *Trends in Cognitive Sciences, 27*, 597–600 [verify].

<div dir="rtl">

*مطالعه‌ی اختیاری:* Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *PNAS, 120*(6), e2218523120. Dillion, D., Tandon, N., Gu, Y., & Gray, K. (2023). Can AI language models replace human participants? *Trends in Cognitive Sciences, 27*, 597–600 [بررسی شود].

</div>

---

## Common mistakes & misconceptions (in project presentations and reports) · اشتباهات رایج و برداشت‌های نادرست (در ارائه‌ها و گزارش‌های پروژه)

1. **Too much on the method, too little on the meaning.** Every parameter and every result needs a psychological interpretation.
2. **Showing a fit statistic without a fit figure.** Always plot data against predictions.
3. **Model comparison without an adequacy check,** or vice versa.
4. **Interpreting parameters that were not shown to be recoverable.**
5. **Overclaiming:** "the model is correct", "the mind is Bayesian". State what the evidence supports and what it does not.
6. **Irreproducible results:** missing seeds, unrecorded package versions, notebook cells run out of order.
7. **Running over time.** Practice the talk; one idea per slide.

<div dir="rtl">

1. **پرداختن زیاد به روش و کم به معنا.** هر پارامتر و هر نتیجه به یک تفسیر روان‌شناختی نیاز دارد.
2. **نشان دادن یک آماره‌ی برازش بدون نمودار برازش.** همیشه داده را در برابر پیش‌بینی‌ها رسم کنید.
3. **مقایسه‌ی مدل بدون بررسی کفایت،** یا برعکس.
4. **تفسیر پارامترهایی که قابل بازیابی بودنشان نشان داده نشده.**
5. **ادعای بیش از حد:** «مدل درست است»، «ذهن بیزی است». بگویید شواهد از چه چیزی پشتیبانی می‌کند و از چه چیزی نه.
6. **نتایج غیرقابل بازتولید:** seedهای جاافتاده، نسخه‌های ثبت‌نشده‌ی بسته‌ها، سلول‌های notebook که بی‌ترتیب اجرا شده‌اند.
7. **رد کردن از زمان.** ارائه را تمرین کنید؛ در هر اسلاید یک ایده.

</div>

---

## Check your understanding (integrative review questions for the final exam) · خودآزمایی (پرسش‌های مرور یکپارچه برای امتحان پایانی)

**1.** A colleague has accuracy and RT data from a speed/accuracy manipulation and wants to know whether the manipulation affects caution or evidence quality. Outline a full modeling plan, naming the model, the fitting method, the evaluation, and the recovery check.
<details><summary>Answer</summary>
Model: drift-diffusion (EZ-diffusion for a first pass, or the full DDM by MLE / hierarchical Bayes). Fit per participant and condition. Compare models in which the manipulation affects only $a$, only $v$, or both (AIC/BIC or a hierarchical model with condition effects; PPC on RT quantiles). Recovery: simulate data at the actual design with each model, and check that parameters and the "which parameter changed" conclusion are recovered. Interpret the condition effects on $a$ and $v$ with uncertainty.
</details>

<div dir="rtl">

**1.** همکاری داده‌ی دقت و RT از یک دست‌کاری سرعت/دقت دارد و می‌خواهد بداند دست‌کاری روی احتیاط اثر می‌گذارد یا کیفیت شواهد. یک برنامه‌ی کامل مدل‌سازی طرح کنید و مدل، روش برازش، ارزیابی و بررسی بازیابی را نام ببرید.
<details><summary>پاسخ</summary>
مدل: drift-diffusion (EZ-diffusion برای دور اول، یا DDM کامل با MLE / بیزی سلسله‌مراتبی). برای هر شرکت‌کننده و شرط برازش کنید. مدل‌هایی را مقایسه کنید که در آن‌ها دست‌کاری فقط روی $a$، فقط روی $v$، یا روی هر دو اثر می‌گذارد (AIC/BIC یا یک مدل سلسله‌مراتبی با اثر شرط؛ PPC روی quantileهای RT). بازیابی: با هر مدل در طرح واقعی داده شبیه‌سازی کنید و بررسی کنید که پارامترها و نتیجه‌ی «کدام پارامتر تغییر کرد» بازیابی می‌شوند. اثر شرط روی $a$ و $v$ را با عدم قطعیتش تفسیر کنید.
</details>

</div>

**2.** When would you choose a Bayes factor over cross-validation for comparing two models, and vice versa?
<details><summary>Answer</summary>
Bayes factor: when the question is which model is more probable given the data (evidence, including support for a null), when meaningful priors are available, and with a prior sensitivity analysis. CV: when the goal is predictive accuracy for new data of a specific kind, priors are hard to justify, or the BF is too sensitive to the priors.
</details>

<div dir="rtl">

**2.** کِی برای مقایسه‌ی دو مدل Bayes factor را به cross-validation ترجیح می‌دهید، و برعکس؟
<details><summary>پاسخ</summary>
Bayes factor: وقتی سؤال این است که با توجه به داده کدام مدل محتمل‌تر است (شواهد، از جمله پشتیبانی از فرض صفر)، وقتی پیشین‌های معنادار در دسترس‌اند، و همراه با تحلیل حساسیت به پیشین. CV: وقتی هدف دقت پیش‌بینی برای داده‌ی تازه از یک نوع مشخص است، توجیه پیشین‌ها سخت است، یا BF بیش از حد به پیشین‌ها حساس است.
</details>

</div>

**3.** Explain how a parameter can be estimated very precisely (narrow CI or posterior) and yet be meaningless.
<details><summary>Answer</summary>
Precision only reflects the curvature of the likelihood under the assumed model. If the model is misspecified (fails PPC/$G^2$), if the parameter trades off with another so that its meaning depends on an arbitrary constraint, or if the optimizer or sampler failed (local minimum, bound, non-convergence), the precise estimate does not measure the intended construct.
</details>

<div dir="rtl">

**3.** توضیح دهید چطور یک پارامتر می‌تواند خیلی دقیق برآورد شود (CI یا پسین باریک) و با این حال بی‌معنی باشد.
<details><summary>پاسخ</summary>
دقت فقط انحنای درست‌نمایی را تحت مدل فرض‌شده نشان می‌دهد. اگر مدل بد مشخص شده باشد (در PPC/$G^2$ رد شود)، اگر پارامتر با پارامتر دیگری معاوضه شود طوری که معنایش به یک قید دلبخواه بستگی داشته باشد، یا اگر بهینه‌ساز یا نمونه‌گیر شکست خورده باشد (کمینه‌ی محلی، کران، عدم همگرایی)، برآورد دقیق سازه‌ی مورد نظر را نمی‌سنجد.
</details>

</div>

**4.** Why do hierarchical models often give better individual estimates than separate individual fits?
<details><summary>Answer</summary>
They share information across participants through the group distribution, shrinking noisy individual estimates toward the group mean in proportion to their uncertainty. This reduces estimation variance more than it adds bias, so estimates are on average closer to the truth.
</details>

<div dir="rtl">

**4.** چرا مدل‌های سلسله‌مراتبی اغلب برآوردهای فردی بهتری از برازش‌های فردی جداگانه می‌دهند؟
<details><summary>پاسخ</summary>
از طریق توزیع گروه بین شرکت‌کننده‌ها اطلاعات به اشتراک می‌گذارند و برآوردهای فردی پرنویز را به نسبت عدم قطعیتشان به سمت میانگین گروه shrink می‌کنند. این واریانس برآورد را بیشتر از سوگیری‌ای که اضافه می‌کند کم می‌کند، پس برآوردها به‌طور میانگین به حقیقت نزدیک‌ترند.
</details>

</div>

**5.** Name three different ways in which this course used simulation, and why each matters.
<details><summary>Answer</summary>
(i) Exploring a model's predictions before fitting (what can and can't it produce). (ii) Parameter and model recovery (can the design and method answer the question). (iii) Bootstrap and predictive checks (uncertainty and adequacy). Further: Monte Carlo and MCMC for computing posteriors.
</details>

<div dir="rtl">

**5.** سه راه مختلفی را که این درس از شبیه‌سازی استفاده کرد نام ببرید و بگویید چرا هرکدام مهم است.
<details><summary>پاسخ</summary>
(1) کاوش پیش‌بینی‌های مدل پیش از برازش (چه چیزی را می‌تواند و نمی‌تواند تولید کند). (2) بازیابی پارامتر و مدل (آیا طرح و روش می‌توانند به سؤال جواب دهند). (3) bootstrap و بررسی‌های پیش‌بینی (عدم قطعیت و کفایت). همچنین: Monte Carlo و MCMC برای محاسبه‌ی پسین‌ها.
</details>

</div>

**6.** A model has the best AIC among four candidates but a posterior predictive check shows a systematic misfit at long delays. What do you report and conclude?
<details><summary>Answer</summary>
Report both. The model is the best of the candidates for prediction, but it is not adequate in absolute terms: none of the candidates captures the long-delay behavior. Conclusions should be restricted accordingly, and a model revision targeting that feature is the next step.
</details>

<div dir="rtl">

**6.** یک مدل بین چهار نامزد بهترین AIC را دارد ولی بررسی پیش‌بینی پسین یک ناهمخوانی نظام‌مند در تأخیرهای طولانی نشان می‌دهد. چه گزارش می‌کنید و چه نتیجه می‌گیرید؟
<details><summary>پاسخ</summary>
هر دو را گزارش کنید. مدل برای پیش‌بینی بهترینِ نامزدهاست، ولی به‌طور مطلق کفایت ندارد: هیچ‌کدام از نامزدها رفتار تأخیرهای طولانی را نمی‌گیرد. نتیجه‌گیری‌ها باید به همین نسبت محدود شوند، و قدم بعدی بازنگری مدل با هدف همان ویژگی است.
</details>

</div>

---

## Assignment · تکلیف

### Final project: written report and code · پروژه‌ی پایانی: گزارش کتبی و کد

- **Due:** one week after this session, and in any case before the final exam (exact date on the course page).
- **Submission:** report (PDF, max. 10 pages for individuals, 14 for pairs, excluding references and appendix) plus a code archive or repository link that reproduces all results.
- **Grading:** see the project brief and rubric (`assessments/project_brief.md`). The report and code are worth 3 of the 6 project points; the proposal (1) and presentation (2) are already graded.
- **Use the feedback** from today: the rubric rewards visible responses to presentation feedback.

<div dir="rtl">

- **مهلت:** یک هفته بعد از این جلسه، و در هر حال پیش از امتحان پایانی (تاریخ دقیق در صفحه‌ی درس).
- **تحویل:** گزارش (PDF، حداکثر 10 صفحه برای انفرادی و 14 برای دونفره، بدون منابع و پیوست) به‌علاوه‌ی یک آرشیو کد یا لینک repository که همه‌ی نتایج را بازتولید کند.
- **نمره‌دهی:** شرح پروژه و rubric را ببینید (`assessments/project_brief.md`). گزارش و کد 3 نمره از 6 نمره‌ی پروژه را دارند؛ پیشنهاد (1) و ارائه (2) قبلاً نمره گرفته‌اند.
- **از بازخورد امروز استفاده کنید:** rubric به پاسخ‌های قابل مشاهده به بازخورد ارائه نمره می‌دهد.

</div>

### Final exam · امتحان پایانی

Written, cumulative (emphasis on Chapters 4–6), formula sheet provided, no laptops; worth 3 of 20 points. See `assessments/final_exam.md` for the format and a sample paper.

<div dir="rtl">

کتبی، جامع (با تأکید بر فصل‌های 4–6)، با برگه‌ی فرمول، بدون لپ‌تاپ؛ 3 نمره از 20. برای قالب و یک نمونه سؤال `assessments/final_exam.md` را ببینید.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Farrell & Lewandowsky (2018)**: the chapter on using models in psychology (the role of models in theory development and common pitfalls) [verify chapter number].
- **Lee & Wagenmakers (2014)**: browse the case studies in Part IV for ideas on how to extend your project.
- **Martin, Kumar & Lao (2021), chapter 9.** End-to-end Bayesian workflows, a good model for structuring a report.
- *Optional, outside the course list:* Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, e49547.

<div dir="rtl">

- **Farrell & Lewandowsky (2018)**: فصل استفاده از مدل‌ها در روان‌شناسی (نقش مدل‌ها در توسعه‌ی نظریه و دام‌های رایج) [شماره‌ی فصل بررسی شود].
- **Lee & Wagenmakers (2014)**: مطالعه‌های موردی بخش IV را برای ایده‌هایی درباره‌ی گسترش پروژه‌تان مرور کنید.
- **Martin, Kumar & Lao (2021)، فصل 9.** گردش‌های کار بیزی از ابتدا تا انتها، الگویی خوب برای ساختار دادن به یک گزارش.
- *اختیاری، خارج از فهرست درس:* Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, e49547.

</div>

**Thank you for a great course, and keep modeling!**

<div dir="rtl">

**از همراهی‌تان در این درس سپاسگزاریم؛ به مدل‌سازی ادامه دهید!**

</div>
