# Week 15: Modeling in Cognitive Science II: Reinforcement Learning, Bayesian Cognition and AI · هفته‌ی 15: مدل‌سازی در علوم شناختی 2: یادگیری تقویتی، شناخت بیزی و هوش مصنوعی

> **Chapter 6: Examples of modeling in different areas of cognitive science** · Lecture 1 h · Lab 2 h
> **Running data:** simulated choices in a two-armed bandit task with a reversal; a simulated visual–haptic cue-combination experiment.

<div dir="rtl">

> **فصل 6: نمونه‌هایی از مدل‌سازی در حوزه‌های مختلف علوم شناختی** · درس 1 ساعت · lab 2 ساعت
> **داده‌ی اصلی:** انتخاب‌های شبیه‌سازی‌شده در یک تکلیف bandit دوبازویی با یک وارونگی (reversal)؛ یک آزمایش شبیه‌سازی‌شده‌ی ترکیب نشانه‌های بینایی–لامسه‌ای (cue combination).

</div>

---

## Key terms · واژه‌های کلیدی

Important terms of this lesson, with their Persian equivalents (repeated even if they appeared in earlier weeks).

<div dir="rtl">

واژه‌های مهم این درس با معادل فارسی‌شان (حتی اگر در درس‌های قبل آمده باشند).

</div>

| English | فارسی | توضیح کوتاه |
|---|---|---|
| simulation | شبیه‌سازی | تولید داده‌ی مصنوعی با اجرای مدل |
| bandit task | تکلیف bandit | انتخاب مکرر بین گزینه‌هایی با پاداش احتمالی |
| cue combination | ترکیب نشانه‌ها (cues) | ترکیب اطلاعات چند حس برای یک برآورد |
| Q-learning | Q-learning | قاعده‌ی یادگیری ارزش گزینه‌ها |
| softmax / inverse temperature (β) | softmax / دمای معکوس | تبدیل ارزش‌ها به احتمال انتخاب |
| learning rate (α) | نرخ یادگیری | اندازه‌ی به‌روزرسانی بعد از هر خطا |
| temperature | دما (temperature) | پارامتر نویز در انتخاب token؛ β = 1/T |
| trial | کوشش (trial) | یک بار انجام تکلیف توسط شرکت‌کننده |
| likelihood | درست‌نمایی | احتمال داده به‌عنوان تابعی از پارامترها |
| fit / fitting | برازش | تنظیم پارامترها تا مدل با داده جور شود |
| parameter recovery | بازیابی پارامتر | آیا برازش، پارامترهای معلوم شبیه‌سازی را برمی‌گرداند |
| parameter | پارامتر | کمیت قابل تنظیم مدل که بین افراد یا شرایط فرق می‌کند |
| ideal observer | مشاهده‌گر ایده‌آل | مدل استنباط بهینه با اطلاعات موجود |
| cognitive model | مدل شناختی | توصیف دقیق و ریاضی یا محاسباتی از یک فرایند ذهنی |
| exploration / exploitation | کاوش / بهره‌برداری | امتحان گزینه‌های دیگر / انتخاب بهترین گزینه‌ی فعلی |
| prediction error | خطای پیش‌بینی | تفاوت پاداش گرفته‌شده و پاداش مورد انتظار |
| reinforcement learning (RL) | یادگیری تقویتی | یادگیری از پاداش و پیامد |
| noise | نویز | تغییرات تصادفی در شواهد یا در داده |
| estimate / estimator | برآورد / برآوردگر | مقدار به‌دست‌آمده برای پارامتر / روش به دست آوردن آن |
| reliability | پایایی (قابلیت اطمینان) | دقت یک نشانه؛ عکس واریانس آن |
| large language model (LLM) | مدل بزرگ زبانی | شبکه‌ی عصبی‌ای که کلمه‌ی بعدی متن را پیش‌بینی می‌کند |
| parameter trade-off | بده‌بستان پارامترها | تغییر یک پارامتر که با پارامتر دیگر جبران می‌شود |
| RLHF / reward model | RLHF / مدل پاداش | آموزش chatbot از روی ترجیحات انسانی |
| Bradley–Terry model | مدل Bradley–Terry | مدل انتخاب برای مقایسه‌های جفتی |

---

## Learning outcomes · اهداف یادگیری

By the end of this week, students will be able to:

<div dir="rtl">

در پایان این هفته، دانشجویان می‌توانند:

</div>

1. **Formalize** reward learning with the Rescorla–Wagner / Q-learning rule and a softmax choice rule, and **interpret** the learning rate and inverse temperature.
2. **Write** the trial-by-trial likelihood of a learning model, **fit** it by MLE, and **evaluate** parameter recovery and model recovery against simpler strategies.
3. **Derive** the predictions of a Bayesian ideal observer for cue combination, and **test** whether simulated behavior is optimal.
4. **Distinguish** Bayesian models of cognition (a claim about the mind) from Bayesian data analysis (a method for scientists).
5. **Discuss** how cognitive models and AI systems inform each other, and how the evaluation tools of this course apply to AI systems proposed as models of cognition.

<div dir="rtl">

1. یادگیری از پاداش را با قاعده‌ی Rescorla–Wagner / Q-learning و قاعده‌ی انتخاب softmax **صورت‌بندی کنند** و نرخ یادگیری و inverse temperature را **تفسیر کنند**.
2. درست‌نمایی trial به trial یک مدل یادگیری را **بنویسند**، آن را با MLE **برازش کنند**، و بازیابی پارامتر و بازیابی مدل را در برابر راهبردهای ساده‌تر **ارزیابی کنند**.
3. پیش‌بینی‌های یک مشاهده‌گر ایده‌آل بیزی (Bayesian ideal observer) را برای ترکیب نشانه‌ها **استخراج کنند** و **بیازمایند** که آیا رفتار شبیه‌سازی‌شده بهینه است.
4. مدل‌های بیزی شناخت (ادعایی درباره‌ی ذهن) را از تحلیل داده‌ی بیزی (روشی برای دانشمندان) **تمیز دهند**.
5. درباره‌ی اینکه مدل‌های شناختی و سیستم‌های هوش مصنوعی چطور به هم کمک می‌کنند، و اینکه ابزارهای ارزیابی این درس چطور روی سیستم‌های هوش مصنوعی‌ای که به‌عنوان مدل شناخت پیشنهاد می‌شوند به کار می‌روند، **بحث کنند**.

</div>

---

## Motivation & big picture · مقدمه

**Learning from consequences.** A participant repeatedly chooses between two slot machines, one paying off more often than the other. Halfway through, the machines secretly swap. How quickly does the participant notice and adapt? How much do they explore versus exploit? One of the most successful models in all of psychology and neuroscience answers with a single equation: update your expectation by a fraction of the **prediction error**, the difference between what you got and what you expected. The same error-driven rule appears in classical conditioning (Rescorla–Wagner), in connectionist learning (the delta rule), in the firing of dopamine neurons, and in the reinforcement-learning algorithms behind modern AI systems. Fitting it to choice data is one of the most common uses of cognitive modeling today, in computational psychiatry for instance.

<div dir="rtl">

**یادگیری از پیامدها.** یک شرکت‌کننده بارها بین دو ماشین بازی انتخاب می‌کند که یکی بیشتر از دیگری پاداش می‌دهد. وسط کار، ماشین‌ها مخفیانه جایشان عوض می‌شود. شرکت‌کننده چقدر سریع متوجه می‌شود و خودش را تطبیق می‌دهد؟ چقدر کاوش (explore) می‌کند و چقدر بهره‌برداری (exploit)؟ یکی از موفق‌ترین مدل‌های کل روان‌شناسی و علوم اعصاب با یک معادله جواب می‌دهد: انتظارتان را به اندازه‌ی کسری از **خطای پیش‌بینی** (prediction error)، یعنی تفاوت چیزی که گرفتید و چیزی که انتظار داشتید، به‌روز کنید. همین قاعده‌ی خطامحور در شرطی‌سازی کلاسیک (Rescorla–Wagner)، در یادگیری پیوندگرا (قاعده‌ی دلتا)، در شلیک نورون‌های دوپامینی، و در الگوریتم‌های یادگیری تقویتی پشت سیستم‌های هوش مصنوعی امروزی دیده می‌شود. برازش آن روی داده‌ی انتخاب یکی از رایج‌ترین کاربردهای مدل‌سازی شناختی امروز است، مثلاً در روان‌پزشکی محاسباتی.

</div>

**The mind as a statistician.** When you see and touch an object at the same time, vision and touch both give noisy estimates of its size. A *Bayesian ideal observer* combines them by weighting each cue by its reliability, which gives an estimate more precise than either alone. Do people do this? This is a different use of the word "Bayesian" from Weeks 9–13: here Bayes' rule is a **hypothesis about the mind**, at Marr's computational level (Week 1).

<div dir="rtl">

**ذهن به‌عنوان آماردان.** وقتی یک شیء را هم‌زمان می‌بینید و لمس می‌کنید، بینایی و لامسه هر دو برآوردی پرنویز از اندازه‌اش می‌دهند. یک *مشاهده‌گر ایده‌آل بیزی* آن‌ها را با وزن دادن به هر نشانه به نسبت پایایی‌اش ترکیب می‌کند، که برآوردی دقیق‌تر از هرکدام به تنهایی می‌دهد. آیا آدم‌ها این کار را می‌کنند؟ این کاربردی متفاوت از کلمه‌ی «بیزی» نسبت به هفته‌های 9–13 است: اینجا قاعده‌ی بیز یک **فرضیه درباره‌ی ذهن** است، در سطح محاسباتی Marr (هفته‌ی 1).

</div>

**Cognitive models ↔ AI.** Many ideas travel in both directions between cognitive modeling and AI: error-driven learning, neural networks, reinforcement learning, Bayesian inference. Today AI systems, including large language models, are themselves proposed as models of human cognition. The tools of this course (likelihoods, model comparison, generalization tests, recovery) are exactly what is needed to evaluate such claims.

<div dir="rtl">

**مدل‌های شناختی ↔ هوش مصنوعی.** خیلی از ایده‌ها در هر دو جهت بین مدل‌سازی شناختی و هوش مصنوعی رفت‌وآمد می‌کنند: یادگیری خطامحور، شبکه‌های عصبی، یادگیری تقویتی، استنباط بیزی. امروز خود سیستم‌های هوش مصنوعی، از جمله مدل‌های بزرگ زبانی (LLMها)، به‌عنوان مدل شناخت انسان پیشنهاد می‌شوند. ابزارهای این درس (درست‌نمایی، مقایسه‌ی مدل، آزمون‌های تعمیم، بازیابی) دقیقاً همان چیزی‌اند که برای ارزیابی چنین ادعاهایی لازم است.

</div>

#### Where is this used? · این موضوع کجا به کار می‌رود؟

- **Computational psychiatry**: reinforcement-learning models are fitted to choices of patients with depression, addiction, schizophrenia or OCD, to test whether they learn differently from rewards and punishments (e.g. a lower learning rate after losses).
- **Neuroscience**: the prediction error of the delta rule matches the activity of dopamine neurons, one of the best-known links between a cognitive model and the brain.
- **Education and games**: adaptive learning systems and game design use RL ideas to model how players and learners adjust to feedback.
- **Perception and robotics**: optimal cue combination explains how people combine vision, touch and hearing, and the same weighting rule is used in sensor fusion.
- **AI**: modern reinforcement learning and the training of chatbots from human preferences (RLHF) use the same choice models (see the AI & LLMs section).

<div dir="rtl">

- **روان‌پزشکی محاسباتی:** مدل‌های یادگیری تقویتی روی انتخاب‌های بیماران افسرده، معتاد، مبتلا به اسکیزوفرنی یا وسواس برازش می‌شوند تا آزموده شود که آیا از پاداش و تنبیه متفاوت یاد می‌گیرند (مثلاً نرخ یادگیری پایین‌تر بعد از ضرر).
- **علوم اعصاب:** خطای پیش‌بینی در قاعده‌ی دلتا با فعالیت نورون‌های دوپامینی جور درمی‌آید؛ یکی از شناخته‌شده‌ترین پیوندهای یک مدل شناختی با مغز.
- **آموزش و بازی:** سیستم‌های یادگیری تطبیقی و طراحی بازی از ایده‌های RL برای مدل کردن اینکه بازیکن‌ها و یادگیرنده‌ها چطور خودشان را با بازخورد تطبیق می‌دهند استفاده می‌کنند.
- **ادراک و رباتیک:** ترکیب بهینه‌ی نشانه‌ها توضیح می‌دهد آدم‌ها چطور بینایی، لامسه و شنوایی را ترکیب می‌کنند، و همین قاعده‌ی وزن‌دهی در ادغام حسگرها (sensor fusion) به کار می‌رود.
- **هوش مصنوعی:** یادگیری تقویتی امروزی و آموزش chatbotها از روی ترجیحات انسانی (RLHF) از همین مدل‌های انتخاب استفاده می‌کنند (بخش هوش مصنوعی و LLMها را ببینید).

</div>

---

## Lecture notes · جزوه‌ی درس

#### In plain words · به زبان ساده

**Learning from rewards.** Each option (e.g. each of two slot machines) has a "value" in the participant's head: how much reward they expect from it. After choosing an option and seeing the outcome, the value is nudged toward what actually happened: *new value = old value + learning rate × (reward − old value)*. The term in brackets is the **prediction error**, the surprise. The **learning rate** $\alpha$ says how big the nudge is. Choices are not perfectly greedy: the **softmax** rule picks the better-valued option more often, and the **inverse temperature** $\beta$ sets how strongly (low $\beta$ = more random exploring, high $\beta$ = almost always the best). Fitting this model means finding the $\alpha$ and $\beta$ that make the participant's actual sequence of choices most likely. **The Bayesian mind:** when two senses give noisy estimates of the same thing (seeing and touching an object's size), the best guess is a weighted average that trusts the more reliable sense more. People often come close to this optimal weighting; the model predicts it with no free parameters, which makes it a strong test.

<div dir="rtl">

**یادگیری از پاداش.** هر گزینه (مثلاً هر کدام از دو دستگاه بازی) در ذهن شرکت‌کننده یک «ارزش» دارد: چقدر پاداش از آن انتظار دارد. بعد از انتخاب یک گزینه و دیدن نتیجه، ارزش کمی به سمت چیزی که واقعاً اتفاق افتاد جابه‌جا می‌شود: *ارزش جدید = ارزش قبلی + نرخ یادگیری × (پاداش − ارزش قبلی)*. عبارت داخل پرانتز **خطای پیش‌بینی** است، یعنی میزان غافلگیری. **نرخ یادگیری** $\alpha$ می‌گوید این جابه‌جایی چقدر بزرگ است. انتخاب‌ها کاملاً حریصانه نیستند: قاعده‌ی **softmax** گزینه‌ی باارزش‌تر را بیشتر انتخاب می‌کند و **inverse temperature** $\beta$ تعیین می‌کند چقدر بیشتر ($\beta$ پایین = کاوش تصادفی‌تر، $\beta$ بالا = تقریباً همیشه بهترین). برازش این مدل یعنی پیدا کردن $\alpha$ و $\beta$ای که دنباله‌ی واقعی انتخاب‌های شرکت‌کننده را محتمل‌ترین کند. **ذهن بیزی:** وقتی دو حس تخمین‌های پرنویزی از یک چیز می‌دهند (دیدن و لمس کردن اندازه‌ی یک شیء)، بهترین حدس یک میانگین وزنی است که به حس قابل اعتمادتر بیشتر اعتماد می‌کند. آدم‌ها اغلب به این وزن‌دهی بهینه نزدیک‌اند؛ مدل این را بدون هیچ پارامتر آزادی پیش‌بینی می‌کند و همین آن را یک آزمون قوی می‌کند.

</div>

**Suggested timing (60 min):** reward learning 20 · fitting learning models 10 · Bayesian models of cognition 15 · cognitive models and AI 10 · course synthesis 5.

<div dir="rtl">

**زمان‌بندی پیشنهادی (60 دقیقه):** یادگیری از پاداش 20 · برازش مدل‌های یادگیری 10 · مدل‌های بیزی شناخت 15 · مدل‌های شناختی و هوش مصنوعی 10 · جمع‌بندی درس 5.

</div>

### 1. Reinforcement learning: the delta rule and Q-learning · 1. یادگیری تقویتی: قاعده‌ی دلتا و Q-learning

**Rescorla–Wagner / delta rule.** After choosing option $o$ on trial $t$ and receiving reward $r_t \in \{0, 1\}$:

<div dir="rtl">

**Rescorla–Wagner / قاعده‌ی دلتا.** بعد از انتخاب گزینه‌ی $o$ در trial $t$ و گرفتن پاداش $r_t \in \{0, 1\}$:

</div>

$$
\delta_t = r_t - Q_t(o) \quad\text{(prediction error)}, \qquad
Q_{t+1}(o) = Q_t(o) + \alpha\,\delta_t,
$$

and the values of unchosen options stay the same. The **learning rate** $\alpha \in [0, 1]$ sets how strongly new outcomes overwrite old expectations. A high $\alpha$ adapts quickly but is noisy; a low $\alpha$ is stable but slow to notice a reversal.

<div dir="rtl">

و ارزش گزینه‌های انتخاب‌نشده ثابت می‌ماند. **نرخ یادگیری** $\alpha \in [0, 1]$ تعیین می‌کند پیامدهای تازه چقدر قوی انتظارات قدیمی را بازنویسی کنند. $\alpha$ بالا سریع تطبیق می‌دهد ولی پرنویز است؛ $\alpha$ پایین پایدار است ولی وارونگی را دیر می‌فهمد.

</div>

**Softmax choice rule.** Values are turned into choice probabilities with **inverse temperature** $\beta \ge 0$:

<div dir="rtl">

**قاعده‌ی انتخاب softmax.** ارزش‌ها با **inverse temperature** $\beta \ge 0$ به احتمال انتخاب تبدیل می‌شوند:

</div>

$$
P(\text{choose } o \text{ on trial } t) = \frac{\exp(\beta\, Q_t(o))}{\sum_{o'} \exp(\beta\, Q_t(o'))}.
$$

$\beta = 0$ means random choice (pure exploration); a large $\beta$ means always picking the currently best option (exploitation). For two options this is a logistic function of the value difference: $P(o_1) = 1/(1 + e^{-\beta(Q_1 - Q_2)})$.

<div dir="rtl">

$\beta = 0$ یعنی انتخاب تصادفی (کاوش محض)؛ $\beta$ بزرگ یعنی همیشه گزینه‌ای که فعلاً بهترین است انتخاب شود (بهره‌برداری). برای دو گزینه این یک تابع لجستیک از تفاوت ارزش‌هاست: $P(o_1) = 1/(1 + e^{-\beta(Q_1 - Q_2)})$.

</div>

**Connections:**
- The update is the **delta rule** of connectionist networks (Verguts, 2022): a single-layer network trained by error correction.
- Prediction errors $\delta_t$ resemble the phasic responses of midbrain dopamine neurons, which made RL models central to computational neuroscience.
- Q-learning with temporal-difference errors is the basis of modern reinforcement learning in AI.

<div dir="rtl">

**ارتباط‌ها:**
- این به‌روزرسانی همان **قاعده‌ی دلتا**ی شبکه‌های پیوندگراست (Verguts, 2022): یک شبکه‌ی تک‌لایه که با تصحیح خطا آموزش می‌بیند.
- خطاهای پیش‌بینی $\delta_t$ شبیه پاسخ‌های فازیک نورون‌های دوپامینی مغز میانی‌اند، و همین مدل‌های RL را در علوم اعصاب محاسباتی محوری کرد.
- Q-learning با خطاهای temporal-difference پایه‌ی یادگیری تقویتی مدرن در هوش مصنوعی است.

</div>

#### Reading the math · خواندن ریاضی

- $Q_t(o)$: the value of option $o$ on trial $t$ (the subscript $t$ is the trial number).
- $\delta_t = r_t - Q_t(o)$: reward received minus reward expected. Positive = pleasant surprise, negative = disappointment.
- $Q_{t+1}(o) = Q_t(o) + \alpha\,\delta_t$. **Example:** $Q = 0.5$, $\alpha = 0.3$, reward 1: $\delta = 0.5$, new $Q = 0.5 + 0.15 = 0.65$. With no reward: $\delta = -0.5$, new $Q = 0.35$.
- **Softmax for two options:** $P(\text{option 1}) = 1/(1 + e^{-\beta(Q_1 - Q_2)})$. With $Q_1 - Q_2 = 0.25$: $\beta = 0$ gives 0.50 (random), $\beta = 3$ gives 0.68, $\beta = 20$ gives 0.99 (almost always option 1).

<div dir="rtl">

- $Q_t(o)$: ارزش گزینه‌ی $o$ در trial شماره‌ی $t$ (زیرنویس $t$ شماره‌ی trial است).
- $\delta_t = r_t - Q_t(o)$: پاداش گرفته‌شده منهای پاداش مورد انتظار. مثبت = غافلگیری خوشایند، منفی = ناامیدی.
- $Q_{t+1}(o) = Q_t(o) + \alpha\,\delta_t$. **مثال:** $Q = 0.5$، $\alpha = 0.3$ و پاداش 1: $\delta = 0.5$ و $Q$ جدید $= 0.5 + 0.15 = 0.65$. بدون پاداش: $\delta = -0.5$ و $Q$ جدید $= 0.35$.
- **softmax برای دو گزینه:** $P(\text{option 1}) = 1/(1 + e^{-\beta(Q_1 - Q_2)})$. با $Q_1 - Q_2 = 0.25$: $\beta = 0$ می‌دهد 0.50 (تصادفی)، $\beta = 3$ می‌دهد 0.68، و $\beta = 20$ می‌دهد 0.99 (تقریباً همیشه گزینه‌ی 1).

</div>

### 2. Fitting a learning model · 2. برازش یک مدل یادگیری

**The likelihood is sequential.** Values depend on the participant's own past choices and rewards, so we run the model through the participant's actual trial sequence and multiply the probabilities it assigned to the choices actually made:

<div dir="rtl">

**درست‌نمایی ترتیبی است.** ارزش‌ها به انتخاب‌ها و پاداش‌های گذشته‌ی خود شرکت‌کننده بستگی دارند، پس مدل را روی دنباله‌ی واقعی trialهای شرکت‌کننده اجرا می‌کنیم و احتمال‌هایی را که به انتخاب‌های واقعاً انجام‌شده نسبت داده در هم ضرب می‌کنیم:

</div>

$$
\ell(\alpha, \beta) = \sum_{t=1}^{T} \ln P\big(\text{choice}_t \mid Q_t(\cdot;\ \alpha, \text{history}_{<t}),\ \beta\big).
$$

**Practical points:**
- Reparameterize: $\alpha = 1/(1 + e^{-\eta_\alpha})$ and $\beta = e^{\eta_\beta}$ (Week 3), and use multi-start.
- **$\alpha$–$\beta$ trade-off:** noisy choice (low $\beta$) and slow or erratic learning (extreme $\alpha$) can produce similar-looking behavior, so the estimates are often correlated across fits, and the sign of the correlation depends on the design and the parameter range. A further problem is that very large $\beta$ values are hard to estimate at all (lab Part C). Recovery studies at the actual design are essential (Week 7).
- **The design matters:** reversals and enough trials are needed to estimate $\alpha$; stable reward probabilities give little information about it.
- **Alternative strategies** must be compared: e.g., *win-stay/lose-shift* (WSLS: repeat a rewarded choice, switch after no reward, with lapse rate $\varepsilon$), or a biased-random model. A good RL fit means little if WSLS fits just as well.

<div dir="rtl">

**نکته‌های عملی:**
- reparameterize کنید: $\alpha = 1/(1 + e^{-\eta_\alpha})$ و $\beta = e^{\eta_\beta}$ (هفته‌ی 3)، و از multi-start استفاده کنید.
- **trade-off $\alpha$–$\beta$:** انتخاب پرنویز ($\beta$ پایین) و یادگیری کند یا نامنظم ($\alpha$ حدی) می‌توانند رفتارهای شبیه به هم بسازند، پس برآوردها در برازش‌های مختلف اغلب همبسته‌اند، و علامت همبستگی به طرح و دامنه‌ی پارامترها بستگی دارد. مشکل دیگر این است که برآورد مقادیر خیلی بزرگ $\beta$ اصلاً سخت است (بخش C lab). مطالعه‌ی بازیابی در همان طرح واقعی ضروری است (هفته‌ی 7).
- **طرح مهم است:** برای برآورد $\alpha$ به وارونگی و trial کافی نیاز است؛ احتمال‌های پاداش ثابت اطلاعات کمی درباره‌اش می‌دهند.
- **راهبردهای جایگزین** باید مقایسه شوند: مثلاً *win-stay/lose-shift* (WSLS: انتخاب پاداش‌گرفته را تکرار کن، بعد از بی‌پاداشی عوض کن، با نرخ لغزش $\varepsilon$)، یا یک مدل تصادفی سوگیر. برازش خوب RL معنای زیادی ندارد اگر WSLS هم به همان خوبی برازش شود.

</div>

#### Reading the math · خواندن ریاضی

$\ell(\alpha, \beta) = \sum_t \ln P(\text{choice}_t \mid Q_t, \beta)$: run the learning model through the participant's *own* sequence of choices and rewards, trial by trial. On each trial, compute the probability the model gave to the choice the participant actually made, take its log, and add up. The worked example (Part 1) does this for four trials: $\ln 0.5 + \ln 0.679 + \ln 0.593 + \ln 0.755 = -1.884$. The best $(\alpha, \beta)$ maximize this sum. It is Week 4's likelihood, except that each trial's probability depends on the history before it.

<div dir="rtl">

$\ell(\alpha, \beta) = \sum_t \ln P(\text{choice}_t \mid Q_t, \beta)$: مدل یادگیری را روی دنباله‌ی انتخاب‌ها و پاداش‌های *خود* شرکت‌کننده، trial به trial، اجرا کن. در هر trial احتمالی را که مدل به انتخابِ واقعی شرکت‌کننده داده حساب کن، لگاریتمش را بگیر و جمع بزن. مثال حل‌شده (بخش 1) این کار را برای چهار trial انجام می‌دهد: $\ln 0.5 + \ln 0.679 + \ln 0.593 + \ln 0.755 = -1.884$. بهترین $(\alpha, \beta)$ این جمع را بیشینه می‌کنند. این همان درست‌نمایی هفته‌ی 4 است، با این تفاوت که احتمال هر trial به تاریخچه‌ی پیش از آن بستگی دارد.

</div>

### 3. Bayesian models of cognition · 3. مدل‌های بیزی شناخت

**Cue combination.** A visual cue $x_V \sim \mathcal{N}(S, \sigma_V)$ and a haptic cue $x_H \sim \mathcal{N}(S, \sigma_H)$ both measure the true size $S$. With a flat prior, the posterior over $S$ is normal with mean

<div dir="rtl">

**ترکیب نشانه‌ها.** یک نشانه‌ی بینایی $x_V \sim \mathcal{N}(S, \sigma_V)$ و یک نشانه‌ی لامسه‌ای $x_H \sim \mathcal{N}(S, \sigma_H)$ هر دو اندازه‌ی واقعی $S$ را می‌سنجند. با پیشین تخت، پسین $S$ نرمال است با میانگین

</div>

$$
\hat S = w_V x_V + w_H x_H, \qquad w_V = \frac{1/\sigma_V^2}{1/\sigma_V^2 + 1/\sigma_H^2}, \quad w_H = 1 - w_V,
$$

and SD

<div dir="rtl">

و انحراف معیار

</div>

$$
\sigma_{VH} = \sqrt{\frac{\sigma_V^2\,\sigma_H^2}{\sigma_V^2 + \sigma_H^2}} \;\le\; \min(\sigma_V, \sigma_H).
$$

**Testable predictions** (tested, e.g., by Ernst & Banks, 2002): (1) the weights should track the cues' reliabilities, which the experimenter can manipulate by degrading one cue; (2) bimodal precision should be *better* than the best single cue, by exactly the amount above. The single-cue SDs are measured separately, so the ideal-observer predictions have **no free parameters**. That makes them strong, falsifiable tests.

<div dir="rtl">

**پیش‌بینی‌های آزمون‌پذیر** (مثلاً آزموده‌شده توسط Ernst & Banks, 2002): (1) وزن‌ها باید پایایی نشانه‌ها را دنبال کنند، که آزمایشگر می‌تواند با تخریب یک نشانه دست‌کاری‌اش کند؛ (2) دقت دوحسی باید *بهتر* از بهترین نشانه‌ی تکی باشد، دقیقاً به اندازه‌ی بالا. انحراف معیارهای تک‌نشانه جداگانه اندازه‌گیری می‌شوند، پس پیش‌بینی‌های مشاهده‌گر ایده‌آل **هیچ پارامتر آزادی ندارند**. همین آن‌ها را آزمون‌هایی قوی و ابطال‌پذیر می‌کند.

</div>

**What a Bayesian model of cognition claims.** That behavior approximates optimal inference given the agent's noise, prior and goals: a **computational-level** account (Marr). It is silent about the algorithm: the brain might approximate Bayes with sampling, heuristics or neural population codes.

<div dir="rtl">

**یک مدل بیزی شناخت چه ادعایی دارد.** اینکه رفتار، با توجه به نویز، پیشین و هدف‌های عامل، تقریبی از استنباط بهینه است: یک تبیین در **سطح محاسباتی** (Marr). درباره‌ی الگوریتم ساکت است: مغز ممکن است بیز را با نمونه‌گیری، heuristicها یا کدهای جمعیتی عصبی تقریب بزند.

</div>

**Criticisms to keep in mind:** with free choices of priors, likelihoods and loss functions, almost any behavior can be called "optimal" after the fact (the flexibility problem of Week 6). Strong tests fix these components independently, as in cue combination.

<div dir="rtl">

**نقدهایی که باید در ذهن داشت:** با انتخاب آزادانه‌ی پیشین‌ها، درست‌نمایی‌ها و تابع‌های زیان، تقریباً هر رفتاری را می‌شود بعد از واقعه «بهینه» نامید (مسئله‌ی انعطاف‌پذیری هفته‌ی 6). آزمون‌های قوی این اجزا را مستقل تثبیت می‌کنند، مثل ترکیب نشانه‌ها.

</div>

**Two meanings, one more time:**

<div dir="rtl">

**دو معنا، یک بار دیگر:**

</div>

| | Bayesian model of cognition | Bayesian data analysis |
|---|---|---|
| Who does the inference? | The participant's mind (hypothetically) | The scientist |
| Prior represents | The participant's beliefs about the world | The scientist's knowledge about parameters |
| Can be wrong if… | People are not optimal | The model or priors are poorly chosen |
| Examples in this course | Cue combination (today) | Weeks 9–13 |

<div dir="rtl">

| | مدل بیزی شناخت | تحلیل داده‌ی بیزی |
|---|---|---|
| چه کسی استنباط می‌کند؟ | ذهن شرکت‌کننده (به‌طور فرضی) | دانشمند |
| پیشین نشان‌دهنده‌ی | باورهای شرکت‌کننده درباره‌ی جهان | دانش دانشمند درباره‌ی پارامترها |
| می‌تواند غلط باشد اگر… | آدم‌ها بهینه نباشند | مدل یا پیشین‌ها بد انتخاب شده باشند |
| نمونه‌ها در این درس | ترکیب نشانه‌ها (امروز) | هفته‌های 9–13 |

</div>

You can analyze a Bayesian model of cognition with maximum likelihood, and a non-Bayesian model (e.g., Q-learning) with Bayesian data analysis.

<div dir="rtl">

می‌توانید یک مدل بیزی شناخت را با بیشینه‌ی درست‌نمایی تحلیل کنید، و یک مدل غیربیزی (مثلاً Q-learning) را با تحلیل داده‌ی بیزی.

</div>

#### Reading the math · خواندن ریاضی

- $w_V = \dfrac{1/\sigma_V^2}{1/\sigma_V^2 + 1/\sigma_H^2}$: the weight of vision is its precision (1/variance) divided by the total precision. A sense twice as precise (half the SD, a quarter of the variance) gets four times the weight.
- $\sigma_{VH} = \sqrt{\sigma_V^2\sigma_H^2/(\sigma_V^2 + \sigma_H^2)}$: the combined SD, always smaller than the better single sense. **Example:** $\sigma_V = 1$, $\sigma_H = 2$: $w_V = 1/(1 + 1/4) = 0.8$ and $\sigma_{VH} = \sqrt{4/5} = 0.894$, about 11% better than vision alone.
- **The test:** measure $\sigma_V$ and $\sigma_H$ separately (one sense at a time), predict $w_V$ and $\sigma_{VH}$ with no free parameters, then check the two-sense data.

<div dir="rtl">

- $w_V = \dfrac{1/\sigma_V^2}{1/\sigma_V^2 + 1/\sigma_H^2}$: وزن بینایی برابر دقت آن (1/واریانس) تقسیم بر دقت کل است. حسی که دو برابر دقیق‌تر باشد (نصف انحراف معیار، یک‌چهارم واریانس) چهار برابر وزن می‌گیرد.
- $\sigma_{VH} = \sqrt{\sigma_V^2\sigma_H^2/(\sigma_V^2 + \sigma_H^2)}$: انحراف معیار ترکیبی که همیشه از بهترین حس تنها کوچک‌تر است. **مثال:** $\sigma_V = 1$ و $\sigma_H = 2$: $w_V = 1/(1 + 1/4) = 0.8$ و $\sigma_{VH} = \sqrt{4/5} = 0.894$، حدود 11% بهتر از بینایی به‌تنهایی.
- **آزمون:** $\sigma_V$ و $\sigma_H$ را جداگانه اندازه بگیر (هر بار یک حس)، $w_V$ و $\sigma_{VH}$ را بدون هیچ پارامتر آزادی پیش‌بینی کن، و بعد داده‌ی دوحسی را بررسی کن.

</div>

#### For an engineer · برای یک مهندس

- **The delta rule is the LMS update.** $Q \leftarrow Q + \alpha(r - Q)$ is a one-tap LMS (or an exponentially weighted moving average with forgetting factor $1-\alpha$): large $\alpha$ tracks changes quickly but is noisy, small $\alpha$ is smooth but slow, the familiar tracking–misadjustment trade-off.
- **Softmax** is the Boltzmann/Gibbs distribution; $\beta$ is an inverse temperature in the physical sense. Sampling with a temperature is also how language models generate text (Week 1 AI box).
- **Fitting $\alpha$ and $\beta$ from choices** is system identification of an adaptive system from its binary outputs only: you never observe $Q$, only the decisions it produces. That is why $\alpha$ and $\beta$ trade off and why recovery checks are essential.
- **Optimal cue combination** uses exactly the inverse-variance weights of **maximal-ratio combining** and of sensor fusion in a Kalman filter: the combined estimate has variance $(1/\sigma_V^2 + 1/\sigma_H^2)^{-1}$. The scientific question is whether the *brain* implements this fusion.

<div dir="rtl">

- **قاعده‌ی دلتا همان به‌روزرسانی LMS است.** $Q \leftarrow Q + \alpha(r - Q)$ یک LMS تک‌ضریبی است (یا یک میانگین متحرک با وزن نمایی و ضریب فراموشی $1-\alpha$): $\alpha$ بزرگ تغییرات را سریع دنبال می‌کند ولی پرنویز است، $\alpha$ کوچک هموار ولی کند است؛ همان trade-off آشنای ردیابی و خطای تنظیم (misadjustment).
- **softmax** همان توزیع Boltzmann/Gibbs است؛ $\beta$ به معنای فیزیکی یک دمای معکوس است. نمونه‌گیری با دما همان روشی است که مدل‌های زبانی متن تولید می‌کنند (کادر هوش مصنوعی هفته‌ی 1).
- **برازش $\alpha$ و $\beta$ از روی انتخاب‌ها** یعنی شناسایی یک سیستم تطبیقی فقط از روی خروجی‌های دودویی آن: هرگز $Q$ را نمی‌بینید، فقط تصمیم‌هایی را که تولید می‌کند. به همین دلیل $\alpha$ و $\beta$ با هم trade-off دارند و بررسی بازیابی ضروری است.
- **ترکیب بهینه‌ی نشانه‌ها** دقیقاً از وزن‌های معکوس واریانس در **ترکیب با نسبت بیشینه (MRC)** و ادغام حسگرها در فیلتر کالمن استفاده می‌کند: واریانس تخمین ترکیبی $(1/\sigma_V^2 + 1/\sigma_H^2)^{-1}$ است. سؤال علمی این است که آیا *مغز* این ادغام را انجام می‌دهد.

</div>

### 4. Cognitive models and artificial intelligence · 4. مدل‌های شناختی و هوش مصنوعی

| Direction | Examples |
|---|---|
| Cognitive science → AI | Neural networks (inspired by neurons and learning rules); reinforcement learning (from animal learning theory); exemplar/prototype ideas in machine-learning classifiers (nearest-neighbor vs. centroid methods) |
| AI → cognitive science | Deep networks as models of visual cortex; RL agents as models of decision making; large language models proposed as models of language processing and of human-like reasoning |
| Shared mathematics | Likelihoods and loss functions; gradient-based optimization (Week 3); Bayesian inference and MCMC; cross-validation and generalization (Week 6) |

<div dir="rtl">

| جهت | نمونه‌ها |
|---|---|
| علوم شناختی ← هوش مصنوعی | شبکه‌های عصبی (الهام‌گرفته از نورون‌ها و قاعده‌های یادگیری)؛ یادگیری تقویتی (از نظریه‌ی یادگیری حیوانی)؛ ایده‌های exemplar/prototype در طبقه‌بندهای یادگیری ماشین (روش‌های نزدیک‌ترین همسایه در برابر مرکزوار) |
| هوش مصنوعی ← علوم شناختی | شبکه‌های عمیق به‌عنوان مدل قشر بینایی؛ عامل‌های RL به‌عنوان مدل تصمیم‌گیری؛ مدل‌های بزرگ زبانی که به‌عنوان مدل پردازش زبان و استدلال انسان‌گونه پیشنهاد می‌شوند |
| ریاضیات مشترک | درست‌نمایی‌ها و تابع‌های زیان؛ بهینه‌سازی مبتنی بر گرادیان (هفته‌ی 3)؛ استنباط بیزی و MCMC؛ cross-validation و تعمیم (هفته‌ی 6) |

</div>

**Evaluating an AI system as a cognitive model** uses exactly the course toolkit:
- Does it predict human data *beyond* fitting it, e.g., new conditions and individual differences (generalization, Week 6)?
- Does it beat simpler, interpretable cognitive models on a fair comparison (Weeks 7, 10)?
- Can we tell from data whether humans and the model use the same mechanism, or only produce similar outputs (model mimicry and recovery, Week 7)?
- Are its parameters or internal states interpretable as psychological constructs (Week 1)?

<div dir="rtl">

**ارزیابی یک سیستم هوش مصنوعی به‌عنوان مدل شناختی** دقیقاً از جعبه‌ابزار درس استفاده می‌کند:
- آیا داده‌ی انسانی را *فراتر* از برازش پیش‌بینی می‌کند، مثلاً شرایط تازه و تفاوت‌های فردی را (تعمیم، هفته‌ی 6)؟
- آیا در یک مقایسه‌ی منصفانه از مدل‌های شناختی ساده‌تر و تفسیرپذیر بهتر است (هفته‌های 7، 10)؟
- آیا می‌توانیم از روی داده بگوییم انسان و مدل از یک سازوکار استفاده می‌کنند، یا فقط خروجی‌های شبیه تولید می‌کنند (تقلید مدل و بازیابی، هفته‌ی 7)؟
- آیا پارامترها یا حالت‌های درونی‌اش به‌عنوان سازه‌های روان‌شناختی تفسیرپذیرند (هفته‌ی 1)؟

</div>

A model with billions of parameters that fits behavior well is not automatically an *explanation*: flexibility, identifiability and interpretability matter as much as fit.

<div dir="rtl">

مدلی با میلیاردها پارامتر که رفتار را خوب برازش می‌کند به‌طور خودکار یک *تبیین* نیست: انعطاف‌پذیری، identifiability و تفسیرپذیری به اندازه‌ی برازش مهم‌اند.

</div>

### 5. Course synthesis · 5. جمع‌بندی درس

Across very different domains (forgetting, detection, categorization, decisions, learning, perception), the workflow has been the same: **formalize → simulate → fit → evaluate → recover → interpret.** The domain changes the model; the logic of modeling stays.

<div dir="rtl">

در حوزه‌های خیلی متفاوت (فراموشی، تشخیص، دسته‌بندی، تصمیم‌گیری، یادگیری، ادراک)، گردش کار یکسان بوده است: **صورت‌بندی ← شبیه‌سازی ← برازش ← ارزیابی ← بازیابی ← تفسیر.** حوزه مدل را عوض می‌کند؛ منطق مدل‌سازی ثابت می‌ماند.

</div>

#### For the instructor · برای مدرس

- **Play the bandit game with the class.** Two "machines" (two students with hidden coins or a random number app, one paying 80% of the time and one 20%), and halfway through secretly swap them. The class experiences exploration, exploitation and reversal before seeing any equation.
- **Do the four Q-learning trials of the worked example on the board** with a table: value before, choice, reward, prediction error, value after. It takes ten minutes and demystifies the code.
- **For cue combination, use your engineering intuition openly**: "combining two noisy sensors" is a natural way to present it, and students from psychology find it illuminating.
- **Keep the AI discussion grounded.** Section 4 can trigger long debates; use the four evaluation questions (generalization, fair comparison, mimicry, interpretability) to keep them focused.
- **Typical questions.**
  - *"Why is $\beta$ hard to estimate?"* Once choices are almost deterministic, increasing $\beta$ further hardly changes the likelihood.
  - *"Is the brain really doing Q-learning?"* It is a good description of many choice data and matches dopamine signals, but more complex models (model-based learning) also have support.
  - *"Do people always combine cues optimally?"* Often close, but not always; the lab participant over-weights touch.

<div dir="rtl">

- **بازی bandit را با کلاس اجرا کنید.** دو «دستگاه» (دو دانشجو با سکه‌ی پنهان یا یک اپلیکیشن عدد تصادفی؛ یکی 80% مواقع پاداش می‌دهد و دیگری 20%)، و در وسط کار مخفیانه جایشان را عوض کنید. کلاس پیش از دیدن هر معادله‌ای کاوش، بهره‌برداری و وارونگی را تجربه می‌کند.
- **چهار trial Q-learning مثال حل‌شده را روی تخته انجام دهید** با یک جدول: ارزش قبل، انتخاب، پاداش، خطای پیش‌بینی، ارزش بعد. ده دقیقه وقت می‌گیرد و کد را رازگشایی می‌کند.
- **برای ترکیب نشانه‌ها آزادانه از شهود مهندسی‌تان استفاده کنید:** «ترکیب دو حسگر پرنویز» راه طبیعی ارائه‌ی آن است و برای دانشجوهای روان‌شناسی روشنگر است.
- **بحث هوش مصنوعی را روی زمین نگه دارید.** بخش 4 می‌تواند بحث‌های طولانی راه بیندازد؛ از چهار سؤال ارزیابی (تعمیم، مقایسه‌ی منصفانه، تقلید، تفسیرپذیری) برای متمرکز نگه داشتن آن استفاده کنید.
- **سؤال‌های رایج.**
  - *«چرا برآورد $\beta$ سخت است؟»* وقتی انتخاب‌ها تقریباً قطعی شدند، بیشتر کردن $\beta$ درست‌نمایی را تقریباً تغییر نمی‌دهد.
  - *«آیا مغز واقعاً Q-learning انجام می‌دهد؟»* توصیف خوبی از بسیاری از داده‌های انتخاب است و با سیگنال‌های دوپامین جور درمی‌آید، ولی مدل‌های پیچیده‌تر (یادگیری مبتنی بر مدل یا model-based) هم پشتیبانی دارند.
  - *«آیا آدم‌ها همیشه نشانه‌ها را بهینه ترکیب می‌کنند؟»* اغلب نزدیک، ولی نه همیشه؛ شرکت‌کننده‌ی lab به لامسه بیش از حد وزن می‌دهد.

</div>

---

## Worked example · مثال حل‌شده

### Part 1: four trials of Q-learning by hand · بخش 1: چهار trial Q-learning با دست

Two options; $\alpha = 0.5$, $\beta = 3$; initial values $Q(1) = Q(2) = 0.5$.

<div dir="rtl">

دو گزینه؛ $\alpha = 0.5$، $\beta = 3$؛ ارزش‌های اولیه $Q(1) = Q(2) = 0.5$.

</div>

| Trial | $Q(1)$ | $Q(2)$ | $P(\text{choose } 1)$ | Choice | Reward | $\delta$ | Update |
|---|---|---|---|---|---|---|---|
| 1 | 0.50 | 0.50 | 0.500 | 1 | 1 | $1 - 0.5 = +0.5$ | $Q(1) = 0.5 + 0.5 \times 0.5 = 0.75$ |
| 2 | 0.75 | 0.50 | $1/(1 + e^{-3 \times 0.25}) = 0.679$ | 1 | 0 | $0 - 0.75 = -0.75$ | $Q(1) = 0.75 - 0.375 = 0.375$ |
| 3 | 0.375 | 0.50 | $1/(1 + e^{-3 \times (-0.125)}) = 0.407$ | 2 | 1 | $1 - 0.5 = +0.5$ | $Q(2) = 0.75$ |
| 4 | 0.375 | 0.75 | $1/(1 + e^{-3 \times (-0.375)}) = 0.245$ | 2 | 1 | $+0.25$ | $Q(2) = 0.875$ |

<div dir="rtl">

| trial | $Q(1)$ | $Q(2)$ | $P(\text{choose } 1)$ | انتخاب | پاداش | $\delta$ | به‌روزرسانی |
|---|---|---|---|---|---|---|---|
| 1 | 0.50 | 0.50 | 0.500 | 1 | 1 | $1 - 0.5 = +0.5$ | $Q(1) = 0.5 + 0.5 \times 0.5 = 0.75$ |
| 2 | 0.75 | 0.50 | $1/(1 + e^{-3 \times 0.25}) = 0.679$ | 1 | 0 | $0 - 0.75 = -0.75$ | $Q(1) = 0.75 - 0.375 = 0.375$ |
| 3 | 0.375 | 0.50 | $1/(1 + e^{-3 \times (-0.125)}) = 0.407$ | 2 | 1 | $1 - 0.5 = +0.5$ | $Q(2) = 0.75$ |
| 4 | 0.375 | 0.75 | $1/(1 + e^{-3 \times (-0.375)}) = 0.245$ | 2 | 1 | $+0.25$ | $Q(2) = 0.875$ |

</div>

**Log-likelihood of these four choices:** $\ln 0.5 + \ln 0.679 + \ln(1 - 0.407) + \ln(1 - 0.245) = -0.693 - 0.387 - 0.523 - 0.281 = -1.884$.

<div dir="rtl">

**لگاریتم درست‌نمایی این چهار انتخاب:** $\ln 0.5 + \ln 0.679 + \ln(1 - 0.407) + \ln(1 - 0.245) = -0.693 - 0.387 - 0.523 - 0.281 = -1.884$.

</div>

**Interpretation.** With $\alpha = 0.5$ a single non-reward halves the value of option 1, and the model predicts a switch, which the participant made. The likelihood rewards parameter values that predict the participant's actual choice sequence.

<div dir="rtl">

**تفسیر.** با $\alpha = 0.5$ یک بار بی‌پاداشی ارزش گزینه‌ی 1 را نصف می‌کند و مدل یک تغییر انتخاب پیش‌بینی می‌کند، که شرکت‌کننده انجامش داد. درست‌نمایی به مقادیر پارامتری پاداش می‌دهد که دنباله‌ی انتخاب واقعی شرکت‌کننده را پیش‌بینی کنند.

</div>

### Part 2: an ideal observer · بخش 2: یک مشاهده‌گر ایده‌آل

Visual SD $\sigma_V = 1$ mm, haptic SD $\sigma_H = 2$ mm. Weights: $w_V = 1/(1 + 1/4) = 0.8$, $w_H = 0.2$. Predicted combined SD: $\sqrt{(1 \times 4)/(1 + 4)} = 0.894$ mm, about 11% better than vision alone. If $x_V = 50$ and $x_H = 54$ mm, the optimal estimate is $0.8 \times 50 + 0.2 \times 54 = 50.8$ mm.

<div dir="rtl">

انحراف معیار بینایی $\sigma_V = 1$ mm، انحراف معیار لامسه $\sigma_H = 2$ mm. وزن‌ها: $w_V = 1/(1 + 1/4) = 0.8$، $w_H = 0.2$. انحراف معیار ترکیبی پیش‌بینی‌شده: $\sqrt{(1 \times 4)/(1 + 4)} = 0.894$ mm، حدود 11% بهتر از بینایی به تنهایی. اگر $x_V = 50$ و $x_H = 54$ mm باشد، برآورد بهینه $0.8 \times 50 + 0.2 \times 54 = 50.8$ mm است.

</div>

**Interpretation.** An observer who simply *averaged* the cues ($w = 0.5$) would have SD $\sqrt{0.25 \times 1 + 0.25 \times 4} = 1.118$ mm, *worse* than vision alone. Optimal weighting is what makes combining cues worthwhile.

<div dir="rtl">

**تفسیر.** مشاهده‌گری که نشانه‌ها را فقط *میانگین* بگیرد ($w = 0.5$) انحراف معیار $\sqrt{0.25 \times 1 + 0.25 \times 4} = 1.118$ mm دارد، یعنی *بدتر* از بینایی به تنهایی. وزن‌دهی بهینه است که ترکیب نشانه‌ها را ارزشمند می‌کند.

</div>

---

## Lab (2 hours) · lab (2 ساعت)

### Goals · اهداف

1. Simulate a Q-learning agent in a reversal bandit task.
2. Fit $(\alpha, \beta)$ by MLE; run parameter recovery and diagnose the $\alpha$–$\beta$ trade-off.
3. Compare Q-learning with win-stay/lose-shift and biased-random models.
4. Test whether a simulated observer combines cues optimally.

<div dir="rtl">

1. شبیه‌سازی یک عامل Q-learning در یک تکلیف bandit با وارونگی.
2. برازش $(\alpha, \beta)$ با MLE؛ اجرای بازیابی پارامتر و تشخیص trade-off $\alpha$–$\beta$.
3. مقایسه‌ی Q-learning با مدل‌های win-stay/lose-shift و تصادفی سوگیر.
4. آزمودن اینکه آیا یک مشاهده‌گر شبیه‌سازی‌شده نشانه‌ها را بهینه ترکیب می‌کند.

</div>

**Timing:** Part A 20 min · Part B 20 min · Part C 25 min · Part D 30 min · Part E 25 min.

<div dir="rtl">

**زمان‌بندی:** بخش A 20 دقیقه · بخش B 20 دقیقه · بخش C 25 دقیقه · بخش D 30 دقیقه · بخش E 25 دقیقه.

</div>

### Part A: a Q-learning agent in a reversal task (20 min) · بخش A: یک عامل Q-learning در تکلیف وارونگی (20 دقیقه)

> **Code · کد:** [`code/week15.py`](code/week15.py), cell 1 · سلول 1

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Total reward: 151 / 200;  chose the better option on 91% of trials
```

### Part B: the likelihood and an MLE fit (20 min) · بخش B: درست‌نمایی و یک برازش MLE (20 دقیقه)

> **Code · کد:** [`code/week15.py`](code/week15.py), cell 2 · سلول 2

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
MLE: alpha = 0.491 (true 0.3), beta = 3.80 (true 5.0), NLL = 51.77
Chance-level NLL (always p = 0.5): 138.63
```

### Part C: parameter recovery and the α–β trade-off (25 min) · بخش C: بازیابی پارامتر و trade-off α–β (25 دقیقه)

> **Code · کد:** [`code/week15.py`](code/week15.py), cell 3 · سلول 3

**Expected output** (about 30–60 s):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 30–60 ثانیه):

</div>

```text
alpha: r(true, recovered) = 0.90
beta: r(true, recovered) = 0.17
corr(recovered alpha, recovered beta) = 0.31 (true values were drawn independently: 0.03)
```

**Interpret:** with 200 trials and one reversal, $\alpha$ is recovered well (r = 0.90) but $\beta$ hardly at all (r = 0.17). This also explains the Part B fit ($\hat\beta = 3.8$ for a true 5.0). Look at the large-$\beta$ region of the $\beta$ panel. Why are high inverse temperatures hard to pin down? (Hint: once choices are almost deterministic, increasing $\beta$ further barely changes the likelihood.) The recovered $\alpha$ and $\beta$ are also correlated (0.31) although the true values were independent: a trade-off. What does this imply for a study that correlates $\beta$ with, say, a clinical questionnaire?

<div dir="rtl">

**تفسیر کنید:** با 200 trial و یک وارونگی، $\alpha$ خوب بازیابی می‌شود (r = 0.90) ولی $\beta$ تقریباً اصلاً نه (r = 0.17). این برازش بخش B را هم توضیح می‌دهد ($\hat\beta = 3.8$ برای مقدار واقعی 5.0). به ناحیه‌ی $\beta$ بزرگ در نمودار $\beta$ نگاه کنید. چرا دماهای معکوس بالا را به سختی می‌شود تعیین کرد؟ (راهنمایی: وقتی انتخاب‌ها تقریباً قطعی شدند، بالاتر بردن $\beta$ درست‌نمایی را به‌زحمت تغییر می‌دهد.) $\alpha$ و $\beta$ بازیابی‌شده هم همبسته‌اند (0.31) با اینکه مقادیر واقعی مستقل بودند: یک معاوضه. این برای مطالعه‌ای که $\beta$ را با مثلاً یک پرسش‌نامه‌ی بالینی همبسته می‌کند چه معنایی دارد؟

</div>

### Part D: is it really reinforcement learning? Model comparison (30 min) · بخش D: آیا واقعاً یادگیری تقویتی است؟ مقایسه‌ی مدل (30 دقیقه)

> **Code · کد:** [`code/week15.py`](code/week15.py), cell 4 · سلول 4

**Expected output** (about 1 minute):

<div dir="rtl">

**خروجی مورد انتظار** (حدود 1 دقیقه):

</div>

```text
AIC for the Part A participant: {'Q-learning': 107.5, 'WSLS': 200.3, 'bias': 278.9}

Model recovery (rows: generating, columns: selected by AIC):
            Q-learning  WSLS  bias
Q-learning          20     0     0
WSLS                 0    20     0
```

### Part E: an ideal observer for cue combination (25 min) · بخش E: یک مشاهده‌گر ایده‌آل برای ترکیب نشانه‌ها (25 دقیقه)

A simulated participant judges the size of objects seen and felt simultaneously. We know the single-cue noise levels from unimodal blocks. Does the participant combine the cues optimally?

<div dir="rtl">

یک شرکت‌کننده‌ی شبیه‌سازی‌شده اندازه‌ی اشیایی را که هم‌زمان دیده و لمس می‌شوند قضاوت می‌کند. سطح نویز تک‌نشانه را از بلوک‌های تک‌حسی می‌دانیم. آیا شرکت‌کننده نشانه‌ها را بهینه ترکیب می‌کند؟

</div>

> **Code · کد:** [`code/week15.py`](code/week15.py), cell 5 · سلول 5

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
Ideal observer: w_V = 0.80, predicted bimodal SD = 0.894 mm
Participant: empirical w_V = 0.56, bimodal SD = 1.006 mm
Best single cue SD = 1.000 mm;  simple average would give 1.118 mm
```

**Interpret:** is this participant optimal? The empirical visual weight (0.56) is well below the optimal 0.80: the participant over-weights the less reliable haptic cue. As a result, their bimodal SD (1.006 mm) is no better than vision alone (1.000 mm), instead of the 0.894 mm an ideal observer would achieve. Note that the ideal-observer prediction had **no free parameters**: that is what makes this a strong test.

<div dir="rtl">

**تفسیر کنید:** آیا این شرکت‌کننده بهینه است؟ وزن بینایی تجربی (0.56) خیلی پایین‌تر از مقدار بهینه‌ی 0.80 است: شرکت‌کننده به نشانه‌ی لامسه‌ای کم‌پایاتر بیش از حد وزن می‌دهد. در نتیجه انحراف معیار دوحسی‌اش (1.006 mm) بهتر از بینایی به تنهایی (1.000 mm) نیست، به جای 0.894 mm که یک مشاهده‌گر ایده‌آل به آن می‌رسید. توجه کنید که پیش‌بینی مشاهده‌گر ایده‌آل **هیچ پارامتر آزادی** نداشت: همین آن را یک آزمون قوی می‌کند.

</div>

(We simulated this participant with a true weight of 0.65. The estimate 0.56 is off by about 3 standard errors, an unusually unlucky sample but a useful reminder that empirical weights also have sampling error. Exercise 4 puts bootstrap intervals around them.)

<div dir="rtl">

(این شرکت‌کننده را با وزن واقعی 0.65 شبیه‌سازی کردیم. برآورد 0.56 حدود 3 خطای استاندارد فاصله دارد، یک نمونه‌ی غیرمعمول بدشانس ولی یادآوری مفید که وزن‌های تجربی هم خطای نمونه‌گیری دارند. تمرین 4 بازه‌های bootstrap دورشان می‌گذارد.)

</div>

### Exercises (increasing difficulty) · تمرین‌ها (به ترتیب سختی)

**Exercise 1 ★.** Reproduce the worked example's four Q-learning trials with `nll_q` (hint: compute the NLL with `theta = (logit 0.5, log 3)` on the four-trial sequence). Do you get −1.884 for the log-likelihood?

<div dir="rtl">

**تمرین 1 ★.** چهار trial Q-learning مثال حل‌شده را با `nll_q` بازتولید کنید (راهنمایی: NLL را با `theta = (logit 0.5, log 3)` روی دنباله‌ی چهار trialی حساب کنید). آیا لگاریتم درست‌نمایی −1.884 به دست می‌آید؟

</div>

**Exercise 2 ★.** Rerun Part C with 50 trials (no reversal) and with 400 trials (three reversals). How does recovery of $\alpha$ change? What does this imply for experimental design?

<div dir="rtl">

**تمرین 2 ★.** بخش C را با 50 trial (بدون وارونگی) و با 400 trial (سه وارونگی) دوباره اجرا کنید. بازیابی $\alpha$ چطور تغییر می‌کند؟ این برای طراحی آزمایش چه معنایی دارد؟

</div>

**Exercise 3 ★★ (two learning rates).** Many studies find different learning rates for positive and negative prediction errors. Implement a model with $\alpha^{+}$ and $\alpha^{-}$, simulate an agent with $\alpha^{+} = 0.4$, $\alpha^{-} = 0.1$, and test with AIC/BIC and a recovery study whether the extra parameter is identifiable at the Part A design.

<div dir="rtl">

**تمرین 3 ★★ (دو نرخ یادگیری).** بسیاری از مطالعه‌ها نرخ‌های یادگیری متفاوتی برای خطاهای پیش‌بینی مثبت و منفی پیدا می‌کنند. مدلی با $\alpha^{+}$ و $\alpha^{-}$ پیاده‌سازی کنید، یک عامل با $\alpha^{+} = 0.4$ و $\alpha^{-} = 0.1$ شبیه‌سازی کنید، و با AIC/BIC و یک مطالعه‌ی بازیابی بیازمایید که آیا پارامتر اضافه در طرح بخش A identifiable است.

</div>

**Exercise 4 ★★ (optimal weights).** In Part E, simulate an observer with $w_V = 0.8$ (optimal) and one with $w_V = 0.5$ (averaging), 100 bimodal trials each. Use a bootstrap (Week 5) to put confidence intervals around the empirical weights and SDs. With 100 trials, can you distinguish the two observers?

<div dir="rtl">

**تمرین 4 ★★ (وزن‌های بهینه).** در بخش E، یک مشاهده‌گر با $w_V = 0.8$ (بهینه) و یکی با $w_V = 0.5$ (میانگین‌گیر)، هرکدام با 100 trial دوحسی، شبیه‌سازی کنید. با bootstrap (هفته‌ی 5) دور وزن‌ها و انحراف معیارهای تجربی بازه‌ی اطمینان بگذارید. با 100 trial می‌توانید دو مشاهده‌گر را از هم تشخیص دهید؟

</div>

**Exercise 5 ★★★ (Advanced: hierarchical RL).** Simulate 20 agents with individual $(\alpha_j, \beta_j)$ and only 80 trials each. Fit them individually by MLE, and then with a hierarchical Bayesian model in PyMC. (Hint: the trial loop can be written with `pytensor.scan`; alternatively, implement a hand-written Metropolis-within-Gibbs sampler using `nll_q` for the individual parameters and conjugate updates for the group means.) Compare recovery of $\alpha_j$ between the two approaches.

<div dir="rtl">

**تمرین 5 ★★★ (پیشرفته: RL سلسله‌مراتبی).** 20 عامل با $(\alpha_j, \beta_j)$ فردی و فقط 80 trial برای هرکدام شبیه‌سازی کنید. آن‌ها را جداگانه با MLE و بعد با یک مدل بیزی سلسله‌مراتبی در PyMC برازش کنید. (راهنمایی: حلقه‌ی trialها را می‌شود با `pytensor.scan` نوشت؛ یا به جایش یک نمونه‌گیر Metropolis-within-Gibbs دست‌نویس پیاده کنید که از `nll_q` برای پارامترهای فردی و به‌روزرسانی‌های conjugate برای میانگین‌های گروه استفاده کند.) بازیابی $\alpha_j$ را بین دو رویکرد مقایسه کنید.

</div>

### Lab check-off · lab check-off

Show: (1) the MLE fit and the recovery plots with your interpretation of the $\beta$ panel, (2) the model-recovery table, and (3) your answer on the optimality of the cue-combination observer.

<div dir="rtl">

نشان دهید: (1) برازش MLE و نمودارهای بازیابی همراه با تفسیرتان از نمودار $\beta$، (2) جدول بازیابی مدل، و (3) جوابتان درباره‌ی بهینه بودن مشاهده‌گر ترکیب نشانه‌ها.

</div>

---

## Connection to AI & LLMs · ارتباط با هوش مصنوعی و LLMها

**The choice rule behind chatbot training.** Modern chatbots are fine-tuned with *reinforcement learning from human feedback* (RLHF). People see two responses and say which they prefer, a **reward model** is fitted to these choices, and the chatbot is then trained by reinforcement learning to maximize the learned reward (Christiano et al., 2017; Ouyang et al., 2022). The reward model is usually the **Bradley–Terry** model, $P(i \succ j) = 1/(1 + e^{-(r_i - r_j)})$. This is the softmax choice rule of this week with $\beta = 1$, and the Luce choice rule of the GCM. Fitting it is an MLE problem from Week 4. So human choice models sit at the heart of how today's AI systems are aligned with human preferences, and so do their problems: noisy choices, identifiability (only *differences* in $r$ matter, so one value is fixed), and the gap between what people choose and what is actually good.

<div dir="rtl">

**قاعده‌ی انتخاب پشت آموزش chatbotها.** chatbotهای امروزی با *یادگیری تقویتی از بازخورد انسانی* (RLHF) تنظیم دقیق (fine-tune) می‌شوند. آدم‌ها دو پاسخ را می‌بینند و می‌گویند کدام را ترجیح می‌دهند، یک **مدل پاداش** (reward model) روی این انتخاب‌ها برازش می‌شود، و بعد chatbot با یادگیری تقویتی آموزش می‌بیند تا پاداش یادگرفته‌شده را بیشینه کند (Christiano et al., 2017; Ouyang et al., 2022). مدل پاداش معمولاً مدل **Bradley–Terry** است، $P(i \succ j) = 1/(1 + e^{-(r_i - r_j)})$. این همان قاعده‌ی انتخاب softmax این هفته با $\beta = 1$، و قاعده‌ی انتخاب Luce در GCM است. برازش آن یک مسئله‌ی MLE از هفته‌ی 4 است. پس مدل‌های انتخاب انسانی در قلب شیوه‌ای قرار دارند که سیستم‌های هوش مصنوعی امروزی با ترجیحات انسانی همسو (align) می‌شوند، و مشکلاتشان هم همین‌جاست: انتخاب‌های پرنویز، identifiability (فقط *تفاوت*‌های $r$ مهم‌اند، پس یک مقدار ثابت می‌شود)، و فاصله‌ی بین آنچه آدم‌ها انتخاب می‌کنند و آنچه واقعاً خوب است.

</div>

> **Code · کد:** [`code/week15.py`](code/week15.py), cell 6 · سلول 6

**Expected output:**

<div dir="rtl">

**خروجی مورد انتظار:**

</div>

```text
304 comparisons; estimated rewards = [0.   0.56 0.5  1.61] (true [0.  0.5 1.  2. ])
```

With about 300 noisy comparisons, the estimated order of responses 1 and 2 is even reversed. A reward model is a fitted cognitive model, and it needs uncertainty estimates and recovery checks like any other.

<div dir="rtl">

با حدود 300 مقایسه‌ی پرنویز، ترتیب برآوردشده‌ی پاسخ‌های 1 و 2 حتی برعکس شده. یک مدل پاداش یک مدل شناختی برازش‌شده است، و مثل هر مدل دیگری به برآورد عدم قطعیت و بررسی بازیابی نیاز دارد.

</div>

**Try it (no API needed).**
- ★ Compute Hessian-based standard errors for the three estimates (Week 5). Is the reversal of responses 1 and 2 within the uncertainty?
- ★★ Run a parameter recovery: how many comparisons are needed before the order of all four responses is recovered correctly in 90% of simulated datasets?
- ★★ Simulate raters who prefer *longer* answers regardless of quality (add a length bonus to the true reward). What does the fitted reward model learn, and what will the chatbot then be trained to do?

<div dir="rtl">

**امتحانش کنید (بدون نیاز به API).**
- ★ خطاهای استاندارد مبتنی بر Hessian را برای سه برآورد حساب کنید (هفته‌ی 5). آیا برعکس شدن پاسخ‌های 1 و 2 در محدوده‌ی عدم قطعیت است؟
- ★★ یک بازیابی پارامتر اجرا کنید: چند مقایسه لازم است تا ترتیب هر چهار پاسخ در 90% مجموعه داده‌های شبیه‌سازی‌شده درست بازیابی شود؟
- ★★ ارزیاب‌هایی را شبیه‌سازی کنید که جواب‌های *طولانی‌تر* را صرف‌نظر از کیفیت ترجیح می‌دهند (یک پاداش طول به پاداش واقعی اضافه کنید). مدل پاداش برازش‌شده چه یاد می‌گیرد، و بعد chatbot برای انجام چه کاری آموزش می‌بیند؟

</div>

*Optional reading:* Christiano, P. F., et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS*. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS*.

<div dir="rtl">

*مطالعه‌ی اختیاری:* Christiano, P. F., et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS*. Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS*.

</div>

---

## Common mistakes & misconceptions · اشتباهات رایج و برداشت‌های نادرست

1. **Fitting a learning model to aggregated choice proportions.** The likelihood must follow each participant's own trial sequence, because values depend on their own history.
2. **Interpreting $\alpha$ without a recovery check.** $\alpha$ and $\beta$ trade off, and $\alpha$ is poorly identified without reversals or enough trials.
3. **Not comparing with simple strategies.** Win-stay/lose-shift or perseveration can mimic learning. Show that the RL model wins a fair comparison.
4. **Forgetting that the softmax uses value *differences*.** Adding a constant to all Q-values changes nothing, while the scale of the values and $\beta$ trade off.
5. **"People are Bayesian" from a post-hoc fit.** If the prior and likelihood were chosen to fit the behavior, optimality is assumed, not tested. Strong tests fix them independently (cue combination).
6. **Confusing the two Bayesianisms** (model of the mind vs. method of analysis).
7. **"A large AI model that fits human data is a good cognitive model."** Fit is not explanation. Ask about generalization, mimicry, identifiability and interpretability, as for any model.

<div dir="rtl">

1. **برازش یک مدل یادگیری روی نسبت‌های انتخاب تجمیع‌شده.** درست‌نمایی باید دنباله‌ی trialهای خود هر شرکت‌کننده را دنبال کند، چون ارزش‌ها به تاریخچه‌ی خودش بستگی دارند.
2. **تفسیر $\alpha$ بدون بررسی بازیابی.** $\alpha$ و $\beta$ با هم trade-off دارند، و $\alpha$ بدون وارونگی یا trial کافی بد شناسایی می‌شود.
3. **مقایسه نکردن با راهبردهای ساده.** win-stay/lose-shift یا پافشاری (perseveration) می‌توانند یادگیری را تقلید کنند. نشان دهید مدل RL در یک مقایسه‌ی منصفانه برنده است.
4. **فراموش کردن اینکه softmax از *تفاوت* ارزش‌ها استفاده می‌کند.** افزودن یک ثابت به همه‌ی ارزش‌های Q چیزی را عوض نمی‌کند، در حالی که مقیاس ارزش‌ها و $\beta$ با هم trade-off دارند.
5. **«آدم‌ها بیزی‌اند» از روی یک برازش پس‌از-واقعه.** اگر پیشین و درست‌نمایی برای برازش رفتار انتخاب شده باشند، بهینگی فرض شده، نه آزموده. آزمون‌های قوی آن‌ها را مستقل تثبیت می‌کنند (ترکیب نشانه‌ها).
6. **قاطی کردن دو نوع بیزی‌گرایی** (مدل ذهن در برابر روش تحلیل).
7. **«یک مدل بزرگ هوش مصنوعی که داده‌ی انسانی را برازش می‌کند، مدل شناختی خوبی است.»** برازش تبیین نیست. مثل هر مدل دیگری درباره‌ی تعمیم، تقلید، identifiability و تفسیرپذیری بپرسید.

</div>

---

## Check your understanding · خودآزمایی

**1.** Write the delta-rule update and explain the role of the prediction error.
<details><summary>Answer</summary>
$Q \leftarrow Q + \alpha(r - Q)$. The prediction error $r - Q$ is the difference between outcome and expectation: positive errors raise the value, negative errors lower it, and the learning rate scales the change.
</details>

<div dir="rtl">

**1.** به‌روزرسانی قاعده‌ی دلتا را بنویسید و نقش خطای پیش‌بینی را توضیح دهید.
<details><summary>پاسخ</summary>
$Q \leftarrow Q + \alpha(r - Q)$. خطای پیش‌بینی $r - Q$ تفاوت پیامد و انتظار است: خطاهای مثبت ارزش را بالا می‌برند، خطاهای منفی پایین می‌آورند، و نرخ یادگیری اندازه‌ی تغییر را تعیین می‌کند.
</details>

</div>

**2.** What does the inverse temperature $\beta$ control? What behavior do $\beta = 0$ and $\beta \to \infty$ produce?
<details><summary>Answer</summary>
The sensitivity of choices to value differences (exploration vs. exploitation). $\beta = 0$: random choice regardless of values. $\beta \to \infty$: always choose the option with the highest current value.
</details>

<div dir="rtl">

**2.** inverse temperature $\beta$ چه چیزی را کنترل می‌کند؟ $\beta = 0$ و $\beta \to \infty$ چه رفتاری تولید می‌کنند؟
<details><summary>پاسخ</summary>
حساسیت انتخاب‌ها به تفاوت ارزش‌ها (کاوش در برابر بهره‌برداری). $\beta = 0$: انتخاب تصادفی بدون توجه به ارزش‌ها. $\beta \to \infty$: همیشه گزینه‌ای با بالاترین ارزش فعلی انتخاب می‌شود.
</details>

</div>

**3.** Why must a learning model's likelihood be computed trial by trial on each participant's actual sequence?
<details><summary>Answer</summary>
The model's predictions on trial $t$ depend on that participant's own previous choices and rewards (through the Q-values), so the probability of each observed choice can only be computed by running the model through the observed history.
</details>

<div dir="rtl">

**3.** چرا درست‌نمایی یک مدل یادگیری باید trial به trial روی دنباله‌ی واقعی هر شرکت‌کننده حساب شود؟
<details><summary>پاسخ</summary>
پیش‌بینی‌های مدل در trial $t$ به انتخاب‌ها و پاداش‌های قبلی خود آن شرکت‌کننده (از طریق ارزش‌های Q) بستگی دارد، پس احتمال هر انتخاب مشاهده‌شده را فقط با اجرای مدل روی تاریخچه‌ی مشاهده‌شده می‌شود حساب کرد.
</details>

</div>

**4.** Explain the $\alpha$–$\beta$ trade-off.
<details><summary>Answer</summary>
Different combinations of learning rate and choice noise can produce similar choice sequences. For example, sluggish adaptation can come from slow learning (low $\alpha$) or from noisy, value-insensitive choice (low $\beta$). The estimates are therefore correlated and individually uncertain; the direction of the correlation depends on the design. In addition, high $\beta$ values are weakly identified because near-deterministic choices look the same for many large $\beta$.
</details>

<div dir="rtl">

**4.** trade-off $\alpha$–$\beta$ را توضیح دهید.
<details><summary>پاسخ</summary>
ترکیب‌های مختلف نرخ یادگیری و نویز انتخاب می‌توانند دنباله‌های انتخاب مشابهی تولید کنند. مثلاً تطبیق کُند می‌تواند از یادگیری کند ($\alpha$ پایین) یا از انتخاب پرنویز و بی‌حساس به ارزش ($\beta$ پایین) بیاید. پس برآوردها همبسته‌اند و هرکدام به تنهایی نامطمئن؛ جهت همبستگی به طرح بستگی دارد. علاوه بر این، مقادیر بالای $\beta$ ضعیف شناسایی می‌شوند، چون انتخاب‌های تقریباً قطعی برای بسیاری از $\beta$های بزرگ یکسان به نظر می‌رسند.
</details>

</div>

**5.** Vision has SD 2 and touch SD 2. What are the optimal weights and the predicted combined SD?
<details><summary>Answer</summary>
Equal reliabilities give $w_V = w_H = 0.5$, and the combined SD is $\sqrt{4 \times 4/8} = \sqrt{2} = 1.41$, better than either cue alone (2).
</details>

<div dir="rtl">

**5.** بینایی انحراف معیار 2 و لامسه انحراف معیار 2 دارد. وزن‌های بهینه و انحراف معیار ترکیبی پیش‌بینی‌شده چقدر است؟
<details><summary>پاسخ</summary>
پایایی‌های برابر $w_V = w_H = 0.5$ می‌دهند، و انحراف معیار ترکیبی $\sqrt{4 \times 4/8} = \sqrt{2} = 1.41$ است، بهتر از هر نشانه به تنهایی (2).
</details>

</div>

**6.** Give one example each of an idea that moved from cognitive science to AI and from AI to cognitive science.
<details><summary>Answer</summary>
Cognitive science → AI: error-driven learning (Rescorla–Wagner / delta rule) leading to neural-network training and reinforcement learning. AI → cognitive science: deep convolutional networks used as models of the ventral visual stream, or RL agents and language models proposed as models of human behavior.
</details>

<div dir="rtl">

**6.** برای هرکدام یک نمونه بزنید: ایده‌ای که از علوم شناختی به هوش مصنوعی رفته، و ایده‌ای که از هوش مصنوعی به علوم شناختی آمده.
<details><summary>پاسخ</summary>
علوم شناختی ← هوش مصنوعی: یادگیری خطامحور (Rescorla–Wagner / قاعده‌ی دلتا) که به آموزش شبکه‌های عصبی و یادگیری تقویتی منجر شد. هوش مصنوعی ← علوم شناختی: شبکه‌های کانولوشنی عمیق که به‌عنوان مدل جریان بینایی شکمی (ventral visual stream) استفاده می‌شوند، یا عامل‌های RL و مدل‌های زبانی که به‌عنوان مدل رفتار انسان پیشنهاد می‌شوند.
</details>

</div>

**7.** A researcher shows that a large language model's responses correlate highly with human responses in a reasoning task. What further evidence would you ask for before accepting it as a cognitive model?
<details><summary>Answer</summary>
Prediction of new conditions and of individual differences (generalization); a fair comparison against simpler cognitive models; tests that distinguish the model's mechanism from alternatives that produce the same outputs (mimicry); and some correspondence between its internal states and psychological constructs.
</details>

<div dir="rtl">

**7.** یک پژوهشگر نشان می‌دهد پاسخ‌های یک مدل بزرگ زبانی در یک تکلیف استدلال همبستگی بالایی با پاسخ‌های انسانی دارد. پیش از پذیرفتنش به‌عنوان یک مدل شناختی چه شواهد دیگری می‌خواهید؟
<details><summary>پاسخ</summary>
پیش‌بینی شرایط تازه و تفاوت‌های فردی (تعمیم)؛ یک مقایسه‌ی منصفانه با مدل‌های شناختی ساده‌تر؛ آزمون‌هایی که سازوکار مدل را از جایگزین‌هایی که همان خروجی‌ها را تولید می‌کنند تمیز دهند (تقلید)؛ و نوعی تناظر بین حالت‌های درونی‌اش و سازه‌های روان‌شناختی.
</details>

</div>

---

## Assignment · تکلیف

No new assignment: **final project presentations are next week**, and the written report and code are due before the final exam. Use this week's lab time for project work and the course wrap-up.

<div dir="rtl">

تکلیف جدیدی نداریم: **ارائه‌های پروژه‌ی پایانی هفته‌ی آینده است**، و گزارش کتبی و کد پیش از امتحان پایانی تحویل داده می‌شوند. وقت lab این هفته را برای کار روی پروژه و جمع‌بندی درس استفاده کنید.

</div>

---

## Further reading · مطالعه‌ی بیشتر

- **Verguts (2022)**: the chapters on the delta rule and on reinforcement learning (error-driven learning and its neural basis) [verify chapters]. *(Main reading for Part 1.)*
- **Farrell & Lewandowsky (2018)**: the chapters on neural network models and on models in neuroscience [verify chapter numbers].
- **Anderson (2014)**: the chapters on neural networks and learning, which connect cognitive and computational neuroscience models [verify chapters].
- *Optional, outside the course list:* Ernst, M. O., & Banks, M. S. (2002). Humans integrate visual and haptic information in a statistically optimal fashion. *Nature, 415*, 429–433. Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, e49547 (its running example is a bandit task like today's).

<div dir="rtl">

- **Verguts (2022)**: فصل‌های قاعده‌ی دلتا و یادگیری تقویتی (یادگیری خطامحور و پایه‌ی عصبی‌اش) [فصل‌ها بررسی شود]. *(منبع اصلی برای بخش 1.)*
- **Farrell & Lewandowsky (2018)**: فصل‌های مدل‌های شبکه‌ی عصبی و مدل‌ها در علوم اعصاب [شماره‌ی فصل‌ها بررسی شود].
- **Anderson (2014)**: فصل‌های شبکه‌های عصبی و یادگیری، که مدل‌های شناختی و علوم اعصاب محاسباتی را به هم وصل می‌کنند [فصل‌ها بررسی شود].
- *اختیاری، خارج از فهرست درس:* Ernst, M. O., & Banks, M. S. (2002). Humans integrate visual and haptic information in a statistically optimal fashion. *Nature, 415*, 429–433. Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife, 8*, e49547 (مثال اصلی‌اش یک تکلیف bandit مثل تکلیف امروز است).

</div>

*Preview for Week 16:* final project presentations, and a closing session on good modeling practice.

<div dir="rtl">

*پیش‌نمایش هفته‌ی 16:* ارائه‌های پروژه‌ی پایانی، و یک جلسه‌ی پایانی درباره‌ی شیوه‌ی خوب مدل‌سازی.

</div>
