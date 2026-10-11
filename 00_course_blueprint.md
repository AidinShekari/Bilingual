# Cognitive Modeling: Course Blueprint (16 weeks) · مدل‌سازی شناختی: نقشه‌ی کلی درس (16 هفته)

**Credits:** 2 units (1 theory + 1 practical), 48 h in total · **Format:** 1 h lecture + 2 h lab per week
**Audience:** MSc and final-year BSc students · **Prerequisites:** statistical methods in cognitive science; experimental methods in cognitive psychology
**Language / tools:** English · Python 3 (numpy, scipy, pandas, matplotlib; PyMC + ArviZ from Week 13), run on students' own laptops

<div dir="rtl">

**واحد:** 2 واحد (1 نظری + 1 عملی)، در مجموع 48 ساعت · **شکل برگزاری:** هر هفته 1 ساعت درس + 2 ساعت lab
**مخاطبان:** دانشجویان کارشناسی ارشد و سال آخر کارشناسی · **پیش‌نیازها:** روش‌های آماری در علوم شناختی؛ روش‌های آزمایشی در روان‌شناسی شناختی
**زبان / ابزار:** Python 3 (numpy، scipy، pandas، matplotlib؛ و از هفته‌ی 13 به بعد PyMC + ArviZ)، روی لپ‌تاپ خود دانشجویان

</div>

## Design principles · اصول طراحی

- **One modeling pipeline used all term.** Every lab follows the same steps: *simulate → fit → evaluate → recover → interpret*.
- **A few datasets come back again and again.** Forgetting curves and signal detection theory (SDT) run through Weeks 2–13, so new methods are compared on familiar data. Chapter 6 adds categorization (GCM), response times (drift-diffusion) and reinforcement learning.
- **"Write it yourself, then use the library."** Students write least squares, maximum likelihood, grid posteriors, Metropolis–Hastings, Gibbs and R-hat by hand before using `scipy.optimize`, PyMC or ArviZ.
- **Chapter weighting.** Ch1: 2 weeks · Ch2: 3 · Ch3: 2 · Ch4: 2 · Ch5: 3 · Ch6: 2. One more week each goes to orientation, the midterm and project presentations.
- **"Metropolis–Gibbs" means two separate algorithms:** Metropolis–Hastings (Week 11) and Gibbs sampling (Week 12). MH-within-Gibbs is covered as an Advanced box.

<div dir="rtl">

- **یک مسیر مدل‌سازی ثابت برای کل ترم.** همه‌ی labها همین مراحل را دنبال می‌کنند: *شبیه‌سازی (simulate) ← برازش (fit) ← ارزیابی (evaluate) ← بازیابی (recover) ← تفسیر (interpret)*.
- **چند مجموعه‌داده‌ی ثابت که مدام تکرار می‌شوند.** منحنی‌های فراموشی و نظریه‌ی تشخیص علامت (SDT) از هفته‌ی 2 تا 13 ادامه دارند، تا روش‌های جدید روی داده‌های آشنا مقایسه شوند. فصل 6 دسته‌بندی (GCM)، زمان واکنش (drift-diffusion) و یادگیری تقویتی (reinforcement learning) را اضافه می‌کند.
- **«اول خودت بنویس، بعد از کتابخانه استفاده کن.»** دانشجویان کمترین مربعات، بیشینه درست‌نمایی، پسین شبکه‌ای، Metropolis–Hastings، Gibbs و R-hat را دستی می‌نویسند و بعد سراغ `scipy.optimize`، PyMC یا ArviZ می‌روند.
- **وزن فصل‌ها.** فصل 1: 2 هفته · فصل 2: 3 · فصل 3: 2 · فصل 4: 2 · فصل 5: 3 · فصل 6: 2. سه هفته‌ی دیگر هم به معارفه، میان‌ترم و ارائه‌ی پروژه‌ها اختصاص دارد.
- **«Metropolis–Gibbs» یعنی دو الگوریتم جدا:** Metropolis–Hastings (هفته‌ی 11) و نمونه‌گیری Gibbs (هفته‌ی 12). روش MH-within-Gibbs در یک کادر «پیشرفته» آمده است.

</div>

## Weekly plan · برنامه‌ی هفتگی

| Wk | Ch | Lecture (1 h) | Lab (2 h) | Learning outcomes | Readings | Assignment / milestone |
|---|---|---|---|---|---|---|
| 1 | 1 | **Orientation: what is a cognitive model?** Why we model; verbal vs. formal theories; Marr's three levels; model families (symbolic, connectionist, stochastic/dynamical, Bayesian); course roadmap; **notation table** | **Laptop setup** (Miniforge/conda environment with the full course stack *including PyMC*, run an install-check script; Colab as fallback); simulate a random walk to a bound and plot simulated "data" | Distinguish descriptive, process and normative models; explain why verbal theories are underspecified; run and plot a model simulation | F&L ch. 1–2; Verguts, introductory chapter [verify]; Anderson, introductory chapter [verify] | **A0** (ungraded): install check plus a one-page note: "Pick a verbal theory; list what it leaves unspecified" |
| 2 | 1 | **Anatomy of a model:** data, free vs. fixed parameters, model equations, noise (data) model; simulation as a thinking tool; first models: SDT ($d'$, $c$) and exponential vs. power forgetting | Implement SDT ($d'$, $c$, ROC curves); simulate exponential and power forgetting; explore how each parameter changes the predictions | Identify the components of a formal model; compute $d'$ and $c$; predict how parameters shape model output | F&L ch. 2; L&W ch. 11 (SDT, a preview) | **A1 released:** "From verbal to formal" (due Wk 4) |
| 3 | 2 | **Least squares & optimization:** SSE, MSE, RMSD; error surfaces; grid search, Nelder–Mead, gradient methods; local minima, starting values, bounds and reparameterization | Fit forgetting curves by grid search, then with `scipy.optimize.minimize`; plot the error surface; multi-start fitting | Implement an LS fit from scratch; compare optimizers; diagnose failed fits | F&L ch. 3; Ghodousian (direct search methods) | — |
| 4 | 2 | **Maximum likelihood:** probability vs. likelihood; log-likelihood; Bernoulli, binomial and Gaussian likelihoods; LS as MLE under Gaussian noise | MLE for forgetting data (binomial recall counts) and for SDT; compare MLE and LS estimates | Derive a likelihood; implement NLL minimization; explain when LS and MLE agree | F&L ch. 4; Azimifar & Ahmadi (ML estimation) | **A1 due · A2 released:** LS vs. MLE (due Wk 6) |
| 5 | 2 | **Uncertainty & multiple participants:** Hessian standard errors, profile likelihood, parametric bootstrap; individual vs. aggregate fitting; aggregation artifacts | Bootstrap CIs; averaging exponential learners produces a spurious "power law of practice"; individual fits | Quantify estimation uncertainty; explain aggregation artifacts; choose a fitting level | F&L ch. 5 | — |
| 6 | 3 | **Evaluation I, fit vs. generalization:** $R^2$, RMSD and deviance and their limits; flexibility and overfitting; hold-out, k-fold and LOO cross-validation | Polynomial overfitting demo; cross-validated comparison of three forgetting models | Explain why good fit ≠ good model; implement k-fold CV; interpret CV results | F&L ch. 10; Azimifar & Ahmadi (generalization) | **A2 due · A3 released:** comparison + recovery (due Wk 9) |
| 7 | 3 | **Evaluation II, selection & recovery:** likelihood-ratio test; AIC, AICc, BIC, Akaike weights; parameter and model recovery; identifiability and trade-offs | Recovery study: true vs. recovered parameter plots; model-recovery confusion matrix (AIC/BIC) | Interpret information criteria; design a recovery study; detect non-identifiability | F&L ch. 10 | **Project teams (1–2 students) formed; proposal brief released** |
| 8 | 1–3 | **Midterm review:** integrated case study of the full pipeline | **Midterm exam** (lab slot, 90 min): conceptual questions + code reading/interpretation, Ch. 1–3 | — | Review of Weeks 1–7 | **Midterm** |
| 9 | 4 | **Bayesian modeling I:** prior, likelihood, posterior, evidence; beta-binomial conjugacy; grid approximation; posterior summaries and HDI; credible vs. confidence intervals | Grid posterior for a recall probability; 2-D grid for SDT; vary prior and sample size; prior predictive simulation | Compute a grid posterior; explain the role of the prior; interpret credible intervals | K ch. 5–6; L&W ch. 1, 3; MKL ch. 1; F&L ch. 6; Azimifar & Ahmadi (Bayesian estimation) | **A3 due · Project proposal due** |
| 10 | 4 (+3) | **Bayesian modeling II:** posterior predictive checks; marginal likelihood and **Bayes factors**; Savage–Dickey; prior sensitivity; BIC as an approximation | PPCs for the forgetting model; Savage–Dickey BF for $d' > 0$; BF between retention models via grid integration | Conduct a PPC; compute and interpret a Bayes factor; evaluate prior sensitivity | L&W ch. 7; F&L ch. 11; K ch. 10 | **A4 released:** Bayesian analysis by grid (due Wk 12) |
| 11 | 5 | **Monte Carlo & Metropolis–Hastings:** Monte Carlo integration; Markov chains; MH; proposal tuning, acceptance rate, burn-in | **MH from scratch** for the forgetting model; trace plots; compare with the grid posterior | Explain why MCMC works; implement MH; tune a proposal | K ch. 7; F&L ch. 7 | — |
| 12 | 5 | **Gibbs sampling & convergence diagnostics:** full conditionals; Gibbs for a normal model; MH-within-Gibbs (Advanced); multiple chains, **R-hat**, ESS, autocorrelation | **Gibbs from scratch**; implement R-hat and ESS and check against ArviZ; break convergence and diagnose it | Implement Gibbs; interpret R-hat, ESS and trace plots; judge chain trustworthiness | K ch. 7; MKL ch. 2; F&L ch. 7 | **A4 due · A5 released:** MCMC + diagnostics (due Wk 14) |
| 13 | 5 | **Probabilistic programming & hierarchical models:** PyMC; HMC/NUTS conceptually (Advanced); partial pooling and shrinkage (linked to Week 5) | **Hierarchical SDT in PyMC**: ArviZ diagnostics, PPCs, comparison with individual MLE fits; (Advanced) LOO/WAIC | Specify a PyMC model; explain partial pooling; report a full Bayesian workflow | L&W ch. 11; K ch. 9; F&L ch. 9; MKL ch. 2, 10 | **Project progress check** (feedback only) |
| 14 | 6 | **Modeling in cognitive science I:** categorization (prototype vs. exemplar; **GCM**); choice/RT (**drift-diffusion**, EZ-diffusion) | Fit the GCM by MLE to 5–4 category-structure data; EZ-diffusion on simulated RTs; interpret the parameters | Fit an exemplar model; map DDM parameters to cognitive constructs | L&W ch. 17; F&L ch. 14 [verify]; Verguts (relevant chapters [verify]) | **A5 due** |
| 15 | 6 | **Modeling in cognitive science II:** Rescorla–Wagner and Q-learning with softmax; Bayesian *models of cognition* vs. Bayesian *data analysis*; connectionist models and links to AI | Fit Q-learning ($\alpha$, $\beta$) to simulated bandit data; parameter recovery; (Advanced) hierarchical version in PyMC | Fit an RL model; assess identifiability; contrast Bayesian cognition with Bayesian statistics | Verguts (learning/RL chapters [verify]); F&L ch. 13 [verify]; Anderson (relevant chapters [verify]) | Final project work |
| 16 | — | **Final project presentations**; wrap-up on good modeling practice | Presentations continue; peer feedback | Communicate and critique a modeling study | — | **Presentations** · report + code due before the final exam |
| Exam period | 1–6 | **Final exam** (written, cumulative, emphasis on Ch. 4–6; formula sheet provided; code reading/interpretation, no laptops) | — | — | — | **Final exam** |

<div dir="rtl">

| هفته | فصل | درس (1 ساعت) | lab (2 ساعت) | اهداف یادگیری | منابع | تکلیف / نقطه‌ی عطف |
|---|---|---|---|---|---|---|
| 1 | 1 | **معارفه: مدل شناختی چیست؟** چرا مدل می‌سازیم؛ نظریه‌ی کلامی در برابر فرمال؛ سه سطح Marr؛ خانواده‌های مدل (نمادین، پیوندگرا یا connectionist، تصادفی/پویا، بیزی)؛ نقشه‌ی درس؛ **جدول نمادگذاری** | **نصب روی لپ‌تاپ** (محیط Miniforge/conda با همه‌ی ابزارهای درس *از جمله PyMC*، اجرای اسکریپت بررسی نصب؛ Colab به‌عنوان جایگزین)؛ شبیه‌سازی random walk تا رسیدن به مرز و رسم «داده»ی شبیه‌سازی‌شده | تمایز مدل‌های توصیفی، فرایندی و هنجاری؛ توضیح اینکه چرا نظریه‌های کلامی ناقص‌اند؛ اجرا و رسم شبیه‌سازی یک مدل | F&L فصل 1–2؛ Verguts، فصل مقدمه [بررسی شود]؛ Anderson، فصل مقدمه [بررسی شود] | **A0** (بدون نمره): بررسی نصب + یادداشتی یک‌صفحه‌ای: «یک نظریه‌ی کلامی انتخاب کنید و بنویسید چه چیزهایی را مشخص نکرده است» |
| 2 | 1 | **کالبدشکافی یک مدل:** داده، پارامتر آزاد در برابر ثابت، معادلات مدل، مدل نویز (noise/data model)؛ شبیه‌سازی به‌عنوان ابزار فکر کردن؛ اولین مدل‌ها: SDT ($d'$، $c$) و فراموشی نمایی در برابر توانی | پیاده‌سازی SDT ($d'$، $c$، منحنی ROC)؛ شبیه‌سازی فراموشی نمایی و توانی؛ بررسی اثر هر پارامتر روی پیش‌بینی‌ها | شناسایی اجزای یک مدل فرمال؛ محاسبه‌ی $d'$ و $c$؛ پیش‌بینی اثر پارامترها روی خروجی مدل | F&L فصل 2؛ L&W فصل 11 (پیش‌نمایش SDT) | **انتشار A1:** «از کلامی به فرمال» (موعد: هفته‌ی 4) |
| 3 | 2 | **کمترین مربعات و بهینه‌سازی:** SSE، MSE، RMSD؛ سطح خطا؛ جستجوی شبکه‌ای، Nelder–Mead، روش‌های گرادیانی؛ کمینه‌ی محلی، مقدار شروع، کران‌ها و reparameterization | برازش منحنی فراموشی با جستجوی شبکه‌ای و سپس با `scipy.optimize.minimize`؛ رسم سطح خطا؛ برازش چندشروعی (multi-start) | پیاده‌سازی برازش LS از صفر؛ مقایسه‌ی بهینه‌سازها؛ تشخیص برازش‌های ناموفق | F&L فصل 3؛ قدوسیان (روش‌های جستجوی مستقیم) | — |
| 4 | 2 | **بیشینه درست‌نمایی:** احتمال در برابر درست‌نمایی؛ log-likelihood؛ درست‌نمایی برنولی، دوجمله‌ای و گاوسی؛ LS به‌عنوان MLE تحت نویز گاوسی | MLE برای داده‌ی فراموشی (تعداد یادآوری دوجمله‌ای) و برای SDT؛ مقایسه‌ی برآوردهای MLE و LS | استخراج درست‌نمایی؛ پیاده‌سازی کمینه‌سازی NLL؛ توضیح اینکه LS و MLE کی یکسان‌اند | F&L فصل 4؛ عظیمی‌فر و احمدی (برآورد ML) | **موعد A1 · انتشار A2:** LS در برابر MLE (موعد: هفته‌ی 6) |
| 5 | 2 | **عدم قطعیت و چند شرکت‌کننده:** خطای استاندارد از Hessian، profile likelihood، bootstrap پارامتری؛ برازش فردی در برابر تجمیعی؛ خطاهای ناشی از میانگین‌گیری | بازه‌ی اطمینان bootstrap؛ میانگین‌گیری از یادگیرنده‌های نمایی یک «قانون توانی تمرین» کاذب می‌سازد؛ برازش‌های فردی | سنجش عدم قطعیت برآورد؛ توضیح خطای میانگین‌گیری؛ انتخاب سطح برازش | F&L فصل 5 | — |
| 6 | 3 | **ارزیابی 1، برازش در برابر تعمیم‌پذیری:** $R^2$، RMSD و deviance و محدودیت‌هایشان؛ انعطاف‌پذیری و overfitting؛ اعتبارسنجی hold-out، k-fold و LOO | نمایش overfitting با چندجمله‌ای؛ مقایسه‌ی سه مدل فراموشی با cross-validation | توضیح اینکه چرا برازش خوب ≠ مدل خوب؛ پیاده‌سازی k-fold CV؛ تفسیر نتایج CV | F&L فصل 10؛ عظیمی‌فر و احمدی (تعمیم‌پذیری) | **موعد A2 · انتشار A3:** مقایسه + بازیابی (موعد: هفته‌ی 9) |
| 7 | 3 | **ارزیابی 2، انتخاب و بازیابی:** آزمون نسبت درست‌نمایی؛ AIC، AICc، BIC و وزن‌های Akaike؛ بازیابی پارامتر و مدل؛ identifiability و trade-off پارامترها | مطالعه‌ی بازیابی: نمودار پارامتر واقعی در برابر بازیابی‌شده؛ confusion matrix بازیابی مدل (AIC/BIC) | تفسیر معیارهای اطلاعاتی؛ طراحی مطالعه‌ی بازیابی؛ تشخیص non-identifiability | F&L فصل 10 | **تشکیل گروه‌های پروژه (1 تا 2 نفر)؛ انتشار راهنمای پیشنهاد پروژه** |
| 8 | 1–3 | **مرور میان‌ترم:** یک مطالعه‌ی موردی یکپارچه از کل مسیر | **آزمون میان‌ترم** (در زمان lab، 90 دقیقه): سؤال مفهومی + خواندن و تفسیر کد، فصل‌های 1 تا 3 | — | مرور هفته‌های 1 تا 7 | **میان‌ترم** |
| 9 | 4 | **مدل‌سازی بیزی 1:** پیشین، درست‌نمایی، پسین، شواهد (evidence)؛ conjugacy beta-binomial؛ تقریب شبکه‌ای؛ خلاصه‌های پسین و HDI؛ credible interval در برابر بازه‌ی اطمینان | پسین شبکه‌ای برای احتمال یادآوری؛ شبکه‌ی دوبعدی برای SDT؛ تغییر پیشین و حجم نمونه؛ شبیه‌سازی پیش‌بینی پیشین | محاسبه‌ی پسین شبکه‌ای؛ توضیح نقش پیشین؛ تفسیر credible interval | K فصل 5–6؛ L&W فصل 1 و 3؛ MKL فصل 1؛ F&L فصل 6؛ عظیمی‌فر و احمدی (برآورد بیزی) | **موعد A3 · موعد پیشنهاد پروژه** |
| 10 | 4 (+3) | **مدل‌سازی بیزی 2:** بررسی پیش‌بینی پسین (PPC)؛ marginal likelihood و **Bayes factor**؛ Savage–Dickey؛ حساسیت به پیشین؛ BIC به‌عنوان تقریب | PPC برای مدل فراموشی؛ Bayes factor Savage–Dickey برای $d' > 0$؛ Bayes factor بین مدل‌های فراموشی با انتگرال‌گیری شبکه‌ای | انجام PPC؛ محاسبه و تفسیر Bayes factor؛ ارزیابی حساسیت به پیشین | L&W فصل 7؛ F&L فصل 11؛ K فصل 10 | **انتشار A4:** تحلیل بیزی با شبکه (موعد: هفته‌ی 12) |
| 11 | 5 | **Monte Carlo و Metropolis–Hastings:** انتگرال‌گیری Monte Carlo؛ زنجیره‌ی مارکوف؛ MH؛ تنظیم proposal، نرخ پذیرش، burn-in | **MH از صفر** برای مدل فراموشی؛ trace plot؛ مقایسه با پسین شبکه‌ای | توضیح اینکه چرا MCMC کار می‌کند؛ پیاده‌سازی MH؛ تنظیم proposal | K فصل 7؛ F&L فصل 7 | — |
| 12 | 5 | **نمونه‌گیری Gibbs و تشخیص همگرایی:** full conditionalها؛ Gibbs برای مدل نرمال؛ MH-within-Gibbs (پیشرفته)؛ چند زنجیره، **R-hat**، ESS، خودهمبستگی | **Gibbs از صفر**؛ پیاده‌سازی R-hat و ESS و مقایسه با ArviZ؛ خراب کردن عمدی همگرایی و تشخیص آن | پیاده‌سازی Gibbs؛ تفسیر R-hat، ESS و trace plot؛ قضاوت درباره‌ی قابل‌اعتماد بودن زنجیره | K فصل 7؛ MKL فصل 2؛ F&L فصل 7 | **موعد A4 · انتشار A5:** MCMC + تشخیص همگرایی (موعد: هفته‌ی 14) |
| 13 | 5 | **برنامه‌نویسی احتمالاتی و مدل‌های سلسله‌مراتبی:** PyMC؛ HMC/NUTS در سطح مفهومی (پیشرفته)؛ partial pooling و shrinkage (مرتبط با هفته‌ی 5) | **SDT سلسله‌مراتبی در PyMC**: تشخیص با ArviZ، PPC، مقایسه با برازش‌های MLE فردی؛ (پیشرفته) LOO/WAIC | تعریف مدل در PyMC؛ توضیح partial pooling؛ گزارش یک گردش کار (workflow) بیزی کامل | L&W فصل 11؛ K فصل 9؛ F&L فصل 9؛ MKL فصل 2 و 10 | **گزارش پیشرفت پروژه** (فقط بازخورد) |
| 14 | 6 | **مدل‌سازی در علوم شناختی 1:** دسته‌بندی (prototype در برابر exemplar؛ **GCM**)؛ انتخاب/زمان واکنش (**drift-diffusion**، EZ-diffusion) | برازش GCM با MLE روی داده‌ی ساختار دسته‌بندی 5-4؛ EZ-diffusion روی زمان‌های واکنش شبیه‌سازی‌شده؛ تفسیر پارامترها | برازش یک مدل exemplar؛ نگاشت پارامترهای DDM به سازه‌های شناختی | L&W فصل 17؛ F&L فصل 14 [بررسی شود]؛ Verguts (فصل‌های مرتبط [بررسی شود]) | **موعد A5** |
| 15 | 6 | **مدل‌سازی در علوم شناختی 2:** Rescorla–Wagner و Q-learning با softmax؛ *مدل‌های بیزی شناخت* در برابر *تحلیل داده‌ی بیزی*؛ مدل‌های پیوندگرا و ارتباط با هوش مصنوعی | برازش Q-learning ($\alpha$، $\beta$) روی داده‌ی bandit شبیه‌سازی‌شده؛ بازیابی پارامتر؛ (پیشرفته) نسخه‌ی سلسله‌مراتبی در PyMC | برازش یک مدل RL؛ ارزیابی identifiability؛ مقایسه‌ی شناخت بیزی با آمار بیزی | Verguts (فصل‌های یادگیری/RL [بررسی شود])؛ F&L فصل 13 [بررسی شود]؛ Anderson (فصل‌های مرتبط [بررسی شود]) | کار روی پروژه‌ی پایانی |
| 16 | — | **ارائه‌ی پروژه‌های پایانی**؛ جمع‌بندی اصول مدل‌سازی خوب | ادامه‌ی ارائه‌ها؛ بازخورد همتایان | ارائه و نقد یک مطالعه‌ی مدل‌سازی | — | **ارائه‌ها** · گزارش + کد پیش از آزمون پایانی |
| دوره‌ی امتحانات | 1–6 | **آزمون پایان‌ترم** (کتبی، جامع، با تأکید بر فصل‌های 4 تا 6؛ برگه‌ی فرمول داده می‌شود؛ خواندن و تفسیر کد، بدون لپ‌تاپ) | — | — | — | **آزمون پایان‌ترم** |

</div>

**Abbreviations:** F&L = Farrell & Lewandowsky (2018) · L&W = Lee & Wagenmakers (2014) · K = Kruschke (2014) · MKL = Martin, Kumar & Lao (2021).
Chapter numbers were written from memory. The ones marked [verify] are less certain; please check all of them against the books.

<div dir="rtl">

**اختصارها:** F&L = Farrell & Lewandowsky (2018) · L&W = Lee & Wagenmakers (2014) · K = Kruschke (2014) · MKL = Martin, Kumar & Lao (2021).
شماره‌ی فصل‌ها از حافظه نوشته شده‌اند. آن‌هایی که [بررسی شود] دارند کمتر قطعی‌اند؛ لطفاً همه را با خود کتاب‌ها مقایسه کنید.

</div>

## Grading (0–20 scale) · نمره‌دهی (از 20)

| Component | Points |
|---|---|
| Lab check-offs (weekly in-lab exercises) | 2.0 |
| Assignments A1–A5 (1.0 each) | 5.0 |
| Short in-lecture quizzes (≈10, drop the lowest 2) | 1.0 |
| Midterm exam (Week 8) | 3.0 |
| Final project: proposal 1.0 · presentation 2.0 · report + reproducible code 3.0 | 6.0 |
| Final exam (cumulative) | 3.0 |
| **Total** | **20.0** |

<div dir="rtl">

| بخش | نمره |
|---|---|
| تأیید تمرین‌های lab (تمرین‌های هفتگی سر کلاس) | 2.0 |
| تکالیف A1 تا A5 (هرکدام 1.0) | 5.0 |
| کوییزهای کوتاه سر کلاس (حدود 10 کوییز، 2 نمره‌ی پایین حذف) | 1.0 |
| آزمون میان‌ترم (هفته‌ی 8) | 3.0 |
| پروژه‌ی پایانی: پیشنهاد 1.0 · ارائه 2.0 · گزارش + کد بازتولیدپذیر 3.0 | 6.0 |
| آزمون پایان‌ترم (جامع) | 3.0 |
| **جمع** | **20.0** |

</div>

## Final project (overview; the full brief and rubric come in Stage 3) · پروژه‌ی پایانی (نمای کلی؛ شرح کامل و روبریک در فایل `assessments/project_brief.md`)

- **Teams of 1–2.** The scope grows with team size. Everyone fits at least two candidate models, runs one model comparison and one parameter-recovery analysis. **Pairs also** do a Bayesian/MCMC analysis (or a hierarchical model) and submit an individual contribution statement.
- **Data:** simulated data, an open dataset, or the student's own experimental data.
- **Milestones:** team formation (Wk 7) → proposal (Wk 9) → progress check (Wk 13) → presentation (Wk 16) → report + code (before the final exam).

<div dir="rtl">

- **گروه‌های 1 یا 2 نفره.** حجم کار با تعداد اعضا بیشتر می‌شود. همه حداقل دو مدل رقیب را برازش می‌کنند، یک مقایسه‌ی مدل و یک تحلیل بازیابی پارامتر انجام می‌دهند. **گروه‌های دونفره علاوه بر این** یک تحلیل بیزی/MCMC (یا یک مدل سلسله‌مراتبی) انجام می‌دهند و بیانیه‌ی سهم فردی تحویل می‌دهند.
- **داده:** داده‌ی شبیه‌سازی‌شده، یک مجموعه‌داده‌ی باز، یا داده‌ی آزمایشی خود دانشجو.
- **نقاط عطف:** تشکیل گروه (هفته‌ی 7) ← پیشنهاد (هفته‌ی 9) ← گزارش پیشرفت (هفته‌ی 13) ← ارائه (هفته‌ی 16) ← گزارش + کد (پیش از آزمون پایانی).

</div>

## Computing on students' own laptops · محاسبه روی لپ‌تاپ دانشجویان

- The full environment, PyMC included, is installed in **Week 1**, so Windows/macOS installation problems are solved long before Week 13.
- Recommended route: **Miniforge (conda-forge)** with a course `environment.yml`, plus a pip `requirements.txt` as an alternative (both delivered in Stage 4).
- **Fallback:** every notebook also runs on Google Colab.

<div dir="rtl">

- کل محیط نرم‌افزاری، از جمله PyMC، در **هفته‌ی 1** نصب می‌شود تا مشکلات نصب روی Windows/macOS خیلی پیش از هفته‌ی 13 حل شوند.
- مسیر پیشنهادی: **Miniforge (conda-forge)** با فایل `environment.yml` درس، و فایل `requirements.txt` برای pip به‌عنوان جایگزین.
- **جایگزین:** همه‌ی notebookها روی Google Colab هم اجرا می‌شوند.

</div>
