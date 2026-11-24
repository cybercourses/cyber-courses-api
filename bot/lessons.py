# -*- coding: utf-8 -*-
"""Lesson content for the cybersecurity + programming courses bot.

Defensive cybersecurity only: how to protect yourself, your accounts and
your devices. No hacking instructions, no attack techniques, no exploit
details anywhere in this file.

Each lesson is a dict with a short title and full text in Arabic (plain
spoken Egyptian Arabic, beginner friendly) plus a concise English version.
Every lesson fits in one Telegram message (well under 4096 characters).
"""

DISCLAIMER_AR = "تنويه: الدورات لأغراض تعليمية وحماية نفسك فقط. القناة غير مسؤولة عن أي سوء استخدام للمعلومات."
DISCLAIMER_EN = "Disclaimer: these courses are for education and self-protection only. The channel is not responsible for any misuse of the information."

CYBER_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه أمن سيبراني؟",
        "title_en": "Lesson 1: What is cybersecurity?",
        "ar": (
            "🛡️ الدرس 1: يعني إيه أمن سيبراني؟\n\n"
            "الأمن السيبراني يعني تحمي نفسك على الإنترنت: حساباتك، فلوسك، صورك، وبياناتك.\n\n"
            "الخطر مش بعيد عنك: كل يوم فيه ناس بتتسرق حساباتهم على فيسبوك وواتساب، أو بيتدفعوا فلوس لنصّابين، "
            "أو بيدخلوا على روابط بتسرق بياناتهم — وكل ده بيحصل بسبب غلطات صغيرة ممكن تتجنبها.\n\n"
            "في الدورة دي هنتعلم خطوة بخطوة:\n"
            "1️⃣ كلمات سر قوية\n"
            "2️⃣ التحقق بخطوتين\n"
            "3️⃣ كشف النصب والروابط المزيفة\n"
            "4️⃣ الواي فاي الآمن\n"
            "5️⃣ حماية حساباتك\n"
            "6️⃣ الفيروسات والبرامج الضارة\n"
            "7️⃣ خصوصيتك وبياناتك\n\n"
            "كل درس قصير وعملي. طبّق اللي فيه النهاردة قبل الدرس اللي بعده 👌\n\n"
            "واجب النهاردة: بص على حساباتك — فيه حساب من غير كلمة سر قوية أو تحقق بخطوتين؟ ابدأ بيه النهاردة.\n\n"
            "اكتب /lesson عشان تاخد الدرس اللي بعده."
        ),
        "en": (
            "🛡️ Lesson 1: What is cybersecurity?\n\n"
            "Cybersecurity means protecting yourself online: your accounts, money, photos and data.\n\n"
            "The danger is real: every day people lose Facebook and WhatsApp accounts, pay scammers, "
            "or click links that steal their data — all because of small mistakes you can avoid.\n\n"
            "In this course we will learn step by step:\n"
            "1️⃣ Strong passwords\n"
            "2️⃣ Two-step verification\n"
            "3️⃣ Spotting scams and fake links\n"
            "4️⃣ Safe Wi-Fi\n"
            "5️⃣ Protecting your accounts\n"
            "6️⃣ Viruses and malware\n"
            "7️⃣ Your privacy and data\n\n"
            "Every lesson is short and practical. Apply today's lesson before the next one 👌\n\n"
            "Today's task: look at your accounts — is there one without a strong password or two-factor authentication? Start with it today.\n\n"
            "Send /lesson for the next lesson."
        ),
    },
    {
        "title_ar": "الدرس 2: كلمة السر القوية",
        "title_en": "Lesson 2: Strong passwords",
        "ar": (
            "🔑 الدرس 2: كلمة السر القوية\n\n"
            "كلمة السر هي أول باب بيحمي حسابك. لو الباب ضعيف، أي حد يقدر يدخل.\n\n"
            "✅ كلمة سر قوية يعني:\n"
            "• طويلة: 12 حرف على الأقل\n"
            "• فيها حروف كبيرة وصغيرة وأرقام ورموز (مثال: Ahly@2024#Zamalek!)\n"
            "• مختلفة لكل حساب — كلمة سر فيسبوك غير واتساب غير الإيميل\n\n"
            "❌ إياك تعمل كده:\n"
            "• اسمك أو تاريخ ميلادك أو رقم تليفونك\n"
            "• 123456 أو password\n"
            "• نفس كلمة السر لكل الحسابات (لو اتسرقت واحدة، كل حساباتك تتسرق)\n\n"
            "💡 نصيحة عملية: استخدم برنامج لإدارة كلمات السر (زي Bitwarden المجاني) — هو يحفظها ويعمل لك كلمات قوية، "
            "وانت تحفظ كلمة سر واحدة بس للبرنامج.\n\n"
            "واجب النهاردة: غيّر كلمة سر أهم حساب عندك (الإيميل أو فيسبوك) وخليها قوية ومختلفة 🔐"
        ),
        "en": (
            "🔑 Lesson 2: Strong passwords\n\n"
            "Your password is the first door protecting your account. If the door is weak, anyone can enter.\n\n"
            "✅ A strong password means:\n"
            "• Long: at least 12 characters\n"
            "• Mix of upper/lowercase letters, numbers and symbols\n"
            "• Different for every account\n\n"
            "❌ Never do this:\n"
            "• Your name, birthday or phone number\n"
            "• 123456 or password\n"
            "• The same password for all accounts (if one leaks, all are lost)\n\n"
            "💡 Practical tip: use a free password manager (like Bitwarden) — it stores them and creates strong ones for you, "
            "and you only remember one master password.\n\n"
            "Today's task: change the password of your most important account (email or Facebook) to a strong, unique one 🔐"
        ),
    },
    {
        "title_ar": "الدرس 3: التحقق بخطوتين",
        "title_en": "Lesson 3: Two-step verification (2FA)",
        "ar": (
            "📱 الدرس 3: التحقق بخطوتين (2FA)\n\n"
            "حتى لو حد عرف كلمة السر بتاعتك، التحقق بخطوتين يوقفه عند الباب التاني.\n\n"
            "إزاي يشتغل؟ بعد ما تدخل كلمة السر، التطبيق يطلب منك كود بيتغير كل 30 ثانية من موبايلك. "
            "من غير موبايلك محدش يقدر يدخل حسابك.\n\n"
            "✅ فعّله النهاردة على:\n"
            "• تليجرام: الإعدادات ← الخصوصية والأمان ← التحقق بخطوتين\n"
            "• واتساب: الإعدادات ← الحساب ← التحقق بخطوتين\n"
            "• فيسبوك: الإعدادات ← كلمة السر والأمان ← المصادقة الثنائية\n"
            "• الإيميل (جوجل): الأمان ← التحقق بخطوتين\n\n"
            "💡 استخدم تطبيق مصادقة زي Google Authenticator أو Authy، أحسن من الكود اللي بييجي في رسالة SMS.\n\n"
            "⚠️ مهم جدًا: احفظ أكواد الاسترداد (backup codes) في مكان آمن — لو ضاع موبايلك هتحتاجهم عشان ترجع حسابك.\n\n"
            "واجب النهاردة: فعّل التحقق بخطوتين على تليجرام وواتساب 🔒"
        ),
        "en": (
            "📱 Lesson 3: Two-step verification (2FA)\n\n"
            "Even if someone learns your password, two-step verification stops them at the second door.\n\n"
            "How it works: after your password, the app asks for a code that changes every 30 seconds on your phone. "
            "Without your phone, nobody can enter your account.\n\n"
            "✅ Turn it on today for:\n"
            "• Telegram: Settings → Privacy and Security → Two-Step Verification\n"
            "• WhatsApp: Settings → Account → Two-step verification\n"
            "• Facebook: Settings → Password and security → Two-factor authentication\n"
            "• Google email: Security → 2-Step Verification\n\n"
            "💡 Use an authenticator app like Google Authenticator or Authy — better than SMS codes.\n\n"
            "⚠️ Very important: save your backup codes somewhere safe — if you lose your phone you will need them.\n\n"
            "Today's task: turn on two-step verification for Telegram and WhatsApp 🔒"
        ),
    },
    {
        "title_ar": "الدرس 4: التصيّد والروابط المزيفة",
        "title_en": "Lesson 4: Phishing and fake links",
        "ar": (
            "🎣 الدرس 4: التصيّد والروابط المزيفة\n\n"
            "التصيّد يعني حد يبعت لك رسالة أو رابط شكله حقيقي، بس هو فخ عشان يسرق حسابك أو فلوسك.\n\n"
            "🚩 علامات النصب — لو شفت أي واحدة منها، وقف:\n"
            "• \"مبروك كسبت جايزة!\" أو \"حسابك هيتقفل النهاردة!\" (استعجال وتخويف)\n"
            "• رابط مختصر أو غريب مش زي الموقع الرسمي (مثال: faceb00k-login.com بدل facebook.com)\n"
            "• حد بيطلب منك كلمة السر أو كود التحقق — مفيش شركة حقيقية بتطلب كده أبدًا\n"
            "• رسالة من \"البنك\" أو \"الشركة\" فيها أخطاء إملائية\n\n"
            "✅ قبل ما تدوس على أي رابط:\n"
            "1. بص على عنوان الرابط كويس\n"
            "2. لو الرسالة بتقول إنها من البنك، افتح تطبيق البنك بنفسك مش من الرابط\n"
            "3. اسأل نفسك: أنا كنت مستني الرسالة دي؟\n\n"
            "واجب النهاردة: افتح آخر 3 رسايل مشبوهة وصلتك، وطلّع علامة نصب واحدة في كل واحدة 🎯"
        ),
        "en": (
            "🎣 Lesson 4: Phishing and fake links\n\n"
            "Phishing is when someone sends you a message or link that looks real, but it is a trap to steal your account or money.\n\n"
            "🚩 Scam signs — if you see any of these, stop:\n"
            "• \"Congratulations, you won a prize!\" or \"Your account will be closed today!\" (urgency and fear)\n"
            "• A shortened or strange link, unlike the official site (e.g. faceb00k-login.com instead of facebook.com)\n"
            "• Anyone asking for your password or verification code — no real company ever asks for that\n"
            "• A message from \"the bank\" full of spelling mistakes\n\n"
            "✅ Before clicking any link:\n"
            "1. Look carefully at the link address\n"
            "2. If it claims to be your bank, open the bank app yourself, not from the link\n"
            "3. Ask yourself: was I expecting this message?\n\n"
            "Today's task: open the last 3 suspicious messages you received and find one scam sign in each 🎯"
        ),
    },
    {
        "title_ar": "الدرس 5: الواي فاي العام الآمن",
        "title_en": "Lesson 5: Safe public Wi-Fi",
        "ar": (
            "📶 الدرس 5: الواي فاي العام الآمن\n\n"
            "واي فاي القهوة والمول والمطار مريح — بس هو أخطر مكان ممكن تستخدم فيه الإنترنت.\n\n"
            "⚠️ ليه خطر؟ لأن أي حد على نفس الشبكة ممكن يشوف اللي بتبعته لو الاتصال مش محمي، "
            "وفيه شبكات مزيفة أصلًا باسم القهوة عشان تصطاد بياناتك.\n\n"
            "✅ قواعد الواي فاي العام:\n"
            "• متعملش عمليات بنكية ولا تدخل كلمات سر مهمة على واي فاي عام — استخدم باقة موبايلك\n"
            "• اتأكد إن الموقع بيبدأ بـ https (القفل اللي جنب العنوان)\n"
            "• اقفل خاصية الاتصال التلقائي بالشبكات (auto-connect)\n"
            "• بعد ما تخلص، اعمل \"نسيان الشبكة\" (Forget network)\n"
            "• لو لازم تستخدمه كتير، استخدم VPN موثوق\n\n"
            "💡 شبكة البيت كمان لازم تكون محمية: غيّر كلمة سر الراوتر الافتراضية، وخلي الواي فاي WPA2 أو WPA3.\n\n"
            "واجب النهاردة: اقفل الاتصال التلقائي بالشبكات من موبايلك، وغيّر كلمة سر واي فاي بيتك لو لسه الافتراضية 📡"
        ),
        "en": (
            "📶 Lesson 5: Safe public Wi-Fi\n\n"
            "Café, mall and airport Wi-Fi is convenient — but it is the most dangerous place to use the internet.\n\n"
            "⚠️ Why is it risky? Anyone on the same network can see what you send if the connection is not protected, "
            "and there are fake networks named after the café just to catch your data.\n\n"
            "✅ Public Wi-Fi rules:\n"
            "• No banking and no important passwords on public Wi-Fi — use your mobile data\n"
            "• Make sure the site starts with https (the lock next to the address)\n"
            "• Turn off auto-connect to networks\n"
            "• After you finish, \"Forget\" the network\n"
            "• If you must use it often, use a trusted VPN\n\n"
            "💡 Your home network must be protected too: change the router's default password and use WPA2 or WPA3.\n\n"
            "Today's task: turn off auto-connect on your phone, and change your home Wi-Fi password if it is still the default 📡"
        ),
    },
    {
        "title_ar": "الدرس 6: حماية حساباتك",
        "title_en": "Lesson 6: Protecting your accounts",
        "ar": (
            "🛡️ الدرس 6: حماية حساباتك\n\n"
            "حساباتك هي حياتك على الإنترنت. راجعها النهاردة زي ما بتراجع باب بيتك.\n\n"
            "✅ اعمل التلات حاجات دول على كل حساب مهم:\n"
            "1️⃣ راجع الجلسات النشطة (Active sessions): في تليجرام وواتساب وفيسبوك وجوجل، شوف الأجهزة المتصلة — "
            "أي جهاز مش بتاعك، اخرج منه فورًا\n"
            "2️⃣ ظبط الخصوصية: مين يشوف رقمك وصورتك ومنشوراتك؟ خليها للأصدقاء بس مش \"الكل\"\n"
            "3️⃣ حدّث بيانات الاسترداد: إيميل احتياطي ورقم تليفون شغال، عشان لو اتسرق حسابك تعرف ترجّعه\n\n"
            "🚩 علامات إن حسابك اتسرق:\n"
            "• رسايل اتبعتت منك وانت مبعتّهاش\n"
            "• كلمة السر اتغيرت لوحدها\n"
            "• جالك تنبيه دخول من مكان غريب\n\n"
            "لو حصل ده: غيّر كلمة السر فورًا، فعّل التحقق بخطوتين، واخرج من كل الجلسات.\n\n"
            "واجب النهاردة: افتح تليجرام ← الإعدادات ← الأجهزة، واخرج من أي جهاز متعرفوش 🔍"
        ),
        "en": (
            "🛡️ Lesson 6: Protecting your accounts\n\n"
            "Your accounts are your life online. Check them today like you check your front door.\n\n"
            "✅ Do these three things on every important account:\n"
            "1️⃣ Review active sessions: in Telegram, WhatsApp, Facebook and Google, look at connected devices — "
            "any device that is not yours, log it out immediately\n"
            "2️⃣ Set your privacy: who can see your number, photo and posts? Friends only, not \"everyone\"\n"
            "3️⃣ Update recovery info: a backup email and a working phone number, so you can recover a stolen account\n\n"
            "🚩 Signs your account was stolen:\n"
            "• Messages sent from you that you did not send\n"
            "• Your password changed by itself\n"
            "• A login alert from a strange place\n\n"
            "If that happens: change the password at once, turn on two-step verification, and log out all sessions.\n\n"
            "Today's task: open Telegram → Settings → Devices, and log out any device you do not know 🔍"
        ),
    },
    {
        "title_ar": "الدرس 7: الفيروسات والخصوصية",
        "title_en": "Lesson 7: Malware and privacy",
        "ar": (
            "🦠 الدرس 7: الفيروسات والبرامج الضارة والخصوصية\n\n"
            "آخر درس في مسار الأمن السيبراني — وده اللي بيجمع كل اللي فات.\n\n"
            "✅ جهازك يفضل نظيف لو عملت كده:\n"
            "• حدّث نظام التشغيل والتطبيقات أول بأول — التحديثات بتقفل ثغرات\n"
            "• نزّل التطبيقات من المتجر الرسمي بس (Google Play / App Store)، مش من روابط\n"
            "• راجع أذونات التطبيقات: ليه تطبيق الكشاف عايز يوصل لجهات اتصالك؟ امنع الأذونات الزيادة\n"
            "• متفتحش مرفقات من ناس متعرفهاش\n\n"
            "🔒 خصوصيتك:\n"
            "• كل تطبيق بياخد بياناتك بيبيعها أو بيستخدمها في إعلانات — قلل اللي بتشاركه\n"
            "• اعمل نسخة احتياطية (backup) لصورك وملفاتك المهمة كل أسبوع — لو جهازك اتسرق أو اتقفل، بياناتك تفضل معاك\n"
            "• راجع إعدادات الخصوصية في فيسبوك وجوجل كل شهر\n\n"
            "🎉 مبروك! خلصت المستوى الأول من الأمن السيبراني. دلوقتي انت بتعرف تحمي نفسك أحسن من 90% من الناس.\n\n"
            "واجب النهاردة: ادخل على إعدادات الخصوصية في فيسبوك وخلّي منشوراتك للأصدقاء بس.\n\n"
            "اللي جاي: المستوى التاني — النسخ الاحتياطي، الدفع الآمن، خدع الهندسة الاجتماعية، ولو حسابك اتسرق تعمل إيه. اكتب /lesson عشان تكمل 👌"
        ),
        "en": (
            "🦠 Lesson 7: Malware and privacy\n\n"
            "Last lesson of the cybersecurity track — this one ties everything together.\n\n"
            "✅ Keep your device clean:\n"
            "• Update your system and apps promptly — updates close security holes\n"
            "• Download apps only from the official store (Google Play / App Store), never from links\n"
            "• Review app permissions: why does a flashlight app need your contacts? Remove extra permissions\n"
            "• Never open attachments from strangers\n\n"
            "🔒 Your privacy:\n"
            "• Every app that takes your data sells it or uses it for ads — share less\n"
            "• Back up your photos and important files weekly — if your device is stolen or locked, your data stays with you\n"
            "• Review privacy settings on Facebook and Google every month\n\n"
            "🎉 Congratulations! You finished Level 1 of cybersecurity. You now protect yourself better than 90% of people.\n\n"
            "Today's task: open your Facebook privacy settings and set your posts to friends only.\n\n"
            "Coming next: Level 2 — backups, safe payments, social engineering tricks, and what to do if your account is hacked. Send /lesson to continue 👌"
        ),
    },
    {
        "title_ar": "الدرس 8: النسخ الاحتياطي الآمن",
        "title_en": "Lesson 8: Secure backups",
        "ar": (
            "💾 الدرس 8: النسخ الاحتياطي الآمن\n\n"
            "موبايلك ممكن يتسرق، والكمبيوتر ممكن يعطل فجأة — واللي بيحميك هو نسخة احتياطية (backup) معمولة صح.\n\n"
            "✅ قاعدة 3-2-1 الذهبية:\n"
            "• 3 نسخ من ملفاتك المهمة\n"
            "• على وسيطين مختلفين (مثلاً: موبايلك + فلاشة أو هارد خارجي)\n"
            "• ونسخة واحدة برّه بيتك (تخزين سحابي زي Google Drive)\n\n"
            "🔒 وخلّي النسخة محمية:\n"
            "• فعّل النسخ الاحتياطي التلقائي لصورك وجهات اتصالك\n"
            "• لو النسخة فيها ملفات حساسة، حطها في مجلد محمي بكلمة سر\n"
            "• جرّب ترجّع ملف من النسخة كل شهر — نسخة مش متجرّبة يعني مفيش نسخة!\n\n"
            "💡 الفدية (ransomware) بتشفّر ملفاتك وتطلب فلوس عشان ترجعها — النسخة الاحتياطية هي اللي بتخليك مش محتاج تدفع حاجة.\n\n"
            "واجب النهاردة: فعّل النسخ الاحتياطي التلقائي على موبايلك، وخد نسخة من صورك المهمة على فلاشة 📸"
        ),
        "en": (
            "💾 Lesson 8: Secure backups\n\n"
            "Your phone can be stolen and your computer can break suddenly — what protects you is a proper backup.\n\n"
            "✅ The golden 3-2-1 rule:\n"
            "• 3 copies of your important files\n"
            "• On 2 different media (e.g. your phone + a USB stick or external drive)\n"
            "• And 1 copy outside your home (cloud storage like Google Drive)\n\n"
            "🔒 Keep the backup protected:\n"
            "• Turn on automatic backup for your photos and contacts\n"
            "• If the backup has sensitive files, put it in a password-protected folder\n"
            "• Try restoring one file every month — an untested backup is no backup!\n\n"
            "💡 Ransomware encrypts your files and demands money to return them — a backup means you never need to pay.\n\n"
            "Today's task: turn on automatic backup on your phone, and copy your important photos to a USB stick 📸"
        ),
    },
    {
        "title_ar": "الدرس 9: الدفع الآمن على الإنترنت",
        "title_en": "Lesson 9: Safe online payments",
        "ar": (
            "💳 الدرس 9: الدفع الآمن على الإنترنت\n\n"
            "لما تدفع أونلاين، انت بتدي بيانات حساسة لموقع — فلازم تتأكد إنه يستاهل الثقة.\n\n"
            "✅ ادفع بأمان:\n"
            "• ادفع من التطبيق الرسمي أو الموقع الرسمي بس، مش من رابط جاي في رسالة\n"
            "• اتأكد من القفل وعلامة https قبل ما تكتب بيانات الكارت\n"
            "• استخدم بطاقة افتراضية أو بطاقة مسبقة الدفع للتسوق أونلاين، وسيب بطاقتك الأساسية بعيد\n"
            "• فعّل تنبيهات البنك (SMS) عشان أي عملية سحب توصلك فورًا\n\n"
            "🚩 وقف فورًا لو:\n"
            "• موقع بيطلب منك كلمة سر البنك أو رقم الـ OTP عشان \"تأكيد الدفع\" — البنك الحقيقي عمره ما يطلب كده\n"
            "• حد بيقولك حوّل فلوس الأول وبعدين تستلم — ده نصب 100%\n"
            "• سعر خيالي أرخص من السوق بكتير — فخ\n\n"
            "واجب النهاردة: راجع آخر 5 عمليات على حسابك البنكي، وتأكد إنك تعرفهم كلهم 🧾"
        ),
        "en": (
            "💳 Lesson 9: Safe online payments\n\n"
            "When you pay online, you hand sensitive data to a website — make sure it deserves your trust.\n\n"
            "✅ Pay safely:\n"
            "• Pay only from the official app or official website, never from a link in a message\n"
            "• Check for the lock and https before typing card details\n"
            "• Use a virtual card or prepaid card for online shopping, and keep your main card away\n"
            "• Turn on bank SMS alerts so every withdrawal reaches you instantly\n\n"
            "🚩 Stop immediately if:\n"
            "• A site asks for your bank password or OTP to \"confirm payment\" — a real bank never asks for that\n"
            "• Someone tells you to transfer money first and receive later — that is 100% a scam\n"
            "• A price far cheaper than the market — a trap\n\n"
            "Today's task: review your last 5 bank transactions and make sure you recognize all of them 🧾"
        ),
    },
    {
        "title_ar": "الدرس 10: خدع الهندسة الاجتماعية",
        "title_en": "Lesson 10: Social engineering tricks",
        "ar": (
            "🎭 الدرس 10: خدع الهندسة الاجتماعية\n\n"
            "أخطر هجوم مش على جهازك — على عقلك. النصّاب بيخليك انت اللي تدي له البيانات بنفسك.\n\n"
            "🎯 أشهر الخدع:\n"
            "• \"أنا من خدمة العملاء، حسابك فيه مشكلة، اديني الكود اللي وصلك\" — مفيش موظف حقيقي بيطلب كود\n"
            "• \"أنا صاحبك، موبايلي اتسرق وكلّمك من رقم جديد، حوّل لي فلوس بسرعة\" — اتصل بصاحبك على رقمه القديم الأول\n"
            "• \"مبروك كسبت!\" + استعجال وضغط — الخوف والاستعجال هما سلاح النصّاب\n"
            "• عرض شغل أو قرض سهل جدًا — الطُعم دايمًا حلو\n\n"
            "✅ القاعدة الذهبية: لو حد طلب منك فلوس أو بيانات أو كود — وقف، واتأكد من مصدر تاني بنفسك "
            "(اتصل بالرقم الرسمي، مش الرقم اللي كلّمك).\n\n"
            "واجب النهاردة: احكي لحد من عيلتك عن خدعة واحدة من دول — النصّابين بيستهدفوا اللي مش عارفين 👨‍👩‍👧"
        ),
        "en": (
            "🎭 Lesson 10: Social engineering tricks\n\n"
            "The most dangerous attack is not on your device — it is on your mind. The scammer makes YOU hand over the data.\n\n"
            "🎯 The most common tricks:\n"
            "• \"I am from customer service, your account has a problem, give me the code you received\" — no real employee ever asks for a code\n"
            "• \"It is your friend, my phone was stolen and I am calling from a new number, send me money quickly\" — call your friend on the old number first\n"
            "• \"Congratulations, you won!\" plus urgency and pressure — fear and rush are the scammer's weapons\n"
            "• A job or loan offer that is too easy — the bait is always sweet\n\n"
            "✅ The golden rule: if someone asks you for money, data or a code — stop, and verify through another channel yourself "
            "(call the official number, not the number that called you).\n\n"
            "Today's task: tell a family member about one of these tricks — scammers target those who do not know 👨‍👩‍👧"
        ),
    },
    {
        "title_ar": "الدرس 11: أمن الموبايل والأجهزة",
        "title_en": "Lesson 11: Phone and device security",
        "ar": (
            "📱 الدرس 11: أمن الموبايل والأجهزة\n\n"
            "موبايلك فيه حياتك كلها — صورك، حساباتك، فلوسك. لو ضاع من غير حماية، اللي يلاقيه يلاقي كل حاجة.\n\n"
            "✅ احمي جهازك:\n"
            "• قفل شاشة قوي: بصمة أو PIN طويل (6 أرقام على الأقل) — مش نمط سهل\n"
            "• فعّل \"العثور على جهازي\" (Find My Device) عشان لو ضاع تقدر تقفله وتمسح بياناته عن بُعد\n"
            "• حدّث النظام والتطبيقات أول بأول — التحديثات بتقفل ثغرات\n"
            "• راجع أذونات التطبيقات: لعبة بتطلب الوصول لجهات اتصالك؟ امنعها\n"
            "• متثبّتش تطبيقات من برّه المتجر الرسمي\n\n"
            "😱 لو موبايلك ضاع أو اتسرق:\n"
            "1. اقفله وامسح بياناته عن بُعد من Find My Device\n"
            "2. غيّر كلمات سر حساباتك المهمة من جهاز تاني\n"
            "3. كلّم شركة الاتصالات توقف الخط\n\n"
            "واجب النهاردة: فعّل \"العثور على جهازي\" وتأكد إن قفل شاشتك قوي 🔐"
        ),
        "en": (
            "📱 Lesson 11: Phone and device security\n\n"
            "Your phone holds your whole life — photos, accounts, money. If it is lost unprotected, whoever finds it finds everything.\n\n"
            "✅ Protect your device:\n"
            "• Strong screen lock: fingerprint or a long PIN (at least 6 digits) — not an easy pattern\n"
            "• Turn on \"Find My Device\" so if it is lost you can lock it and erase it remotely\n"
            "• Update the system and apps promptly — updates close security holes\n"
            "• Review app permissions: a game asking for your contacts? Deny it\n"
            "• Never install apps from outside the official store\n\n"
            "😱 If your phone is lost or stolen:\n"
            "1. Lock it and erase it remotely from Find My Device\n"
            "2. Change the passwords of your important accounts from another device\n"
            "3. Call your carrier to suspend the line\n\n"
            "Today's task: turn on \"Find My Device\" and make sure your screen lock is strong 🔐"
        ),
    },
    {
        "title_ar": "الدرس 12: التصفح الآمن",
        "title_en": "Lesson 12: Safe browsing",
        "ar": (
            "🌐 الدرس 12: التصفح الآمن\n\n"
            "المتصفح هو بابك للإنترنت — ولو الباب مفتوح على أي حاجة، المشاكل بتدخل معاه.\n\n"
            "✅ اتصفح بأمان:\n"
            "• اتأكد من https والقفل قبل ما تكتب أي بيانات\n"
            "• نزّل الملفات والبرامج من المواقع الرسمية بس\n"
            "• حدّث المتصفح — النسخ القديمة فيها ثغرات معروفة\n"
            "• راجع الإضافات (extensions) اللي مثبّتها: أي إضافة مش بتستخدمها، شيلها\n"
            "• الوضع الخفي (incognito) بيخفي السجل من جهازك بس، مش بيخفيك عن المواقع — مش حماية كاملة\n\n"
            "⚠️ على جهاز مش بتاعك (كمبيوتر عام أو موبايل صاحبك):\n"
            "• متعلّمش \"تذكرني\" ولا تحفظ كلمة السر\n"
            "• اخرج من كل حساباتك قبل ما تمشي\n"
            "• امسح سجل التصفح وملفات تعريف الارتباط بعد ما تخلص\n\n"
            "واجب النهاردة: افتح إضافات المتصفح عندك، وشيل أي إضافة متعرفهاش أو مش بتستخدمها 🧹"
        ),
        "en": (
            "🌐 Lesson 12: Safe browsing\n\n"
            "Your browser is your door to the internet — and if the door is open to anything, trouble walks in with it.\n\n"
            "✅ Browse safely:\n"
            "• Check https and the lock before typing any data\n"
            "• Download files and programs only from official sites\n"
            "• Update your browser — old versions have known holes\n"
            "• Review your installed extensions: remove any you do not use\n"
            "• Incognito mode hides history from your device only, not from websites — it is not full protection\n\n"
            "⚠️ On a device that is not yours (a public computer or a friend's phone):\n"
            "• Do not tick \"remember me\" and do not save passwords\n"
            "• Log out of all your accounts before you leave\n"
            "• Clear browsing history and cookies when you finish\n\n"
            "Today's task: open your browser extensions and remove any you do not know or do not use 🧹"
        ),
    },
    {
        "title_ar": "الدرس 13: لو حسابك اتسرق — تعمل إيه؟",
        "title_en": "Lesson 13: If your account is hacked — what to do",
        "ar": (
            "🆘 الدرس 13: لو حسابك اتسرق — تعمل إيه؟\n\n"
            "حتى الحذرين ممكن يتسرق حسابهم. المهم متتوترش، واتصرف بسرعة وبالترتيب.\n\n"
            "🚨 خطوات الإنقاذ (بالترتيب):\n"
            "1️⃣ غيّر كلمة السر فورًا — من جهاز تاني نضيف، مش من نفس الجهاز المشبوه\n"
            "2️⃣ اخرج من كل الجلسات (في تليجرام: الإعدادات ← الأجهزة ← إنهاء كل الجلسات)\n"
            "3️⃣ فعّل التحقق بخطوتين لو مش مفعّل\n"
            "4️⃣ راجع الإيميل ورقم التليفون المربوطين بالحساب — لو اتغيّروا، رجّعهم\n"
            "5️⃣ حذّر أصحابك إن حسابك اتسرق، عشان محدش يبعت فلوس للنصّاب\n"
            "6️⃣ بلّغ المنصة (فيسبوك/تليجرام/واتساب) إن الحساب اتسرق\n"
            "7️⃣ لو مربوط ببطاقة بنكية، كلّم البنك وراجع العمليات\n\n"
            "⚠️ ومتدفعش فدية لأي حد يقولك \"هيرجّع لك الحساب بفلوس\" — ده نصّاب تاني.\n\n"
            "واجب النهاردة: اكتب الخطوات دي في ملاحظة على موبايلك — وقت الأزمة مش وقت التفكير 📝"
        ),
        "en": (
            "🆘 Lesson 13: If your account is hacked — what to do\n\n"
            "Even careful people can lose an account. The important thing is not to panic — act fast and in order.\n\n"
            "🚨 Rescue steps (in order):\n"
            "1️⃣ Change the password at once — from a different, clean device, not the suspicious one\n"
            "2️⃣ Log out of all sessions (in Telegram: Settings → Devices → Terminate all other sessions)\n"
            "3️⃣ Turn on two-step verification if it is off\n"
            "4️⃣ Check the email and phone number linked to the account — if they were changed, restore them\n"
            "5️⃣ Warn your friends that your account was stolen, so nobody sends money to the scammer\n"
            "6️⃣ Report to the platform (Facebook/Telegram/WhatsApp) that the account was stolen\n"
            "7️⃣ If a bank card is linked, call the bank and review transactions\n\n"
            "⚠️ And never pay a ransom to anyone who says \"I will return your account for money\" — that is another scammer.\n\n"
            "Today's task: write these steps in a note on your phone — a crisis is not the time to think 📝"
        ),
    },
    {
        "title_ar": "الدرس 14: خصوصيتك على السوشيال ميديا",
        "title_en": "Lesson 14: Privacy on social media",
        "ar": (
            "🔒 الدرس 14: خصوصيتك على السوشيال ميديا\n\n"
            "كل بوست بتنشره بيقول عنك أكتر مما تتخيل: مكانك، عاداتك، وأوقات غيابك عن البيت.\n\n"
            "✅ قواعد النشر الآمن:\n"
            "• راجع مين يشوف منشوراتك — خليها \"الأصدقاء\" مش \"العامة\"\n"
            "• متنشرش صور فيها عنوان بيتك، أو لوحة عربية، أو تذاكر سفر (فيها بياناتك)\n"
            "• اقفل خاصية الموقع (location) في الصور والبوستات — النصّابين بيعرفوا انت فين\n"
            "• متنشرش وانت مسافر إن بيتك فاضي — استنى لما ترجع\n"
            "• راجع التطبيقات المتصلة بحسابك على فيسبوك وجوجل، وشيل اللي مش بتستخدمه\n\n"
            "👤 طلبات الصداقة:\n"
            "• حساب جديد من غير صور ولا أصدقاء مشتركين؟ متقبلوش\n"
            "• حد بيبعت لك رسايل غريبة بعد ما قبلته؟ اعمل حظر وبلّغ\n\n"
            "🎉 مبروك! خلصت المستوى التاني من الأمن السيبراني. دلوقتي بتعرف تحمي نفسك وحساباتك وخصوصيتك.\n\n"
            "واجب النهاردة: افتح إعدادات الخصوصية في فيسبوك، وخلّي منشوراتك للأصدقاء بس، وشيل تطبيق واحد متصل بحسابك مش بتستخدمه.\n\n"
            "الخطوة اللي بعدها: مسار البرمجة — اكتب /lesson عشان تبدأ بايثون 🐍"
        ),
        "en": (
            "🔒 Lesson 14: Privacy on social media\n\n"
            "Every post you publish says more about you than you think: your location, your habits, and when you are away from home.\n\n"
            "✅ Safe posting rules:\n"
            "• Check who sees your posts — set them to \"Friends\", not \"Public\"\n"
            "• Never post photos showing your home address, a car plate, or travel tickets (they carry your data)\n"
            "• Turn off location in photos and posts — scammers learn where you are\n"
            "• Do not post while traveling that your home is empty — wait until you are back\n"
            "• Review the apps connected to your Facebook and Google accounts, and remove the ones you do not use\n\n"
            "👤 Friend requests:\n"
            "• A new account with no photos and no mutual friends? Do not accept it\n"
            "• Someone sending strange messages after you accepted? Block and report\n\n"
            "🎉 Congratulations! You finished Level 2 of cybersecurity. Now you know how to protect yourself, your accounts and your privacy.\n\n"
            "Today's task: open your Facebook privacy settings, set your posts to Friends only, and remove one connected app you do not use.\n\n"
            "Next step: the programming track — send /lesson to start Python 🐍"
        ),
    },
]

PYTHON_LESSONS = [
    {
        "title_ar": "الدرس 1: جهّز بايثون — التثبيت خطوة بخطوة",
        "title_en": "Lesson 1: Setting up Python — step-by-step installation",
        "ar": (
            "🖥️ الدرس 1: جهّز بايثون — التثبيت خطوة بخطوة\n\n"
            "قبل ما نكتب أي كود، لازم بايثون يبقى شغال على جهازك. هنعمله في 5 دقايق — كمبيوتر أو موبايل.\n\n"
            "💻 على الكمبيوتر (ويندوز):\n"
            "1. افتح المتصفح وادخل على python.org\n"
            "2. دوس على زرار \"Download Python\" الأصفر، ونزّل الملف\n"
            "3. افتح الملف اللي نزل — هيفتح لك برنامج التثبيت\n"
            "4. ⚠️ أهم خطوة: علّم صح على \"Add Python to PATH\" اللي تحت — من غيرها الكمبيوتر مش هيعرف بايثون\n"
            "5. دوس Install Now، واستنى لحد ما يخلص، وبعدين Close\n\n"
            "اتأكد إنه اشتغل:\n"
            "• افتح قائمة Start واكتب cmd ودوس Enter — هتفتح شاشة سوداء (الطرفية)\n"
            "• اكتب python ودوس Enter — لازم تشوف >>> دي علامة إن بايثون شغال\n"
            "• اكتب print(\"أهلاً\") ودوس Enter — هيطبع أهلاً على الشاشة 🎉\n"
            "• اكتب exit() عشان تخرج\n\n"
            "تشغيل ملف:\n"
            "• افتح المفكرة (Notepad)، اكتب print(\"أهلاً بالعالم\")، واحفظ الملف باسم hello.py\n"
            "• في نفس الشاشة السوداء، اكتب python hello.py — لازم تكون في نفس المجلد اللي حفظت فيه الملف\n\n"
            "📱 على الموبايل (أندرويد):\n"
            "1. افتح Google Play وابحث عن Pydroid 3 ونزّله (مجاني)\n"
            "2. افتح التطبيق — هتلاقي محرر جاهز\n"
            "3. اكتب print(\"أهلاً\") ودوس على زرار التشغيل الأصفر ▶️\n"
            "4. هيطبع أهلاً تحت — كده انت جاهز تتعلم من موبايلك 📱\n\n"
            "واجب النهاردة: ثبّت بايثون (كمبيوتر أو موبايل)، وشغّل أول print بتاعك — ولو وقفت في خطوة، ارجع للدرس واعملها تاني خطوة خطوة."
        ),
        "en": (
            "🖥️ Lesson 1: Setting up Python — step-by-step installation\n\n"
            "Before we write any code, Python must be running on your device. It takes 5 minutes — computer or phone.\n\n"
            "💻 On a computer (Windows):\n"
            "1. Open your browser and go to python.org\n"
            "2. Click the yellow \"Download Python\" button and download the file\n"
            "3. Open the downloaded file — the installer will open\n"
            "4. ⚠️ The most important step: tick \"Add Python to PATH\" at the bottom — without it your computer will not know Python\n"
            "5. Click Install Now, wait until it finishes, then Close\n\n"
            "Make sure it works:\n"
            "• Open the Start menu, type cmd and press Enter — a black screen (the terminal) will open\n"
            "• Type python and press Enter — you should see >>> which means Python is running\n"
            "• Type print(\"Hello\") and press Enter — it prints Hello on the screen 🎉\n"
            "• Type exit() to quit\n\n"
            "Running a file:\n"
            "• Open Notepad, type print(\"Hello, world\"), and save the file as hello.py\n"
            "• In the same black screen, type python hello.py — you must be in the same folder where you saved the file\n\n"
            "📱 On a phone (Android):\n"
            "1. Open Google Play, search for Pydroid 3 and install it (free)\n"
            "2. Open the app — you will find a ready editor\n"
            "3. Type print(\"Hello\") and press the yellow Run button ▶️\n"
            "4. It prints Hello below — now you are ready to learn from your phone 📱\n\n"
            "Today's task: install Python (computer or phone) and run your first print — and if you get stuck on a step, come back to this lesson and do it again step by step."
        ),
    },
    {
        "title_ar": "الدرس 2: يعني إيه برمجة؟",
        "title_en": "Lesson 2: What is programming?",
        "ar": (
            "🐍 الدرس 2: يعني إيه برمجة؟\n\n"
            "البرمجة يعني تكتب تعليمات للكمبيوتر يعملها — زي ما بتكتب وصفة أكل للطباخ.\n\n"
            "بايثون (Python) هي أسهل لغة تبدأ بيها، وهي أكتر لغة مستخدمة في الأمن السيبراني والذكاء الاصطناعي.\n\n"
            "📥 لو لسه مثبّتش بايثون، ارجع للدرس 1 (التثبيت) وخلّصه الأول — هنحتاج بايثون شغال عشان نجرّب.\n\n"
            "💻 أول برنامج ليك — اكتب السطر ده وشغّله:\n"
            "print(\"أهلاً بالعالم\")\n\n"
            "هيطبع على الشاشة: أهلاً بالعالم 🎉\n\n"
            "مبروك، انت كده مبرمج! كل البرامج الكبيرة بتبدأ بسطر زي ده.\n\n"
            "واجب النهاردة: ثبّت بايثون وشغّل أول print بتاعك، وجرّب تغيّر الكلام اللي بين علامات التنصيص."
        ),
        "en": (
            "🐍 Lesson 2: What is programming?\n\n"
            "Programming means writing instructions for the computer to follow — like writing a recipe for a cook.\n\n"
            "Python is the easiest language to start with, and the most used in cybersecurity and AI.\n\n"
            "📥 If you have not installed Python yet, go back to Lesson 1 (setup) and finish it first — we need Python running to try things.\n\n"


            "💻 Your first program — write this line and run it:\n"
            "print(\"Hello, world\")\n\n"
            "It prints on the screen: Hello, world 🎉\n\n"
            "Congratulations, you are a programmer now! Every big program starts with a line like this.\n\n"
            "Today's task: install Python, run your first print, and try changing the text inside the quotes."
        ),
    },
    {
        "title_ar": "الدرس 3: المتغيرات",
        "title_en": "Lesson 3: Variables",
        "ar": (
            "📦 الدرس 3: المتغيرات\n\n"
            "المتغير هو علبة بتحط فيها قيمة وتسميها، عشان تستخدمها بعدين.\n\n"
            "اسم = \"خالد\"\n"
            "عمر = 30\n"
            "طول = 175.5\n"
            "متجوز = False\n\n"
            "أنواع البيانات:\n"
            "• نص (str): بين علامتي تنصيص \"...\"\n"
            "• رقم صحيح (int): 30\n"
            "• رقم عشري (float): 175.5\n"
            "• صح/غلط (bool): True أو False\n\n"
            "جرّب الكود ده:\n"
            "name = \"خالد\"\n"
            "age = 30\n"
            "print(\"اسمي\", name, \"وعمري\", age)\n\n"
            "💡 اسم المتغير يكون واضح: \"password_length\" أحسن من \"x\".\n\n"
            "واجب النهاردة: اعمل متغيرات لاسمك وعمرك ومدينتك، واطبعهم في جملة واحدة."
        ),
        "en": (
            "📦 Lesson 3: Variables\n\n"
            "A variable is a box where you store a value and give it a name, to use it later.\n\n"
            "name = \"Khaled\"\n"
            "age = 30\n"
            "height = 175.5\n"
            "married = False\n\n"
            "Data types:\n"
            "• Text (str): inside quotes \"...\"\n"
            "• Whole number (int): 30\n"
            "• Decimal number (float): 175.5\n"
            "• True/False (bool): True or False\n\n"
            "Try this code:\n"
            "name = \"Khaled\"\n"
            "age = 30\n"
            "print(\"My name is\", name, \"and I am\", age)\n\n"
            "💡 Name variables clearly: \"password_length\" is better than \"x\".\n\n"
            "Today's task: make variables for your name, age and city, and print them in one sentence."
        ),
    },
    {
        "title_ar": "الدرس 4: الإدخال والحساب",
        "title_en": "Lesson 4: Input and math",
        "ar": (
            "🧮 الدرس 4: الإدخال والحساب\n\n"
            "البرنامج يبقى مفيد لما يسأل المستخدم ويدخل بيانات.\n\n"
            "name = input(\"اسمك إيه؟ \")\n"
            "print(\"أهلاً\", name)\n\n"
            "⚠️ input بترجع نص دايمًا. لو عايز رقم، حوّله:\n"
            "age = int(input(\"عمرك كام؟ \"))\n"
            "print(\"هيبقى عمرك السنة الجاية\", age + 1)\n\n"
            "العمليات الحسابية:\n"
            "• + جمع، - طرح، * ضرب، / قسمة\n"
            "• % باقي القسمة، ** أس\n"
            "• مثال: 10 % 3 = 1 ، 2 ** 3 = 8\n\n"
            "جرّب تعمل آلة حاسبة صغيرة:\n"
            "a = int(input(\"أول رقم: \"))\n"
            "b = int(input(\"تاني رقم: \"))\n"
            "print(\"المجموع =\", a + b)\n"
            "print(\"الحاصل ضربهم =\", a * b)\n\n"
            "واجب النهاردة: اعمل برنامج يسأل عن سعر حاجة وعددها، ويحسب التمن الكلي."
        ),
        "en": (
            "🧮 Lesson 4: Input and math\n\n"
            "A program becomes useful when it asks the user for input.\n\n"
            "name = input(\"What is your name? \")\n"
            "print(\"Hello\", name)\n\n"
            "⚠️ input always returns text. If you want a number, convert it:\n"
            "age = int(input(\"How old are you? \"))\n"
            "print(\"Next year you will be\", age + 1)\n\n"
            "Math operators:\n"
            "• + add, - subtract, * multiply, / divide\n"
            "• % remainder, ** power\n"
            "• Example: 10 % 3 = 1, 2 ** 3 = 8\n\n"
            "Try a small calculator:\n"
            "a = int(input(\"First number: \"))\n"
            "b = int(input(\"Second number: \"))\n"
            "print(\"Sum =\", a + b)\n"
            "print(\"Product =\", a * b)\n\n"
            "Today's task: write a program that asks for a price and a quantity, and prints the total."
        ),
    },
    {
        "title_ar": "الدرس 5: الشروط (if)",
        "title_en": "Lesson 5: Conditions (if)",
        "ar": (
            "🚦 الدرس 5: الشروط (if)\n\n"
            "الشرط بيخلي البرنامج يقرر: لو حصل كذا، اعمل كذا — غير كده اعمل حاجة تانية.\n\n"
            "password = input(\"اكتب كلمة السر: \")\n"
            "if len(password) >= 8:\n"
            "    print(\"كلمة السر قوية ✅\")\n"
            "else:\n"
            "    print(\"كلمة السر قصيرة ❌ لازم 8 حروف على الأقل\")\n\n"
            "⚠️ المسافات في أول السطر مهمة في بايثون — الكود اللي جوه الشرط لازم يكون مزاح 4 مسافات.\n\n"
            "المقارنات:\n"
            "• == يساوي، != مش يساوي\n"
            "• > أكبر من، < أصغر من\n"
            "• >= أكبر من أو يساوي\n"
            "• and (و)، or (أو)، not (مش)\n\n"
            "جرّب:\n"
            "age = int(input(\"عمرك كام؟ \"))\n"
            "if age >= 18:\n"
            "    print(\"انت بالغ\")\n"
            "elif age >= 13:\n"
            "    print(\"انت مراهق\")\n"
            "else:\n"
            "    print(\"انت طفل\")\n\n"
            "واجب النهاردة: اعمل برنامج يفحص قوة كلمة السر: لو أقل من 8 حروف \"ضعيفة\"، من 8 لـ 11 \"متوسطة\"، 12 أو أكتر \"قوية\"."
        ),
        "en": (
            "🚦 Lesson 5: Conditions (if)\n\n"
            "A condition lets the program decide: if this happens, do that — otherwise do something else.\n\n"
            "password = input(\"Enter a password: \")\n"
            "if len(password) >= 8:\n"
            "    print(\"Strong password ✅\")\n"
            "else:\n"
            "    print(\"Too short ❌ at least 8 characters\")\n\n"
            "⚠️ Indentation matters in Python — code inside the condition must be indented by 4 spaces.\n\n"
            "Comparisons:\n"
            "• == equal, != not equal\n"
            "• > greater than, < less than\n"
            "• >= greater than or equal\n"
            "• and, or, not\n\n"
            "Try:\n"
            "age = int(input(\"How old are you? \"))\n"
            "if age >= 18:\n"
            "    print(\"You are an adult\")\n"
            "elif age >= 13:\n"
            "    print(\"You are a teenager\")\n"
            "else:\n"
            "    print(\"You are a child\")\n\n"
            "Today's task: write a program that checks password strength: under 8 chars \"weak\", 8-11 \"medium\", 12+ \"strong\"."
        ),
    },
    {
        "title_ar": "الدرس 6: الحلقات (loops)",
        "title_en": "Lesson 6: Loops",
        "ar": (
            "🔁 الدرس 6: الحلقات (loops)\n\n"
            "الحلقة بتكرر نفس الكود بدل ما تكتبه 100 مرة.\n\n"
            "for i in range(5):\n"
            "    print(\"أهلاً\", i)\n\n"
            "هيطبع \"أهلاً\" 5 مرات مع الأرقام 0 لحد 4.\n\n"
            "الحلقة while بتكرر لحد ما الشرط يبقى غلط:\n"
            "count = 3\n"
            "while count > 0:\n"
            "    print(count)\n"
            "    count = count - 1\n"
            "print(\"انطلق! 🚀\")\n\n"
            "جرّب: جدول الضرب\n"
            "n = int(input(\"جدول ضرب كام؟ \"))\n"
            "for i in range(1, 11):\n"
            "    print(n, \"x\", i, \"=\", n * i)\n\n"
            "💡 احذر الحلقة اللي مبتخلصش (while True من غير break) — هتفضل شغالة على طول!\n\n"
            "واجب النهاردة: اعمل برنامج يطبع الأرقام الزوجية من 2 لحد 20."
        ),
        "en": (
            "🔁 Lesson 6: Loops\n\n"
            "A loop repeats the same code instead of writing it 100 times.\n\n"
            "for i in range(5):\n"
            "    print(\"Hello\", i)\n\n"
            "This prints \"Hello\" 5 times with numbers 0 to 4.\n\n"
            "The while loop repeats until the condition is false:\n"
            "count = 3\n"
            "while count > 0:\n"
            "    print(count)\n"
            "    count = count - 1\n"
            "print(\"Go! 🚀\")\n\n"
            "Try: multiplication table\n"
            "n = int(input(\"Which table? \"))\n"
            "for i in range(1, 11):\n"
            "    print(n, \"x\", i, \"=\", n * i)\n\n"
            "💡 Beware the loop that never ends (while True without break) — it runs forever!\n\n"
            "Today's task: write a program that prints the even numbers from 2 to 20."
        ),
    },
    {
        "title_ar": "الدرس 7: القوائم والدوال",
        "title_en": "Lesson 7: Lists and functions",
        "ar": (
            "📋 الدرس 7: القوائم والدوال\n\n"
            "القائمة (list) بتحفظ مجموعة حاجات مع بعض:\n\n"
            "friends = [\"أحمد\", \"محمد\", \"سارة\"]\n"
            "print(friends[0])  # أحمد\n"
            "friends.append(\"علي\")  # يضيف علي في الآخر\n"
            "print(len(friends))  # 4\n\n"
            "والدالة (function) هي كود جاهز بتنادي عليه باسم:\n\n"
            "def is_strong(password):\n"
            "    return len(password) >= 12\n\n"
            "print(is_strong(\"123\"))        # False\n"
            "print(is_strong(\"Ahmed@2024#Z\"))  # True\n\n"
            "جرّب تعمل قائمة مهام:\n"
            "tasks = []\n"
            "tasks.append(\"غيّر كلمة السر\")\n"
            "tasks.append(\"فعّل التحقق بخطوتين\")\n"
            "for t in tasks:\n"
            "    print(\"☐\", t)\n\n"
            "واجب النهاردة: اعمل دالة بتاخد كلمة سر وترجع \"قوية\" أو \"ضعيفة\"، وجرّبها على 3 كلمات سر مختلفة."
        ),
        "en": (
            "📋 Lesson 7: Lists and functions\n\n"
            "A list stores a group of things together:\n\n"
            "friends = [\"Ahmed\", \"Mohamed\", \"Sara\"]\n"
            "print(friends[0])  # Ahmed\n"
            "friends.append(\"Ali\")  # adds Ali at the end\n"
            "print(len(friends))  # 4\n\n"
            "A function is ready code you call by name:\n\n"
            "def is_strong(password):\n"
            "    return len(password) >= 12\n\n"
            "print(is_strong(\"123\"))        # False\n"
            "print(is_strong(\"Ahmed@2024#Z\"))  # True\n\n"
            "Try a to-do list:\n"
            "tasks = []\n"
            "tasks.append(\"Change password\")\n"
            "tasks.append(\"Turn on 2FA\")\n"
            "for t in tasks:\n"
            "    print(\"☐\", t)\n\n"
            "Today's task: write a function that takes a password and returns \"strong\" or \"weak\", and test it with 3 different passwords."
        ),
    },
    {
        "title_ar": "الدرس 8: مشروعك الأول — مولّد كلمات سر",
        "title_en": "Lesson 8: Your first project — password generator",
        "ar": (
            "🎓 الدرس 8: مشروعك الأول — مولّد كلمات سر\n\n"
            "دلوقتي هنجمع كل اللي اتعلمته في برنامج واحد مفيد: برنامج يولّد كلمة سر قوية عشوائية.\n\n"
            "import random\n"
            "import string\n\n"
            "def make_password(length=12):\n"
            "    chars = string.ascii_letters + string.digits + \"!@#$%\"\n"
            "    password = \"\"\n"
            "    for i in range(length):\n"
            "        password += random.choice(chars)\n"
            "    return password\n\n"
            "print(\"كلمة السر الجديدة:\", make_password(12))\n"
            "print(\"كلمة سر أطول:\", make_password(16))\n\n"
            "إيه اللي حصل هنا؟\n"
            "• استخدمنا مكتبتين جاهزتين: random و string\n"
            "• الدالة بتاخد الطول وتعمل حلقة تختار حرف عشوائي كل مرة\n"
            "• الناتج كلمة سر قوية ومختلفة كل مرة تشغّل البرنامج\n\n"
            "🎉 مبروك! خلصت أول 7 دروس برمجة، وعملت أول مشروع حقيقي بيربط البرمجة بالأمن السيبراني.\n\n"
            "واجب النهاردة: شغّل مولّد كلمات السر وولّد كلمة سر جديدة لحساب واحد عندك — وغيّرها فعلاً.\n\n"
            "اللي جاي: المستوى المتوسط — نصوص وقواميس وملفات وكلاسات، وبعدين المستوى المتقدم. اكتب /lesson عشان تكمل 👌"
        ),
        "en": (
            "🎓 Lesson 8: Your first project — password generator\n\n"
            "Now let's combine everything into one useful program: a generator that creates a strong random password.\n\n"
            "import random\n"
            "import string\n\n"
            "def make_password(length=12):\n"
            "    chars = string.ascii_letters + string.digits + \"!@#$%\"\n"
            "    password = \"\"\n"
            "    for i in range(length):\n"
            "        password += random.choice(chars)\n"
            "    return password\n\n"
            "print(\"New password:\", make_password(12))\n"
            "print(\"Longer password:\", make_password(16))\n\n"
            "What happened here?\n"
            "• We used two ready libraries: random and string\n"
            "• The function takes a length and loops, picking a random character each time\n"
            "• The result is a strong, different password every run\n\n"
            "🎉 Congratulations! You finished your first 7 programming lessons and built your first real project, "
            "linking programming with cybersecurity.\n\n"
            "Today's task: run the password generator, make a new password for one of your accounts — and actually change it.\n\n"
            "Coming next: the intermediate level — strings, dictionaries, files and classes, then the advanced level. Send /lesson to continue 👌"
        ),
    },
    {
        "title_ar": "الدرس 9: السلاسل النصية (strings)",
        "title_en": "Lesson 9: Strings",
        "ar": (
            "🔤 الدرس 9: السلاسل النصية (strings)\n\n"
            "النص في بايثون مش مجرد كلام — تقدر تقطّعه وتدوّر فيه وتغيّره.\n\n"
            "msg = \"أهلاً بيك في بايثون\"\n"
            "print(msg.upper())  # بيحوّل الحروف لكبيرة\n"
            "print(msg.lower())\n"
            "print(len(msg))  # عدد الحروف\n"
            "print(msg[0])  # أول حرف\n"
            "print(msg[0:5])  # أول 5 حروف\n\n"
            "البحث والتبديل:\n"
            "email = \"khaled@gmail.com\"\n"
            "print(\"@\" in email)  # True\n"
            "print(email.replace(\"gmail\", \"yahoo\"))\n\n"
            "أحسن طريقة تكتب نص فيه متغيرات (f-string):\n"
            "name = \"خالد\"\n"
            "age = 30\n"
            "print(f\"اسمي {name} وعمري {age}\")\n\n"
            "واجب النهاردة: اكتب برنامج ياخد إيميل من المستخدم، ويطبع الاسم اللي قبل @.\n"
            "تلميح: استخدم split(\"@\")."
        ),
        "en": (
            "🔤 Lesson 9: Strings\n\n"
            "A string in Python is not just text — you can slice it, search it and change it.\n\n"
            "msg = \"Welcome to Python\"\n"
            "print(msg.upper())  # makes letters uppercase\n"
            "print(msg.lower())\n"
            "print(len(msg))  # number of characters\n"
            "print(msg[0])  # first character\n"
            "print(msg[0:5])  # first 5 characters\n\n"
            "Search and replace:\n"
            "email = \"khaled@gmail.com\"\n"
            "print(\"@\" in email)  # True\n"
            "print(email.replace(\"gmail\", \"yahoo\"))\n\n"
            "The best way to write text with variables (f-string):\n"
            "name = \"Khaled\"\n"
            "age = 30\n"
            "print(f\"My name is {name} and I am {age}\")\n\n"
            "Today's task: write a program that takes an email from the user and prints the name before @.\n"
            "Hint: use split(\"@\")."
        ),
    },
    {
        "title_ar": "الدرس 10: القواميس (dictionaries)",
        "title_en": "Lesson 10: Dictionaries",
        "ar": (
            "📖 الدرس 10: القواميس (dictionaries)\n\n"
            "القاموس بيحفظ بيانات على شكل \"مفتاح: قيمة\" — زي دفتر تليفونات: الاسم هو المفتاح، والرقم هو القيمة.\n\n"
            "phone = {\"أحمد\": \"01012345678\", \"سارة\": \"01198765432\"}\n"
            "print(phone[\"أحمد\"])\n"
            "phone[\"علي\"] = \"01255555555\"  # يضيف جديد\n"
            "phone[\"أحمد\"] = \"01000000000\"  # يعدّل الموجود\n\n"
            "⚠️ لو المفتاح مش موجود، البرنامج بيقع. استخدم get:\n"
            "print(phone.get(\"محمد\", \"مش موجود\"))\n\n"
            "اللف على القاموس:\n"
            "for name, number in phone.items():\n"
            "    print(name, \"->\", number)\n\n"
            "واجب النهاردة: اعمل قاموس فيه 3 مدن وعدد سكانها، واطبع المدن اللي عدد سكانها أكبر من مليون."
        ),
        "en": (
            "📖 Lesson 10: Dictionaries\n\n"
            "A dictionary stores data as \"key: value\" — like a phone book: the name is the key, the number is the value.\n\n"
            "phone = {\"Ahmed\": \"01012345678\", \"Sara\": \"01198765432\"}\n"
            "print(phone[\"Ahmed\"])\n"
            "phone[\"Ali\"] = \"01255555555\"  # adds a new one\n"
            "phone[\"Ahmed\"] = \"01000000000\"  # updates the existing one\n\n"
            "⚠️ If the key does not exist, the program crashes. Use get:\n"
            "print(phone.get(\"Mohamed\", \"not found\"))\n\n"
            "Looping over a dictionary:\n"
            "for name, number in phone.items():\n"
            "    print(name, \"->\", number)\n\n"
            "Today's task: make a dictionary of 3 cities and their populations, and print the cities with more than a million people."
        ),
    },
    {
        "title_ar": "الدرس 11: التعامل مع الأخطاء",
        "title_en": "Lesson 11: Handling errors",
        "ar": (
            "🛟 الدرس 11: التعامل مع الأخطاء\n\n"
            "المستخدم ممكن يكتب أي حاجة غلط — والبرنامج الشاطر مبيقعش، بيتصرف.\n\n"
            "try:\n"
            "    age = int(input(\"عمرك كام؟ \"))\n"
            "    print(\"السنة الجاية هيبقى عمرك\", age + 1)\n"
            "except ValueError:\n"
            "    print(\"اكتب رقم صحيح يا صاحبي 🙂\")\n\n"
            "لو حصل خطأ من نوع تاني؟ استخدم except عام:\n"
            "try:\n"
            "    result = 10 / int(input(\"اقسم على كام؟ \"))\n"
            "    print(result)\n"
            "except ZeroDivisionError:\n"
            "    print(\"مينفعش تقسم على صفر!\")\n"
            "except ValueError:\n"
            "    print(\"اكتب رقم!\")\n\n"
            "💡 القاعدة: جرّب الجزء اللي ممكن يغلط جوه try، وخلّي رسالة الخطأ واضحة للمستخدم.\n\n"
            "واجب النهاردة: عدّل الآلة الحاسبة من الدرس 4 — لو المستخدم كتب حروف بدل أرقام، البرنامج يقوله \"اكتب أرقام\" بدل ما يقع."
        ),
        "en": (
            "🛟 Lesson 11: Handling errors\n\n"
            "The user can type anything wrong — and a good program does not crash, it handles it.\n\n"
            "try:\n"
            "    age = int(input(\"How old are you? \"))\n"
            "    print(\"Next year you will be\", age + 1)\n"
            "except ValueError:\n"
            "    print(\"Please type a whole number 🙂\")\n\n"
            "Another kind of error? Use a general except:\n"
            "try:\n"
            "    result = 10 / int(input(\"Divide by how much? \"))\n"
            "    print(result)\n"
            "except ZeroDivisionError:\n"
            "    print(\"You cannot divide by zero!\")\n"
            "except ValueError:\n"
            "    print(\"Type a number!\")\n\n"
            "💡 The rule: put the part that can fail inside try, and make the error message clear to the user.\n\n"
            "Today's task: fix the calculator from lesson 4 — if the user types letters instead of numbers, the program says \"type numbers\" instead of crashing."
        ),
    },
    {
        "title_ar": "الدرس 12: الملفات",
        "title_en": "Lesson 12: Files",
        "ar": (
            "📁 الدرس 12: الملفات\n\n"
            "البرنامج ينسى كل حاجة لما يقفل — إلا لو حفظتها في ملف.\n\n"
            "الكتابة في ملف:\n"
            "with open(\"notes.txt\", \"w\", encoding=\"utf-8\") as f:\n"
            "    f.write(\"أول ملاحظة\\n\")\n"
            "    f.write(\"تاني ملاحظة\\n\")\n\n"
            "القراءة من ملف:\n"
            "with open(\"notes.txt\", \"r\", encoding=\"utf-8\") as f:\n"
            "    print(f.read())\n\n"
            "💡 كلمة with بتقفل الملف لوحدها حتى لو حصل خطأ — استخدمها دايمًا.\n\n"
            "الإضافة من غير ما تمسح القديم (\"a\" بدل \"w\"):\n"
            "with open(\"notes.txt\", \"a\", encoding=\"utf-8\") as f:\n"
            "    f.write(\"ملاحظة جديدة\\n\")\n\n"
            "واجب النهاردة: اعمل برنامج يسألك عن مهمة ويحفظها في ملف tasks.txt، وكل مرة تشغّله يطبع كل المهام المحفوظة."
        ),
        "en": (
            "📁 Lesson 12: Files\n\n"
            "A program forgets everything when it closes — unless you save it in a file.\n\n"
            "Writing to a file:\n"
            "with open(\"notes.txt\", \"w\", encoding=\"utf-8\") as f:\n"
            "    f.write(\"first note\\n\")\n"
            "    f.write(\"second note\\n\")\n\n"
            "Reading from a file:\n"
            "with open(\"notes.txt\", \"r\", encoding=\"utf-8\") as f:\n"
            "    print(f.read())\n\n"
            "💡 The word with closes the file by itself, even if an error happens — always use it.\n\n"
            "Appending without erasing the old content (\"a\" instead of \"w\"):\n"
            "with open(\"notes.txt\", \"a\", encoding=\"utf-8\") as f:\n"
            "    f.write(\"a new note\\n\")\n\n"
            "Today's task: write a program that asks you for a task and saves it in tasks.txt, and every time you run it, it prints all saved tasks."
        ),
    },
    {
        "title_ar": "الدرس 13: المكتبات و pip",
        "title_en": "Lesson 13: Libraries and pip",
        "ar": (
            "📦 الدرس 13: المكتبات و pip\n\n"
            "بايثون قوية عشان فيها مكتبات جاهزة لكل حاجة — مش لازم تخترع العجلة من جديد.\n\n"
            "مكتبات جاهزة مع بايثون:\n"
            "import datetime\n"
            "print(datetime.date.today())  # تاريخ النهاردة\n\n"
            "import os\n"
            "print(os.getcwd())  # المجلد اللي انت فيه\n\n"
            "مكتبات من برّه (pip):\n"
            "في التيرمينال اكتب:\n"
            "pip install requests\n\n"
            "(لو الأمر مش شغال، جرّب: python3 -m pip install requests)\n\n"
            "وبعدين في الكود:\n"
            "import requests\n"
            "r = requests.get(\"https://example.com\", timeout=10)\n"
            "print(r.status_code)  # 200 يعني الموقع شغال ✅\n\n"
            "💡 القاعدة: قبل ما تكتب كود لحاجة، دوّر على مكتبة جاهزة — حد عملها وجرّبها قبلك.\n\n"
            "واجب النهاردة: ثبّت مكتبة requests، واكتب برنامج يفحص لو موقع example.com شغال ولا لأ."
        ),
        "en": (
            "📦 Lesson 13: Libraries and pip\n\n"
            "Python is powerful because it has ready libraries for everything — no need to reinvent the wheel.\n\n"
            "Libraries that come with Python:\n"
            "import datetime\n"
            "print(datetime.date.today())  # today's date\n\n"
            "import os\n"
            "print(os.getcwd())  # the folder you are in\n\n"
            "Libraries from outside (pip):\n"
            "In the terminal type:\n"
            "pip install requests\n\n"
            "(If the command does not work, try: python3 -m pip install requests)\n\n"
            "Then in the code:\n"
            "import requests\n"
            "r = requests.get(\"https://example.com\", timeout=10)\n"
            "print(r.status_code)  # 200 means the site is up ✅\n\n"
            "💡 The rule: before writing code for something, look for a ready library — someone built and tested it before you.\n\n"
            "Today's task: install the requests library and write a program that checks whether example.com is up."
        ),
    },
    {
        "title_ar": "الدرس 14: الكلاسات (OOP)",
        "title_en": "Lesson 14: Classes (OOP)",
        "ar": (
            "🏛️ الدرس 14: الكلاسات (OOP)\n\n"
            "الكلاس هو قالب بتعمل منه حاجات شبه بعض — زي قالب الكحك: نفس الشكل، وحشوات مختلفة 🍪\n\n"
            "class Account:\n"
            "    def __init__(self, site, username):\n"
            "        self.site = site\n"
            "        self.username = username\n\n"
            "    def show(self):\n"
            "        print(f\"الموقع: {self.site} — اليوزر: {self.username}\")\n\n"
            "a1 = Account(\"فيسبوك\", \"khaled\")\n"
            "a2 = Account(\"جيميل\", \"khaled@gmail.com\")\n"
            "a1.show()\n"
            "a2.show()\n\n"
            "إيه اللي حصل؟\n"
            "• __init__ بتشتغل أول ما تعمل نسخة من الكلاس\n"
            "• self يعني \"الحاجة دي نفسها\" — كل نسخة ليها بياناتها\n"
            "• الدوال جوه الكلاس اسمها methods\n\n"
            "واجب النهاردة: اعمل كلاس Book فيه اسم الكتاب والمؤلف، ودالة تعرضهم في سطر واحد، واعمل منه 3 كتب."
        ),
        "en": (
            "🏛️ Lesson 14: Classes (OOP)\n\n"
            "A class is a template you use to make similar things — like a cookie cutter: same shape, different fillings 🍪\n\n"
            "class Account:\n"
            "    def __init__(self, site, username):\n"
            "        self.site = site\n"
            "        self.username = username\n\n"
            "    def show(self):\n"
            "        print(f\"Site: {self.site} — User: {self.username}\")\n\n"
            "a1 = Account(\"Facebook\", \"khaled\")\n"
            "a2 = Account(\"Gmail\", \"khaled@gmail.com\")\n"
            "a1.show()\n"
            "a2.show()\n\n"
            "What happened?\n"
            "• __init__ runs as soon as you create an instance of the class\n"
            "• self means \"this thing itself\" — every instance has its own data\n"
            "• Functions inside a class are called methods\n\n"
            "Today's task: make a Book class with a title and an author, a method that shows them in one line, and create 3 books from it."
        ),
    },
    {
        "title_ar": "الدرس 15: مشروع — مدير كلمات سر بسيط",
        "title_en": "Lesson 15: Project — simple password manager",
        "ar": (
            "🔐 الدرس 15: مشروع — مدير كلمات سر بسيط\n\n"
            "هنجمع اللي اتعلمناه (قواميس + ملفات + دوال) في برنامج عملي: مدير كلمات سر يحفظ بياناتك في ملف.\n\n"
            "import json\n\n"
            "def load():\n"
            "    try:\n"
            "        with open(\"vault.json\", \"r\", encoding=\"utf-8\") as f:\n"
            "            return json.load(f)\n"
            "    except FileNotFoundError:\n"
            "        return {}\n\n"
            "def save(data):\n"
            "    with open(\"vault.json\", \"w\", encoding=\"utf-8\") as f:\n"
            "        json.dump(data, f, ensure_ascii=False, indent=2)\n\n"
            "vault = load()\n"
            "site = input(\"الموقع: \")\n"
            "vault[site] = input(\"كلمة السر: \")\n"
            "save(vault)\n"
            "print(\"اتحفظت ✅ عندك\", len(vault), \"حسابات محفوظة\")\n\n"
            "⚠️ ده للتعلم بس — مدير كلمات سر حقيقي لازم يشفّر البيانات قبل ما يحفظها، مش يحفظها زي ما هي.\n\n"
            "واجب النهاردة: شغّل البرنامج واحفظ حسابين، وبعدين افتح ملف vault.json وشوف البيانات اتحفظت إزاي.\n\n"
            "🎉 مبروك! خلصت المستوى المتوسط. اللي جاي: المستوى المتقدم — API وقواعد بيانات واختبارات."
        ),
        "en": (
            "🔐 Lesson 15: Project — simple password manager\n\n"
            "Let's combine what we learned (dictionaries + files + functions) into a practical program: a password manager that saves your data in a file.\n\n"
            "import json\n\n"
            "def load():\n"
            "    try:\n"
            "        with open(\"vault.json\", \"r\", encoding=\"utf-8\") as f:\n"
            "            return json.load(f)\n"
            "    except FileNotFoundError:\n"
            "        return {}\n\n"
            "def save(data):\n"
            "    with open(\"vault.json\", \"w\", encoding=\"utf-8\") as f:\n"
            "        json.dump(data, f, ensure_ascii=False, indent=2)\n\n"
            "vault = load()\n"
            "site = input(\"Site: \")\n"
            "vault[site] = input(\"Password: \")\n"
            "save(vault)\n"
            "print(\"Saved ✅ you have\", len(vault), \"accounts stored\")\n\n"
            "⚠️ This is for learning only — a real password manager must encrypt the data before saving it, not store it as it is.\n\n"
            "Today's task: run the program and save two accounts, then open vault.json and see how the data was saved.\n\n"
            "🎉 Congratulations! You finished the intermediate level. Coming next: the advanced level — APIs, databases and testing."
        ),
    },
    {
        "title_ar": "الدرس 16: اختصارات القوائم والمولّدات",
        "title_en": "Lesson 16: List comprehensions and generators",
        "ar": (
            "⚡ الدرس 16: اختصارات القوائم والمولّدات\n\n"
            "بايثون فيها طريقة مختصرة تعمل قائمة جديدة من قائمة قديمة — سطر واحد بدل حلقة كاملة.\n\n"
            "الطريقة الطويلة:\n"
            "squares = []\n"
            "for n in range(1, 6):\n"
            "    squares.append(n * n)\n\n"
            "الطريقة المختصرة (list comprehension):\n"
            "squares = [n * n for n in range(1, 6)]\n"
            "print(squares)  # [1, 4, 9, 16, 25]\n\n"
            "ومع شرط:\n"
            "evens = [n for n in range(1, 21) if n % 2 == 0]\n"
            "print(evens)\n\n"
            "المولّد (generator) — نفس الفكرة بس بيطلّع قيمة قيمة من غير ما يحفظ القائمة كلها في الذاكرة:\n"
            "gen = (n * n for n in range(1, 1000001))\n"
            "print(next(gen))  # 1\n"
            "print(next(gen))  # 4\n\n"
            "💡 استخدم الـ comprehension للقراءة السريعة، والمولّد لما البيانات تكون كبيرة جدًا.\n\n"
            "واجب النهاردة: اعمل comprehension يطلّع أطوال الكلمات في قائمة أسماء: [\"أحمد\", \"سارة\", \"علي\"]."
        ),
        "en": (
            "⚡ Lesson 16: List comprehensions and generators\n\n"
            "Python has a shortcut to build a new list from an old one — one line instead of a whole loop.\n\n"
            "The long way:\n"
            "squares = []\n"
            "for n in range(1, 6):\n"
            "    squares.append(n * n)\n\n"
            "The shortcut (list comprehension):\n"
            "squares = [n * n for n in range(1, 6)]\n"
            "print(squares)  # [1, 4, 9, 16, 25]\n\n"
            "With a condition:\n"
            "evens = [n for n in range(1, 21) if n % 2 == 0]\n"
            "print(evens)\n\n"
            "A generator — the same idea, but it yields one value at a time without storing the whole list in memory:\n"
            "gen = (n * n for n in range(1, 1000001))\n"
            "print(next(gen))  # 1\n"
            "print(next(gen))  # 4\n\n"
            "💡 Use comprehensions for readable code, and generators when the data is huge.\n\n"
            "Today's task: write a comprehension that gives the lengths of the names in [\"Ahmed\", \"Sara\", \"Ali\"]."
        ),
    },
    {
        "title_ar": "الدرس 17: التعامل مع الـ APIs",
        "title_en": "Lesson 17: Working with APIs",
        "ar": (
            "🌐 الدرس 17: التعامل مع الـ APIs\n\n"
            "الـ API هو باب بيخلي برنامجك يكلم خدمة على الإنترنت وياخد منها بيانات جاهزة.\n\n"
            "import requests\n\n"
            "r = requests.get(\"https://jsonplaceholder.typicode.com/todos/1\", timeout=10)\n"
            "if r.status_code == 200:  # 200 يعني تمام\n"
            "    data = r.json()  # البيانات بتيجي على شكل قاموس\n"
            "    print(data[\"title\"])\n"
            "else:\n"
            "    print(\"الطلب فشل، كود الحالة:\", r.status_code)\n\n"
            "نقاط مهمة:\n"
            "• دايمًا حط timeout عشان البرنامج ميعلّقش\n"
            "• اتأكد من status_code قبل ما تقرأ البيانات — لو مش 200 متكمّلش\n"
            "• لو الـ API محتاج مفتاح (API key)، خزّنه في متغير بيئة مش في الكود\n\n"
            "جرّب API تاني — GitHub (من غير مفتاح، بس ليه حد للطلبات في الساعة):\n"
            "r = requests.get(\"https://api.github.com/users/octocat\", timeout=10)\n"
            "if r.status_code == 200:\n"
            "    data = r.json()\n"
            "    print(data[\"login\"])  # octocat\n"
            "    print(data[\"public_repos\"])  # عدد المشاريع العامة\n"
            "else:\n"
            "    print(\"GitHub مش متاح دلوقتي، جرّب بعد شوية\")\n\n"
            "واجب النهاردة: اكتب برنامج يجيب من GitHub API عدد المتابعين (followers) لأي يوزر تكتبه."
        ),
        "en": (
            "🌐 Lesson 17: Working with APIs\n\n"
            "An API is a door that lets your program talk to an online service and get ready data from it.\n\n"
            "import requests\n\n"
            "r = requests.get(\"https://jsonplaceholder.typicode.com/todos/1\", timeout=10)\n"
            "if r.status_code == 200:  # 200 means OK\n"
            "    data = r.json()  # the data comes as a dictionary\n"
            "    print(data[\"title\"])\n"
            "else:\n"
            "    print(\"Request failed, status code:\", r.status_code)\n\n"
            "Important points:\n"
            "• Always set a timeout so the program never hangs\n"
            "• Check the status_code before reading the data — if it is not 200, do not continue\n"
            "• If the API needs a key, store it in an environment variable, not in the code\n\n"
            "Try another API — GitHub (no key, but it has an hourly request limit):\n"
            "r = requests.get(\"https://api.github.com/users/octocat\", timeout=10)\n"
            "if r.status_code == 200:\n"
            "    data = r.json()\n"
            "    print(data[\"login\"])  # octocat\n"
            "    print(data[\"public_repos\"])  # number of public projects\n"
            "else:\n"
            "    print(\"GitHub is not available right now, try again later\")\n\n"
            "Today's task: write a program that gets the number of followers of any username from the GitHub API."
        ),
    },
    {
        "title_ar": "الدرس 18: قواعد البيانات (SQLite)",
        "title_en": "Lesson 18: Databases (SQLite)",
        "ar": (
            "🗄️ الدرس 18: قواعد البيانات (SQLite)\n\n"
            "لما البيانات تكبر، الملفات النصية مش كفاية — هنا بتيجي قواعد البيانات.\n\n"
            "import sqlite3\n\n"
            "db = sqlite3.connect(\"tasks.db\")\n"
            "db.execute(\"CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)\")\n"
            "db.execute(\"INSERT INTO tasks (title, done) VALUES (?, ?)\", (\"غيّر كلمة السر\", 0))\n"
            "db.commit()\n\n"
            "for row in db.execute(\"SELECT id, title, done FROM tasks\"):\n"
            "    print(row)\n"
            "db.close()\n\n"
            "نقاط مهمة:\n"
            "• علامة ? بتحميك من حقن SQL — متلصقش بيانات المستخدم في الاستعلام بنفسك\n"
            "• commit() بتحفظ التغييرات، ومن غيرها مفيش حاجة بتتحفظ\n"
            "• SQLite ملف واحد، مش محتاج سيرفر — مثالي للمشاريع الصغيرة\n\n"
            "واجب النهاردة: اعمل قاعدة بيانات مهام، وضيف 3 مهام، واطبع المهام اللي لسه مش مخلّصة (done = 0)."
        ),
        "en": (
            "🗄️ Lesson 18: Databases (SQLite)\n\n"
            "When data grows, text files are not enough — that is where databases come in.\n\n"
            "import sqlite3\n\n"
            "db = sqlite3.connect(\"tasks.db\")\n"
            "db.execute(\"CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)\")\n"
            "db.execute(\"INSERT INTO tasks (title, done) VALUES (?, ?)\", (\"Change password\", 0))\n"
            "db.commit()\n\n"
            "for row in db.execute(\"SELECT id, title, done FROM tasks\"):\n"
            "    print(row)\n"
            "db.close()\n\n"
            "Important points:\n"
            "• The ? placeholder protects you from SQL injection — never paste user data into the query yourself\n"
            "• commit() saves the changes; without it nothing is saved\n"
            "• SQLite is a single file, no server needed — perfect for small projects\n\n"
            "Today's task: make a tasks database, add 3 tasks, and print the tasks that are not done yet (done = 0)."
        ),
    },
    {
        "title_ar": "الدرس 19: الاختبارات (testing)",
        "title_en": "Lesson 19: Testing",
        "ar": (
            "🧪 الدرس 19: الاختبارات (testing)\n\n"
            "الاختبار هو كود بيجرّب كودك — عشان تتأكد إنه شغال صح قبل ما حد تاني يستخدمه.\n\n"
            "أبسط اختبار: assert\n"
            "def is_strong(password):\n"
            "    return len(password) >= 12\n\n"
            "assert is_strong(\"123\") == False\n"
            "assert is_strong(\"Ahmed@2024#Z\") == True\n"
            "print(\"كل الاختبارات عدّت ✅\")\n\n"
            "لو assert فشل، البرنامج بيقف ويقولك فين المشكلة بالظبط.\n\n"
            "اختبارات منظمة بـ unittest:\n"
            "import unittest\n\n"
            "class TestPassword(unittest.TestCase):\n"
            "    def test_short(self):\n"
            "        self.assertFalse(is_strong(\"123\"))\n\n"
            "    def test_long(self):\n"
            "        self.assertTrue(is_strong(\"Ahmed@2024#Z\"))\n\n"
            "unittest.main()\n\n"
            "💡 القاعدة: كل دالة مهمة ليها اختبار — والاختبار بيتكتب قبل ما تنسى الكود بيعمل إيه.\n\n"
            "واجب النهاردة: اكتب اختبارين لدالة بتجمع رقمين: واحد بأرقام عادية، وواحد بصفر."
        ),
        "en": (
            "🧪 Lesson 19: Testing\n\n"
            "A test is code that tries your code — so you know it works before anyone else uses it.\n\n"
            "The simplest test: assert\n"
            "def is_strong(password):\n"
            "    return len(password) >= 12\n\n"
            "assert is_strong(\"123\") == False\n"
            "assert is_strong(\"Ahmed@2024#Z\") == True\n"
            "print(\"All tests passed ✅\")\n\n"
            "If an assert fails, the program stops and tells you exactly where the problem is.\n\n"
            "Organized tests with unittest:\n"
            "import unittest\n\n"
            "class TestPassword(unittest.TestCase):\n"
            "    def test_short(self):\n"
            "        self.assertFalse(is_strong(\"123\"))\n\n"
            "    def test_long(self):\n"
            "        self.assertTrue(is_strong(\"Ahmed@2024#Z\"))\n\n"
            "unittest.main()\n\n"
            "💡 The rule: every important function gets a test — and tests are written before you forget what the code does.\n\n"
            "Today's task: write two tests for a function that adds two numbers: one with normal numbers, one with zero."
        ),
    },
    {
        "title_ar": "الدرس 20: البيئات الافتراضية (venv)",
        "title_en": "Lesson 20: Virtual environments (venv)",
        "ar": (
            "📦 الدرس 20: البيئات الافتراضية (venv)\n\n"
            "كل مشروع ليه مكتباته وإصداراته — والبيئة الافتراضية بتفصل مشروعك عن باقي الجهاز.\n\n"
            "في التيرمينال، جوه مجلد مشروعك:\n"
            "python3 -m venv venv\n\n"
            "(على ويندوز اكتب python بدل python3)\n\n"
            "التفعيل:\n"
            "• ويندوز: venv\\Scripts\\activate\n"
            "• ماك/لينكس: source venv/bin/activate\n\n"
            "بعد التفعيل، أي pip install بيثبّت جوه المشروع بس:\n"
            "pip install requests\n"
            "pip freeze > requirements.txt  # بتحفظ قائمة المكتبات\n\n"
            "وأي حد ياخد مشروعك يعمل:\n"
            "pip install -r requirements.txt\n\n"
            "💡 ليه مهم؟ لو مشروع محتاج requests إصدار 2 ومشروع تاني محتاج إصدار 3، كل واحد ياخد نسخته من غير ما يخرب التاني.\n\n"
            "واجب النهاردة: اعمل بيئة افتراضية لمشروع مدير كلمات السر، وثبّت فيها أي مكتبة محتاجها."
        ),
        "en": (
            "📦 Lesson 20: Virtual environments (venv)\n\n"
            "Every project has its own libraries and versions — a virtual environment separates your project from the rest of the machine.\n\n"
            "In the terminal, inside your project folder:\n"
            "python3 -m venv venv\n\n"
            "(On Windows type python instead of python3)\n\n"
            "Activate it:\n"
            "• Windows: venv\\Scripts\\activate\n"
            "• Mac/Linux: source venv/bin/activate\n\n"
            "After activation, any pip install goes into the project only:\n"
            "pip install requests\n"
            "pip freeze > requirements.txt  # saves the list of libraries\n\n"
            "And anyone who takes your project runs:\n"
            "pip install -r requirements.txt\n\n"
            "💡 Why does it matter? If one project needs requests version 2 and another needs version 3, each gets its own copy without breaking the other.\n\n"
            "Today's task: make a virtual environment for the password-manager project, and install any library it needs."
        ),
    },
    {
        "title_ar": "الدرس 21: مشروع أمني — فاحص سلامة الملفات",
        "title_en": "Lesson 21: Security project — file-integrity checker",
        "ar": (
            "🔍 الدرس 21: مشروع أمني — فاحص سلامة الملفات\n\n"
            "المشروع ده دفاعي 100%: برنامج بيحسب \"بصمة\" لكل ملف مهم عندك، وبعدين يفحص لو أي ملف اتغيّر من غير ما تعرف.\n\n"
            "import hashlib\n"
            "import json\n"
            "import os\n\n"
            "def fingerprint(path):\n"
            "    h = hashlib.sha256()\n"
            "    with open(path, \"rb\") as f:\n"
            "        h.update(f.read())\n"
            "    return h.hexdigest()\n\n"
            "# أول مرة: احفظ البصمات\n"
            "files = [\"notes.txt\", \"vault.json\"]\n"
            "saved = {p: fingerprint(p) for p in files if os.path.exists(p)}\n"
            "with open(\"fingerprints.json\", \"w\") as f:\n"
            "    json.dump(saved, f)\n"
            "print(\"اتحفظت بصمات\", len(saved), \"ملف ✅\")\n\n"
            "# بعدين: افحص\n"
            "with open(\"fingerprints.json\") as f:\n"
            "    saved = json.load(f)\n"
            "for path, old in saved.items():\n"
            "    if not os.path.exists(path):\n"
            "        print(\"❌ اتمسح:\", path)\n"
            "    elif fingerprint(path) != old:\n"
            "        print(\"⚠️ اتغيّر:\", path)\n"
            "    else:\n"
            "        print(\"✅ سليم:\", path)\n\n"
            "💡 دي فكرة برامج حماية حقيقية — أي فيروس بيعدّل ملف، الفحص بيكشفه.\n\n"
            "ملحوظة: الملفين notes.txt و vault.json عملتهم في الدروس اللي فاتت (12 و 15) — لو مش موجودين عندك، اعملهم الأول.\n\n"
            "واجب النهاردة: شغّل البرنامج على الملفين، وبعدين عدّل واحد فيهم وشوف الفحص بيكشفه ولا لأ."
        ),
        "en": (
            "🔍 Lesson 21: Security project — file-integrity checker\n\n"
            "This project is 100% defensive: a program that computes a \"fingerprint\" for each important file, then checks if any file changed without you knowing.\n\n"
            "import hashlib\n"
            "import json\n"
            "import os\n\n"
            "def fingerprint(path):\n"
            "    h = hashlib.sha256()\n"
            "    with open(path, \"rb\") as f:\n"
            "        h.update(f.read())\n"
            "    return h.hexdigest()\n\n"
            "# First time: save the fingerprints\n"
            "files = [\"notes.txt\", \"vault.json\"]\n"
            "saved = {p: fingerprint(p) for p in files if os.path.exists(p)}\n"
            "with open(\"fingerprints.json\", \"w\") as f:\n"
            "    json.dump(saved, f)\n"
            "print(\"Saved fingerprints for\", len(saved), \"files ✅\")\n\n"
            "# Later: check\n"
            "with open(\"fingerprints.json\") as f:\n"
            "    saved = json.load(f)\n"
            "for path, old in saved.items():\n"
            "    if not os.path.exists(path):\n"
            "        print(\"❌ Deleted:\", path)\n"
            "    elif fingerprint(path) != old:\n"
            "        print(\"⚠️ Changed:\", path)\n"
            "    else:\n"
            "        print(\"✅ OK:\", path)\n\n"
            "💡 This is how real protection software works — any virus that modifies a file gets caught by the check.\n\n"
            "Note: notes.txt and vault.json are files you made in earlier lessons (12 and 15) — if you do not have them, make them first.\n\n"
            "Today's task: run the program on the two files, then change one of them and see if the check catches it."
        ),
    },
    {
        "title_ar": "الدرس 22: المشروع الختامي — أداة \"حارس حساباتي\"",
        "title_en": "Lesson 22: Capstone project — \"My account guard\" tool",
        "ar": (
            "🎓 الدرس 22: المشروع الختامي — أداة \"حارس حساباتي\"\n\n"
            "آخر درس في بايثون — هنجمع كل حاجة في أداة واحدة ليها قائمة (menu) بتعمل حاجات مفيدة.\n\n"
            "الأداة بتعمل:\n"
            "1. فحص قوة كلمة السر (من الدرس 5 + 7)\n"
            "2. توليد كلمة سر قوية (من الدرس 8)\n\n"
            "import random\n"
            "import string\n\n"
            "def is_strong(p):\n"
            "    return len(p) >= 12\n\n"
            "def make_password(length=14):\n"
            "    chars = string.ascii_letters + string.digits + \"!@#$%\"\n"
            "    return \"\".join(random.choice(chars) for _ in range(length))\n\n"
            "while True:\n"
            "    print(\"\\n1- افحص كلمة سر | 2- ولّد كلمة سر | 3- خروج\")\n"
            "    choice = input(\"اختيارك: \")\n"
            "    if choice == \"1\":\n"
            "        p = input(\"كلمة السر: \")\n"
            "        print(\"قوية ✅\" if is_strong(p) else \"ضعيفة ❌\")\n"
            "    elif choice == \"2\":\n"
            "        print(\"كلمة السر:\", make_password())\n"
            "    elif choice == \"3\":\n"
            "        print(\"مع السلامة 👋\")\n"
            "        break\n"
            "    else:\n"
            "        print(\"اختيار مش صحيح\")\n\n"
            "🎉 مبروك يا بطل! خلصت 22 درس بايثون — من أول print لحد برنامج كامل بقائمة. دلوقتي تقدر تبني أدواتك بنفسك.\n\n"
            "واجب النهاردة: شغّل الأداة وجرّب التلات اختيارات، وبعدين زوّد اختيار رابع: \"افحص كلمة سر من ملف\" — اقرأ كلمة السر من ملف نصي وافحصها.\n\n"
            "اللي جاي: مسار روبي — لغة تانية بنفس الأساسيات. اكتب /lesson عشان تبدأ روبي 💎"
        ),
        "en": (
            "🎓 Lesson 22: Capstone project — \"My account guard\" tool\n\n"
            "The last Python lesson — let's combine everything into one tool with a menu that does useful things.\n\n"
            "The tool does:\n"
            "1. Check password strength (from lessons 5 + 7)\n"
            "2. Generate a strong password (from lesson 8)\n\n"
            "import random\n"
            "import string\n\n"
            "def is_strong(p):\n"
            "    return len(p) >= 12\n\n"
            "def make_password(length=14):\n"
            "    chars = string.ascii_letters + string.digits + \"!@#$%\"\n"
            "    return \"\".join(random.choice(chars) for _ in range(length))\n\n"
            "while True:\n"
            "    print(\"\\n1- Check a password | 2- Generate a password | 3- Exit\")\n"
            "    choice = input(\"Your choice: \")\n"
            "    if choice == \"1\":\n"
            "        p = input(\"Password: \")\n"
            "        print(\"Strong ✅\" if is_strong(p) else \"Weak ❌\")\n"
            "    elif choice == \"2\":\n"
            "        print(\"Password:\", make_password())\n"
            "    elif choice == \"3\":\n"
            "        print(\"Goodbye 👋\")\n"
            "        break\n"
            "    else:\n"
            "        print(\"Invalid choice\")\n\n"
            "🎉 Congratulations, champion! You finished 22 Python lessons — from your first print to a full program with a menu. Now you can build your own tools.\n\n"
            "Today's task: run the tool and try all three choices, then add a fourth choice: \"check a password from a file\" — read the password from a text file and check it.\n\n"
            "Coming next: the Ruby track — another language with the same basics. Send /lesson to start Ruby 💎"
        ),
    },
]

RUBY_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه روبي؟",
        "title_en": "Lesson 1: What is Ruby?",
        "ar": (
            "💎 الدرس 1: يعني إيه روبي؟\n\n"
            "روبي (Ruby) لغة برمجة مشهورة بسهولتها، وكودها بيتقري زي الإنجليزي. هي اللي مبني عليها إطار العمل الشهير Rails اللي بيشغّل مواقع كبيرة.\n\n"
            "📥 جهّز جهازك:\n"
            "• ويندوز: نزّل RubyInstaller من rubyinstaller.org\n"
            "• ماك: اكتب في التيرمينال brew install ruby\n"
            "• لينكس: sudo apt install ruby\n\n"
            "اتأكد إنها اتثبّتت:\n"
            "ruby -v\n\n"
            "💻 أول برنامج ليك — اكتب السطر ده في ملف اسمه hello.rb وشغّله بـ ruby hello.rb:\n"
            "puts \"أهلاً بالعالم\"\n\n"
            "هيطبع على الشاشة: أهلاً بالعالم 🎉\n\n"
            "💡 في روبي، puts يعني \"اطبع\" — زي print في بايثون.\n\n"
            "📱 على الموبايل (من غير تثبيت):\n"
            "• افتح المتصفح وادخل على jdoodle.com — اختار Ruby\n"
            "• اكتب الكود في المحرر ودوس Execute — هيشتغل من غير ما تثبّت حاجة\n"
            "• ده أسهل طريق تجرّب بيه روبي من موبايلك\n\n"
            "💻 عشان تفتح الطرفية على ويندوز: افتح قائمة Start واكتب cmd ودوس Enter — وبعدين اكتب ruby hello.rb.\n\n"
            "واجب النهاردة: ثبّت روبي، وشغّل أول puts بتاعك، وجرّب تغيّر الكلام اللي بين علامات التنصيص."
        ),
        "en": (
            "💎 Lesson 1: What is Ruby?\n\n"
            "Ruby is a programming language famous for being easy, and its code reads like English. It is the language behind the famous Rails framework that powers big websites.\n\n"
            "📥 Set up your device:\n"
            "• Windows: download RubyInstaller from rubyinstaller.org\n"
            "• Mac: type in the terminal brew install ruby\n"
            "• Linux: sudo apt install ruby\n\n"
            "Make sure it installed:\n"
            "ruby -v\n\n"
            "💻 Your first program — write this line in a file called hello.rb and run it with ruby hello.rb:\n"
            "puts \"Hello, world\"\n\n"
            "It prints on the screen: Hello, world 🎉\n\n"
            "💡 In Ruby, puts means \"print\" — like print in Python.\n\n"
            "📱 On a phone (no install needed):\n"
            "• Open your browser and go to jdoodle.com — choose Ruby\n"
            "• Type your code in the editor and press Execute — it runs without installing anything\n"
            "• This is the easiest way to try Ruby from your phone\n\n"
            "💻 To open the terminal on Windows: open the Start menu, type cmd and press Enter — then type ruby hello.rb.\n\n"
            "Today's task: install Ruby, run your first puts, and try changing the text inside the quotes."
        ),
    },
    {
        "title_ar": "الدرس 2: المتغيرات",
        "title_en": "Lesson 2: Variables",
        "ar": (
            "📦 الدرس 2: المتغيرات\n\n"
            "المتغير في روبي زي بايثون بالظبط — علبة بتحط فيها قيمة وتسميها.\n\n"
            "name = \"خالد\"\n"
            "age = 30\n"
            "height = 175.5\n"
            "married = false\n\n"
            "⚠️ لاحظ: في روبي بنكتب false بحروف صغيرة، مش False زي بايثون. و true كمان صغيرة.\n\n"
            "الطباعة مع المتغيرات:\n"
            "puts \"اسمي #{name} وعمري #{age}\"\n\n"
            "ده اسمه string interpolation — بتحط المتغير جوه النص بين #{ } وروبي بتبدّله بقيمته.\n\n"
            "أنواع البيانات:\n"
            "• نص (String): بين علامتي تنصيص\n"
            "• رقم صحيح (Integer): 30\n"
            "• رقم عشري (Float): 175.5\n"
            "• صح/غلط: true أو false\n\n"
            "واجب النهاردة: اعمل متغيرات لاسمك وعمرك ومدينتك، واطبعهم في جملة واحدة باستخدام #{ }."
        ),
        "en": (
            "📦 Lesson 2: Variables\n\n"
            "A variable in Ruby is exactly like in Python — a box where you store a value and give it a name.\n\n"
            "name = \"Khaled\"\n"
            "age = 30\n"
            "height = 175.5\n"
            "married = false\n\n"
            "⚠️ Note: in Ruby we write false in lowercase, not False like Python. And true is lowercase too.\n\n"
            "Printing with variables:\n"
            "puts \"My name is #{name} and I am #{age}\"\n\n"
            "This is called string interpolation — you put the variable inside the text between #{ } and Ruby replaces it with its value.\n\n"
            "Data types:\n"
            "• Text (String): inside quotes\n"
            "• Whole number (Integer): 30\n"
            "• Decimal number (Float): 175.5\n"
            "• True/False: true or false\n\n"
            "Today's task: make variables for your name, age and city, and print them in one sentence using #{ }."
        ),
    },
    {
        "title_ar": "الدرس 3: الإدخال والحساب",
        "title_en": "Lesson 3: Input and math",
        "ar": (
            "🧮 الدرس 3: الإدخال والحساب\n\n"
            "في روبي، gets بتقرأ اللي المستخدم يكتبه.\n\n"
            "print \"اسمك إيه؟ \"\n"
            "name = gets.chomp\n"
            "puts \"أهلاً #{name}\"\n\n"
            "💡 chomp بتشيل سطر جديد اللي في آخر الإدخال — من غيرها الاسم هيبقى فيه سطر فاضي.\n\n"
            "⚠️ gets بترجع نص دايمًا. لو عايز رقم، حوّله:\n"
            "print \"عمرك كام؟ \"\n"
            "age = gets.chomp.to_i\n"
            "puts \"السنة الجاية هيبقى عمرك #{age + 1}\"\n\n"
            "العمليات الحسابية:\n"
            "• + جمع، - طرح، * ضرب، / قسمة\n"
            "• % باقي القسمة، ** أس\n"
            "• مثال: 10 % 3 = 1 ، 2 ** 3 = 8\n\n"
            "واجب النهاردة: اعمل آلة حاسبة صغيرة تسأل عن رقمين وتطبع مجموعهم وحاصل ضربهم."
        ),
        "en": (
            "🧮 Lesson 3: Input and math\n\n"
            "In Ruby, gets reads what the user types.\n\n"
            "print \"What is your name? \"\n"
            "name = gets.chomp\n"
            "puts \"Hello #{name}\"\n\n"
            "💡 chomp removes the newline at the end of the input — without it the name would have an empty line.\n\n"
            "⚠️ gets always returns text. If you want a number, convert it:\n"
            "print \"How old are you? \"\n"
            "age = gets.chomp.to_i\n"
            "puts \"Next year you will be #{age + 1}\"\n\n"
            "Math operators:\n"
            "• + add, - subtract, * multiply, / divide\n"
            "• % remainder, ** power\n"
            "• Example: 10 % 3 = 1, 2 ** 3 = 8\n\n"
            "Today's task: make a small calculator that asks for two numbers and prints their sum and product."
        ),
    },
    {
        "title_ar": "الدرس 4: الشروط (if)",
        "title_en": "Lesson 4: Conditions (if)",
        "ar": (
            "🚦 الدرس 4: الشروط (if)\n\n"
            "في روبي الشروط شبه بايثون، بس بدل elif بنكتب elsif، وبدل المسافات بنقفل بـ end.\n\n"
            "print \"اكتب كلمة السر: \"\n"
            "password = gets.chomp\n"
            "if password.length >= 8\n"
            "  puts \"كلمة السر قوية ✅\"\n"
            "else\n"
            "  puts \"كلمة السر قصيرة ❌ لازم 8 حروف على الأقل\"\n"
            "end\n\n"
            "مع elsif:\n"
            "print \"عمرك كام؟ \"\n"
            "age = gets.chomp.to_i\n"
            "if age >= 18\n"
            "  puts \"انت بالغ\"\n"
            "elsif age >= 13\n"
            "  puts \"انت مراهق\"\n"
            "else\n"
            "  puts \"انت طفل\"\n"
            "end\n\n"
            "المقارنات: == يساوي، != مش يساوي، > أكبر من، < أصغر من، && (و)، || (أو)، ! (مش).\n\n"
            "واجب النهاردة: اعمل برنامج يفحص قوة كلمة السر: أقل من 8 \"ضعيفة\"، من 8 لـ 11 \"متوسطة\"، 12 أو أكتر \"قوية\"."
        ),
        "en": (
            "🚦 Lesson 4: Conditions (if)\n\n"
            "Conditions in Ruby are like Python, but instead of elif we write elsif, and instead of indentation we close with end.\n\n"
            "print \"Enter a password: \"\n"
            "password = gets.chomp\n"
            "if password.length >= 8\n"
            "  puts \"Strong password ✅\"\n"
            "else\n"
            "  puts \"Too short ❌ at least 8 characters\"\n"
            "end\n\n"
            "With elsif:\n"
            "print \"How old are you? \"\n"
            "age = gets.chomp.to_i\n"
            "if age >= 18\n"
            "  puts \"You are an adult\"\n"
            "elsif age >= 13\n"
            "  puts \"You are a teenager\"\n"
            "else\n"
            "  puts \"You are a child\"\n"
            "end\n\n"
            "Comparisons: == equal, != not equal, > greater than, < less than, && (and), || (or), ! (not).\n\n"
            "Today's task: write a program that checks password strength: under 8 \"weak\", 8-11 \"medium\", 12+ \"strong\"."
        ),
    },
    {
        "title_ar": "الدرس 5: الحلقات (loops)",
        "title_en": "Lesson 5: Loops",
        "ar": (
            "🔁 الدرس 5: الحلقات (loops)\n\n"
            "في روبي فيه طرق كتير للتكرار — وأشهرها times و while و each.\n\n"
            "5.times do |i|\n"
            "  puts \"أهلاً #{i}\"\n"
            "end\n\n"
            "وهيطبع \"أهلاً\" 5 مرات مع الأرقام 0 لحد 4.\n\n"
            "الحلقة while بتكرر لحد ما الشرط يبقى غلط:\n"
            "count = 3\n"
            "while count > 0\n"
            "  puts count\n"
            "  count -= 1\n"
            "end\n"
            "puts \"انطلق! 🚀\"\n\n"
            "الحلقة each بتلف على عناصر القائمة:\n"
            "friends = [\"أحمد\", \"محمد\", \"سارة\"]\n"
            "friends.each do |f|\n"
            "  puts \"أهلاً #{f}\"\n"
            "end\n\n"
            "💡 احذر الحلقة اللي مبتخلصش (while true من غير break) — هتفضل شغالة على طول!\n\n"
            "واجب النهاردة: اعمل برنامج يطبع جدول ضرب رقم تختاره، من 1 لحد 10."
        ),
        "en": (
            "🔁 Lesson 5: Loops\n\n"
            "Ruby has many ways to repeat — the most famous are times, while and each.\n\n"
            "5.times do |i|\n"
            "  puts \"Hello #{i}\"\n"
            "end\n\n"
            "This prints \"Hello\" 5 times with numbers 0 to 4.\n\n"
            "The while loop repeats until the condition is false:\n"
            "count = 3\n"
            "while count > 0\n"
            "  puts count\n"
            "  count -= 1\n"
            "end\n"
            "puts \"Go! 🚀\"\n\n"
            "The each loop goes over the elements of a list:\n"
            "friends = [\"Ahmed\", \"Mohamed\", \"Sara\"]\n"
            "friends.each do |f|\n"
            "  puts \"Hello #{f}\"\n"
            "end\n\n"
            "💡 Beware the loop that never ends (while true without break) — it runs forever!\n\n"
            "Today's task: write a program that prints the multiplication table of a number you choose, from 1 to 10."
        ),
    },
    {
        "title_ar": "الدرس 6: المصفوفات والدوال",
        "title_en": "Lesson 6: Arrays and methods",
        "ar": (
            "📋 الدرس 6: المصفوفات والدوال\n\n"
            "المصفوفة (array) في روبي زي القائمة في بايثون:\n\n"
            "friends = [\"أحمد\", \"محمد\", \"سارة\"]\n"
            "puts friends[0]  # أحمد\n"
            "friends.push(\"علي\")  # يضيف علي في الآخر\n"
            "puts friends.length  # 4\n\n"
            "والدالة (method) في روبي بتتكتب بـ def:\n\n"
            "def strong?(password)\n"
            "  password.length >= 12\n"
            "end\n\n"
            "puts strong?(\"123\")  # false\n"
            "puts strong?(\"Ahmed@2024#Z\")  # true\n\n"
            "💡 في روبي، آخر سطر في الدالة هو الناتج تلقائيًا — مش لازم تكتب return.\n"
            "وعلامة الاستفهام في اسم الدالة معناها \"السؤال ده إجابته صح ولا غلط؟\" — عادة حلوة في روبي.\n\n"
            "واجب النهاردة: اعمل دالة بتاخد كلمة سر وترجع \"قوية\" أو \"ضعيفة\"، وجرّبها على 3 كلمات سر مختلفة."
        ),
        "en": (
            "📋 Lesson 6: Arrays and methods\n\n"
            "An array in Ruby is like a list in Python:\n\n"
            "friends = [\"Ahmed\", \"Mohamed\", \"Sara\"]\n"
            "puts friends[0]  # Ahmed\n"
            "friends.push(\"Ali\")  # adds Ali at the end\n"
            "puts friends.length  # 4\n\n"
            "A method in Ruby is written with def:\n\n"
            "def strong?(password)\n"
            "  password.length >= 12\n"
            "end\n\n"
            "puts strong?(\"123\")  # false\n"
            "puts strong?(\"Ahmed@2024#Z\")  # true\n\n"
            "💡 In Ruby, the last line of a method is automatically the result — you do not need to write return.\n"
            "And the question mark in a method name means \"is the answer to this question true or false?\" — a nice Ruby habit.\n\n"
            "Today's task: write a method that takes a password and returns \"strong\" or \"weak\", and test it with 3 different passwords."
        ),
    },
    {
        "title_ar": "الدرس 7: مشروعك الأول — لعبة تخمين الرقم",
        "title_en": "Lesson 7: Your first project — number-guessing game",
        "ar": (
            "🎓 الدرس 7: مشروعك الأول — لعبة تخمين الرقم\n\n"
            "هنجمع كل اللي اتعلمناه في لعبة: الكمبيوتر يختار رقم سري، وانت تحاول تخمّنه.\n\n"
            "secret = rand(1..100)\n"
            "puts \"خمّن رقم من 1 لـ 100!\"\n\n"
            "loop do\n"
            "  print \"تخمينك: \"\n"
            "  guess = gets.chomp.to_i\n"
            "  if guess == secret\n"
            "    puts \"🎉 صح! الرقم كان #{secret}\"\n"
            "    break\n"
            "  elsif guess < secret\n"
            "    puts \"أكبر من كده ⬆️\"\n"
            "  else\n"
            "    puts \"أصغر من كده ⬇️\"\n"
            "  end\n"
            "end\n\n"
            "إيه اللي حصل هنا؟\n"
            "• rand(1..100) بيختار رقم عشوائي\n"
            "• loop do بيكرر لحد ما نعمل break\n"
            "• كل تخمين بيقولك أكبر ولا أصغر، لحد ما توصل للرقم\n\n"
            "🎉 مبروك! خلصت أول 7 دروس روبي، وعملت أول لعبة حقيقية.\n\n"
            "واجب النهاردة: شغّل اللعبة 3 مرات، وبعدين عدّلها: خلي الرقم من 1 لـ 50 بدل 100.\n\n"
            "اللي جاي: دروس روبي متقدمة قريبًا. اكتب /courses عشان تشوف كل الدورات 💎"
        ),
        "en": (
            "🎓 Lesson 7: Your first project — number-guessing game\n\n"
            "Let's combine everything into a game: the computer picks a secret number, and you try to guess it.\n\n"
            "secret = rand(1..100)\n"
            "puts \"Guess a number from 1 to 100!\"\n\n"
            "loop do\n"
            "  print \"Your guess: \"\n"
            "  guess = gets.chomp.to_i\n"
            "  if guess == secret\n"
            "    puts \"🎉 Correct! The number was #{secret}\"\n"
            "    break\n"
            "  elsif guess < secret\n"
            "    puts \"Bigger than that ⬆️\"\n"
            "  else\n"
            "    puts \"Smaller than that ⬇️\"\n"
            "  end\n"
            "end\n\n"
            "What happened here?\n"
            "• rand(1..100) picks a random number\n"
            "• loop do repeats until we call break\n"
            "• Every guess tells you bigger or smaller, until you reach the number\n\n"
            "🎉 Congratulations! You finished your first 7 Ruby lessons and built your first real game.\n\n"
            "Today's task: play the game 3 times, then change it: make the number from 1 to 50 instead of 100.\n\n"
            "Coming next: advanced Ruby lessons soon. Send /courses to see all courses 💎"
        ),
    },
]

NETWORKS_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه شبكة؟",
        "title_en": "Lesson 1: What is a network?",
        "ar": (
            "🌐 الدرس 1: يعني إيه شبكة؟\n\n"
            "الشبكة يعني أجهزة متوصلة ببعض وبتكلم بعض: موبايلك واللابتوب والتلفزيون والطابعة في بيتك — كلهم على شبكة واحدة.\n\n"
            "نوعين لازم تعرفهم:\n"
            "• الشبكة المحلية (LAN): الأجهزة اللي في بيتك أو مكتبك، متوصلة بالراوتر\n"
            "• الإنترنت: شبكات كتير متوصلة ببعض — شبكة بيتك + شبكة جوجل + شبكة فيسبوك، كلهم شبكة واحدة كبيرة\n\n"
            "مثال: لما تبعت صورة من موبايلك للابتوب على نفس الواي فاي، الصورة بتسافر جوه شبكة بيتك بس.\n"
            "ولما تبعتها لصاحبك في بلد تانية، الصورة بتسافر من شبكتك للإنترنت لحد شبكته.\n\n"
            "💡 كل اللي هنتعلمه في الأمن السيبراني والبرمجة مبني على الشبكات — افهم الشبكة، تفهم كل حاجة.\n\n"
            "واجب النهاردة: عدّ الأجهزة المتصلة بواي فاي بيتك (موبايلات، لابتوب، تلفزيون، طابعة...) واكتبهم في ورقة."
        ),
        "en": (
            "🌐 Lesson 1: What is a network?\n\n"
            "A network means devices connected to each other and talking to each other: your phone, laptop, TV and printer at home — all on one network.\n\n"
            "Two types you must know:\n"
            "• Local network (LAN): the devices in your home or office, connected to the router\n"
            "• The internet: many networks connected together — your home network + Google's network + Facebook's network, all one big network\n\n"
            "Example: when you send a photo from your phone to your laptop on the same Wi-Fi, the photo travels inside your home network only.\n"
            "And when you send it to a friend in another country, the photo travels from your network across the internet to their network.\n\n"
            "💡 Everything in cybersecurity and programming is built on networks — understand the network and you understand everything.\n\n"
            "Today's task: count the devices connected to your home Wi-Fi (phones, laptop, TV, printer...) and write them on a paper."
        ),
    },
    {
        "title_ar": "الدرس 2: عنوان الـ IP",
        "title_en": "Lesson 2: The IP address",
        "ar": (
            "🔢 الدرس 2: عنوان الـ IP\n\n"
            "الـ IP هو عنوان الجهاز على الشبكة — زي عنوان البيت بالظبط. من غير عنوان، مفيش حاجة توصل.\n\n"
            "شكله كده: 192.168.1.5 — أربع أرقام بينهم نقط.\n\n"
            "نوعين:\n"
            "• خاص (Private): عنوان جهازك جوه بيتك، زي 192.168.1.5 — بيشوفه الراوتر بس\n"
            "• عام (Public): عنوان الراوتر بتاعك على الإنترنت — ده اللي بيشوفه العالم برّه\n\n"
            "🔍 اعرف عنوانك بنفسك:\n"
            "• على الكمبيوتر (ويندوز): افتح cmd واكتب ipconfig — دوّر على IPv4 Address\n"
            "• على الموبايل (أندرويد): الإعدادات ← الواي فاي ← دوس على الشبكة المتصلة — هتلاقي عنوان IP\n\n"
            "واجب النهاردة: اعرف عنوان الـ IP بتاع موبايلك واكتبه في ملاحظة."
        ),
        "en": (
            "🔢 Lesson 2: The IP address\n\n"
            "The IP is the address of a device on the network — exactly like a home address. Without an address, nothing arrives.\n\n"
            "It looks like this: 192.168.1.5 — four numbers separated by dots.\n\n"
            "Two types:\n"
            "• Private: your device's address inside your home, like 192.168.1.5 — only the router sees it\n"
            "• Public: your router's address on the internet — this is what the outside world sees\n\n"
            "🔍 Find your own address:\n"
            "• On a computer (Windows): open cmd and type ipconfig — look for IPv4 Address\n"
            "• On a phone (Android): Settings → Wi-Fi → tap the connected network — you will find the IP address\n\n"
            "Today's task: find your phone's IP address and write it in a note."
        ),
    },
    {
        "title_ar": "الدرس 3: الراوتر والواي فاي",
        "title_en": "Lesson 3: The router and Wi-Fi",
        "ar": (
            "📶 الدرس 3: الراوتر والواي فاي\n\n"
            "الراوتر هو الجهاز اللي موصّل شبكة بيتك بالإنترنت، وبيوزّع الواي فاي على أجهزتك.\n\n"
            "إزاي بيشتغل؟\n"
            "• سلك الإنترنت بيدخل الراوتر من شركة الاتصالات\n"
            "• الراوتر بيعمل شبكة واي فاي في بيتك، وكل جهاز بيتصل بيها بكلمة سر\n"
            "• الراوتر بيدي كل جهاز عنوان IP (من الدرس اللي فات) وبيوصّل البيانات بينهم وبين الإنترنت\n\n"
            "📡 الواي فاي نوعين:\n"
            "• 2.4GHz: بيوصل أبعد (أوض بعيدة)، بس أبطأ\n"
            "• 5GHz: أسرع بكتير، بس مداه أقصر (نفس الأوضة تقريبًا)\n\n"
            "💡 اسم الشبكة اللي بتشوفه في موبايلك اسمه SSID — وغالبًا الراوتر بيعمل شبكتين، واحدة 2.4 وواحدة 5G.\n\n"
            "واجب النهاردة: بص على الراوتر بتاعك — شوف اسمه وموديله، وشوف موبايلك متصل على 2.4 ولا 5G."
        ),
        "en": (
            "📶 Lesson 3: The router and Wi-Fi\n\n"
            "The router is the device that connects your home network to the internet and shares Wi-Fi with your devices.\n\n"
            "How does it work?\n"
            "• The internet cable enters the router from your provider\n"
            "• The router makes a Wi-Fi network in your home, and every device connects with a password\n"
            "• The router gives every device an IP address (from the last lesson) and carries data between them and the internet\n\n"
            "📡 Wi-Fi has two types:\n"
            "• 2.4GHz: reaches farther (distant rooms), but slower\n"
            "• 5GHz: much faster, but shorter range (almost the same room)\n\n"
            "💡 The network name you see on your phone is called SSID — and the router usually makes two networks, one 2.4 and one 5G.\n\n"
            "Today's task: look at your router — see its name and model, and check whether your phone is connected to 2.4 or 5G."
        ),
    },
    {
        "title_ar": "الدرس 4: الـ DNS",
        "title_en": "Lesson 4: DNS",
        "ar": (
            "📖 الدرس 4: الـ DNS\n\n"
            "الـ DNS هو دليل تليفونات الإنترنت: بيحوّل الاسم اللي بتكتبه (زي facebook.com) لعنوان IP اللي الكمبيوتر يفهمه.\n\n"
            "إزاي بيحصل؟\n"
            "1. بتكتب facebook.com في المتصفح\n"
            "2. جهازك يسأل خادم الـ DNS: \"الاسم ده عنوانه إيه؟\"\n"
            "3. الـ DNS يرد: \"عنوانه 157.240.1.35 مثلاً\"\n"
            "4. المتصفح يروح للعنوان ده ويفتح الموقع ✅\n\n"
            "💡 خادم الـ DNS بتاعك غالبًا من شركة الاتصالات، وبيتظبط لوحده من الراوتر.\n"
            "ولو الـ DNS وقف، المواقع مش هتفتح بالاسم — حتى لو الإنترنت شغال!\n\n"
            "واجب النهاردة: افتح cmd واكتب ping facebook.com — أول سطر هيوريك عنوان الـ IP اللي الـ DNS رجّعه. اكتبه."
        ),
        "en": (
            "📖 Lesson 4: DNS\n\n"
            "DNS is the internet's phone book: it turns the name you type (like facebook.com) into the IP address the computer understands.\n\n"
            "How does it happen?\n"
            "1. You type facebook.com in the browser\n"
            "2. Your device asks the DNS server: \"what is the address of this name?\"\n"
            "3. DNS answers: \"its address is 157.240.1.35, for example\"\n"
            "4. The browser goes to that address and opens the site ✅\n\n"
            "💡 Your DNS server is usually from your provider, and the router sets it automatically.\n"
            "And if DNS stops working, sites will not open by name — even if the internet is working!\n\n"
            "Today's task: open cmd and type ping facebook.com — the first line shows the IP address DNS returned. Write it down."
        ),
    },
    {
        "title_ar": "الدرس 5: إزاي البيانات بتسافر",
        "title_en": "Lesson 5: How data travels",
        "ar": (
            "✈️ الدرس 5: إزاي البيانات بتسافر\n\n"
            "لما تبعت رسالة أو تفتح موقع، البيانات مش بتسافر مرة واحدة — بتتقسّم لحزم (packets) صغيرة، وكل حزمة عليها عنوان المرسل والمستقبل.\n\n"
            "الرحلة:\n"
            "1. موبايلك يقسّم الرسالة لحزم\n"
            "2. كل حزمة تسافر من راوتر لراوتر (زي محطات) لحد ما توصل للسيرفر\n"
            "3. السيرفر يجمّع الحزم ويرجع الرد بنفس الطريقة\n\n"
            "💡 الحزم ممكن تسافر في طرق مختلفة، وبتتجمع بالترتيب في الآخر — زي ما تبعت كتاب صفحة صفحة مع سواقين مختلفين، ويتجمع في الآخر.\n\n"
            "نوعين من التوصيل:\n"
            "• TCP: بيتأكد إن كل حزمة وصلت وبالترتيب (للمواقع والملفات)\n"
            "• UDP: أسرع ومش بيتأكد (للمكالمات والفيديو المباشر — لو حزمة ضاعت، مش مهم)\n\n"
            "واجب النهاردة: افتح cmd واكتب ping 8.8.8.8 — بص على time= — ده الوقت اللي الحزمة بتاخده تروح وترجع بالمللي ثانية."
        ),
        "en": (
            "✈️ Lesson 5: How data travels\n\n"
            "When you send a message or open a site, the data does not travel at once — it is split into small packets, and every packet carries the sender's and receiver's addresses.\n\n"
            "The journey:\n"
            "1. Your phone splits the message into packets\n"
            "2. Every packet travels from router to router (like stations) until it reaches the server\n"
            "3. The server gathers the packets and sends the reply back the same way\n\n"
            "💡 Packets can travel by different routes, and they are gathered in order at the end — like sending a book page by page with different drivers, and it is assembled at the end.\n\n"
            "Two delivery types:\n"
            "• TCP: makes sure every packet arrived and in order (for websites and files)\n"
            "• UDP: faster and does not check (for calls and live video — if a packet is lost, it does not matter)\n\n"
            "Today's task: open cmd and type ping 8.8.8.8 — look at time= — that is how long a packet takes to go and return, in milliseconds."
        ),
    },
    {
        "title_ar": "الدرس 6: البورتات والبروتوكولات ببساطة",
        "title_en": "Lesson 6: Ports and protocols, simply",
        "ar": (
            "🚪 الدرس 6: البورتات والبروتوكولات ببساطة\n\n"
            "البروتوكول يعني قواعد متفق عليها بيتكلم بيها جهازين — زي لغة مشتركة.\n\n"
            "أشهر البروتوكولات:\n"
            "• HTTP: لغة صفحات الويب العادية\n"
            "• HTTPS: نفسها بس مشفّرة (الحرف S يعني Secure — آمن) — القفل اللي في المتصفح\n"
            "• SMTP: لغة إرسال الإيميل\n"
            "• FTP: لغة نقل الملفات\n\n"
            "والبورت؟ هو رقم الباب على الجهاز:\n"
            "• عنوان الـ IP يوصّلك للعمارة، والبورت يوصّلك للشقة — أي خدمة ليها بابها\n"
            "• 80 = صفحات HTTP، 443 = صفحات HTTPS، 25 و 587 = الإيميل\n\n"
            "💡 مش لازم تحفظ الأرقام — المهم تفهم الفكرة: كل خدمة بتتكلم على باب معين.\n\n"
            "واجب النهاردة: افتح المتصفح وبص على شريط العنوان في 3 مواقع — مين فيهم https (فيه قفل) ومين http؟ اكتبهم."
        ),
        "en": (
            "🚪 Lesson 6: Ports and protocols, simply\n\n"
            "A protocol means agreed rules two devices use to talk — like a shared language.\n\n"
            "The most famous protocols:\n"
            "• HTTP: the language of normal web pages\n"
            "• HTTPS: the same but encrypted (the S means Secure) — the lock in the browser\n"
            "• SMTP: the language of sending email\n"
            "• FTP: the language of transferring files\n\n"
            "And a port? It is the door number on a device:\n"
            "• The IP address gets you to the building, and the port gets you to the apartment — every service has its door\n"
            "• 80 = HTTP pages, 443 = HTTPS pages, 25 and 587 = email\n\n"
            "💡 You do not need to memorize the numbers — the important thing is to understand the idea: every service talks on a certain door.\n\n"
            "Today's task: open your browser and look at the address bar of 3 sites — which of them are https (with a lock) and which are http? Write them down."
        ),
    },
    {
        "title_ar": "الدرس 7: أمان شبكتك في البيت",
        "title_en": "Lesson 7: Securing your home network",
        "ar": (
            "🏠 الدرس 7: أمان شبكتك في البيت\n\n"
            "دلوقتي عرفت الشبكة بتشتغل إزاي — خلّص المستوى الأول بخطوات تحمي شبكة بيتك.\n\n"
            "✅ اعمل الخمس حاجات دول:\n"
            "1. غيّر كلمة سر الواي فاي — قوية وطويلة (12 حرف على الأقل)\n"
            "2. اتأكد إن نوع الحماية WPA2 أو WPA3 (مش WEP — دي قديمة ومكسورة)\n"
            "3. غيّر كلمة سر مدير الراوتر (admin) — مش كلمة السر الافتراضية\n"
            "4. متشاركش كلمة سر الواي فاي مع أي حد غريب\n"
            "5. حدّث الراوتر (firmware) — التحديث بيقفل ثغرات\n\n"
            "💡 التفاصيل الكاملة لكل خطوة جاية في المستوى التاني — دروس الحماية.\n\n"
            "🎉 مبروك! خلصت المستوى الأول من الشبكات — دلوقتي انت فاهم الإنترنت بيشتغل إزاي.\n\n"
            "واجب النهاردة: افتح إعدادات الواي فاي على موبايلك وشوف نوع الحماية (WPA2 ولا WPA3؟) — ولو كلمة سر الواي فاي لسه الافتراضية، غيّرها النهاردة."
        ),
        "en": (
            "🏠 Lesson 7: Securing your home network\n\n"
            "Now you know how the network works — finish Level 1 with steps that protect your home network.\n\n"
            "✅ Do these five things:\n"
            "1. Change your Wi-Fi password — strong and long (at least 12 characters)\n"
            "2. Make sure the security type is WPA2 or WPA3 (not WEP — it is old and broken)\n"
            "3. Change the router admin password — not the default one\n"
            "4. Do not share your Wi-Fi password with strangers\n"
            "5. Update the router (firmware) — updates close holes\n\n"
            "💡 The full details of every step are coming in Level 2 — the protection lessons.\n\n"
            "🎉 Congratulations! You finished Level 1 of networks — now you understand how the internet works.\n\n"
            "Today's task: open the Wi-Fi settings on your phone and check the security type (WPA2 or WPA3?) — and if the Wi-Fi password is still the default, change it today."
        ),
    },
    {
        "title_ar": "الدرس 8: الجدار الناري",
        "title_en": "Lesson 8: The firewall",
        "ar": (
            "🧱 الدرس 8: الجدار الناري\n\n"
            "الجدار الناري (Firewall) هو حارس على باب شبكتك: بيقرر إيه اللي يدخل وإيه اللي يخرج، وبيمنع أي اتصال مش مطلوب.\n\n"
            "عندك جدار ناري في 3 أماكن وانت مش واخد بالك:\n"
            "• في الراوتر: جدار ناري مدمج بيمنع أي حد من برّه يدخل شبكتك من غير ما تطلب\n"
            "• في ويندوز: Windows Firewall شغال لوحده — متطفيهوش أبدًا\n"
            "• في الموبايل: نظام التشغيل بيحمي التطبيقات من الاتصالات الغريبة\n\n"
            "💡 لما برنامج يسألك \"تسمح له يعدي من الجدار الناري؟\" — اسمح بس للبرامج اللي تعرفها وتثق فيها (زي المتصفح أو لعبة أونلاين معروفة).\n\n"
            "⚠️ لو طفيت الجدار الناري عشان \"برنامج مش شغال\" — دي أسوأ حاجة تعملها. دور على حل تاني، وخلّيه شغال.\n\n"
            "واجب النهاردة: افتح Windows Security على الكمبيوتر وتأكد إن الجدار الناري شغال (Firewall & network protection — لازم يكون On)."
        ),
        "en": (
            "🧱 Lesson 8: The firewall\n\n"
            "A firewall is a guard at your network's door: it decides what comes in and what goes out, and blocks any connection you did not ask for.\n\n"
            "You already have a firewall in 3 places without noticing:\n"
            "• In the router: a built-in firewall that stops anyone outside from entering your network uninvited\n"
            "• In Windows: Windows Firewall runs by itself — never turn it off\n"
            "• On your phone: the system protects apps from strange connections\n\n"
            "💡 When a program asks \"allow it through the firewall?\" — allow only programs you know and trust (like the browser or a known online game).\n\n"
            "⚠️ If you turn the firewall off because \"a program is not working\" — that is the worst thing you can do. Find another solution, and keep it on.\n\n"
            "Today's task: open Windows Security on your computer and make sure the firewall is on (Firewall & network protection — it must say On)."
        ),
    },
    {
        "title_ar": "الدرس 9: تأمين الراوتر",
        "title_en": "Lesson 9: Securing the router",
        "ar": (
            "🔐 الدرس 9: تأمين الراوتر\n\n"
            "الراوتر هو أهم جهاز في شبكتك — لو حد دخله، يقدر يشوف كل أجهزتك. أمّنه في 5 خطوات:\n\n"
            "1. افتح المتصفح واكتب 192.168.1.1 — هتفتح صفحة الراوتر (العنوان مكتوب على الاستيكر اللي تحت الراوتر)\n"
            "2. سجّل دخول: اسم المستخدم وكلمة السر الافتراضية غالبًا admin / admin\n"
            "3. ⚠️ غيّر كلمة سر المدير فورًا — دي أهم خطوة، عشان أي حد يعرف الافتراضية يدخل\n"
            "4. حدّث الـ firmware: دوّر في الإعدادات على \"Firmware Update\" وحدّث لآخر نسخة\n"
            "5. اقفل الـ WPS: زرار في الراوتر بيخلي الأجهزة تتصل من غير كلمة سر — سهل يتكسر، اقفله من الإعدادات\n"
            "6. غيّر اسم الشبكة (SSID) الافتراضي — عشان ميكشفش نوع الراوتر بتاعك\n\n"
            "واجب النهاردة: ادخل على صفحة الراوتر وغيّر كلمة سر المدير — اعملها قوية ومختلفة عن كلمة سر الواي فاي."
        ),
        "en": (
            "🔐 Lesson 9: Securing the router\n\n"
            "The router is the most important device in your network — if someone gets in, they can see all your devices. Secure it in 5 steps:\n\n"
            "1. Open your browser and type 192.168.1.1 — the router page opens (the address is on the sticker under the router)\n"
            "2. Log in: the default username and password are usually admin / admin\n"
            "3. ⚠️ Change the admin password at once — this is the most important step, because anyone who knows the default can enter\n"
            "4. Update the firmware: look in the settings for \"Firmware Update\" and update to the latest version\n"
            "5. Turn off WPS: a button on the router that lets devices connect without a password — it is easy to break, turn it off in the settings\n"
            "6. Change the default network name (SSID) — so it does not reveal your router model\n\n"
            "Today's task: open the router page and change the admin password — make it strong and different from the Wi-Fi password."
        ),
    },
    {
        "title_ar": "الدرس 10: شبكة الضيوف",
        "title_en": "Lesson 10: The guest network",
        "ar": (
            "👥 الدرس 10: شبكة الضيوف\n\n"
            "لما ضيف ييجي بيتك ويطلب الواي فاي، متديلوش كلمة سر شبكتك — اديله شبكة الضيوف.\n\n"
            "شبكة الضيوف (Guest Network) هي شبكة واي فاي تانية من نفس الراوتر، بس معزولة:\n"
            "• الضيف بياخد إنترنت عادي ✅\n"
            "• بس مبيشوفش أجهزتك: لا اللابتوب ولا الطابعة ولا الملفات المشتركة ❌\n\n"
            "ليه مهمة؟ موبايل الضيف ممكن يكون عليه فيروس — ولو دخل شبكتك، الفيروس يقدر يحاول يوصل لأجهزتك. شبكة الضيوف بتوقفه عند الباب.\n\n"
            "إزاي تشغّلها؟ من صفحة الراوتر: دوّر على \"Guest Network\" وفعّلها، وحط لها كلمة سر مختلفة وبسيطة للضيوف.\n\n"
            "واجب النهاردة: فعّل شبكة الضيوف على الراوتر بتاعك، وحط لها كلمة سر سهلة تقولها لأي ضيف."
        ),
        "en": (
            "👥 Lesson 10: The guest network\n\n"
            "When a guest comes to your home and asks for Wi-Fi, do not give them your network password — give them the guest network.\n\n"
            "The guest network is a second Wi-Fi network from the same router, but isolated:\n"
            "• The guest gets normal internet ✅\n"
            "• But they cannot see your devices: no laptop, no printer, no shared files ❌\n\n"
            "Why does it matter? A guest's phone might have a virus — and if it joins your network, the virus can try to reach your devices. The guest network stops it at the door.\n\n"
            "How to turn it on? From the router page: look for \"Guest Network\", turn it on, and give it a different, simple password for guests.\n\n"
            "Today's task: turn on the guest network on your router, and give it an easy password you can tell any guest."
        ),
    },
    {
        "title_ar": "الدرس 11: مين على الواي فاي بتاعك؟",
        "title_en": "Lesson 11: Who is on your Wi-Fi?",
        "ar": (
            "🔍 الدرس 11: مين على الواي فاي بتاعك؟\n\n"
            "جارك ممكن يكون بيستخدم الواي فاي بتاعك وانت مش عارف — اعرف مين متصل واطرد الغريب.\n\n"
            "إزاي تشوف المتصلين؟\n"
            "• من صفحة الراوتر: دوّر على \"Connected Devices\" أو \"DHCP Clients\" — هتلاقي قائمة بكل جهاز متصل واسمه وعنوانه\n"
            "• أو من موبايلك: نزّل تطبيق Fing المجاني — بيفحص الشبكة ويوريك كل الأجهزة المتصلة\n\n"
            "🚩 جهاز غريب في القائمة؟\n"
            "1. غيّر كلمة سر الواي فاي فورًا — كل الأجهزة هتتقطع، وانت وصّل أجهزتك تاني بالكلمة الجديدة\n"
            "2. اتأكد إن الحماية WPA2 أو WPA3\n"
            "3. راجع القائمة تاني بعد يوم — لو الغريب رجع، يبقى حد عارف الكلمة الجديدة\n\n"
            "💡 كل جهاز ليه بصمة اسمها MAC address — عنوان ثابت مبيتغيرش، والراوتر بيعرفه بيه.\n\n"
            "واجب النهاردة: افتح قائمة الأجهزة المتصلة (من الراوتر أو Fing) وعدّهم — لو لقيت جهاز متعرفوش، غيّر كلمة سر الواي فاي."
        ),
        "en": (
            "🔍 Lesson 11: Who is on your Wi-Fi?\n\n"
            "Your neighbor might be using your Wi-Fi without you knowing — see who is connected and kick out strangers.\n\n"
            "How to see connected devices?\n"
            "• From the router page: look for \"Connected Devices\" or \"DHCP Clients\" — you will find a list of every connected device with its name and address\n"
            "• Or from your phone: install the free Fing app — it scans the network and shows you all connected devices\n\n"
            "🚩 A strange device on the list?\n"
            "1. Change the Wi-Fi password at once — all devices will disconnect, and you reconnect yours with the new password\n"
            "2. Make sure the protection is WPA2 or WPA3\n"
            "3. Check the list again after a day — if the stranger is back, someone knows the new password\n\n"
            "💡 Every device has a fingerprint called a MAC address — a fixed address that never changes, and the router knows it by that.\n\n"
            "Today's task: open the list of connected devices (from the router or Fing) and count them — if you find a device you do not know, change the Wi-Fi password."
        ),
    },
    {
        "title_ar": "الدرس 12: الـ VPN ببساطة",
        "title_en": "Lesson 12: VPN, simply",
        "ar": (
            "🛡️ الدرس 12: الـ VPN ببساطة\n\n"
            "الـ VPN هو نفق مشفّر بين جهازك والإنترنت: بياناتك بتسافر جواه، ومحدش على الشبكة يقدر يشوفها.\n\n"
            "إيه اللي بيعمله؟\n"
            "• بيخفي اللي بتعمله عن اللي على نفس الواي فاي (في القهوة أو المطار)\n"
            "• بيخفي نشاطك عن مزود الإنترنت\n"
            "• بيخليك تظهر كأنك في بلد تانية\n\n"
            "وإيه اللي مش بيعمله؟\n"
            "• مش بيخفيك تمامًا — الشركة اللي بتشغّل الـ VPN شايفة نشاطك\n"
            "• مش بيحميك من الفيروسات ولا من روابط النصب\n"
            "• مش بيخلي أي حاجة غير قانونية قانونية\n\n"
            "⚠️ خد بالك: VPN مجاني عشوائي ممكن يبيع بياناتك — اختار شركة معروفة (زي Proton VPN اللي ليه باقة مجانية)، ومتستخدمش VPN من إعلان مشبوه.\n\n"
            "واجب النهاردة: لو بتستخدم واي فاي عام كتير، نزّل VPN موثوق وشغّله مرة واحدة عشان تشوف بيشتغل إزاي."
        ),
        "en": (
            "🛡️ Lesson 12: VPN, simply\n\n"
            "A VPN is an encrypted tunnel between your device and the internet: your data travels inside it, and nobody on the network can see it.\n\n"
            "What does it do?\n"
            "• It hides what you do from people on the same Wi-Fi (in a café or airport)\n"
            "• It hides your activity from your internet provider\n"
            "• It makes you appear as if you are in another country\n\n"
            "And what does it NOT do?\n"
            "• It does not make you fully invisible — the company running the VPN sees your activity\n"
            "• It does not protect you from viruses or scam links\n"
            "• It does not make anything illegal legal\n\n"
            "⚠️ Be careful: a random free VPN might sell your data — choose a known company (like Proton VPN, which has a free plan), and never use a VPN from a suspicious ad.\n\n"
            "Today's task: if you often use public Wi-Fi, install a trusted VPN and turn it on once to see how it works."
        ),
    },
    {
        "title_ar": "الدرس 13: التحديثات",
        "title_en": "Lesson 13: Updates",
        "ar": (
            "🔄 الدرس 13: التحديثات\n\n"
            "كل تحديث بينزل عشان يقفل ثغرة اتكشفت — واللي مبيحدّثش، بيسيب الباب مفتوح.\n\n"
            "حدّث التلاتة دول دايمًا:\n"
            "• الراوتر: الـ firmware — من صفحة الراوتر، دوّر على \"Firmware Update\"\n"
            "• الموبايل: النظام والتطبيقات — من المتجر والإعدادات\n"
            "• الكمبيوتر: الويندوز والبرامج — فعّل التحديث التلقائي\n\n"
            "💡 فعّل التحديث التلقائي في كل جهاز — كده الثغرات بتتقفل لوحدها من غير ما تفتكر.\n\n"
            "⚠️ جهاز قديم الشركة بطلت تحدّثه (موبايل قديم أو راوتر قديم) بقى خطر — فكّر تبدّله، أو على الأقل متستخدموش في حاجات مهمة زي البنك.\n\n"
            "واجب النهاردة: افتح موبايلك والكمبيوتر، ودوّر على التحديثات ونزّلها — وافتح صفحة الراوتر وشوف الـ firmware بتاعه آخر نسخة ولا لأ."
        ),
        "en": (
            "🔄 Lesson 13: Updates\n\n"
            "Every update comes out to close a hole that was discovered — and whoever does not update leaves the door open.\n\n"
            "Always update these three:\n"
            "• The router: the firmware — from the router page, look for \"Firmware Update\"\n"
            "• The phone: the system and apps — from the store and settings\n"
            "• The computer: Windows and programs — turn on automatic updates\n\n"
            "💡 Turn on automatic updates on every device — that way holes close by themselves without you remembering.\n\n"
            "⚠️ An old device the company stopped updating (an old phone or router) has become a risk — think about replacing it, or at least do not use it for important things like banking.\n\n"
            "Today's task: open your phone and computer, look for updates and install them — and open the router page to see if its firmware is the latest version."
        ),
    },
    {
        "title_ar": "الدرس 14: لو شبكتك اتاخترقت تعمل إيه",
        "title_en": "Lesson 14: If your network is hacked — what to do",
        "ar": (
            "🆘 الدرس 14: لو شبكتك اتاخترقت تعمل إيه\n\n"
            "علامات إن شبكتك فيها حد غريب:\n"
            "• الإنترنت بطيء فجأة من غير سبب\n"
            "• أجهزة غريبة في قائمة المتصلين\n"
            "• إعدادات الراوتر اتغيرت لوحدها\n"
            "• استهلاك البيانات زاد جدًا فجأة\n\n"
            "🚨 خطوات الإنقاذ (بالترتيب):\n"
            "1. افصل الأجهزة أو اقفل الواي فاي مؤقتًا\n"
            "2. اعمل إعادة ضبط المصنع للراوتر (دوس على زرار Reset بإبرة 10 ثواني)\n"
            "3. حط كلمة سر مدير جديدة وقوية، وكلمة سر واي فاي جديدة (WPA2/WPA3)\n"
            "4. حدّث الـ firmware لآخر نسخة\n"
            "5. راجع الأجهزة المتصلة — مفيش غريب\n"
            "6. غيّر كلمات سر حساباتك المهمة من جهاز نضيف\n"
            "7. شغّل شبكة الضيوف للزوار بدل شبكتك\n\n"
            "🎉 مبروك! خلصت المستوى التاني من الشبكات — دلوقتي بتعرف تحمي شبكتك زي المحترفين.\n\n"
            "واجب النهاردة: اكتب الخطوات دي في ملاحظة على موبايلك — وقت الأزمة مش وقت التفكير."
        ),
        "en": (
            "🆘 Lesson 14: If your network is hacked — what to do\n\n"
            "Signs that a stranger is in your network:\n"
            "• The internet suddenly becomes slow for no reason\n"
            "• Strange devices in the connected list\n"
            "• Router settings changed by themselves\n"
            "• Data usage suddenly jumped a lot\n\n"
            "🚨 Rescue steps (in order):\n"
            "1. Disconnect devices or turn Wi-Fi off temporarily\n"
            "2. Factory-reset the router (press the Reset button with a pin for 10 seconds)\n"
            "3. Set a new strong admin password and a new Wi-Fi password (WPA2/WPA3)\n"
            "4. Update the firmware to the latest version\n"
            "5. Check connected devices — no strangers\n"
            "6. Change the passwords of your important accounts from a clean device\n"
            "7. Turn on the guest network for visitors instead of your network\n\n"
            "🎉 Congratulations! You finished Level 2 of networks — now you know how to protect your network like a professional.\n\n"
            "Today's task: write these steps in a note on your phone — a crisis is not the time to think."
        ),
    },
    {
        "title_ar": "الدرس 15: نموذج TCP/IP ببساطة",
        "title_en": "Lesson 15: The TCP/IP model, simply",
        "ar": (
            "🧱 الدرس 15: نموذج TCP/IP ببساطة\n\n"
            "مهندسين الشبكات قسّموا شغل الإنترنت لـ 4 طبقات — كل طبقة بتعمل شغلانة واحدة، وبتسلّم للي بعدها.\n\n"
            "الـ 4 طبقات (من فوق لتحت):\n"
            "1. التطبيقات (Application): اللي بتشوفه — المتصفح، واتساب، تليجرام\n"
            "2. النقل (Transport): TCP و UDP — بيوصّلوا الحزم ويتأكدوا من الترتيب\n"
            "3. الإنترنت (Internet): الـ IP — العناوين والتوجيه من شبكة لشبكة\n"
            "4. الوصول للشبكة (Network Access): الواي فاي والكابل — السلك والهواء اللي بتمشي عليه البيانات\n\n"
            "مثال: بعت طرد — تكتب الجواب (التطبيقات)، تحطه في ظرف وتكتب عليه تتبع (النقل)، تكتب العنوان (الإنترنت)، وتديه لشركة الشحن (الوصول).\n\n"
            "💡 لما حاجة تعطل، الطبقات بتقولك المشكلة فين: الموقع مش بيفتح؟ ممكن تكون طبقة التطبيقات. الواي فاي مش متصل أصلًا؟ دي طبقة الوصول.\n\n"
            "واجب النهاردة: افتح موقع، وسمّي كل طبقة بتعمل إيه في اللحظة دي — اكتبهم في 4 سطور."
        ),
        "en": (
            "🧱 Lesson 15: The TCP/IP model, simply\n\n"
            "Network engineers divided the internet's work into 4 layers — every layer does one job and hands over to the next.\n\n"
            "The 4 layers (top to bottom):\n"
            "1. Application: what you see — the browser, WhatsApp, Telegram\n"
            "2. Transport: TCP and UDP — they deliver packets and check the order\n"
            "3. Internet: IP — addresses and routing from network to network\n"
            "4. Network Access: Wi-Fi and cable — the wire and air the data travels on\n\n"
            "Example: you send a parcel — you write the letter (Application), put it in an envelope with tracking (Transport), write the address (Internet), and hand it to the shipping company (Access).\n\n"
            "💡 When something breaks, the layers tell you where the problem is: the site does not open? It might be the Application layer. Wi-Fi not connected at all? That is the Access layer.\n\n"
            "Today's task: open a website and name what each layer does at that moment — write them in 4 lines."
        ),
    },
    {
        "title_ar": "الدرس 16: قناع الشبكة الفرعية",
        "title_en": "Lesson 16: The subnet mask",
        "ar": (
            "🎭 الدرس 16: قناع الشبكة الفرعية\n\n"
            "قناع الشبكة (Subnet Mask) هو اللي بيقول: أنهو جزء من الـ IP هو عنوان الشبكة، وأنهو جزء هو رقم الجهاز.\n\n"
            "أشهر قناع: 255.255.255.0\n"
            "• معناه: أول 3 أرقام = الشبكة، وآخر رقم = الجهاز\n"
            "• مثال: شبكة 192.168.1.0 — الأجهزة فيها من 192.168.1.1 لحد 192.168.1.254\n"
            "• الراوتر نفسه غالبًا بياخد 192.168.1.1\n\n"
            "💡 الـ 255 يعني \"ثابت\"، والـ 0 يعني \"متغير\":\n"
            "• 255.255.255.0 = أول 3 أرقام ثابتين (الشبكة)، وآخر رقم بيتغير (الأجهزة)\n"
            "• وده بيسمّوه /24 — هتشوفه مكتوب كده: 192.168.1.0/24\n\n"
            "مش لازم تحسبه بإيدك — المهم تعرف تقراه لما تشوفه.\n\n"
            "واجب النهاردة: افتح تفاصيل الواي فاي على موبايلك — اكتب عنوان الـ IP وقناع الشبكة (Subnet Mask) اللي شايفهم."
        ),
        "en": (
            "🎭 Lesson 16: The subnet mask\n\n"
            "The subnet mask tells you: which part of the IP is the network address, and which part is the device number.\n\n"
            "The most common mask: 255.255.255.0\n"
            "• It means: the first 3 numbers = the network, and the last number = the device\n"
            "• Example: network 192.168.1.0 — devices in it go from 192.168.1.1 to 192.168.1.254\n"
            "• The router itself usually takes 192.168.1.1\n\n"
            "💡 255 means \"fixed\" and 0 means \"changes\":\n"
            "• 255.255.255.0 = the first 3 numbers are fixed (the network), and the last number changes (the devices)\n"
            "• This is called /24 — you will see it written like this: 192.168.1.0/24\n\n"
            "You do not need to calculate it by hand — the important thing is to recognize it when you see it.\n\n"
            "Today's task: open the Wi-Fi details on your phone — write down the IP address and the subnet mask you see."
        ),
    },
    {
        "title_ar": "الدرس 17: الـ DHCP",
        "title_en": "Lesson 17: DHCP",
        "ar": (
            "🤝 الدرس 17: الـ DHCP\n\n"
            "الـ DHCP هو الموظف اللي بيوزّع عناوين IP على الأجهزة أول ما تدخل الشبكة — من غير ما تعمل أي حاجة.\n\n"
            "إزاي بيشتغل؟\n"
            "1. موبايلك يدخل الواي فاي ويقول: \"عايز عنوان!\"\n"
            "2. الراوتر (خادم الـ DHCP) يرد: \"خد 192.168.1.5\"\n"
            "3. العنوان ده \"إيجار\" لمدة معينة — وبعدين يتجدد لوحده\n\n"
            "💡 عشان كده عنوان موبايلك بيتغير أحيانًا — الراوتر بيدي كل مرة عنوان متاح.\n"
            "والراوتر عنده قائمة بكل العناوين اللي وزّعها (DHCP Clients) — دي نفس القائمة اللي شفتها في درس \"مين على الواي فاي بتاعك\".\n\n"
            "واجب النهاردة: افتح صفحة الراوتر ودوّر على قائمة DHCP Clients — شوف أسماء أجهزتك وعناوينها."
        ),
        "en": (
            "🤝 Lesson 17: DHCP\n\n"
            "DHCP is the clerk that hands out IP addresses to devices as soon as they join the network — without you doing anything.\n\n"
            "How does it work?\n"
            "1. Your phone joins Wi-Fi and says: \"I need an address!\"\n"
            "2. The router (the DHCP server) answers: \"take 192.168.1.5\"\n"
            "3. This address is a \"rental\" for a while — then it renews by itself\n\n"
            "💡 That is why your phone's address changes sometimes — the router gives an available address each time.\n"
            "And the router keeps a list of all the addresses it handed out (DHCP Clients) — the same list you saw in the \"who is on your Wi-Fi\" lesson.\n\n"
            "Today's task: open the router page and look for the DHCP Clients list — see the names of your devices and their addresses."
        ),
    },
    {
        "title_ar": "الدرس 18: IP ثابت ولا متحرك؟",
        "title_en": "Lesson 18: Static or dynamic IP?",
        "ar": (
            "🔀 الدرس 18: IP ثابت ولا متحرك؟\n\n"
            "فيه نوعين من العناوين — وكل واحد ليه استخدامه:\n\n"
            "• متحرك (Dynamic): الراوتر بيديه لك بالـ DHCP وبيتغير مع الوقت — ده الطبيعي للموبايلات واللابتوبات\n"
            "• ثابت (Static): عنوان مبيتغيرش أبدًا — للأجهزة اللي لازم توصل لها بنفس العنوان دايمًا: الطابعة، كاميرات المراقبة، السيرفرات\n\n"
            "إزاي تثبّت عنوان لجهاز؟ أسهل طريقة: من الراوتر نفسه:\n"
            "• افتح صفحة الراوتر ← DHCP Reservation (أو Address Reservation)\n"
            "• اختار الجهاز من القائمة وثبّت له عنوان — كده الراوتر هيديله نفس العنوان كل مرة\n\n"
            "💡 متحطش عنوان ثابت من دماغك — ممكن يتعارض مع عنوان جهاز تاني. استخدم الحجز من الراوتر.\n\n"
            "واجب النهاردة: ادخل على إعدادات الراوتر وثبّت عنوان لجهاز بتستخدمه دايمًا (الطابعة مثلاً)."
        ),
        "en": (
            "🔀 Lesson 18: Static or dynamic IP?\n\n"
            "There are two kinds of addresses — and each has its use:\n\n"
            "• Dynamic: the router gives it to you with DHCP and it changes over time — this is normal for phones and laptops\n"
            "• Static: an address that never changes — for devices you must always reach at the same address: the printer, security cameras, servers\n\n"
            "How do you fix an address for a device? The easiest way: from the router itself:\n"
            "• Open the router page → DHCP Reservation (or Address Reservation)\n"
            "• Pick the device from the list and fix an address for it — the router will give it the same address every time\n\n"
            "💡 Do not make up a fixed address yourself — it might clash with another device's address. Use the reservation from the router.\n\n"
            "Today's task: open the router settings and reserve an address for a device you always use (the printer, for example)."
        ),
    },
    {
        "title_ar": "الدرس 19: التوجيه والتبديل",
        "title_en": "Lesson 19: Routing and switching",
        "ar": (
            "🔀 الدرس 19: التوجيه والتبديل\n\n"
            "جهازين شبه بعض بس شغلهم مختلف — اعرف الفرق:\n\n"
            "• السويتش (Switch): بيوصّل الأجهزة جوه نفس الشبكة ببعض — زي مشترك الكهرباء: كابلات كتير داخلة، وكل جهاز بيكلم التاني جوه البيت\n"
            "• الراوتر (Router): بيوصّل الشبكات ببعض — شبكة بيتك بالإنترنت، وبيقرر الحزمة تروح فين\n\n"
            "💡 الراوتر بتاعك فيه سويتش جواه: الفتحات اللي في ضهر الراوتر (LAN ports) دي السويتش المدمج — وصّل فيها الكمبيوتر أو التلفزيون بكابل.\n\n"
            "مثال يوضح:\n"
            "• السويتش = السنترال الداخلي بتاع شركة: موظف بيكلم موظف تاني جوه نفس الشركة\n"
            "• الراوتر = الخط اللي بيطلع برّه الشركة للعالم\n\n"
            "واجب النهاردة: بص على ضهر الراوتر بتاعك — عدّ فتحات الـ LAN (دي السويتش)، وشوف كابل واحد متوصل فيها ولا لأ."
        ),
        "en": (
            "🔀 Lesson 19: Routing and switching\n\n"
            "Two devices that look alike but do different jobs — know the difference:\n\n"
            "• Switch: connects devices inside the same network together — like a power strip: many cables in, and every device talks to the others inside the home\n"
            "• Router: connects networks together — your home network to the internet, and it decides where packets go\n\n"
            "💡 Your router has a switch inside it: the ports on the back of the router (LAN ports) are the built-in switch — plug the computer or TV in with a cable.\n\n"
            "An example to make it clear:\n"
            "• The switch = a company's internal phone exchange: an employee calling another employee inside the same company\n"
            "• The router = the line that goes outside the company to the world\n\n"
            "Today's task: look at the back of your router — count the LAN ports (that is the switch), and see if a cable is plugged into one."
        ),
    },
    {
        "title_ar": "الدرس 20: حل مشاكل الشبكة",
        "title_en": "Lesson 20: Troubleshooting your network",
        "ar": (
            "🔧 الدرس 20: حل مشاكل الشبكة\n\n"
            "الإنترنت وقف؟ متتوترش — امشي على الخطوات دي بالترتيب:\n\n"
            "1. بص على الراوتر: اللمبات شغالة؟ والكابلات متوصلة؟\n"
            "2. ريستارت الراوتر: افصله من الكهرباء 30 ثانية وشغّله تاني — دي بتحل نص المشاكل\n"
            "3. جرّب جهاز تاني: لو الموبايل بس اللي واقف واللابتوب شغال، المشكلة في الموبايل مش في الشبكة\n"
            "4. اعمل ping للراوتر: افتح cmd واكتب ping 192.168.1.1 — لو رد عليك، شبكة بيتك سليمة والمشكلة في خط الإنترنت\n"
            "5. اعمل ping لـ 8.8.8.8 — لو رد بس المواقع مش بتفتح، دي مشكلة DNS (من الدرس 4)\n"
            "6. لو كل ده فشل، كلّم شركة الاتصالات — وقولهم اللي جربته بالظبط\n\n"
            "💡 القاعدة: حدّد المشكلة فين الأول (جهازك؟ شبكة بيتك؟ خط الإنترنت؟) — وبعدين حلّها.\n\n"
            "واجب النهاردة: افتح cmd واكتب ping 192.168.1.1 وبعدين ping 8.8.8.8 — اكتب النتيجتين (الوقت time=) في ملاحظة."
        ),
        "en": (
            "🔧 Lesson 20: Troubleshooting your network\n\n"
            "The internet stopped? Do not panic — follow these steps in order:\n\n"
            "1. Look at the router: are the lights on? Are the cables connected?\n"
            "2. Restart the router: unplug it for 30 seconds and plug it back — this fixes half of all problems\n"
            "3. Try another device: if only the phone is down and the laptop works, the problem is in the phone, not the network\n"
            "4. Ping the router: open cmd and type ping 192.168.1.1 — if it answers, your home network is fine and the problem is the internet line\n"
            "5. Ping 8.8.8.8 — if it answers but sites do not open, it is a DNS problem (from lesson 4)\n"
            "6. If all of that fails, call your provider — and tell them exactly what you tried\n\n"
            "💡 The rule: find out WHERE the problem is first (your device? your home network? the internet line?) — then fix it.\n\n"
            "Today's task: open cmd and type ping 192.168.1.1 and then ping 8.8.8.8 — write down both results (the time=) in a note."
        ),
    },
    {
        "title_ar": "الدرس 21: المشروع الختامي — جهّز وأمّن شبكة بيتك",
        "title_en": "Lesson 21: Capstone — set up and secure your home network",
        "ar": (
            "🎓 الدرس 21: المشروع الختامي — جهّز وأمّن شبكة بيتك\n\n"
            "آخر درس في الشبكات — هنجمع كل حاجة في قائمة واحدة تنفذها على شبكة بيتك.\n\n"
            "✅ قائمة المشروع (اعمل واحدة كل يوم):\n"
            "1. غيّر كلمة سر مدير الراوتر (الدرس 9)\n"
            "2. كلمة سر واي فاي قوية + حماية WPA2 أو WPA3 (الدرس 7)\n"
            "3. حدّث الـ firmware لآخر نسخة (الدرس 13)\n"
            "4. اقفل الـ WPS (الدرس 9)\n"
            "5. شغّل شبكة الضيوف (الدرس 10)\n"
            "6. راجع الأجهزة المتصلة واطرد الغريب (الدرس 11)\n"
            "7. اتأكد إن الجدار الناري شغال (الدرس 8)\n"
            "8. اكتب بيانات شبكتك في ملاحظة آمنة: عنوان الـ IP والبوابة (192.168.1.1) والـ DNS\n"
            "9. اختبر: اعمل ping للراوتر وافتح موقع — كله شغال؟ ✅\n\n"
            "واجب النهاردة: نفّذ الخطوات التسع دي على شبكة بيتك النهاردة، خطوة بخطوة — واكتب في ورقة كل حاجة غيّرتها.\n\n"
            "🎉 مبروك يا بطل! خلصت 21 درس شبكات — من \"يعني إيه شبكة\" لحد ما أمّنت شبكة بيتك بنفسك. دلوقتي انت فاهم الإنترنت بجد.\n\n"
            "اللي جاي: مسارات البرمجة وقواعد البيانات بتتبني على اللي اتعلمته هنا. اكتب /lesson عشان تكمل 👌"
        ),
        "en": (
            "🎓 Lesson 21: Capstone — set up and secure your home network\n\n"
            "The last networks lesson — let's put everything together in one checklist for your home network.\n\n"
            "✅ Project checklist (do one every day):\n"
            "1. Change the router admin password (lesson 9)\n"
            "2. Strong Wi-Fi password + WPA2 or WPA3 protection (lesson 7)\n"
            "3. Update the firmware to the latest version (lesson 13)\n"
            "4. Turn off WPS (lesson 9)\n"
            "5. Turn on the guest network (lesson 10)\n"
            "6. Check connected devices and kick out strangers (lesson 11)\n"
            "7. Make sure the firewall is on (lesson 8)\n"
            "8. Write your network details in a safe note: the IP address, the gateway (192.168.1.1) and the DNS\n"
            "9. Test: ping the router and open a site — everything works? ✅\n\n"
            "Today's task: do these 9 steps on your home network today, one by one — and write down everything you changed on paper.\n\n"
            "🎉 Congratulations, champion! You finished 21 networks lessons — from \"what is a network\" to securing your home network yourself. Now you really understand the internet.\n\n"
            "Coming next: the programming and database tracks are built on what you learned here. Send /lesson to continue 👌"
        ),
    },
]

HTML_CSS_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه صفحة ويب؟",
        "title_en": "Lesson 1: What is a webpage?",
        "ar": (
            "🌐 الدرس 1: يعني إيه صفحة ويب؟\n\n"
            "أي صفحة ويب بتتكون من 3 حاجات شغالة مع بعض:\n\n"
            "• HTML: الهيكل — العضم بتاع الصفحة (عناوين، فقرات، صور، روابط)\n"
            "• CSS: الشكل — الألوان والخطوط والأحجام (اللبس بتاع الصفحة)\n"
            "• JavaScript: الحركة — اللي بيخلي الأزرار تشتغل والقوائم تتفتح\n\n"
            "مثال: بيت — HTML هو الحيطان والأوض، CSS هو الدهان والعفش، و JavaScript هو الكهرباء والأبواب اللي بتتفتح.\n\n"
            "💡 في الدورة دي هنتعلم HTML و CSS — وبعدها تقدر تعمل صفحتك بنفسك من غير أي برامج مدفوعة.\n\n"
            "واجب النهاردة: افتح أي موقع، ودوس كليك يمين واختار \"View page source\" — بص على الوسوم (tags) اللي بين < >، دي الـ HTML بتاع الصفحة."
        ),
        "en": (
            "🌐 Lesson 1: What is a webpage?\n\n"
            "Every webpage is made of 3 things working together:\n\n"
            "• HTML: the structure — the bones of the page (headings, paragraphs, images, links)\n"
            "• CSS: the look — colors, fonts and sizes (the clothes of the page)\n"
            "• JavaScript: the movement — what makes buttons work and menus open\n\n"
            "Example: a house — HTML is the walls and rooms, CSS is the paint and furniture, and JavaScript is the electricity and the doors that open.\n\n"
            "💡 In this course we will learn HTML and CSS — and after that you can make your own page without any paid programs.\n\n"
            "Today's task: open any website, right-click and choose \"View page source\" — look at the tags between < >, that is the page's HTML."
        ),
    },
    {
        "title_ar": "الدرس 2: أول صفحة HTML",
        "title_en": "Lesson 2: Your first HTML page",
        "ar": (
            "📄 الدرس 2: أول صفحة HTML\n\n"
            "الوسم (tag) هو أمر بين قوسين < > — بيقول للمتصفح يعرض إيه.\n\n"
            "أهم الوسوم:\n"
            "• <h1> عنوان كبير (وفيه h2 و h3 أصغر)\n"
            "• <p> فقرة نص\n"
            "• <a href=\"...\"> رابط — href هو عنوان الموقع\n"
            "• <img src=\"...\" alt=\"...\"> صورة — src هو مكان الصورة، و alt وصف ليها\n\n"
            "اكتب الكود ده في المفكرة واحفظه باسم index.html، وبعدين افتحه بدبل كليك:\n"
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "  <title>صفحتي الأولى</title>\n"
            "</head>\n"
            "<body>\n"
            "  <h1>أهلاً بيك في صفحتي</h1>\n"
            "  <p>دي أول صفحة عملتها بنفسي.</p>\n"
            "  <a href=\"https://example.com\">زور موقع مثال</a>\n"
            "</body>\n"
            "</html>\n\n"
            "💡 كل وسم بيتقفل: <p> ... </p> — الشرطة / معناها \"النهاية\".\n\n"
            "واجب النهاردة: اعمل صفحتك: عنوان h1 فيه اسمك، وفقرة عن نفسك، ورابط لموقع بتحبه."
        ),
        "en": (
            "📄 Lesson 2: Your first HTML page\n\n"
            "A tag is a command between angle brackets < > — it tells the browser what to show.\n\n"
            "The most important tags:\n"
            "• <h1> a big heading (and h2, h3 are smaller)\n"
            "• <p> a text paragraph\n"
            "• <a href=\"...\"> a link — href is the site address\n"
            "• <img src=\"...\" alt=\"...\"> an image — src is where the image is, and alt describes it\n\n"
            "Write this code in Notepad, save it as index.html, then double-click to open it:\n"
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "  <title>My first page</title>\n"
            "</head>\n"
            "<body>\n"
            "  <h1>Welcome to my page</h1>\n"
            "  <p>This is the first page I made myself.</p>\n"
            "  <a href=\"https://example.com\">Visit an example site</a>\n"
            "</body>\n"
            "</html>\n\n"
            "💡 Every tag closes: <p> ... </p> — the slash / means \"the end\".\n\n"
            "Today's task: make your page: an h1 heading with your name, a paragraph about yourself, and a link to a site you like."
        ),
    },
    {
        "title_ar": "الدرس 3: القوائم والجداول",
        "title_en": "Lesson 3: Lists and tables",
        "ar": (
            "📋 الدرس 3: القوائم والجداول\n\n"
            "القوائم بتنظم الحاجات في سطور — والجداول بترتب البيانات في صفوف وأعمدة.\n\n"
            "قائمة نقط (من غير ترتيب):\n"
            "<ul>\n"
            "  <li>أحمد</li>\n"
            "  <li>سارة</li>\n"
            "  <li>علي</li>\n"
            "</ul>\n\n"
            "قائمة مرقمة: بدّل ul بـ ol — هتطلع 1، 2، 3.\n\n"
            "جدول:\n"
            "<table>\n"
            "  <tr>\n"
            "    <th>اليوم</th>\n"
            "    <th>الدرس</th>\n"
            "  </tr>\n"
            "  <tr>\n"
            "    <td>السبت</td>\n"
            "    <td>بايثون</td>\n"
            "  </tr>\n"
            "</table>\n\n"
            "💡 tr يعني صف (row)، و th يعني عنوان عمود، و td يعني خلية عادية.\n\n"
            "واجب النهاردة: اعمل جدول فيه دروس الأسبوع بتاعك: عمود لليوم وعمود للدرس — 3 صفوف على الأقل."
        ),
        "en": (
            "📋 Lesson 3: Lists and tables\n\n"
            "Lists organize things into lines — and tables arrange data into rows and columns.\n\n"
            "Bullet list (no order):\n"
            "<ul>\n"
            "  <li>Ahmed</li>\n"
            "  <li>Sara</li>\n"
            "  <li>Ali</li>\n"
            "</ul>\n\n"
            "Numbered list: replace ul with ol — it shows 1, 2, 3.\n\n"
            "Table:\n"
            "<table>\n"
            "  <tr>\n"
            "    <th>Day</th>\n"
            "    <th>Lesson</th>\n"
            "  </tr>\n"
            "  <tr>\n"
            "    <td>Saturday</td>\n"
            "    <td>Python</td>\n"
            "  </tr>\n"
            "</table>\n\n"
            "💡 tr means a row, th means a column header, and td means a normal cell.\n\n"
            "Today's task: make a table of your week lessons: a column for the day and a column for the lesson — at least 3 rows."
        ),
    },
    {
        "title_ar": "الدرس 4: النماذج (forms)",
        "title_en": "Lesson 4: Forms",
        "ar": (
            "📝 الدرس 4: النماذج (forms)\n\n"
            "النموذج (form) هو اللي بيخلي الزائر يكتب بيانات — زي نموذج التسجيل أو تسجيل الدخول.\n\n"
            "<form>\n"
            "  <label>الاسم:</label>\n"
            "  <input type=\"text\" placeholder=\"اكتب اسمك\">\n"
            "  <label>الإيميل:</label>\n"
            "  <input type=\"email\" placeholder=\"example@mail.com\">\n"
            "  <label>كلمة السر:</label>\n"
            "  <input type=\"password\">\n"
            "  <button>اشترك</button>\n"
            "</form>\n\n"
            "أنواع الـ input:\n"
            "• text: نص عادي\n"
            "• email: إيميل — المتصفح بيتأكد إنه شكله صح\n"
            "• password: بيخفي اللي بتكتبه بنقط\n"
            "• placeholder: كلام خفيف جوه الخانة بيشرح تكتب إيه\n\n"
            "💡 النموذج لوحده مش بيحفظ البيانات — الحفظ محتاج سيرفر (هنتعلمه مع بايثون بعدين).\n\n"
            "واجب النهاردة: اعمل نموذج اشتراك: اسم + إيميل + زرار \"اشترك\" — وحطه في صفحتك."
        ),
        "en": (
            "📝 Lesson 4: Forms\n\n"
            "A form is what lets a visitor type data — like a registration or login form.\n\n"
            "<form>\n"
            "  <label>Name:</label>\n"
            "  <input type=\"text\" placeholder=\"Type your name\">\n"
            "  <label>Email:</label>\n"
            "  <input type=\"email\" placeholder=\"example@mail.com\">\n"
            "  <label>Password:</label>\n"
            "  <input type=\"password\">\n"
            "  <button>Subscribe</button>\n"
            "</form>\n\n"
            "Input types:\n"
            "• text: normal text\n"
            "• email: an email — the browser checks it looks right\n"
            "• password: hides what you type with dots\n"
            "• placeholder: light text inside the field explaining what to type\n\n"
            "💡 A form alone does not save data — saving needs a server (we will learn that with Python later).\n\n"
            "Today's task: make a subscription form: name + email + a \"Subscribe\" button — and put it on your page."
        ),
    },
    {
        "title_ar": "الدرس 5: يعني إيه CSS؟",
        "title_en": "Lesson 5: What is CSS?",
        "ar": (
            "🎨 الدرس 5: يعني إيه CSS؟\n\n"
            "الـ CSS هو اللي بيلوّن الصفحة ويظبط شكلها: لون الخط، حجمه، نوعه، ولون الخلفية.\n\n"
            "القاعدة بسيطة: المحدد { الخاصية: القيمة؛ }\n"
            "• المحدد (selector): مين اللي هيتلون — مثلاً h1\n"
            "• الخاصية (property): إيه اللي هيتغير — مثلاً color\n"
            "• القيمة (value): بكام — مثلاً blue\n\n"
            "حط الكود ده جوه <style> في الـ <head> بتاع صفحتك:\n"
            "h1 {\n"
            "  color: blue;\n"
            "  font-size: 32px;\n"
            "}\n"
            "p {\n"
            "  color: gray;\n"
            "  font-family: Arial;\n"
            "}\n"
            "body {\n"
            "  background-color: #f5f5f5;\n"
            "}\n\n"
            "💡 الألوان ممكن بالاسم (blue, red) أو بالكود (#ff0000 للأحمر).\n\n"
            "واجب النهاردة: لوّن عنوان صفحتك h1 وحط حجمه 32px، وغيّر لون الفقرات للرمادي."
        ),
        "en": (
            "🎨 Lesson 5: What is CSS?\n\n"
            "CSS is what colors the page and sets its look: the text color, its size, its font, and the background color.\n\n"
            "The rule is simple: selector { property: value; }\n"
            "• Selector: who gets colored — for example h1\n"
            "• Property: what changes — for example color\n"
            "• Value: to what — for example blue\n\n"
            "Put this code inside <style> in the <head> of your page:\n"
            "h1 {\n"
            "  color: blue;\n"
            "  font-size: 32px;\n"
            "}\n"
            "p {\n"
            "  color: gray;\n"
            "  font-family: Arial;\n"
            "}\n"
            "body {\n"
            "  background-color: #f5f5f5;\n"
            "}\n\n"
            "💡 Colors can be by name (blue, red) or by code (#ff0000 for red).\n\n"
            "Today's task: color your page's h1 heading, set its size to 32px, and change the paragraphs to gray."
        ),
    },
    {
        "title_ar": "الدرس 6: تنسيق الصفحة",
        "title_en": "Lesson 6: Page layout",
        "ar": (
            "🧱 الدرس 6: تنسيق الصفحة\n\n"
            "كل عنصر في الصفحة هو صندوق (box): المحتوى جواه، وبعدين padding، وبعدين border، وبعدين margin.\n\n"
            "• padding: مسافة جوه الصندوق (بين المحتوى والحدود)\n"
            "• margin: مسافة برّه الصندوق (بينه وبين اللي جنبه)\n"
            "• border: خط حوالين الصندوق\n\n"
            "والـ flexbox بيرتب الصناديق جنب بعض بسهولة:\n"
            ".boxes {\n"
            "  display: flex;\n"
            "  justify-content: center;\n"
            "}\n"
            ".box {\n"
            "  width: 100px;\n"
            "  height: 100px;\n"
            "  background-color: lightblue;\n"
            "  margin: 10px;\n"
            "  padding: 10px;\n"
            "}\n\n"
            "وحط في الـ HTML:\n"
            "<div class=\"boxes\">\n"
            "  <div class=\"box\">واحد</div>\n"
            "  <div class=\"box\">اتنين</div>\n"
            "  <div class=\"box\">تلاتة</div>\n"
            "</div>\n\n"
            "💡 النقطة قبل الاسم (.box) معناها \"كلاس\" — بيتطبق على أي عنصر واخد نفس الاسم.\n\n"
            "واجب النهاردة: اعمل 3 صناديق جنب بعض بـ flex، ولوّن كل واحد بلون مختلف."
        ),
        "en": (
            "🧱 Lesson 6: Page layout\n\n"
            "Every element on a page is a box: the content inside, then padding, then border, then margin.\n\n"
            "• padding: space inside the box (between the content and the edge)\n"
            "• margin: space outside the box (between it and its neighbors)\n"
            "• border: a line around the box\n\n"
            "And flexbox arranges boxes next to each other easily:\n"
            ".boxes {\n"
            "  display: flex;\n"
            "  justify-content: center;\n"
            "}\n"
            ".box {\n"
            "  width: 100px;\n"
            "  height: 100px;\n"
            "  background-color: lightblue;\n"
            "  margin: 10px;\n"
            "  padding: 10px;\n"
            "}\n\n"
            "And in the HTML put:\n"
            "<div class=\"boxes\">\n"
            "  <div class=\"box\">One</div>\n"
            "  <div class=\"box\">Two</div>\n"
            "  <div class=\"box\">Three</div>\n"
            "</div>\n\n"
            "💡 The dot before the name (.box) means \"class\" — it applies to any element with the same name.\n\n"
            "Today's task: make 3 boxes next to each other with flex, and color each one a different color."
        ),
    },
    {
        "title_ar": "الدرس 7: المشروع الختامي — صفحتي الشخصية",
        "title_en": "Lesson 7: Final project — my personal page",
        "ar": (
            "🎓 الدرس 7: المشروع الختامي — صفحتي الشخصية\n\n"
            "آخر درس — هنجمع كل حاجة في صفحة شخصية كاملة:\n\n"
            "• عنوان h1 فيه اسمك\n"
            "• صورة (img) — صورتك أو أي صورة\n"
            "• فقرة عن نفسك\n"
            "• قائمة هواياتك (ul)\n"
            "• جدول الدورات اللي بتاخدها (table)\n"
            "• نموذج تواصل (form: اسم + إيميل + زرار)\n"
            "• CSS: ألوان + flex للصناديق\n\n"
            "الهيكل:\n"
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "  <title>صفحتي الشخصية</title>\n"
            "  <style>\n"
            "    h1 { color: darkblue; }\n"
            "    body { font-family: Arial; }\n"
            "  </style>\n"
            "</head>\n"
            "<body>\n"
            "  <h1>أنا خالد</h1>\n"
            "  <p>بحب البرمجة وبتعلم كل يوم.</p>\n"
            "</body>\n"
            "</html>\n\n"
            "🎉 مبروك! خلصت 7 دروس HTML/CSS — دلوقتي تقدر تعمل صفحات بنفسك.\n\n"
            "واجب النهاردة: كمّل الصفحة دي بكل العناصر اللي فوق، وافتحها في المتصفح وورّيها لصاحبك."
        ),
        "en": (
            "🎓 Lesson 7: Final project — my personal page\n\n"
            "The last lesson — let's put everything together in a full personal page:\n\n"
            "• An h1 heading with your name\n"
            "• A photo (img) — your photo or any photo\n"
            "• A paragraph about yourself\n"
            "• A list of your hobbies (ul)\n"
            "• A table of the courses you take (table)\n"
            "• A contact form (form: name + email + button)\n"
            "• CSS: colors + flex for the boxes\n\n"
            "The structure:\n"
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "  <title>My personal page</title>\n"
            "  <style>\n"
            "    h1 { color: darkblue; }\n"
            "    body { font-family: Arial; }\n"
            "  </style>\n"
            "</head>\n"
            "<body>\n"
            "  <h1>I am Khaled</h1>\n"
            "  <p>I love programming and I learn every day.</p>\n"
            "</body>\n"
            "</html>\n\n"
            "🎉 Congratulations! You finished 7 HTML/CSS lessons — now you can make pages yourself.\n\n"
            "Today's task: complete this page with all the elements above, open it in your browser, and show it to a friend."
        ),
    },
]

SQL_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه قاعدة بيانات؟",
        "title_en": "Lesson 1: What is a database?",
        "ar": (
            "🗄️ الدرس 1: يعني إيه قاعدة بيانات؟\n\n"
            "قاعدة البيانات هي مكان منظم لحفظ البيانات — زي جدول إكسل بيفكر.\n\n"
            "• الجدول (Table): زي ورقة إكسل — فيه أعمدة وصفوف\n"
            "• العمود (Column): نوع البيانات — مثلاً الاسم، العمر\n"
            "• الصف (Row): سجل واحد — مثلاً طالب واحد ببياناته\n\n"
            "مثال: جدول \"طلاب\":\n"
            "id | name  | age\n"
            "1  | أحمد  | 20\n"
            "2  | سارة  | 22\n\n"
            "ليه مش إكسل وخلاص؟\n"
            "• قاعدة البيانات بتتحمل ملايين الصفوف وتدور فيها في ثانية\n"
            "• ناس كتير تقدر تستخدمها في نفس الوقت من غير ما تخرب\n"
            "• بتربط الجداول ببعض (هنشوف ده في درس الـ JOIN)\n\n"
            "واجب النهاردة: ارسم على ورقة جدول \"طلاب\" فيه 3 أعمدة (id، name، age) و 3 صفوف من عندك."
        ),
        "en": (
            "🗄️ Lesson 1: What is a database?\n\n"
            "A database is an organized place to store data — like an Excel sheet that thinks.\n\n"
            "• Table: like an Excel sheet — it has columns and rows\n"
            "• Column: the kind of data — for example name, age\n"
            "• Row: one record — for example one student with their data\n\n"
            "Example: a \"students\" table:\n"
            "id | name  | age\n"
            "1  | Ahmed | 20\n"
            "2  | Sara  | 22\n\n"
            "Why not just Excel?\n"
            "• A database handles millions of rows and searches them in a second\n"
            "• Many people can use it at the same time without breaking it\n"
            "• It connects tables together (we will see that in the JOIN lesson)\n\n"
            "Today's task: draw on paper a \"students\" table with 3 columns (id, name, age) and 3 rows of your own."
        ),
    },
    {
        "title_ar": "الدرس 2: جهّز SQLite",
        "title_en": "Lesson 2: Setting up SQLite",
        "ar": (
            "💾 الدرس 2: جهّز SQLite\n\n"
            "هنشتغل بـ SQLite — أصغر وأسهل قاعدة بيانات: ملف واحد، من غير سيرفر ولا تثبيت معقد.\n\n"
            "على الكمبيوتر (أسهل طريقتين):\n"
            "• بايثون فيه SQLite جاهز: مكتبة sqlite3 بتيجي مع بايثون (استخدمناها في درس قواعد البيانات)\n"
            "• أو نزّل DB Browser for SQLite (مجاني) من sqlitebrowser.org — برنامج بواجهة رسومية\n\n"
            "📱 على الموبايل (من غير تثبيت):\n"
            "• افتح المتصفح وادخل على sqliteonline.com — محرر SQL مجاني بيشتغل في المتصفح، من غير حساب\n"
            "• اكتب الكود ودوس Run — النتيجة بتظهر تحت على طول\n\n"
            "جرّب إنه شغال — اكتب ده ودوس Run:\n"
            "SELECT 1;\n\n"
            "لازم تشوف النتيجة: 1 ✅\n\n"
            "واجب النهاردة: افتح sqliteonline.com وشغّل SELECT 1; — وبعدين جرّب SELECT 2 + 3; وشوف النتيجة."
        ),
        "en": (
            "💾 Lesson 2: Setting up SQLite\n\n"
            "We will work with SQLite — the smallest and easiest database: one file, no server and no complex install.\n\n"
            "On a computer (two easiest ways):\n"
            "• Python already has SQLite built in: the sqlite3 library comes with Python (we used it in the databases lesson)\n"
            "• Or download DB Browser for SQLite (free) from sqlitebrowser.org — a program with a graphical interface\n\n"
            "📱 On a phone (no install):\n"
            "• Open your browser and go to sqliteonline.com — a free SQL editor that runs in the browser, no account needed\n"
            "• Type the code and press Run — the result appears below at once\n\n"
            "Try that it works — type this and press Run:\n"
            "SELECT 1;\n\n"
            "You should see the result: 1 ✅\n\n"
            "Today's task: open sqliteonline.com and run SELECT 1; — then try SELECT 2 + 3; and see the result."
        ),
    },
    {
        "title_ar": "الدرس 3: إنشاء جدول (CREATE TABLE)",
        "title_en": "Lesson 3: Creating a table (CREATE TABLE)",
        "ar": (
            "🏗️ الدرس 3: إنشاء جدول (CREATE TABLE)\n\n"
            "قبل ما تحفظ بيانات، لازم تعمل الجدول الأول — وتقول كل عمود نوعه إيه.\n\n"
            "CREATE TABLE students (\n"
            "  id INTEGER PRIMARY KEY,\n"
            "  name TEXT,\n"
            "  age INTEGER\n"
            ");\n\n"
            "إيه اللي حصل؟\n"
            "• CREATE TABLE students: اعمل جدول اسمه students\n"
            "• id INTEGER PRIMARY KEY: عمود رقم، والمفتاح الأساسي — رقم فريد لكل صف (1، 2، 3...)\n"
            "• name TEXT: عمود نص\n"
            "• age INTEGER: عمود رقم صحيح\n\n"
            "💡 أنواع البيانات الأساسية: INTEGER (رقم صحيح)، TEXT (نص)، REAL (رقم عشري زي 175.5).\n\n"
            "واجب النهاردة: اعمل جدول courses فيه: id رقم (مفتاح أساسي)، و title نص، و lessons رقم."
        ),
        "en": (
            "🏗️ Lesson 3: Creating a table (CREATE TABLE)\n\n"
            "Before saving data, you must make the table first — and say what type every column is.\n\n"
            "CREATE TABLE students (\n"
            "  id INTEGER PRIMARY KEY,\n"
            "  name TEXT,\n"
            "  age INTEGER\n"
            ");\n\n"
            "What happened?\n"
            "• CREATE TABLE students: make a table called students\n"
            "• id INTEGER PRIMARY KEY: a number column, and the primary key — a unique number for every row (1, 2, 3...)\n"
            "• name TEXT: a text column\n"
            "• age INTEGER: a whole-number column\n\n"
            "💡 The basic data types: INTEGER (whole number), TEXT (text), REAL (decimal like 175.5).\n\n"
            "Today's task: make a courses table with: id as a number (primary key), title as text, and lessons as a number."
        ),
    },
    {
        "title_ar": "الدرس 4: إضافة بيانات (INSERT)",
        "title_en": "Lesson 4: Adding data (INSERT)",
        "ar": (
            "➕ الدرس 4: إضافة بيانات (INSERT)\n\n"
            "الجدول جاهز — دلوقتي نملاه بيانات:\n\n"
            "INSERT INTO students (name, age) VALUES ('أحمد', 20);\n"
            "INSERT INTO students (name, age) VALUES ('سارة', 22);\n\n"
            "وممكن تضيف أكتر من صف في أمر واحد:\n"
            "INSERT INTO students (name, age) VALUES ('علي', 19), ('منى', 21);\n\n"
            "💡 ملاحظتين:\n"
            "• مكتبناش الـ id — عشان INTEGER PRIMARY KEY بيملاه لوحده (1، 2، 3، 4...)\n"
            "• النص بين علامتي تنصيص ' ' — والأرقام من غير تنصيص\n\n"
            "اتأكد إنها اتحفظت:\n"
            "SELECT * FROM students;\n\n"
            "واجب النهاردة: ضيف 3 طلاب لجدولك — وبعدين اعرضهم بـ SELECT *."
        ),
        "en": (
            "➕ Lesson 4: Adding data (INSERT)\n\n"
            "The table is ready — now let's fill it with data:\n\n"
            "INSERT INTO students (name, age) VALUES ('Ahmed', 20);\n"
            "INSERT INTO students (name, age) VALUES ('Sara', 22);\n\n"
            "And you can add more than one row in a single command:\n"
            "INSERT INTO students (name, age) VALUES ('Ali', 19), ('Mona', 21);\n\n"
            "💡 Two notes:\n"
            "• We did not write the id — because INTEGER PRIMARY KEY fills it by itself (1, 2, 3, 4...)\n"
            "• Text goes between quotes ' ' — and numbers without quotes\n\n"
            "Make sure it was saved:\n"
            "SELECT * FROM students;\n\n"
            "Today's task: add 3 students to your table — then show them with SELECT *."
        ),
    },
    {
        "title_ar": "الدرس 5: البحث (SELECT + WHERE)",
        "title_en": "Lesson 5: Searching (SELECT + WHERE)",
        "ar": (
            "🔍 الدرس 5: البحث (SELECT + WHERE)\n\n"
            "أهم أمر في SQL — تجيب البيانات اللي انت عايزها بس.\n\n"
            "كل حاجة:\n"
            "SELECT * FROM students;\n\n"
            "أعمدة معينة بس:\n"
            "SELECT name, age FROM students;\n\n"
            "مع شرط (WHERE):\n"
            "SELECT name, age FROM students WHERE age >= 20;\n"
            "SELECT name FROM students WHERE name = 'أحمد';\n\n"
            "الشروط زي بايثون: = يساوي، > أكبر من، < أصغر من، >= ، <= ، != مش يساوي.\n"
            "وممكن شرطين: WHERE age >= 20 AND name != 'علي'\n\n"
            "💡 النجمة * معناها \"كل الأعمدة\".\n\n"
            "واجب النهاردة: اعرض أسماء الطلاب اللي عمرهم أكبر من 21 — وبعدين اعرض كل بيانات الطالب اللي اسمه 'سارة'."
        ),
        "en": (
            "🔍 Lesson 5: Searching (SELECT + WHERE)\n\n"
            "The most important command in SQL — get only the data you want.\n\n"
            "Everything:\n"
            "SELECT * FROM students;\n\n"
            "Certain columns only:\n"
            "SELECT name, age FROM students;\n\n"
            "With a condition (WHERE):\n"
            "SELECT name, age FROM students WHERE age >= 20;\n"
            "SELECT name FROM students WHERE name = 'Ahmed';\n\n"
            "Conditions are like Python: = equal, > greater than, < less than, >=, <=, != not equal.\n"
            "And two conditions: WHERE age >= 20 AND name != 'Ali'\n\n"
            "💡 The star * means \"all columns\".\n\n"
            "Today's task: show the names of students older than 21 — then show all data of the student named 'Sara'."
        ),
    },
    {
        "title_ar": "الدرس 6: التعديل والحذف (UPDATE + DELETE)",
        "title_en": "Lesson 6: Updating and deleting (UPDATE + DELETE)",
        "ar": (
            "✏️ الدرس 6: التعديل والحذف (UPDATE + DELETE)\n\n"
            "التعديل:\n"
            "UPDATE students SET age = 21 WHERE name = 'أحمد';\n\n"
            "الحذف:\n"
            "DELETE FROM students WHERE id = 4;\n\n"
            "⚠️ تحذير مهم جدًا — من غير WHERE:\n"
            "• UPDATE students SET age = 21; — هيغيّر عمر كل الطلاب!\n"
            "• DELETE FROM students; — هيمسح الجدول كله!\n"
            "القاعدة: اكتب الـ WHERE الأول في دماغك، وبعدين اكتب الأمر.\n\n"
            "💡 قبل أي DELETE، جرّب نفس الشرط بـ SELECT الأول عشان تشوف هيمسح إيه:\n"
            "SELECT * FROM students WHERE id = 4;\n\n"
            "واجب النهاردة: عدّل عمر طالب واحد عندك، واحذف صف واحد بـ id — واعرض الجدول قبل وبعد عشان تشوف الفرق."
        ),
        "en": (
            "✏️ Lesson 6: Updating and deleting (UPDATE + DELETE)\n\n"
            "Updating:\n"
            "UPDATE students SET age = 21 WHERE name = 'Ahmed';\n\n"
            "Deleting:\n"
            "DELETE FROM students WHERE id = 4;\n\n"
            "⚠️ A very important warning — without WHERE:\n"
            "• UPDATE students SET age = 21; — it changes the age of ALL students!\n"
            "• DELETE FROM students; — it deletes the whole table!\n"
            "The rule: write the WHERE in your head first, then write the command.\n\n"
            "💡 Before any DELETE, try the same condition with SELECT first to see what it will delete:\n"
            "SELECT * FROM students WHERE id = 4;\n\n"
            "Today's task: change the age of one student, and delete one row by id — and show the table before and after to see the difference."
        ),
    },
    {
        "title_ar": "الدرس 7: المشروع الختامي — قاعدة بيانات الطلاب + JOIN",
        "title_en": "Lesson 7: Final project — students database + JOIN",
        "ar": (
            "🎓 الدرس 7: المشروع الختامي — قاعدة بيانات الطلاب + JOIN\n\n"
            "آخر درس — هنربط جدولين ببعض: الطلاب والدورات. الطالب بياخد دورة، والرابط بينهم جدول تالت.\n\n"
            "CREATE TABLE courses (\n"
            "  id INTEGER PRIMARY KEY,\n"
            "  title TEXT\n"
            ");\n"
            "CREATE TABLE enrollments (\n"
            "  student_id INTEGER,\n"
            "  course_id INTEGER\n"
            ");\n\n"
            "ضيف بيانات:\n"
            "INSERT INTO courses (title) VALUES ('بايثون'), ('روبي');\n"
            "INSERT INTO enrollments (student_id, course_id) VALUES (1, 1), (2, 1), (2, 2);\n\n"
            "الـ JOIN بيربط الجداول على حسب الـ id:\n"
            "SELECT students.name, courses.title\n"
            "FROM students\n"
            "JOIN enrollments ON students.id = enrollments.student_id\n"
            "JOIN courses ON courses.id = enrollments.course_id;\n\n"
            "النتيجة: كل طالب مع الدورات اللي بياخدها — أحمد/بايثون، سارة/بايثون، سارة/روبي.\n\n"
            "🎉 مبروك! خلصت 7 دروس SQL — دلوقتي تقدر تعمل قاعدة بيانات وتسألها أي سؤال.\n\n"
            "واجب النهاردة: ابنِ قاعدة البيانات دي كاملة (3 جداول + البيانات)، وشغّل استعلام الـ JOIN — وورّيني النتيجة."
        ),
        "en": (
            "🎓 Lesson 7: Final project — students database + JOIN\n\n"
            "The last lesson — let's connect two tables: students and courses. A student takes a course, and the link between them is a third table.\n\n"
            "CREATE TABLE courses (\n"
            "  id INTEGER PRIMARY KEY,\n"
            "  title TEXT\n"
            ");\n"
            "CREATE TABLE enrollments (\n"
            "  student_id INTEGER,\n"
            "  course_id INTEGER\n"
            ");\n\n"
            "Add data:\n"
            "INSERT INTO courses (title) VALUES ('Python'), ('Ruby');\n"
            "INSERT INTO enrollments (student_id, course_id) VALUES (1, 1), (2, 1), (2, 2);\n\n"
            "JOIN connects tables by matching ids:\n"
            "SELECT students.name, courses.title\n"
            "FROM students\n"
            "JOIN enrollments ON students.id = enrollments.student_id\n"
            "JOIN courses ON courses.id = enrollments.course_id;\n\n"
            "The result: every student with the courses they take — Ahmed/Python, Sara/Python, Sara/Ruby.\n\n"
            "🎉 Congratulations! You finished 7 SQL lessons — now you can build a database and ask it any question.\n\n"
            "Today's task: build this whole database (3 tables + data), run the JOIN query — and show me the result."
        ),
    },
]

SQLI_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه SQL Injection؟",
        "title_en": "Lesson 1: What is SQL injection?",
        "ar": (
            "💉 الدرس 1: يعني إيه SQL Injection؟\n"
            "📗 المستوى الأول: الأساسيات — هنفهم المشكلة الأول قبل ما نصلحها.\n\n"
            "تخيل موقع فيه صفحة دخول: بتكتب اسمك وكلمة السر، والموقع بيسأل قاعدة البيانات: \"فيه مستخدم بالاسم ده وكلمة السر دي؟\"\n\n"
            "الـ SQL Injection يعني حد يكتب في خانة الدخول — بدل اسمه — أمر لقاعدة البيانات، والموقع ينفذه من غير ما ياخد باله!\n\n"
            "مثال: بدل ما يكتب \"أحمد\"، يكتب: ' OR '1'='1\n"
            "قاعدة البيانات بتفهمها كده: \"دخّله، لأن 1 = 1 صح على طول\" — فيدخل من غير كلمة سر!\n\n"
            "ليه الموضوع خطير؟\n"
            "• المهاجم ممكن يشوف بيانات مش بتاعته (إيميلات وكلمات سر)\n"
            "• ممكن يدخل حسابات غيره — حتى حساب المدير\n"
            "• وممكن يمسح بيانات الموقع كله\n\n"
            "⚠️ مهم جدًا: الدورة دي للتعلم والحماية بس — بنتعلم إزاي الهجوم بيشتغل عشان نحمي نفسنا ومواقعنا. أي تجربة بتكون على موقعك أو معملك الخاص بس، وممنوع تمامًا تجرب على مواقع غيرك.\n\n"
            "واجب النهاردة: اكتب في 3 سطور بكلامك انت: إيه هو الـ SQL Injection، وليه لازم صاحب أي موقع يخاف منه."
        ),
        "en": (
            "💉 Lesson 1: What is SQL injection?\n"
            "📗 Level 1: Basics — first we understand the problem, then we fix it.\n\n"
            "Imagine a website with a login page: you type your name and password, and the site asks the database: \"is there a user with this name and password?\"\n\n"
            "SQL injection means someone types — instead of their name — a command for the database into the login box, and the site runs it without noticing!\n\n"
            "Example: instead of \"Ahmed\", they type: ' OR '1'='1\n"
            "The database understands it as: \"let them in, because 1 = 1 is always true\" — so they get in without a password!\n\n"
            "Why is it dangerous?\n"
            "• The attacker can see data that is not theirs (emails, passwords)\n"
            "• They can enter other people's accounts — even the admin's\n"
            "• They can delete the whole site's data\n\n"
            "⚠️ Very important: this course is for learning and protection only — we learn how the attack works so we can protect ourselves and our sites. Any testing is only on your own site or your own lab, and it is strictly forbidden to try it on other people's sites.\n\n"
            "Today's task: in 3 lines, in your own words: what is SQL injection, and why should every site owner be afraid of it?"
        ),
    },
    {
        "title_ar": "الدرس 2: إزاي قواعد البيانات والاستعلامات بتشتغل",
        "title_en": "Lesson 2: Databases & queries",
        "ar": (
            "💾 الدرس 2: إزاي قواعد البيانات والاستعلامات بتشتغل\n\n"
            "قبل ما نفهم الحقن، لازم نفهم الموقع بيكلم قاعدة البيانات إزاي.\n\n"
            "قاعدة البيانات فيها جداول — زي جدول \"users\" فيه عمودين: username و password.\n\n"
            "لما تدخل اسمك وكلمة السر، الموقع بيبعت لقاعدة البيانات سؤال (استعلام) زي ده:\n"
            "SELECT * FROM users WHERE username='ahmed' AND password='1234'\n\n"
            "يعني: \"هات الصف اللي اسمه ahmed وكلمة سره 1234\" — لو لقاه، تدخل. لو ملقاهوش، الدخول يفشل.\n\n"
            "والخدعة كلها هنا: الموقع بيبني السؤال ده بـ \"لزق\" — بياخد اللي انت كتبته ويلزقه جوه السؤال. جرّب الكود ده على جهازك (قاعدة بيانات تجريبية خاصة بيك):\n"
            "import sqlite3\n"
            "conn = sqlite3.connect(\":memory:\")\n"
            "cur = conn.cursor()\n"
            "cur.execute(\"CREATE TABLE users (username TEXT, password TEXT)\")\n"
            "cur.execute(\"INSERT INTO users VALUES ('ahmed', '1234')\")\n"
            "conn.commit()\n"
            "name = \"ahmed\"\n"
            "pw = \"1234\"\n"
            "query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "print(query)\n"
            "cur.execute(query)\n"
            "print(cur.fetchall())\n\n"
            "هتشوف السؤال مطبوع، والنتيجة: [('ahmed', '1234')] — يعني لقاه ودخل ✅\n\n"
            "⚠️ الكود ده للشرح بس — هو نفسه الطريقة الضعيفة اللي هنكسرها في الدرس الجاي، وبعدين نصلحها.\n\n"
            "واجب النهاردة: شغّل الكود ده عندك، وبعدين غيّر كلمة السر لـ \"غلط\" وشوف النتيجة بقت [] (فاضي — يعني الدخول فشل)."
        ),
        "en": (
            "💾 Lesson 2: How databases work\n\n"
            "Before we understand injection, we need to understand how a site talks to its database.\n\n"
            "A database has tables — like a \"users\" table with two columns: username and password.\n\n"
            "When you log in, the site sends the database a question (a query) like this:\n"
            "SELECT * FROM users WHERE username='ahmed' AND password='1234'\n\n"
            "Meaning: \"bring me the row named ahmed with password 1234\" — if it finds it, you get in. If not, login fails.\n\n"
            "And here is the whole trick: the site builds this question by \"gluing\" — it takes what you typed and pastes it inside the question. Try this code on your machine (your own test database):\n"
            "import sqlite3\n"
            "conn = sqlite3.connect(\":memory:\")\n"
            "cur = conn.cursor()\n"
            "cur.execute(\"CREATE TABLE users (username TEXT, password TEXT)\")\n"
            "cur.execute(\"INSERT INTO users VALUES ('ahmed', '1234')\")\n"
            "conn.commit()\n"
            "name = \"ahmed\"\n"
            "pw = \"1234\"\n"
            "query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "print(query)\n"
            "cur.execute(query)\n"
            "print(cur.fetchall())\n\n"
            "You will see the question printed, and the result: [('ahmed', '1234')] — it found him, login OK ✅\n\n"
            "⚠️ This code is for explanation only — it is the same weak way we will break in the next lesson, and then fix.\n\n"
            "Today's task: run this code, then change the password to \"wrong\" and see the result become [] (empty — login failed)."
        ),
    },
    {
        "title_ar": "الدرس 3: إزاي الحقن بيحصل",
        "title_en": "Lesson 3: How injection works",
        "ar": (
            "🕳️ الدرس 3: إزاي الحقن بيحصل\n\n"
            "نفس الكود بتاع الدرس اللي فات — بس المهاجم مش هيكتب اسمه، هيكتب ده في خانة الاسم:\n"
            "' OR '1'='1' -- \n\n"
            "الموقع الغبي هيلزق الكلام ده جوه السؤال، فيبقى السؤال كده:\n"
            "SELECT * FROM users WHERE username='' OR '1'='1' -- ' AND password='anything'\n\n"
            "إيه اللي حصل؟\n"
            "• علامة -- دي معناها \"تعليق\" — يعني كل اللي بعدها قاعدة البيانات بتتجاهله (يعني فحص كلمة السر اتلغى!)\n"
            "• و '1'='1' دي جملة صح على طول — فقاعدة البيانات بترجع أول مستخدم تلاقيه\n\n"
            "جرّب بنفسك على قاعدة بيانات تجريبية خاصة بيك (نفس إعداد الدرس اللي فات):\n"
            "name = \"' OR '1'='1' -- \"\n"
            "pw = \"anything\"\n"
            "query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "print(query)\n"
            "cur.execute(query)\n"
            "print(cur.fetchall())\n\n"
            "النتيجة: [('ahmed', '1234')] — دخل من غير ما يعرف كلمة السر! 😱\n\n"
            "⚠️ ده على معملك الخاص بس — الهدف تفهم الثغرة عشان تسدّها، مش عشان تستعملها على مواقع غيرك.\n\n"
            "واجب النهاردة: شغّل الكود ده، واكتب في سطرين: إيه اللي خلّى الهجوم ينجح — التعليق (--) ولا الـ OR ولا الاتنين؟"
        ),
        "en": (
            "🕳️ Lesson 3: How injection happens\n\n"
            "The same code as the last lesson — but the attacker will not type their name; they type this in the name box:\n"
            "' OR '1'='1' -- \n\n"
            "The careless site pastes it into the question, so the question becomes:\n"
            "SELECT * FROM users WHERE username='' OR '1'='1' -- ' AND password='anything'\n\n"
            "What happened?\n"
            "• The -- mark means \"comment\" — the database ignores everything after it (so the password check is gone!)\n"
            "• And '1'='1' is always true — so the database returns the first user it finds\n\n"
            "Try it yourself on your own test database (same setup as the last lesson):\n"
            "name = \"' OR '1'='1' -- \"\n"
            "pw = \"anything\"\n"
            "query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "print(query)\n"
            "cur.execute(query)\n"
            "print(cur.fetchall())\n\n"
            "Result: [('ahmed', '1234')] — they got in without knowing the password! 😱\n\n"
            "⚠️ This is on your own lab only — the goal is to understand the hole so you can close it, not to use it on other people's sites.\n\n"
            "Today's task: run this code, and write in two lines: what made the attack work — the comment (--), the OR, or both?"
        ),
    },
    {
        "title_ar": "الدرس 4: أنواع الحقن",
        "title_en": "Lesson 4: Injection types",
        "ar": (
            "🧩 الدرس 4: أنواع الحقن\n\n"
            "الحقن مش نوع واحد — دي أشهر 4 أنواع، وكل واحد ليه فكرة مختلفة:\n\n"
            "1️⃣ الحقن اللي بيطلع رسالة خطأ (Error-based):\n"
            "المهاجم بيكتب حاجة غلط عمدًا، ورسالة الخطأ نفسها بتفضح معلومات — زي اسم الجدول أو العمود. مثال: صفحة تقول \"no such column: password\" — كده المهاجم عرف إن فيه عمود اسمه حاجة تانية.\n\n"
            "2️⃣ الحقن بـ UNION (Union-based):\n"
            "المهاجم بيلزق استعلام تاني بالـ UNION عشان يسحب بيانات من جدول تاني — مثال: ' UNION SELECT username, password FROM users -- فيرجع له أسماء وكلمات سر كل المستخدمين.\n\n"
            "3️⃣ الحقن الأعمى (Blind):\n"
            "الموقع مش بيطلع أي رسالة ولا بيانات — فالمهاجم بيسأل أسئلة \"صح ولا غلط\" ويستنتج من رد فعل الصفحة. مثال: ' AND (SELECT COUNT(*) FROM users) > 5 -- لو الصفحة فتحت عادي يبقى فيه أكتر من 5 مستخدمين.\n\n"
            "4️⃣ الحقن بالوقت (Time-based):\n"
            "نوع من الأعمى: المهاجم بيطلب من قاعدة البيانات تستنى — مثال: ' AND SLEEP(5) -- لو الصفحة اتأخرت 5 ثواني، يبقى الحقن شغال.\n\n"
            "⚠️ كل الأمثلة دي للفهم بس، وعلى معملك الخاص — مش عشان تجربها على أي موقع.\n\n"
            "واجب النهاردة: اكتب نوع واحد من الأربعة واشرحه لصاحبك بكلامك انت في 3 سطور."
        ),
        "en": (
            "🧩 Lesson 4: Injection types\n\n"
            "Injection is not one type — here are the 4 most famous types, each with a different idea:\n\n"
            "1️⃣ Error-based injection:\n"
            "The attacker types something wrong on purpose, and the error message itself leaks information — like a table or column name. Example: a page says \"no such column: password\" — now the attacker knows there is a different column name.\n\n"
            "2️⃣ Union-based injection:\n"
            "The attacker glues a second query with UNION to pull data from another table — example: ' UNION SELECT username, password FROM users -- which returns all users' names and passwords.\n\n"
            "3️⃣ Blind injection:\n"
            "The site shows no message and no data — so the attacker asks \"true or false\" questions and guesses from the page's reaction. Example: ' AND (SELECT COUNT(*) FROM users) > 5 -- if the page loads normally, there are more than 5 users.\n\n"
            "4️⃣ Time-based injection:\n"
            "A kind of blind: the attacker asks the database to wait — example: ' AND SLEEP(5) -- if the page is 5 seconds late, the injection works.\n\n"
            "⚠️ All these examples are for understanding only, and on your own lab — never to try on any site.\n\n"
            "Today's task: pick one of the four types and explain it to a friend in your own words in 3 lines."
        ),
    },
    {
        "title_ar": "الدرس 5: فين بيستخبى الحقن؟",
        "title_en": "Lesson 5: Where it hides",
        "ar": (
            "🔍 الدرس 5: فين بيستخبى الحقن؟\n\n"
            "الحقن مش في صفحة الدخول بس — أي مكان المستخدم يكتب فيه حاجة ممكن يكون مدخل، لو الكلام ده بيوصل لاستعلام:\n\n"
            "• صفحات الدخول — خانة الاسم وكلمة السر (أشهر مكان)\n"
            "• صناديق البحث — بتكتب كلمة، والموقع بيدوّر بيها في قاعدة البيانات\n"
            "• الروابط — البارامترات اللي في الـ URL زي: site.com/product?id=5 — جرّب تغيّر الـ 5، لو الموقع بياخدها زي ما هي للاستعلام، دي ثغرة محتملة\n"
            "• نماذج التسجيل والتعليقات — الاسم، الإيميل، نص التعليق\n"
            "• أي خانة في أي نموذج — حتى اختيار الدولة أو التصنيف، لو بيتبعت لقاعدة البيانات\n\n"
            "القاعدة الذهبية: أي مدخل من المستخدم = مكان محتمل للحقن. المبرمج الشاطر بيفترض إن كل اللي جاي من المستخدم \"مش مضمون\" لحد ما يتأكد منه.\n\n"
            "⚠️ وانت بتدوّر على الأماكن دي، دوّر في موقعك أو معملك الخاص بس.\n\n"
            "واجب النهاردة: افتح موقعك (أو معملك التجريبي) واكتب قائمة بـ 5 أماكن المستخدم بيكتب فيها حاجة — دي الأماكن اللي لازم تتأكد إنها محمية."
        ),
        "en": (
            "🔍 Lesson 5: Where it hides\n\n"
            "Injection is not only in login pages — any place where a user types something can be an entry point, if that text reaches a query:\n\n"
            "• Login pages — the name and password boxes (the most famous place)\n"
            "• Search boxes — you type a word, and the site searches the database with it\n"
            "• Links — the parameters in the URL like: site.com/product?id=5 — if you change the 5 and the site passes it to the query as-is, that is a possible hole\n"
            "• Registration and comment forms — the name, email, comment text\n"
            "• Any box in any form — even choosing a country or a category, if it is sent to the database\n\n"
            "The golden rule: any input from the user = a possible injection point. A good programmer assumes everything coming from the user is \"untrusted\" until it is checked.\n\n"
            "⚠️ When you look for these places, look only in your own site or your own lab.\n\n"
            "Today's task: open your own site (or your test lab) and write a list of 5 places where the user types something — those are the places you must make sure are protected."
        ),
    },
    {
        "title_ar": "الدرس 6: ليه الحقن خطير؟",
        "title_en": "Lesson 6: The danger",
        "ar": (
            "⚠️ الدرس 6: ليه الحقن خطير؟\n\n"
            "الحقن مش \"حركة ذكية\" وخلاص — ده ممكن يدمّر موقع وشغل صاحبه:\n\n"
            "• سرقة بيانات: إيميلات وكلمات سر وعناوين آلاف المستخدمين — ولو الموقع متجر، ممكن بيانات الدفع كمان\n"
            "• تخطي الدخول: المهاجم يدخل حساب المدير ويتحكم في الموقع كله — يغيّر الأسعار، يمسح المحتوى\n"
            "• مسح البيانات: أمر واحد زي '; DROP TABLE users; -- ممكن يمسح جدول كامل — ولو مفيش نسخة احتياطية، البيانات راحت\n"
            "• الابتزاز: المهاجم يسرق البيانات ويطلب فلوس عشان ما ينشرهاش\n"
            "• المسؤولية القانونية: لو بيانات عملائك اتسربت من موقعك، انت المسؤول قدامهم وقدام القانون — حتى لو انت مش اللي سرقها\n\n"
            "مثال حقيقي مبسط: متجر صغير فيه 10,000 عميل اتسرقت بياناتهم — صاحب المتجر دفع غرامات، وخسر ثقة عملائه، وقفل المتجر. كل ده بسبب ثغرة كان ممكن تتسد بسطر كود واحد (هنشوفه في المستوى التاني).\n\n"
            "واجب النهاردة: اكتب 3 حاجات ممكن تحصل لموقعك لو حد استغل ثغرة حقن فيه — ورتّبهم من الأخطر للأقل خطرًا."
        ),
        "en": (
            "⚠️ Lesson 6: Why it is dangerous\n\n"
            "Injection is not just a \"clever trick\" — it can destroy a site and its owner's work:\n\n"
            "• Data theft: emails, passwords and addresses of thousands of users — and if the site is a shop, payment data too\n"
            "• Login bypass: the attacker enters the admin account and controls the whole site — changing prices, deleting content\n"
            "• Deleting data: one command like '; DROP TABLE users; -- can delete a whole table — and with no backup, the data is gone\n"
            "• Blackmail: the attacker steals the data and asks for money not to publish it\n"
            "• Legal responsibility: if your customers' data leaks from your site, you are responsible before them and before the law — even if you are not the one who stole it\n\n"
            "A simple real example: a small shop with 10,000 customers had their data stolen — the owner paid fines, lost his customers' trust, and closed the shop. All because of a hole that could have been closed with one line of code (we will see it in Level 2).\n\n"
            "Today's task: write 3 things that could happen to your site if someone used an injection hole in it — ordered from most to least dangerous."
        ),
    },
    {
        "title_ar": "الدرس 7: إزاي تعرف إن موقعك فيه الثغرة؟",
        "title_en": "Lesson 7: Spotting the hole",
        "ar": (
            "🕵️ الدرس 7: إزاي تعرف إن موقعك فيه الثغرة؟\n\n"
            "قبل ما تحمي موقعك، لازم تعرف هل فيه الثغرة أصلًا ولا لأ — ودي علامات تدوّر عليها في موقعك أو معملك الخاص:\n\n"
            "1️⃣ جرّب علامة تنصيص واحدة ' في خانة بحث أو دخول — لو الصفحة طلعت رسالة خطأ فيها كلام عن قاعدة بيانات (زي \"SQL syntax\" أو اسم جدول)، دي علامة خطر قوية\n"
            "2️⃣ رسايل الخطأ بتفضح أسماء جداول أو أعمدة — أي رسالة فيها كلام تقني عن قاعدة البيانات معناها إن الخطأ واصل للمستخدم، وده غلط\n"
            "3️⃣ نتايج غريبة: بحث بكلمة عادية يرجّع كل حاجة، أو صفحة بتتصرف بشكل مختلف مع مدخلات غريبة — جرّب ' OR '1'='1 في البحث عندك وشوف النتيجة\n"
            "4️⃣ اختبر على نسخة تجريبية من موقعك — مش على الموقع الشغال ببيانات حقيقية، عشان ما تبوّظش حاجة\n\n"
            "لو لقيت أي علامة من دي، متقلقش — المستوى التاني كله عن إزاي تسد الثغرة دي نهائيًا.\n\n"
            "⚠️ الاختبار ده على موقعك أو معملك الخاص بس — ممنوع تجربه على أي موقع مش بتاعك.\n\n"
            "واجب النهاردة: على معملك التجريبي، جرّب علامة ' في خانة البحث، واكتب اللي حصل بالظبط: طلعت رسالة خطأ؟ ولا الصفحة اشتغلت عادي؟"
        ),
        "en": (
            "🕵️ Lesson 7: Spotting the hole\n\n"
            "Before you protect your site, you need to know whether the hole is even there — here are signs to look for in your own site or lab:\n\n"
            "1️⃣ Try a single quote ' in a search or login box — if the page shows a database error (like \"SQL syntax\" or a table name), that is a strong danger sign\n"
            "2️⃣ Error messages that reveal table or column names — any message with technical database talk means the error reaches the user, and that is wrong\n"
            "3️⃣ Strange results: a search with a normal word returns everything, or a page behaves differently with strange inputs — try ' OR '1'='1 in your own search and see the result\n"
            "4️⃣ Test on a test copy of your site — not on the live site with real data, so you do not break anything\n\n"
            "If you find any of these signs, do not worry — all of Level 2 is about how to close this hole for good.\n\n"
            "⚠️ This testing is only on your own site or lab — never try it on any site that is not yours.\n\n"
            "Today's task: in your test lab, try the ' mark in the search box, and write down exactly what happened: did an error appear? Or did the page work normally?"
        ),
    },
    {
        "title_ar": "الدرس 8: الاستعلامات المُعامَلة",
        "title_en": "Lesson 8: Parameterized queries",
        "ar": (
            "🛡️ الدرس 8: الاستعلامات المُعامَلة — الحل الأول والأهم\n"
            "📗 المستوى التاني: الحماية — دلوقتي هنسد الثغرة نهائيًا.\n\n"
            "الحل السحري اسمه \"الاستعلامات المُعامَلة\" (Parameterized Queries): بدل ما تلزق كلام المستخدم جوه السؤال، بتبعت السؤال والبيانات منفصلين — وقاعدة البيانات بتفهم إن المدخلات \"بيانات\" مش \"أوامر\"، فمستحيل تتنفذ.\n\n"
            "في بايثون (sqlite3) — علامة ? مكان كل قيمة:\n"
            "cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (name, pw))\n\n"
            "جرّب بنفسك — نفس هجوم الدرس التالت، بس بالطريقة الصح (نفس إعداد قاعدة البيانات التجريبية):\n"
            "name = \"' OR '1'='1' -- \"\n"
            "pw = \"anything\"\n"
            "cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (name, pw))\n"
            "print(cur.fetchall())\n\n"
            "النتيجة: [] — فاضي! الهجوم فشل، لأن قاعدة البيانات دوّرت على مستخدم اسمه حرفيًا \"' OR '1'='1' -- \" وملقتوش ✅\n\n"
            "وفي PHP مع MySQL (MySQLi) — نفس الفكرة:\n"
            "$stmt = $conn->prepare(\"SELECT * FROM users WHERE username = ? AND password = ?\");\n"
            "$stmt->bind_param(\"ss\", $username, $password);\n"
            "$stmt->execute();\n"
            "$result = $stmt->get_result();\n\n"
            "⚠️ مثال الـ PHP ده اتأكدنا من سلامة الصياغة بتاعته بـ php -l — جرّبه على سيرفر MySQL الخاص بيك.\n\n"
            "واجب النهاردة: خد كود الدخول الضعيف من الدرس التالت وحوّله للطريقة المُعامَلة، وشغّله بالهجوم وبالدخول الصح — الهجوم لازم يفشل، والدخول الصح لازم ينجح."
        ),
        "en": (
            "🛡️ Lesson 8: Parameterized queries — the first and most important fix\n"
            "📗 Level 2: Protection — now we close the hole for good.\n\n"
            "The magic fix is called \"parameterized queries\": instead of pasting the user's text inside the question, you send the question and the data separately — and the database understands the input is \"data\", not \"commands\", so it can never run as code.\n\n"
            "In Python (sqlite3) — a ? mark in place of every value:\n"
            "cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (name, pw))\n\n"
            "Try it yourself — the same attack from Lesson 3, but the right way (same test database setup):\n"
            "name = \"' OR '1'='1' -- \"\n"
            "pw = \"anything\"\n"
            "cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (name, pw))\n"
            "print(cur.fetchall())\n\n"
            "Result: [] — empty! The attack failed, because the database looked for a user literally named \"' OR '1'='1' -- \" and found none ✅\n\n"
            "And in PHP with MySQL (MySQLi) — the same idea:\n"
            "$stmt = $conn->prepare(\"SELECT * FROM users WHERE username = ? AND password = ?\");\n"
            "$stmt->bind_param(\"ss\", $username, $password);\n"
            "$stmt->execute();\n"
            "$result = $stmt->get_result();\n\n"
            "⚠️ We checked this PHP example's syntax with php -l — try it on your own MySQL server.\n\n"
            "Today's task: take the weak login code from Lesson 3, change it to the parameterized way, and run it with the attack and with the correct login — the attack must fail, and the correct login must work."
        ),
    },
    {
        "title_ar": "الدرس 9: التحقق من المدخلات",
        "title_en": "Lesson 9: Validating input",
        "ar": (
            "✅ الدرس 9: التحقق من المدخلات\n\n"
            "الطبقة التانية من الحماية: قبل ما المدخلات توصل لقاعدة البيانات أصلًا، اتأكد إنها بالشكل المتوقع.\n\n"
            "القواعد:\n"
            "• الرقم لازم يبقى رقم: لو بتستقبل id، حوّله لـ int — ولو التحويل فشل، ارفض المدخلات\n"
            "• النص ليه شكل محدد: اسم المستخدم مثلًا حروف وأرقام و _ بس، وبطول معين (3 لـ 20 حرف)\n"
            "• حدّد الطول: مفيش اسم مستخدم طوله 500 حرف!\n\n"
            "جرّب الكود ده:\n"
            "import re\n"
            "def valid_username(name):\n"
            "    return re.fullmatch(r\"[A-Za-z0-9_]{3,20}\", name) is not None\n"
            "print(valid_username(\"ahmed_1\"))\n"
            "print(valid_username(\"' OR '1'='1\"))\n"
            "def to_id(text):\n"
            "    try:\n"
            "        return int(text)\n"
            "    except ValueError:\n"
            "        return None\n"
            "print(to_id(\"25\"))\n"
            "print(to_id(\"5 OR 1=1\"))\n\n"
            "النتيجة: True، وبعدين False، وبعدين 25، وبعدين None — يعني المدخلات المشبوهة اترفضت قبل ما توصل لقاعدة البيانات ✅\n\n"
            "⚠️ مهم: التحقق طبقة تانية مش بديل — مدخلات شكلها سليم ممكن تبقى هجوم برضه. الاستعلامات المُعامَلة (الدرس اللي فات) هي الأساس، والتحقق بييجي فوقها.\n\n"
            "واجب النهاردة: اكتب دالة تحقق للإيميل (لازم يبقى فيه @ ونقطة) وجرّبها على إيميل صح وإيميل فيه علامة ' ."
        ),
        "en": (
            "✅ Lesson 9: Validating input\n\n"
            "The second layer of protection: before input even reaches the database, make sure it looks the way you expect.\n\n"
            "The rules:\n"
            "• A number must be a number: if you expect an id, convert it to int — and if the conversion fails, reject the input\n"
            "• Text has a fixed shape: a username, for example, is only letters, numbers and _ , with a set length (3 to 20 characters)\n"
            "• Limit the length: no username is 500 characters long!\n\n"
            "Try this code:\n"
            "import re\n"
            "def valid_username(name):\n"
            "    return re.fullmatch(r\"[A-Za-z0-9_]{3,20}\", name) is not None\n"
            "print(valid_username(\"ahmed_1\"))\n"
            "print(valid_username(\"' OR '1'='1\"))\n"
            "def to_id(text):\n"
            "    try:\n"
            "        return int(text)\n"
            "    except ValueError:\n"
            "        return None\n"
            "print(to_id(\"25\"))\n"
            "print(to_id(\"5 OR 1=1\"))\n\n"
            "Result: True, then False, then 25, then None — the suspicious inputs were rejected before reaching the database ✅\n\n"
            "⚠️ Important: validation is a second layer, not a replacement — input that looks fine can still be an attack. Parameterized queries (last lesson) are the foundation, and validation sits on top.\n\n"
            "Today's task: write a validation function for an email (it must have @ and a dot) and try it on a good email and on an email containing a ' mark."
        ),
    },
    {
        "title_ar": "الدرس 10: أقل صلاحية لحساب قاعدة البيانات",
        "title_en": "Lesson 10: Least privilege",
        "ar": (
            "🔑 الدرس 10: أقل صلاحية لحساب قاعدة البيانات\n\n"
            "تخيل إن المهاجم نجح في الحقن رغم كل حاجة — إيه اللي يقدر يعمله؟ ده بيعتمد على صلاحيات حساب قاعدة البيانات اللي الموقع بيستخدمه!\n\n"
            "لو حساب الموقع هو المدير (root/admin)، المهاجم يقدر يعمل أي حاجة: يمسح جداول، يعمل حسابات جديدة، يشوف كل قواعد البيانات.\n\n"
            "لكن لو حساب الموقع محدود، الضرر محدود. القاعدة: ادّي حساب الموقع أقل صلاحية ممكنة — اللي يحتاجه بس:\n\n"
            "أوامر MySQL — بتتنفذ على سيرفر MySQL الخاص بيك:\n"
            "CREATE USER 'website'@'localhost' IDENTIFIED BY 'Put-A-Strong-Password-Here';\n"
            "GRANT SELECT, INSERT, UPDATE ON shop.* TO 'website'@'localhost';\n"
            "FLUSH PRIVILEGES;\n\n"
            "يعني: حساب اسمه website يقدر يقرأ ويضيف ويعدّل في قاعدة بيانات المتجر بس — لا يقدر يمسح (DELETE)، ولا يمسح جداول (DROP)، ولا يشوف قواعد بيانات تانية.\n\n"
            "وفي SQLite (مفيش حسابات ومستخدمين): البديل إن ملف قاعدة البيانات يبقى برّه المجلد العام للموقع، ويبقى عندك نسخة احتياطية يومية — لو حصل حاجة، ترجّعها.\n\n"
            "واجب النهاردة: شوف موقعك (أو اسأل اللي مستضيفه): حساب قاعدة البيانات بتاع الموقع صلاحياته إيه؟ لو هو المدير، اكتب خطة تقلل صلاحياته."
        ),
        "en": (
            "🔑 Lesson 10: Least privilege\n\n"
            "Imagine the attacker succeeds with injection despite everything — what can they do? That depends on the permissions of the database account the site uses!\n\n"
            "If the site's account is the admin (root/admin), the attacker can do anything: delete tables, create new accounts, see all databases.\n\n"
            "But if the site's account is limited, the damage is limited. The rule: give the site's account the smallest permissions possible — only what it needs:\n\n"
            "MySQL commands — run them on your own MySQL server:\n"
            "CREATE USER 'website'@'localhost' IDENTIFIED BY 'Put-A-Strong-Password-Here';\n"
            "GRANT SELECT, INSERT, UPDATE ON shop.* TO 'website'@'localhost';\n"
            "FLUSH PRIVILEGES;\n\n"
            "Meaning: an account called website can only read, add and edit in the shop database — it cannot delete rows (DELETE), cannot drop tables (DROP), and cannot see other databases.\n\n"
            "And in SQLite (no accounts and users): the alternative is to keep the database file outside the site's public folder, and keep a daily backup — if something happens, you restore it.\n\n"
            "Today's task: check your site (or ask your host): what permissions does the site's database account have? If it is the admin, write a plan to reduce its permissions."
        ),
    },
    {
        "title_ar": "الدرس 11: الإجراءات المخزنة",
        "title_en": "Lesson 11: Stored procedures",
        "ar": (
            "📦 الدرس 11: الإجراءات المخزنة\n\n"
            "الإجراء المخزن (Stored Procedure) يعني الاستعلام نفسه يبقى محفوظ جوه قاعدة البيانات — والموقع بيناديه باسمه ويبعت له البيانات منفصلة. كده منطق الاستعلام ثابت ومحدش يقدر يغيّره من برّه.\n\n"
            "مثال MySQL — بيتكتب مرة واحدة على سيرفر MySQL الخاص بيك:\n"
            "DELIMITER //\n"
            "CREATE PROCEDURE login_user(IN u VARCHAR(50), IN p VARCHAR(50))\n"
            "BEGIN SELECT * FROM users WHERE username = u AND password = p; END //\n"
            "DELIMITER ;\n"
            "CALL login_user('ahmed', '1234');\n\n"
            "المدخلات هنا بتتبعت كقيم (u و p) مش كجزء من نص الاستعلام — فمستحيل تتحول لأوامر.\n\n"
            "وفي بايثون نفس المبدأ بدالة بتغلّف الاستعلام المُعامَل — جرّب:\n"
            "def get_user(conn, username):\n"
            "    cur = conn.cursor()\n"
            "    cur.execute(\"SELECT * FROM users WHERE username=?\", (username,))\n"
            "    return cur.fetchone()\n"
            "print(get_user(conn, \"ahmed\"))\n"
            "print(get_user(conn, \"' OR '1'='1\"))\n\n"
            "النتيجة: ('ahmed', '1234')، وبعدين None — الدالة دي هي \"الإجراء المخزن\" بتاعك في بايثون ✅\n\n"
            "⚠️ ملحوظة: الإجراءات المخزنة بتساعد بس مش بديل — لو بنيت النداء نفسه باللزق (concatenation)، رجعت للثغرة تاني. القاعدة الذهبية لسه هي: البيانات منفصلة عن الاستعلام.\n\n"
            "واجب النهاردة: حوّل أي استعلام في مشروعك لدالة زي get_user دي — استعلام ثابت جوّه الدالة، والمدخلات بتتبعت كقيم."
        ),
        "en": (
            "📦 Lesson 11: Stored procedures\n\n"
            "A stored procedure means the query itself is saved inside the database — and the site calls it by name and sends the data separately. That way the query logic is fixed and nobody can change it from outside.\n\n"
            "MySQL example — written once on your own MySQL server:\n"
            "DELIMITER //\n"
            "CREATE PROCEDURE login_user(IN u VARCHAR(50), IN p VARCHAR(50))\n"
            "BEGIN SELECT * FROM users WHERE username = u AND password = p; END //\n"
            "DELIMITER ;\n"
            "CALL login_user('ahmed', '1234');\n\n"
            "The inputs here are sent as values (u and p), not as part of the query text — so they can never turn into commands.\n\n"
            "And in Python the same idea with a function wrapping a parameterized query — try it:\n"
            "def get_user(conn, username):\n"
            "    cur = conn.cursor()\n"
            "    cur.execute(\"SELECT * FROM users WHERE username=?\", (username,))\n"
            "    return cur.fetchone()\n"
            "print(get_user(conn, \"ahmed\"))\n"
            "print(get_user(conn, \"' OR '1'='1\"))\n\n"
            "Result: ('ahmed', '1234'), then None — this function is your \"stored procedure\" in Python ✅\n\n"
            "⚠️ Note: stored procedures help but are not a replacement — if you build the call itself with concatenation, you are back to the hole. The golden rule stays: data separate from the query.\n\n"
            "Today's task: turn any query in your project into a function like get_user — a fixed query inside the function, and inputs sent as values."
        ),
    },
    {
        "title_ar": "الدرس 12: ليه الـ escaping مش كفاية",
        "title_en": "Lesson 12: Why escaping fails",
        "ar": (
            "🧯 الدرس 12: الـ escaping وليه مش كفاية لوحده\n\n"
            "الـ escaping يعني تهرب من علامات التنصيص — تحوّل ' لـ '' عشان قاعدة البيانات تفهمها كحرف عادي مش كنهاية للنص.\n\n"
            "جرّب — الهروب شغال هنا:\n"
            "name = \"' OR '1'='1\"\n"
            "safe = name.replace(\"'\", \"''\")\n"
            "query = f\"SELECT * FROM users WHERE username='{safe}'\"\n"
            "cur.execute(query)\n"
            "print(cur.fetchall())\n\n"
            "النتيجة: [] — الهجوم فشل ✅ بس استنى… شوف الحقن الرقمي — مفيش علامات تنصيص أصلًا عشان تهرب منها:\n"
            "cur.execute(\"CREATE TABLE products (id INTEGER, name TEXT)\")\n"
            "cur.execute(\"INSERT INTO products VALUES (1, 'phone'), (2, 'laptop')\")\n"
            "conn.commit()\n"
            "user_id = \"1 OR 1=1\"\n"
            "query2 = f\"SELECT * FROM products WHERE id={user_id}\"\n"
            "cur.execute(query2)\n"
            "print(cur.fetchall())\n\n"
            "النتيجة: [(1, 'phone'), (2, 'laptop')] — كل المنتجات! 😱 الهروب ما عملش حاجة لأن مفيش ' في المدخلات أصلًا.\n\n"
            "وكمان: كل قاعدة بيانات ليها طريقة هروب مختلفة — ولو نسيت مكان واحد، الثغرة رجعت. والمدخلات المتخزنة (second-order) ممكن تتخزن سليمة وتتنفذ بعدين.\n\n"
            "الخلاصة: الـ escaping زي حزام الأمان — والاستعلامات المُعامَلة هي الفرامل. استخدم الفرامل (الدرس 8)، والحزام زيادة أمان مش أكتر.\n\n"
            "واجب النهاردة: جرّب الكودين اللي فوق، واكتب في سطرين: ليه الهروب نفع في الأول وفشل في التاني؟"
        ),
        "en": (
            "🧯 Lesson 12: Escaping is not enough\n\n"
            "Escaping means running away from quote marks — turning ' into '' so the database reads it as a normal character, not as the end of the text.\n\n"
            "Try it — escaping works here:\n"
            "name = \"' OR '1'='1\"\n"
            "safe = name.replace(\"'\", \"''\")\n"
            "query = f\"SELECT * FROM users WHERE username='{safe}'\"\n"
            "cur.execute(query)\n"
            "print(cur.fetchall())\n\n"
            "Result: [] — the attack failed ✅ But wait… look at numeric injection — there are no quotes at all to escape:\n"
            "cur.execute(\"CREATE TABLE products (id INTEGER, name TEXT)\")\n"
            "cur.execute(\"INSERT INTO products VALUES (1, 'phone'), (2, 'laptop')\")\n"
            "conn.commit()\n"
            "user_id = \"1 OR 1=1\"\n"
            "query2 = f\"SELECT * FROM products WHERE id={user_id}\"\n"
            "cur.execute(query2)\n"
            "print(cur.fetchall())\n\n"
            "Result: [(1, 'phone'), (2, 'laptop')] — all the products! 😱 Escaping did nothing because there is no ' in the input at all.\n\n"
            "Also: every database escapes differently — and if you forget one place, the hole is back. And stored input (second-order) can be stored safely and run later.\n\n"
            "The summary: escaping is like a seatbelt — and parameterized queries are the brakes. Use the brakes (Lesson 8); the seatbelt is only extra safety.\n\n"
            "Today's task: run both code examples above, and write in two lines: why did escaping work in the first one and fail in the second?"
        ),
    },
    {
        "title_ar": "الدرس 13: أساسيات الـ WAF",
        "title_en": "Lesson 13: WAF basics",
        "ar": (
            "🧱 الدرس 13: أساسيات الـ WAF\n\n"
            "الـ WAF يعني جدار حماية لتطبيقات الويب (Web Application Firewall) — حارس واقف قدام موقعك، بيفحص كل طلب داخل، ولو لقى حاجة مشبوهة بيمنعها قبل ما توصل للكود بتاعك.\n\n"
            "إيه اللي بيمنعه؟ أنماط معروفة زي: ' OR 1=1، و UNION SELECT، و -- ، و DROP TABLE — يعني نفس حركات الحقن اللي اتعلمناها.\n\n"
            "أشهر مثال مجاني: ModSecurity مع مجموعة قواعد OWASP — قاعدة زي دي:\n"
            "SecRule ARGS \"@rx (?i:union\\s+select)\" \"id:1001,deny,msg:'Possible SQL injection'\"\n\n"
            "معناها: لو أي مدخلات فيها \"union select\" (بأي حالة حروف)، امنع الطلب وسجّل \"حقن محتمل\".\n\n"
            "⚠️ بس خد بالك من حاجتين:\n"
            "• الـ WAF شبكة أمان مش علاج — المهاجم ممكن يلف عليه (بترميز الحروف مثلًا)، فإصلاح الكود الأول (الاستعلامات المُعامَلة) وبعدين الـ WAF\n"
            "• القواعد ممكن تمنع مستخدم عادي بالغلط — لازم تراقب سجلاته وتظبطه\n\n"
            "واجب النهاردة: دوّر على \"ModSecurity OWASP\" واكتب في سطرين: إيه هو، وهل استضافة موقعك بتوفره ولا لأ؟"
        ),
        "en": (
            "🧱 Lesson 13: WAF basics\n\n"
            "A WAF (Web Application Firewall) is a guard standing in front of your site — it checks every incoming request, and if it finds something suspicious it blocks it before it reaches your code.\n\n"
            "What does it block? Known patterns like: ' OR 1=1, UNION SELECT, --, and DROP TABLE — the same injection moves we learned.\n\n"
            "The most famous free example: ModSecurity with the OWASP rule set — a rule like this:\n"
            "SecRule ARGS \"@rx (?i:union\\s+select)\" \"id:1001,deny,msg:'Possible SQL injection'\"\n\n"
            "Meaning: if any input contains \"union select\" (in any letter case), block the request and log \"possible SQL injection\".\n\n"
            "⚠️ But watch out for two things:\n"
            "• The WAF is a safety net, not a cure — attackers can go around it (by encoding characters, for example), so fix the code first (parameterized queries), then the WAF\n"
            "• The rules can block a normal user by mistake — you must watch its logs and tune it\n\n"
            "Today's task: search for \"ModSecurity OWASP\" and write in two lines: what it is, and does your site's hosting offer it or not?"
        ),
    },
    {
        "title_ar": "الدرس 14: إخفاء رسائل خطأ قاعدة البيانات",
        "title_en": "Lesson 14: Hiding DB errors",
        "ar": (
            "🙈 الدرس 14: إخفاء رسائل خطأ قاعدة البيانات\n\n"
            "فاكر الحقن اللي بيطلع رسالة خطأ (الدرس 4)؟ المهاجم بيستفيد من رسايل الخطأ عشان يعرف أسماء الجداول والأعمدة — فأول خطوة: المستخدم العادي ميشوفش رسايل قاعدة البيانات أبدًا.\n\n"
            "القاعدة: رسالة عامة للمستخدم + التفاصيل في سجل خاص بيك انت بس.\n\n"
            "جرّب الكود ده:\n"
            "def login(name, pw):\n"
            "    try:\n"
            "        cur.execute(\"SELECT * FROM missing_table WHERE username=?\", (name,))\n"
            "        return cur.fetchall()\n"
            "    except Exception as e:\n"
            "        with open(\"/tmp/errors.log\", \"a\", encoding=\"utf-8\") as f:\n"
            "            f.write(f\"DB error: {e}\\n\")\n"
            "        return \"حصلت مشكلة، جرّب تاني بعد شوية\"\n"
            "print(login(\"ahmed\", \"1234\"))\n\n"
            "المستخدم هيشوف بس: \"حصلت مشكلة، جرّب تاني بعد شوية\" — لكن انت هتلاقي في ملف errors.log السطر ده:\n"
            "DB error: no such table: missing_table\n\n"
            "كده المهاجم مش هيعرف أي حاجة عن قاعدة بياناتك، وانت لسه شايف كل التفاصيل عشان تصلحها.\n\n"
            "واجب النهاردة: دوّر في كود موقعك (أو معملك) على أي مكان بيطبع رسالة خطأ قاعدة بيانات للمستخدم — وغيّرها لرسالة عامة + سجل خاص."
        ),
        "en": (
            "🙈 Lesson 14: Hiding DB errors\n\n"
            "Remember error-based injection (Lesson 4)? The attacker uses error messages to learn table and column names — so the first step is: the normal user must never see database errors.\n\n"
            "The rule: a generic message for the user + the details in a private log only for you.\n\n"
            "Try this code:\n"
            "def login(name, pw):\n"
            "    try:\n"
            "        cur.execute(\"SELECT * FROM missing_table WHERE username=?\", (name,))\n"
            "        return cur.fetchall()\n"
            "    except Exception as e:\n"
            "        with open(\"/tmp/errors.log\", \"a\", encoding=\"utf-8\") as f:\n"
            "            f.write(f\"DB error: {e}\\n\")\n"
            "        return \"Something went wrong, try again in a bit\"\n"
            "print(login(\"ahmed\", \"1234\"))\n\n"
            "The user only sees: \"Something went wrong, try again in a bit\" — but you will find this line in the errors.log file:\n"
            "DB error: no such table: missing_table\n\n"
            "That way the attacker learns nothing about your database, and you still see all the details so you can fix them.\n\n"
            "Today's task: look in your site's code (or your lab) for any place that prints a database error to the user — and change it to a generic message + a private log."
        ),
    },
    {
        "title_ar": "الدرس 15: معمل الاختبار الخاص بيك",
        "title_en": "Lesson 15: Your test lab",
        "ar": (
            "🧪 الدرس 15: جهّز معمل اختبار خاص بيك\n"
            "📗 المستوى التالت: اختبار وإصلاح متقدم — دلوقتي هنختبر ونصلح زي المحترفين.\n\n"
            "المحترف مش بيختبر على موقع شغال — بيعمل معمل صغير على جهازه، فيه نسخة ضعيفة من التطبيق، ويكسرها ويصلحها براحته من غير ما يأذي حد.\n\n"
            "جهّز معملك في 4 خطوات:\n"
            "1️⃣ بايثون + sqlite3 — موجودين عندك أصلًا من درس بايثون الأول\n"
            "2️⃣ قاعدة بيانات تجريبية ببيانات وهمية — زي جدول users اللي عملناه (ahmed / 1234) — ممنوع بيانات حقيقية في المعمل\n"
            "3️⃣ نسخة ضعيفة من صفحة الدخول — احفظ الكود ده في ملف lab_login.py على جهازك:\n"
            "import sqlite3\n"
            "conn = sqlite3.connect(\":memory:\")\n"
            "cur = conn.cursor()\n"
            "cur.execute(\"CREATE TABLE users (username TEXT, password TEXT)\")\n"
            "cur.execute(\"INSERT INTO users VALUES ('ahmed', '1234')\")\n"
            "conn.commit()\n"
            "def weak_login(name, pw):\n"
            "    query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "    cur.execute(query)\n"
            "    return cur.fetchall()\n"
            "print(weak_login(\"ahmed\", \"1234\"))\n"
            "print(weak_login(\"' OR '1'='1' -- \", \"x\"))\n\n"
            "النتيجة: الدخول الصح بيرجع الصف، والهجوم بيرجع الصف برضه — المعمل جاهز، والثغرة قدام عينك.\n\n"
            "4️⃣ القاعدة الذهبية: المعمل على جهازك بس، وبتختبر فيه موقعك انت بس — تجربة أي موقع مش بتاعك ممنوعة بالقانون، حتى لو نيتك سليمة. ولو لقيت ثغرة في موقع غيرك بالصدفة، بلّغ صاحبه بأدب من غير ما تستغلها.\n\n"
            "واجب النهاردة: اعمل ملف lab_login.py عندك وشغّله — وتأكد إن السطرين بيطبعوا نفس النتيجة (يعني الثغرة موجودة في المعمل)."
        ),
        "en": (
            "🧪 Lesson 15: Building your lab\n"
            "📗 Level 3: Advanced testing & fixing — now we test and fix like professionals.\n\n"
            "A professional never tests on a live site — they build a small lab on their machine, with a weak copy of the app, and break it and fix it freely without hurting anyone.\n\n"
            "Set up your lab in 4 steps:\n"
            "1️⃣ Python + sqlite3 — you already have them from the first Python lesson\n"
            "2️⃣ A test database with fake data — like the users table we made (ahmed / 1234) — never real data in the lab\n"
            "3️⃣ A weak copy of the login page — save this code in a file called lab_login.py on your machine:\n"
            "import sqlite3\n"
            "conn = sqlite3.connect(\":memory:\")\n"
            "cur = conn.cursor()\n"
            "cur.execute(\"CREATE TABLE users (username TEXT, password TEXT)\")\n"
            "cur.execute(\"INSERT INTO users VALUES ('ahmed', '1234')\")\n"
            "conn.commit()\n"
            "def weak_login(name, pw):\n"
            "    query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "    cur.execute(query)\n"
            "    return cur.fetchall()\n"
            "print(weak_login(\"ahmed\", \"1234\"))\n"
            "print(weak_login(\"' OR '1'='1' -- \", \"x\"))\n\n"
            "Result: the correct login returns the row, and the attack returns the row too — the lab is ready, and the hole is right in front of you.\n\n"
            "4️⃣ The golden rule: the lab is on your machine only, and you test your own site only — testing any site that is not yours is forbidden by law, even with good intentions. And if you find a hole in someone else's site by accident, tell its owner politely without using it.\n\n"
            "Today's task: make the lab_login.py file and run it — and make sure both lines print the same result (meaning the hole exists in the lab)."
        ),
    },
    {
        "title_ar": "الدرس 16: اختبر موقعك بأداة زي sqlmap",
        "title_en": "Lesson 16: Testing with sqlmap",
        "ar": (
            "🔎 الدرس 16: اختبر موقعك بأداة زي sqlmap\n\n"
            "الـ sqlmap أداة مجانية ومشهورة بتختبر الحقن أوتوماتيك — بدل ما تجرّب بإيدك، هي بتجرّب مئات الحركات وتقولك: \"البارامتر ده ضعيف\" ولا \"سليم\".\n\n"
            "⚠️ تنبيه قبل أي حاجة: الـ sqlmap بتتشغل على معملك أو موقعك الخاص بس — تشغيلها على أي موقع مش بتاعك ممنوع بالقانون، حتى لو \"للتجربة\".\n\n"
            "التثبيت (على جهازك):\n"
            "pip install sqlmap\n"
            "ولو pip رفض على لينكس وقال externally-managed-environment، جرّب: sudo apt install sqlmap\n\n"
            "أمر الفحص على تطبيق تجريبي شغال على جهازك (localhost):\n"
            "sqlmap -u \"http://127.0.0.1:8000/login?user=test\" --batch --level 1\n\n"
            "إيه اللي بيحصل؟\n"
            "• -u: رابط الصفحة اللي هتتفحص — ولازم يبقى تطبيقك انت على جهازك\n"
            "• --batch: متسألنيش، كمّل لوحدك بالاختيارات الافتراضية\n"
            "• --level 1: اختبار خفيف — كفاية للبداية (المستويات الأعلى بتجرّب أكتر)\n\n"
            "لو لقى ثغرة، هيقولك حاجة زي: \"parameter 'user' is vulnerable\" — يعني البارامتر user ضعيف. ولو ملقاش، هيقول: \"all tested parameters do not appear to be injectable\" — يعني سليم.\n\n"
            "واجب النهاردة: نزّل sqlmap على جهازك (pip install sqlmap) وشغّل sqlmap --version — لازم تشوف رقم الإصدار. ومتفحصش أي رابط غير رابط معملك الخاص."
        ),
        "en": (
            "🔎 Lesson 16: Testing with sqlmap\n\n"
            "sqlmap is a free and famous tool that tests injection automatically — instead of trying by hand, it tries hundreds of tricks and tells you: \"this parameter is weak\" or \"it is safe\".\n\n"
            "⚠️ A warning before anything: sqlmap runs only on your own lab or your own site — running it on any site that is not yours is forbidden by law, even \"just to try\".\n\n"
            "Install (on your machine):\n"
            "pip install sqlmap\n"
            "If pip refuses on Linux (externally-managed-environment), try: sudo apt install sqlmap\n\n"
            "The scan command on a test app running on your machine (localhost):\n"
            "sqlmap -u \"http://127.0.0.1:8000/login?user=test\" --batch --level 1\n\n"
            "What happens?\n"
            "• -u: the page URL to scan — it must be your own app on your machine\n"
            "• --batch: do not ask me, continue with the default choices\n"
            "• --level 1: a light test — enough for the start (higher levels try more)\n\n"
            "If it finds a hole, it will say something like: \"parameter 'user' is vulnerable\" — meaning the user parameter is weak. And if it finds nothing, it will say: \"all tested parameters do not appear to be injectable\" — meaning it is safe.\n\n"
            "Today's task: install sqlmap on your machine (pip install sqlmap) and run sqlmap --version — you should see the version number. And do not scan any link except your own lab's link."
        ),
    },
    {
        "title_ar": "الدرس 17: قراءة تقرير الفحص",
        "title_en": "Lesson 17: Reading reports",
        "ar": (
            "📋 الدرس 17: اقرأ تقرير الفحص وصلّح اللي فيه\n\n"
            "الفحص لوحده مش كفاية — لازم تعرف تقرأ التقرير وتحول كل سطر فيه لإصلاح.\n\n"
            "ده شكل جزء من تقرير sqlmap (مثال توضيحي):\n"
            "Parameter: user (GET)\n"
            "Type: boolean-based blind\n"
            "Title: AND boolean-based blind - WHERE or HAVING clause\n"
            "Payload: user=test' AND 1234=1234--\n\n"
            "يعني إيه كل سطر؟\n"
            "• Parameter: user — الثغرة في البارامتر user (اللي بييجي من الرابط)\n"
            "• Type: boolean-based blind — نوع الحقن (أعمى — زي الدرس 4)\n"
            "• Payload — الحركة اللي نجحت: ' AND 1234=1234 — يعني الشرط اتحقّق وعدّى\n\n"
            "خطوات الإصلاح بالترتيب:\n"
            "1️⃣ رتّب حسب الخطورة: الدخول والبحث الأول، وبعدين الباقي\n"
            "2️⃣ صلّح بالاستعلامات المُعامَلة (الدرس 8) — ده الإصلاح الحقيقي، مش إخفاء المشكلة\n"
            "3️⃣ أعد الفحص بعد الإصلاح — لازم التقرير يقول: \"all tested parameters do not appear to be injectable\"\n"
            "4️⃣ لو التقرير لسه بيقول إن فيه ثغرة، يبقى الإصلاح موصلش للمكان الصح — دوّر تاني\n\n"
            "⚠️ التقرير ده على معملك أو موقعك الخاص بس — ومتشاركش تقارير فحص مواقع غيرك مع حد.\n\n"
            "واجب النهاردة: اكتب خطة إصلاح من 3 خطوات لثغرة وهمية في بارامتر \"search\": إيه اللي هتصلحه الأول، وإزاي هتتأكد إن الإصلاح نجح؟"
        ),
        "en": (
            "📋 Lesson 17: Reading scan reports\n\n"
            "Scanning alone is not enough — you must know how to read the report and turn every line in it into a fix.\n\n"
            "This is what part of a sqlmap report looks like (an example):\n"
            "Parameter: user (GET)\n"
            "Type: boolean-based blind\n"
            "Title: AND boolean-based blind - WHERE or HAVING clause\n"
            "Payload: user=test' AND 1234=1234--\n\n"
            "What does each line mean?\n"
            "• Parameter: user — the hole is in the user parameter (the one from the link)\n"
            "• Type: boolean-based blind — the injection type (blind — like Lesson 4)\n"
            "• Payload — the trick that worked: ' AND 1234=1234 — meaning the condition was true and passed\n\n"
            "Fix steps in order:\n"
            "1️⃣ Order by danger: login and search first, then the rest\n"
            "2️⃣ Fix with parameterized queries (Lesson 8) — that is the real fix, not hiding the problem\n"
            "3️⃣ Re-scan after fixing — the report must say: \"all tested parameters do not appear to be injectable\"\n"
            "4️⃣ If the report still says there is a hole, the fix did not reach the right place — look again\n\n"
            "⚠️ This report is about your own lab or site only — and never share scan reports of other people's sites with anyone.\n\n"
            "Today's task: write a 3-step fix plan for an imaginary hole in a \"search\" parameter: what will you fix first, and how will you make sure the fix worked?"
        ),
    },
    {
        "title_ar": "الدرس 18: أنماط كود ضعيفة وإزاي تصلحها",
        "title_en": "Lesson 18: Fixing weak code",
        "ar": (
            "🔧 الدرس 18: أنماط كود ضعيفة حقيقية وإزاي تصلحها\n\n"
            "دلوقتي هنشوف 3 أنماط ضعيفة حقيقية — كل واحد قبل وبعد — وجرّبهم بنفسك على قاعدة بيانات تجريبية:\n\n"
            "1️⃣ الدخول باللزق (شفناه في الدرس 3):\n"
            "query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "الإصلاح: cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (name, pw))\n\n"
            "2️⃣ رقم من الرابط من غير تحويل:\n"
            "user_id = \"1 OR 1=1\"\n"
            "query = f\"SELECT * FROM products WHERE id={user_id}\"\n"
            "هيرجع كل المنتجات! الإصلاح: حوّل لرقم الأول وبعدين استعلم بالـ ?:\n"
            "user_id = int(\"1\")\n"
            "cur.execute(\"SELECT * FROM products WHERE id=?\", (user_id,))\n\n"
            "3️⃣ البحث بالـ LIKE واللزق:\n"
            "q = \"' OR '1'='1' -- \"\n"
            "query = f\"SELECT * FROM products WHERE name LIKE '%{q}%'\"\n"
            "هيرجع كل المنتجات برضه! الإصلاح: النمط نفسه يتبعت كقيمة:\n"
            "cur.execute(\"SELECT * FROM products WHERE name LIKE ?\", (\"%\" + \"phone\" + \"%\",))\n\n"
            "القاعدة اللي بتربط التلاتة: أي حاجة جاية من المستخدم بتتبعت كقيمة منفصلة (؟)، ومبتتلزقش أبدًا جوه نص الاستعلام.\n\n"
            "واجب النهاردة: خد النمط رقم 2 وجرّبه بنفسك: شغّل النسخة الضعيفة بـ \"1 OR 1=1\" وشوفها بترجع كل حاجة، وبعدين شغّل النسخة المصلحة بـ 1 وشوفها بترجع منتج واحد بس."
        ),
        "en": (
            "🔧 Lesson 18: Fixing weak patterns\n\n"
            "Now we will see 3 real weak patterns — each one before and after — and try them yourself on a test database:\n\n"
            "1️⃣ Login with gluing (we saw it in Lesson 3):\n"
            "query = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "The fix: cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (name, pw))\n\n"
            "2️⃣ A number from the link without converting:\n"
            "user_id = \"1 OR 1=1\"\n"
            "query = f\"SELECT * FROM products WHERE id={user_id}\"\n"
            "It returns all products! The fix: convert to a number first, then query with ?:\n"
            "user_id = int(\"1\")\n"
            "cur.execute(\"SELECT * FROM products WHERE id=?\", (user_id,))\n\n"
            "3️⃣ Search with LIKE and gluing:\n"
            "q = \"' OR '1'='1' -- \"\n"
            "query = f\"SELECT * FROM products WHERE name LIKE '%{q}%'\"\n"
            "It returns all products too! The fix: the pattern itself is sent as a value:\n"
            "cur.execute(\"SELECT * FROM products WHERE name LIKE ?\", (\"%\" + \"phone\" + \"%\",))\n\n"
            "The rule behind all three: anything coming from the user is sent as a separate value (?), and is never glued inside the query text.\n\n"
            "Today's task: take pattern 2 and try it yourself: run the weak version with \"1 OR 1=1\" and see it return everything, then run the fixed version with 1 and see it return only one product."
        ),
    },
    {
        "title_ar": "الدرس 19: دخول وبحث آمنين من الصفر",
        "title_en": "Lesson 19: Secure login & search",
        "ar": (
            "🏗️ الدرس 19: تنفيذ دخول وبحث آمنين من الصفر\n\n"
            "دلوقتي هنجمع كل اللي اتعلمناه في كود كامل ونضيف — دخول وبحث آمنين من أول سطر:\n\n"
            "def secure_login(conn, username, password):\n"
            "    cur = conn.cursor()\n"
            "    cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (username, password))\n"
            "    return cur.fetchone() is not None\n"
            "def secure_search(conn, keyword):\n"
            "    if len(keyword) > 50:\n"
            "        return []\n"
            "    cur = conn.cursor()\n"
            "    cur.execute(\"SELECT * FROM products WHERE name LIKE ?\", (\"%\" + keyword + \"%\",))\n"
            "    return cur.fetchall()\n\n"
            "جرّب على قاعدة البيانات التجريبية (users فيها ahmed/1234، وproducts فيها phone و laptop):\n"
            "print(secure_login(conn, \"ahmed\", \"1234\"))\n"
            "print(secure_login(conn, \"' OR '1'='1' -- \", \"x\"))\n"
            "print(secure_search(conn, \"phone\"))\n"
            "print(secure_search(conn, \"' OR '1'='1\"))\n\n"
            "النتيجة: True، وبعدين False، وبعدين [(1, 'phone')]، وبعدين [] — الدخول الصح شغال، والهجوم فاشل، والبحث شغال ✅\n\n"
            "لاحظ الطبقات التلاتة مع بعض: استعلام مُعامَل + تحقق من الطول + رسالة خطأ عامة لو حصل استثناء (الدرس 14).\n\n"
            "واجب النهاردة: انسخ الدالتين دول في ملف عندك، وشغّل الـ 4 سطور اللي فوق — لازم النتيجة تبقى True و False و [(1, 'phone')] و [] بالترتيب ده."
        ),
        "en": (
            "🏗️ Lesson 19: Secure login + search\n\n"
            "Now we put everything we learned together in one complete and secure code — login and search from the first line:\n\n"
            "def secure_login(conn, username, password):\n"
            "    cur = conn.cursor()\n"
            "    cur.execute(\"SELECT * FROM users WHERE username=? AND password=?\", (username, password))\n"
            "    return cur.fetchone() is not None\n"
            "def secure_search(conn, keyword):\n"
            "    if len(keyword) > 50:\n"
            "        return []\n"
            "    cur = conn.cursor()\n"
            "    cur.execute(\"SELECT * FROM products WHERE name LIKE ?\", (\"%\" + keyword + \"%\",))\n"
            "    return cur.fetchall()\n\n"
            "Try it on the test database (users has ahmed/1234, and products has phone and laptop):\n"
            "print(secure_login(conn, \"ahmed\", \"1234\"))\n"
            "print(secure_login(conn, \"' OR '1'='1' -- \", \"x\"))\n"
            "print(secure_search(conn, \"phone\"))\n"
            "print(secure_search(conn, \"' OR '1'='1\"))\n\n"
            "Result: True, then False, then [(1, 'phone')], then [] — the correct login works, the attack fails, and the search works ✅\n\n"
            "Notice the three layers together: parameterized query + length check + a generic error message if something goes wrong (Lesson 14).\n\n"
            "Today's task: copy these two functions into a file, and run the 4 lines above — the result must be True and False and [(1, 'phone')] and [] in this order."
        ),
    },
    {
        "title_ar": "الدرس 20: تسجيل ومراقبة محاولات الهجوم",
        "title_en": "Lesson 20: Logging attacks",
        "ar": (
            "📝 الدرس 20: تسجيل ومراقبة محاولات الهجوم\n\n"
            "الحماية مش بس منع الهجوم — لازم تعرف إنه حصل أصلًا! السجل (Log) هو دفتر أحوال موقعك: كل محاولة دخول فاشلة، وكل مدخلات مشبوهة، بتتسجل فيه بالتاريخ والوقت.\n\n"
            "جرّب الكود ده على جهازك:\n"
            "import datetime\n"
            "SUSPICIOUS = [\"'\", '\"', \" OR \", \"UNION\", \"--\", \";\"]\n"
            "def is_suspicious(text):\n"
            "    t = text.upper()\n"
            "    return any(p in t for p in SUSPICIOUS)\n"
            "def log_attempt(username, ok):\n"
            "    flag = \"SUSPICIOUS\" if is_suspicious(username) else \"normal\"\n"
            "    line = f\"{datetime.datetime.now()} | user={username} | ok={ok} | {flag}\\n\"\n"
            "    with open(\"/tmp/security.log\", \"a\", encoding=\"utf-8\") as f:\n"
            "        f.write(line)\n"
            "    return flag\n"
            "print(log_attempt(\"ahmed\", True))\n"
            "print(log_attempt(\"' OR '1'='1\", False))\n"
            "print(log_attempt(\"admin' --\", False))\n\n"
            "النتيجة: normal، وبعدين SUSPICIOUS، وبعدين SUSPICIOUS — والمحاولات المشبوهة اتسجلت في ملف security.log ✅\n\n"
            "بعد التسجيل بتعمل إيه؟\n"
            "• راجع السجل كل أسبوع — لو لقيت محاولات كتير من نفس المكان، يبقى حد بيجرّب عليك\n"
            "• قاعدة بسيطة: 5 محاولات فاشلة ورا بعض من نفس الـ IP = حظر مؤقت 15 دقيقة\n"
            "• ومتسجلش كلمات السر أبدًا في السجل — حتى الفاشلة منها\n\n"
            "واجب النهاردة: شغّل الكود ده، وافتح ملف security.log وشوف الـ 3 سطور — وبعدين اكتب قاعدة حظر بسيطة بكلامك: بعد كام محاولة فاشلة تحظر، ولمدة قد إيه؟"
        ),
        "en": (
            "📝 Lesson 20: Logging attacks\n\n"
            "Protection is not only blocking attacks — you must know they happened at all! The log is your site's diary: every failed login and every suspicious input is written in it with the date and time.\n\n"
            "Try this code on your machine:\n"
            "import datetime\n"
            "SUSPICIOUS = [\"'\", '\"', \" OR \", \"UNION\", \"--\", \";\"]\n"
            "def is_suspicious(text):\n"
            "    t = text.upper()\n"
            "    return any(p in t for p in SUSPICIOUS)\n"
            "def log_attempt(username, ok):\n"
            "    flag = \"SUSPICIOUS\" if is_suspicious(username) else \"normal\"\n"
            "    line = f\"{datetime.datetime.now()} | user={username} | ok={ok} | {flag}\\n\"\n"
            "    with open(\"/tmp/security.log\", \"a\", encoding=\"utf-8\") as f:\n"
            "        f.write(line)\n"
            "    return flag\n"
            "print(log_attempt(\"ahmed\", True))\n"
            "print(log_attempt(\"' OR '1'='1\", False))\n"
            "print(log_attempt(\"admin' --\", False))\n\n"
            "Result: normal, then SUSPICIOUS, then SUSPICIOUS — and the suspicious attempts were saved in the security.log file ✅\n\n"
            "What do you do after logging?\n"
            "• Check the log every week — if you see many attempts from the same place, someone is trying you\n"
            "• A simple rule: 5 failed attempts in a row from the same IP = a 15-minute temporary block\n"
            "• And never log passwords in the log — not even the failed ones\n\n"
            "Today's task: run this code, open the security.log file and see the 3 lines — then write a simple block rule in your own words: after how many failed attempts do you block, and for how long?"
        ),
    },
    {
        "title_ar": "الدرس 21: المشروع الختامي",
        "title_en": "Lesson 21: Final project",
        "ar": (
            "🎓 الدرس 21: المشروع الختامي — راجع وصلّح تطبيق صغير ضعيف\n\n"
            "وصلنا للآخر — دلوقتي هتراجع تطبيق صغير ضعيف وتصلحه من الأول للآخر، زي ما بيعمل المحترفين.\n\n"
            "التطبيق الضعيف (على معملك الخاص): دخول + بحث باللزق:\n"
            "def weak_login(conn, name, pw):\n"
            "    cur = conn.cursor()\n"
            "    q = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "    cur.execute(q)\n"
            "    return cur.fetchall()\n"
            "def weak_search(conn, kw):\n"
            "    cur = conn.cursor()\n"
            "    q = f\"SELECT * FROM products WHERE name LIKE '%{kw}%'\"\n"
            "    cur.execute(q)\n"
            "    return cur.fetchall()\n\n"
            "المراجعة — 3 ثغرات لقيناها:\n"
            "1️⃣ الدخول باللزق: هجوم ' OR '1'='1' -- بيدخل من غير كلمة سر\n"
            "2️⃣ البحث باللزق: نفس الهجوم بيرجع كل المنتجات\n"
            "3️⃣ مفيش تسجيل ولا رسايل خطأ عامة — يعني لو حد هاجمك مش هتعرف\n\n"
            "الإصلاح: استبدل الدالتين بالدالتين الآمنين من الدرس 19 (secure_login و secure_search) — استعلامات مُعامَلة + تحقق من الطول — وزوّد التسجيل من الدرس 20.\n\n"
            "والتأكيد بعد الإصلاح — لازم النتيجة تبقى كده:\n"
            "الدخول الصح: True — والهجوم: False — والبحث الصح: [(1, 'phone')] — وهجوم البحث: []\n\n"
            "🎉 مبروك! خلصت دورة حماية من SQL Injection — دلوقتي تعرف: إيه هو الحقن، وإزاي بيحصل، وإزاي تسدّه، وإزاي تختبر موقعك وتراقبه.\n\n"
            "واجب النهاردة: خد أي مشروع صغير عندك (أو معمل lab_login.py) واعمل نفس المراجعة: دوّر على أي استعلام باللزق، وصلّحه بالطريقة المُعامَلة، وجرّب الهجوم القديم — لازم يفشل."
        ),
        "en": (
            "🎓 Lesson 21: Final project — review and fix a weak app\n\n"
            "We made it to the end — now you will review a small weak app and fix it from start to finish, like professionals do.\n\n"
            "The weak app (in your own lab): login + search with gluing:\n"
            "def weak_login(conn, name, pw):\n"
            "    cur = conn.cursor()\n"
            "    q = f\"SELECT * FROM users WHERE username='{name}' AND password='{pw}'\"\n"
            "    cur.execute(q)\n"
            "    return cur.fetchall()\n"
            "def weak_search(conn, kw):\n"
            "    cur = conn.cursor()\n"
            "    q = f\"SELECT * FROM products WHERE name LIKE '%{kw}%'\"\n"
            "    cur.execute(q)\n"
            "    return cur.fetchall()\n\n"
            "The review — 3 holes we found:\n"
            "1️⃣ Login with gluing: the ' OR '1'='1' -- attack gets in without a password\n"
            "2️⃣ Search with gluing: the same attack returns all products\n"
            "3️⃣ No logging and no generic error messages — so if someone attacks you, you will not know\n\n"
            "The fix: replace both functions with the secure ones from Lesson 19 (secure_login and secure_search) — parameterized queries + length check — and add the logging from Lesson 20.\n\n"
            "And the check after fixing — the result must be:\n"
            "Correct login: True — the attack: False — correct search: [(1, 'phone')] — search attack: []\n\n"
            "🎉 Congratulations! You finished the SQL Injection Protection course — now you know: what injection is, how it happens, how to close it, and how to test your site and watch it.\n\n"
            "Today's task: take any small project of yours (or the lab_login.py lab) and do the same review: look for any glued query, fix it the parameterized way, and try the old attack — it must fail."
        ),
    },
]

AI_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه ذكاء اصطناعي؟",
        "title_en": "Lesson 1: What is AI?",
        "ar": (
            "🤖 الدرس 1: يعني إيه ذكاء اصطناعي؟\n"
            "📗 المستوى الأول: الأساسيات — هنفهم الذكاء الاصطناعي قبل ما نستخدمه.\n\n"
            "الذكاء الاصطناعي (AI) يعني برنامج كمبيوتر اتعلم من بيانات كتير، فبقى يعرف يجاوب على أسئلة، يكتب نصوص، يعمل صور، ويلخّص حاجات — زي الإنسان اللي اتعلم من الخبرة.\n\n"
            "انت بتستخدمه كل يوم من غير ما تاخد بالك:\n"
            "• جوجل بيكمّل بحثك وبيصحح كلامك\n"
            "• يوتيوب وفيسبوك بيرشحوا لك فيديوهات على ذوقك\n"
            "• المساعد الصوتي في موبايلك بيفهم كلامك\n"
            "• خرائط جوجل بتتوقع الزحمة\n\n"
            "الذكاء الاصطناعي مش سحر ولا روبوت بيفكر زي الإنسان — هو برنامج بيتعلم الأنماط من البيانات. عشان كده ممكن يغلط، وهنعرف في الدروس الجاية إزاي نستخدمه صح.\n\n"
            "واجب النهاردة: افتح ChatGPT أو Gemini واسأله سؤال واحد بس: \"اشرح لي الذكاء الاصطناعي في 3 سطور\" — وشوف إجابته."
        ),
        "en": (
            "🤖 Lesson 1: What is AI?\n"
            "📗 Level 1: Basics — first we understand AI, then we use it.\n\n"
            "Artificial Intelligence (AI) is a computer program that learned from lots of data, so it can answer questions, write texts, create images and summarize things — like a person who learned from experience.\n\n"
            "You already use it every day without noticing:\n"
            "• Google completes your search and corrects your words\n"
            "• YouTube and Facebook suggest videos you like\n"
            "• The voice assistant on your phone understands you\n"
            "• Google Maps predicts traffic\n\n"
            "AI is not magic and not a robot that thinks like a human — it is a program that learns patterns from data. That is why it can make mistakes, and in the next lessons we will learn how to use it well.\n\n"
            "Today's task: open ChatGPT or Gemini and ask one question: \"Explain AI to me in 3 lines\" — and read the answer."
        ),
    },
    {
        "title_ar": "الدرس 2: ChatGPT وGemini إزاي تشغلهم",
        "title_en": "Lesson 2: ChatGPT & Gemini",
        "ar": (
            "💬 الدرس 2: ChatGPT وGemini إزاي تشغلهم\n\n"
            "أشهر أداتين ذكاء اصطناعي مجانيتين، وطريقة تشغيلهم سهلة:\n\n"
            "ChatGPT:\n"
            "1️⃣ افتح chatgpt.com من المتصفح أو نزّل التطبيق\n"
            "2️⃣ اعمل حساب بالإيميل (أو بحساب جوجل)\n"
            "3️⃣ اكتب سؤالك في الخانة اللي تحت ودوس إرسال\n\n"
            "Gemini (بتاع جوجل):\n"
            "1️⃣ افتح gemini.google.com\n"
            "2️⃣ سجّل دخول بحساب جوجل بتاعك — من غير حساب جديد\n"
            "3️⃣ اكتب سؤالك على طول\n\n"
            "النسخة المجانية في الاتنين كفاية للتعلم والشغل اليومي. النسخة المدفوعة أسرع وأقوى، بس مش محتاجها دلوقتي.\n\n"
            "💡 جرّب تسأل نفس السؤال في الاتنين وقارن الإجابتين — هتلاقي كل واحد ليه أسلوب مختلف.\n\n"
            "واجب النهاردة: اعمل حساب على ChatGPT أو Gemini، واسأله: \"اعمل لي خطة مذاكرة لمدة أسبوع\" — واحفظ الرد."
        ),
        "en": (
            "💬 Lesson 2: ChatGPT & Gemini\n\n"
            "The two most famous free AI tools, and starting them is easy:\n\n"
            "ChatGPT:\n"
            "1️⃣ Open chatgpt.com in your browser or download the app\n"
            "2️⃣ Create an account with your email (or Google account)\n"
            "3️⃣ Type your question in the box and send\n\n"
            "Gemini (by Google):\n"
            "1️⃣ Open gemini.google.com\n"
            "2️⃣ Sign in with your Google account — no new account needed\n"
            "3️⃣ Ask your question right away\n\n"
            "The free version of both is enough for learning and daily work. The paid version is faster and stronger, but you do not need it now.\n\n"
            "💡 Try asking the same question in both and compare the answers — each has a different style.\n\n"
            "Today's task: create an account on ChatGPT or Gemini and ask: \"Make me a one-week study plan\" — and save the answer."
        ),
    },
    {
        "title_ar": "الدرس 3: كتابة الأوامر الصح (prompt)",
        "title_en": "Lesson 3: Good prompts",
        "ar": (
            "✍️ الدرس 3: كتابة الأوامر الصح (prompt)\n\n"
            "الأمر (prompt) هو الكلام اللي بتكتبه للذكاء الاصطناعي. كل ما كان أوضح، كل ما كانت الإجابة أحسن.\n\n"
            "❌ أمر ضعيف: \"اكتب عن التسويق\"\n"
            "✅ أمر قوي: \"انت خبير تسويق. اكتب بوست فيسبوك قصير عن متجر ملابس، موجّه لشباب من 18 لـ 25 سنة، باللهجة المصرية، وفي آخره سؤال يخلي الناس تعلّق.\"\n\n"
            "الأمر القوي فيه 4 حاجات:\n"
            "1️⃣ الدور: \"انت خبير...\" — بيخليه يجاوب كمتخصص\n"
            "2️⃣ المهمة بوضوح: اكتب إيه بالظبط\n"
            "3️⃣ الجمهور والأسلوب: لمين وبأي لغة\n"
            "4️⃣ الشكل المطلوب: قصير، نقاط، جدول، سؤال في الآخر\n\n"
            "💡 لو الإجابة مش عاجباك، قوله: \"اختصرها\" أو \"خليها أبسط\" أو \"اديني مثال تاني\" — هو بيتحسن كل ما توضح له.\n\n"
            "واجب النهاردة: اكتب أمر قوي بالأربع حاجات دول، واطلب منه بوست عن أي موضوع تحبه — وقارن النتيجة بالأمر الضعيف."
        ),
        "en": (
            "✍️ Lesson 3: Good prompts\n\n"
            "A prompt is what you write to the AI. The clearer it is, the better the answer.\n\n"
            "❌ Weak prompt: \"Write about marketing\"\n"
            "✅ Strong prompt: \"You are a marketing expert. Write a short Facebook post for a clothes shop, for young people aged 18 to 25, in Egyptian dialect, ending with a question that makes people comment.\"\n\n"
            "A strong prompt has 4 parts:\n"
            "1️⃣ Role: \"You are an expert...\" — makes it answer like a specialist\n"
            "2️⃣ Clear task: exactly what to write\n"
            "3️⃣ Audience and style: for whom, in which language\n"
            "4️⃣ Format: short, bullet points, table, a question at the end\n\n"
            "💡 If you do not like the answer, say: \"make it shorter\" or \"make it simpler\" or \"give me another example\" — it improves as you clarify.\n\n"
            "Today's task: write a strong prompt with all four parts and ask for a post about any topic you like — then compare it with the weak prompt."
        ),
    },
    {
        "title_ar": "الدرس 4: الذكاء الاصطناعي ممكن يغلط — إزاي تتأكد",
        "title_en": "Lesson 4: AI can be wrong",
        "ar": (
            "⚠️ الدرس 4: الذكاء الاصطناعي ممكن يغلط — إزاي تتأكد\n\n"
            "الذكاء الاصطناعي ساعات بيجاوب بثقة وهو غلطان — بيألف أرقام أو أسماء أو تواريخ مش حقيقية. ده اسمه \"هلوسة\" (hallucination).\n\n"
            "إزاي تتأكد؟\n"
            "1️⃣ أي معلومة مهمة (رقم، تاريخ، حكم ديني أو قانوني) راجعها من مصدر موثوق — جوجل أو كتاب أو موقع رسمي\n"
            "2️⃣ قوله: \"اديني مصدر المعلومة دي\" — وافتح المصدر بنفسك\n"
            "3️⃣ اسأل نفس السؤال بصيغة تانية، وشوف الإجابة هتتغير ولا ثابتة\n"
            "4️⃣ لو الموضوع يخص صحتك أو فلوسك أو قرار مهم — اسأل إنسان متخصص، مش الذكاء الاصطناعي بس\n\n"
            "القاعدة الذهبية: الذكاء الاصطناعي مساعد سريع، مش مرجع نهائي. استخدمه عشان تفهم وتبدأ، وتأكد بنفسك قبل ما تنشر أو تقرر.\n\n"
            "واجب النهاردة: اسأله عن حقيقة تاريخية تعرفها كويس (مثال: سنة بناء الأهرامات)، وشوف إجابته صح ولا فيها غلط."
        ),
        "en": (
            "⚠️ Lesson 4: AI can be wrong\n\n"
            "AI sometimes answers confidently while being wrong — it invents numbers, names or dates that are not real. This is called \"hallucination\".\n\n"
            "How to check:\n"
            "1️⃣ Any important fact (number, date, religious or legal ruling) — verify it from a trusted source: Google, a book, or an official site\n"
            "2️⃣ Ask it: \"give me the source of this information\" — and open the source yourself\n"
            "3️⃣ Ask the same question in a different way and see if the answer changes\n"
            "4️⃣ If it concerns your health, money or an important decision — ask a human specialist, not AI alone\n\n"
            "The golden rule: AI is a fast helper, not a final reference. Use it to understand and start, and verify yourself before you publish or decide.\n\n"
            "Today's task: ask it about a historical fact you know well (for example: when were the pyramids built) and check if its answer is right or wrong."
        ),
    },
    {
        "title_ar": "الدرس 5: الخصوصية — متبعتش بيانات حساسة",
        "title_en": "Lesson 5: Privacy",
        "ar": (
            "🔒 الدرس 5: الخصوصية — متبعتش بيانات حساسة\n\n"
            "أي حاجة بتكتبها للذكاء الاصطناعي ممكن تتخزن وتستخدم في تحسين الخدمة. ففيه حاجات ممنوع تبعتها أبدًا:\n\n"
            "❌ ممنوع تمامًا:\n"
            "• كلمات سر أو أرقام بطاقات بنكية\n"
            "• الرقم القومي أو رقم جواز السفر\n"
            "• صور بطاقتك أو وشك أو صور عيلتك الخاصة\n"
            "• أسرار شغلك أو بيانات عملاء\n"
            "• رسايل خاصة بينك وبين حد\n\n"
            "✅ آمن تبعته:\n"
            "• أسئلة عامة ومعلومات تعليمية\n"
            "• نصوص انت كاتبها وعايز تحسينها\n"
            "• أفكار مشاريع من غير بيانات شخصية\n\n"
            "💡 نصيحة: قبل ما تلصق أي نص، اقرأه مرة واحدة واسأل نفسك: \"لو النص ده اتنشر، هيضرني؟\" — لو الإجابة أيوه، متبعتوش.\n\n"
            "واجب النهاردة: راجع آخر 5 حاجات بعتها للذكاء الاصطناعي — فيه حاجة منهم كان فيها بيانات شخصية؟ لو فيه، متعملش كده تاني."
        ),
        "en": (
            "🔒 Lesson 5: Privacy\n\n"
            "Anything you write to an AI can be stored and used to improve the service. So there are things you must never send:\n\n"
            "❌ Never send:\n"
            "• Passwords or bank card numbers\n"
            "• Your national ID or passport number\n"
            "• Photos of your ID card, your face, or your family's private photos\n"
            "• Your work secrets or client data\n"
            "• Private messages between you and someone\n\n"
            "✅ Safe to send:\n"
            "• General questions and learning information\n"
            "• Texts you wrote and want to improve\n"
            "• Project ideas without personal data\n\n"
            "💡 Tip: before you paste any text, read it once and ask yourself: \"If this text was published, would it harm me?\" — if yes, do not send it.\n\n"
            "Today's task: review the last 5 things you sent to an AI — did any of them contain personal data? If so, do not do it again."
        ),
    },
    {
        "title_ar": "الدرس 6: عمل صور بالذكاء الاصطناعي",
        "title_en": "Lesson 6: AI images",
        "ar": (
            "🖼️ الدرس 6: عمل صور بالذكاء الاصطناعي\n\n"
            "تقدر تعمل صورة من مجرد وصف بالكلام — في ChatGPT أو Gemini أو أي مولّد صور.\n\n"
            "وصف ضعيف: \"اعمل صورة قطة\"\n"
            "وصف قوي: \"قطة برتقالية صغيرة قاعدة على شباك قديم في قرية مصرية، نور الشمس داخل عليها، ستايل رسم كرتوني دافئ\"\n\n"
            "الوصف القوي فيه:\n"
            "1️⃣ الموضوع: إيه اللي في الصورة\n"
            "2️⃣ المكان والجو: فين وإضاءة عاملة إزاي\n"
            "3️⃣ الستايل: كرتوني، واقعي، رسم زيتي\n"
            "4️⃣ الألوان والمزاج: دافئ، هادي، مبهج\n\n"
            "💡 لو الصورة مش زي ما انت عايز، قوله: \"غيّر الخلفية\" أو \"خلي القطة أكبر\" — وعدّل لحد ما تعجبك.\n\n"
            "⚠️ مهم: متستخدمش صورة مولّدة على إنها صورة حقيقية، ومتعملش صور لناس حقيقيين من غير إذنهم.\n\n"
            "واجب النهاردة: اعمل صورة بوصف قوي من 3 سطور، واحفظها — هتحتاجها في درس صناعة المحتوى."
        ),
        "en": (
            "🖼️ Lesson 6: AI images\n\n"
            "You can create an image from just a written description — in ChatGPT, Gemini or any image generator.\n\n"
            "Weak description: \"Make a picture of a cat\"\n"
            "Strong description: \"A small orange cat sitting on an old window in an Egyptian village, sunlight coming in, warm cartoon drawing style\"\n\n"
            "A strong description has:\n"
            "1️⃣ Subject: what is in the picture\n"
            "2️⃣ Place and mood: where, and how the light looks\n"
            "3️⃣ Style: cartoon, realistic, oil painting\n"
            "4️⃣ Colors and feeling: warm, calm, cheerful\n\n"
            "💡 If the picture is not what you want, say: \"change the background\" or \"make the cat bigger\" — and keep adjusting until you like it.\n\n"
            "⚠️ Important: do not present a generated image as a real photo, and do not create images of real people without their permission.\n\n"
            "Today's task: create an image with a strong 3-line description and save it — you will need it in the content creation lesson."
        ),
    },
    {
        "title_ar": "الدرس 7: عمل فيديو وبوستات",
        "title_en": "Lesson 7: AI videos & posts",
        "ar": (
            "🎬 الدرس 7: عمل فيديو وبوستات\n\n"
            "الذكاء الاصطناعي يساعدك تعمل بوست أو فيديو قصير بسرعة، بس انت اللي بتظبطه في الآخر.\n\n"
            "لبوست سوشيال ميديا:\n"
            "1️⃣ اطلب منه 3 أفكار لبوست عن موضوعك\n"
            "2️⃣ اختار أحسن فكرة، وقوله يكتبها بأسلوبك\n"
            "3️⃣ عدّل الكلام بنفسك — حط لمستك وكلامك انت\n"
            "4️⃣ ضيف صورة مولّدة بالذكاء الاصطناعي (درس 6) أو صورة حقيقية\n\n"
            "لفيديو قصير:\n"
            "1️⃣ اطلب منه سكربت فيديو 30 ثانية: جملة جذابة في الأول، 3 نقاط في النص، ونداء في الآخر\n"
            "2️⃣ اقرأ السكربت بصوتك وسجّله\n"
            "3️⃣ استخدم تطبيق مونتاج بسيط زي CapCut عشان تقطّع وتركّب\n\n"
            "القاعدة: الذكاء الاصطناعي يبدأ لك الشغل، وانت تخلّصه. المحتوى اللي فيه لمستك انت هو اللي الناس بتحبه.\n\n"
            "واجب النهاردة: اعمل بوست واحد كامل بالطريقة دي (فكرة + نص + صورة) — وانشره أو احفظه عندك."
        ),
        "en": (
            "🎬 Lesson 7: AI videos & posts\n\n"
            "AI helps you make a post or a short video quickly, but you finish it yourself.\n\n"
            "For a social media post:\n"
            "1️⃣ Ask it for 3 post ideas about your topic\n"
            "2️⃣ Pick the best idea and ask it to write it in your style\n"
            "3️⃣ Edit the words yourself — add your own touch\n"
            "4️⃣ Add an AI-generated image (lesson 6) or a real photo\n\n"
            "For a short video:\n"
            "1️⃣ Ask for a 30-second video script: a hook at the start, 3 points in the middle, a call to action at the end\n"
            "2️⃣ Read the script in your voice and record it\n"
            "3️⃣ Use a simple editing app like CapCut to cut and assemble\n\n"
            "The rule: AI starts the work, you finish it. Content with your own touch is what people love.\n\n"
            "Today's task: make one complete post this way (idea + text + image) — publish it or save it."
        ),
    },
]

AI_LESSONS += [
    {
        "title_ar": "الدرس 8: أتمتة شغلك بالذكاء الاصطناعي",
        "title_en": "Lesson 8: Automate your work",
        "ar": (
            "⚙️ الدرس 8: أتمتة شغلك بالذكاء الاصطناعي\n"
            "📘 المستوى التاني: الاستخدام المتقدم — هنخلي الذكاء الاصطناعي يشتغل مكانك في المهام المملة.\n\n"
            "الأتمتة يعني تخلي الذكاء الاصطناعي يعمل المهام اللي بتكررها كل يوم:\n\n"
            "• تلخيص إيميلات ورسايل طويلة في 3 سطور\n"
            "• تحويل كلام مسجّل صوتيًا لنص مكتوب\n"
            "• ترتيب أفكارك في جدول أو قايمة مهام\n"
            "• كتابة ردود جاهزة على أسئلة بتتكرر\n"
            "• مقارنة أسعار أو عروض من نصوص طويلة\n\n"
            "ابدأ بمهمة واحدة بس: اختار أكتر حاجة بتضيع وقتك كل يوم، واطلب من الذكاء الاصطناعي يعملها لك مرة واحدة — لو النتيجة عجبتك، كررها كل يوم بنفس الأمر.\n\n"
            "💡 احفظ الأوامر اللي بتنجح معاك في ملف عندك — دي بقت \"أدواتك\" الخاصة.\n\n"
            "واجب النهاردة: اختار مهمة مملة بتعملها كل يوم، وخلّي الذكاء الاصطناعي يعملها لك النهاردة."
        ),
        "en": (
            "⚙️ Lesson 8: Automate your work\n"
            "📘 Level 2: Advanced use — we make AI do the boring tasks for you.\n\n"
            "Automation means letting AI do the tasks you repeat every day:\n\n"
            "• Summarize long emails and messages in 3 lines\n"
            "• Turn voice recordings into written text\n"
            "• Organize your ideas into a table or task list\n"
            "• Write ready replies for repeated questions\n"
            "• Compare prices or offers from long texts\n\n"
            "Start with one task only: pick the thing that wastes your time every day, and ask the AI to do it once — if you like the result, repeat it daily with the same prompt.\n\n"
            "💡 Save the prompts that work for you in a file — these become your own tools.\n\n"
            "Today's task: pick one boring task you do every day and let the AI do it for you today."
        ),
    },
    {
        "title_ar": "الدرس 9: مساعد ذكي لمشروعك",
        "title_en": "Lesson 9: AI assistant for your project",
        "ar": (
            "🤝 الدرس 9: مساعد ذكي لمشروعك\n\n"
            "لو عندك صفحة أو محل أو مشروع صغير، الذكاء الاصطناعي ممكن يبقى مساعدك اللي بيرد على الناس.\n\n"
            "إزاي تعمله؟\n"
            "1️⃣ اكتب قايمة بأكتر 10 أسئلة عملاءك بيسألوها (السعر؟ التوصيل؟ المواعيد؟)\n"
            "2️⃣ اطلب من الذكاء الاصطناعي يكتب إجابة جاهزة لكل سؤال — بأسلوبك ولهجتك\n"
            "3️⃣ احفظ الإجابات في ملف، واستخدمها لما حد يسألك\n"
            "4️⃣ كل ما ييجي سؤال جديد، ضيفه للقايمة\n\n"
            "مثال: عميل يسأل \"التوصيل بكام؟\" — الإجابة الجاهزة: \"التوصيل 30 جنيه داخل القاهرة، ومجاني للطلبات فوق 500 جنيه 🙂\"\n\n"
            "⚠️ الردود الجاهزة تساعدك، بس لو العميل عنده مشكلة حقيقية أو شكوى — رد انت بنفسك.\n\n"
            "واجب النهاردة: اكتب 5 أسئلة بيسألها عملاءك أو متابعينك، وخلّي الذكاء الاصطناعي يكتب إجابة لكل واحد."
        ),
        "en": (
            "🤝 Lesson 9: AI assistant for your project\n\n"
            "If you have a page, a shop or a small project, AI can be your helper that answers people.\n\n"
            "How to build it:\n"
            "1️⃣ Write a list of the 10 questions your customers ask most (price? delivery? opening hours?)\n"
            "2️⃣ Ask the AI to write a ready answer for each question — in your style and dialect\n"
            "3️⃣ Save the answers in a file and use them when someone asks\n"
            "4️⃣ Every time a new question comes, add it to the list\n\n"
            "Example: a customer asks \"How much is delivery?\" — ready answer: \"Delivery is 30 EGP inside Cairo, and free for orders over 500 EGP 🙂\"\n\n"
            "⚠️ Ready answers help you, but if a customer has a real problem or complaint — answer yourself.\n\n"
            "Today's task: write 5 questions your customers or followers ask, and let the AI write an answer for each one."
        ),
    },
    {
        "title_ar": "الدرس 10: الذكاء الاصطناعي في الشغل والدراسة",
        "title_en": "Lesson 10: AI at work & study",
        "ar": (
            "📚 الدرس 10: الذكاء الاصطناعي في الشغل والدراسة\n\n"
            "الذكاء الاصطناعي مش للّعب بس — هو أداة مذاكرة وشغل قوية:\n\n"
            "في الدراسة:\n"
            "• \"اشرح لي الدرس ده كأني عندي 10 سنين\" — بيبسّط أي موضوع صعب\n"
            "• \"اعمل لي 10 أسئلة اختبار على الدرس ده\" — ويصحح إجاباتك\n"
            "• \"لخّص لي المقال ده في 5 نقاط\"\n\n"
            "في الشغل:\n"
            "• كتابة إيميل رسمي من نقاط بسيطة\n"
            "• تلخيص اجتماع أو تقرير طويل\n"
            "• ترجمة نص ومراجعة الترجمة\n"
            "• عمل جدول مقارنة بين خيارات\n\n"
            "⚠️ في الدراسة: استخدمه عشان تفهم، مش عشان يغش لك. لو كتبت واجبك كله بالذكاء الاصطناعي من غير ما تفهم، هتتعب في الامتحان.\n\n"
            "واجب النهاردة: اختار موضوع صعب عليك، واطلب منه يشرحه لك ببساطة — وبعدين اشرحه انت لحد تاني بكلامك."
        ),
        "en": (
            "📚 Lesson 10: AI at work & study\n\n"
            "AI is not only for fun — it is a strong study and work tool:\n\n"
            "For studying:\n"
            "• \"Explain this lesson to me like I am 10 years old\" — it simplifies any hard topic\n"
            "• \"Make 10 quiz questions about this lesson\" — and it corrects your answers\n"
            "• \"Summarize this article in 5 points\"\n\n"
            "For work:\n"
            "• Writing a formal email from simple points\n"
            "• Summarizing a long meeting or report\n"
            "• Translating a text and checking the translation\n"
            "• Making a comparison table between options\n\n"
            "⚠️ For studying: use it to understand, not to cheat. If AI writes all your homework without you understanding, you will struggle in the exam.\n\n"
            "Today's task: pick a topic that is hard for you and ask it to explain it simply — then explain it to someone else in your own words."
        ),
    },
    {
        "title_ar": "الدرس 11: حدوده وأخطاؤه",
        "title_en": "Lesson 11: Limits & mistakes",
        "ar": (
            "🚧 الدرس 11: حدوده وأخطاؤه\n\n"
            "الذكاء الاصطناعي قوي، بس ليه حدود لازم تعرفها:\n\n"
            "❌ اللي مبيعرفش يعمله:\n"
            "• أخبار اللحظة: معلوماته ممكن تكون قديمة، فاسأل جوجل عن الأخبار العاجلة\n"
            "• الحسابات المعقدة: ساعات بيغلط في الرياضيات — راجع بالألة الحاسبة\n"
            "• يفهم مشاعرك بجد: هو بيقلّد الفهم، مش بيشعر\n"
            "• ياخد قرار مكانك: القرارات المهمة (صحية، مالية، قانونية) ليها متخصصين\n"
            "• يعرف حاجات عنك: مش بيعرف مين انت إلا اللي انت قلته له في المحادثة\n\n"
            "💡 الخلاصة: الذكاء الاصطناعي زي آلة حاسبة ذكية — بيسرّع شغلك، بس انت العقل اللي بيراجع ويقرر.\n\n"
            "واجب النهاردة: جرّب تسأله مسألة حسابية صعبة شوية (مثال: 17 × 23 + 148) وشوف هيجاوب صح ولا غلط — وتأكد بالألة الحاسبة."
        ),
        "en": (
            "🚧 Lesson 11: Limits & mistakes\n\n"
            "AI is strong, but it has limits you must know:\n\n"
            "❌ What it cannot do:\n"
            "• Breaking news: its information may be old — ask Google for urgent news\n"
            "• Hard math: it sometimes makes mistakes in calculations — check with a calculator\n"
            "• Truly understand your feelings: it imitates understanding, it does not feel\n"
            "• Decide for you: important decisions (health, money, legal) belong to specialists\n"
            "• Know things about you: it only knows what you told it in the chat\n\n"
            "💡 The summary: AI is like a smart calculator — it speeds up your work, but you are the mind that checks and decides.\n\n"
            "Today's task: try asking it a slightly hard math question (example: 17 × 23 + 148) and see if it answers right or wrong — and check with a calculator."
        ),
    },
    {
        "title_ar": "الدرس 12: صناعة محتوى بالذكاء الاصطناعي",
        "title_en": "Lesson 12: AI content creation",
        "ar": (
            "🎥 الدرس 12: صناعة محتوى بالذكاء الاصطناعي\n\n"
            "خطوات عمل محتوى كامل بالذكاء الاصطناعي — من الفكرة للنشر:\n\n"
            "1️⃣ الفكرة: \"اديني 5 أفكار فيديو عن حماية الواي فاي للمبتدئين\"\n"
            "2️⃣ السكربت: \"اكتب سكربت 60 ثانية عن الفكرة رقم 2 — جملة جذابة في الأول و3 نقاط\"\n"
            "3️⃣ الصورة: اعمل صورة مصغّرة (thumbnail) بوصف قوي\n"
            "4️⃣ الصوت: سجّل السكربت بصوتك انت — صوتك أحسن من أي صوت آلي\n"
            "5️⃣ المونتاج: ركّب الصوت والصورة في CapCut\n"
            "6️⃣ المراجعة: اسمع الفيديو مرة أخيرة — في معلومة غلط؟ الكلام واضح؟\n"
            "7️⃣ النشر: عنوان جذاب + وصف + هاشتاجات\n\n"
            "⚠️ القاعدة: الذكاء الاصطناعي يساعدك تنتج أكتر، بس المحتوى لازم يعدّي على عينك وعقلك قبل النشر — انت المسؤول عن كل كلمة بتطلع باسمك.\n\n"
            "واجب النهاردة: اعمل فيديو قصير واحد بالخطوات دي — حتى لو 30 ثانية بس."
        ),
        "en": (
            "🎥 Lesson 12: AI content creation\n\n"
            "Steps to make full content with AI — from idea to publishing:\n\n"
            "1️⃣ Idea: \"Give me 5 video ideas about Wi-Fi protection for beginners\"\n"
            "2️⃣ Script: \"Write a 60-second script about idea 2 — a hook first and 3 points\"\n"
            "3️⃣ Image: make a thumbnail with a strong description\n"
            "4️⃣ Voice: record the script in your own voice — your voice is better than any robot voice\n"
            "5️⃣ Editing: assemble voice and image in CapCut\n"
            "6️⃣ Review: listen once more — any wrong information? Is the speech clear?\n"
            "7️⃣ Publish: catchy title + description + hashtags\n\n"
            "⚠️ The rule: AI helps you produce more, but the content must pass your eyes and mind before publishing — you are responsible for every word published under your name.\n\n"
            "Today's task: make one short video with these steps — even just 30 seconds."
        ),
    },
    {
        "title_ar": "الدرس 13: خطة استخدام يومية",
        "title_en": "Lesson 13: Daily AI routine",
        "ar": (
            "🗓️ الدرس 13: خطة استخدام يومية\n\n"
            "عشان الذكاء الاصطناعي يفيدك بجد، خليه عادة يومية — 30 دقيقة بس:\n\n"
            "☀️ الصبح (10 دقايق):\n"
            "• \"لخّص لي أهم أخبار التكنولوجيا النهاردة في 5 نقاط\"\n"
            "• راجع مهام اليوم واطلب منه يرتبها بالأهمية\n\n"
            "🌤️ الظهر (10 دقايق):\n"
            "• اتعلم حاجة جديدة: \"اشرح لي موضوع ___ ببساطة\"\n"
            "• اسأله 3 أسئلة عن الحاجة اللي بتتعلمها\n\n"
            "🌙 بالليل (10 دقايق):\n"
            "• \"ساعدني أجهز بوست أو رسالة لبكرة\"\n"
            "• راجع اللي اتعلمته النهاردة: \"اختبرني في ___\"\n\n"
            "💡 الاستمرارية أهم من الكمية: 30 دقيقة كل يوم أحسن من 5 ساعات يوم واحد في الأسبوع.\n\n"
            "واجب النهاردة: جرّب الخطة دي النهاردة كاملة — الصبح والظهر وبالليل — وقول لنفسك: إيه أكتر جزء فادك؟"
        ),
        "en": (
            "🗓️ Lesson 13: Daily AI routine\n\n"
            "To really benefit from AI, make it a daily habit — just 30 minutes:\n\n"
            "☀️ Morning (10 minutes):\n"
            "• \"Summarize today's most important tech news in 5 points\"\n"
            "• Review today's tasks and ask it to sort them by importance\n\n"
            "🌤️ Midday (10 minutes):\n"
            "• Learn something new: \"Explain ___ simply\"\n"
            "• Ask it 3 questions about what you are learning\n\n"
            "🌙 Evening (10 minutes):\n"
            "• \"Help me prepare a post or message for tomorrow\"\n"
            "• Review what you learned today: \"Quiz me on ___\"\n\n"
            "💡 Consistency matters more than quantity: 30 minutes every day beats 5 hours one day a week.\n\n"
            "Today's task: try this full plan today — morning, midday and evening — and ask yourself: which part helped you most?"
        ),
    },
    {
        "title_ar": "الدرس 14: المشروع الختامي — مساعدك الذكي",
        "title_en": "Lesson 14: Final project",
        "ar": (
            "🏆 الدرس 14: المشروع الختامي — مساعدك الذكي\n\n"
            "وصلنا لآخر درس في الدورة — دلوقتي هتبني مساعدك الذكي الخاص:\n\n"
            "المشروع: مساعد ذكي لمهمة حقيقية في حياتك — اختار واحدة:\n"
            "• مساعد ردود لصفحتك أو مشروعك\n"
            "• مساعد مذاكرة لمادة بتتعلمها\n"
            "• مساعد محتوى بينشر معاك كل يوم\n\n"
            "الخطوات:\n"
            "1️⃣ اكتب 5 أوامر (prompts) قوية للمهمة دي — بالطريقة اللي اتعلمناها في الدرس 3\n"
            "2️⃣ جرّب كل أمر 3 مرات، وعدّل اللي نتيجته ضعيفة\n"
            "3️⃣ احفظ الأوامر اللي نجحت في ملف واحد — ده بقى \"مساعدك\"\n"
            "4️⃣ استخدمه أسبوع كامل، وسجّل: إيه اللي وفر عليك وقت؟ وإيه اللي محتاج تحسين؟\n\n"
            "🎉 مبروك! انت دلوقتي بتعرف تستخدم الذكاء الاصطناعي بجد — مش بس تسأله، لكن تخليه يشتغل معاك كل يوم.\n\n"
            "واجب النهاردة: اعمل ملف الأوامر الخمسة بتوعك، وجرّب أول أمر فيهم النهاردة."
        ),
        "en": (
            "🏆 Lesson 14: Final project\n\n"
            "We reached the last lesson — now build your own AI helper:\n\n"
            "The project: an AI helper for a real task in your life — pick one:\n"
            "• A reply helper for your page or project\n"
            "• A study helper for a subject you are learning\n"
            "• A content helper that publishes with you every day\n\n"
            "Steps:\n"
            "1️⃣ Write 5 strong prompts for this task — the way we learned in lesson 3\n"
            "2️⃣ Try each prompt 3 times and fix the weak ones\n"
            "3️⃣ Save the prompts that worked in one file — that is your \"helper\"\n"
            "4️⃣ Use it for a full week and write down: what saved you time? What needs improvement?\n\n"
            "🎉 Congratulations! You now really know how to use AI — not just asking it, but making it work with you every day.\n\n"
            "Today's task: make your file with the five prompts and try the first one today."
        ),
    },
]

FREELANCE_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه عمل حر؟",
        "title_en": "Lesson 1: What is freelancing?",
        "ar": (
            "💰 الدرس 1: يعني إيه عمل حر؟\n\n"
            "العمل الحر (Freelancing) يعني تبيع مهارتك على الإنترنت لعملاء من أي مكان — من غير مدير ومن غير وظيفة ثابتة. العميل يطلب شغل، انت تعمله، وهو يدفع لك.\n\n"
            "أمثلة لخدمات مطلوبة:\n"
            "• تصميم بوستات وشعارات\n"
            "• كتابة مقالات وبوستات\n"
            "• برمجة مواقع وتطبيقات\n"
            "• ترجمة\n"
            "• إدارة صفحات سوشيال ميديا\n"
            "• تحليل بيانات\n\n"
            "⚠️ كلام صادق من الأول: العمل الحر مش فلوس سريعة. البداية بطيئة — أول عميل أصعب عميل، وأول فلوس قليلة. اللي بينجح هو اللي بيتعلم مهارة كويس، ويشتغل باستمرار، ويبني سمعة. مفيش \"اكسب 1000 دولار في أسبوع\" — ده كلام نصب.\n\n"
            "واجب النهاردة: اكتب 3 مهارات عندك (أو بتتعلمها في الدورات دي) — واختار واحدة تحس إنك تقدر تبيعها."
        ),
        "en": (
            "💰 Lesson 1: What is freelancing?\n\n"
            "Freelancing means selling your skill online to clients anywhere — no boss, no fixed job. A client asks for work, you do it, and they pay you.\n\n"
            "Examples of in-demand services:\n"
            "• Designing posts and logos\n"
            "• Writing articles and posts\n"
            "• Programming websites and apps\n"
            "• Translation\n"
            "• Managing social media pages\n"
            "• Data analysis\n\n"
            "⚠️ Honest words from the start: freelancing is not fast money. The beginning is slow — the first client is the hardest, and the first money is small. Whoever succeeds is the one who learns a skill well, works continuously, and builds a reputation. There is no \"earn 1000 dollars in a week\" — that is a scam.\n\n"
            "Today's task: write down 3 skills you have (or are learning in these courses) — and pick one you feel you could sell."
        ),
    },
    {
        "title_ar": "الدرس 2: اختار مهارتك",
        "title_en": "Lesson 2: Pick your skill",
        "ar": (
            "🎯 الدرس 2: اختار مهارتك\n\n"
            "أكبر غلطة في العمل الحر: تحاول تتعلم كل حاجة في نفس الوقت. الصح: مهارة واحدة، وتتقنها.\n\n"
            "اختار مهارتك بـ 3 أسئلة:\n"
            "1️⃣ بتحب تعمل إيه؟ (الحاجة اللي بتستمتع بيها هتكمل فيها)\n"
            "2️⃣ إيه المطلوب في السوق؟ (تصميم، كتابة، برمجة، تسويق، بيانات — كلها مطلوبة)\n"
            "3️⃣ إيه اللي تقدر تتعلمه في 3 شهور؟ (اختار حاجة واقعية لمستواك)\n\n"
            "أمثلة سريعة للبداية:\n"
            "• بتحب الكتابة؟ ابدأ بكتابة البوستات والمقالات\n"
            "• بتحب التصميم؟ ابدأ بـ Canva (دورة التصميم)\n"
            "• بتحب الأرقام؟ ابدأ بتحليل البيانات\n"
            "• بتعرف إنجليزي؟ الترجمة والكتابة بالإنجليزي مطلوبة جدًا\n\n"
            "واجب النهاردة: اختار مهارة واحدة بس والتزم بيها — واكتب خطة 3 شهور: كل أسبوع هتتعلم إيه فيها."
        ),
        "en": (
            "🎯 Lesson 2: Pick your skill\n\n"
            "The biggest mistake in freelancing: trying to learn everything at once. The right way: one skill, and master it.\n\n"
            "Pick your skill with 3 questions:\n"
            "1️⃣ What do you love doing? (What you enjoy, you will continue)\n"
            "2️⃣ What does the market need? (Design, writing, programming, marketing, data — all in demand)\n"
            "3️⃣ What can you learn in 3 months? (Pick something realistic for your level)\n\n"
            "Quick examples to start:\n"
            "• Love writing? Start with posts and articles\n"
            "• Love design? Start with Canva (design course)\n"
            "• Love numbers? Start with data analysis\n"
            "• Know English? Translation and English writing are very much in demand\n\n"
            "Today's task: pick only one skill and commit to it — and write a 3-month plan: what will you learn each week?"
        ),
    },
    {
        "title_ar": "الدرس 3: اعمل حساب على Upwork وFiverr وخمسات",
        "title_en": "Lesson 3: Upwork, Fiverr, Khamsat",
        "ar": (
            "🌐 الدرس 3: اعمل حساب على Upwork وFiverr وخمسات\n\n"
            "المنصات دي هي السوق اللي بيجمعك بالعملاء. أشهر 3 منصات:\n\n"
            "• Upwork: للعملاء الأجانب، مشاريع كبيرة، الدفع بالدولار\n"
            "• Fiverr: بتعرض خدمتك بسعر ثابت، والعميل ييجي لك\n"
            "• خمسات (Khamsat): منصة عربية، التعامل بالعربي والدولار\n\n"
            "خطوات عمل حساب قوي:\n"
            "1️⃣ صورة شخصية واضحة ومحترمة (مش صورة كرتون)\n"
            "2️⃣ عنوان يوضح مهارتك: مثال \"مصمم سوشيال ميديا | بوستات وإعلانات\"\n"
            "3️⃣ وصف صادق: مين انت، بتعمل إيه، وإيه اللي يميزك — من غير كذب ولا مبالغة\n"
            "4️⃣ حط مهاراتك الحقيقية بس\n"
            "5️⃣ اعمل حساب على منصة واحدة الأول، واتقنها، وبعدين زوّد\n\n"
            "⚠️ متدفعش فلوس لأي حد يقولك \"هجيب لك شغل\" — المنصات نفسها مجانية للتسجيل.\n\n"
            "واجب النهاردة: اعمل حساب على منصة واحدة من التلاتة، واكتب العنوان والوصف بتاعك."
        ),
        "en": (
            "🌐 Lesson 3: Upwork, Fiverr, Khamsat\n\n"
            "These platforms are the market that connects you with clients. The 3 most famous:\n\n"
            "• Upwork: for foreign clients, bigger projects, paid in dollars\n"
            "• Fiverr: you offer your service at a fixed price, and clients come to you\n"
            "• Khamsat: an Arab platform, dealing in Arabic and dollars\n\n"
            "Steps for a strong profile:\n"
            "1️⃣ A clear, respectful personal photo (not a cartoon)\n"
            "2️⃣ A title showing your skill: example \"Social media designer | posts and ads\"\n"
            "3️⃣ An honest description: who you are, what you do, what makes you special — no lies, no exaggeration\n"
            "4️⃣ List only your real skills\n"
            "5️⃣ Start with one platform, master it, then add more\n\n"
            "⚠️ Never pay anyone who says \"I will get you work\" — the platforms themselves are free to join.\n\n"
            "Today's task: create an account on one of the three platforms and write your title and description."
        ),
    },
    {
        "title_ar": "الدرس 4: اعمل معرض أعمال من غير عملاء",
        "title_en": "Lesson 4: Portfolio without clients",
        "ar": (
            "🖼️ الدرس 4: اعمل معرض أعمال من غير عملاء\n\n"
            "العميل مش هيدفع لك من غير ما يشوف شغلك. طيب تعمل إيه وانت لسه معندكش عملاء؟ اعمل مشاريع تجريبية!\n\n"
            "إزاي تبني معرض أعمال من الصفر:\n"
            "1️⃣ اختار 3 مشاريع وهمية: مثال — بوستات لمطعم، شعار لمحل، مقال عن موضوع تحبه\n"
            "2️⃣ اعملها بجد كأنها لعميل حقيقي — وبجودة عالية\n"
            "3️⃣ حطها في حسابك على المنصة، أو في ملف Google Drive، أو صفحة Behance مجانية\n"
            "4️⃣ تحت كل مشروع اكتب سطر: \"إيه المشكلة، وإيه الحل اللي عملته\"\n\n"
            "💡 معرض الأعمال ده أهم من الشهادات — العميل بيشتري اللي شايفه بعينه.\n\n"
            "واجب النهاردة: اعمل أول مشروع تجريبي في مهارتك — بوست، أو مقال، أو تصميم — واحفظه في معرض أعمالك."
        ),
        "en": (
            "🖼️ Lesson 4: Portfolio without clients\n\n"
            "A client will not pay you without seeing your work. So what do you do when you have no clients yet? Make sample projects!\n\n"
            "How to build a portfolio from zero:\n"
            "1️⃣ Pick 3 imaginary projects: example — posts for a restaurant, a logo for a shop, an article about a topic you love\n"
            "2️⃣ Make them seriously, as if for a real client — with high quality\n"
            "3️⃣ Put them in your platform profile, or a Google Drive folder, or a free Behance page\n"
            "4️⃣ Under each project write one line: \"what was the problem, and what solution did I make?\"\n\n"
            "💡 This portfolio matters more than certificates — the client buys what they see with their own eyes.\n\n"
            "Today's task: make your first sample project in your skill — a post, an article, or a design — and save it in your portfolio."
        ),
    },
    {
        "title_ar": "الدرس 5: إزاي تكتب عرض يجيب شغل",
        "title_en": "Lesson 5: Proposals that win",
        "ar": (
            "✉️ الدرس 5: إزاي تكتب عرض يجيب شغل\n\n"
            "لما عميل ينشر شغل على Upwork، بيجيله عشرات العروض. عرضك لازم يبان مختلف في أول سطرين.\n\n"
            "العرض القوي فيه:\n"
            "1️⃣ اقرأ طلب العميل كويس الأول — واذكر حاجة من طلبه عشان يعرف إنك قرأت\n"
            "2️⃣ أول سطرين: إزاي هتحل مشكلته — مش \"أنا فلان وعندي خبرة\"\n"
            "3️⃣ مثال واحد من شغلك شبه اللي هو عايزه (حط لينك معرض أعمالك)\n"
            "4️⃣ سؤال ذكي في الآخر: \"تحب التصميم يكون بألوان معينة؟\" — السؤال بيفتح حوار\n"
            "5️⃣ قصير: 5-8 سطور بس. العميل مش هيقرأ مقال\n\n"
            "❌ إياك تنسخ نفس العرض لكل العملاء — العميل بيعرف من أول كلمة.\n\n"
            "واجب النهاردة: اختار أي إعلان شغل على منصة، واكتب عرض كامل ليه بالطريقة دي — حتى لو مش هتبعته."
        ),
        "en": (
            "✉️ Lesson 5: Proposals that win\n\n"
            "When a client posts a job on Upwork, they get dozens of proposals. Yours must stand out in the first two lines.\n\n"
            "A strong proposal has:\n"
            "1️⃣ Read the client's request well first — and mention something from it so they know you read it\n"
            "2️⃣ First two lines: how you will solve their problem — not \"I am X and I have experience\"\n"
            "3️⃣ One example of your work similar to what they want (link your portfolio)\n"
            "4️⃣ A smart question at the end: \"Do you want the design in specific colors?\" — a question opens a conversation\n"
            "5️⃣ Short: 5-8 lines only. The client will not read an essay\n\n"
            "❌ Never copy the same proposal to every client — the client knows from the first word.\n\n"
            "Today's task: pick any job post on a platform and write a full proposal for it this way — even if you will not send it."
        ),
    },
    {
        "title_ar": "الدرس 6: التسعير والتفاوض",
        "title_en": "Lesson 6: Pricing & negotiation",
        "ar": (
            "💵 الدرس 6: التسعير والتفاوض\n\n"
            "أصعب سؤال للمبتدئ: أطلب كام؟\n\n"
            "قواعد التسعير في البداية:\n"
            "1️⃣ ابدأ بسعر قليل بس مش مجاني — الشغل المجاني بيعلّم العميل إن وقتك ببلاش\n"
            "2️⃣ شوف غيرك بيطلب كام في نفس الخدمة على نفس المنصة، وحط سعرك قريب منهم\n"
            "3️⃣ احسب وقتك: لو الشغل هياخد 5 ساعات، والساعة بـ 5 دولار، يبقى 25 دولار — مش أقل\n"
            "4️⃣ كل ما تجمع تقييمات كويسة، زوّد سعرك شوية\n\n"
            "التفاوض:\n"
            "• العميل قال \"غالي\"؟ قوله إيه اللي هياخده بالسعر ده، وقدّم خيار أرخص بخدمة أقل — متخفضش السعر من غير ما تقلل الشغل\n"
            "• اتفق على كل حاجة كتابة قبل ما تبدأ: السعر، عدد التعديلات، وميعاد التسليم\n"
            "• متبدأش شغل من غير اتفاق واضح — الاتفاق الكتابي بيحميك\n\n"
            "واجب النهاردة: حدّد سعر 3 خدمات في مهارتك — واكتبهم في ورقة عندك."
        ),
        "en": (
            "💵 Lesson 6: Pricing & negotiation\n\n"
            "The hardest question for a beginner: how much should I charge?\n\n"
            "Pricing rules at the start:\n"
            "1️⃣ Start with a low price, but not free — free work teaches the client that your time is worthless\n"
            "2️⃣ See what others charge for the same service on the same platform, and set your price near theirs\n"
            "3️⃣ Count your time: if the work takes 5 hours and an hour is 5 dollars, that is 25 dollars — not less\n"
            "4️⃣ As you collect good reviews, raise your price a little\n\n"
            "Negotiation:\n"
            "• Client says \"expensive\"? Tell them what they get for this price, and offer a cheaper option with less service — do not lower the price without reducing the work\n"
            "• Agree on everything in writing before you start: price, number of revisions, delivery date\n"
            "• Do not start work without a clear agreement — a written agreement protects you\n\n"
            "Today's task: set a price for 3 services in your skill — and write them on a paper."
        ),
    },
    {
        "title_ar": "الدرس 7: استلم فلوسك بأمان",
        "title_en": "Lesson 7: Getting paid safely",
        "ar": (
            "🛡️ الدرس 7: استلم فلوسك بأمان\n\n"
            "أهم قاعدة في العمل الحر: فلوسك تتأمن قبل ما تسلّم الشغل.\n\n"
            "✅ الطريقة الآمنة:\n"
            "• اشتغل جوه المنصة (Upwork / Fiverr / خمسات) — المنصة بتحجز فلوس العميل عندها، ولما تسلّم الشغل بتديك فلوسك\n"
            "• على Upwork: اطلب من العميل يعمل Milestone (دفعة محجوزة) قبل ما تبدأ\n"
            "• على Fiverr: العميل بيدفع الأول للمنصة، وانت تستلم بعد التسليم\n"
            "• اسحب فلوسك من المنصة بالطريقة المتاحة في بلدك (Payoneer أو حساب بنكي حسب المنصة)\n\n"
            "❌ احذر النصب:\n"
            "• عميل يقولك \"اشتغل الأول وبعدين هدفع\" من غير ضمان — ارفض\n"
            "• حد يطلب منك تدفع رسوم عشان \"تفتح\" شغل — ده نصب\n"
            "• حد يطلب بيانات بطاقتك البنكية أو كلمة سر — نصب\n"
            "• شغل برّه المنصة في البداية: مفيش ضمان، ومفيش حد يحميك لو العميل مدفعش\n\n"
            "🎉 مبروك! خلصت دورة العمل الحر — دلوقتي عندك الخريطة كاملة: مهارة، حساب، معرض أعمال، عروض، تسعير، ودفع آمن. البداية بطيئة، بس كل عميل راضي بيجيب اللي بعده.\n\n"
            "واجب النهاردة: قدّم على أول شغل حقيقي — حتى لو صغير. أول خطوة هي أصعب خطوة."
        ),
        "en": (
            "🛡️ Lesson 7: Getting paid safely\n\n"
            "The most important rule in freelancing: your money is secured before you deliver the work.\n\n"
            "✅ The safe way:\n"
            "• Work inside the platform (Upwork / Fiverr / Khamsat) — the platform holds the client's money, and when you deliver, it pays you\n"
            "• On Upwork: ask the client to create a Milestone (reserved payment) before you start\n"
            "• On Fiverr: the client pays the platform first, and you receive it after delivery\n"
            "• Withdraw your money from the platform with the method available in your country (Payoneer or bank account, depending on the platform)\n\n"
            "❌ Beware of scams:\n"
            "• A client who says \"work first and I will pay later\" without a guarantee — refuse\n"
            "• Someone asking you to pay fees to \"unlock\" work — that is a scam\n"
            "• Someone asking for your bank card details or password — a scam\n"
            "• Working outside the platform at the start: no guarantee, and nobody protects you if the client does not pay\n\n"
            "🎉 Congratulations! You finished the freelancing course — now you have the full map: a skill, an account, a portfolio, proposals, pricing, and safe payment. The start is slow, but every happy client brings the next one.\n\n"
            "Today's task: apply for your first real job — even a small one. The first step is the hardest step."
        ),
    },
]

DATA_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه تحليل بيانات؟",
        "title_en": "Lesson 1: What is data analysis?",
        "ar": (
            "📊 الدرس 1: يعني إيه تحليل بيانات؟\n\n"
            "تحليل البيانات يعني تاخد أرقام كتير وتحوّلها لقرار صح. كل حاجة حوالينا بيانات: مبيعات محل، مشاهدات فيديو، درجات طلبة، مصاريف البيت.\n\n"
            "مثال بسيط: محل بيبيع 3 منتجات. من غير تحليل، صاحبه مش عارف إيه اللي بيكسب. بالتحليل يعرف:\n"
            "• إيه أكتر منتج بيتباع؟\n"
            "• إمتى المبيعات بتزيد (الصبح ولا بالليل؟)\n"
            "• إيه المنتج اللي بيخسر ولازم يوقفه؟\n\n"
            "أدوات محلل البيانات (هنتعلمها في الدورة دي):\n"
            "1️⃣ إكسل — للجداول والحسابات السريعة\n"
            "2️⃣ SQL — عشان تسأل قواعد البيانات أسئلة (اتعلمناها في دورة SQL)\n"
            "3️⃣ بايثون (pandas) — لتحليل بيانات كبيرة بسرعة\n"
            "4️⃣ Power BI — عشان تعمل لوحات بيانات وشكل حلو\n\n"
            "واجب النهاردة: اختار موضوع فيه أرقام (مبيعات، مصاريف، مشاهدات) واكتب 3 أسئلة عايز تجاوب عليها من الأرقام دي."
        ),
        "en": (
            "📊 Lesson 1: What is data analysis?\n\n"
            "Data analysis means taking lots of numbers and turning them into a good decision. Everything around us is data: a shop's sales, a video's views, students' grades, household expenses.\n\n"
            "Simple example: a shop sells 3 products. Without analysis, the owner does not know what makes money. With analysis they know:\n"
            "• Which product sells most?\n"
            "• When do sales rise (morning or night?)\n"
            "• Which product loses money and must stop?\n\n"
            "A data analyst's tools (we will learn them in this course):\n"
            "1️⃣ Excel — for tables and quick calculations\n"
            "2️⃣ SQL — to ask databases questions (we learned it in the SQL course)\n"
            "3️⃣ Python (pandas) — to analyze big data fast\n"
            "4️⃣ Power BI — to make dashboards that look good\n\n"
            "Today's task: pick a topic with numbers (sales, expenses, views) and write 3 questions you want to answer from those numbers."
        ),
    },
    {
        "title_ar": "الدرس 2: إكسل من الصفر",
        "title_en": "Lesson 2: Excel from zero",
        "ar": (
            "📗 الدرس 2: إكسل من الصفر\n\n"
            "إكسل هو أول أداة تحليل بيانات — موجود على أي جهاز، وسهل.\n\n"
            "ابدأ كده:\n"
            "1️⃣ افتح Excel واعمل جدول: أول صف فيه العناوين (مثال: المنتج | السعر | الكمية | التاريخ)\n"
            "2️⃣ اكتب بياناتك تحت العناوين — صف لكل عملية بيع\n"
            "3️⃣ حدّد الجدول كله، ودوس Ctrl+T عشان يبقى جدول رسمي (ألوان وفلتر تلقائي)\n"
            "4️⃣ الفرز: من تبويب Data دوس Sort — رتب من الأكبر للأصغر أو من الأقدم للأحدث\n"
            "5️⃣ الفلتر: دوس على السهم اللي جنب العنوان، واختار اللي عايز تشوفه بس (مثال: منتج واحد بس)\n\n"
            "💡 جرّب بنفسك: اعمل جدول مبيعات صغير من 10 صفوف، وفرزهم من الأغلى للأرخص.\n\n"
            "واجب النهاردة: اعمل جدول إكسل بمصاريفك الشخصية لمدة أسبوع — التاريخ، الحاجة، والسعر."
        ),
        "en": (
            "📗 Lesson 2: Excel from zero\n\n"
            "Excel is the first data analysis tool — on every computer, and easy.\n\n"
            "Start like this:\n"
            "1️⃣ Open Excel and make a table: the first row has headers (example: Product | Price | Quantity | Date)\n"
            "2️⃣ Write your data under the headers — one row per sale\n"
            "3️⃣ Select the whole table and press Ctrl+T to make it a formal table (colors and automatic filter)\n"
            "4️⃣ Sorting: from the Data tab press Sort — order from biggest to smallest or oldest to newest\n"
            "5️⃣ Filtering: press the arrow next to a header and choose what you want to see only (example: one product only)\n\n"
            "💡 Try it yourself: make a small sales table of 10 rows and sort them from most expensive to cheapest.\n\n"
            "Today's task: make an Excel table with your personal expenses for one week — date, item, and price."
        ),
    },
    {
        "title_ar": "الدرس 3: دوال إكسل الأساسية",
        "title_en": "Lesson 3: Essential Excel formulas",
        "ar": (
            "🧮 الدرس 3: دوال إكسل الأساسية\n\n"
            "الدوال (Formulas) هي اللي بتحوّل إكسل من جدول لحاسبة ذكية. أهم 5 دوال:\n\n"
            "• SUM: بيجمع أرقام — مثال: =SUM(B2:B10) بيجمع كل الأسعار من الصف 2 لـ 10\n"
            "• AVERAGE: بيحسب المتوسط — مثال: =AVERAGE(B2:B10)\n"
            "• COUNT: بيعد الخلايا اللي فيها أرقام — مثال: =COUNT(B2:B10)\n"
            "• IF: لو الشرط صح اعمل كده، ولو غلط اعمل كده — مثال: =IF(B2>100,\"غالي\",\"رخيص\")\n"
            "• VLOOKUP: بيدوّر على قيمة في جدول تاني ويجيب اللي جنبها — مثال: =VLOOKUP(\"أحمد\",A2:B10,2,FALSE)\n\n"
            "القاعدة: كل دالة بتبدأ بـ = وبعدين اسمها وبعدين القيم بين قوسين.\n\n"
            "💡 اكتب الدالة في خلية فاضية، ودوس Enter — النتيجة هتطلع على طول. ولو غيّرت أي رقم، النتيجة بتتحدث لوحدها.\n\n"
            "واجب النهاردة: في جدول مصاريفك، احسب المجموع الكلي بـ SUM والمتوسط بـ AVERAGE — واعمل عمود IF يقول \"كبير\" لو المصروف فوق 100."
        ),
        "en": (
            "🧮 Lesson 3: Essential Excel formulas\n\n"
            "Formulas turn Excel from a table into a smart calculator. The 5 most important:\n\n"
            "• SUM: adds numbers — example: =SUM(B2:B10) adds all prices from row 2 to 10\n"
            "• AVERAGE: calculates the average — example: =AVERAGE(B2:B10)\n"
            "• COUNT: counts cells with numbers — example: =COUNT(B2:B10)\n"
            "• IF: if the condition is true do this, if false do that — example: =IF(B2>100,\"expensive\",\"cheap\")\n"
            "• VLOOKUP: looks up a value in another table and brings what is next to it — example: =VLOOKUP(\"Ahmed\",A2:B10,2,FALSE)\n\n"
            "The rule: every formula starts with = then its name, then the values in parentheses.\n\n"
            "💡 Write the formula in an empty cell and press Enter — the result appears right away. And if you change any number, the result updates by itself.\n\n"
            "Today's task: in your expenses table, calculate the total with SUM and the average with AVERAGE — and add an IF column that says \"big\" if an expense is over 100."
        ),
    },
    {
        "title_ar": "الدرس 4: SQL في التحليل",
        "title_en": "Lesson 4: SQL for analysis",
        "ar": (
            "🗄️ الدرس 4: SQL في التحليل\n\n"
            "اتعلمنا SQL في دورتها — دلوقتي هنستخدمها في التحليل: نسأل قاعدة البيانات أسئلة تطلع لنا أرقام مفيدة.\n\n"
            "تخيل جدول مبيعات (sales) فيه: product و price و qty. جرّب الكود ده على جهازك:\n"
            "import sqlite3\n"
            "conn = sqlite3.connect(\":memory:\")\n"
            "cur = conn.cursor()\n"
            "cur.execute(\"CREATE TABLE sales (product TEXT, price REAL, qty INTEGER)\")\n"
            "cur.execute(\"INSERT INTO sales VALUES ('phone', 5000, 2)\")\n"
            "cur.execute(\"INSERT INTO sales VALUES ('phone', 5000, 3)\")\n"
            "cur.execute(\"INSERT INTO sales VALUES ('charger', 200, 10)\")\n"
            "conn.commit()\n"
            "cur.execute(\"SELECT product, SUM(price * qty) AS total FROM sales GROUP BY product\")\n"
            "print(cur.fetchall())\n\n"
            "هتشوف: [('charger', 2000.0), ('phone', 25000.0)] — يعني التليفون جاب 25000 والشاحن 2000.\n\n"
            "أهم أوامر التحليل:\n"
            "• GROUP BY: يجمع الصفوف المتشابهة (كل منتج لوحده)\n"
            "• SUM / AVG / COUNT: المجموع والمتوسط والعدد\n"
            "• ORDER BY total DESC: رتب من الأكبر للأصغر\n"
            "• WHERE: فلتر قبل الحساب (مثال: WHERE price > 100)\n\n"
            "واجب النهاردة: شغّل الكود ده، وبعدين ضيف منتج رابع بنفسك، واعمل استعلام يطلع متوسط السعر لكل منتج."
        ),
        "en": (
            "🗄️ Lesson 4: SQL for analysis\n\n"
            "We learned SQL in its course — now we use it for analysis: asking the database questions that give useful numbers.\n\n"
            "Imagine a sales table with: product, price and qty. Try this code on your machine:\n"
            "import sqlite3\n"
            "conn = sqlite3.connect(\":memory:\")\n"
            "cur = conn.cursor()\n"
            "cur.execute(\"CREATE TABLE sales (product TEXT, price REAL, qty INTEGER)\")\n"
            "cur.execute(\"INSERT INTO sales VALUES ('phone', 5000, 2)\")\n"
            "cur.execute(\"INSERT INTO sales VALUES ('phone', 5000, 3)\")\n"
            "cur.execute(\"INSERT INTO sales VALUES ('charger', 200, 10)\")\n"
            "conn.commit()\n"
            "cur.execute(\"SELECT product, SUM(price * qty) AS total FROM sales GROUP BY product\")\n"
            "print(cur.fetchall())\n\n"
            "You will see: [('charger', 2000.0), ('phone', 25000.0)] — the phone made 25000 and the charger 2000.\n\n"
            "The most important analysis commands:\n"
            "• GROUP BY: groups similar rows together (each product alone)\n"
            "• SUM / AVG / COUNT: total, average and count\n"
            "• ORDER BY total DESC: sort from biggest to smallest\n"
            "• WHERE: filter before calculating (example: WHERE price > 100)\n\n"
            "Today's task: run this code, then add a fourth product yourself, and write a query that shows the average price per product."
        ),
    },
    {
        "title_ar": "الدرس 5: بايثون مع pandas",
        "title_en": "Lesson 5: Python with pandas",
        "ar": (
            "🐍 الدرس 5: بايثون مع pandas\n\n"
            "pandas هي أشهر مكتبة بايثون لتحليل البيانات — بتقرأ ملفات إكسل وCSV وتحسب في ثواني. جرّب الكود ده على جهازك:\n"
            "import pandas as pd\n"
            "data = {\"product\": [\"phone\", \"phone\", \"charger\"], \"price\": [5000, 5000, 200], \"qty\": [2, 3, 10]}\n"
            "df = pd.DataFrame(data)\n"
            "df[\"total\"] = df[\"price\"] * df[\"qty\"]\n"
            "print(df)\n"
            "print(df.groupby(\"product\")[\"total\"].sum())\n\n"
            "هتشوف الجدول كامل، وبعدين مجموع كل منتج: charger 2000 و phone 25000 — نفس نتيجة SQL بس بكود أقصر.\n\n"
            "أهم أوامر pandas:\n"
            "• pd.read_csv(\"file.csv\") — اقرأ ملف بيانات\n"
            "• df.head() — شوف أول 5 صفوف\n"
            "• df.describe() — ملخص سريع: المتوسط والأكبر والأصغر\n"
            "• df.groupby(\"product\").sum() — اجمع حسب مجموعة\n"
            "• df.sort_values(\"total\") — رتب الجدول\n\n"
            "💡 لو pandas مش متثبتة عندك، اكتب في التيرمينال: pip install pandas\n\n"
            "واجب النهاردة: شغّل الكود ده، وبعدين اعمل DataFrame بمصاريفك من الدرس 2، واحسب مجموع كل نوع مصروف."
        ),
        "en": (
            "🐍 Lesson 5: Python with pandas\n\n"
            "pandas is the most famous Python library for data analysis — it reads Excel and CSV files and calculates in seconds. Try this code on your machine:\n"
            "import pandas as pd\n"
            "data = {\"product\": [\"phone\", \"phone\", \"charger\"], \"price\": [5000, 5000, 200], \"qty\": [2, 3, 10]}\n"
            "df = pd.DataFrame(data)\n"
            "df[\"total\"] = df[\"price\"] * df[\"qty\"]\n"
            "print(df)\n"
            "print(df.groupby(\"product\")[\"total\"].sum())\n\n"
            "You will see the full table, then each product's total: charger 2000 and phone 25000 — the same result as SQL but with shorter code.\n\n"
            "The most important pandas commands:\n"
            "• pd.read_csv(\"file.csv\") — read a data file\n"
            "• df.head() — see the first 5 rows\n"
            "• df.describe() — quick summary: average, biggest, smallest\n"
            "• df.groupby(\"product\").sum() — sum by group\n"
            "• df.sort_values(\"total\") — sort the table\n\n"
            "💡 If pandas is not installed, type in the terminal: pip install pandas\n\n"
            "Today's task: run this code, then make a DataFrame with your expenses from lesson 2, and calculate the total of each expense type."
        ),
    },
    {
        "title_ar": "الدرس 6: عمل لوحة بيانات (Power BI)",
        "title_en": "Lesson 6: Dashboards with Power BI",
        "ar": (
            "📈 الدرس 6: عمل لوحة بيانات (Power BI)\n\n"
            "لوحة البيانات (Dashboard) هي صفحة واحدة فيها رسوم بيانية وأرقام مهمة — المدير يبص عليها ويفهم كل حاجة في دقيقة.\n\n"
            "إزاي تعمل لوحة بيانات بـ Power BI (مجاني من مايكروسوفت):\n"
            "1️⃣ نزّل Power BI Desktop المجاني من موقع مايكروسوفت\n"
            "2️⃣ افتحه ودوس Get Data ← Excel — واختار ملف بياناتك (مثال: جدول المبيعات)\n"
            "3️⃣ من اليمين اسحب الأعمدة للرسوم البيانية:\n"
            "   • اسحب \"product\" و\"total\" — هيطلع رسم بياني بالأعمدة\n"
            "   • اسحب التاريخ — هيطلع خط بياني للمبيعات عبر الوقت\n"
            "4️⃣ دوس على أي رسم عشان تكبّره وتشوف التفاصيل\n"
            "5️⃣ احفظ الملف، وشاركه مع فريقك\n\n"
            "💡 اللوحة الكويسة فيها 3-4 رسوم بس، وكل رسم بيجاوب على سؤال واحد واضح.\n\n"
            "واجب النهاردة: نزّل Power BI، واستورد جدول المبيعات بتاعك، واعمل رسم بياني واحد على الأقل."
        ),
        "en": (
            "📈 Lesson 6: Dashboards with Power BI\n\n"
            "A dashboard is one page with charts and important numbers — a manager looks at it and understands everything in a minute.\n\n"
            "How to make a dashboard with Power BI (free from Microsoft):\n"
            "1️⃣ Download free Power BI Desktop from Microsoft's site\n"
            "2️⃣ Open it and press Get Data ← Excel — and pick your data file (example: the sales table)\n"
            "3️⃣ From the right, drag columns onto charts:\n"
            "   • Drag \"product\" and \"total\" — you get a bar chart\n"
            "   • Drag the date — you get a line chart of sales over time\n"
            "4️⃣ Click any chart to enlarge it and see details\n"
            "5️⃣ Save the file and share it with your team\n\n"
            "💡 A good dashboard has only 3-4 charts, and each chart answers one clear question.\n\n"
            "Today's task: download Power BI, import your sales table, and make at least one chart."
        ),
    },
    {
        "title_ar": "الدرس 7: المشروع الختامي — حلّل بيانات حقيقية",
        "title_en": "Lesson 7: Final project",
        "ar": (
            "🏆 الدرس 7: المشروع الختامي — حلّل بيانات حقيقية\n\n"
            "وصلنا لآخر درس — دلوقتي هتعمل تحليل كامل بنفسك:\n\n"
            "المشروع: اختار بيانات حقيقية عندك — مبيعات محل، مصاريفك، مشاهدات فيديوهاتك، أو أي أرقام — وجاوب على 3 أسئلة:\n"
            "1️⃣ إيه أكتر حاجة بتكسب / بتتصرف؟\n"
            "2️⃣ الأرقام بتزيد ولا بتقل مع الوقت؟\n"
            "3️⃣ إيه القرار اللي هتاخده بناءً على الأرقام؟\n\n"
            "الخطوات:\n"
            "1️⃣ حط البيانات في جدول إكسل نظيف\n"
            "2️⃣ احسب المجاميع والمتوسطات (بإكسل أو SQL أو pandas — اختار اللي يعجبك)\n"
            "3️⃣ اعمل رسم بياني واحد على الأقل يوضح النتيجة\n"
            "4️⃣ اكتب النتيجة في 5 سطور: السؤال، الرقم، والقرار\n\n"
            "🎉 مبروك! انت دلوقتي محلل بيانات مبتدئ — بتعرف تجمع بيانات، تحللها، وتطلع منها قرار.\n\n"
            "واجب النهاردة: ابدأ المشروع — جهّز جدول البيانات بتاعك، واحسب أول رقم."
        ),
        "en": (
            "🏆 Lesson 7: Final project\n\n"
            "We reached the last lesson — now do a full analysis yourself:\n\n"
            "The project: pick real data you have — a shop's sales, your expenses, your videos' views, or any numbers — and answer 3 questions:\n"
            "1️⃣ What earns / costs the most?\n"
            "2️⃣ Are the numbers rising or falling over time?\n"
            "3️⃣ What decision will you take based on the numbers?\n\n"
            "Steps:\n"
            "1️⃣ Put the data in a clean Excel table\n"
            "2️⃣ Calculate totals and averages (with Excel, SQL or pandas — pick what you like)\n"
            "3️⃣ Make at least one chart showing the result\n"
            "4️⃣ Write the result in 5 lines: the question, the number, and the decision\n\n"
            "🎉 Congratulations! You are now a beginner data analyst — you can collect data, analyze it, and make a decision from it.\n\n"
            "Today's task: start the project — prepare your data table and calculate the first number."
        ),
    },
]

MARKETING_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه تسويق رقمي؟",
        "title_en": "Lesson 1: What is digital marketing?",
        "ar": (
            "📣 الدرس 1: يعني إيه تسويق رقمي؟\n\n"
            "التسويق الرقمي يعني توصل لعملاءك على الإنترنت — مش بس إعلانات مدفوعة، لكن كل حاجة بتخلي الناس تعرفك وتشتري منك.\n\n"
            "قنوات التسويق الرقمي:\n"
            "• السوشيال ميديا: فيسبوك، إنستجرام، تيك توك، يوتيوب\n"
            "• محركات البحث: جوجل (الناس تدور عليك)\n"
            "• الإيميل: رسايل للعملاء القدام\n"
            "• المحتوى: بوستات وفيديوهات مفيدة تجيب متابعين\n"
            "• الإعلانات المدفوعة: توصل لناس أكتر بفلوس قليلة\n\n"
            "مثال: محل ملابس بيعمل بوستات لمنتجاته كل يوم + إعلان صغير بـ 100 جنيه — فيوصله ناس من منطقته كلها، من غير ما يفتح فرع تاني.\n\n"
            "واجب النهاردة: اختار مشروع (حقيقي أو وهمي) واكتب: إيه المنتج، ومين العميل، وفين هتوصله على الإنترنت."
        ),
        "en": (
            "📣 Lesson 1: What is digital marketing?\n\n"
            "Digital marketing means reaching your customers on the internet — not only paid ads, but everything that makes people know you and buy from you.\n\n"
            "Digital marketing channels:\n"
            "• Social media: Facebook, Instagram, TikTok, YouTube\n"
            "• Search engines: Google (people search for you)\n"
            "• Email: messages to old customers\n"
            "• Content: useful posts and videos that bring followers\n"
            "• Paid ads: reach more people with little money\n\n"
            "Example: a clothes shop posts its products every day + a small ad for 100 EGP — so people from the whole area reach it, without opening a second branch.\n\n"
            "Today's task: pick a project (real or imaginary) and write: what is the product, who is the customer, and where will you reach them online?"
        ),
    },
    {
        "title_ar": "الدرس 2: اعرف جمهورك",
        "title_en": "Lesson 2: Know your audience",
        "ar": (
            "🎯 الدرس 2: اعرف جمهورك\n\n"
            "أكبر غلطة في التسويق: تكلم \"كل الناس\". اللي بيكلم كل الناس، محدش بيسمعه. لازم تعرف جمهورك بالظبط.\n\n"
            "اعمل بطاقة جمهورك في 5 سطور:\n"
            "1️⃣ السن: مثال — شباب من 18 لـ 30 سنة\n"
            "2️⃣ المكان: فين ساكنين؟ (مصر؟ القاهرة؟)\n"
            "3️⃣ الاهتمامات: بيحبوا إيه؟ (كورة؟ موضة؟ تكنولوجيا؟)\n"
            "4️⃣ المشكلة: إيه اللي مضايقهم وانت هتحله؟\n"
            "5️⃣ فين موجودين على الإنترنت؟ (فيسبوك؟ تيك توك؟ يوتيوب؟)\n\n"
            "مثال: متجر ملابس رياضية — جمهوره: شباب 18-30، بيحبوا الكورة والجيم، مشكلتهم إن اللبس الرياضي الأصلي غالي، وموجودين على إنستجرام وتيك توك.\n\n"
            "واجب النهاردة: اعمل بطاقة جمهور لمشروعك — الخمس سطور دول — واكتبها في ورقة."
        ),
        "en": (
            "🎯 Lesson 2: Know your audience\n\n"
            "The biggest marketing mistake: talking to \"everyone\". Whoever talks to everyone, nobody hears them. You must know your audience exactly.\n\n"
            "Make your audience card in 5 lines:\n"
            "1️⃣ Age: example — young people from 18 to 30\n"
            "2️⃣ Place: where do they live? (Egypt? Cairo?)\n"
            "3️⃣ Interests: what do they love? (Football? Fashion? Technology?)\n"
            "4️⃣ Problem: what bothers them that you will solve?\n"
            "5️⃣ Where are they online? (Facebook? TikTok? YouTube?)\n\n"
            "Example: a sports clothes shop — its audience: young people 18-30, love football and the gym, their problem is that original sports clothes are expensive, and they are on Instagram and TikTok.\n\n"
            "Today's task: make an audience card for your project — these five lines — and write it on a paper."
        ),
    },
    {
        "title_ar": "الدرس 3: صناعة محتوى ينتشر",
        "title_en": "Lesson 3: Content that spreads",
        "ar": (
            "🔥 الدرس 3: صناعة محتوى ينتشر\n\n"
            "المحتوى هو قلب التسويق — بوست أو فيديو مفيد يخلي الناس تتابعك وتشتري منك من غير ما تحس إنك بتبيع.\n\n"
            "معادلة المحتوى اللي ينتشر:\n"
            "1️⃣ أول 3 ثواني: جملة تجذب — سؤال، رقم صادم، أو وعد (\"3 أخطاء بتدمر الواي فاي بتاعك\")\n"
            "2️⃣ النص: فايدة حقيقية — معلومة، حل، أو قصة قصيرة\n"
            "3️⃣ الآخر: سؤال أو دعوة — \"جربت كده قبل كده؟ قولنا في التعليقات\"\n\n"
            "أنواع محتوى ناجحة:\n"
            "• علّم حاجة: \"إزاي تحمي حسابك في دقيقة\"\n"
            "• ورّي نتيجة: قبل وبعد\n"
            "• اسأل رأيهم: استفتاء أو سؤال\n"
            "• اضحكهم: موقف طريف من الشغل\n\n"
            "💡 الثبات أهم من الكمال: بوست واحد كل يوم أحسن من 10 بوستات في يوم واحد وبعدين اختفاء.\n\n"
            "واجب النهاردة: اكتب 3 أفكار بوستات لمشروعك بالمعادلة دي — جملة جذابة + فايدة + سؤال في الآخر."
        ),
        "en": (
            "🔥 Lesson 3: Content that spreads\n\n"
            "Content is the heart of marketing — a useful post or video that makes people follow you and buy from you without feeling that you are selling.\n\n"
            "The formula for content that spreads:\n"
            "1️⃣ First 3 seconds: an attractive line — a question, a shocking number, or a promise (\"3 mistakes destroying your Wi-Fi\")\n"
            "2️⃣ The middle: real value — information, a solution, or a short story\n"
            "3️⃣ The end: a question or invitation — \"Have you tried this before? Tell us in the comments\"\n\n"
            "Successful content types:\n"
            "• Teach something: \"How to protect your account in one minute\"\n"
            "• Show a result: before and after\n"
            "• Ask their opinion: a poll or question\n"
            "• Make them laugh: a funny situation from work\n\n"
            "💡 Consistency beats perfection: one post every day is better than 10 posts in one day and then disappearing.\n\n"
            "Today's task: write 3 post ideas for your project with this formula — a hook + value + a question at the end."
        ),
    },
    {
        "title_ar": "الدرس 4: إعلانات السوشيال ميديا",
        "title_en": "Lesson 4: Social media ads",
        "ar": (
            "💸 الدرس 4: إعلانات السوشيال ميديا\n\n"
            "الإعلان المدفوع بيوصّل بوستك لناس مش متابعينك — بس لازم تعمله صح، وإلا فلوسك تروح على الفاضي.\n\n"
            "خطوات أول إعلان ناجح:\n"
            "1️⃣ الهدف: اختار هدف واحد بس — مثال: \"رسايل على الصفحة\" أو \"زيارات للموقع\"\n"
            "2️⃣ الجمهور: استخدم بطاقة الجمهور من الدرس 2 — السن، المكان، الاهتمامات\n"
            "3️⃣ المحتوى: أحسن بوست عندك (اللي جاب تفاعل من غير إعلان) هو أحسن إعلان\n"
            "4️⃣ الميزانية: ابدأ صغير — 50 أو 100 جنيه في اليوم لمدة 3 أيام، وشوف النتيجة\n"
            "5️⃣ الاختبار: اعمل إعلانين بصورتين مختلفتين، واللي يجيب نتيجة أحسن كمّل عليه\n\n"
            "⚠️ متحطش ميزانية كبيرة من أول يوم — جرّب صغير، اتعلم، وبعدين كبّر.\n\n"
            "واجب النهاردة: جهّز خطة إعلان واحد على الورق: الهدف، الجمهور، المحتوى، والميزانية."
        ),
        "en": (
            "💸 Lesson 4: Social media ads\n\n"
            "A paid ad delivers your post to people who do not follow you — but you must do it right, or your money goes to waste.\n\n"
            "Steps for a first successful ad:\n"
            "1️⃣ Goal: pick one goal only — example: \"messages to the page\" or \"visits to the website\"\n"
            "2️⃣ Audience: use the audience card from lesson 2 — age, place, interests\n"
            "3️⃣ Content: your best post (the one that got engagement without ads) is the best ad\n"
            "4️⃣ Budget: start small — 50 or 100 EGP per day for 3 days, and see the result\n"
            "5️⃣ Testing: make two ads with two different images, and continue with the one that performs better\n\n"
            "⚠️ Do not put a big budget on day one — test small, learn, then scale up.\n\n"
            "Today's task: prepare one ad plan on paper: goal, audience, content, and budget."
        ),
    },
    {
        "title_ar": "الدرس 5: SEO أساسيات",
        "title_en": "Lesson 5: SEO basics",
        "ar": (
            "🔍 الدرس 5: SEO أساسيات\n\n"
            "SEO يعني تخلي جوجل يلاقيك لما حد يدور على اللي انت بتقدمه — من غير ما تدفع إعلانات.\n\n"
            "إزاي جوجل بيختار مين يطلع الأول؟\n"
            "1️⃣ الكلمة المفتاحية: الكلمة اللي الناس بتدور بيها — مثال: \"محل موبايلات في القاهرة\" — لازم تكون في عنوان صفحتك وفي أول سطر\n"
            "2️⃣ المحتوى المفيد: صفحة فيها إجابة حقيقية أحسن من صفحة مليانة كلمات وبس\n"
            "3️⃣ العنوان الواضح: عنوان الصفحة يقول بالظبط إيه اللي جواها\n"
            "4️⃣ سرعة الصفحة: الصفحة البطيئة جوجل بيأخرها — صغّر الصور\n"
            "5️⃣ روابط من مواقع تانية تشاور عليك — دي زي \"تصويت\" لصالحك\n\n"
            "💡 جرّب بنفسك: دوّر على جوجل عن خدمة بتقدمها، وشوف أول 3 نتائج بيعملوا إيه — واتعلم منهم.\n\n"
            "واجب النهاردة: اكتب 5 كلمات مفتاحية الناس ممكن تدور بيها على مشروعك — وحط واحدة في عنوان صفحتك."
        ),
        "en": (
            "🔍 Lesson 5: SEO basics\n\n"
            "SEO means making Google find you when someone searches for what you offer — without paying for ads.\n\n"
            "How does Google choose who comes first?\n"
            "1️⃣ Keyword: the word people search with — example: \"mobile shop in Cairo\" — it must be in your page title and first line\n"
            "2️⃣ Useful content: a page with a real answer beats a page stuffed with words\n"
            "3️⃣ Clear title: the page title says exactly what is inside\n"
            "4️⃣ Page speed: a slow page gets pushed down by Google — shrink your images\n"
            "5️⃣ Links from other sites pointing to you — like a \"vote\" for you\n\n"
            "💡 Try it yourself: search Google for a service you offer, look at the first 3 results and what they do — and learn from them.\n\n"
            "Today's task: write 5 keywords people might search for to find your project — and put one in your page title."
        ),
    },
    {
        "title_ar": "الدرس 6: قياس النتائج",
        "title_en": "Lesson 6: Measuring results",
        "ar": (
            "📈 الدرس 6: قياس النتائج\n\n"
            "التسويق من غير قياس زي سواقة وانت مغمض — لازم تعرف إيه اللي شغال وإيه اللي مش شغال.\n\n"
            "أهم الأرقام اللي تتابعها:\n"
            "• الوصول (Reach): كام واحد شاف البوست\n"
            "• التفاعل: لايكات وتعليقات ومشاركات — التفاعل العالي يعني المحتوى عجب الناس\n"
            "• الضغطات: كام واحد داس على اللينك بتاعك\n"
            "• التحويل: كام واحد اشترى أو بعت رسالة بعد ما شاف الإعلان\n"
            "• التكلفة: كل عميل كلّفك كام جنيه إعلان\n\n"
            "أدوات مجانية للقياس:\n"
            "• فيسبوك وإنستجرام: Insights جوه التطبيق — شوف أي بوست جاب أكتر وصول\n"
            "• جوجل: Google Analytics — شوف الناس بتيجي موقعك منين\n\n"
            "💡 القاعدة: اللي بيجيب نتيجة كمّل عليه، واللي مش بيجيب وقّفه — حتى لو عاجبك انت شخصيًا.\n\n"
            "واجب النهاردة: افتح Insights لصفحتك، واكتب: إيه أحسن بوست عندك؟ وإيه أسوأ بوست؟ وليه؟"
        ),
        "en": (
            "📈 Lesson 6: Measuring results\n\n"
            "Marketing without measuring is like driving with your eyes closed — you must know what works and what does not.\n\n"
            "The most important numbers to follow:\n"
            "• Reach: how many people saw the post\n"
            "• Engagement: likes, comments and shares — high engagement means people liked the content\n"
            "• Clicks: how many people pressed your link\n"
            "• Conversions: how many bought or sent a message after seeing the ad\n"
            "• Cost: how many EGP each customer cost you in ads\n\n"
            "Free tools for measuring:\n"
            "• Facebook and Instagram: Insights inside the app — see which post got the most reach\n"
            "• Google: Google Analytics — see where people come to your site from\n\n"
            "💡 The rule: continue what brings results, stop what does not — even if you personally like it.\n\n"
            "Today's task: open your page's Insights and write: what is your best post? And your worst post? And why?"
        ),
    },
    {
        "title_ar": "الدرس 7: خطة تسويق لمشروع صغير",
        "title_en": "Lesson 7: Marketing plan",
        "ar": (
            "🏆 الدرس 7: خطة تسويق لمشروع صغير\n\n"
            "وصلنا لآخر درس — دلوقتي هتعمل خطة تسويق كاملة لمشروعك في صفحة واحدة:\n\n"
            "الخطة:\n"
            "1️⃣ الهدف: مثال — \"أجيب 100 رسالة استفسار في شهر\"\n"
            "2️⃣ الجمهور: بطاقة الجمهور من الدرس 2\n"
            "3️⃣ القنوات: فيسبوك + إنستجرام (اختار اتنين بس في البداية)\n"
            "4️⃣ المحتوى: جدول أسبوع — مثال: السبت بوست منتج، الاتنين فيديو تعليمي، الأربعاء سؤال للمتابعين\n"
            "5️⃣ الإعلانات: 300 جنيه في الشهر — إعلانين تجريبيين بـ 150 لكل واحد\n"
            "6️⃣ القياس: كل أسبوع راجع الأرقام (الدرس 6) وعدّل الخطة\n\n"
            "🎉 مبروك! خلصت دورة التسويق الرقمي — دلوقتي عندك خطة كاملة، مش معلومات متفرقة.\n\n"
            "واجب النهاردة: اكتب خطة التسويق بتاعتك في صفحة واحدة — وابدأ أول بوست منها النهاردة."
        ),
        "en": (
            "🏆 Lesson 7: Marketing plan\n\n"
            "We reached the last lesson — now make a full marketing plan for your project on one page:\n\n"
            "The plan:\n"
            "1️⃣ Goal: example — \"get 100 inquiry messages in a month\"\n"
            "2️⃣ Audience: the audience card from lesson 2\n"
            "3️⃣ Channels: Facebook + Instagram (pick only two at the start)\n"
            "4️⃣ Content: a weekly table — example: Saturday a product post, Monday a teaching video, Wednesday a question for followers\n"
            "5️⃣ Ads: 300 EGP per month — two test ads at 150 each\n"
            "6️⃣ Measuring: every week review the numbers (lesson 6) and adjust the plan\n\n"
            "🎉 Congratulations! You finished the digital marketing course — now you have a full plan, not scattered information.\n\n"
            "Today's task: write your marketing plan on one page — and publish the first post from it today."
        ),
    },
]

MOBILE_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه تطبيق؟",
        "title_en": "Lesson 1: What is an app?",
        "ar": (
            "📱 الدرس 1: يعني إيه تطبيق؟\n\n"
            "التطبيق هو برنامج بيشتغل على موبايلك: واتساب، فيسبوك، لعبة، تطبيق بنك — كل دي تطبيقات.\n\n"
            "أنواع التطبيقات:\n"
            "• Native: معمول بلغة الموبايل نفسه (Kotlin للأندرويد، Swift للآيفون) — أسرع، بس لازم تعمل نسختين\n"
            "• Cross-platform: كود واحد يشتغل على أندرويد وآيفون مع بعض — زي Flutter وReact Native\n\n"
            "في الدورة دي هنتعلم Flutter — لأنه:\n"
            "• كود واحد لأندرويد وآيفون\n"
            "• سريع في التعلم لو تعرف أساسيات البرمجة\n"
            "• مطلوب جدًا في سوق العمل الحر\n"
            "• مجاني ومفتوح المصدر من جوجل\n\n"
            "مكونات أي تطبيق:\n"
            "• واجهة: الشاشات والأزرار اللي المستخدم بيشوفها\n"
            "• منطق: الكود اللي بيخلي الأزرار تشتغل\n"
            "• بيانات: المعلومات اللي التطبيق بيحفظها (مثال: قايمة المهام)\n\n"
            "واجب النهاردة: اكتب 3 تطبيقات بتستخدمها كل يوم — وإيه أكتر حاجة بتعجبك في كل واحد فيهم."
        ),
        "en": (
            "📱 Lesson 1: What is an app?\n\n"
            "An app is a program that runs on your phone: WhatsApp, Facebook, a game, a bank app — all of these are apps.\n\n"
            "Types of apps:\n"
            "• Native: made in the phone's own language (Kotlin for Android, Swift for iPhone) — fastest, but you must build two versions\n"
            "• Cross-platform: one code runs on Android and iPhone together — like Flutter and React Native\n\n"
            "In this course we will learn Flutter — because:\n"
            "• One code for Android and iPhone\n"
            "• Fast to learn if you know programming basics\n"
            "• Very much in demand in freelance work\n"
            "• Free and open source from Google\n\n"
            "Parts of any app:\n"
            "• Interface: the screens and buttons the user sees\n"
            "• Logic: the code that makes the buttons work\n"
            "• Data: the information the app saves (example: a task list)\n\n"
            "Today's task: write down 3 apps you use every day — and what you like most in each one."
        ),
    },
    {
        "title_ar": "الدرس 2: Flutter من الصفر",
        "title_en": "Lesson 2: Flutter from zero",
        "ar": (
            "🦋 الدرس 2: Flutter من الصفر\n\n"
            "Flutter بيشتغل بلغة اسمها Dart — لغة سهلة شبه بايثون وجافاسكريبت. خطوات التثبيت:\n\n"
            "1️⃣ نزّل Flutter SDK من الموقع الرسمي flutter.dev\n"
            "2️⃣ نزّل Android Studio (مجاني) — عشان تشغّل محاكي أندرويد\n"
            "3️⃣ افتح التيرمينال واكتب: flutter doctor — هيقولك إيه ناقص\n"
            "4️⃣ كمّل أي حاجة ناقصة (عادةً بيطلب تثبيت أدوات أندرويد)\n"
            "5️⃣ اكتب: flutter create my_first_app — وهيعمل لك أول مشروع\n"
            "6️⃣ افتح المشروع في Android Studio ودوس Run — هيطلع لك تطبيق تجريبي شغال!\n\n"
            "💡 لو جهازك ضعيف، جرّب تشغّل التطبيق على موبايلك الحقيقي بدل المحاكي — أسرع وأخف.\n\n"
            "⚠️ التثبيت أول مرة بياخد وقت (تحميل كبير) — خليك صبور، مرة واحدة بس.\n\n"
            "واجب النهاردة: ثبّت Flutter وAndroid Studio، وشغّل أمر flutter doctor — واكتب النتيجة."
        ),
        "en": (
            "🦋 Lesson 2: Flutter from zero\n\n"
            "Flutter works with a language called Dart — an easy language similar to Python and JavaScript. Installation steps:\n\n"
            "1️⃣ Download the Flutter SDK from the official site flutter.dev\n"
            "2️⃣ Download Android Studio (free) — to run an Android emulator\n"
            "3️⃣ Open the terminal and type: flutter doctor — it tells you what is missing\n"
            "4️⃣ Complete anything missing (usually it asks to install Android tools)\n"
            "5️⃣ Type: flutter create my_first_app — it creates your first project\n"
            "6️⃣ Open the project in Android Studio and press Run — a working demo app appears!\n\n"
            "💡 If your computer is weak, try running the app on your real phone instead of the emulator — faster and lighter.\n\n"
            "⚠️ The first installation takes time (big download) — be patient, it is only once.\n\n"
            "Today's task: install Flutter and Android Studio, run the flutter doctor command — and write down the result."
        ),
    },
    {
        "title_ar": "الدرس 3: أول تطبيق",
        "title_en": "Lesson 3: Your first app",
        "ar": (
            "👋 الدرس 3: أول تطبيق\n\n"
            "لما تعمل مشروع Flutter جديد، بيطلع لك تطبيق تجريبي فيه عدّاد — دوس على الزرار والرقم بيزيد. خلينا نفهم الكود:\n\n"
            "الكود الأساسي بيتكون من Widgets — يعني \"قطع\" بتبني بيها الشاشة:\n"
            "• MaterialApp: التطبيق كله\n"
            "• Scaffold: هيكل الشاشة (شريط فوق وجسم في النص)\n"
            "• AppBar: الشريط اللي فوق وفيه العنوان\n"
            "• Text: أي كلام يظهر على الشاشة\n"
            "• Center: بيحط اللي جواه في نص الشاشة\n\n"
            "أبسط تطبيق — شاشة فيها كلمة \"أهلاً\":\n"
            "MaterialApp(\n"
            "  home: Scaffold(\n"
            "    appBar: AppBar(title: Text('تطبيقي الأول')),\n"
            "    body: Center(child: Text('أهلاً بالعالم!')),\n"
            "  ),\n"
            ")\n\n"
            "غيّر كلمة \"أهلاً بالعالم!\" لأي كلام تحبه، وشغّل التطبيق — هتشوف كلامك على الشاشة!\n\n"
            "واجب النهاردة: اعمل أول تطبيق وغيّر النص لاسمك — وشوف اسمك بيظهر على شاشة الموبايل."
        ),
        "en": (
            "👋 Lesson 3: Your first app\n\n"
            "When you create a new Flutter project, you get a demo app with a counter — press the button and the number grows. Let us understand the code:\n\n"
            "The basic code is made of Widgets — \"pieces\" you build the screen with:\n"
            "• MaterialApp: the whole app\n"
            "• Scaffold: the screen structure (a bar on top and a body in the middle)\n"
            "• AppBar: the top bar with the title\n"
            "• Text: any words shown on the screen\n"
            "• Center: puts what is inside it in the middle of the screen\n\n"
            "The simplest app — a screen with the word \"Hello\":\n"
            "MaterialApp(\n"
            "  home: Scaffold(\n"
            "    appBar: AppBar(title: Text('My first app')),\n"
            "    body: Center(child: Text('Hello world!')),\n"
            "  ),\n"
            ")\n\n"
            "Change \"Hello world!\" to any words you like, run the app — and you will see your words on the screen!\n\n"
            "Today's task: make your first app and change the text to your name — and see your name on the phone screen."
        ),
    },
    {
        "title_ar": "الدرس 4: واجهات وأزرار",
        "title_en": "Lesson 4: UI & buttons",
        "ar": (
            "🎨 الدرس 4: واجهات وأزرار\n\n"
            "الشاشة الحلوة بتتبني من Widgets بسيطة بتتركب فوق بعض:\n\n"
            "• Column: بيرتب الحاجات فوق بعض (عمودي)\n"
            "• Row: بيرتب الحاجات جنب بعض (أفقي)\n"
            "• ElevatedButton: زرار لما تدوس عليه بيعمل حاجة\n"
            "• TextField: خانة يكتب فيها المستخدم\n"
            "• Image: صورة من الإنترنت أو من جهازك\n"
            "• Padding: مسافة حوالين أي حاجة عشان الشكل يبقى مريح\n\n"
            "مثال: شاشة فيها عنوان + خانة كتابة + زرار:\n"
            "Column(\n"
            "  children: [\n"
            "    Text('اكتب اسمك:'),\n"
            "    TextField(),\n"
            "    ElevatedButton(\n"
            "      onPressed: () {},\n"
            "      child: Text('أهلاً بيك'),\n"
            "    ),\n"
            "  ],\n"
            ")\n\n"
            "💡 القاعدة: كل حاجة في Flutter هي Widget — حتى المسافات والألوان.\n\n"
            "واجب النهاردة: اعمل شاشة فيها عنوان، وخانة كتابة، وزرارين جنب بعض."
        ),
        "en": (
            "🎨 Lesson 4: UI & buttons\n\n"
            "A nice screen is built from simple Widgets stacked together:\n\n"
            "• Column: arranges things on top of each other (vertical)\n"
            "• Row: arranges things next to each other (horizontal)\n"
            "• ElevatedButton: a button that does something when pressed\n"
            "• TextField: a box where the user types\n"
            "• Image: a picture from the internet or your device\n"
            "• Padding: space around anything so it looks comfortable\n\n"
            "Example: a screen with a title + a text field + a button:\n"
            "Column(\n"
            "  children: [\n"
            "    Text('Write your name:'),\n"
            "    TextField(),\n"
            "    ElevatedButton(\n"
            "      onPressed: () {},\n"
            "      child: Text('Welcome'),\n"
            "    ),\n"
            "  ],\n"
            ")\n\n"
            "💡 The rule: everything in Flutter is a Widget — even spaces and colors.\n\n"
            "Today's task: make a screen with a title, a text field, and two buttons next to each other."
        ),
    },
    {
        "title_ar": "الدرس 5: حفظ بيانات",
        "title_en": "Lesson 5: Saving data",
        "ar": (
            "💾 الدرس 5: حفظ بيانات\n\n"
            "التطبيق من غير حفظ بيانات بينسى كل حاجة لما يتقفل. فيه طريقتين سهلين للحفظ:\n\n"
            "1️⃣ SharedPreferences — لحاجات صغيرة وبسيطة:\n"
            "• اسم المستخدم، أو آخر حاجة عملها، أو إعدادات (فاتح الوضع الليلي ولا لأ)\n"
            "• بتحفظ قيمة واحدة بمفتاح: مثال — احفظ \"name\" = \"أحمد\"\n\n"
            "2️⃣ قاعدة بيانات محلية (sqflite) — لقوايم وحاجات كتير:\n"
            "• قايمة مهام، مصاريف، ملاحظات\n"
            "• بتحفظ جدول كامل زي ما اتعلمنا في دورة SQL\n\n"
            "مثال بسيط — احفظ اسم المستخدم:\n"
            "final prefs = await SharedPreferences.getInstance();\n"
            "await prefs.setString('name', 'أحمد');\n"
            "String name = prefs.getString('name') ?? 'ضيف';\n\n"
            "السطر الأول بيفتح مكان الحفظ، التاني بيحفظ الاسم، والتالت بيقرأه (ولو مش موجود بيحط \"ضيف\").\n\n"
            "واجب النهاردة: اعمل تطبيق يحفظ اسم المستخدم — اكتب اسمك، اقفل التطبيق، افتحه تاني، ولازم اسمك يفضل موجود."
        ),
        "en": (
            "💾 Lesson 5: Saving data\n\n"
            "An app without saving data forgets everything when it closes. There are two easy ways to save:\n\n"
            "1️⃣ SharedPreferences — for small, simple things:\n"
            "• Username, the last thing done, or settings (dark mode on or off)\n"
            "• Saves one value with a key: example — save \"name\" = \"Ahmed\"\n\n"
            "2️⃣ Local database (sqflite) — for lists and lots of things:\n"
            "• Task lists, expenses, notes\n"
            "• Saves a full table like we learned in the SQL course\n\n"
            "Simple example — save the username:\n"
            "final prefs = await SharedPreferences.getInstance();\n"
            "await prefs.setString('name', 'Ahmed');\n"
            "String name = prefs.getString('name') ?? 'Guest';\n\n"
            "The first line opens the storage, the second saves the name, and the third reads it (and if it is missing it puts \"Guest\").\n\n"
            "Today's task: make an app that saves the username — write your name, close the app, open it again, and your name must still be there."
        ),
    },
    {
        "title_ar": "الدرس 6: تطبيق مصاريف",
        "title_en": "Lesson 6: Expenses app",
        "ar": (
            "💸 الدرس 6: تطبيق مصاريف\n\n"
            "دلوقتي هنجمع اللي اتعلمناه في تطبيق واحد حقيقي: تطبيق مصاريف.\n\n"
            "التطبيق يعمل إيه؟\n"
            "1️⃣ شاشة فيها قايمة المصاريف (الاسم + السعر + التاريخ)\n"
            "2️⃣ زرار \"+\" يفتح شاشة إضافة: خانة للاسم وخانة للسعر\n"
            "3️⃣ لما تدوس \"حفظ\"، المصروف يتضاف للقايمة ويتحفظ في قاعدة البيانات\n"
            "4️⃣ فوق القايمة: مجموع المصاريف الكلي (بيتحسب تلقائي)\n"
            "5️⃣ اسحب أي مصروف لليمين عشان تمسحه\n\n"
            "خطوات البناء (يوم ورا يوم):\n"
            "• اليوم الأول: الشاشة الرئيسية والقايمة\n"
            "• اليوم التاني: شاشة الإضافة والزرار\n"
            "• اليوم التالت: الحفظ في قاعدة البيانات\n"
            "• اليوم الرابع: المجموع الكلي والمسح\n\n"
            "💡 التطبيق ده هو نفسه مشروع تحليل البيانات من دورة البيانات — بس دلوقتي على الموبايل!\n\n"
            "واجب النهاردة: ارسم شاشات التطبيق على ورقة — الشاشة الرئيسية وشاشة الإضافة — وحدد مكان كل زرار."
        ),
        "en": (
            "💸 Lesson 6: Expenses app\n\n"
            "Now we combine everything we learned in one real app: an expenses app.\n\n"
            "What does the app do?\n"
            "1️⃣ A screen with the expenses list (name + price + date)\n"
            "2️⃣ A \"+\" button that opens an add screen: a field for the name and a field for the price\n"
            "3️⃣ When you press \"Save\", the expense is added to the list and saved in the database\n"
            "4️⃣ Above the list: the total expenses (calculated automatically)\n"
            "5️⃣ Swipe any expense to the right to delete it\n\n"
            "Building steps (day by day):\n"
            "• Day one: the main screen and the list\n"
            "• Day two: the add screen and the button\n"
            "• Day three: saving in the database\n"
            "• Day four: the total and deleting\n\n"
            "💡 This app is the same project as the data analysis course — but now on mobile!\n\n"
            "Today's task: draw the app screens on paper — the main screen and the add screen — and mark where each button goes."
        ),
    },
    {
        "title_ar": "الدرس 7: نشر التطبيق",
        "title_en": "Lesson 7: Publishing your app",
        "ar": (
            "🚀 الدرس 7: نشر التطبيق\n\n"
            "بعد ما تخلص تطبيقك، لازم الناس تقدر تنزّله — وده اسمه النشر.\n\n"
            "النشر على أندرويد (Google Play):\n"
            "1️⃣ اعمل حساب مطوّر على Google Play — برسوم مرة واحدة (25 دولار)\n"
            "2️⃣ في Flutter اكتب: flutter build appbundle — هيعمل لك ملف النشر\n"
            "3️⃣ ارفع الملف على Google Play Console\n"
            "4️⃣ اكتب وصف التطبيق، وحط صور للشاشات، واختار التصنيف\n"
            "5️⃣ ابعت للمراجعة — بتاخد من يوم لـ 3 أيام عادةً\n\n"
            "قبل النشر، راجع القايمة دي:\n"
            "✅ التطبيق بيشتغل من غير أخطاء؟ جرّبه على موبايل حقيقي\n"
            "✅ أيقونة التطبيق واسم التطبيق واضحين؟\n"
            "✅ مفيش بيانات وهمية أو كلام تجريبي جوه التطبيق؟\n"
            "✅ سياسة خصوصية لو التطبيق بيجمع أي بيانات؟\n\n"
            "💡 بديل مجاني للتجربة: ابعت ملف APK لأصحابك على واتساب أو تليجرام — ينزّلوه ويجرّبوه من غير متجر.\n\n"
            "🎉 مبروك! خلصت دورة تطبيقات الموبايل — دلوقتي تقدر تعمل تطبيق كامل وتنشره.\n\n"
            "واجب النهاردة: اعمل ملف APK من تطبيق المصاريف بتاعك، وابعته لحد من أصحابك يجرّبه."
        ),
        "en": (
            "🚀 Lesson 7: Publishing your app\n\n"
            "After you finish your app, people must be able to download it — that is called publishing.\n\n"
            "Publishing on Android (Google Play):\n"
            "1️⃣ Make a developer account on Google Play — a one-time fee (25 dollars)\n"
            "2️⃣ In Flutter type: flutter build appbundle — it creates the publish file\n"
            "3️⃣ Upload the file to the Google Play Console\n"
            "4️⃣ Write the app description, add screenshots, and pick the category\n"
            "5️⃣ Send it for review — usually takes 1 to 3 days\n\n"
            "Before publishing, check this list:\n"
            "✅ Does the app work without errors? Try it on a real phone\n"
            "✅ Are the app icon and name clear?\n"
            "✅ No fake data or test words inside the app?\n"
            "✅ A privacy policy if the app collects any data?\n\n"
            "💡 A free alternative for testing: send the APK file to your friends on WhatsApp or Telegram — they install it and try it without a store.\n\n"
            "🎉 Congratulations! You finished the mobile apps course — now you can build a full app and publish it.\n\n"
            "Today's task: build an APK file from your expenses app and send it to a friend to try."
        ),
    },
]

LINUX_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه لينكس؟",
        "title_en": "Lesson 1: What is Linux?",
        "ar": (
            "🐧 الدرس 1: يعني إيه لينكس؟\n\n"
            "لينكس هو نظام تشغيل زي ويندوز وماك — بس مجاني ومفتوح المصدر، وبيشغّل معظم سيرفرات الإنترنت في العالم.\n\n"
            "ليه تتعلم لينكس؟\n"
            "• كل سيرفرات المواقع والتطبيقات تقريبًا بتشتغل عليه\n"
            "• مطلوب جدًا في شغل السيرفرات والأمن السيبراني والسحابة\n"
            "• مجاني تمامًا — مفيش ترخيص ولا كراك\n"
            "• خفيف وبيشتغل على أجهزة قديمة\n\n"
            "أشهر توزيعات لينكس (نسخ منه):\n"
            "• Ubuntu — الأسهل للمبتدئين، شكله قريب من ويندوز\n"
            "• Debian — ثابت جدًا، أساس Ubuntu\n"
            "• Kali Linux — للمختصين في الأمن السيبراني (مش للمبتدئين)\n\n"
            "إزاي تبدأ من غير ما تمسح ويندوز؟\n"
            "• جرّب Ubuntu من فلاشة (Live USB) من غير تثبيت\n"
            "• أو ثبّته جوه VirtualBox كجهاز وهمي\n"
            "• أو استخدم WSL على ويندوز — لينكس جوه ويندوز\n\n"
            "واجب النهاردة: نزّل Ubuntu وحضّر فلاشة تجربة، أو فعّل WSL على جهازك."
        ),
        "en": (
            "🐧 Lesson 1: What is Linux?\n\n"
            "Linux is an operating system like Windows and Mac — but free and open source, and it runs most of the world's internet servers.\n\n"
            "Why learn Linux?\n"
            "• Almost all website and app servers run on it\n"
            "• Very much in demand for server, cybersecurity and cloud work\n"
            "• Completely free — no license, no cracks\n"
            "• Light, and runs on old computers\n\n"
            "Famous Linux distributions (versions of it):\n"
            "• Ubuntu — easiest for beginners, looks close to Windows\n"
            "• Debian — very stable, the base of Ubuntu\n"
            "• Kali Linux — for cybersecurity specialists (not for beginners)\n\n"
            "How to start without deleting Windows?\n"
            "• Try Ubuntu from a USB stick (Live USB) without installing\n"
            "• Or install it inside VirtualBox as a virtual machine\n"
            "• Or use WSL on Windows — Linux inside Windows\n\n"
            "Today's task: download Ubuntu and prepare a trial USB stick, or enable WSL on your computer."
        ),
    },
    {
        "title_ar": "الدرس 2: التيرمينال",
        "title_en": "Lesson 2: The terminal",
        "ar": (
            "💻 الدرس 2: التيرمينال\n\n"
            "التيرمينال (سطر الأوامر) هو أهم أداة في لينكس — بتكتب أمر، والجهاز ينفذه. في الأول شكله يخوف، بس بعد 3 أوامر هتحبه.\n\n"
            "افتحه إزاي؟\n"
            "• على Ubuntu: دوس Ctrl+Alt+T\n"
            "• على WSL: افتح تطبيق Ubuntu من قايمة ويندوز\n\n"
            "أول 3 أوامر:\n"
            "• pwd — بيقولك انت فين دلوقتي (أي مجلد)\n"
            "• ls — بيعرض الملفات والمجلدات اللي حواليك\n"
            "• whoami — بيقولك اسم المستخدم بتاعك\n\n"
            "جرّبهم دلوقتي — التيرمينال مش هيكسر حاجة بالأوامر دي. الأوامر دي بتقرأ بس، مش بتمسح ولا بتغيّر.\n\n"
            "💡 نصيحة: السهم اللي فوق في الكيبورد بيجيب آخر أمر كتبته — مش لازم تكتب كل مرة من الأول.\n\n"
            "واجب النهاردة: افتح التيرمينال واكتب التلات أوامر دول، واكتب النتيجة عندك."
        ),
        "en": (
            "💻 Lesson 2: The terminal\n\n"
            "The terminal (command line) is the most important tool in Linux — you type a command and the computer runs it. At first it looks scary, but after 3 commands you will love it.\n\n"
            "How to open it?\n"
            "• On Ubuntu: press Ctrl+Alt+T\n"
            "• On WSL: open the Ubuntu app from the Windows menu\n\n"
            "Your first 3 commands:\n"
            "• pwd — tells you where you are now (which folder)\n"
            "• ls — shows the files and folders around you\n"
            "• whoami — tells you your username\n\n"
            "Try them now — the terminal will not break anything with these commands. They only read, they do not delete or change.\n\n"
            "💡 Tip: the up arrow on your keyboard brings back the last command you typed — no need to type it again.\n\n"
            "Today's task: open the terminal, type these three commands, and write down the result."
        ),
    },
    {
        "title_ar": "الدرس 3: الأوامر الأساسية",
        "title_en": "Lesson 3: Basic commands",
        "ar": (
            "⌨️ الدرس 3: الأوامر الأساسية\n\n"
            "دلوقتي هنتعلم أوامر التنقل والبحث — دي الأوامر اللي هتستخدمها كل يوم:\n\n"
            "التنقل:\n"
            "• cd folder — ادخل مجلد\n"
            "• cd .. — ارجع مجلد لورا\n"
            "• cd ~ — ارجع لمجلد البيت (home)\n\n"
            "العرض والبحث:\n"
            "• ls -la — اعرض كل الملفات حتى المخفية، مع التفاصيل\n"
            "• cat file.txt — اعرض محتوى ملف\n"
            "• grep \"word\" file.txt — دوّر على كلمة جوه ملف\n"
            "• find . -name \"*.txt\" — دوّر على كل ملفات txt\n\n"
            "المساعدة:\n"
            "• man ls — دليل الأمر (شرح كامل) — دوس q عشان تخرج\n"
            "• ls --help — شرح مختصر للأمر\n\n"
            "💡 جرّب: cd ~ وبعدين ls — هتشوف مجلدات البيت بتاعتك (Desktop, Documents...).\n\n"
            "واجب النهاردة: اعمل جولة بالأوامر دي — ادخل 3 مجلدات، ودوّر على ملف باسمه بـ find."
        ),
        "en": (
            "⌨️ Lesson 3: Basic commands\n\n"
            "Now we learn navigation and search commands — the ones you will use every day:\n\n"
            "Navigation:\n"
            "• cd folder — enter a folder\n"
            "• cd .. — go one folder back\n"
            "• cd ~ — go back to your home folder\n\n"
            "Viewing and searching:\n"
            "• ls -la — show all files even hidden ones, with details\n"
            "• cat file.txt — show a file's content\n"
            "• grep \"word\" file.txt — search for a word inside a file\n"
            "• find . -name \"*.txt\" — find all txt files\n\n"
            "Help:\n"
            "• man ls — the command manual (full explanation) — press q to exit\n"
            "• ls --help — a short explanation of the command\n\n"
            "💡 Try: cd ~ then ls — you will see your home folders (Desktop, Documents...).\n\n"
            "Today's task: take a tour with these commands — enter 3 folders and search for a file by name with find."
        ),
    },
    {
        "title_ar": "الدرس 4: الملفات والصلاحيات",
        "title_en": "Lesson 4: Files & permissions",
        "ar": (
            "📁 الدرس 4: الملفات والصلاحيات\n\n"
            "في لينكس، كل ملف ليه 3 صلاحيات: قراءة (r) وكتابة (w) وتنفيذ (x) — ولمين؟ للمالك، وللمجموعة، وللكل.\n\n"
            "أوامر الملفات:\n"
            "• touch file.txt — اعمل ملف فاضي\n"
            "• mkdir myfolder — اعمل مجلد جديد\n"
            "• cp file.txt copy.txt — انسخ ملف\n"
            "• mv file.txt newname.txt — انقل أو غيّر اسم ملف\n"
            "• rm file.txt — امسح ملف (خلي بالك: مفيش سلة مهملات!)\n"
            "• rm -r folder — امسح مجلد وكل اللي جواه\n\n"
            "الصلاحيات:\n"
            "• ls -l — بتشوف الصلاحيات: مثال -rw-r--r-- يعني المالك يقرأ ويكتب، والباقي يقرأ بس\n"
            "• chmod +x script.sh — خلّي الملف قابل للتنفيذ\n"
            "• sudo — نفّذ الأمر بصلاحيات المدير (هيطلب كلمة السر)\n\n"
            "⚠️ احذر: rm -rf / بيمسح كل حاجة — متكتبهوش أبدًا، حتى على سبيل التجربة.\n\n"
            "واجب النهاردة: اعمل مجلد جديد، اعمل جواه ملف، انسخه، غيّر اسمه، وبعدين امسح النسخة."
        ),
        "en": (
            "📁 Lesson 4: Files & permissions\n\n"
            "In Linux, every file has 3 permissions: read (r), write (w) and execute (x) — and for whom? The owner, the group, and everyone.\n\n"
            "File commands:\n"
            "• touch file.txt — create an empty file\n"
            "• mkdir myfolder — create a new folder\n"
            "• cp file.txt copy.txt — copy a file\n"
            "• mv file.txt newname.txt — move or rename a file\n"
            "• rm file.txt — delete a file (careful: there is no recycle bin!)\n"
            "• rm -r folder — delete a folder and everything inside it\n\n"
            "Permissions:\n"
            "• ls -l — shows permissions: example -rw-r--r-- means the owner can read and write, others can only read\n"
            "• chmod +x script.sh — make a file executable\n"
            "• sudo — run a command with admin rights (it asks for your password)\n\n"
            "⚠️ Beware: rm -rf / deletes everything — never type it, not even to try.\n\n"
            "Today's task: make a new folder, create a file inside it, copy it, rename it, then delete the copy."
        ),
    },
    {
        "title_ar": "الدرس 5: تثبيت برامج",
        "title_en": "Lesson 5: Installing software",
        "ar": (
            "📦 الدرس 5: تثبيت برامج\n\n"
            "في لينكس مفيش \"نزّل ملف exe من أي موقع\" — البرامج بتتثبت من مستودع رسمي آمن بأمر واحد.\n\n"
            "على Ubuntu (باستخدام apt):\n"
            "• sudo apt update — حدّث قايمة البرامج المتاحة\n"
            "• sudo apt install firefox — ثبّت فايرفوكس\n"
            "• sudo apt install python3 — ثبّت بايثون\n"
            "• sudo apt remove firefox — احذف برنامج\n"
            "• apt list --installed — شوف إيه المتثبت عندك\n\n"
            "ليه الطريقة دي أحسن؟\n"
            "• البرامج من مصدر رسمي — مفيش فيروسات ولا برامج مزيفة\n"
            "• التحديثات بتيجي بأمر واحد: sudo apt upgrade\n"
            "• الحذف نضيف — مش بيسيب بقايا زي ويندوز\n\n"
            "💡 أول حاجة تعملها على أي جهاز لينكس جديد: sudo apt update && sudo apt upgrade — عشان كل حاجة تبقى محدثة.\n\n"
            "واجب النهاردة: ثبّت برنامج واحد بـ apt — مثال: htop (أداة تشوف بيها البرامج الشغالة) — وبعدين شغّله."
        ),
        "en": (
            "📦 Lesson 5: Installing software\n\n"
            "In Linux there is no \"download an exe file from any site\" — programs install from an official safe repository with one command.\n\n"
            "On Ubuntu (using apt):\n"
            "• sudo apt update — update the list of available programs\n"
            "• sudo apt install firefox — install Firefox\n"
            "• sudo apt install python3 — install Python\n"
            "• sudo apt remove firefox — remove a program\n"
            "• apt list --installed — see what is installed on your machine\n\n"
            "Why is this way better?\n"
            "• Programs come from an official source — no viruses, no fake programs\n"
            "• Updates come with one command: sudo apt upgrade\n"
            "• Removal is clean — it does not leave leftovers like Windows\n\n"
            "💡 The first thing to do on any new Linux machine: sudo apt update && sudo apt upgrade — so everything is up to date.\n\n"
            "Today's task: install one program with apt — example: htop (a tool to see running programs) — then run it."
        ),
    },
    {
        "title_ar": "الدرس 6: سكربتات بسيطة",
        "title_en": "Lesson 6: Simple scripts",
        "ar": (
            "📜 الدرس 6: سكربتات بسيطة\n\n"
            "السكربت هو ملف فيه أوامر بتتنفذ ورا بعض — بدل ما تكتبها كل مرة بإيدك. جرّب السكربت ده:\n"
            "#!/bin/bash\n"
            "echo \"أهلاً بيك يا $USER\"\n"
            "echo \"التاريخ النهاردة: $(date)\"\n"
            "echo \"المساحة الفاضية:\"\n"
            "df -h | grep -E \"^/dev\"\n\n"
            "إزاي تشغله؟\n"
            "1️⃣ احفظ الكود في ملف اسمه welcome.sh\n"
            "2️⃣ اكتب: chmod +x welcome.sh — عشان يبقى قابل للتنفيذ\n"
            "3️⃣ اكتب: ./welcome.sh — وهيطبع ترحيب وتاريخ ومساحة القرص\n\n"
            "شرح سريع:\n"
            "• السطر الأول #!/bin/bash بيقول للينكس: \"ده سكربت باش\"\n"
            "• echo بيطبع كلام على الشاشة\n"
            "• $USER متغير جاهز فيه اسم المستخدم بتاعك\n"
            "• $(date) بينفذ أمر date ويحط نتيجته في النص\n\n"
            "واجب النهاردة: اعمل السكربت ده وشغّله — وبعدين زوّد عليه سطر يطبع عدد الملفات في مجلد البيت (ls ~ | wc -l)."
        ),
        "en": (
            "📜 Lesson 6: Simple scripts\n\n"
            "A script is a file with commands that run one after another — instead of typing them by hand every time. Try this script:\n"
            "#!/bin/bash\n"
            "echo \"Hello $USER\"\n"
            "echo \"Today is: $(date)\"\n"
            "echo \"Free space:\"\n"
            "df -h | grep -E \"^/dev\"\n\n"
            "How to run it?\n"
            "1️⃣ Save the code in a file called welcome.sh\n"
            "2️⃣ Type: chmod +x welcome.sh — to make it executable\n"
            "3️⃣ Type: ./welcome.sh — it prints a greeting, the date and disk space\n\n"
            "Quick explanation:\n"
            "• The first line #!/bin/bash tells Linux: \"this is a bash script\"\n"
            "• echo prints words on the screen\n"
            "• $USER is a ready variable with your username\n"
            "• $(date) runs the date command and puts its result in the text\n\n"
            "Today's task: make this script and run it — then add a line that prints the number of files in your home folder (ls ~ | wc -l)."
        ),
    },
    {
        "title_ar": "الدرس 7: لينكس في السيرفرات",
        "title_en": "Lesson 7: Linux on servers",
        "ar": (
            "🖥️ الدرس 7: لينكس في السيرفرات\n\n"
            "ليه كل سيرفرات العالم لينكس؟ لأنه ثابت، آمن، ومجاني — وبيشتغل من غير شاشة، بالأوامر بس.\n\n"
            "أهم حاجات تعرفها عن السيرفرات:\n"
            "• SSH: بتدخل على السيرفر من بعيد بأمر: ssh user@server-ip — وبتشتغل عليه كأنك قاعد قدامه\n"
            "• الخدمات: أي برنامج بيشتغل على طول في الخلفية اسمه service — مثال: systemctl status nginx\n"
            "• السجلات (logs): لو حاجة باظت، شوف السجل: journalctl -u nginx — هيقولك إيه الغلط\n"
            "• النسخ الاحتياطي: قبل أي تغيير مهم، خد نسخة من ملفاتك\n"
            "• التحديثات: حدّث السيرفر بانتظام: sudo apt update && sudo apt upgrade\n\n"
            "⚠️ قاعدة ذهبية للسيرفرات: متجرّبش أوامر خطيرة على سيرفر حقيقي — جرّب الأول على جهاز وهمي عندك.\n\n"
            "🎉 مبروك! خلصت دورة لينكس — دلوقتي تعرف التيرمينال، والأوامر، والملفات، والسكربتات، وفكرة السيرفرات. دي بداية طريق السيرفرات والسحابة والأمن السيبراني.\n\n"
            "واجب النهاردة: اكتب في ورقة: إيه أكتر 5 أوامر هتستخدمها كل يوم؟ واحفظهم."
        ),
        "en": (
            "🖥️ Lesson 7: Linux on servers\n\n"
            "Why are all the world's servers Linux? Because it is stable, secure and free — and it works without a screen, with commands only.\n\n"
            "The most important things about servers:\n"
            "• SSH: you enter the server from far away with a command: ssh user@server-ip — and work on it as if sitting in front of it\n"
            "• Services: any program running in the background is called a service — example: systemctl status nginx\n"
            "• Logs: if something breaks, check the log: journalctl -u nginx — it tells you what went wrong\n"
            "• Backup: before any important change, take a copy of your files\n"
            "• Updates: update the server regularly: sudo apt update && sudo apt upgrade\n\n"
            "⚠️ Golden rule for servers: never try dangerous commands on a real server — try first on a virtual machine on your computer.\n\n"
            "🎉 Congratulations! You finished the Linux course — now you know the terminal, commands, files, scripts, and the idea of servers. This is the start of the path to servers, cloud and cybersecurity.\n\n"
            "Today's task: write on a paper: what are the 5 commands you will use every day? And memorize them."
        ),
    },
]

JS_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه جافاسكريبت؟",
        "title_en": "Lesson 1: What is JavaScript?",
        "ar": (
            "🟨 الدرس 1: يعني إيه جافاسكريبت؟\n\n"
            "جافاسكريبت (JavaScript) هي اللغة اللي بتخلي صفحات الويب تتحرك وتتفاعل — من غيرها الصفحة تبقى صورة ثابتة.\n\n"
            "الفرق بين التلاتة:\n"
            "• HTML: هيكل الصفحة (العناوين والنصوص والصور)\n"
            "• CSS: شكل الصفحة (الألوان والخطوط)\n"
            "• JavaScript: سلوك الصفحة (الأزرار، القوايم، التفاعل)\n\n"
            "أمثلة من حياتك اليومية:\n"
            "• تدوس زرار \"أعجبني\" والعدد يزيد من غير ما الصفحة تتحمل من الأول\n"
            "• تكتب في خانة بحث وتطلع لك اقتراحات وانت بتكتب\n"
            "• قايمة تفتح وتقفل لما تدوس عليها\n\n"
            "إزاي تجرّبها دلوقتي من غير تثبيت؟\n"
            "افتح أي صفحة في كروم، دوس F12، اختار تبويب Console، واكتب:\n"
            "console.log(\"أهلاً بالعالم!\")\n\n"
            "هتشوف الجملة مطبوعة تحت — انت كده شغّلت أول كود جافاسكريبت!\n\n"
            "واجب النهاردة: افتح الـ Console واكتب 3 جمل بـ console.log — اسمك، وسنك، ومدينتك."
        ),
        "en": (
            "🟨 Lesson 1: What is JavaScript?\n\n"
            "JavaScript is the language that makes web pages move and interact — without it, a page is just a static picture.\n\n"
            "The difference between the three:\n"
            "• HTML: the page structure (titles, texts, images)\n"
            "• CSS: the page look (colors and fonts)\n"
            "• JavaScript: the page behavior (buttons, menus, interaction)\n\n"
            "Examples from your daily life:\n"
            "• You press \"Like\" and the number grows without the page reloading\n"
            "• You type in a search box and suggestions appear while you type\n"
            "• A menu opens and closes when you press it\n\n"
            "How to try it now without installing anything?\n"
            "Open any page in Chrome, press F12, choose the Console tab, and type:\n"
            "console.log(\"Hello world!\")\n\n"
            "You will see the sentence printed below — you just ran your first JavaScript code!\n\n"
            "Today's task: open the Console and write 3 lines with console.log — your name, your age, and your city."
        ),
    },
    {
        "title_ar": "الدرس 2: المتغيرات والدوال",
        "title_en": "Lesson 2: Variables & functions",
        "ar": (
            "📦 الدرس 2: المتغيرات والدوال\n\n"
            "المتغير هو \"علبة\" بتحط فيها قيمة وتستخدمها بعدين. والدالة هي \"وصفة\" بتعمل حاجة معينة كل ما تنادي عليها.\n\n"
            "المتغيرات:\n"
            "let name = \"Ahmed\";\n"
            "let age = 25;\n"
            "let price = 99.5;\n"
            "let isStudent = true;\n"
            "console.log(\"My name is \" + name + \" and I am \" + age);\n\n"
            "let معناها \"اعمل متغير\" — وبعدين اسمه، وبعدين = والقيمة. النصوص بين علامتي تنصيص، والأرقام من غير، وصح/غلط بـ true و false.\n\n"
            "الدوال:\n"
            "function sayHello(userName) {\n"
            "  return \"Hello \" + userName + \"!\";\n"
            "}\n"
            "console.log(sayHello(\"Ahmed\"));\n"
            "console.log(sayHello(\"Mona\"));\n\n"
            "الدالة sayHello بتاخد اسم وترد بجملة ترحيب — وكل ما تنادي عليها باسم مختلف، ترد رد مختلف. ده بيوفر عليك تكرار الكود.\n\n"
            "واجب النهاردة: اعمل متغيرات لاسمك وسنك ومدينتك، واعمل دالة بتطبع جملة تعريف بيك — وجرّبها باسمين مختلفين."
        ),
        "en": (
            "📦 Lesson 2: Variables & functions\n\n"
            "A variable is a \"box\" where you put a value and use it later. A function is a \"recipe\" that does something every time you call it.\n\n"
            "Variables:\n"
            "let name = \"Ahmed\";\n"
            "let age = 25;\n"
            "let price = 99.5;\n"
            "let isStudent = true;\n"
            "console.log(\"My name is \" + name + \" and I am \" + age);\n\n"
            "let means \"make a variable\" — then its name, then = and the value. Texts go between quotes, numbers without quotes, and true/false for yes/no.\n\n"
            "Functions:\n"
            "function sayHello(userName) {\n"
            "  return \"Hello \" + userName + \"!\";\n"
            "}\n"
            "console.log(sayHello(\"Ahmed\"));\n"
            "console.log(sayHello(\"Mona\"));\n\n"
            "The sayHello function takes a name and returns a greeting — and every time you call it with a different name, it answers differently. This saves you from repeating code.\n\n"
            "Today's task: make variables for your name, age and city, and make a function that prints a sentence introducing you — and try it with two different names."
        ),
    },
    {
        "title_ar": "الدرس 3: التفاعل مع الصفحة",
        "title_en": "Lesson 3: Interacting with the page",
        "ar": (
            "🖱️ الدرس 3: التفاعل مع الصفحة\n\n"
            "جافاسكريبت بتقدر تمسك أي حاجة في الصفحة وتغيّرها — ده اسمه DOM.\n\n"
            "اعمل ملف HTML بسيط وحط فيه:\n"
            "<h1 id=\"title\">أهلاً بيك</h1>\n"
            "<button id=\"myBtn\">دوس عليّا</button>\n"
            "<script>\n"
            "document.getElementById(\"myBtn\").onclick = function() {\n"
            "  document.getElementById(\"title\").textContent = \"أهلاً بيك يا بطل!\";\n"
            "};\n"
            "</script>\n\n"
            "شرح الكود:\n"
            "• document.getElementById(\"myBtn\") — بيمسك الزرار من الصفحة\n"
            "• onclick — \"لما حد يدوس على الزرار، اعمل اللي جوه الأقواس\"\n"
            "• textContent — بيغيّر الكلام اللي جوه العنوان\n\n"
            "افتح الملف في المتصفح ودوس على الزرار — العنوان هيتغير قدامك!\n\n"
            "واجب النهاردة: اعمل صفحة فيها عنوان وزرار — ولما تدوس الزرار، العنوان يتغير لاسمك."
        ),
        "en": (
            "🖱️ Lesson 3: Interacting with the page\n\n"
            "JavaScript can grab anything on the page and change it — this is called the DOM.\n\n"
            "Make a simple HTML file and put this in it:\n"
            "<h1 id=\"title\">Welcome</h1>\n"
            "<button id=\"myBtn\">Click me</button>\n"
            "<script>\n"
            "document.getElementById(\"myBtn\").onclick = function() {\n"
            "  document.getElementById(\"title\").textContent = \"Welcome, hero!\";\n"
            "};\n"
            "</script>\n\n"
            "Code explanation:\n"
            "• document.getElementById(\"myBtn\") — grabs the button from the page\n"
            "• onclick — \"when someone presses the button, do what is inside the braces\"\n"
            "• textContent — changes the words inside the title\n\n"
            "Open the file in your browser and press the button — the title will change in front of you!\n\n"
            "Today's task: make a page with a title and a button — when you press the button, the title changes to your name."
        ),
    },
    {
        "title_ar": "الدرس 4: الأحداث والأزرار",
        "title_en": "Lesson 4: Events & buttons",
        "ar": (
            "🔘 الدرس 4: الأحداث والأزرار\n\n"
            "الحدث (Event) هو أي حاجة المستخدم يعملها: دوسة، كتابة، تحريك ماوس. جافاسكريبت بتسمع الأحداث دي وترد عليها.\n\n"
            "أشهر الأحداث:\n"
            "• click — دوسة على زرار أو أي حاجة\n"
            "• input — المستخدم بيكتب في خانة\n"
            "• mouseover — الماوس عدّى فوق حاجة\n"
            "• keydown — المستخدم داس على زرار في الكيبورد\n\n"
            "مثال: عدّاد لايكات — كل دوسة بتزود واحد:\n"
            "let likes = 0;\n"
            "document.getElementById(\"likeBtn\").onclick = function() {\n"
            "  likes = likes + 1;\n"
            "  document.getElementById(\"count\").textContent = likes;\n"
            "};\n\n"
            "ومثال تاني: خانة كتابة بترد على طول وانت بتكتب:\n"
            "document.getElementById(\"nameInput\").oninput = function(event) {\n"
            "  document.getElementById(\"hello\").textContent = \"أهلاً \" + event.target.value;\n"
            "};\n\n"
            "event.target.value يعني \"الكلام اللي المستخدم كتبه دلوقتي في الخانة\".\n\n"
            "واجب النهاردة: اعمل صفحة فيها زرار لايك وعدّاد — وخلّي كل دوسة تزود العدّاد واحد."
        ),
        "en": (
            "🔘 Lesson 4: Events & buttons\n\n"
            "An event is anything the user does: a click, typing, moving the mouse. JavaScript listens to these events and responds to them.\n\n"
            "The most famous events:\n"
            "• click — a press on a button or anything\n"
            "• input — the user is typing in a field\n"
            "• mouseover — the mouse passed over something\n"
            "• keydown — the user pressed a keyboard key\n\n"
            "Example: a like counter — each press adds one:\n"
            "let likes = 0;\n"
            "document.getElementById(\"likeBtn\").onclick = function() {\n"
            "  likes = likes + 1;\n"
            "  document.getElementById(\"count\").textContent = likes;\n"
            "};\n\n"
            "And another example: a text field that answers while you type:\n"
            "document.getElementById(\"nameInput\").oninput = function(event) {\n"
            "  document.getElementById(\"hello\").textContent = \"Hello \" + event.target.value;\n"
            "};\n\n"
            "event.target.value means \"the words the user just typed in the field\".\n\n"
            "Today's task: make a page with a like button and a counter — and make each press add one to the counter."
        ),
    },
    {
        "title_ar": "الدرس 5: جلب بيانات من API",
        "title_en": "Lesson 5: Fetching data from an API",
        "ar": (
            "🌐 الدرس 5: جلب بيانات من API\n\n"
            "API يعني خدمة على الإنترنت بتديك بيانات جاهزة — مثال: أسعار العملات، الطقس، أو بوستات تجريبية. جافاسكريبت بتجيب البيانات دي وتعرضها في صفحتك.\n\n"
            "جرّب الكود ده في الـ Console بتاع المتصفح:\n"
            "fetch(\"https://jsonplaceholder.typicode.com/posts/1\")\n"
            "  .then(function(response) { return response.json(); })\n"
            "  .then(function(post) {\n"
            "    console.log(\"Title: \" + post.title);\n"
            "    console.log(\"Body: \" + post.body);\n"
            "  });\n\n"
            "شرح الكود:\n"
            "• fetch(\"الرابط\") — بيطلب البيانات من الرابط ده\n"
            "• .then — \"لما البيانات توصل، اعمل كده\"\n"
            "• response.json() — بيحوّل الرد لبيانات مفهومة\n"
            "• post.title و post.body — العنوان والنص بتاع البوست رقم 1\n\n"
            "💡 الموقع jsonplaceholder.typicode.com هو موقع تجريبي مجاني للتعلم — بياناته وهمية وآمنة للتجربة.\n\n"
            "واجب النهاردة: شغّل الكود ده في الـ Console، وبعدين غيّر رقم البوست من 1 لـ 5 وشوف النتيجة."
        ),
        "en": (
            "🌐 Lesson 5: Fetching data from an API\n\n"
            "An API is a service on the internet that gives you ready data — example: currency prices, weather, or sample posts. JavaScript fetches this data and shows it on your page.\n\n"
            "Try this code in the browser Console:\n"
            "fetch(\"https://jsonplaceholder.typicode.com/posts/1\")\n"
            "  .then(function(response) { return response.json(); })\n"
            "  .then(function(post) {\n"
            "    console.log(\"Title: \" + post.title);\n"
            "    console.log(\"Body: \" + post.body);\n"
            "  });\n\n"
            "Code explanation:\n"
            "• fetch(\"the link\") — asks for data from that link\n"
            "• .then — \"when the data arrives, do this\"\n"
            "• response.json() — turns the reply into understandable data\n"
            "• post.title and post.body — the title and text of post number 1\n\n"
            "💡 The site jsonplaceholder.typicode.com is a free practice site for learning — its data is fake and safe to try.\n\n"
            "Today's task: run this code in the Console, then change the post number from 1 to 5 and see the result."
        ),
    },
    {
        "title_ar": "الدرس 6: مشروع صفحة تفاعلية",
        "title_en": "Lesson 6: Interactive page project",
        "ar": (
            "🛠️ الدرس 6: مشروع صفحة تفاعلية\n\n"
            "دلوقتي هنجمع كل اللي اتعلمناه في صفحة واحدة: قايمة مهام (To-Do List) تفاعلية.\n\n"
            "الصفحة تعمل إيه؟\n"
            "1️⃣ خانة كتابة + زرار \"ضيف\" — تكتب مهمة وتدوس، تتضاف للقايمة\n"
            "2️⃣ كل مهمة جنبها زرار \"تم\" — لما تدوس عليه، المهمة تتشطب (خط عليها)\n"
            "3️⃣ زرار \"امسح\" — يمسح المهمة من القايمة\n"
            "4️⃣ عدّاد فوق: \"عندك 3 مهام\" — بيتحدث تلقائي\n\n"
            "الخطوات (يوم ورا يوم):\n"
            "• اليوم الأول: الـ HTML — الخانة والزرار والقايمة الفاضية\n"
            "• اليوم التاني: زرار \"ضيف\" بيضيف المهمة للقايمة\n"
            "• اليوم التالت: زرار \"تم\" بيشطب المهمة، وزرار \"امسح\" بيمسحها\n"
            "• اليوم الرابع: العدّاد + شوية CSS عشان الشكل يبقى حلو\n\n"
            "💡 المشروع ده هو أول مشروع حقيقي تحطه في معرض أعمالك — صورته شغالة أحسن من أي شهادة.\n\n"
            "واجب النهاردة: اعمل ملف HTML لقايمة المهام — الخانة والزرار والقايمة — وخلّي زرار \"ضيف\" يشتغل."
        ),
        "en": (
            "🛠️ Lesson 6: Interactive page project\n\n"
            "Now we combine everything we learned in one page: an interactive To-Do List.\n\n"
            "What does the page do?\n"
            "1️⃣ A text field + an \"Add\" button — you write a task and press, it joins the list\n"
            "2️⃣ Each task has a \"Done\" button next to it — when you press it, the task gets crossed out\n"
            "3️⃣ A \"Delete\" button — removes the task from the list\n"
            "4️⃣ A counter on top: \"You have 3 tasks\" — updates automatically\n\n"
            "Steps (day by day):\n"
            "• Day one: the HTML — the field, the button and the empty list\n"
            "• Day two: the \"Add\" button adds the task to the list\n"
            "• Day three: the \"Done\" button crosses out the task, and \"Delete\" removes it\n"
            "• Day four: the counter + some CSS to make it look nice\n\n"
            "💡 This project is the first real project to put in your portfolio — a working screenshot beats any certificate.\n\n"
            "Today's task: make an HTML file for the task list — the field, the button and the list — and make the \"Add\" button work."
        ),
    },
    {
        "title_ar": "الدرس 7: الجاي بعد كده (React)",
        "title_en": "Lesson 7: What is next (React)",
        "ar": (
            "🚀 الدرس 7: الجاي بعد كده (React)\n\n"
            "لو فهمت جافاسكريبت، الخطوة الجاية هي React — أشهر مكتبة لبناء واجهات المواقع والتطبيقات.\n\n"
            "إيه React؟\n"
            "• مكتبة جافاسكريبت من فيسبوك — بتخليك تبني واجهات من \"مكونات\" (Components) جاهزة\n"
            "• بدل ما تكتب كود طويل عشان تغيّر حاجة في الصفحة، React بيحدّث الصفحة لوحده لما البيانات تتغير\n"
            "• مطلوبة جدًا في الوظايف والعمل الحر\n\n"
            "خطة التعلم بعد الدورة دي:\n"
            "1️⃣ راجع الدروس دي كلها واعمل مشروع قايمة المهام كامل\n"
            "2️⃣ اتعلم أساسيات React: المكونات، والـ Props، والـ State\n"
            "3️⃣ اعمل نفس مشروع قايمة المهام بـ React — وهتشوف الفرق بنفسك\n"
            "4️⃣ بعدها: Node.js عشان تعمل السيرفر — وتبقى Full-Stack\n\n"
            "🎉 مبروك! خلصت دورة جافاسكريبت — دلوقتي تعرف المتغيرات والدوال، والتفاعل مع الصفحة، والأحداث، والـ API، وعملت مشروع تفاعلي كامل.\n\n"
            "واجب النهاردة: اكتب خطة تعلمك الجاية في ورقة — إيه أول حاجة هتتعلمها بعد جافاسكريبت؟"
        ),
        "en": (
            "🚀 Lesson 7: What is next (React)\n\n"
            "If you understood JavaScript, the next step is React — the most famous library for building website and app interfaces.\n\n"
            "What is React?\n"
            "• A JavaScript library from Facebook — it lets you build interfaces from ready \"Components\"\n"
            "• Instead of writing long code to change something on the page, React updates the page by itself when the data changes\n"
            "• Very much in demand in jobs and freelance work\n\n"
            "Your learning plan after this course:\n"
            "1️⃣ Review all these lessons and finish the full task-list project\n"
            "2️⃣ Learn React basics: Components, Props, and State\n"
            "3️⃣ Build the same task-list project with React — and see the difference yourself\n"
            "4️⃣ After that: Node.js to build the server — and become Full-Stack\n\n"
            "🎉 Congratulations! You finished the JavaScript course — now you know variables and functions, page interaction, events, APIs, and you built a full interactive project.\n\n"
            "Today's task: write your next learning plan on paper — what is the first thing you will learn after JavaScript?"
        ),
    },
]

DESIGN_LESSONS = [
    {
        "title_ar": "الدرس 1: التصميم للمبتدئين",
        "title_en": "Lesson 1: Design for beginners",
        "ar": (
            "🎨 الدرس 1: التصميم للمبتدئين\n\n"
            "التصميم مش موهبة سحرية — هو قواعد بسيطة أي حد يقدر يتعلمها. لو عرفت القواعد، أي بوست تعمله هيبقى شكله حلو.\n\n"
            "أهم 5 قواعد:\n"
            "1️⃣ البساطة: متحطش حاجات كتير في التصميم — كل ما كان أبسط، كان أوضح\n"
            "2️⃣ التباين: الكلام لازم يبان على الخلفية — كلام غامق على خلفية فاتحة (أو العكس)\n"
            "3️⃣ المحاذاة: العناصر مرتبة على خط واحد — مش كل حاجة في مكان عشوائي\n"
            "4️⃣ التكرار: نفس الخط ونفس الألوان في كل تصاميمك — عشان الناس تعرفك\n"
            "5️⃣ المساحة الفاضية: سيب فراغ حوالين الكلام — العين بترتاح\n\n"
            "أدواتك في الدورة دي:\n"
            "• Canva — للتصميم السريع (مجاني)\n"
            "• CapCut — للمونتاج (مجاني)\n\n"
            "📥 حمّلهم مجانًا من هنا:\n"
            "• Canva: canva.com (من المتصفح) أو من متجر بلاي: https://play.google.com/store/apps/details?id=com.canva.editor\n"
            "• CapCut: capcut.com أو من متجر بلاي: https://play.google.com/store/apps/details?id=com.lemon.lvoverseas\n\n"
            "واجب النهاردة: افتح Canva، وشوف 5 تصاميم جاهزة — واكتب إيه اللي عجبك في كل واحد (الألوان؟ الخط؟ الترتيب؟)."
        ),
        "en": (
            "🎨 Lesson 1: Design for beginners\n\n"
            "Design is not a magic talent — it is simple rules anyone can learn. If you know the rules, any post you make will look good.\n\n"
            "The 5 most important rules:\n"
            "1️⃣ Simplicity: do not put too many things in the design — the simpler it is, the clearer it is\n"
            "2️⃣ Contrast: the words must show on the background — dark text on a light background (or the opposite)\n"
            "3️⃣ Alignment: elements arranged on one line — not everything in a random place\n"
            "4️⃣ Repetition: the same font and colors in all your designs — so people recognize you\n"
            "5️⃣ Empty space: leave space around the words — the eye rests\n\n"
            "Your tools in this course:\n"
            "• Canva — for fast design (free)\n"
            "• CapCut — for video editing (free)\n\n"
            "📥 Download them free here:\n"
            "• Canva: canva.com (in the browser) or from Google Play: https://play.google.com/store/apps/details?id=com.canva.editor\n"
            "• CapCut: capcut.com or from Google Play: https://play.google.com/store/apps/details?id=com.lemon.lvoverseas\n\n"
            "Today's task: open Canva, look at 5 ready designs — and write what you liked in each one (the colors? The font? The layout?)."
        ),
    },
    {
        "title_ar": "الدرس 2: Canva",
        "title_en": "Lesson 2: Canva",
        "ar": (
            "🖌️ الدرس 2: Canva\n\n"
            "Canva هو أسهل برنامج تصميم — بيشتغل من المتصفح أو الموبايل، والنسخة المجانية كفاية.\n\n"
            "📥 التحميل: canva.com من المتصفح، أو التطبيق من متجر بلاي: https://play.google.com/store/apps/details?id=com.canva.editor\n\n"
            "خطوات أول تصميم:\n"
            "1️⃣ افتح canva.com واعمل حساب مجاني\n"
            "2️⃣ دوس \"Create a design\" واختار المقاس — مثال: \"Instagram Post\" (مربع 1080×1080)\n"
            "3️⃣ اختار قالب جاهز (Template) قريب من اللي عايزه — وعدّل عليه\n"
            "4️⃣ غيّر الكلام: دوس على أي نص واكتب كلامك\n"
            "5️⃣ غيّر الألوان والصور من القايمة اللي على الشمال\n"
            "6️⃣ دوس Share ← Download — وحمّل التصميم كصورة\n\n"
            "💡 نصيحة: في البداية استخدم القوالب الجاهزة وعدّل عليها — متبدأش من صفحة فاضية. مع الوقت هتعمل تصاميمك من الصفر.\n\n"
            "واجب النهاردة: اعمل أول تصميم ليك على Canva — بوست فيه جملة تحفيزية — وحمّله عندك."
        ),
        "en": (
            "🖌️ Lesson 2: Canva\n\n"
            "Canva is the easiest design program — it works in the browser or on mobile, and the free version is enough.\n\n"
            "📥 Download: canva.com in the browser, or the app from Google Play: https://play.google.com/store/apps/details?id=com.canva.editor\n\n"
            "Steps for your first design:\n"
            "1️⃣ Open canva.com and make a free account\n"
            "2️⃣ Press \"Create a design\" and pick a size — example: \"Instagram Post\" (square 1080×1080)\n"
            "3️⃣ Pick a ready template close to what you want — and edit it\n"
            "4️⃣ Change the text: press any text and write your words\n"
            "5️⃣ Change colors and pictures from the menu on the left\n"
            "6️⃣ Press Share ← Download — and download the design as an image\n\n"
            "💡 Tip: at the start use ready templates and edit them — do not start from an empty page. With time you will make your designs from scratch.\n\n"
            "Today's task: make your first design on Canva — a post with a motivational sentence — and download it."
        ),
    },
    {
        "title_ar": "الدرس 3: ألوان وخطوط",
        "title_en": "Lesson 3: Colors & fonts",
        "ar": (
            "🌈 الدرس 3: ألوان وخطوط\n\n"
            "الألوان والخطوط هما اللي بيدّوا تصميمك شخصية — واختيار غلط ممكن يبوّظ تصميم حلو.\n\n"
            "الألوان:\n"
            "• اختار لونين أو تلاتة بس في التصميم — مش أكتر\n"
            "• الألوان الدافية (أحمر، برتقالي، أصفر) بتحسس بالحماس والطاقة\n"
            "• الألوان الباردة (أزرق، أخضر) بتحسس بالهدوء والثقة\n"
            "• جرّب موقع coolors.co — بيديك مجموعات ألوان جاهزة ومتناسقة\n\n"
            "الخطوط:\n"
            "• خط واحد للعناوين (كبير وعريض) وخط تاني للنص (واضح وسهل القراءة)\n"
            "• متستخدمش أكتر من خطين في التصميم الواحد\n"
            "• الخط لازم يتقري بسهولة — الخطوط المزخرفة للعناوين بس، مش للنص الطويل\n"
            "• للعربي: خطوط زي Cairo وTajawal وAlmarai شكلها نضيف وبتتقري بسهولة\n\n"
            "واجب النهاردة: اختار لوحة ألوان (3 ألوان) وخطين — دول هيبقوا \"هوية\" تصاميمك من النهاردة."
        ),
        "en": (
            "🌈 Lesson 3: Colors & fonts\n\n"
            "Colors and fonts give your design its personality — a wrong choice can ruin a good design.\n\n"
            "Colors:\n"
            "• Pick only two or three colors in a design — not more\n"
            "• Warm colors (red, orange, yellow) feel exciting and energetic\n"
            "• Cold colors (blue, green) feel calm and trustworthy\n"
            "• Try the site coolors.co — it gives ready, matching color sets\n\n"
            "Fonts:\n"
            "• One font for titles (big and bold) and another for text (clear and easy to read)\n"
            "• Do not use more than two fonts in one design\n"
            "• The font must be easy to read — fancy fonts are for titles only, not long text\n"
            "• For Arabic: fonts like Cairo, Tajawal and Almarai look clean and read easily\n\n"
            "Today's task: pick a color palette (3 colors) and two fonts — these will be the \"identity\" of your designs from today."
        ),
    },
    {
        "title_ar": "الدرس 4: تصميم بوست",
        "title_en": "Lesson 4: Designing a post",
        "ar": (
            "📱 الدرس 4: تصميم بوست\n\n"
            "دلوقتي هنجمع القواعد في بوست كامل — من الفكرة للتحميل:\n\n"
            "خطوات البوست:\n"
            "1️⃣ الفكرة: إيه اللي عايز تقوله؟ (مثال: خصم 20% على منتج)\n"
            "2️⃣ المقاس: بوست إنستجرام مربع (1080×1080) أو ستوري (1080×1920)\n"
            "3️⃣ الخلفية: لون من لوحة ألوانك، أو صورة مناسبة — بس خليها هادية عشان الكلام يبان\n"
            "4️⃣ العنوان: جملة قصيرة وكبيرة — مثال: \"خصم 20% النهاردة بس!\"\n"
            "5️⃣ التفاصيل: سطر أو سطرين صغيرين تحت العنوان\n"
            "6️⃣ الدعوة: \"اطلب دلوقتي\" أو \"ابعت رسالة\" — لازم تقول للناس يعملوا إيه\n"
            "7️⃣ المراجعة: بص على التصميم من بعيد — الكلام باين؟ العين بتروح للعنوان الأول؟\n\n"
            "💡 جرّب تبعت التصميم لصاحبك قبل النشر واسأله: \"فهمت إيه من البوست ده في 3 ثواني؟\"\n\n"
            "واجب النهاردة: صمّم بوست إعلان كامل بالخطوات دي — وحمّله."
        ),
        "en": (
            "📱 Lesson 4: Designing a post\n\n"
            "Now we combine the rules in one full post — from idea to download:\n\n"
            "Post steps:\n"
            "1️⃣ Idea: what do you want to say? (example: 20% discount on a product)\n"
            "2️⃣ Size: Instagram square post (1080×1080) or story (1080×1920)\n"
            "3️⃣ Background: a color from your palette, or a suitable picture — but keep it calm so the words show\n"
            "4️⃣ Title: a short, big sentence — example: \"20% off today only!\"\n"
            "5️⃣ Details: one or two small lines under the title\n"
            "6️⃣ Call to action: \"Order now\" or \"Send a message\" — you must tell people what to do\n"
            "7️⃣ Review: look at the design from far — are the words clear? Does the eye go to the title first?\n\n"
            "💡 Try sending the design to a friend before publishing and ask: \"What did you understand from this post in 3 seconds?\"\n\n"
            "Today's task: design a full ad post with these steps — and download it."
        ),
    },
    {
        "title_ar": "الدرس 5: المونتاج للمبتدئين",
        "title_en": "Lesson 5: Editing for beginners",
        "ar": (
            "🎬 الدرس 5: المونتاج للمبتدئين\n\n"
            "المونتاج هو ترتيب الفيديو: تقطيع، وتركيب، وموسيقى، ونصوص. والفيديو الحلو مش محتاج معدات غالية — موبايلك كفاية.\n\n"
            "أساسيات أي فيديو كويس:\n"
            "1️⃣ قصّ الزيادات: أي ثانية مملة أو صمت طويل — احذفها\n"
            "2️⃣ البداية القوية: أول 3 ثواني يحددوا هل الناس هتكمل ولا هتقلب — ابدأ بأقوى جملة\n"
            "3️⃣ الصوت الواضح: صوّر في مكان هادي، وقرّب الموبايل منك\n"
            "4️⃣ النصوص على الشاشة: ناس كتير بتتفرج من غير صوت — حط أهم الكلام كنص\n"
            "5️⃣ الإيقاع: غيّر المشهد كل 3-5 ثواني عشان المشاهد ميزهقش\n\n"
            "ترتيب الشغل:\n"
            "• صوّر كل المقاطع الأول\n"
            "• رتبها على الخط الزمني (Timeline)\n"
            "• قصّ الزيادات\n"
            "• ضيف موسيقى هادية ونصوص\n"
            "• صدّر الفيديو (Export) بالجودة المناسبة\n\n"
            "واجب النهاردة: صوّر 3 مقاطع قصيرة (كل واحد 10 ثواني) عن أي موضوع — ورتبهم ورا بعض في أي تطبيق مونتاج."
        ),
        "en": (
            "🎬 Lesson 5: Editing for beginners\n\n"
            "Editing is arranging the video: cutting, assembling, music, and texts. A good video does not need expensive equipment — your phone is enough.\n\n"
            "Basics of any good video:\n"
            "1️⃣ Cut the extras: any boring second or long silence — delete it\n"
            "2️⃣ Strong start: the first 3 seconds decide if people continue or scroll — start with your strongest sentence\n"
            "3️⃣ Clear sound: film in a quiet place and hold the phone close to you\n"
            "4️⃣ Text on screen: many people watch without sound — put the important words as text\n"
            "5️⃣ Pace: change the scene every 3-5 seconds so the viewer does not get bored\n\n"
            "Work order:\n"
            "• Film all clips first\n"
            "• Arrange them on the Timeline\n"
            "• Cut the extras\n"
            "• Add calm music and texts\n"
            "• Export the video in the right quality\n\n"
            "Today's task: film 3 short clips (10 seconds each) about any topic — and arrange them one after another in any editing app."
        ),
    },
    {
        "title_ar": "الدرس 6: CapCut",
        "title_en": "Lesson 6: CapCut",
        "ar": (
            "✂️ الدرس 6: CapCut\n\n"
            "CapCut هو أشهر تطبيق مونتاج مجاني — بيشتغل على الموبايل والكمبيوتر، وفيه كل اللي تحتاجه.\n\n"
            "📥 لو مش عندك التطبيق حمّله مجانًا من هنا: capcut.com أو من متجر بلاي: https://play.google.com/store/apps/details?id=com.lemon.lvoverseas\n\n"
            "خطوات أول فيديو على CapCut:\n"
            "1️⃣ افتح التطبيق ودوس New Project — واختار المقاطع اللي صورتها\n"
            "2️⃣ رتب المقاطع على الخط الزمني بالسحب\n"
            "3️⃣ عشان تقصّ: دوس على المقطع، وحرّك الطرفين، أو دوس Split في المكان اللي عايز تقطع عنده\n"
            "4️⃣ ضيف نص: دوس Text — واكتب العنوان، واختار الخط واللون\n"
            "5️⃣ ضيف موسيقى: دوس Audio — واختار موسيقى هادية من المكتبة (أو ارفع موسيقى من جهازك)\n"
            "6️⃣ سرّع أو بطّئ: دوس Speed — سرّع المقاطع المملة 1.5x\n"
            "7️⃣ صدّر: دوس Export — واختار جودة 1080p\n\n"
            "💡 فيه قوالب جاهزة (Templates) في CapCut: اختار قالب، حط صورك، والفيديو يتعمل لوحده — طريقة سريعة تتعلم منها.\n\n"
            "واجب النهاردة: اعمل فيديو 30 ثانية على CapCut — قصّ، نص، وموسيقى — وصدّره."
        ),
        "en": (
            "✂️ Lesson 6: CapCut\n\n"
            "CapCut is the most famous free editing app — it works on mobile and computer, and has everything you need.\n\n"
            "📥 If you do not have the app yet, download it free here: capcut.com or from Google Play: https://play.google.com/store/apps/details?id=com.lemon.lvoverseas\n\n"
            "Steps for your first video on CapCut:\n"
            "1️⃣ Open the app and press New Project — and pick the clips you filmed\n"
            "2️⃣ Arrange the clips on the Timeline by dragging\n"
            "3️⃣ To cut: press a clip, move its edges, or press Split where you want to cut\n"
            "4️⃣ Add text: press Text — write the title and pick the font and color\n"
            "5️⃣ Add music: press Audio — pick calm music from the library (or upload music from your device)\n"
            "6️⃣ Speed up or slow down: press Speed — speed boring clips to 1.5x\n"
            "7️⃣ Export: press Export — and pick 1080p quality\n\n"
            "💡 CapCut has ready templates: pick a template, put your pictures, and the video makes itself — a fast way to learn from.\n\n"
            "Today's task: make a 30-second video on CapCut — cut, text, and music — and export it."
        ),
    },
    {
        "title_ar": "الدرس 7: مشروع فيديو قصير كامل",
        "title_en": "Lesson 7: Full short video project",
        "ar": (
            "🏆 الدرس 7: مشروع فيديو قصير كامل\n\n"
            "وصلنا لآخر درس — دلوقتي هتعمل فيديو قصير كامل من الأول للآخر:\n\n"
            "المشروع: فيديو 60 ثانية عن موضوع تحبه (أو عن منتج/مشروع ليك)\n\n"
            "الخطوات:\n"
            "1️⃣ الفكرة والسكربت: اكتب 3 نقاط هتقولها — جملة جذابة في الأول، ونقطتين في النص، ودعوة في الآخر\n"
            "2️⃣ الصورة المصغّرة: صمّمها على Canva (درس 4) — عنوان كبير وواضح\n"
            "3️⃣ التصوير: صوّر في مكان هادي، إضاءة كويسة، والموبايل ثابت (حطه على حاجة)\n"
            "4️⃣ المونتاج على CapCut: قصّ الزيادات، ضيف نصوص على الشاشة، وموسيقى هادية\n"
            "5️⃣ المراجعة: اتفرج على الفيديو كامل مرة أخيرة — الصوت واضح؟ الكلام مفهوم؟ مفيش غلطة؟\n"
            "6️⃣ النشر: عنوان جذاب + وصف قصير + هاشتاجات\n\n"
            "🎉 مبروك! خلصت دورة التصميم والمونتاج — دلوقتي تقدر تعمل بوست وفيديو كاملين بنفسك.\n\n"
            "واجب النهاردة: ابدأ المشروع — اكتب السكربت بتاع الفيديو بتاعك النهاردة."
        ),
        "en": (
            "🏆 Lesson 7: Full short video project\n\n"
            "We reached the last lesson — now make one full short video from start to finish:\n\n"
            "The project: a 60-second video about a topic you love (or about a product/project of yours)\n\n"
            "Steps:\n"
            "1️⃣ Idea and script: write 3 points you will say — a hook first, two points in the middle, a call to action at the end\n"
            "2️⃣ Thumbnail: design it on Canva (lesson 4) — a big, clear title\n"
            "3️⃣ Filming: film in a quiet place, good light, and the phone steady (put it on something)\n"
            "4️⃣ Editing on CapCut: cut the extras, add on-screen texts, and calm music\n"
            "5️⃣ Review: watch the full video one last time — is the sound clear? Are the words understood? Any mistake?\n"
            "6️⃣ Publishing: catchy title + short description + hashtags\n\n"
            "🎉 Congratulations! You finished the design and editing course — now you can make a full post and video yourself.\n\n"
            "Today's task: start the project — write the script of your video today."
        ),
    },
]

CLOUD_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه سحابة؟",
        "title_en": "Lesson 1: What is the cloud?",
        "ar": (
            "☁️ الدرس 1: يعني إيه سحابة؟\n\n"
            "السحابة (Cloud) يعني تستخدم كمبيوترات وسيرفرات على الإنترنت بدل جهازك — تخزن عليها، وتشغّل عليها برامج ومواقع.\n\n"
            "أمثلة بتستخدمها كل يوم:\n"
            "• صورك على Google Photos — مش على موبايلك بس\n"
            "• ملفاتك على Google Drive — تفتحها من أي جهاز\n"
            "• فيديوهاتك على يوتيوب — متخزنة على سيرفرات جوجل\n"
            "• واتساب بيحفظ نسخة من رسايلك على السحابة\n\n"
            "ليه الشركات بتحب السحابة؟\n"
            "• مش محتاجة تشتري سيرفرات غالية\n"
            "• تقدر تكبّر أو تصغّر حسب الحاجة — تدفع على قد استخدامك\n"
            "• البيانات محفوظة في أكتر من مكان — لو سيرفر باظ، التاني شغال\n\n"
            "أشهر شركات السحابة:\n"
            "• Amazon AWS — الأكبر في العالم\n"
            "• Google Cloud — بتاع جوجل\n"
            "• Microsoft Azure — بتاع مايكروسوفت\n\n"
            "واجب النهاردة: افتح Google Drive بتاعك — شوف مساحتك المجانية كام، وإيه الملفات اللي متخزنة عليه."
        ),
        "en": (
            "☁️ Lesson 1: What is the cloud?\n\n"
            "The cloud means using computers and servers on the internet instead of your own device — storing on them and running programs and websites on them.\n\n"
            "Examples you use every day:\n"
            "• Your photos on Google Photos — not only on your phone\n"
            "• Your files on Google Drive — open them from any device\n"
            "• Your videos on YouTube — stored on Google's servers\n"
            "• WhatsApp saves a copy of your messages on the cloud\n\n"
            "Why do companies love the cloud?\n"
            "• No need to buy expensive servers\n"
            "• You can grow or shrink as needed — you pay for what you use\n"
            "• Data is saved in more than one place — if one server breaks, the other works\n\n"
            "The most famous cloud companies:\n"
            "• Amazon AWS — the biggest in the world\n"
            "• Google Cloud — by Google\n"
            "• Microsoft Azure — by Microsoft\n\n"
            "Today's task: open your Google Drive — see how much free space you have, and what files are stored on it."
        ),
    },
    {
        "title_ar": "الدرس 2: AWS وGoogle Cloud المجاني",
        "title_en": "Lesson 2: Free AWS & Google Cloud",
        "ar": (
            "🎁 الدرس 2: AWS وGoogle Cloud المجاني\n\n"
            "شركات السحابة بتديك فترة مجانية عشان تتعلم — من غير ما تدفع حاجة، بس لازم تسجّل ببطاقة بنكية للتحقق.\n\n"
            "Google Cloud (الأسهل للبداية):\n"
            "• 300 دولار رصيد مجاني لمدة 90 يوم للتجربة\n"
            "• بعدها فيه خدمات مجانية دايمًا بحدود صغيرة (Always Free)\n"
            "• اعمل حساب من console.cloud.google.com\n\n"
            "AWS (أمازون):\n"
            "• سنة كاملة مجانية بحدود (Free Tier) — سيرفر صغير مجاني كل شهر\n"
            "• اعمل حساب من aws.amazon.com\n\n"
            "⚠️ مهم جدًا — عشان متدفعش فلوس بالغلط:\n"
            "• استخدم الخدمات المجانية بس في البداية\n"
            "• اعمل تنبيه ميزانية (Budget Alert) على 0 دولار — لو حاجة هتكلف فلوس، يجيلك إيميل\n"
            "• امسح أي سيرفر أو خدمة بعد ما تخلص التجربة\n"
            "• متشغّلش سيرفرات كبيرة — الصغير المجاني كفاية للتعلم\n\n"
            "واجب النهاردة: اعمل حساب مجاني على Google Cloud أو AWS — وفعّل تنبيه الميزانية."
        ),
        "en": (
            "🎁 Lesson 2: Free AWS & Google Cloud\n\n"
            "Cloud companies give you a free period to learn — without paying anything, but you must register with a bank card for verification.\n\n"
            "Google Cloud (easiest to start):\n"
            "• 300 dollars of free credit for 90 days to try\n"
            "• After that there are always-free services with small limits (Always Free)\n"
            "• Make an account at console.cloud.google.com\n\n"
            "AWS (Amazon):\n"
            "• A full free year with limits (Free Tier) — a small free server every month\n"
            "• Make an account at aws.amazon.com\n\n"
            "⚠️ Very important — so you do not pay money by mistake:\n"
            "• Use only free services at the start\n"
            "• Make a budget alert at 0 dollars — if anything will cost money, you get an email\n"
            "• Delete any server or service after you finish trying it\n"
            "• Do not run big servers — the small free one is enough for learning\n\n"
            "Today's task: make a free account on Google Cloud or AWS — and turn on the budget alert."
        ),
    },
    {
        "title_ar": "الدرس 3: استضافة موقع",
        "title_en": "Lesson 3: Hosting a website",
        "ar": (
            "🌐 الدرس 3: استضافة موقع\n\n"
            "الاستضافة يعني تحط ملفات موقعك على سيرفر على الإنترنت، عشان أي حد يقدر يفتحه من أي مكان.\n\n"
            "خطوات استضافة موقع ثابت (HTML/CSS) مجانًا:\n"
            "1️⃣ جهّز ملفات موقعك — مثال: index.html و style.css\n"
            "2️⃣ اختار استضافة مجانية: GitHub Pages أو Netlify أو Vercel\n"
            "3️⃣ على Netlify مثلاً: اعمل حساب، دوس \"Add new site\"، اسحب ملفات الموقع وحطها — والموقع هيتنشر في دقيقة\n"
            "4️⃣ هيطلع لك رابط — مثال: my-site.netlify.app — ابعته لأي حد يفتحه\n\n"
            "ليه Netlify وGitHub Pages كويسين للبداية؟\n"
            "• مجانيين للمواقع الثابتة\n"
            "• النشر بسحب الملفات — من غير أوامر معقدة\n"
            "• بيدوك شهادة أمان (HTTPS) تلقائي\n\n"
            "💡 لو موقعك فيه بايثون أو قاعدة بيانات (مش ثابت)، هتحتاج سيرفر — ده في درس قواعد البيانات السحابية الجاي.\n\n"
            "واجب النهاردة: اعمل صفحة HTML بسيطة (من دورة HTML/CSS) وانشرها على Netlify — وابعت الرابط لصاحبك."
        ),
        "en": (
            "🌐 Lesson 3: Hosting a website\n\n"
            "Hosting means putting your website files on a server on the internet, so anyone can open it from anywhere.\n\n"
            "Steps to host a static website (HTML/CSS) for free:\n"
            "1️⃣ Prepare your website files — example: index.html and style.css\n"
            "2️⃣ Pick a free host: GitHub Pages, Netlify or Vercel\n"
            "3️⃣ On Netlify for example: make an account, press \"Add new site\", drag your website files and drop them — the site publishes in one minute\n"
            "4️⃣ You get a link — example: my-site.netlify.app — send it to anyone to open\n\n"
            "Why are Netlify and GitHub Pages good for starting?\n"
            "• Free for static websites\n"
            "• Publishing by dragging files — no complicated commands\n"
            "• They give you a security certificate (HTTPS) automatically\n\n"
            "💡 If your site has Python or a database (not static), you will need a server — that is in the next lesson about cloud databases.\n\n"
            "Today's task: make a simple HTML page (from the HTML/CSS course) and publish it on Netlify — and send the link to a friend."
        ),
    },
    {
        "title_ar": "الدرس 4: قواعد بيانات سحابية",
        "title_en": "Lesson 4: Cloud databases",
        "ar": (
            "🗄️ الدرس 4: قواعد بيانات سحابية\n\n"
            "قاعدة البيانات السحابية يعني بيانات موقعك أو تطبيقك متخزنة على سيرفر سحابي — مش على جهازك — فأي حد يقدر يستخدم التطبيق من أي مكان.\n\n"
            "ليه سحابية مش محلية؟\n"
            "• لو جهازك اتقفل، البيانات لسه موجودة على السحابة\n"
            "• أكتر من مستخدم يقدروا يستخدموا نفس البيانات في نفس الوقت\n"
            "• الشركة السحابية بتعمل نسخ احتياطي تلقائي\n\n"
            "أشهر قواعد البيانات السحابية المجانية للبداية:\n"
            "• Firebase (جوجل): قاعدة بيانات جاهزة للتطبيقات — والنسخة المجانية كفاية للتجربة\n"
            "• Supabase: بديل مجاني ومفتوح المصدر — شبه Firebase وبيشتغل بـ SQL اللي اتعلمناه\n"
            "• MongoDB Atlas: قاعدة بيانات مجانية بحدود صغيرة\n\n"
            "مثال: تطبيق المصاريف اللي عملناه في دورة الموبايل — لو حفظ بياناته على Supabase، تقدر تفتح مصاريفك من موبايلك ومن الكمبيوتر.\n\n"
            "واجب النهاردة: اعمل حساب مجاني على Supabase أو Firebase — واعمل أول جدول تجريبي."
        ),
        "en": (
            "🗄️ Lesson 4: Cloud databases\n\n"
            "A cloud database means your website or app data is stored on a cloud server — not on your device — so anyone can use the app from anywhere.\n\n"
            "Why cloud and not local?\n"
            "• If your device turns off, the data is still on the cloud\n"
            "• More than one user can use the same data at the same time\n"
            "• The cloud company makes automatic backups\n\n"
            "The most famous free cloud databases to start:\n"
            "• Firebase (Google): a ready database for apps — the free version is enough for trying\n"
            "• Supabase: a free, open-source alternative — like Firebase and works with the SQL we learned\n"
            "• MongoDB Atlas: a free database with small limits\n\n"
            "Example: the expenses app we made in the mobile course — if it saves its data on Supabase, you can open your expenses from your phone and your computer.\n\n"
            "Today's task: make a free account on Supabase or Firebase — and create your first trial table."
        ),
    },
    {
        "title_ar": "الدرس 5: نسخ احتياطي",
        "title_en": "Lesson 5: Backups",
        "ar": (
            "💾 الدرس 5: نسخ احتياطي\n\n"
            "النسخة الاحتياطية (Backup) يعني نسخة تانية من بياناتك في مكان تاني — لو الأصل ضاع، ترجع النسخة.\n\n"
            "قاعدة 3-2-1 الذهبية:\n"
            "• 3 نسخ من بياناتك المهمة\n"
            "• على نوعين مختلفين (مثال: جهازك + سحابة)\n"
            "• ونسخة واحدة على الأقل بعيدة عن البيت (على السحابة مثلاً)\n\n"
            "إزاي تطبقها ببلاش؟\n"
            "1️⃣ ملفاتك المهمة على Google Drive أو OneDrive — بتتزامن تلقائي\n"
            "2️⃣ صور موبايلك على Google Photos — نسخة تلقائية\n"
            "3️⃣ كود مشاريعك على GitHub — نسخة تالتة ومجانية\n"
            "4️⃣ كل شهر: خد نسخة من ملفاتك المهمة على فلاشة وحطها في مكان آمن\n\n"
            "⚠️ جرّب ترجّع النسخة مرة واحدة على الأقل — نسخة احتياطية مش متجربة = مفيش نسخة احتياطية.\n\n"
            "واجب النهاردة: فعّل المزامنة التلقائية لـ Google Drive أو OneDrive على جهازك — وتأكد إن أهم ملفاتك عليه."
        ),
        "en": (
            "💾 Lesson 5: Backups\n\n"
            "A backup is a second copy of your data in another place — if the original is lost, you restore the copy.\n\n"
            "The golden 3-2-1 rule:\n"
            "• 3 copies of your important data\n"
            "• On two different kinds (example: your device + cloud)\n"
            "• And at least one copy far from home (on the cloud, for example)\n\n"
            "How to apply it for free?\n"
            "1️⃣ Your important files on Google Drive or OneDrive — they sync automatically\n"
            "2️⃣ Your phone photos on Google Photos — automatic copy\n"
            "3️⃣ Your project code on GitHub — a third, free copy\n"
            "4️⃣ Every month: copy your important files to a USB stick and keep it somewhere safe\n\n"
            "⚠️ Try restoring the backup at least once — a backup never tested = no backup at all.\n\n"
            "Today's task: turn on automatic sync for Google Drive or OneDrive on your device — and make sure your most important files are on it."
        ),
    },
    {
        "title_ar": "الدرس 6: أمان السحابة",
        "title_en": "Lesson 6: Cloud security",
        "ar": (
            "🔐 الدرس 6: أمان السحابة\n\n"
            "بياناتك على السحابة آمنة — بس بشرط تعمل اللي عليك. أهم قواعد الأمان:\n\n"
            "1️⃣ كلمة سر قوية + تحقق بخطوتين على حساب السحابة — ده أهم حاجة (راجع دورة الأمن السيبراني)\n"
            "2️⃣ صلاحيات قليلة: كل شخص أو تطبيق ياخد أقل صلاحية يحتاجها — مش \"كل الصلاحيات\"\n"
            "3️⃣ مفاتيح API سرية: أي مفتاح أو كلمة سر للبرمجة متحطهوش في الكود اللي بتنشره على GitHub — حطه في ملف إعدادات منفصل ومخفي\n"
            "4️⃣ تشفير: السحابة بتشفر بياناتك وهي رايحة وجاية — تأكد إن رابط موقعك بيبدأ بـ https مش http\n"
            "5️⃣ راجع مين بيدخل: كل فترة شوف الأجهزة المتصلة بحسابك، واحذف أي جهاز مش عارفه\n\n"
            "⚠️ أشهر غلطة: ناس بتنشر مفاتيح AWS أو Firebase على GitHub بالغلط — وحد يلاقيها ويدفعهم آلاف الدولارات. متعملش كده أبدًا.\n\n"
            "واجب النهاردة: فعّل التحقق بخطوتين على حساب Google Cloud أو AWS بتاعك — وراجع الأجهزة المتصلة بحساب جوجل."
        ),
        "en": (
            "🔐 Lesson 6: Cloud security\n\n"
            "Your data on the cloud is safe — but only if you do your part. The most important security rules:\n\n"
            "1️⃣ Strong password + two-step verification on your cloud account — the most important thing (review the cybersecurity course)\n"
            "2️⃣ Few permissions: every person or app gets the smallest permission it needs — not \"all permissions\"\n"
            "3️⃣ API keys are secret: any key or password for programming must not go in code you publish on GitHub — put it in a separate, hidden settings file\n"
            "4️⃣ Encryption: the cloud encrypts your data on the way — make sure your site link starts with https, not http\n"
            "5️⃣ Check who enters: every while, look at the devices connected to your account and remove any device you do not know\n\n"
            "⚠️ The most famous mistake: people publish AWS or Firebase keys on GitHub by accident — and someone finds them and charges them thousands of dollars. Never do that.\n\n"
            "Today's task: turn on two-step verification for your Google Cloud or AWS account — and review the devices connected to your Google account."
        ),
    },
    {
        "title_ar": "الدرس 7: مشروع — ارفع موقعك على السحابة",
        "title_en": "Lesson 7: Final project",
        "ar": (
            "🏆 الدرس 7: مشروع — ارفع موقعك على السحابة\n\n"
            "وصلنا لآخر درس — دلوقتي هترفع موقعك كامل على السحابة:\n\n"
            "المشروع:\n"
            "1️⃣ جهّز موقعك: صفحة HTML/CSS من دورة تصميم الويب — أو موقعك الشخصي\n"
            "2️⃣ انشره على Netlify أو Vercel (درس 3) — وخد الرابط\n"
            "3️⃣ لو موقعك فيه بيانات: اربطه بقاعدة بيانات Supabase المجانية (درس 4)\n"
            "4️⃣ فعّل النسخ الاحتياطي: احفظ نسخة من ملفات الموقع على Google Drive (درس 5)\n"
            "5️⃣ أمّن حسابك: تحقق بخطوتين + راجع الصلاحيات (درس 6)\n"
            "6️⃣ ابعت رابط موقعك لـ 3 أصحاب — واسألهم: الموقع فتح بسرعة؟ شكله حلو؟\n\n"
            "🎉 مبروك! خلصت دورة السحابة — دلوقتي تعرف يعني إيه سحابة، وتستضيف موقع، وتستخدم قواعد بيانات سحابية، وتعمل نسخ احتياطي، وتحمي حسابك.\n\n"
            "واجب النهاردة: ابدأ الخطوة الأولى — جهّز ملفات موقعك للنشر."
        ),
        "en": (
            "🏆 Lesson 7: Final project\n\n"
            "We reached the last lesson — now put your full website on the cloud:\n\n"
            "The project:\n"
            "1️⃣ Prepare your site: an HTML/CSS page from the web design course — or your personal site\n"
            "2️⃣ Publish it on Netlify or Vercel (lesson 3) — and take the link\n"
            "3️⃣ If your site has data: connect it to a free Supabase database (lesson 4)\n"
            "4️⃣ Turn on backup: save a copy of the site files on Google Drive (lesson 5)\n"
            "5️⃣ Secure your account: two-step verification + review permissions (lesson 6)\n"
            "6️⃣ Send your site link to 3 friends — and ask them: did the site open fast? Does it look good?\n\n"
            "🎉 Congratulations! You finished the cloud course — now you know what the cloud is, how to host a site, use cloud databases, make backups, and protect your account.\n\n"
            "Today's task: start the first step — prepare your website files for publishing."
        ),
    },
]

ECOMMERCE_LESSONS = [
    {
        "title_ar": "الدرس 1: يعني إيه متجر إلكتروني؟",
        "title_en": "Lesson 1: What is e-commerce?",
        "ar": (
            "🛒 الدرس 1: يعني إيه متجر إلكتروني؟\n\n"
            "المتجر الإلكتروني هو محل على الإنترنت — الناس تدخل، تتفرج، تشتري، وتدفع، من غير ما تروح أي مكان.\n\n"
            "ليه التجارة الإلكترونية بتكبر؟\n"
            "• الزبون بيشتري في أي وقت — حتى الساعة 3 الفجر\n"
            "• توصل لعملاء في أي محافظة — مش منطقتك بس\n"
            "• تكلفة أقل من محل حقيقي — مفيش إيجار ولا كهربا لمحل\n"
            "• تقدر تبدأ صغير وتكبّر مع الوقت\n\n"
            "أمثلة لمتاجر إلكترونية:\n"
            "• متجر ملابس، أو إكسسوارات، أو منتجات يدوية\n"
            "• متجر منتجات رقمية: كتب إلكترونية، تصاميم، كورسات\n"
            "• البيع على فيسبوك وإنستجرام (من غير متجر كامل في البداية)\n\n"
            "⚠️ كلام صادق: المتجر مش بيبيع لوحده — لازم منتج كويس، وصور حلوة، وتسويق (دورة التسويق الرقمي)، وخدمة عملاء محترمة.\n\n"
            "واجب النهاردة: اكتب 5 منتجات تقدر تبيعها على الإنترنت — منهم منتجين تقدر تعملهم أو تجيبهم بسهولة."
        ),
        "en": (
            "🛒 Lesson 1: What is e-commerce?\n\n"
            "An online store is a shop on the internet — people enter, look around, buy, and pay, without going anywhere.\n\n"
            "Why is e-commerce growing?\n"
            "• The customer buys any time — even at 3 AM\n"
            "• You reach customers in any city — not only your area\n"
            "• Lower cost than a real shop — no rent, no shop electricity\n"
            "• You can start small and grow with time\n\n"
            "Examples of online stores:\n"
            "• A clothes shop, accessories, or handmade products\n"
            "• A digital products shop: e-books, designs, courses\n"
            "• Selling on Facebook and Instagram (without a full store at the start)\n\n"
            "⚠️ Honest words: a store does not sell by itself — you need a good product, nice pictures, marketing (the digital marketing course), and respectful customer service.\n\n"
            "Today's task: write 5 products you could sell online — including two you can make or get easily."
        ),
    },
    {
        "title_ar": "الدرس 2: اختار منتجك",
        "title_en": "Lesson 2: Pick your product",
        "ar": (
            "🎯 الدرس 2: اختار منتجك\n\n"
            "اختيار المنتج هو أهم قرار في المتجر — منتج غلط يعني متجر ميت.\n\n"
            "اختار منتجك بـ 4 أسئلة:\n"
            "1️⃣ الناس بتدور عليه؟ دوّر على جوجل وفيسبوك — فيه ناس بتسأل عنه؟\n"
            "2️⃣ تقدر تجيبه بسعر كويس؟ (سعره جملة أقل من سعر البيع بفرق يستاهل)\n"
            "3️⃣ سهل شحنه؟ (صغير وخفيف ومش بيتكسر — الشحن الصعب بياكل الربح)\n"
            "4️⃣ فيه منافسة كتير؟ (منافسة قليلة أحسن في البداية)\n\n"
            "أفكار منتجات مناسبة للبداية:\n"
            "• إكسسوارات موبايل\n"
            "• منتجات يدوية (شموع، صابون، تطريز)\n"
            "• ملابس أطفال\n"
            "• منتجات رقمية (تصاميم جاهزة، قوالب) — مفيش شحن أصلًا!\n\n"
            "💡 ابدأ بمنتج واحد أو اتنين بس — متجر فيه 100 منتج من أول يوم صعب تديره.\n\n"
            "واجب النهاردة: اختار منتج واحد من قايمة الدرس اللي فات، وجاوب على الأربع أسئلة دول عنه."
        ),
        "en": (
            "🎯 Lesson 2: Pick your product\n\n"
            "Picking the product is the most important decision in the store — a wrong product means a dead store.\n\n"
            "Pick your product with 4 questions:\n"
            "1️⃣ Do people search for it? Search Google and Facebook — are people asking about it?\n"
            "2️⃣ Can you get it at a good price? (Wholesale price lower than selling price with a worthy difference)\n"
            "3️⃣ Is it easy to ship? (Small, light, and does not break — hard shipping eats the profit)\n"
            "4️⃣ Is there a lot of competition? (Little competition is better at the start)\n\n"
            "Product ideas good for starting:\n"
            "• Mobile accessories\n"
            "• Handmade products (candles, soap, embroidery)\n"
            "• Children's clothes\n"
            "• Digital products (ready designs, templates) — no shipping at all!\n\n"
            "💡 Start with one or two products only — a store with 100 products from day one is hard to manage.\n\n"
            "Today's task: pick one product from the last lesson's list and answer these four questions about it."
        ),
    },
    {
        "title_ar": "الدرس 3: اعمل متجر",
        "title_en": "Lesson 3: Build your store",
        "ar": (
            "🏪 الدرس 3: اعمل متجر\n\n"
            "مش لازم تعمل موقع من الصفر — فيه منصات جاهزة تعمل لك المتجر في يوم واحد:\n\n"
            "البداية السهلة (من غير موقع):\n"
            "• صفحة فيسبوك أو إنستجرام للمتجر — اعرض منتجاتك في بوستات، والطلب بالرسايل\n"
            "• واتساب بزنس — كتالوج منتجات جوه واتساب\n\n"
            "متجر كامل (لما تكبر شوية):\n"
            "• Shopify — أشهر منصة متاجر، باشتراك شهري\n"
            "• WooCommerce — إضافة مجانية على ووردبريس\n"
            "• سلة وزد — منصات عربية مشهورة\n\n"
            "أي متجر لازم يكون فيه:\n"
            "1️⃣ صور واضحة للمنتج من أكتر من زاوية\n"
            "2️⃣ سعر واضح — من غير \"السعر على الخاص\" (دي بتطفّش الزباين)\n"
            "3️⃣ وصف صادق: الخامة، المقاس، واللون\n"
            "4️⃣ طريقة طلب سهلة: زرار واتساب أو نموذج طلب\n\n"
            "واجب النهاردة: اعمل صفحة متجر على فيسبوك أو إنستجرام — وحط فيها أول منتج بالصورة والسعر والوصف."
        ),
        "en": (
            "🏪 Lesson 3: Build your store\n\n"
            "You do not need to build a website from scratch — there are ready platforms that make your store in one day:\n\n"
            "The easy start (without a website):\n"
            "• A Facebook or Instagram page for the store — show your products in posts, and take orders by messages\n"
            "• WhatsApp Business — a product catalog inside WhatsApp\n\n"
            "A full store (when you grow a little):\n"
            "• Shopify — the most famous store platform, with a monthly subscription\n"
            "• WooCommerce — a free addition to WordPress\n"
            "• Salla and Zid — famous Arab platforms\n\n"
            "Any store must have:\n"
            "1️⃣ Clear pictures of the product from more than one angle\n"
            "2️⃣ A clear price — without \"price in private messages\" (that drives customers away)\n"
            "3️⃣ An honest description: material, size, and color\n"
            "4️⃣ An easy way to order: a WhatsApp button or an order form\n\n"
            "Today's task: make a store page on Facebook or Instagram — and put your first product there with picture, price and description."
        ),
    },
    {
        "title_ar": "الدرس 4: الدفع والشحن",
        "title_en": "Lesson 4: Payment & shipping",
        "ar": (
            "💳 الدرس 4: الدفع والشحن\n\n"
            "الدفع والشحن هما أكتر حاجتين بيخوفوا الزبون — لو سهلتهم، المبيعات بتزيد.\n\n"
            "طرق الدفع:\n"
            "• الدفع عند الاستلام (Cash on Delivery) — الأسهل للزبون في البداية، وأكتر طريقة مطلوبة في مصر\n"
            "• محافظ إلكترونية: فودافون كاش، إنستا باي — الزبون يحوّل قبل الشحن\n"
            "• الدفع بالبطاقة أونلاين — لما متجرك يكبر (عن طريق بوابات دفع زي Paymob أو Fawry)\n\n"
            "الشحن:\n"
            "• شركات شحن: أرامكس، Bosta، J&T — بتاخد الطلب من عندك وتوصله للزبون\n"
            "• اتفق على سعر الشحن قبل ما تبيع — وحطه واضح في المتجر\n"
            "• الشحن المجاني للطلبات الكبيرة بيشجع الناس تشتري أكتر\n"
            "• تابع الشحنة لحد ما توصل — وبلّغ الزبون أول بأول\n\n"
            "⚠️ احذر: متبعتش طلب من غير ما تتأكد من عنوان الزبون ورقم تليفونه — واتصل بيه قبل الشحن.\n\n"
            "واجب النهاردة: اسأل شركة شحن واحدة عن أسعارها — واكتب سعر الشحن لـ 3 محافظات مختلفة."
        ),
        "en": (
            "💳 Lesson 4: Payment & shipping\n\n"
            "Payment and shipping are the two things that scare customers most — if you make them easy, sales grow.\n\n"
            "Payment methods:\n"
            "• Cash on Delivery — easiest for the customer at the start, and the most requested in Egypt\n"
            "• E-wallets: Vodafone Cash, InstaPay — the customer transfers before shipping\n"
            "• Online card payment — when your store grows (through payment gateways like Paymob or Fawry)\n\n"
            "Shipping:\n"
            "• Shipping companies: Aramex, Bosta, J&T — they take the order from you and deliver it to the customer\n"
            "• Agree on the shipping price before you sell — and put it clearly in the store\n"
            "• Free shipping for big orders encourages people to buy more\n"
            "• Track the shipment until it arrives — and tell the customer step by step\n\n"
            "⚠️ Beware: do not send an order without confirming the customer's address and phone number — and call them before shipping.\n\n"
            "Today's task: ask one shipping company about its prices — and write the shipping price for 3 different cities."
        ),
    },
    {
        "title_ar": "الدرس 5: تسويق المتجر",
        "title_en": "Lesson 5: Marketing your store",
        "ar": (
            "📣 الدرس 5: تسويق المتجر\n\n"
            "المتجر من غير تسويق زي محل في صحرا — محدش هيعرف عنه. استخدم اللي اتعلمناه في دورة التسويق:\n\n"
            "1️⃣ المحتوى: بوستات يومية للمنتج — صور حلوة، وفيديو قصير للمنتج وهو بيشتغل\n"
            "2️⃣ العروض: خصم أول طلب، أو \"اشتري 2 وخد التالت هدية\" — العرض بيحرّك الناس\n"
            "3️⃣ آراء العملاء: لما عميل يشتري ويعجبه، اطلب منه صورة أو رأي — وانشره (بإذنه)\n"
            "4️⃣ إعلانات صغيرة: إعلان فيسبوك بـ 100 جنيه على بوست منتج — جرّب وقيس النتيجة (دورة التسويق درس 4 و6)\n"
            "5️⃣ المجموعات: انشر في جروبات مهتمة بنفس المنتج — بس من غير إزعاج، وبقيمة حقيقية\n\n"
            "💡 أهم قاعدة: صورة المنتج هي البيع — صورة وحشة = مفيش بيع، حتى لو المنتج ممتاز.\n\n"
            "واجب النهاردة: اعمل 3 بوستات لمنتجك: بوست عرض سعر، وبوست فيديو قصير، وبوست سؤال للمتابعين."
        ),
        "en": (
            "📣 Lesson 5: Marketing your store\n\n"
            "A store without marketing is like a shop in a desert — nobody will know about it. Use what we learned in the marketing course:\n\n"
            "1️⃣ Content: daily posts for the product — nice pictures, and a short video of the product working\n"
            "2️⃣ Offers: a discount on the first order, or \"buy 2 get the third free\" — offers move people\n"
            "3️⃣ Customer opinions: when a customer buys and likes it, ask them for a picture or an opinion — and publish it (with their permission)\n"
            "4️⃣ Small ads: a Facebook ad for 100 EGP on a product post — try it and measure the result (marketing course lessons 4 and 6)\n"
            "5️⃣ Groups: post in groups interested in the same product — but without annoying anyone, and with real value\n\n"
            "💡 The most important rule: the product picture is the sale — a bad picture = no sale, even if the product is excellent.\n\n"
            "Today's task: make 3 posts for your product: a price-offer post, a short video post, and a question post for followers."
        ),
    },
    {
        "title_ar": "الدرس 6: خدمة العملاء",
        "title_en": "Lesson 6: Customer service",
        "ar": (
            "🤝 الدرس 6: خدمة العملاء\n\n"
            "العميل اللي بيتعامل كويس بيرجع يشتري تاني — وبيجيب أصحابه. والعميل اللي بيتعامل وحش بيحكي لـ 10 ناس.\n\n"
            "قواعد خدمة العملاء:\n"
            "1️⃣ رد بسرعة: العميل اللي بيستنى كتير بيروح لغيرك — حاول ترد في أقل من ساعة\n"
            "2️⃣ رد بأدب حتى لو العميل متعصب — \"أنا آسف على المشكلة، وهنحلها لك دلوقتي\"\n"
            "3️⃣ كن صادق: لو المنتج هيتأخر، قول للعميل قبل ما يسألك\n"
            "4️⃣ الشكوى فرصة: عميل اشتكى وحليت مشكلته بسرعة — بيبقى أوفى عميل عندك\n"
            "5️⃣ بعد البيع: ابعت رسالة بعد الاستلام: \"وصل لك الطلب؟ عجبك؟\" — الرسالة دي بتجيب تقييمات وطلبات تانية\n\n"
            "💡 جهّز ردود جاهزة للأسئلة اللي بتتكرر (السعر؟ الشحن؟ المقاسات؟) — زي ما اتعلمنا في دورة الذكاء الاصطناعي درس 9.\n\n"
            "واجب النهاردة: اكتب 5 ردود جاهزة لأكتر 5 أسئلة عملاءك بيسألوها."
        ),
        "en": (
            "🤝 Lesson 6: Customer service\n\n"
            "A customer treated well comes back to buy again — and brings their friends. A customer treated badly tells 10 people.\n\n"
            "Customer service rules:\n"
            "1️⃣ Answer fast: a customer who waits long goes to someone else — try to answer in less than an hour\n"
            "2️⃣ Answer politely even if the customer is angry — \"I am sorry about the problem, we will solve it for you now\"\n"
            "3️⃣ Be honest: if the product will be late, tell the customer before they ask\n"
            "4️⃣ A complaint is an opportunity: a customer who complained and you solved their problem fast — becomes your most loyal customer\n"
            "5️⃣ After the sale: send a message after delivery: \"Did the order arrive? Did you like it?\" — this message brings reviews and more orders\n\n"
            "💡 Prepare ready answers for repeated questions (price? shipping? sizes?) — like we learned in the AI course lesson 9.\n\n"
            "Today's task: write 5 ready answers for the 5 questions your customers ask most."
        ),
    },
    {
        "title_ar": "الدرس 7: مشروع متجر تجريبي كامل",
        "title_en": "Lesson 7: Full demo store project",
        "ar": (
            "🏆 الدرس 7: مشروع متجر تجريبي كامل\n\n"
            "وصلنا لآخر درس — دلوقتي هتعمل متجر تجريبي كامل، من غير ما تدفع جنيه:\n\n"
            "المشروع:\n"
            "1️⃣ المنتج: اختار منتج واحد (درس 2)\n"
            "2️⃣ الصفحة: اعمل صفحة متجر على فيسبوك أو إنستجرام (درس 3)\n"
            "3️⃣ الصور: صوّر المنتج 3 صور من زوايا مختلفة — إضاءة كويسة وخلفية نضيفة\n"
            "4️⃣ الوصف والسعر: اكتب وصف صادق وسعر واضح (درس 3)\n"
            "5️⃣ طريقة الطلب: زرار واتساب أو رسايل الصفحة (درس 4)\n"
            "6️⃣ التسويق: 3 بوستات في أول أسبوع (درس 5)\n"
            "7️⃣ الردود: جهّز 5 ردود جاهزة (درس 6)\n\n"
            "🎉 مبروك! خلصت دورة التجارة الإلكترونية — دلوقتي عندك متجر تجريبي جاهز، ولو جاب أول طلب حقيقي، كمّل وكبّر.\n\n"
            "واجب النهاردة: ابدأ الخطوة الأولى — اعمل صفحة المتجر وحط أول منتج."
        ),
        "en": (
            "🏆 Lesson 7: Full demo store project\n\n"
            "We reached the last lesson — now make one full demo store, without paying a pound:\n\n"
            "The project:\n"
            "1️⃣ Product: pick one product (lesson 2)\n"
            "2️⃣ Page: make a store page on Facebook or Instagram (lesson 3)\n"
            "3️⃣ Pictures: photograph the product in 3 pictures from different angles — good light and a clean background\n"
            "4️⃣ Description and price: write an honest description and a clear price (lesson 3)\n"
            "5️⃣ Ordering: a WhatsApp button or page messages (lesson 4)\n"
            "6️⃣ Marketing: 3 posts in the first week (lesson 5)\n"
            "7️⃣ Replies: prepare 5 ready answers (lesson 6)\n\n"
            "🎉 Congratulations! You finished the e-commerce course — now you have a ready demo store, and if it gets the first real order, continue and grow.\n\n"
            "Today's task: start the first step — make the store page and put the first product."
        ),
    },
]

# The full course: cybersecurity (14), then Python (22), then Ruby (7),
# then networks (21), then HTML/CSS (7), then SQL (7), then SQL Injection (21),
# then AI (14), freelancing (7), data analysis (7), digital marketing (7),
# then mobile apps (7), Linux (7), JavaScript (7), design & editing (7),
# then cloud (7) and e-commerce (7).
# Index 0..175. Track start offsets (used by the bot's track buttons).
CYBER_START = 0
PYTHON_START = len(CYBER_LESSONS)
RUBY_START = len(CYBER_LESSONS) + len(PYTHON_LESSONS)
NETWORKS_START = len(CYBER_LESSONS) + len(PYTHON_LESSONS) + len(RUBY_LESSONS)
HTML_CSS_START = NETWORKS_START + len(NETWORKS_LESSONS)
SQL_START = HTML_CSS_START + len(HTML_CSS_LESSONS)
SQLI_START = SQL_START + len(SQL_LESSONS)
AI_START = SQLI_START + len(SQLI_LESSONS)
FREELANCE_START = AI_START + len(AI_LESSONS)
DATA_START = FREELANCE_START + len(FREELANCE_LESSONS)
MARKETING_START = DATA_START + len(DATA_LESSONS)
MOBILE_START = MARKETING_START + len(MARKETING_LESSONS)
LINUX_START = MOBILE_START + len(MOBILE_LESSONS)
JS_START = LINUX_START + len(LINUX_LESSONS)
DESIGN_START = JS_START + len(JS_LESSONS)
CLOUD_START = DESIGN_START + len(DESIGN_LESSONS)
ECOMMERCE_START = CLOUD_START + len(CLOUD_LESSONS)

ALL_LESSONS = [
    {"track_ar": "الأمن السيبراني", "track_en": "Cybersecurity", **lesson}
    for lesson in CYBER_LESSONS
] + [
    {"track_ar": "البرمجة — بايثون", "track_en": "Programming — Python", **lesson}
    for lesson in PYTHON_LESSONS
] + [
    {"track_ar": "البرمجة — روبي", "track_en": "Programming — Ruby", **lesson}
    for lesson in RUBY_LESSONS
] + [
    {"track_ar": "الشبكات", "track_en": "Networks", **lesson}
    for lesson in NETWORKS_LESSONS
] + [
    {"track_ar": "تصميم الويب — HTML/CSS", "track_en": "Web Design — HTML/CSS", **lesson}
    for lesson in HTML_CSS_LESSONS
] + [
    {"track_ar": "قواعد البيانات — SQL", "track_en": "Databases — SQL", **lesson}
    for lesson in SQL_LESSONS
] + [
    {"track_ar": "حماية من SQL Injection", "track_en": "SQL Injection Protection", **lesson}
    for lesson in SQLI_LESSONS
] + [
    {"track_ar": "الذكاء الاصطناعي", "track_en": "Artificial Intelligence", **lesson}
    for lesson in AI_LESSONS
] + [
    {"track_ar": "العمل الحر والربح من الإنترنت", "track_en": "Freelancing & Earning Online", **lesson}
    for lesson in FREELANCE_LESSONS
] + [
    {"track_ar": "تحليل البيانات", "track_en": "Data Analysis", **lesson}
    for lesson in DATA_LESSONS
] + [
    {"track_ar": "التسويق الرقمي", "track_en": "Digital Marketing", **lesson}
    for lesson in MARKETING_LESSONS
] + [
    {"track_ar": "تطبيقات الموبايل", "track_en": "Mobile Apps", **lesson}
    for lesson in MOBILE_LESSONS
] + [
    {"track_ar": "لينكس", "track_en": "Linux", **lesson}
    for lesson in LINUX_LESSONS
] + [
    {"track_ar": "جافاسكريبت", "track_en": "JavaScript", **lesson}
    for lesson in JS_LESSONS
] + [
    {"track_ar": "التصميم والمونتاج", "track_en": "Design & Video Editing", **lesson}
    for lesson in DESIGN_LESSONS
] + [
    {"track_ar": "السحابة", "track_en": "Cloud", **lesson}
    for lesson in CLOUD_LESSONS
] + [
    {"track_ar": "التجارة الإلكترونية", "track_en": "E-commerce", **lesson}
    for lesson in ECOMMERCE_LESSONS
]


def lesson_text(index, lang="ar"):
    """Return (header, body) for lesson index in the requested language."""
    lesson = ALL_LESSONS[index % len(ALL_LESSONS)]
    if lang == "en":
        track = lesson["track_en"]
        title = lesson["title_en"]
        body = lesson["en"]
    else:
        track = lesson["track_ar"]
        title = lesson["title_ar"]
        body = lesson["ar"]
    return track, title, body


def courses_text(lang="ar"):
    """Compact listing: one line per track (name + lesson count).

    Must stay under Telegram's 4096-char message limit in both languages.
    """
    tracks = [
        ("🛡️", "الأمن السيبراني", "Cybersecurity", CYBER_LESSONS),
        ("🐍", "البرمجة: بايثون", "Programming: Python", PYTHON_LESSONS),
        ("💎", "البرمجة: روبي", "Programming: Ruby", RUBY_LESSONS),
        ("🌐", "الشبكات", "Networks", NETWORKS_LESSONS),
        ("🎨", "تصميم الويب: HTML/CSS", "Web Design: HTML/CSS", HTML_CSS_LESSONS),
        ("🗄️", "قواعد البيانات: SQL", "Databases: SQL", SQL_LESSONS),
        ("💉", "حماية من SQL Injection", "SQL Injection Protection", SQLI_LESSONS),
        ("🤖", "الذكاء الاصطناعي", "Artificial Intelligence", AI_LESSONS),
        ("💰", "العمل الحر والربح من الإنترنت", "Freelancing & Earning Online", FREELANCE_LESSONS),
        ("📊", "تحليل البيانات", "Data Analysis", DATA_LESSONS),
        ("📣", "التسويق الرقمي", "Digital Marketing", MARKETING_LESSONS),
        ("📱", "تطبيقات الموبايل", "Mobile Apps", MOBILE_LESSONS),
        ("🐧", "لينكس", "Linux", LINUX_LESSONS),
        ("🟨", "جافاسكريبت", "JavaScript", JS_LESSONS),
        ("🎬", "التصميم والمونتاج", "Design & Video Editing", DESIGN_LESSONS),
        ("☁️", "السحابة", "Cloud", CLOUD_LESSONS),
        ("🛒", "التجارة الإلكترونية", "E-commerce", ECOMMERCE_LESSONS),
    ]
    if lang == "en":
        lines = [f"📚 Our courses (free for now) — {len(ALL_LESSONS)} lessons:\n"]
        for i, (emoji, _ar, en, lessons) in enumerate(tracks, 1):
            lines.append(f"{emoji} Track {i} — {en} ({len(lessons)} lessons)")
        lines.append("\n⭐ Special course: /subscribe")
        lines.append("Send /lesson to get your next lesson. Send /start to begin.")
        return "\n".join(lines)
    lines = [f"📚 الدورات بتاعتنا (مجانية دلوقتي) — {len(ALL_LESSONS)} درس:\n"]
    for i, (emoji, ar, _en, lessons) in enumerate(tracks, 1):
        lines.append(f"{emoji} المسار {i} — {ar} ({len(lessons)} درس)")
    lines.append("\n⭐ الدورة الخاصة: /subscribe")
    lines.append("اكتب /lesson عشان تاخد الدرس اللي بعده. واكتب /start عشان تبدأ من الأول.")
    return "\n".join(lines)
