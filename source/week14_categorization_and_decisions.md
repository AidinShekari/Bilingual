# Week 14: Modeling in Cognitive Science I: Categorization (GCM) and Decision Making (Drift-Diffusion) · هفته‌ی 14: مدل‌سازی در علوم شناختی 1: دسته‌بندی (GCM) و تصمیم‌گیری (Drift-Diffusion)

> **Chapter 6: Examples of modeling in different areas of cognitive science** · Lecture 1 h · Lab 2 h
> **Running data:** simulated classification data for the classic 5-4 category structure, and simulated choice-RT data from a drift-diffusion process in a speed/accuracy × easy/hard design.

<div dir="rtl">

> **فصل 6: نمونه‌هایی از مدل‌سازی در حوزه‌های مختلف علوم شناختی** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** داده‌ی دسته‌بندی شبیه‌سازی‌شده برای ساختار کلاسیک 5-4، و داده‌ی انتخاب–RT شبیه‌سازی‌شده از یک فرایند drift-diffusion در یک طرح سرعت/دقت × آسان/سخت.

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| categorization | دسته‌بندی | قرار دادن محرک در یک دسته |
| Generalized Context Model (GCM) | مدل بافت تعمیم‌یافته | مدل exemplar دسته‌بندی بر پایه‌ی شباهت |
| drift rate | نرخ رانش | سرعت میانگین جمع شدن شواهد؛ نشانه‌ی کیفیت شواهد |
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| response time (RT) | زمان واکنش | فاصله‌ی ارائه‌ی محرک تا پاسخ |
| drift-diffusion model (DDM) | مدل drift-diffusion (رانش–انتشار) | انباشت پیوسته‌ی شواهد بین دو مرز |
| speed–accuracy trade-off | بده‌بستان سرعت و دقت | سریع‌تر پاسخ دادن به قیمت خطای بیشتر |
| accuracy | دقت | نسبت پاسخ‌های درست |
| exemplar | نمونه (exemplar) | یک مورد ذخیره‌شده در حافظه از یک دسته |
| prototype | پیش‌نمونه (prototype) | خلاصه یا میانگین یک دسته |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| attention weight | وزن توجه | سهم توجه به هر بُعد محرک |
| sensitivity (d′) | حساسیت | فاصله‌ی توزیع علامت و نویز |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| EZ-diffusion | EZ-diffusion | برآورد ساده‌ی پارامترهای DDM از سه آماره |
| parameter recovery | بازیابی پارامتر | آیا برازش، پارامترهای معلوم شبیه‌سازی را برمی‌گرداند |
| evidence | شواهد | اطلاعاتی که برای تصمیم جمع می‌شود |
| stimulus | محرک | چیزی که به شرکت‌کننده نشان داده می‌شود |
| boundary separation | فاصله‌ی مرزها | مقدار شواهد لازم برای پاسخ؛ نشانه‌ی احتیاط |
| non-decision time | زمان غیرتصمیمی | زمان دیدن محرک و اجرای حرکت پاسخ |
| similarity | شباهت | نزدیکی دو محرک در فضای روان‌شناختی |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| embedding | embedding (بردار معنایی) | برداری که مدل برای یک کلمه یا متن می‌سازد |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Describe** exemplar and prototype theories of categorization and **formalize** them as the GCM and a prototype model.
2. **Fit** the GCM and the prototype model to classification data by MLE, **compare** them, and **interpret** attention weights and sensitivity.
3. **Describe** the drift-diffusion model (DDM) as the continuous limit of the Week 1 random walk, and **map** its parameters onto cognitive constructs.
4. **Estimate** DDM parameters with the closed-form EZ-diffusion method and **validate** it by parameter recovery.
5. **Interpret** experimental effects in terms of model parameters ("this manipulation changed caution, not evidence quality").

<div dir="rtl">

1. نظریه‌های نمونه‌محور (exemplar) و پیش‌نمونه‌ای (prototype) دسته‌بندی را **توصیف کنند** و آن‌ها را به‌صورت GCM و یک مدل prototype **صورت‌بندی کنند**.
2. GCM و مدل prototype را با MLE روی داده‌ی دسته‌بندی **برازش کنند**، **مقایسه کنند**، و وزن‌های توجه و حساسیت را **تفسیر کنند**.
3. مدل drift-diffusion (DDM) را به‌عنوان حد پیوسته‌ی random walk هفته‌ی 1 **توصیف کنند** و پارامترهایش را به سازه‌های شناختی **نگاشت کنند**.
4. پارامترهای DDM را با روش بسته‌ی (closed-form) EZ-diffusion **برآورد کنند** و آن را با بازیابی پارامتر **اعتبارسنجی کنند**.
5. اثرهای آزمایشی را بر حسب پارامترهای مدل **تفسیر کنند** («این دست‌کاری احتیاط را تغییر داد، نه کیفیت شواهد را»).

</div>

---

## Motivation & big picture · مقدمه

The first 13 weeks built a toolkit, mostly on two small running examples (forgetting and SDT). Chapter 6 shows the toolkit at work on models that have shaped whole research areas. This week covers two of the most influential.

<div dir="rtl">

13 هفته‌ی اول یک جعبه‌ابزار ساختند، بیشتر روی دو مثال کوچک (فراموشی و SDT). فصل 6 جعبه‌ابزار را روی مدل‌هایی به کار می‌گیرد که کل حوزه‌های پژوهشی را شکل داده‌اند. این هفته دو تا از تأثیرگذارترین‌ها را می‌بینیم.

</div>

**Categorization.** How do we decide that a new animal is a dog? *Prototype theory* says that we compare it with a summary of the category, the average dog. *Exemplar theory* says that we compare it with stored memories of every dog (and every cat) we have seen. Both sound plausible, and verbal arguments went back and forth for years. Formal models made the difference: Medin and Schaffer's 5-4 category structure was designed so that the two theories make **opposite predictions** for specific stimuli. Nosofsky's **Generalized Context Model (GCM)** turned exemplar theory into a precise, fit-able model with interpretable attention weights.

<div dir="rtl">

**دسته‌بندی.** چطور تصمیم می‌گیریم که یک حیوان تازه سگ است؟ *نظریه‌ی prototype* می‌گوید آن را با یک خلاصه‌ی دسته، یعنی سگ میانگین، مقایسه می‌کنیم. *نظریه‌ی exemplar* می‌گوید آن را با خاطره‌های ذخیره‌شده‌ی همه‌ی سگ‌ها (و همه‌ی گربه‌ها)یی که دیده‌ایم مقایسه می‌کنیم. هر دو معقول به نظر می‌رسند و بحث‌های کلامی سال‌ها رفت و برگشت. مدل‌های فرمال بودند که فرق را ساختند: ساختار دسته‌ی 5-4 مدین و شیفر طوری طراحی شد که دو نظریه برای محرک‌های مشخصی **پیش‌بینی‌های متضاد** داشته باشند. **مدل بافت تعمیم‌یافته (GCM)** نوسوفسکی نظریه‌ی exemplar را به یک مدل دقیق و قابل برازش با وزن‌های توجه تفسیرپذیر تبدیل کرد.

</div>

**Decision making.** In Week 1 we built a random walk that accumulates evidence to a boundary. Its continuous version, the **drift-diffusion model**, is arguably the most successful model in cognitive psychology: it explains accuracy *and* the full RT distributions of correct and error responses, with parameters for evidence quality, caution and non-decision time. It is used to study ageing, ADHD, depression, learning and the effect of drugs. Fitting the full DDM is computationally heavy, but the **EZ-diffusion** method gives good estimates from three summary statistics with closed-form equations.

<div dir="rtl">

**تصمیم‌گیری.** در هفته‌ی 1 یک random walk ساختیم که شواهد را تا رسیدن به یک مرز جمع می‌کند. نسخه‌ی پیوسته‌اش، **مدل drift-diffusion**، احتمالاً موفق‌ترین مدل روان‌شناسی شناختی است: دقت *و* کل توزیع‌های RT پاسخ‌های درست و خطا را توضیح می‌دهد، با پارامترهایی برای کیفیت شواهد، احتیاط و non-decision time. برای مطالعه‌ی پیری، ADHD، افسردگی، یادگیری و اثر داروها از آن استفاده می‌شود. برازش DDM کامل از نظر محاسباتی سنگین است، ولی روش **EZ-diffusion** با معادله‌های بسته از سه آماره‌ی خلاصه برآوردهای خوبی می‌دهد.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Categorization models** explain how people learn concepts (medical students learning to recognize skin lesions, children learning words), and they are used to design better training: which examples to show, and in what order.
- **Exemplar ideas in machine learning**: nearest-neighbor classifiers and kernel methods classify a new case by its similarity to stored examples, the same principle as the GCM.
- **The drift-diffusion model** is one of the most used models in cognitive neuroscience and clinical research: ageing, ADHD, depression, anxiety, effects of drugs and sleep deprivation. It is also used in consumer research (how fast people choose between products) and in neuroeconomics.
- **EZ-diffusion** is popular because it needs only three summary statistics per person and no optimization, so it can be applied to existing datasets quickly.

<div dir="rtl">

- **مدل‌های دسته‌بندی** توضیح می‌دهند آدم‌ها چطور مفهوم‌ها را یاد می‌گیرند (دانشجوی پزشکی که یاد می‌گیرد ضایعه‌های پوستی را تشخیص دهد، کودکی که کلمه یاد می‌گیرد)، و برای طراحی آموزش بهتر استفاده می‌شوند: کدام مثال‌ها را و با چه ترتیبی نشان دهیم.
- **ایده‌ی exemplar در یادگیری ماشین:** طبقه‌بندهای نزدیک‌ترین همسایه (nearest neighbor) و روش‌های kernel یک مورد جدید را بر اساس شباهتش به مثال‌های ذخیره‌شده طبقه‌بندی می‌کنند؛ همان اصل GCM.
- **مدل drift-diffusion** یکی از پرکاربردترین مدل‌ها در علوم اعصاب شناختی و پژوهش بالینی است: سالمندی، ADHD، افسردگی، اضطراب، اثر داروها و بی‌خوابی. در پژوهش مصرف‌کننده (اینکه آدم‌ها با چه سرعتی بین محصولات انتخاب می‌کنند) و در عصب‌اقتصاد هم استفاده می‌شود.
- **EZ-diffusion** محبوب است چون برای هر نفر فقط سه آماره‌ی خلاصه لازم دارد و به بهینه‌سازی نیاز ندارد، پس می‌شود آن را سریع روی داده‌های موجود اجرا کرد.

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

Two famous models this week. **Categorization:** how do we decide that a new animal is a dog? One theory says we compare it with an average "ideal dog" (**prototype**). Another says we compare it with all the dogs and cats we remember and see which group it resembles more overall (**exemplars**). The **GCM** turns the exemplar idea into math: measure the distance between the new item and each stored example (paying more **attention** to some features than others), turn distance into similarity (closer = much more similar), and choose category A with probability "total similarity to A / total similarity to all". A clever set of stimuli (the 5-4 structure) makes the two theories predict *opposite* things for some items. **Decisions:** the **drift-diffusion model** is the continuous version of Week 1's random walk. Evidence drifts toward the correct boundary at an average speed $v$ (quality of evidence) while being jiggled by noise; a response is made when a boundary $a$ (caution) is reached; a fixed time $T_{er}$ is added for seeing and pressing. **EZ-diffusion** is a shortcut that computes $v$, $a$ and $T_{er}$ from just three numbers: accuracy, and the mean and variance of correct RTs.

<div dir="rtl">

این هفته دو مدل معروف داریم. **دسته‌بندی:** چطور تصمیم می‌گیریم یک حیوان تازه سگ است؟ یک نظریه می‌گوید آن را با یک «سگ ایده‌آل» میانگین مقایسه می‌کنیم (**prototype**). نظریه‌ی دیگر می‌گوید آن را با همه‌ی سگ‌ها و گربه‌هایی که به یاد داریم مقایسه می‌کنیم و می‌بینیم در مجموع به کدام گروه بیشتر شبیه است (**exemplarها**). **GCM** ایده‌ی exemplar را به ریاضی تبدیل می‌کند: فاصله‌ی آیتم جدید با هر مثال ذخیره‌شده را بسنج (با **توجه** بیشتر به بعضی ویژگی‌ها)، فاصله را به شباهت تبدیل کن (نزدیک‌تر = خیلی شبیه‌تر)، و دسته‌ی A را با احتمال «شباهت کل به A / شباهت کل به همه» انتخاب کن. یک مجموعه محرک هوشمندانه (ساختار 5-4) کاری می‌کند که دو نظریه برای بعضی آیتم‌ها پیش‌بینی‌های *متضاد* داشته باشند. **تصمیم‌گیری:** **مدل drift-diffusion** نسخه‌ی پیوسته‌ی random walk هفته‌ی 1 است. شواهد با سرعت میانگین $v$ (کیفیت شواهد) به سمت مرز درست می‌رود و هم‌زمان نویز آن را تکان می‌دهد؛ وقتی به مرز $a$ (احتیاط) برسد پاسخ داده می‌شود؛ یک زمان ثابت $T_{er}$ هم برای دیدن و زدن کلید اضافه می‌شود. **EZ-diffusion** یک میان‌بر است که $v$، $a$ و $T_{er}$ را فقط از سه عدد حساب می‌کند: دقت، و میانگین و واریانس زمان واکنش پاسخ‌های درست.

</div>

**Suggested timing (60 min):** categorization theories and the 5-4 structure 10 · GCM 15 · prototype model and the critical predictions 5 · the drift-diffusion model 15 · EZ-diffusion 10 · interpretation 5.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** نظریه‌های دسته‌بندی و ساختار 5-4 10 · GCM 15 · مدل prototype و پیش‌بینی‌های کلیدی 5 · مدل drift-diffusion 15 · EZ-diffusion 10 · تفسیر 5.

</div>

### 1. The 5-4 category structure · 1. ساختار دسته‌ی 5-4

Stimuli vary on four binary dimensions (e.g., the shape, color, size and position of a geometric figure in Medin & Schaffer's design; facial features in later versions). Participants learn to classify 9 training stimuli into categories A and B, then classify 7 new **transfer** stimuli without feedback. The commonly used stimulus set is [verify against Medin & Schaffer, 1978, or Smith & Minda, 2000]:

<div dir="rtl">

محرک‌ها روی چهار بعد دودویی فرق دارند (مثلاً شکل، رنگ، اندازه و موقعیت یک شکل هندسی در طرح مدین و شیفر؛ ویژگی‌های چهره در نسخه‌های بعدی). شرکت‌کننده‌ها یاد می‌گیرند 9 محرک آموزشی را در دسته‌های A و B بگذارند، و بعد 7 محرک **انتقال** (transfer) تازه را بدون بازخورد دسته‌بندی می‌کنند. مجموعه محرک رایج این است [با Medin & Schaffer, 1978 یا Smith & Minda, 2000 بررسی شود]:

</div>

| Category A | Category B | Transfer |
|---|---|---|
| A1 1110 | B1 1100 | T1 1001 |
| A2 1010 | B2 0110 | T2 1000 |
| A3 1011 | B3 0001 | T3 1111 |
| A4 1101 | B4 0000 | T4 0010 |
| A5 0111 | | T5 0101 |
| | | T6 0011 |
| | | T7 0100 |

<div dir="rtl">

| دسته‌ی A | دسته‌ی B | انتقال |
|---|---|---|
| A1 1110 | B1 1100 | T1 1001 |
| A2 1010 | B2 0110 | T2 1000 |
| A3 1011 | B3 0001 | T3 1111 |
| A4 1101 | B4 0000 | T4 0010 |
| A5 0111 | | T5 0101 |
| | | T6 0011 |
| | | T7 0100 |

</div>

The category A prototype is 1111 and the B prototype is 0000. The critical comparison: **A1 (1110)** shares three features with the A prototype, while **A2 (1010)** shares only two. A prototype model therefore predicts that A1 is classified *better* than A2. But A2 is highly similar to two other A exemplars (A1 and A3) and to no B exemplar, whereas A1 is highly similar to two **B** exemplars (B1 and B2). An exemplar model can therefore predict that A2 is classified *at least as well* as A1, and in the empirical data A2 is typically classified better.

<div dir="rtl">

prototype دسته‌ی A برابر 1111 و prototype دسته‌ی B برابر 0000 است. مقایسه‌ی کلیدی: **A1 (1110)** سه ویژگی با prototype دسته‌ی A مشترک دارد، ولی **A2 (1010)** فقط دو تا. پس مدل prototype پیش‌بینی می‌کند A1 *بهتر* از A2 دسته‌بندی شود. اما A2 به دو exemplar دیگر A (یعنی A1 و A3) خیلی شبیه است و به هیچ exemplar از B شبیه نیست، در حالی که A1 به دو exemplar از **B** (یعنی B1 و B2) خیلی شبیه است. پس مدل exemplar می‌تواند پیش‌بینی کند که A2 *دست‌کم به خوبیِ* A1 دسته‌بندی شود، و در داده‌های تجربی A2 معمولاً بهتر دسته‌بندی می‌شود.

</div>

### 2. The Generalized Context Model (GCM) · 2. مدل بافت تعمیم‌یافته (GCM)

**Distance** between stimulus $i$ and stored exemplar $e$, with attention weights $w_m \ge 0$, $\sum_m w_m = 1$ (city-block metric for separable dimensions):

<div dir="rtl">

**فاصله** بین محرک $i$ و exemplar ذخیره‌شده‌ی $e$، با وزن‌های توجه $w_m \ge 0$ و $\sum_m w_m = 1$ (متریک city-block برای ابعاد جدایی‌پذیر):

</div>

$$
\mathrm{dist}_{ie} = \sum_{m=1}^{4} w_m\, |x_{im} - x_{em}|.
$$

**Similarity** decays exponentially with distance, with **sensitivity** $c$:

<div dir="rtl">

**شباهت** با فاصله به‌صورت نمایی کم می‌شود، با **حساسیت** $c$:

</div>

$$
s_{ie} = \exp(-c \cdot \mathrm{dist}_{ie}).
$$

**Choice rule** (summed similarity, Luce ratio):

<div dir="rtl">

**قاعده‌ی انتخاب** (شباهت جمع‌شده، نسبت Luce):

</div>

$$
P(A \mid i) = \frac{\sum_{e \in A} s_{ie}}{\sum_{e \in A} s_{ie} + \sum_{e \in B} s_{ie}}.
$$

**Parameters:** $c$ (how steeply similarity falls with distance; large $c$ means only very close exemplars matter) and three free attention weights (the fourth is $1 - $ the others), so $k = 4$. (This is the overloaded $c$ from the Week 1 notation table; this week it means sensitivity, not an SDT criterion.)

<div dir="rtl">

**پارامترها:** $c$ (شباهت با فاصله چقدر تند کم می‌شود؛ $c$ بزرگ یعنی فقط exemplarهای خیلی نزدیک مهم‌اند) و سه وزن توجه آزاد (چهارمی $1 - $ بقیه است)، پس $k = 4$. (این همان $c$ چندمعنایی جدول نمادگذاری هفته‌ی 1 است؛ این هفته یعنی حساسیت، نه ملاک SDT.)

</div>

**Interpretation of attention weights:** $w_m$ is the share of attention given to dimension $m$. Optimal attention emphasizes dimensions that are diagnostic of the category. In the 5-4 structure, dimensions 1 and 3 are the most diagnostic.

<div dir="rtl">

**تفسیر وزن‌های توجه:** $w_m$ سهم توجهی است که به بعد $m$ داده می‌شود. توجه بهینه روی ابعادی تأکید می‌کند که برای دسته تشخیصی (diagnostic) هستند. در ساختار 5-4، ابعاد 1 و 3 تشخیصی‌ترین‌اند.

</div>

**Prototype model:** the same distance, similarity and choice rule, but each category is represented by its prototype only: $P(A\mid i) = s_{i,P_A}/(s_{i,P_A} + s_{i,P_B})$. Also $k = 4$, so the comparison is not affected by parameter counting.

<div dir="rtl">

**مدل prototype:** همان فاصله، شباهت و قاعده‌ی انتخاب، ولی هر دسته فقط با prototype خودش نمایش داده می‌شود: $P(A\mid i) = s_{i,P_A}/(s_{i,P_A} + s_{i,P_B})$. این هم $k = 4$ دارد، پس شمارش پارامترها روی مقایسه اثری ندارد.

</div>

**Likelihood:** if stimulus $i$ is classified $n_i$ times and called "A" $y_i$ times, then $y_i \sim \mathrm{Binomial}(n_i, P(A\mid i))$, fitted by MLE with multi-start (Weeks 3–4). Weights are best estimated through a **softmax reparameterization** (Week 3), $w = \mathrm{softmax}(\eta_1, \eta_2, \eta_3, 0)$, and $c = e^{\gamma}$.

<div dir="rtl">

**درست‌نمایی:** اگر محرک $i$ به تعداد $n_i$ بار دسته‌بندی شود و $y_i$ بار «A» نامیده شود، $y_i \sim \mathrm{Binomial}(n_i, P(A\mid i))$ است و با MLE و multi-start برازش می‌شود (هفته‌های 3–4). وزن‌ها بهتر است با یک **reparameterization softmax** (هفته‌ی 3) برآورد شوند، $w = \mathrm{softmax}(\eta_1, \eta_2, \eta_3, 0)$، و $c = e^{\gamma}$.

</div>

> **Advanced:** the full GCM adds a response-bias parameter $b_A$, a similarity exponent (Gaussian vs. exponential similarity), a metric parameter $r$ (city-block $r = 1$ vs. Euclidean $r = 2$) and sometimes a response-determinism parameter $\gamma$ (raising summed similarities to a power). Lee & Wagenmakers (chapter 17) develop a Bayesian, hierarchical GCM.

<div dir="rtl">

> **پیشرفته:** GCM کامل یک پارامتر سوگیری پاسخ $b_A$، یک توان شباهت (شباهت گاوسی در برابر نمایی)، یک پارامتر متریک $r$ (city-block با $r = 1$ در برابر اقلیدسی با $r = 2$) و گاهی یک پارامتر قطعیت پاسخ (response determinism) $\gamma$ (به توان رساندن شباهت‌های جمع‌شده) اضافه می‌کند. Lee & Wagenmakers (فصل 17) یک GCM بیزی و سلسله‌مراتبی می‌سازند.

</div>

#### Reading the math · خواندن ریاضی

- **Distance** $\sum_m w_m|x_{im} - x_{em}|$: count the features on which the new item $i$ and the stored example $e$ differ, but weight each feature by its attention $w_m$. With 4 binary features and equal weights 0.25, one mismatching feature gives distance 0.25.
- **Similarity** $e^{-c \cdot \mathrm{dist}}$: distance 0 gives similarity 1; with $c = 2$, distance 0.25 gives $e^{-0.5} = 0.61$, distance 1 gives $e^{-2} = 0.14$. A larger $c$ makes similarity drop faster, so only very close examples matter.
- **Choice rule:** add the similarities to all A examples and to all B examples, and divide. In the worked example, T3 has total similarity 2.79 to A and 1.09 to B, so $P(A) = 2.79/3.89 = 0.72$.

<div dir="rtl">

- **فاصله** $\sum_m w_m|x_{im} - x_{em}|$: ویژگی‌هایی را بشمار که آیتم جدید $i$ و مثال ذخیره‌شده‌ی $e$ در آن‌ها فرق دارند، ولی هر ویژگی را با توجه آن یعنی $w_m$ وزن بده. با 4 ویژگی دودویی و وزن‌های برابر 0.25، یک ویژگی ناهمخوان فاصله‌ی 0.25 می‌دهد.
- **شباهت** $e^{-c \cdot \mathrm{dist}}$: فاصله‌ی 0 شباهت 1 می‌دهد؛ با $c = 2$، فاصله‌ی 0.25 شباهت $e^{-0.5} = 0.61$ و فاصله‌ی 1 شباهت $e^{-2} = 0.14$ می‌دهد. $c$ بزرگ‌تر باعث می‌شود شباهت سریع‌تر کم شود، پس فقط مثال‌های خیلی نزدیک مهم‌اند.
- **قاعده‌ی انتخاب:** شباهت‌ها به همه‌ی مثال‌های A و همه‌ی مثال‌های B را جمع بزن و تقسیم کن. در مثال حل‌شده، T3 شباهت کل 2.79 به A و 1.09 به B دارد، پس $P(A) = 2.79/3.89 = 0.72$.

</div>

### 3. The drift-diffusion model (DDM) · 3. مدل drift-diffusion (DDM)

Take the Week 1 random walk and let the step size and step duration shrink together. Evidence $X(t)$ then evolves continuously:

<div dir="rtl">

random walk هفته‌ی 1 را بگیرید و بگذارید اندازه‌ی گام و مدت گام با هم کوچک شوند. آن‌وقت شواهد $X(t)$ به‌طور پیوسته تغییر می‌کند:

</div>

$$
dX = v\,dt + s\,dW(t), \qquad X(0) = z,
$$

where $dW$ is Gaussian white noise (a Wiener process). A response is made when $X$ reaches $a$ (correct) or $0$ (error); $\mathrm{RT} = T_{\text{decision}} + T_{er}$.

<div dir="rtl">

که در آن $dW$ نویز سفید گاوسی (فرایند Wiener) است. وقتی $X$ به $a$ (درست) یا $0$ (خطا) برسد پاسخ داده می‌شود؛ $\mathrm{RT} = T_{\text{decision}} + T_{er}$.

</div>

| Parameter | Meaning | Typical manipulation that changes it |
|---|---|---|
| $v$ (drift rate) | Quality / rate of evidence accumulation | Stimulus difficulty; perceptual sensitivity; attention |
| $a$ (boundary separation) | Response caution (speed–accuracy setting) | Speed vs. accuracy instructions |
| $z$ (starting point) | A priori bias toward one response | Base rates, payoffs |
| $T_{er}$ (non-decision time; also written $t_0$) | Encoding + motor time | Response modality, stimulus degradation |
| $s$ (within-trial noise) | Scaling constant | Fixed (by convention $s = 0.1$ in EZ, $s = 1$ elsewhere) |

<div dir="rtl">

| پارامتر | معنا | دست‌کاری معمولی که تغییرش می‌دهد |
|---|---|---|
| $v$ (drift rate) | کیفیت / نرخ انباشت شواهد | دشواری محرک؛ حساسیت ادراکی؛ توجه |
| $a$ (فاصله‌ی مرزها) | احتیاط پاسخ (تنظیم سرعت–دقت) | دستورالعمل سرعت در برابر دقت |
| $z$ (نقطه‌ی شروع) | سوگیری پیشینی به سمت یک پاسخ | نرخ‌های پایه، پاداش‌ها |
| $T_{er}$ (non-decision time؛ $t_0$ هم نوشته می‌شود) | زمان رمزگذاری + حرکتی | نوع پاسخ، تخریب محرک |
| $s$ (نویز درون trial) | ثابت مقیاس | ثابت (طبق قرارداد $s = 0.1$ در EZ و $s = 1$ در جاهای دیگر) |

</div>

The full DDM also includes across-trial variability in drift, starting point and non-decision time. Week 1, Exercise 5 showed that drift variability produces slow errors.

<div dir="rtl">

DDM کامل تغییرپذیری بین trialها در drift، نقطه‌ی شروع و non-decision time را هم دارد. تمرین 5 هفته‌ی 1 نشان داد که تغییرپذیری drift خطاهای کند تولید می‌کند.

</div>

**Signature predictions:** right-skewed RT distributions; a speed–accuracy trade-off when $a$ changes; easier stimuli giving responses that are faster *and* more accurate (higher $v$); a change in $T_{er}$ shifting the whole RT distribution without changing its shape.

<div dir="rtl">

**پیش‌بینی‌های شاخص:** توزیع‌های RT چوله به راست؛ trade-off سرعت–دقت وقتی $a$ تغییر می‌کند؛ محرک‌های آسان‌تر که پاسخ‌هایی هم سریع‌تر *و* هم دقیق‌تر می‌دهند ($v$ بالاتر)؛ تغییر $T_{er}$ که کل توزیع RT را بدون تغییر شکلش جابه‌جا می‌کند.

</div>

#### Reading the math · خواندن ریاضی

$dX = v\,dt + s\,dW(t)$ reads: "in a tiny time step $dt$, the evidence changes by a deterministic push $v\,dt$ plus a random kick $s\,dW$". $dW$ is Gaussian noise whose variance is proportional to $dt$ (so over a step of length $dt$ the kick has SD $s\sqrt{dt}$). In the lab simulation this becomes exactly Week 1's random walk with small steps: `x += v*dt + s*sqrt(dt)*randn()`. The table of parameters is the important part to memorize: $v$ = evidence quality, $a$ = caution, $z$ = bias, $T_{er}$ = non-decision time.

<div dir="rtl">

$dX = v\,dt + s\,dW(t)$ این‌طور خوانده می‌شود: «در یک گام زمانی خیلی کوچک $dt$، شواهد به اندازه‌ی یک هل قطعی $v\,dt$ به‌علاوه‌ی یک ضربه‌ی تصادفی $s\,dW$ تغییر می‌کند». $dW$ نویز گاوسی است که واریانسش متناسب با $dt$ است (پس در یک گام به طول $dt$ ضربه انحراف معیار $s\sqrt{dt}$ دارد). در شبیه‌سازی lab این دقیقاً همان random walk هفته‌ی 1 با گام‌های کوچک است: `x += v*dt + s*sqrt(dt)*randn()`. جدول پارامترها بخشی است که باید به خاطر سپرد: $v$ = کیفیت شواهد، $a$ = احتیاط، $z$ = سوگیری، $T_{er}$ = non-decision time.

</div>

### 4. EZ-diffusion · 4. EZ-diffusion

Wagenmakers, van der Maas and Grasman (2007) derived closed-form estimates of $v$, $a$ and $T_{er}$ (assuming $z = a/2$, no across-trial variability, $s = 0.1$) from three statistics: the proportion correct $P_c$, the **variance** of correct RTs $V_{RT}$ (in s²) and the **mean** of correct RTs $M_{RT}$ (in s):

<div dir="rtl">

Wagenmakers، van der Maas و Grasman (2007) برآوردهای بسته‌ی $v$، $a$ و $T_{er}$ را (با فرض $z = a/2$، بدون تغییرپذیری بین trialها، $s = 0.1$) از سه آماره به دست آوردند: نسبت پاسخ‌های درست $P_c$، **واریانس** RTهای درست $V_{RT}$ (بر حسب s²) و **میانگین** RTهای درست $M_{RT}$ (بر حسب s):

</div>

$$
L = \operatorname{logit}(P_c) = \ln\frac{P_c}{1 - P_c}, \qquad
x = \frac{L\,(L P_c^2 - L P_c + P_c - 0.5)}{V_{RT}},
$$

$$
v = \operatorname{sign}(P_c - 0.5)\; s\; x^{1/4}, \qquad
a = \frac{s^2 L}{v},
$$

$$
y = -\frac{v a}{s^2}, \qquad
\mathrm{MDT} = \frac{a}{2v}\cdot\frac{1 - e^{y}}{1 + e^{y}}, \qquad
T_{er} = M_{RT} - \mathrm{MDT}.
$$

**Edge cases:** the formulas fail at $P_c = 0.5$ (then $v = 0$) and $P_c = 1$ (then $L = \infty$). For $P_c = 1$, a standard fix is to use $P_c = 1 - 1/(2N)$, analogous to the extreme-rate corrections of Week 2.

<div dir="rtl">

**حالت‌های مرزی:** فرمول‌ها در $P_c = 0.5$ (که آن‌وقت $v = 0$) و $P_c = 1$ (که آن‌وقت $L = \infty$) کار نمی‌کنند. برای $P_c = 1$ یک راه‌حل استاندارد استفاده از $P_c = 1 - 1/(2N)$ است، شبیه تصحیح‌های نرخ حدی هفته‌ی 2.

</div>

**Strengths and limits.** EZ is fast, needs no optimization and recovers parameters well when its assumptions hold (lab Part C). It ignores error RTs and the shape of the RT distribution beyond mean and variance, and it cannot estimate bias or across-trial variabilities. For those, fit the full DDM by MLE or with hierarchical Bayesian methods (e.g., the HDDM package or the Wiener likelihood in PyMC/Stan).

<div dir="rtl">

**نقاط قوت و محدودیت‌ها.** EZ سریع است، به بهینه‌سازی نیاز ندارد و وقتی فرض‌هایش برقرارند پارامترها را خوب بازیابی می‌کند (بخش C lab). RTهای خطا و شکل توزیع RT فراتر از میانگین و واریانس را نادیده می‌گیرد، و نمی‌تواند سوگیری یا تغییرپذیری‌های بین trialها را برآورد کند. برای این‌ها DDM کامل را با MLE یا روش‌های بیزی سلسله‌مراتبی برازش کنید (مثلاً بسته‌ی HDDM یا درست‌نمایی Wiener در PyMC/Stan).

</div>

#### Reading the math · خواندن ریاضی

The EZ equations look intimidating but are a recipe; nobody needs to memorize them.

1. $L = \ln(P_c/(1-P_c))$: the **logit** of accuracy ("log odds of being correct"). $P_c = 0.8$ gives $L = \ln 4 = 1.39$.
2. $x$ combines accuracy with the **variance** of correct RTs: the more variable the RTs for a given accuracy, the lower the drift.
3. $v$ and $a$ then follow from $L$ and $x$; $\mathrm{MDT}$ is the predicted *mean decision time*.
4. $T_{er} = M_{RT} - \mathrm{MDT}$: whatever part of the mean RT is not decision time is non-decision time.

Use the worked example (Part 2) to show each step with numbers; then let the computer do it (the function `ez_diffusion` in the lab code).

<div dir="rtl">

معادله‌های EZ ترسناک به نظر می‌رسند ولی یک دستور پخت‌اند؛ لازم نیست کسی آن‌ها را حفظ کند.

1. $L = \ln(P_c/(1-P_c))$: **logit** دقت («لگاریتم بخت درست بودن»). $P_c = 0.8$ می‌دهد $L = \ln 4 = 1.39$.
2. $x$ دقت را با **واریانس** زمان واکنش پاسخ‌های درست ترکیب می‌کند: هرچه زمان‌های واکنش برای یک دقت مشخص پراکنده‌تر باشند، drift کمتر است.
3. بعد $v$ و $a$ از $L$ و $x$ به دست می‌آیند؛ $\mathrm{MDT}$ *میانگین زمان تصمیم* پیش‌بینی‌شده است.
4. $T_{er} = M_{RT} - \mathrm{MDT}$: هر بخشی از میانگین زمان واکنش که زمان تصمیم نیست، non-decision time است.

از مثال حل‌شده (بخش 2) برای نشان دادن هر قدم با عدد استفاده کنید؛ بعد بگذارید کامپیوتر انجامش دهد (تابع `ez_diffusion` در کد lab).

</div>

#### For an engineer · برای یک مهندس

- **GCM** is a similarity-based classifier with an exponential kernel and a weighted L1 (city-block) metric, close to a **kernel / Parzen-window classifier**. The attention weights act like learned feature weights; $c$ is the inverse kernel width.
- The **DDM** is a **Wiener process with drift** between two absorbing boundaries: the classic first-passage-time problem. The continuous-time SPRT (Week 1 box) is exactly this process, with $v$ ∝ signal amplitude and $s$ the noise level.
- RT distributions are **first-passage-time distributions**, which are right-skewed for the same reason detection delays of a sequential detector are.
- **EZ-diffusion** is a method-of-moments estimator: it matches three sample moments (accuracy, mean and variance of correct RTs) to their closed-form model expressions, instead of maximizing a likelihood.

<div dir="rtl">

- **GCM** یک طبقه‌بند مبتنی بر شباهت با کرنل نمایی و یک متریک L1 وزن‌دار (city-block) است، نزدیک به یک **طبقه‌بند کرنلی / پنجره‌ی Parzen**. وزن‌های توجه مثل وزن‌های یادگرفته‌شده‌ی ویژگی‌ها عمل می‌کنند؛ $c$ معکوس پهنای کرنل است.
- **DDM** یک **فرایند Wiener با رانش** بین دو مرز جاذب است: مسئله‌ی کلاسیک زمان اولین عبور (first-passage time). SPRT پیوسته در زمان (کادر هفته‌ی 1) دقیقاً همین فرایند است، با $v$ متناسب با دامنه‌ی سیگنال و $s$ سطح نویز.
- توزیع‌های زمان واکنش همان **توزیع‌های زمان اولین عبور** هستند و به همان دلیلی چوله به راست‌اند که تأخیرهای آشکارسازی یک آشکارساز ترتیبی.
- **EZ-diffusion** یک تخمین‌گر روش گشتاورها (method of moments) است: سه گشتاور نمونه (دقت، میانگین و واریانس زمان واکنش‌های درست) را با عبارت‌های بسته‌ی مدل برابر می‌گذارد، به جای اینکه درست‌نمایی را بیشینه کند.

</div>

#### For the instructor · برای مدرس

- **Let students be the participants.** Before the GCM, show the 9 training stimuli of the 5-4 structure as simple drawings (e.g. shapes with 4 binary features), teach the categories with feedback, then test A1 and A2. The class's own data often show the exemplar pattern.
- **Draw the DDM as Week 1's picture with a smooth, noisy path.** Then change one parameter at a time on the board (wider boundaries, steeper drift, later start) and ask what happens to accuracy and RT.
- **Do not derive EZ.** Present it as a "calculator" and spend the time on interpretation (lab Part E): which manipulation changed which parameter.
- **Typical questions.**
  - *"Prototype or exemplar, who won?"* For small, poorly structured categories exemplar models usually fit better; for large, well-structured ones prototypes do well. Both ideas survive in modern models.
  - *"Why not just compare mean RTs?"* A slower group could be more cautious, have worse evidence, or be slower motorically; only the DDM separates them.
  - *"Are the parameters of EZ and the full DDM the same?"* They estimate the same quantities, but EZ assumes no bias and no trial-to-trial variability.

<div dir="rtl">

- **بگذارید دانشجوها خودشان شرکت‌کننده باشند.** پیش از GCM، 9 محرک آموزشی ساختار 5-4 را به شکل نقاشی‌های ساده نشان دهید (مثلاً شکل‌هایی با 4 ویژگی دودویی)، دسته‌ها را با بازخورد یاد بدهید و بعد A1 و A2 را آزمون کنید. داده‌ی خود کلاس اغلب الگوی exemplar را نشان می‌دهد.
- **DDM را با همان تصویر هفته‌ی 1 و یک مسیر هموار و پرنویز بکشید.** بعد هر بار یک پارامتر را روی تخته تغییر دهید (مرزهای دورتر، drift تندتر، شروع دیرتر) و بپرسید دقت و زمان واکنش چه می‌شود.
- **EZ را اثبات نکنید.** آن را به‌عنوان یک «ماشین‌حساب» معرفی کنید و وقت را روی تفسیر بگذارید (بخش E lab): کدام دست‌کاری کدام پارامتر را تغییر داد.
- **سؤال‌های رایج.**
  - *«prototype یا exemplar، کدام برنده شد؟»* برای دسته‌های کوچک و کم‌ساختار معمولاً مدل‌های exemplar بهتر برازش می‌شوند؛ برای دسته‌های بزرگ و پرساختار prototype هم خوب کار می‌کند. هر دو ایده در مدل‌های امروزی زنده‌اند.
  - *«چرا فقط میانگین زمان واکنش را مقایسه نکنیم؟»* یک گروه کندتر ممکن است محتاط‌تر باشد، شواهد بدتری داشته باشد یا از نظر حرکتی کندتر باشد؛ فقط DDM این‌ها را جدا می‌کند.
  - *«آیا پارامترهای EZ و DDM کامل یکی‌اند؟»* همان کمیت‌ها را برآورد می‌کنند، ولی EZ فرض می‌کند سوگیری و تغییرپذیری بین trialها وجود ندارد.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: one GCM prediction by hand · بخش 1: یک پیش‌بینی GCM با دست

Stimulus T3 (1111), equal attention $w_m = 0.25$, sensitivity $c = 2$.

<div dir="rtl">

محرک T3 (1111)، توجه برابر $w_m = 0.25$، حساسیت $c = 2$.

</div>

| Exemplar | Mismatching dimensions | Distance | Similarity $e^{-2\,\mathrm{dist}}$ |
|---|---|---|---|
| A1 1110 | 1 | 0.25 | 0.607 |
| A2 1010 | 2 | 0.50 | 0.368 |
| A3 1011 | 1 | 0.25 | 0.607 |
| A4 1101 | 1 | 0.25 | 0.607 |
| A5 0111 | 1 | 0.25 | 0.607 |
| **Sum A** | | | **2.794** |
| B1 1100 | 2 | 0.50 | 0.368 |
| B2 0110 | 2 | 0.50 | 0.368 |
| B3 0001 | 3 | 0.75 | 0.223 |
| B4 0000 | 4 | 1.00 | 0.135 |
| **Sum B** | | | **1.094** |

<div dir="rtl">

| Exemplar | ابعاد ناهمخوان | فاصله | شباهت $e^{-2\,\mathrm{dist}}$ |
|---|---|---|---|
| A1 1110 | 1 | 0.25 | 0.607 |
| A2 1010 | 2 | 0.50 | 0.368 |
| A3 1011 | 1 | 0.25 | 0.607 |
| A4 1101 | 1 | 0.25 | 0.607 |
| A5 0111 | 1 | 0.25 | 0.607 |
| **جمع A** | | | **2.794** |
| B1 1100 | 2 | 0.50 | 0.368 |
| B2 0110 | 2 | 0.50 | 0.368 |
| B3 0001 | 3 | 0.75 | 0.223 |
| B4 0000 | 4 | 1.00 | 0.135 |
| **جمع B** | | | **1.094** |

</div>

$$
P(A\mid \text{T3}) = \frac{2.794}{2.794 + 1.094} = 0.719.
$$

**Interpretation.** T3 is the A prototype, yet the exemplar model predicts only about 72% "A" responses with these parameters: two B exemplars (B1 and B2) are only two features away. A larger $c$ (sharper similarity) would raise this probability, because the nearest neighbors (four A exemplars at distance 0.25) would dominate.

<div dir="rtl">

**تفسیر.** T3 خودِ prototype دسته‌ی A است، ولی مدل exemplar با این پارامترها فقط حدود 72% پاسخ «A» پیش‌بینی می‌کند: دو exemplar از B (یعنی B1 و B2) فقط دو ویژگی فاصله دارند. یک $c$ بزرگ‌تر (شباهت تیزتر) این احتمال را بالا می‌برد، چون نزدیک‌ترین همسایه‌ها (چهار exemplar از A در فاصله‌ی 0.25) غالب می‌شوند.

</div>

### Part 2: EZ-diffusion by hand · بخش 2: EZ-diffusion با دست

A participant has $P_c = 0.802$, $V_{RT} = 0.112$ s², $M_{RT} = 0.723$ s.

<div dir="rtl">

یک شرکت‌کننده $P_c = 0.802$، $V_{RT} = 0.112$ s² و $M_{RT} = 0.723$ s دارد.

</div>

1. $L = \ln(0.802/0.198) = 1.399$.
2. $x = 1.399 \times (1.399 \times 0.643 - 1.399 \times 0.802 + 0.802 - 0.5)/0.112 = 0.998$.
3. $v = 0.1 \times 0.998^{1/4} = 0.100$.
4. $a = 0.01 \times 1.399/0.100 = 0.140$.
5. $y = -0.100 \times 0.140/0.01 = -1.399$, so $\mathrm{MDT} = (0.140/0.200) \times (1 - e^{-1.399})/(1 + e^{-1.399}) = 0.423$ s.
6. $T_{er} = 0.723 - 0.423 = 0.300$ s.

<div dir="rtl">

1. $L = \ln(0.802/0.198) = 1.399$.
2. $x = 1.399 \times (1.399 \times 0.643 - 1.399 \times 0.802 + 0.802 - 0.5)/0.112 = 0.998$.
3. $v = 0.1 \times 0.998^{1/4} = 0.100$.
4. $a = 0.01 \times 1.399/0.100 = 0.140$.
5. $y = -0.100 \times 0.140/0.01 = -1.399$، پس $\mathrm{MDT} = (0.140/0.200) \times (1 - e^{-1.399})/(1 + e^{-1.399}) = 0.423$ s.
6. $T_{er} = 0.723 - 0.423 = 0.300$ s.

</div>

**Interpretation.** Of the mean correct RT of 723 ms, about 423 ms is spent accumulating evidence and 300 ms on encoding and responding. Drift 0.10 and boundary 0.14 (in EZ units with $s = 0.1$) are typical values for a moderately difficult task.

<div dir="rtl">

**تفسیر.** از میانگین RT درست 723 میلی‌ثانیه، حدود 423 میلی‌ثانیه صرف انباشت شواهد و 300 میلی‌ثانیه صرف رمزگذاری و پاسخ می‌شود. drift 0.10 و مرز 0.14 (در واحدهای EZ با $s = 0.1$) مقادیر معمولی برای یک تکلیف با دشواری متوسط‌اند.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Implement the GCM and the prototype model for the 5-4 structure; simulate data from the GCM.
2. Fit both models by MLE, compare them, and examine the critical A1-vs-A2 prediction.
3. Check parameter recovery for the GCM.
4. Simulate a drift-diffusion process, recover its parameters with EZ-diffusion, and interpret a 2 × 2 experiment.

<div dir="rtl">

1. پیاده‌سازی GCM و مدل prototype برای ساختار 5-4؛ شبیه‌سازی داده از GCM.
2. برازش هر دو مدل با MLE، مقایسه‌شان، و بررسی پیش‌بینی کلیدی A1 در برابر A2.
3. بررسی بازیابی پارامتر برای GCM.
4. شبیه‌سازی یک فرایند drift-diffusion، بازیابی پارامترهایش با EZ-diffusion، و تفسیر یک آزمایش 2 × 2.

</div>

**Timing:** Part A 20 min · Part B 25 min · Part C 15 min · Part D 40 min · Part E 20 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 20 دقیقه · بخش B 25 دقیقه · بخش C 15 دقیقه · بخش D 40 دقیقه · بخش E 20 دقیقه.

</div>

### Part A: the 5-4 structure and two models (20 min) · بخش A: ساختار 5-4 و دو مدل (20 دقیقه)

> **Code · کد:** [`code/week14.py`](code/week14.py), cell 1 · سلول 1

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
stimulus features  P(A) true  A responses / 20
      A1     1110       0.84                15
      A2     1010       0.88                18
      A3     1011       0.91                18
      A4     1101       0.60                10
      A5     0111       0.60                11
      B1     1100       0.47                10
      B2     0110       0.47                11
      B3     0001       0.16                 4
      B4     0000       0.12                 2
      T1     1001       0.58                11
      T2     1000       0.48                11
      T3     1111       0.87                20
      T4     0010       0.48                10
      T5     0101       0.26                 6
      T6     0011       0.58                12
      T7     0100       0.19                 4
```

### Part B: fit and compare (25 min) · بخش B: برازش و مقایسه (25 دقیقه)

> **Code · کد:** [`code/week14.py`](code/week14.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
GCM       NLL =  28.36  AIC =  64.72  BIC =  79.79  c = 3.82  w = [0.397 0.111 0.426 0.066]
prototype NLL =  30.02  AIC =  68.04  BIC =  83.11  c = 1.90  w = [0.435 0.009 0.461 0.095]
stimulus  observed   GCM  prototype
      A1      0.75 0.842      0.822
      A2      0.90 0.884      0.818
```

**Interpret:**
1. Which model is preferred, and how strong is the evidence? ($\Delta\mathrm{AIC} = 3.3$, so Akaike weights of about 0.84 vs. 0.16: a moderate preference, not a decisive one.)
2. Look at A1 and A2. The data show A2 (0.90) classified better than A1 (0.75). The GCM predicts this ordering (0.88 vs. 0.84); the prototype model cannot (0.82 vs. 0.82). Why does this comparison discriminate between the theories more sharply than the overall fit statistic?
3. Interpret the GCM attention weights. Which dimensions did the participant attend to, and does that make sense given the category structure?

<div dir="rtl">

**تفسیر کنید:**
1. کدام مدل ترجیح دارد و شواهد چقدر قوی است؟ ($\Delta\mathrm{AIC} = 3.3$، پس وزن‌های Akaike حدود 0.84 در برابر 0.16: ترجیحی متوسط، نه قاطع.)
2. به A1 و A2 نگاه کنید. داده نشان می‌دهد A2 (0.90) بهتر از A1 (0.75) دسته‌بندی شده. GCM این ترتیب را پیش‌بینی می‌کند (0.88 در برابر 0.84)؛ مدل prototype نمی‌تواند (0.82 در برابر 0.82). چرا این مقایسه بین دو نظریه تیزتر از آماره‌ی برازش کلی تمایز می‌گذارد؟
3. وزن‌های توجه GCM را تفسیر کنید. شرکت‌کننده به کدام ابعاد توجه کرده، و آیا با ساختار دسته جور درمی‌آید؟

</div>

### Part C: is the GCM recoverable at this design? (15 min) · بخش C: آیا GCM در این طرح قابل بازیابی است؟ (15 دقیقه)

> **Code · کد:** [`code/week14.py`](code/week14.py), cell 3 · سلول 3

**Expected output** (about 1 minute):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 1 دقیقه):

</div>

```text
c: r(true, recovered) = 0.08
w1: r(true, recovered) = 0.91
w2: r(true, recovered) = 0.76
w3: r(true, recovered) = 0.89
w4: r(true, recovered) = 0.85
```

**What to notice:** the attention weights are recovered well (r = 0.76–0.91), but the sensitivity $c$ is essentially **not recoverable** at this design (r = 0.08). With only 16 stimuli and 20 trials each, a large $c$ and a moderate $c$ can produce very similar response proportions (once $c$ is large, predictions saturate), and $c$ trades off with how concentrated the weights are. So we should interpret the attention weights from Part B but **not** the value $\hat c = 3.82$. More trials, a wider range of stimuli, or a Bayesian prior on $c$ would help. This is exactly the kind of result a recovery study is for (Week 7).

<div dir="rtl">

**به چه دقت کنید:** وزن‌های توجه خوب بازیابی می‌شوند (r = 0.76–0.91)، ولی حساسیت $c$ در این طرح عملاً **قابل بازیابی نیست** (r = 0.08). با فقط 16 محرک و 20 trial برای هرکدام، یک $c$ بزرگ و یک $c$ متوسط می‌توانند نسبت‌های پاسخ خیلی شبیهی بدهند (وقتی $c$ بزرگ شد، پیش‌بینی‌ها اشباع می‌شوند)، و $c$ با میزان متمرکز بودن وزن‌ها trade-off دارد. پس باید وزن‌های توجه بخش B را تفسیر کنیم ولی مقدار $\hat c = 3.82$ را **نه**. trialهای بیشتر، دامنه‌ی محرک گسترده‌تر، یا یک پیشین بیزی روی $c$ کمک می‌کند. این دقیقاً همان نوع نتیجه‌ای است که مطالعه‌ی بازیابی برایش ساخته شده (هفته‌ی 7).

</div>

### Part D: drift-diffusion and EZ (40 min) · بخش D: drift-diffusion و EZ (40 دقیقه)

> **Code · کد:** [`code/week14.py`](code/week14.py), cell 4 · سلول 4

**Expected output** (about 30 s):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 30 ثانیه):

</div>

```text
instruction difficulty    Pc   MRT  v_true  v_EZ  a_true  a_EZ  Ter_EZ
      speed       easy 0.870 0.423    0.25 0.243    0.08 0.078   0.304
      speed       hard 0.732 0.466    0.12 0.115    0.08 0.088   0.288
   accuracy       easy 0.975 0.572    0.25 0.261    0.14 0.140   0.317
   accuracy       hard 0.818 0.697    0.12 0.111    0.14 0.135   0.313
```

> **Code · کد:** [`code/week14.py`](code/week14.py), cell 5 · سلول 5

### Part E: interpret the 2 × 2 experiment (20 min) · بخش E: تفسیر آزمایش 2 × 2 (20 دقیقه)

Answer in your notebook:
1. Which EZ parameter changes with the **instruction** manipulation, and which with **difficulty**? Did either manipulation affect the parameter it should *not* affect?
2. Describe how the RT distribution changes from speed to accuracy instructions (Part D figure). Which part of the distribution changes most: the leading edge or the tail?
3. A clinical study finds that patients are slower than controls but equally accurate. Sketch two different DDM accounts of this result, and say which data would distinguish them.

<div dir="rtl">

در notebook جواب دهید:
1. کدام پارامتر EZ با دست‌کاری **دستورالعمل** تغییر می‌کند و کدام با **دشواری**؟ آیا هیچ‌کدام از دست‌کاری‌ها روی پارامتری که *نباید* اثر بگذارد اثر گذاشت؟
2. توصیف کنید توزیع RT از دستورالعمل سرعت به دقت چطور تغییر می‌کند (نمودار بخش D). کدام بخش توزیع بیشتر تغییر می‌کند: لبه‌ی جلویی یا دنباله؟
3. یک مطالعه‌ی بالینی نشان می‌دهد بیماران از گروه کنترل کندترند ولی به همان اندازه دقیق. دو تبیین مختلف DDM برای این نتیجه طرح کنید و بگویید کدام داده‌ها بین آن‌ها تمایز می‌گذارند.

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Compute $P(A\mid\text{A1})$ and $P(A\mid\text{A2})$ by hand for equal weights and $c = 2$ under both models. Do they reproduce the critical prediction?

<div dir="rtl">

**تمرین 1 ★.** $P(A\mid\text{A1})$ و $P(A\mid\text{A2})$ را برای وزن‌های برابر و $c = 2$ تحت هر دو مدل با دست حساب کنید. آیا پیش‌بینی کلیدی را بازتولید می‌کنند؟

</div>

**Exercise 2 ★.** Apply EZ to the worked example's statistics and to $P_c = 1.0$ with $N = 100$ trials (use the edge correction). What happens without the correction?

<div dir="rtl">

**تمرین 2 ★.** EZ را روی آماره‌های مثال حل‌شده و روی $P_c = 1.0$ با $N = 100$ trial (با تصحیح مرزی) اعمال کنید. بدون تصحیح چه اتفاقی می‌افتد؟

</div>

**Exercise 3 ★★ (prototype data).** Generate data from the **prototype** model and fit both models. Does the model comparison identify the generating model? Run a small model recovery (20 datasets per generating model) and build the 2 × 2 confusion matrix.

<div dir="rtl">

**تمرین 3 ★★ (داده‌ی prototype).** داده را از مدل **prototype** تولید کنید و هر دو مدل را برازش کنید. آیا مقایسه‌ی مدل، مدل مولد را تشخیص می‌دهد؟ یک بازیابی مدل کوچک اجرا کنید (20 مجموعه داده برای هر مدل مولد) و confusion matrix 2 × 2 را بسازید.

</div>

**Exercise 4 ★★ (EZ recovery and bias).** For 200 simulated participants with random $(v, a, T_{er})$ and only 100 trials each, compare EZ estimates with the true values. Which parameter is recovered worst? Then add across-trial drift variability to the simulator (Week 1, Exercise 5) and check which EZ estimate becomes biased.

<div dir="rtl">

**تمرین 4 ★★ (بازیابی و سوگیری EZ).** برای 200 شرکت‌کننده‌ی شبیه‌سازی‌شده با $(v, a, T_{er})$ تصادفی و فقط 100 trial برای هرکدام، برآوردهای EZ را با مقادیر واقعی مقایسه کنید. کدام پارامتر بدتر از همه بازیابی می‌شود؟ بعد تغییرپذیری بین trialها drift را به شبیه‌ساز اضافه کنید (تمرین 5 هفته‌ی 1) و ببینید کدام برآورد EZ سوگیر می‌شود.

</div>

**Exercise 5 ★★★ (Advanced: Bayesian GCM).** Fit the GCM in PyMC with priors $c \sim \mathrm{Gamma}(2, \text{scale } 2)$ and $w \sim \mathrm{Dirichlet}(1, 1, 1, 1)$. Compare the posterior of the attention weights with the MLE, and run a posterior predictive check on the A1-vs-A2 difference. (See Lee & Wagenmakers, chapter 17, for a hierarchical version.)

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: GCM بیزی).** GCM را در PyMC با پیشین‌های $c \sim \mathrm{Gamma}(2, \text{scale } 2)$ و $w \sim \mathrm{Dirichlet}(1, 1, 1, 1)$ برازش کنید. پسین وزن‌های توجه را با MLE مقایسه کنید و یک بررسی پیش‌بینی پسین روی تفاوت A1 و A2 اجرا کنید. (برای نسخه‌ی سلسله‌مراتبی، Lee & Wagenmakers فصل 17 را ببینید.)

</div>

### Lab check-off · lab check-off

Show: (1) the fit table and prediction plot for the GCM vs. the prototype model with your answer to question 2, (2) the EZ table for the 2 × 2 design, and (3) your answer to Part E, question 1.

<div dir="rtl">

نشان دهید: (1) جدول برازش و نمودار پیش‌بینی GCM در برابر مدل prototype همراه با جوابتان به سؤال 2، (2) جدول EZ برای طرح 2 × 2، و (3) جوابتان به سؤال 1 بخش E.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**Exemplar models in a learned "semantic space".** The GCM needs a psychological space in which to measure distances. Traditionally, that space comes from similarity ratings and multidimensional scaling. Language models offer an alternative: every word or sentence is mapped to an **embedding vector**, and the distances between vectors are often used as a stand-in for psychological similarity. Combining embeddings with the GCM gives a model that can classify *any* new word with no extra similarity ratings. Whether embedding distances match human similarity is an empirical question, and you can test it with the tools of this course.

<div dir="rtl">

**مدل‌های exemplar در یک «فضای معنایی» یادگرفته‌شده.** GCM به یک فضای روان‌شناختی نیاز دارد تا فاصله‌ها را در آن اندازه بگیرد. به‌طور سنتی این فضا از رتبه‌بندی‌های شباهت و مقیاس‌بندی چندبعدی (MDS) می‌آید. مدل‌های زبانی یک جایگزین پیشنهاد می‌کنند: هر کلمه یا جمله به یک **بردار embedding** نگاشت می‌شود، و فاصله‌ی بین بردارها اغلب به جای شباهت روان‌شناختی استفاده می‌شود. ترکیب embeddingها با GCM مدلی می‌دهد که می‌تواند *هر* کلمه‌ی تازه‌ای را بدون رتبه‌بندی شباهت اضافه دسته‌بندی کند. اینکه فاصله‌های embedding با شباهت انسانی جور درمی‌آیند یا نه یک سؤال تجربی است، و می‌توانید آن را با ابزارهای این درس بیازمایید.

</div>

> **Code · کد:** [`code/week14.py`](code/week14.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
P(fruit | tomato) = 0.902
P(fruit | knife) = 0.094
P(fruit | nutcracker) = 0.370
```

**Try it (no API needed).**
- ★ Change $c$ to 1 and to 10. How do the three predictions change, and why does "nutcracker" change the most?
- ★★ Suppose 20 participants classified the three probes, with 19, 1 and 12 "fruit" responses. Fit $c$ by MLE (binomial likelihood, Week 4) and run a $G^2$ test. Does the embedding space with a single parameter fit?
- ★★ Discussion: the embeddings were learned from text, not from perception. For which categories might text-based similarity differ systematically from human similarity (think of color or shape)?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ $c$ را به 1 و به 10 تغییر دهید. سه پیش‌بینی چطور عوض می‌شوند، و چرا «nutcracker» بیشتر از همه تغییر می‌کند؟
- ★★ فرض کنید 20 شرکت‌کننده سه محرک آزمون را دسته‌بندی کرده‌اند، با 19، 1 و 12 پاسخ «fruit». $c$ را با MLE برازش کنید (درست‌نمایی دوجمله‌ای، هفته‌ی 4) و یک آزمون $G^2$ اجرا کنید. آیا فضای embedding با یک پارامتر برازش خوبی دارد؟
- ★★ بحث: embeddingها از متن یاد گرفته شده‌اند، نه از ادراک. برای کدام دسته‌ها ممکن است شباهت مبتنی بر متن به‌طور نظام‌مند با شباهت انسانی فرق کند (به رنگ یا شکل فکر کنید)؟

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **Unconstrained attention weights.** Without a sum-to-one constraint, $c$ and $w$ trade off perfectly (non-identifiable). Use a softmax reparameterization.
2. **Judging exemplar vs. prototype models by overall fit only.** The theoretically diagnostic predictions (A1 vs. A2) are often more informative than small differences in AIC.
3. **Averaging classification data over participants** who attend to different dimensions. This can make an exemplar-like individual look prototype-like (and vice versa); recall Week 5's aggregation artifacts.
4. **Using EZ with incorrect units.** RTs must be in **seconds** and the variance in s², with $s = 0.1$. Mixing ms and s gives nonsense.
5. **Applying EZ when its assumptions are violated** (strong bias, slow or fast errors). Check error RTs; use the full DDM if needed.
6. **"A slower group has a lower drift rate."** Slowness can come from a higher boundary, a lower drift, or a longer non-decision time. Only a model fitted to accuracy *and* RT distributions can tell which.
7. **Forgetting the edge cases** $P_c = 1$ or $P_c \le 0.5$ in EZ.

<div dir="rtl">

1. **وزن‌های توجه بدون قید.** بدون قید جمع‌برابر-یک، $c$ و $w$ کاملاً با هم trade-off دارند (non-identifiable). از reparameterization softmax استفاده کنید.
2. **قضاوت درباره‌ی مدل‌های exemplar و prototype فقط با برازش کلی.** پیش‌بینی‌هایی که از نظر نظری تشخیصی‌اند (A1 در برابر A2) اغلب آگاهی‌بخش‌تر از تفاوت‌های کوچک AIC هستند.
3. **میانگین‌گیری داده‌ی دسته‌بندی روی شرکت‌کننده‌هایی** که به ابعاد مختلف توجه می‌کنند. این می‌تواند یک فرد exemplar‌گونه را prototype‌گونه نشان دهد (و برعکس)؛ خطاهای میانگین‌گیری هفته‌ی 5 را به یاد بیاورید.
4. **استفاده از EZ با واحدهای غلط.** RTها باید بر حسب **ثانیه** و واریانس بر حسب s² باشد، با $s = 0.1$. قاطی کردن ms و s نتیجه‌ی بی‌معنی می‌دهد.
5. **استفاده از EZ وقتی فرض‌هایش نقض شده‌اند** (سوگیری قوی، خطاهای کند یا سریع). RTهای خطا را بررسی کنید؛ در صورت نیاز از DDM کامل استفاده کنید.
6. **«گروه کندتر drift rate پایین‌تری دارد.»** کندی می‌تواند از مرز بالاتر، drift پایین‌تر یا non-decision time طولانی‌تر بیاید. فقط مدلی که روی دقت *و* توزیع‌های RT برازش شده می‌تواند بگوید کدام.
7. **فراموش کردن حالت‌های مرزی** $P_c = 1$ یا $P_c \le 0.5$ در EZ.

</div>

---

## Check your understanding · خودآزمایی

**1.** State the core difference between exemplar and prototype theories in one sentence each.
<details><summary>Answer</summary>
Exemplar: a category is represented by all stored instances, and classification depends on summed similarity to them. Prototype: a category is represented by a single summary (central tendency), and classification depends on similarity to that summary.
</details>

<div dir="rtl">

**1.** تفاوت اصلی نظریه‌های exemplar و prototype را هرکدام در یک جمله بیان کنید.
<details><summary>پاسخ</summary>
Exemplar: یک دسته با همه‌ی نمونه‌های ذخیره‌شده نمایش داده می‌شود و دسته‌بندی به شباهت جمع‌شده با آن‌ها بستگی دارد. Prototype: یک دسته با یک خلاصه‌ی واحد (گرایش مرکزی) نمایش داده می‌شود و دسته‌بندی به شباهت با آن خلاصه بستگی دارد.
</details>

</div>

**2.** In the 5-4 structure, why is the A1-vs-A2 comparison diagnostic?
<details><summary>Answer</summary>
A1 is closer to the A prototype (3 of 4 features), so a prototype model predicts it is classified better than A2. But A2 is very similar to other A exemplars and to no B exemplar, while A1 is similar to two B exemplars, so the exemplar model can predict A2 ≥ A1. The theories make opposite ordinal predictions.
</details>

<div dir="rtl">

**2.** در ساختار 5-4، چرا مقایسه‌ی A1 و A2 تشخیصی است؟
<details><summary>پاسخ</summary>
A1 به prototype دسته‌ی A نزدیک‌تر است (3 از 4 ویژگی)، پس مدل prototype پیش‌بینی می‌کند بهتر از A2 دسته‌بندی شود. ولی A2 به exemplarهای دیگر A خیلی شبیه است و به هیچ exemplar از B شبیه نیست، در حالی که A1 به دو exemplar از B شبیه است، پس مدل exemplar می‌تواند A2 ≥ A1 را پیش‌بینی کند. دو نظریه پیش‌بینی‌های ترتیبی متضاد دارند.
</details>

</div>

**3.** What do the GCM parameters $c$ and $w_m$ represent?
<details><summary>Answer</summary>
$c$ is sensitivity: how quickly similarity decreases with psychological distance (large $c$ means only very close exemplars matter). $w_m$ is the proportion of attention allocated to dimension $m$, which stretches distances along attended dimensions.
</details>

<div dir="rtl">

**3.** پارامترهای $c$ و $w_m$ در GCM چه چیزی را نشان می‌دهند؟
<details><summary>پاسخ</summary>
$c$ حساسیت است: شباهت با فاصله‌ی روان‌شناختی چقدر سریع کم می‌شود ($c$ بزرگ یعنی فقط exemplarهای خیلی نزدیک مهم‌اند). $w_m$ نسبت توجهی است که به بعد $m$ داده می‌شود و فاصله‌ها را در امتداد ابعاد مورد توجه کش می‌دهد.
</details>

</div>

**4.** Which DDM parameter would you expect to change under (a) speed vs. accuracy instructions, (b) harder stimuli, (c) a slower motor response (e.g., foot instead of finger)?
<details><summary>Answer</summary>
(a) Boundary separation $a$. (b) Drift rate $v$. (c) Non-decision time $T_{er}$.
</details>

<div dir="rtl">

**4.** انتظار دارید کدام پارامتر DDM تحت این موارد تغییر کند: (الف) دستورالعمل سرعت در برابر دقت، (ب) محرک‌های سخت‌تر، (ج) پاسخ حرکتی کندتر (مثلاً پا به جای انگشت)؟
<details><summary>پاسخ</summary>
(الف) فاصله‌ی مرزها $a$. (ب) drift rate $v$. (ج) non-decision time $T_{er}$.
</details>

</div>

**5.** What three statistics does EZ-diffusion need, and what are its main assumptions?
<details><summary>Answer</summary>
Proportion correct, the variance of correct RTs, and the mean of correct RTs. It assumes an unbiased starting point ($z = a/2$), no across-trial variability in parameters, and the scaling $s = 0.1$.
</details>

<div dir="rtl">

**5.** EZ-diffusion به کدام سه آماره نیاز دارد و فرض‌های اصلی‌اش چیست؟
<details><summary>پاسخ</summary>
نسبت پاسخ‌های درست، واریانس RTهای درست و میانگین RTهای درست. فرض می‌کند نقطه‌ی شروع بی‌سوگیر است ($z = a/2$)، پارامترها تغییرپذیری بین trialها ندارند، و مقیاس $s = 0.1$ است.
</details>

</div>

**6.** How is the DDM related to the random walk model of Week 1?
<details><summary>Answer</summary>
It is the continuous-time, continuous-evidence limit of the random walk: as step size and step duration go to zero together, the random walk converges to a Wiener diffusion process with drift $v$ and noise $s$.
</details>

<div dir="rtl">

**6.** DDM چه ارتباطی با مدل random walk هفته‌ی 1 دارد؟
<details><summary>پاسخ</summary>
حد زمان-پیوسته و شواهد-پیوسته‌ی random walk است: وقتی اندازه‌ی گام و مدت گام با هم به صفر میل کنند، random walk به یک فرایند انتشار Wiener با drift $v$ و نویز $s$ همگرا می‌شود.
</details>

</div>

---

## Assignment · تکلیف

- **A5 (MCMC from scratch)** is due at the start of this week's lecture.
- No new assignment: work on the **final project**. If your project uses the GCM or DDM, today's code is a good starting point; cite the course materials and say what you changed.

<div dir="rtl">

- **A5 (MCMC از صفر)** در ابتدای درس این هفته تحویل داده می‌شود.
- تکلیف جدیدی نداریم: روی **پروژه‌ی پایانی** کار کنید. اگر پروژه‌تان از GCM یا DDM استفاده می‌کند، کد امروز نقطه‌ی شروع خوبی است؛ به مواد درس ارجاع دهید و بگویید چه چیزی را تغییر داده‌اید.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Lee & Wagenmakers (2014), chapter 17.** The Generalized Context Model, fitted in a Bayesian (and hierarchical) way to category-learning data. *(Main reading for categorization.)*
- **Farrell & Lewandowsky (2018)**: the chapter on models of choice response time [verify chapter number] for the drift-diffusion model and its relatives.
- **Verguts (2022)**: the chapters on categorization and on decision making [verify chapters].
- *Optional, outside the course list:* Wagenmakers, E.-J., van der Maas, H. L. J., & Grasman, R. P. P. P. (2007). An EZ-diffusion model for response time and accuracy. *Psychonomic Bulletin & Review, 14*, 3–22. Medin, D. L., & Schaffer, M. M. (1978). Context theory of classification learning. *Psychological Review, 85*, 207–238.

<div dir="rtl">

- **Lee & Wagenmakers (2014)، فصل 17.** مدل بافت تعمیم‌یافته که به روش بیزی (و سلسله‌مراتبی) روی داده‌ی یادگیری دسته برازش می‌شود. *(منبع اصلی برای دسته‌بندی.)*
- **Farrell & Lewandowsky (2018)**: فصل مدل‌های زمان پاسخ انتخابی [شماره‌ی فصل بررسی شود] برای مدل drift-diffusion و خویشاوندانش.
- **Verguts (2022)**: فصل‌های دسته‌بندی و تصمیم‌گیری [فصل‌ها بررسی شود].
- *اختیاری، خارج از فهرست درس:* Wagenmakers, E.-J., van der Maas, H. L. J., & Grasman, R. P. P. P. (2007). An EZ-diffusion model for response time and accuracy. *Psychonomic Bulletin & Review, 14*, 3–22. Medin, D. L., & Schaffer, M. M. (1978). Context theory of classification learning. *Psychological Review, 85*, 207–238.

</div>

*Preview for Week 15:* learning from rewards (reinforcement learning), the mind as a Bayesian observer, and how cognitive models and AI systems inform each other.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 15:* یادگیری از پاداش‌ها (یادگیری تقویتی)، ذهن به‌عنوان یک مشاهده‌گر بیزی، و اینکه مدل‌های شناختی و سیستم‌های هوش مصنوعی چطور به هم کمک می‌کنند.

</div>
