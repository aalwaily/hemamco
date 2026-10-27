# Bilingual content for the HEMAMCO site. Every text is an (english, arabic) pair.

MONTHS_AR = {"Jan": "يناير", "Feb": "فبراير", "Mar": "مارس", "Apr": "أبريل", "May": "مايو", "Jun": "يونيو",
             "Jul": "يوليو", "Aug": "أغسطس", "Sep": "سبتمبر", "Oct": "أكتوبر", "Nov": "نوفمبر", "Dec": "ديسمبر",
             "January": "يناير", "February": "فبراير", "March": "مارس", "April": "أبريل", "August": "أغسطس"}

SERVICES = [
    ("civil", ("Civil &amp; Earth Works", "الأعمال المدنية والترابية"), "svc-civil.jpg", "excavator",
     ("Site development, roads, asphalting, earthworks, drainage and substation buildings — delivered to Saudi Aramco and Royal Commission standards.",
      "تطوير المواقع والطرق والسفلتة والأعمال الترابية وشبكات التصريف ومباني المحطات الفرعية، وفق معايير أرامكو السعودية والهيئة الملكية.")),
    ("piping", ("Mechanical &amp; Piping", "الأعمال الميكانيكية والأنابيب"), "svc-piping.jpg", "pipe",
     ("Complete construction from engineering and procurement to fabrication, field erection and commissioning for oil &amp; gas, mining and water.",
      "تنفيذ متكامل من الهندسة والتوريد إلى التصنيع والتركيب الميداني والتشغيل لقطاعات النفط والغاز والتعدين والمياه.")),
    ("fabrication", ("Fabrication Works", "أعمال التصنيع"), "svc-fabrication.jpg", "wrench",
     ("A 10,000 m² covered workshop in our Dammam lay-down yard for pipe spooling, skids, modules, tanks, vessels and heavy structural steel.",
      "ورشة مغطاة بمساحة 10,000 م² في ساحتنا بالدمام لتصنيع وصلات الأنابيب والوحدات المحمولة والخزانات والأوعية والهياكل الفولاذية الثقيلة.")),
    ("steel", ("Steel Erection", "تركيب الهياكل الفولاذية"), "svc-steel.jpg", "beam",
     ("Heavy-duty structures, metal buildings, pipe racks and platforms — the skeletal core of industrial, commercial and retail facilities.",
      "الهياكل الثقيلة والمباني المعدنية وحوامل الأنابيب والمنصات، وهي العمود الفقري للمنشآت الصناعية والتجارية.")),
    ("electrical", ("Electrical &amp; Instrumentation", "الأعمال الكهربائية والأجهزة الدقيقة"), "svc-electrical.jpg", "bolt",
     ("Overhead and underground power lines, fibre optics, substation switchgear, building wiring, street lighting and instrument installation.",
      "خطوط الكهرباء الهوائية والأرضية، والألياف الضوئية، ولوحات المحطات الفرعية، وتمديدات المباني، وإنارة الشوارع، وتركيب الأجهزة الدقيقة.")),
    ("fireproofing", ("Fireproofing &amp; Painting", "الحماية من الحريق والدهانات"), "svc-painting.jpg", "flame",
     ("Sandblasting, protective coatings and painting plus fabrication and installation of fireproofing materials and sprinkler control systems.",
      "السفع الرملي والطلاءات الواقية والدهانات، إلى جانب تصنيع وتركيب مواد الحماية من الحريق وأنظمة التحكم بالرشاشات.")),
]

CLIENTS = [(("Saudi Aramco", "أرامكو السعودية"), ("Oil &amp; Gas", "النفط والغاز")),
           (("SABIC", "سابك"), ("Petrochemicals", "البتروكيماويات")),
           (("Ma’aden", "معادن"), ("Mining", "التعدين")),
           (("MARAFIQ", "مرافق"), ("Utilities", "المرافق")),
           (("YASREF", "ياسرف"), ("Refining", "التكرير")),
           (("SEC", "السعودية للكهرباء"), ("Electricity", "الكهرباء"))]

ARAMCO = ("Saudi Aramco", "أرامكو السعودية")
ONGOING = [
    ("project-big-img1.jpg", ("Manual Excavation and Backfilling Works for Underground 8\" Dia. Waterlines",
                              "أعمال الحفر اليدوي والردم لخطوط المياه الأرضية بقطر 8 بوصات"),
     ARAMCO, "August 2022", ("Civil &amp; Earthworks", "أعمال مدنية وترابية")),
    ("project-big-img2.jpg", ("Preparation and Construction of Right of Way (ROW) — Hawiyah &amp; Harad 30\" Pipeline Project",
                              "تجهيز وإنشاء حرم الطريق لمشروع خط أنابيب الحوية وحرض بقطر 30 بوصة"),
     ARAMCO, "May 2022", ("Pipeline / ROW", "خطوط الأنابيب / حرم الطريق")),
    ("project-big-img3.jpg", ("Mechanical Structural Works &amp; Steel Erection", "الأعمال الإنشائية الميكانيكية وتركيب الهياكل الفولاذية"),
     ARAMCO, "February 2022", ("Mechanical &amp; Steel", "ميكانيكا وهياكل فولاذية")),
    ("project-big-img4.jpg", ("Earthworks and Construction of Chain-Link Fence and Gates — TINAT GM",
                              "أعمال ترابية وإنشاء سياج شبكي وبوابات — TINAT GM"),
     ARAMCO, "April 2022", ("Civil &amp; Fencing", "أعمال مدنية وأسوار")),
]

EP = ("Eastern Province", "المنطقة الشرقية")
RIVIERA = ("Riviera Compound 1, Al-Khobar", "مجمع ريفييرا 1، الخبر")
GALLERY = [
    (1, ("Manual Excavation Works", "أعمال الحفر اليدوي"), ("Ras Tanura", "رأس تنورة"), "civil"),
    (2, ("Mechanical &amp; Piping Works", "الأعمال الميكانيكية والأنابيب"), EP, "mechanical"),
    (3, ("Steel Erection Works", "تركيب الهياكل الفولاذية"), ("Ras Tanura", "رأس تنورة"), "steel"),
    (4, ("Structural Works", "الأعمال الإنشائية"), ("Ras Al-Khair", "رأس الخير"), "steel"),
    (5, ("Mechanical Works", "الأعمال الميكانيكية"), RIVIERA, "mechanical"),
    (6, ("Excavation, Structural &amp; Finishing Works", "أعمال الحفر والإنشاء والتشطيب"), RIVIERA, "civil"),
    (11, ("Road Works", "أعمال الطرق"), ("Ras Al-Khair", "رأس الخير"), "civil"),
    (12, ("Telecom &amp; Power Supply Tower Installation", "تركيب أبراج الاتصالات والكهرباء"), EP, "electrical"),
    (13, ("Civil &amp; Mechanical Works", "الأعمال المدنية والميكانيكية"), EP, "civil mechanical"),
    (14, ("Civil &amp; Mechanical Works", "الأعمال المدنية والميكانيكية"), EP, "civil mechanical"),
    (15, ("Civil &amp; Electrical Works", "الأعمال المدنية والكهربائية"), EP, "civil electrical"),
    (16, ("Civil &amp; Electrical Works", "الأعمال المدنية والكهربائية"), EP, "civil electrical"),
]

FIN = ("Finishing Works", "أعمال التشطيب")
MEP = ("MEP &amp; Finishing Works", "الأعمال الكهروميكانيكية والتشطيب")
FILL = ("Supply of Select Fill Materials", "توريد مواد الردم المختارة")
INTERLOCK = ("Supply &amp; Installation of Interlock and Curb Stone", "توريد وتركيب البلاط المتداخل وحجر الأرصفة")
HAMOUD = ("Hamoud AlSamah AlSharary Cont. Est.", "مؤسسة حمود السماح الشراري للمقاولات")
RC = ("Royal Commission", "الهيئة الملكية")
SDHOP = ("Saudi Aramco SDHOP", "أرامكو السعودية SDHOP")
SEC = ("SEC", "السعودية للكهرباء")
KAAB = ("King Abdulaziz Air Base, Dhahran", "قاعدة الملك عبدالعزيز الجوية، الظهران")
SBUILD = ("Saudi Build Cont. Co.", "الشركة السعودية للبناء والمقاولات")
COMPLETED = [
    (("Dareen Shopping Mall, Dammam", "مجمع دارين التجاري، الدمام"), FIN, ("Dareen Mall", "دارين مول"), 1875000.00, "Oct 2021"),
    (("Arja Al-Khaleej Contracting Est.", "مؤسسة أرجاء الخليج للمقاولات"), ("Foundation of Skid for Chemical Farm", "أساسات وحدة محمولة لمزرعة كيميائية"), ARAMCO, 480000.00, "Sep 2021"),
    (("Al Qemma Al-Ahlia Schools — Ras Tanura", "مدارس القمة الأهلية — رأس تنورة"), FIN, ("Al Qemma Al-Ahlia", "القمة الأهلية"), 2480780.00, "Mar 2021"),
    (("Residential Building (Al Rabee), Al-Khobar Al-Aziziya", "مبنى سكني (الربيع)، الخبر – العزيزية"), ("Plumbing, Electrical &amp; Finishing Works", "أعمال السباكة والكهرباء والتشطيب"), ("Al-Rabee", "الربيع"), 2788587.00, "Nov 2020"),
    (("Zamil Travel Office Building, Al-Khobar", "مبنى مكاتب الزامل للسفر، الخبر"), FIN, ("Zamil Travel &amp; Tourism", "الزامل للسفر والسياحة"), 596450.00, "Aug 2020"),
    (("Nazieh Khalifa Group", "مجموعة نزيه خليفة"), FIN, ("Nazieh Khalifa Group", "مجموعة نزيه خليفة"), 768000.00, "Jul 2020"),
    (("Al Dossary Village Residential, Half Moon Aziziya", "قرية الدوسري السكنية، نصف القمر – العزيزية"), MEP, ("Al Dossary", "الدوسري"), 2889370.00, "May 2020"),
    (("Large Private Villas, Al-Khobar &amp; Dhahran", "فلل خاصة كبيرة، الخبر والظهران"), ("Construction &amp; Finishing Works", "أعمال الإنشاء والتشطيب"), ("Private Owners", "ملاك من القطاع الخاص"), 16845000.00, "Nov 2019"),
    (("Building No. 56 King Faisal University Office Building, Dammam", "المبنى رقم 56 مبنى مكاتب جامعة الملك فيصل، الدمام"), FIN, ("King Faisal University", "جامعة الملك فيصل"), 1235000.00, "Sep 2019"),
    (("The Royal Hall, Half Moon Aziziya", "القاعة الملكية، نصف القمر – العزيزية"), FIN, ("King Fahad Military City", "مدينة الملك فهد العسكرية"), 1110000.00, "Dec 2018"),
    (("Al Faisal Steel Training Center, Second Industrial", "مركز تدريب الفيصل للحديد، الصناعية الثانية"), FIN, ("Al-Faisal Steel", "الفيصل للحديد"), 1655000.00, "Oct 2018"),
    (("Eva International Contracting Est.", "مؤسسة إيفا الدولية للمقاولات"), ("Site Preparation", "تجهيز الموقع"), RC, 1865000.00, "Aug 2018"),
    (("Ahmed Emara Cont. Est.", "مؤسسة أحمد عمارة للمقاولات"), INTERLOCK, RC, 887000.00, "Nov 2017"),
    (("Al Jaber Cont. Ltd.", "شركة الجابر للمقاولات المحدودة"), MEP, ("Ministry of Housing, Abqaiq", "وزارة الإسكان، بقيق"), 878000.00, "Sep 2017"),
    (("Azmeel", "أزميل"), FILL, SDHOP, 898000.00, "Jul 2017"),
    (("Shade Corporation Ltd.", "شركة شيد المحدودة"), FILL, SDHOP, 1438765.00, "May 2017"),
    (("Al Yamama", "اليمامة"), MEP, SDHOP, 875458.00, "Nov 2016"),
    (("Saudi Gulf Hydraulic Co.", "الشركة السعودية الخليجية للهيدروليك"), ("Civil &amp; Electrical Works", "الأعمال المدنية والكهربائية"), ("Saudi Gulf Hydraulics Co.", "الشركة السعودية الخليجية للهيدروليك"), 1670000.00, "Jul 2016"),
    (("Ayed Al Anzi Est.", "مؤسسة عايد العنزي"), INTERLOCK, ("Royal Commission Jubail", "الهيئة الملكية بالجبيل"), 437000.00, "Jun 2016"),
    (("Rashid Al Hammadi Group", "مجموعة راشد الحمادي"), ("Civil, Structural &amp; Electro-Mechanical Works", "الأعمال المدنية والإنشائية والكهروميكانيكية"), ("Al-Khobar Gardens, Jenan Group", "حدائق الخبر، مجموعة جنان"), 3010000.00, "Apr 2016"),
    (("Dimensional Diamond", "دايمنشنال دايموند"), ("Road Works", "أعمال الطرق"), RC, 5500000.00, "Jan 2016"),
    (("Shapoorji Pallonji Contracting", "شابورجي بالونجي للمقاولات"), MEP, ("AbdulKarim Building, Al-Khobar", "مبنى عبدالكريم، الخبر"), 2967000.00, "Oct 2015"),
    (("TESLA Energy Solutions", "تسلا لحلول الطاقة"), ("Maintenance Work &amp; Al Qurayyah Power Plant", "أعمال الصيانة ومحطة كهرباء القريّة"), ("SISCO", "سيسكو"), 1700000.00, "Aug 2015"),
    (KAAB, ("4 Building Soil Stabilization", "تثبيت تربة 4 مبانٍ"), KAAB, 2587000.00, "Dec 2014"),
    (HAMOUD, ("Multi-Purpose Gym", "صالة رياضية متعددة الأغراض"), ("SABGSD", "SABGSD"), 798000.00, "Aug 2014"),
    (("AICCO", "AICCO"), ("Civil Structure Project", "مشروع هيكل مدني"), ("Jubail AICCO", "AICCO الجبيل"), 2450000.00, "Jan 2013"),
    (HAMOUD, ("Fire Fighting &amp; Fire Alarm System, Aliyah Schools, Doha Dhahran", "نظام مكافحة وإنذار الحريق، مدارس العلية، الدوحة – الظهران"), ("2-SABGSD", "2-SABGSD"), 2824000.00, "Mar 2013"),
    (("KENTZ", "كنتز"), ("Civil &amp; Structural Works for Jubail Port Expansion-2", "الأعمال المدنية والإنشائية لتوسعة ميناء الجبيل 2"), ("SABTANK", "سابتانك"), 1866694.00, "Jul 2012"),
    (HAMOUD, ("40-Car Parking Shades", "مظلات مواقف 40 سيارة"), KAAB, 385000.00, "Oct 2012"),
    (HAMOUD, ("11-PACU Replacement, Aaliyah Boys and Girls Schools", "استبدال 11 وحدة تكييف (PACU)، مدارس العلية للبنين والبنات"), ("SABGSD", "SABGSD"), 6388000.00, "Jun 2011"),
    (("Saudi Build Cont. Co. — Sub-Station", "الشركة السعودية للبناء والمقاولات — محطة فرعية"), ("Waterproofing Uyun, Al Hassa", "أعمال العزل المائي، العيون، الأحساء"), SEC, 1583000.00, "Apr 2011"),
    (("Najran Co.", "شركة نجران"), ("IC5 — Recovery of Isopentane from NG (PK Ref No. 0720068)", "IC5 — استخلاص الأيزوبنتان من الغاز الطبيعي (المرجع 0720068)"), ("S.A. Kentz", "إس.إيه. كنتز"), 1271006.48, "Jan – Oct 2010"),
    (HAMOUD, ("Roof and Wet Areas Waterproofing", "عزل الأسطح والمناطق الرطبة"), ("Al Hugayet Tower, Al-Khobar", "برج الحقيط، الخبر"), 1893000.00, "Dec 2009"),
    (("Al Zamil Cont. Est.", "مؤسسة الزامل للمقاولات"), ("Roof Waterproofing", "عزل الأسطح"), ("5-SABGSD", "5-SABGSD"), 3883000.00, "Feb 2009"),
    (SBUILD, ("Sub-Station Waterproofing, Takasushi Dammam", "عزل محطة فرعية، تاكاسوشي الدمام"), SEC, 1372000.00, "Sep 2008"),
    (("OLAYAN / Najran Co.", "العليان / شركة نجران"), ("Fabrication of Structural Steel PC-3", "تصنيع الهياكل الفولاذية PC-3"), ("Petro Rabigh", "بترو رابغ"), 2607306.00, "Sep 2007 – Dec 2008"),
    (("Myung Hyun Cont. Co.", "شركة ميونغ هيون للمقاولات"), ("Sub-Station Civil Works, Uthmaniyah", "الأعمال المدنية لمحطة فرعية، العثمانية"), SEC, 5682000.00, "Oct 2008"),
    (("AKAKE Contracting Est.", "مؤسسة أكاكي للمقاولات"), ("Concrete Repair", "إصلاح الخرسانة"), ("48 Apt. Al Eskan, Al-Khobar", "48 شقة، الإسكان، الخبر"), 4388000.00, "Jul 2007"),
    (("HHI / Najran Company", "هيونداي للصناعات الثقيلة / شركة نجران"), ("Foundation &amp; Structural", "الأساسات والهياكل"), ("Shaybah Gas Plant", "معمل غاز الشيبة"), 1507306.00, "Nov 2006 – Jul 2008"),
    (("Tala Contracting Co.", "شركة تالا للمقاولات"), ("Hardscaping", "أعمال التنسيق الصلب"), ("Ministry of Housing", "وزارة الإسكان"), 874000.00, "Aug 2006"),
]

MANPOWER = [
    (("Management &amp; Administration", "الإدارة والشؤون الإدارية"), [
        (("General Manager", "مدير عام"), 1), (("Admin Manager", "مدير إداري"), 1), (("Finance Manager", "مدير مالي"), 1),
        (("Accounting Team", "فريق المحاسبة"), 3), (("HR Manager", "مدير الموارد البشرية"), 1), (("HR Team", "فريق الموارد البشرية"), 5),
        (("Company Management", "إدارة الشركة"), 10), (("Secretary", "سكرتير"), 6), (("Documents Controller", "مراقب وثائق"), 5),
        (("IT", "تقنية المعلومات"), 3), (("Data Entry Operator", "مدخل بيانات"), 6), (("Time-keeper", "مراقب دوام"), 10)]),
    (("Engineering &amp; Project Control", "الهندسة وضبط المشاريع"), [
        (("Operation Manager", "مدير العمليات"), 1), (("Project Manager", "مدير مشروع"), 5), (("Site Superintendent", "مشرف موقع"), 10),
        (("Project Engineer", "مهندس مشروع"), 15), (("Planner / Scheduler", "مخطط / مجدول"), 3), (("Quantity Surveyor", "مساح كميات"), 5),
        (("Land Surveyor", "مساح أراضٍ"), 4), (("AutoCAD Operator", "مشغل أوتوكاد"), 2)]),
    (("Quality, Health, Safety &amp; Environment", "الجودة والصحة والسلامة والبيئة"), [
        (("QA/QC Manager", "مدير ضمان وضبط الجودة"), 3), (("HSE Manager", "مدير الصحة والسلامة والبيئة"), 1),
        (("QC Inspector", "مفتش جودة"), 6), (("Safety Officer", "مسؤول سلامة"), 20)]),
    (("Site Workforce &amp; Trades", "العمالة الميدانية والحرف"), [
        (("Foreman", "رئيس عمال"), 24), (("Heavy Equipment Operator", "مشغل معدات ثقيلة"), 30), (("Driver (Heavy &amp; Light)", "سائق (ثقيل وخفيف)"), 50),
        (("Heavy Equipment Mechanic", "ميكانيكي معدات ثقيلة"), 5), (("Mechanic Helper", "مساعد ميكانيكي"), 50),
        (("Multi-Skilled Worker", "عامل متعدد المهارات"), 125), (("Skilled Labour", "عمالة ماهرة"), 250), (("Helper", "مساعد"), 178),
        (("Cleaner", "عامل نظافة"), 20), (("Steel Erector", "مركّب هياكل فولاذية"), 80), (("Carpenter", "نجار"), 30),
        (("Steel Fixer", "حداد تسليح"), 33), (("Fitter", "فني تركيب"), 31), (("Mason", "بنّاء"), 50), (("Technician (misc.)", "فني (متنوع)"), 30)]),
]

NA = ("—", "—")
EQUIPMENT = [
    (("Trailer Dump Trucks", "شاحنات قلابة بمقطورة"), ("32 m³", "32 م³"), 14),
    (("Bulldozer", "جرافة (بلدوزر)"), ("D15 / D9", "D15 / D9"), 4),
    (("Wheel Loaders", "لوادر بعجلات"), ("950 / 966 / 980", "950 / 966 / 980"), 8),
    (("Motor Grader", "ممهدة (جريدر)"), ("14G", "14G"), 3),
    (("Water Trucks", "صهاريج مياه"), ("20,000 L", "20,000 لتر"), 8),
    (("Roller Compactors", "هراسات"), ("8 – 10 tons", "8 – 10 طن"), 8),
    (("Fuel Tankers", "صهاريج وقود"), ("15,000 L", "15,000 لتر"), 3),
    (("Boom Trucks", "شاحنات برافعة"), ("5 – 10 tons", "5 – 10 طن"), 2),
    (("Flat Bed Trailer", "مقطورة مسطحة"), ("40 tons", "40 طن"), 3),
    (("Low Bed Trailers", "مقطورات منخفضة (لوبد)"), NA, 3),
    (("Excavator / Rock Breakers", "حفارات / كسارات صخور"), NA, 5),
    (("JCB Front End Loader", "لودر أمامي JCB"), NA, 4),
    (("Plate Compactors", "دكاكات صفيحية"), NA, 10),
    (("Hand Roller Compactors", "هراسات يدوية"), ("1 ton", "1 طن"), 3),
    (("Service Pick-up", "سيارات خدمة (بيك أب)"), ("2 / 4 tons", "2 / 4 طن"), 22),
    (("Dyna Trucks", "شاحنات دينا"), NA, 6),
    (("Buses", "حافلات"), ("50 seats", "50 مقعدًا"), 10),
    (("Mini Coaster", "حافلات صغيرة (كوستر)"), ("16 seats", "16 مقعدًا"), 5),
    (("Mobile Crane", "رافعة متحركة"), ("50 tons", "50 طن"), 1),
    (("Mobile Crane", "رافعة متحركة"), ("30 tons", "30 طن"), 1),
    (("Power Generators", "مولدات كهرباء"), ("32 / 50 / 300 kVA", "32 / 50 / 300 ك.ف.أ"), 8),
    (("Tower Lights", "أبراج إنارة"), NA, 12),
    (("Site Portable Offices (various sizes)", "مكاتب موقع متنقلة (مقاسات مختلفة)"), NA, 30),
    (("Dewatering Pump and Pipe Headers", "مضخات نزح المياه ومجمّعات الأنابيب"), ("160 LM", "160 م.ط"), 5),
]

TOTAL_STAFF = sum(q for _, rows in MANPOWER for _, q in rows)
TOTAL_EQUIP = sum(q for _, _, q in EQUIPMENT)
TOTAL_VALUE = sum(r[3] for r in COMPLETED)
