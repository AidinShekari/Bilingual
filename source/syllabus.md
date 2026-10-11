# Syllabus: Cognitive Modeling · طرح درس: مدل‌سازی شناختی (Cognitive Modeling)

| | |
|---|---|
| **Course** | Cognitive Modeling (elective specialization course) |
| **Credits** | 2 units: 1 theory unit (16 h) + 1 practical unit (32 h) = 48 h |
| **Format** | 16 weeks × (1 h lecture + 2 h hands-on lab) |
| **Audience** | MSc students and final-year BSc students in cognitive science, psychology, computer science and AI |
| **Prerequisites** | Statistical methods in cognitive science; experimental methods in cognitive psychology. Basic probability, statistics and introductory programming are assumed; Bayesian statistics is *not* assumed. |
| **Instructor** | *[name, office, e-mail, office hours]* |
| **Teaching assistant** | *[name, e-mail, lab hours]* |
| **Course page** | *[LMS link]* |

<div dir="rtl">

| | |
|---|---|
| **نام درس** | مدل‌سازی شناختی (درس اختیاری تخصصی) |
| **واحد** | 2 واحد: 1 واحد نظری (16 ساعت) + 1 واحد عملی (32 ساعت) = 48 ساعت |
| **شکل برگزاری** | 16 هفته × (1 ساعت درس + 2 ساعت lab عملی) |
| **مخاطبان** | دانشجویان کارشناسی ارشد و سال آخر کارشناسی در علوم شناختی، روان‌شناسی، علوم کامپیوتر و هوش مصنوعی |
| **پیش‌نیازها** | روش‌های آماری در علوم شناختی؛ روش‌های آزمایشی در روان‌شناسی شناختی. فرض بر این است که دانشجو با احتمال، آمار و برنامه‌نویسی مقدماتی آشناست؛ آشنایی با آمار بیزی لازم *نیست*. |
| **مدرس** | *[نام، اتاق، ایمیل، ساعت حضور]* |
| **دستیار آموزشی** | *[نام، ایمیل، ساعت‌های lab]* |
| **صفحه‌ی درس** | *[لینک سامانه‌ی آموزشی (LMS)]* |

</div>

---

## Course description · شرح درس

Cognitive models are explicit, mathematical or computational descriptions of the processes behind behavior. This course teaches how to build such models, fit them to experimental data, evaluate them, and interpret what they say about the mind. We move from intuition to formalism to code to interpretation: from the logic of a model, through least-squares and maximum-likelihood estimation, model evaluation and Bayesian inference, to Markov chain Monte Carlo and hierarchical models. We finish with models from memory, perception, categorization, decision making and learning, and their links to artificial intelligence. Every week includes a two-hour lab in Python in which students fit, evaluate and interpret a model on (simulated or real) experimental data.

<div dir="rtl">

مدل‌های شناختی توصیف‌های صریح، ریاضی یا محاسباتی، از فرایندهایی هستند که پشت رفتار قرار دارند. در این درس یاد می‌گیریم چنین مدل‌هایی را بسازیم، روی داده‌های آزمایشی برازش (fit) کنیم، ارزیابی کنیم، و تفسیر کنیم که درباره‌ی ذهن چه می‌گویند. مسیر درس از شهود به فرمول، از فرمول به کد، و از کد به تفسیر است: از منطق یک مدل، با گذر از برآورد کمترین مربعات (least squares) و بیشینه درست‌نمایی (maximum likelihood)، ارزیابی مدل و استنباط بیزی، تا Markov chain Monte Carlo (MCMC) و مدل‌های سلسله‌مراتبی (hierarchical). درس را با مدل‌هایی از حوزه‌های حافظه، ادراک، دسته‌بندی (categorization)، تصمیم‌گیری و یادگیری، و ارتباط آن‌ها با هوش مصنوعی تمام می‌کنیم. هر هفته یک lab دوساعته با Python داریم که در آن دانشجویان یک مدل را روی داده‌ی آزمایشی (شبیه‌سازی‌شده یا واقعی) برازش، ارزیابی و تفسیر می‌کنند.

</div>

## Learning goals · اهداف یادگیری

**General goals.** By the end of the course students will be familiar with:
1. different approaches to and models of cognitive modeling;
2. how to design a model to address a cognitive problem;
3. applications of modeling in cognitive science and artificial intelligence.

<div dir="rtl">

**اهداف کلی.** در پایان درس، دانشجویان با موارد زیر آشنا خواهند بود:
1. رویکردها و مدل‌های مختلف مدل‌سازی شناختی؛
2. چگونگی طراحی یک مدل برای حل یک مسئله‌ی شناختی؛
3. کاربردهای مدل‌سازی در علوم شناختی و هوش مصنوعی.

</div>

**Specific goals.** Students will gain the skills to:
1. implement modeling methods on experimental data;
2. interpret research results obtained with cognitive models.

<div dir="rtl">

**اهداف ویژه.** دانشجویان مهارت‌های زیر را کسب می‌کنند:
1. پیاده‌سازی روش‌های مدل‌سازی روی داده‌های آزمایشی؛
2. تفسیر نتایج پژوهشی به‌دست‌آمده با مدل‌های شناختی.

</div>

## Topics · سرفصل‌ها

1. Fundamentals of cognitive modeling
2. Parameter estimation methods (least squares / mean squared error, maximum likelihood)
3. Evaluation of cognitive models
4. Bayesian modeling
5. Parameter estimation with data-driven methods (Monte Carlo, Metropolis–Hastings and Gibbs sampling, MCMC)
6. Examples of modeling in different areas of cognitive science

<div dir="rtl">

1. مبانی مدل‌سازی شناختی
2. روش‌های برآورد پارامتر (کمترین مربعات / میانگین مربعات خطا یا MSE، بیشینه درست‌نمایی)
3. ارزیابی مدل‌های شناختی
4. مدل‌سازی بیزی
5. برآورد پارامتر با روش‌های داده‌محور (Monte Carlo، نمونه‌گیری Metropolis–Hastings و Gibbs، MCMC)
6. نمونه‌هایی از مدل‌سازی در حوزه‌های مختلف علوم شناختی

</div>

## Weekly schedule · برنامه‌ی هفتگی

| Week | Chapter | Lecture | Lab | Due |
|---|---|---|---|---|
| 1 | 1 | What is a cognitive model? Marr's levels; notation | Install the course environment; simulate a random walk | — |
| 2 | 1 | Anatomy of a model: SDT and forgetting curves | SDT, ROC/zROC; forgetting curves with binomial noise | A0 |
| 3 | 2 | Least squares, error surfaces and optimization | Grid search, Nelder–Mead, L-BFGS-B; failure modes | — |
| 4 | 2 | Maximum likelihood | Binomial MLE; $G^2$; multi-condition SDT | A1 |
| 5 | 2 | Uncertainty; fitting many participants | Hessian, profile and bootstrap CIs; aggregation artifacts | — |
| 6 | 3 | Fit vs. generalization; cross-validation | Overfitting; K-fold CV; generalization criterion | A2 |
| 7 | 3 | LRT, AIC/BIC; parameter and model recovery | Recovery studies; confusion matrices | Project teams |
| 8 | 1–3 | Midterm review: the whole pipeline | **Midterm exam** (90 min) + project consultation | — |
| 9 | 4 | Bayesian modeling I: priors, posteriors, grids | Beta-binomial; 2-D grid posterior for SDT; prior predictive checks | A3, project proposal |
| 10 | 4 | Bayesian modeling II: PPCs and Bayes factors | PPC; Bayes factors by grid and Savage–Dickey; prior sensitivity | — |
| 11 | 5 | Monte Carlo and Metropolis–Hastings | Metropolis from scratch; tuning | — |
| 12 | 5 | Gibbs sampling; convergence diagnostics | Gibbs from scratch; R-hat and ESS; ArviZ | A4 |
| 13 | 5 | Probabilistic programming; hierarchical models | Hierarchical SDT in PyMC | Progress check |
| 14 | 6 | Categorization (GCM) and decisions (drift-diffusion) | GCM vs. prototype; EZ-diffusion | A5 |
| 15 | 6 | Reinforcement learning, Bayesian cognition and AI | Q-learning fits and recovery; ideal observer | — |
| 16 | — | Synthesis and good modeling practice | **Project presentations** | Presentations |
| Exam period | 1–6 | — | **Final exam** (120 min) | Report + code (before the exam) |

<div dir="rtl">

| هفته | فصل | درس نظری | lab | موعد تحویل |
|---|---|---|---|---|
| 1 | 1 | مدل شناختی چیست؟ سطوح تحلیل Marr؛ نمادگذاری | نصب محیط نرم‌افزاری درس؛ شبیه‌سازی random walk | — |
| 2 | 1 | کالبدشکافی یک مدل: SDT و منحنی‌های فراموشی | SDT و ROC/zROC؛ منحنی فراموشی با نویز دوجمله‌ای | A0 |
| 3 | 2 | کمترین مربعات، سطح خطا و بهینه‌سازی | جستجوی شبکه‌ای (grid search)، Nelder–Mead، L-BFGS-B؛ حالت‌های شکست | — |
| 4 | 2 | بیشینه درست‌نمایی | MLE دوجمله‌ای؛ $G^2$؛ SDT چندشرطی | A1 |
| 5 | 2 | عدم قطعیت؛ برازش برای چند شرکت‌کننده | بازه‌های اطمینان Hessian، profile و bootstrap؛ خطاهای ناشی از میانگین‌گیری | — |
| 6 | 3 | برازش در برابر تعمیم‌پذیری؛ cross-validation | overfitting؛ K-fold CV؛ معیار تعمیم | A2 |
| 7 | 3 | LRT، AIC/BIC؛ بازیابی پارامتر و مدل | مطالعات بازیابی؛ confusion matrix | تشکیل گروه‌های پروژه |
| 8 | 1–3 | مرور میان‌ترم: کل مسیر مدل‌سازی | **آزمون میان‌ترم** (90 دقیقه) + مشاوره‌ی پروژه | — |
| 9 | 4 | مدل‌سازی بیزی 1: پیشین، پسین، شبکه | Beta-binomial؛ پسین شبکه‌ای دوبعدی برای SDT؛ بررسی پیش‌بینی پیشین | A3، پیشنهاد پروژه |
| 10 | 4 | مدل‌سازی بیزی 2: PPC و Bayes factor | PPC؛ Bayes factor با شبکه و Savage–Dickey؛ حساسیت به پیشین | — |
| 11 | 5 | Monte Carlo و Metropolis–Hastings | Metropolis از صفر؛ تنظیم (tuning) | — |
| 12 | 5 | نمونه‌گیری Gibbs؛ تشخیص همگرایی | Gibbs از صفر؛ R-hat و ESS؛ ArviZ | A4 |
| 13 | 5 | برنامه‌نویسی احتمالاتی؛ مدل‌های سلسله‌مراتبی | SDT سلسله‌مراتبی در PyMC | گزارش پیشرفت |
| 14 | 6 | دسته‌بندی (GCM) و تصمیم‌گیری (drift-diffusion) | GCM در برابر prototype؛ EZ-diffusion | A5 |
| 15 | 6 | یادگیری تقویتی، شناخت بیزی و هوش مصنوعی | برازش و بازیابی Q-learning؛ مشاهده‌گر ایده‌آل | — |
| 16 | — | جمع‌بندی و اصول مدل‌سازی خوب | **ارائه‌ی پروژه‌ها** | ارائه‌ها |
| دوره‌ی امتحانات | 1–6 | — | **آزمون پایان‌ترم** (120 دقیقه) | گزارش + کد (پیش از آزمون) |

</div>

Detailed materials for each week are in `weekNN_*.md`.

<div dir="rtl">

مواد کامل هر هفته در فایل‌های `weekNN_*.md` است.

</div>

## Assessment (0–20 scale) · ارزشیابی (از 20)

| Component | Points |
|---|---|
| Lab check-offs (weekly in-lab exercises) | 2.0 |
| Assignments A1–A5 (1.0 each; A0 required, ungraded) | 5.0 |
| In-lecture quizzes (about 10; lowest 2 dropped) | 1.0 |
| Midterm exam (Week 8) | 3.0 |
| Final project: proposal 1.0 · presentation 2.0 · report + code 3.0 | 6.0 |
| Final exam (cumulative, emphasis on Chapters 4–6) | 3.0 |
| **Total** | **20.0** |

<div dir="rtl">

| بخش | نمره |
|---|---|
| تأیید تمرین‌های lab (تمرین‌های هفتگی سر کلاس) | 2.0 |
| تکالیف A1 تا A5 (هرکدام 1.0؛ A0 الزامی ولی بدون نمره) | 5.0 |
| کوییزهای سر کلاس (حدود 10 کوییز؛ 2 نمره‌ی پایین حذف می‌شود) | 1.0 |
| آزمون میان‌ترم (هفته‌ی 8) | 3.0 |
| پروژه‌ی پایانی: پیشنهاد 1.0 · ارائه 2.0 · گزارش + کد 3.0 | 6.0 |
| آزمون پایان‌ترم (جامع، با تأکید بر فصل‌های 4 تا 6) | 3.0 |
| **جمع** | **20.0** |

</div>

Details, rubrics and policies are in [`assessments/`](assessments/README.md).

<div dir="rtl">

جزئیات، روبریک‌ها و قوانین در پوشه‌ی [`assessments/`](assessments/README.md) آمده است.

</div>

## Policies (summary) · قوانین (خلاصه)

- **Late work:** −10% per day, maximum 3 days.
- **Collaboration:** discuss freely; write your own code and text (the project is a team product for pairs). Acknowledge discussions and reused code.
- **AI tools:** allowed for debugging, explanations and language editing. State how you used them; you must be able to explain everything you submit.
- **Exams:** closed book, formula sheet provided, non-programmable calculator allowed.
- **Attendance:** labs are where most learning happens; lab check-offs require attendance (or an agreed alternative).
- **Accessibility:** students needing accommodations should contact the instructor in the first two weeks.

<div dir="rtl">

- **تأخیر در تحویل:** 10% کسر نمره برای هر روز، حداکثر 3 روز.
- **همکاری:** گفت‌وگو آزاد است، ولی کد و متن را خودتان بنویسید (برای گروه‌های دونفره، پروژه کار مشترک گروه است). گفت‌وگوها و کدهای استفاده‌شده‌ی دیگران را ذکر کنید.
- **ابزارهای هوش مصنوعی:** برای رفع اشکال (debugging)، توضیح مفاهیم و ویرایش زبانی مجاز است. نحوه‌ی استفاده را بنویسید؛ باید بتوانید همه‌ی آن‌چه تحویل می‌دهید را توضیح دهید.
- **آزمون‌ها:** کتاب‌بسته، برگه‌ی فرمول داده می‌شود، ماشین‌حساب غیربرنامه‌پذیر مجاز است.
- **حضور:** بیشترِ یادگیری در lab اتفاق می‌افتد؛ تأیید تمرین‌های lab به حضور (یا یک جایگزین توافق‌شده) نیاز دارد.
- **دسترس‌پذیری:** دانشجویانی که به شرایط ویژه نیاز دارند در دو هفته‌ی اول با مدرس تماس بگیرند.

</div>

## Software · نرم‌افزار

Python 3.11+ with numpy, scipy, pandas, matplotlib, JupyterLab, PyMC and ArviZ, installed on students' own laptops in Week 1 (Miniforge/conda-forge recommended; Google Colab as fallback). See `environment.yml`, `requirements.txt` and the Week 1 lab.

<div dir="rtl">

Python 3.11 یا بالاتر با کتابخانه‌های numpy، scipy، pandas، matplotlib، JupyterLab، PyMC و ArviZ که در هفته‌ی 1 روی لپ‌تاپ خود دانشجویان نصب می‌شود (Miniforge/conda-forge توصیه می‌شود؛ Google Colab گزینه‌ی جایگزین است). فایل‌های `environment.yml` و `requirements.txt` (در پوشه‌ی اصلی) و lab هفته‌ی 1 را ببینید.

</div>

## Readings · منابع

Main references (see [`reading_list.md`](reading_list.md) for the chapter mapping):
- Farrell, S., & Lewandowsky, S. (2018). *Computational modeling of cognition and behavior.* Cambridge University Press. **(primary text, Weeks 1–8)**
- Lee, M. D., & Wagenmakers, E.-J. (2014). *Bayesian cognitive modeling: A practical course.* Cambridge University Press. **(primary text, Weeks 9–14)**
- Kruschke, J. K. (2014). *Doing Bayesian data analysis: A tutorial with R, JAGS, and Stan* (2nd ed.). Academic Press.
- Martin, O. A., Kumar, R., & Lao, J. (2021). *Bayesian modeling and computation in Python.* Chapman and Hall/CRC.
- Anderson, B. (2014). *Computational neuroscience and cognitive modelling: A student's introduction to methods and procedures.* SAGE.
- Verguts, T. (2022). *Introduction to modeling cognitive processes.* MIT Press.
- Ghodousian, A. (1401). *Mabani-ye ravesh-haye mostaghim dar behine-sazi gheyr-khatti* [Foundations of direct methods in nonlinear optimization] (in Persian).
- Azimifar, Z., & Ahmadi, E. (1396). *Shenasayi-ye amari-ye olgu: yadgiri-ye nazari-ye moghaddamati* [Statistical pattern recognition: Introductory learning theory], vol. 1 (in Persian).

<div dir="rtl">

منابع اصلی (برای ارتباط فصل‌ها با هفته‌ها فایل [`reading_list.md`](reading_list.md) را ببینید):
- Farrell, S., & Lewandowsky, S. (2018). *Computational modeling of cognition and behavior.* Cambridge University Press. **(کتاب اصلی، هفته‌های 1 تا 8)**
- Lee, M. D., & Wagenmakers, E.-J. (2014). *Bayesian cognitive modeling: A practical course.* Cambridge University Press. **(کتاب اصلی، هفته‌های 9 تا 14)**
- Kruschke, J. K. (2014). *Doing Bayesian data analysis: A tutorial with R, JAGS, and Stan* (2nd ed.). Academic Press.
- Martin, O. A., Kumar, R., & Lao, J. (2021). *Bayesian modeling and computation in Python.* Chapman and Hall/CRC.
- Anderson, B. (2014). *Computational neuroscience and cognitive modelling: A student's introduction to methods and procedures.* SAGE.
- Verguts, T. (2022). *Introduction to modeling cognitive processes.* MIT Press.
- قدوسیان، ع. (1401). *مبانی روش‌های مستقیم در بهینه‌سازی غیرخطی.*
- عظیمی‌فر، ز. و احمدی، ا. (1396). *شناسایی آماری الگو: یادگیری نظری مقدماتی*، جلد 1.

</div>
