#!/usr/bin/env python3
"""Generates the bilingual HEMAMCO site: English at the root, Arabic (RTL) in /ar/.

Usage (from the repository root):  python3 tools/build_site.py public_html
"""
import html, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "icons.py")).read())
exec(open(os.path.join(HERE, "data_bi.py")).read())

ROOT = sys.argv[1]
YEARS = 20  # since 2006
LANG = "en"
P = ""  # path prefix to the site root ("" for English, "../" for Arabic)

def T(en, ar):
    return ar if LANG == "ar" else en

def L(pair):
    return pair[1] if LANG == "ar" else pair[0]

def date(s):
    if LANG != "ar":
        return s
    return re.sub(r"[A-Z][a-z]+", lambda m: MONTHS_AR.get(m.group(0), m.group(0)), s)

def E(text):
    return html.escape(text, quote=True)

def lines(pair):
    return "<br>".join(E(part) for part in L(pair).split("\n"))

def pct_text(p):
    if p is None:
        return T("Not stated", "غير مذكورة")
    if float(p) == int(p):
        return f"{int(p)}%"
    return f"{p:.1f}".rstrip("0").rstrip(".") + "%"

def arrow():
    return ic("arrow").replace("<svg", '<svg class="arr"', 1)

def IMG(name):
    return f"{P}assets/images/site/{name}"

def PIMG(name):
    return f"{P}assets/images/{name}"

PHONE = '<span dir="ltr">+966 13 817 4333</span>'

# ---------------- navigation ----------------
def NAV():
    return [
        (T("Home", "الرئيسية"), "index.html", []),
        (T("About", "من نحن"), "about.html", [(T("Company Overview", "نبذة عن الشركة"), "about.html"),
                                             (T("Safety Policy", "سياسة السلامة"), "safety.html"),
                                             (T("Quality Control Policy", "سياسة ضبط الجودة"), "quality.html"),
                                             (T("Organization Chart", "الهيكل التنظيمي"), "org.html")]),
        (T("Services", "خدماتنا"), "service.html", []),
        (T("Projects", "المشاريع"), "project.html", [(T("Projects Overview", "نظرة عامة"), "project.html"),
                                                     (T("Ongoing Projects", "المشاريع الجارية"), "ongoing.html"),
                                                     (T("Completed Projects", "المشاريع المنجزة"), "completed.html"),
                                                     (T("Project Gallery", "معرض المشاريع"), "gallery.html")]),
        (T("Resources", "الموارد"), "manpower.html", [(T("Manpower", "القوى العاملة"), "manpower.html"),
                                                      (T("Equipment", "المعدات"), "equipment.html")]),
        (T("Contact", "اتصل بنا"), "contact.html", []),
    ]

def nav_html(current):
    out = []
    for label, href, kids in NAV():
        active = "active" if current == href or current in [h for _, h in kids] else ""
        if kids:
            sub = "".join(f'<li><a href="{h}"{" class=active" if h == current else ""}>{l}</a></li>' for l, h in kids)
            out.append(f'<li class="has-dd"><a href="{href}" class="{active}" aria-haspopup="true">{label} {ic("caret").replace("<svg", "<svg class=caret", 1)}</a><ul class="dropdown">{sub}</ul></li>')
        else:
            out.append(f'<li><a href="{href}" class="{active}">{label}</a></li>')
    return "".join(out)

def lang_switch(current):
    if LANG == "ar":
        return f'<a class="lang-switch" href="../{current}" hreflang="en" lang="en">{ic("globe")}<span>English</span></a>'
    return f'<a class="lang-switch" href="ar/{current}" hreflang="ar" lang="ar">{ic("globe")}<span>العربية</span></a>'

def head(title, desc, current):
    en_url, ar_url = ("../" if LANG == "ar" else "") + current, ("" if LANG == "ar" else "ar/") + current
    font = ("family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800"
            if LANG == "ar" else "family=IBM+Plex+Sans+Arabic:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800")
    return f'''<!DOCTYPE html>
<html lang="{LANG}" dir="{"rtl" if LANG == "ar" else "ltr"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#172074">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{IMG("hero-riyadh.jpg")}">
<meta property="og:locale" content="{"ar_SA" if LANG == "ar" else "en_US"}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="icon" type="image/png" sizes="32x32" href="{IMG("favicon-32.png")}">
<link rel="icon" type="image/png" sizes="48x48" href="{IMG("favicon-48.png")}">
<link rel="icon" type="image/png" sizes="192x192" href="{IMG("favicon-192.png")}">
<link rel="apple-touch-icon" sizes="180x180" href="{IMG("apple-touch-icon.png")}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{font}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/css/site.css">
</head>
<body>
'''

def header(current):
    other_name = T('<span class="ar" lang="ar">شركة هممكو المحدودة</span>', '<span lang="en">Hemamco Company Limited</span>')
    return f'''<div class="topbar">
  <div class="container">
    <div class="group">
      <a href="tel:+966138174333">{ic("phone")} {PHONE}</a>
      <a href="mailto:info@hemamco.com" class="hide-sm">{ic("mail")} info@hemamco.com</a>
      <span class="tb-item hide-sm">{ic("pin")} {T("Dammam, Kingdom of Saudi Arabia", "الدمام، المملكة العربية السعودية")}</span>
    </div>
    <div class="group hide-sm">{other_name}</div>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="{T("Hemamco Company Limited — Home", "شركة هممكو المحدودة — الرئيسية")}">
      <picture><source srcset="{IMG("logo.webp")}" type="image/webp"><img src="{IMG("logo.png")}" alt="{T("Hemamco Company Limited", "شركة هممكو المحدودة")}" width="125" height="58"></picture>
    </a>
    <nav class="nav-wrap" aria-label="{T("Main", "القائمة الرئيسية")}">
      <ul class="nav">{nav_html(current)}</ul>
      <div class="mobile-cta"><a href="contact.html" class="btn btn-primary" style="width:100%">{T("Request a Quote", "اطلب عرض سعر")} {arrow()}</a></div>
    </nav>
    <div class="header-cta">
      {lang_switch(current)}
      <a href="contact.html" class="btn btn-primary">{T("Request a Quote", "اطلب عرض سعر")} {arrow()}</a>
      <button class="menu-toggle" aria-label="{T("Open menu", "فتح القائمة")}" aria-expanded="false">{ic("menu")}</button>
    </div>
  </div>
</header>
<main>
'''

def cta():
    return f'''<section class="section-sm">
  <div class="container">
    <div class="cta reveal">
      <img class="bg" src="{IMG("kingdom-centre.jpg")}" alt="" loading="lazy">
      <div class="inner">
        <div>
          <span class="eyebrow">{T("Let’s build together", "لنبنِ معًا")}</span>
          <h2>{T("Planning a project in the Kingdom? Talk to our engineering team.", "تخطط لمشروع في المملكة؟ تحدّث مع فريقنا الهندسي.")}</h2>
          <p>{T("From site development to plant shutdowns, we deliver safe, on-schedule and cost-effective execution across Saudi Arabia.",
                "من تطوير المواقع إلى إيقاف المصانع للصيانة، ننفّذ أعمالنا بأمان وفي الموعد وبتكلفة فعّالة في جميع أنحاء المملكة.")}</p>
        </div>
        <div class="actions">
          <a href="contact.html" class="btn btn-accent">{T("Request a Quote", "اطلب عرض سعر")} {arrow()}</a>
          <a href="service.html" class="btn btn-ghost">{T("Our services", "خدماتنا")}</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''

def footer():
    return f'''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="footer-logo"><img src="{IMG("logo.png")}" alt="{T("Hemamco Company Limited", "شركة هممكو المحدودة")}" loading="lazy" width="121" height="56"></a>
        <p>{T("Since 2006, Hemamco Company Limited has delivered civil, mechanical, fabrication, electrical and industrial services for the Kingdom’s leading energy, utilities and petrochemical organisations.",
              "منذ عام 2006 تقدّم شركة هممكو المحدودة الأعمال المدنية والميكانيكية والتصنيع والأعمال الكهربائية والخدمات الصناعية لكبرى جهات الطاقة والمرافق والبتروكيماويات في المملكة.")}</p>
        <div class="socials">
          <a href="https://www.facebook.com/Hemam-Al-Ard-Cont-Company-178056326137829/" aria-label="Facebook" target="_blank" rel="noopener">{ic("fb")}</a>
          <a href="https://twitter.com/ArdHemam" aria-label="X (Twitter)" target="_blank" rel="noopener">{ic("x")}</a>
          <a href="mailto:info@hemamco.com" aria-label="{T("Email", "البريد الإلكتروني")}">{ic("mail")}</a>
        </div>
      </div>
      <div>
        <h4>{T("Company", "الشركة")}</h4>
        <ul>
          <li><a href="about.html">{T("About Hemamco", "عن هممكو")}</a></li>
          <li><a href="safety.html">{T("Safety Policy", "سياسة السلامة")}</a></li>
          <li><a href="quality.html">{T("Quality Control", "ضبط الجودة")}</a></li>
          <li><a href="org.html">{T("Organization Chart", "الهيكل التنظيمي")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{T("Explore", "تصفّح")}</h4>
        <ul>
          <li><a href="service.html">{T("Our Services", "خدماتنا")}</a></li>
          <li><a href="ongoing.html">{T("Ongoing Projects", "المشاريع الجارية")}</a></li>
          <li><a href="completed.html">{T("Completed Projects", "المشاريع المنجزة")}</a></li>
          <li><a href="gallery.html">{T("Project Gallery", "معرض المشاريع")}</a></li>
          <li><a href="manpower.html">{T("Manpower &amp; Equipment", "القوى العاملة والمعدات")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{T("Head Office", "المقر الرئيسي")}</h4>
        <ul class="f-contact">
          <li>{ic("pin")}<span>{T("P.O. Box 9334, Dammam 32273<br>Kingdom of Saudi Arabia", "ص.ب 9334، الدمام 32273<br>المملكة العربية السعودية")}</span></li>
          <li>{ic("phone")}<a href="tel:+966138174333">{PHONE}</a></li>
          <li>{ic("mail")}<a href="mailto:info@hemamco.com">info@hemamco.com</a></li>
          <li>{ic("clock")}<span>{T("Sun – Thu: 7:30 AM – 5:00 PM", "الأحد – الخميس: 7:30 ص – 5:00 م")}</span></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <span>© <span id="year">2026</span> {T("Hemamco Company Limited. All rights reserved.", "شركة هممكو المحدودة. جميع الحقوق محفوظة.")}</span>
      <span>{T('<span class="ar" lang="ar">شركة هممكو المحدودة — الدمام، المملكة العربية السعودية</span>', '<span lang="en">Hemamco Company Limited — Dammam, Saudi Arabia</span>')}</span>
    </div>
  </div>
</footer>
<button class="to-top" aria-label="{T("Back to top", "العودة إلى الأعلى")}">{ic("up")}</button>
<script src="{P}assets/js/site.js" defer></script>
</body>
</html>
'''

def page_hero(title, sub, crumbs, img):
    cr = f'<li><a href="index.html">{T("Home", "الرئيسية")}</a></li>' + "".join(
        (f'<li><a href="{h}">{l}</a></li>' if h else f'<li aria-current="page">{l}</li>') for l, h in crumbs)
    return f'''<section class="page-hero">
  <img class="bg" src="{IMG(img)}" alt="">
  <div class="container">
    <ol class="crumbs">{cr}</ol>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
'''

PAGE_LINK = re.compile(r'href="((?:\.\./|ar/)?)([a-z-]+)\.html(#[^"]*)?"')

def clean_links(html):
    """Drop ".html" from links between pages: about.html -> about, index.html -> ./"""
    def repl(m):
        prefix, page, frag = m.group(1), m.group(2), m.group(3) or ""
        return f'href="{(prefix or "./") if page == "index" else prefix + page}{frag}"'
    return PAGE_LINK.sub(repl, html)

def write(name, title, desc, body):
    out_dir = os.path.join(ROOT, "ar") if LANG == "ar" else ROOT
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
        f.write(clean_links(head(title, desc, name) + header(name) + body + footer()))
    print("wrote", ("ar/" if LANG == "ar" else "") + name)

def site_title(page):
    return f'{page} | {T("Hemamco Company Limited", "شركة هممكو المحدودة")}'

def CHECK(text):
    return f"<li>{ic('check')} {text}</li>"

# ---------------- shared blocks ----------------
def stats_block(cls="stats-bar"):
    items = [(TOTAL_STAFF, T("Skilled professionals", "موظف ومهني ماهر")), (TOTAL_EQUIP, T("Equipment units", "وحدة معدات")),
             (YEARS, T("Years in the Kingdom", "عامًا في المملكة")), (len(COMPLETED), T("Projects delivered", "مشروعًا منجزًا"))]
    s = "".join(f'<div class="stat"><div class="num"><span class="n" data-count="{n}">{n:,}</span><span>+</span></div><div class="label">{l}</div></div>' for n, l in items)
    return f'<section class="{cls}"><div class="container"><div class="inner reveal">{s}</div></div></section>'

def svc_cards():
    out = []
    for i, (key, title, img, icon, text) in enumerate(SERVICES):
        out.append(f'''<article class="svc-card reveal d{i % 3 + 1}">
  <div class="img"><img src="{IMG(img)}" alt="{L(title)}" loading="lazy"><span class="icon">{ic(icon)}</span></div>
  <div class="body"><h3>{L(title)}</h3><p>{L(text)}</p><a href="service.html#{key}" class="link-arrow">{T("Learn more", "اعرف المزيد")} {arrow()}</a></div>
</article>''')
    return "\n".join(out)

def clients_block():
    c = "".join(f'<div class="client"><div class="name">{L(n)}</div><div class="kind">{L(k)}</div></div>' for n, k in CLIENTS)
    return f'<div class="clients reveal">{c}</div>'

def proj_cards(items):
    cards = []
    for img, title, client, value, service, dt, pct in items:
        meta = f"{E(L(client))} · {E(date(dt))}"
        if pct is not None:
            meta += f" · {pct_text(pct)}"
        cards.append(f'''<a class="proj-card reveal" href="ongoing.html">
  <img src="{PIMG(img)}" alt="{E(L(title))}" loading="lazy">
  <div class="info"><span class="tag">{E(L(service))}</span><h3>{E(L(title))}</h3><div class="meta">{meta}</div></div>
</a>''')
    return "\n".join(cards)

def side(current):
    links = [(T("Company Overview", "نبذة عن الشركة"), "about.html"), (T("Safety Policy", "سياسة السلامة"), "safety.html"),
             (T("Quality Control Policy", "سياسة ضبط الجودة"), "quality.html"), (T("Organization Chart", "الهيكل التنظيمي"), "org.html")]
    li = "".join(f'<li><a href="{h}"{" class=active" if h == current else ""}>{l} {arrow()}</a></li>' for l, h in links)
    return f'<aside class="sticky-side"><ul class="side-nav">{li}</ul></aside>'

def completion_block(pct):
    label = T("Completion", "نسبة الإنجاز")
    if pct is None:
        return f'<div class="completion"><div class="top"><span>{label}</span><strong>{pct_text(None)}</strong></div></div>'
    width = f"{pct:.2f}".rstrip("0").rstrip(".")
    return f'''<div class="completion">
  <div class="top"><span>{label}</span><strong>{pct_text(pct)}</strong></div>
  <div class="track" role="progressbar" aria-valuenow="{width}" aria-valuemin="0" aria-valuemax="100" aria-label="{label}"><span class="bar" style="width:{width}%"></span></div>
</div>'''

def project_rows():
    out = ""
    for img, title, client, value, service, dt, pct in ONGOING:
        out += f'''<article class="project-row reveal">
  <div class="img"><img src="{PIMG(img)}" alt="{E(L(title))}" loading="lazy"></div>
  <div class="body">
    <span class="status-pill ongoing">{T("Ongoing", "جارٍ")}</span>
    <h3>{E(L(title))}</h3>
    <dl class="dl"><dt>{T("Client", "العميل")}</dt><dd>{E(L(client))}</dd><dt>{T("Contract value", "قيمة العقد")}</dt><dd>{E(L(value))}</dd><dt>{T("Type of service", "نوع الخدمة")}</dt><dd>{E(L(service))}</dd><dt>{T("Start date", "تاريخ البدء")}</dt><dd>{E(date(dt))}</dd></dl>
    {completion_block(pct)}
  </div>
</article>'''
    return out

def res_tabs(current):
    return f'''<div class="filters reveal" style="justify-content:flex-start">
  <a href="manpower.html" class="btn {"btn-primary" if current == "manpower.html" else "btn-outline"}">{ic("users")} {T("Manpower", "القوى العاملة")}</a>
  <a href="equipment.html" class="btn {"btn-primary" if current == "equipment.html" else "btn-outline"}">{ic("truck")} {T("Equipment", "المعدات")}</a>
</div>'''

# ======================= PAGES =======================
def page_home():
    hero = [
        ("hero-riyadh.jpg", T("Building the Kingdom since 2006", "نبني المملكة منذ 2006"),
         T("Engineering &amp; construction <em>built on safety, quality</em> and commitment.",
           "هندسة وإنشاءات <em>قائمة على السلامة والجودة</em> والالتزام."),
         T("Hemamco Company Limited delivers civil, mechanical, fabrication and electrical works for Saudi Arabia’s leading energy, utilities and industrial organisations.",
           "تقدّم شركة هممكو المحدودة الأعمال المدنية والميكانيكية والتصنيع والأعمال الكهربائية لكبرى جهات الطاقة والمرافق والصناعة في المملكة العربية السعودية.")),
        ("hero-refinery.jpg", T("Oil, Gas &amp; Petrochemical", "النفط والغاز والبتروكيماويات"),
         T("Trusted on the Kingdom’s <em>most demanding</em> industrial sites.",
           "شريك موثوق في <em>أكثر المواقع الصناعية تطلبًا</em> في المملكة."),
         T("From pipeline right-of-way to plant shutdowns, our teams work to Saudi Aramco, SABIC and Ma’aden standards — on schedule and within budget.",
           "من حرم خطوط الأنابيب إلى إيقاف المصانع للصيانة، تعمل فرقنا وفق معايير أرامكو السعودية وسابك ومعادن، في الموعد وضمن الميزانية.")),
        ("hero-desert-site.jpg", T("Vision 2030 ready", "جاهزون لرؤية 2030"),
         T("Cost-effective engineering, <em>delivered with precision.</em>", "حلول هندسية فعّالة التكلفة <em>تُنفَّذ بدقة.</em>"),
         T(f"Solid QA/QC, value engineering and a {TOTAL_STAFF:,}+ strong workforce make Hemamco a benchmark of professionalism across the Eastern Province.",
           f"ضبط جودة متين، وهندسة قيمية، وقوى عاملة تتجاوز {TOTAL_STAFF:,} موظف، تجعل هممكو معيارًا للاحترافية في المنطقة الشرقية.")),
    ]
    slides = "".join(f'<div class="hero-slide{" active" if i == 0 else ""}"><img src="{IMG(img)}" alt="" {"fetchpriority=high" if i == 0 else "loading=lazy"}></div>' for i, (img, *_ ) in enumerate(hero))
    texts = "".join(f'''<div class="hero-text"{"" if i == 0 else " hidden"}>
  <div class="hero-badge"><b>{T("HEMAMCO", "هممكو")}</b> {badge}</div>
  <h1>{h}</h1>
  <p>{p}</p>
</div>''' for i, (_, badge, h, p) in enumerate(hero))
    dots = "".join(f'<button class="{"active" if i == 0 else ""}" aria-label="{T("Slide", "الشريحة")} {i + 1}"></button>' for i in range(len(hero)))
    feature = lambda icn, h, p: f'<div class="feature"><div class="ic">{ic(icn)}</div><div><h4>{h}</h4><p>{p}</p></div></div>'
    body = f'''<section class="hero">
  {slides}
  <div class="container">
    <div class="hero-content">
      {texts}
      <div class="actions">
        <a href="service.html" class="btn btn-accent">{T("Explore our services", "استكشف خدماتنا")} {arrow()}</a>
        <a href="contact.html" class="btn btn-ghost">{T("Request a quote", "اطلب عرض سعر")}</a>
      </div>
    </div>
  </div>
  <div class="hero-dots">{dots}</div>
</section>
{stats_block()}

<section class="section">
  <div class="container split">
    <div class="media-stack reveal">
      <div class="main"><img src="{IMG("engineer.jpg")}" alt="{T("Site engineer directing works", "مهندس موقع يوجّه الأعمال")}" loading="lazy"></div>
      <div class="sub"><img src="{PIMG("project-big-img1.jpg")}" alt="{T("Hemamco crew on a Saudi Aramco site", "فريق هممكو في أحد مواقع أرامكو السعودية")}" loading="lazy"></div>
      <div class="badge-years"><div class="n">{YEARS}+</div><div class="t">{T("Years of<br>excellence", "عامًا من<br>التميّز")}</div></div>
    </div>
    <div class="reveal d1">
      <span class="eyebrow">{T("About Hemamco", "عن هممكو")}</span>
      <h2>{T("A Dammam-based contractor with the resources of the Kingdom’s best.", "مقاول من الدمام بموارد تضاهي أفضل الشركات في المملكة.")}</h2>
      <p class="lead">{T("Founded in 2006, Hemamco Company Limited has grown through determination, skill and strong working ethics into a dynamic organisation of highly skilled, motivated professionals.",
                         "تأسست شركة هممكو المحدودة عام 2006، ونمت بالعزيمة والمهارة وأخلاقيات العمل الراسخة لتصبح مؤسسة ديناميكية تضم نخبة من المهنيين ذوي الكفاءة العالية.")}</p>
      <p>{T("Today our resources are on par with any reputable construction company in the Kingdom — enabling us to execute everything from small works to multi-million riyal projects for national energy, utilities and petrochemical leaders.",
            "واليوم تضاهي مواردنا أي شركة إنشاءات مرموقة في المملكة، مما يمكّننا من تنفيذ كل شيء من الأعمال الصغيرة إلى المشاريع التي تبلغ قيمتها ملايين الريالات لكبرى جهات الطاقة والمرافق والبتروكيماويات.")}</p>
      <ul class="checklist">
        {CHECK(T("Saudi Aramco &amp; SABIC approved work standards", "معايير عمل معتمدة لدى أرامكو السعودية وسابك"))}
        {CHECK(T("10,000 m² fabrication facility in Dammam", "منشأة تصنيع بمساحة 10,000 م² في الدمام"))}
        {CHECK(T("Dedicated QA/QC and HSE departments", "إدارات مختصة بالجودة والصحة والسلامة والبيئة"))}
        {CHECK(T(f"In-house fleet of {TOTAL_EQUIP}+ equipment units", f"أسطول خاص يضم أكثر من {TOTAL_EQUIP} وحدة معدات"))}
      </ul>
      <a href="about.html" class="btn btn-primary">{T("Discover our story", "اكتشف قصتنا")} {arrow()}</a>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">{T("What we do", "ماذا نقدّم")}</span>
      <h2>{T("Integrated services for industry and infrastructure", "خدمات متكاملة للصناعة والبنية التحتية")}</h2>
      <p class="lead">{T("Multi-discipline capabilities under one roof — so our clients deal with one accountable partner from mobilisation to handover.",
                         "قدرات متعددة التخصصات تحت سقف واحد، ليتعامل عملاؤنا مع شريك واحد مسؤول من التجهيز حتى التسليم.")}</p>
    </div>
    <div class="grid grid-3">
{svc_cards()}
    </div>
    <div style="text-align:center;margin-top:50px"><a href="service.html" class="btn btn-outline">{T("View all services", "عرض جميع الخدمات")} {arrow()}</a></div>
  </div>
</section>

<section class="section bg-navy">
  <div class="container split wide-left">
    <div class="reveal">
      <span class="eyebrow">{T("Why Hemamco", "لماذا هممكو")}</span>
      <h2>{T("Quality, safety and commitment on every site.", "الجودة والسلامة والالتزام في كل موقع.")}</h2>
      <p class="lead">{T("We provide safe and cost-effective engineering services that meet both local and international standards.",
                         "نقدّم خدمات هندسية آمنة وفعّالة التكلفة تلبّي المعايير المحلية والدولية.")}</p>
      <div class="grid grid-2" style="margin-top:36px;gap:18px">
        {feature("shield", T("Safety first", "السلامة أولًا"), T("A loss-prevention program targeting zero accidents, with 20+ dedicated safety officers.", "برنامج لمنع الخسائر يستهدف صفر حوادث، مع أكثر من 20 مسؤول سلامة متفرغ."))}
        {feature("award", T("Solid QA/QC", "ضبط جودة متين"), T("Independent quality control authorised to stop any non-conforming activity.", "ضبط جودة مستقل مخوّل بإيقاف أي نشاط غير مطابق."))}
        {feature("users", T("Effective teamwork", "عمل جماعي فعّال"), T("Experienced managers, engineers and trades working as one accountable team.", "مدراء ومهندسون وحرفيون ذوو خبرة يعملون كفريق واحد مسؤول."))}
        {feature("coins", T("Financially stable", "استقرار مالي"), T("A strong financial position ready to fund the smooth completion of projects.", "مركز مالي قوي قادر على تمويل إنجاز المشاريع بسلاسة."))}
      </div>
    </div>
    <div class="media reveal d2"><img src="{IMG("team-site.jpg")}" alt="{T("Engineers reviewing plans on site", "مهندسون يراجعون المخططات في الموقع")}" loading="lazy"></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal" style="display:flex;justify-content:space-between;align-items:flex-end;max-width:none;gap:30px;flex-wrap:wrap">
      <div style="max-width:640px"><span class="eyebrow">{T("Our projects", "مشاريعنا")}</span><h2 style="margin:0">{T("Current work across the Kingdom", "أعمالنا الحالية في أنحاء المملكة")}</h2></div>
      <a href="ongoing.html" class="btn btn-outline">{T("All projects", "جميع المشاريع")} {arrow()}</a>
    </div>
    <div class="grid grid-3">
{proj_cards(ONGOING[:3])}
    </div>
  </div>
</section>

<section class="section-sm bg-soft">
  <div class="container">
    <div class="section-head center reveal" style="margin-bottom:40px">
      <span class="eyebrow">{T("Trusted by", "شركاء النجاح")}</span>
      <h2>{T("The Kingdom’s industry leaders", "روّاد الصناعة في المملكة")}</h2>
    </div>
    {clients_block()}
  </div>
</section>
{cta()}'''
    write("index.html", T("Hemamco Company Limited | Engineering & Construction in Saudi Arabia", "شركة هممكو المحدودة | الهندسة والإنشاءات في المملكة العربية السعودية"),
          T("Hemamco Company Limited — Dammam-based contractor delivering civil, mechanical, piping, fabrication, steel erection, electrical and fireproofing works across Saudi Arabia since 2006.",
            "شركة هممكو المحدودة — مقاول من الدمام ينفّذ الأعمال المدنية والميكانيكية والأنابيب والتصنيع وتركيب الهياكل الفولاذية والأعمال الكهربائية والحماية من الحريق في المملكة منذ 2006."),
          body)

def page_about():
    panel = lambda icn, h, p, d="": f'<div class="panel reveal {d}"><h3><span class="ic">{ic(icn)}</span>{h}</h3><p>{p}</p></div>'
    body = page_hero(T("About Hemamco", "عن هممكو"), T("Secure, safe and more than two decades of excellence in Saudi construction.", "أكثر من عقدين من التميّز والأمان في قطاع الإنشاءات السعودي."),
                     [(T("About", "من نحن"), None)], "header-riyadh.jpg") + f'''
<section class="section">
  <div class="container split">
    <div class="media-stack reveal">
      <div class="main"><img src="{IMG("team-site.jpg")}" alt="{T("Hemamco engineers on site", "مهندسو هممكو في الموقع")}" loading="lazy"></div>
      <div class="sub"><img src="{IMG("svc-fabrication.jpg")}" alt="{T("Fabrication workshop", "ورشة التصنيع")}" loading="lazy"></div>
      <div class="badge-years"><div class="n">2006</div><div class="t">{T("Established", "سنة التأسيس")}</div></div>
    </div>
    <div class="reveal d1">
      <span class="eyebrow">{T("Who we are", "من نحن")}</span>
      <h2>{T("Built on determination, skill and integrity.", "قائمون على العزيمة والمهارة والنزاهة.")}</h2>
      <p class="lead">{T("Hemamco Company Limited was established in 2006 with a bold vision to excel in the construction industry.", "تأسست شركة هممكو المحدودة عام 2006 برؤية طموحة للتميّز في قطاع الإنشاءات.")}</p>
      <p>{T("Through unwavering determination, exceptional skills, a dedicated workforce and adherence to the highest professional standards, our organisation has evolved into a dynamic enterprise staffed by highly skilled, motivated and committed professionals. Today, we possess resources and capabilities that rival any reputable construction company in the Kingdom of Saudi Arabia.",
            "بفضل العزيمة الراسخة والمهارات الاستثنائية والكوادر المتفانية والالتزام بأعلى المعايير المهنية، تطورت مؤسستنا لتصبح منشأة ديناميكية تضم مهنيين ذوي كفاءة عالية والتزام كبير. واليوم نمتلك موارد وقدرات تضاهي أي شركة إنشاءات مرموقة في المملكة العربية السعودية.")}</p>
      <p>{T("We specialise in comprehensive civil, mechanical, fabrication and construction services — earthworks, site development, roads, sidewalks, perimeter fencing, asphalt paving, water distribution, drainage and sewerage networks, landscaping, street lighting and building construction.",
            "نتخصص في الخدمات المدنية والميكانيكية والتصنيع والإنشاءات المتكاملة، بما في ذلك الأعمال الترابية وتطوير المواقع والطرق والأرصفة والأسوار المحيطة والسفلتة وشبكات توزيع المياه والتصريف والصرف الصحي وتنسيق المواقع وإنارة الشوارع وتشييد المباني.")}</p>
    </div>
  </div>
</section>
{stats_block("section-sm bg-soft")}
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      {panel("eye", T("Our Vision", "رؤيتنا"), T("To be recognised as one of the leading engineering and construction companies in Saudi Arabia by delivering high-quality, safety-focused and cost-effective services that meet both local and international standards.", "أن نكون من الشركات الرائدة في الهندسة والإنشاءات في المملكة العربية السعودية من خلال تقديم خدمات عالية الجودة تركّز على السلامة وفعّالة التكلفة وتلبّي المعايير المحلية والدولية."))}
      {panel("target", T("Our Mission", "رسالتنا"), T("To establish Hemamco as an industry leader by independently executing major projects while maintaining an exemplary reputation and earning the appreciation of our valued clients.", "ترسيخ مكانة هممكو كشركة رائدة في القطاع عبر التنفيذ المستقل للمشاريع الكبرى مع الحفاظ على سمعة نموذجية ونيل تقدير عملائنا الكرام."), "d1")}
      {panel("flag", T("Our Values", "قيمنا"), T("We conduct our business with integrity, honesty and dedication — using our professional expertise to achieve the success our stakeholders deserve, through continuous improvement.", "نمارس أعمالنا بنزاهة وأمانة وتفانٍ، مستثمرين خبرتنا المهنية والتحسين المستمر لتحقيق النجاح الذي يستحقه شركاؤنا."), "d2")}
    </div>
  </div>
</section>
<section class="section bg-soft">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">{T("Industrial capability", "القدرات الصناعية")}</span>
      <h2>{T("Mechanical and industrial services throughout the Kingdom.", "خدمات ميكانيكية وصناعية في جميع أنحاء المملكة.")}</h2>
      <p>{T("In addition to civil works, Hemamco provides superior mechanical engineering services including:", "إلى جانب الأعمال المدنية، تقدّم هممكو خدمات هندسية ميكانيكية متميزة تشمل:")}</p>
      <ul class="checklist">
        {CHECK(T("Pipeline construction &amp; maintenance", "إنشاء خطوط الأنابيب وصيانتها"))}
        {CHECK(T("Mechanical installations", "التركيبات الميكانيكية"))}
        {CHECK(T("Plant shutdowns", "أعمال إيقاف المصانع للصيانة"))}
        {CHECK(T("Electrical &amp; instrumentation", "الكهرباء والأجهزة الدقيقة"))}
        {CHECK(T("Insulation services", "خدمات العزل"))}
        {CHECK(T("Onshore pipeline repair &amp; reconditioning", "إصلاح وتأهيل خطوط الأنابيب البرية"))}
        {CHECK(T("Industrial piping fabrication &amp; erection", "تصنيع وتركيب الأنابيب الصناعية"))}
        {CHECK(T("Industrial tank maintenance", "صيانة الخزانات الصناعية"))}
        {CHECK(T("Protective coating &amp; painting", "الطلاءات الواقية والدهانات"))}
        {CHECK(T("Steel structure fabrication &amp; erection", "تصنيع وتركيب الهياكل الفولاذية"))}
      </ul>
      <a href="service.html" class="btn btn-primary">{T("Our services", "خدماتنا")} {arrow()}</a>
    </div>
    <div class="reveal d1" style="border-radius:22px;overflow:hidden;box-shadow:var(--shadow);aspect-ratio:4/4.4"><img src="{IMG("oil-gas-plant.jpg")}" alt="{T("Industrial plant at night", "منشأة صناعية ليلًا")}" loading="lazy" style="width:100%;height:100%;object-fit:cover"></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">{T("Our distinguished clients", "عملاؤنا المميزون")}</span>
      <h2>{T("Partners who trust our work", "شركاء يثقون بأعمالنا")}</h2>
      <p class="lead">{T("Over two decades we have built an impressive portfolio across building construction, mechanical engineering, fabrication, pipeline construction and maintenance services.",
                         "على مدى أكثر من عقدين بنينا سجلًا مميزًا في تشييد المباني والهندسة الميكانيكية والتصنيع وإنشاء خطوط الأنابيب وخدمات الصيانة.")}</p>
    </div>
    {clients_block()}
  </div>
</section>
{cta()}'''
    write("about.html", site_title(T("About Us", "من نحن")),
          T("Established in 2006 in Dammam, Hemamco Company Limited is a leading Saudi engineering and construction contractor.",
            "تأسست شركة هممكو المحدودة عام 2006 في الدمام، وهي من مقاولي الهندسة والإنشاءات الرائدين في المملكة."), body)

def steps(items):
    return '<ol class="steps">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def page_safety():
    body = page_hero(T("Safety Policy", "سياسة السلامة"), T("Every employee is entitled to a safe and healthy work environment.", "من حق كل موظف أن يعمل في بيئة آمنة وصحية."),
                     [(T("About", "من نحن"), "about.html"), (T("Safety Policy", "سياسة السلامة"), None)], "header-steel.jpg") + f'''
<section class="section">
  <div class="container layout-side">
    <div>
      <div class="prose reveal">
        <span class="eyebrow">{T("Loss Prevention Program", "برنامج منع الخسائر")}</span>
        <h2>{T("Safety is a condition of employment at Hemamco.", "السلامة شرط أساسي للعمل في هممكو.")}</h2>
        <p class="lead">{T("The Hemamco Loss Prevention Program is based on the premise that every employee is entitled to a safe and healthy work environment. It is designed specifically for the protection of our employees and visitors, and management and all employees are directed to make safety and loss prevention a top priority.",
                           "يقوم برنامج منع الخسائر في هممكو على مبدأ أن لكل موظف الحق في بيئة عمل آمنة وصحية. وقد صُمّم البرنامج خصيصًا لحماية موظفينا وزوارنا، ويُوجَّه الإداريون وجميع الموظفين إلى جعل السلامة ومنع الخسائر أولوية قصوى.")}</p>
        <p>{T("The goals we set are achieved through a cooperative effort among all employees and management. Safe work habits and awareness of all safety rules and policies are a condition of employment. All employees are required to attend training sessions to become familiar with these rules and to abide by them; they are enforced like any other company policy, and failure to comply can result in reprimand, suspension or termination.",
              "تتحقق أهدافنا بالتعاون بين جميع الموظفين والإدارة. وتُعدّ عادات العمل الآمنة والوعي بجميع قواعد وسياسات السلامة شرطًا للتوظيف. ويُلزَم جميع الموظفين بحضور الدورات التدريبية للتعرّف على هذه القواعد والتقيّد بها، وتُطبَّق كأي سياسة أخرى في الشركة، وقد يؤدي عدم الالتزام بها إلى الإنذار أو الإيقاف أو إنهاء الخدمة.")}</p>
        <p>{T("All employees are encouraged to make suggestions that help maintain safe work conditions and to bring them to their supervisor’s attention. It is through our joint participation that accidents can be prevented — but only you can make safe work practices a habit.",
              "نشجّع جميع الموظفين على تقديم المقترحات التي تساعد على الحفاظ على ظروف عمل آمنة ورفعها إلى مشرفيهم. فبالمشاركة المشتركة يمكن منع الحوادث، لكنك وحدك من يجعل ممارسات العمل الآمنة عادة.")}</p>
      </div>
      <div class="grid grid-3" style="margin-top:44px">
        <div class="panel reveal"><h3><span class="ic">{ic("flag")}</span>{T("Goals", "الأهداف")}</h3>{steps([
            T("Annually reduce employee accidents and injuries until they stand at or near zero.", "خفض حوادث وإصابات الموظفين سنويًا حتى تصل إلى الصفر أو تقترب منه."),
            T("Help develop safe work habits and attitudes among employees.", "المساعدة على ترسيخ عادات وسلوكيات العمل الآمن لدى الموظفين."),
            T("Provide a channel of communication between employees and management.", "توفير قناة تواصل بين الموظفين والإدارة.")])}</div>
        <div class="panel reveal d1"><h3><span class="ic">{ic("target")}</span>{T("Objectives", "الغايات")}</h3><p>{T("Establish a Loss Prevention Program that reduces injuries and accidents to a minimum — not merely keeping with, but surpassing the best experience of similar operations.", "إرساء برنامج لمنع الخسائر يخفّض الإصابات والحوادث إلى الحد الأدنى، لا بمجاراة أفضل تجارب المنشآت المماثلة فحسب، بل بتجاوزها.")}</p></div>
        <div class="panel reveal d2"><h3><span class="ic">{ic("list")}</span>{T("Tactics", "الأساليب")}</h3>{steps([
            T("Review past injuries quarterly for trends and causes.", "مراجعة الإصابات السابقة كل ثلاثة أشهر لتحديد الاتجاهات والأسباب."),
            T("Review the program annually to meet current safety needs.", "مراجعة البرنامج سنويًا لتلبية احتياجات السلامة الحالية."),
            T("Provide supervisors and employees with safety training.", "توفير التدريب على السلامة للمشرفين والموظفين.")])}</div>
      </div>
    </div>
    {side("safety.html")}
  </div>
</section>
{cta()}'''
    write("safety.html", site_title(T("Safety Policy", "سياسة السلامة")),
          T("Hemamco Loss Prevention Program — goals, objectives and tactics for a safe and healthy workplace.", "برنامج منع الخسائر في هممكو — الأهداف والغايات والأساليب لبيئة عمل آمنة وصحية."), body)

def page_quality():
    panel = lambda icn, h, p, d="": f'<div class="panel reveal {d}"><h3><span class="ic">{ic(icn)}</span>{h}</h3><p>{p}</p></div>'
    body = page_hero(T("Quality Control Policy", "سياسة ضبط الجودة"), T("Consistent quality of work that conforms to contract requirements and specifications.", "جودة عمل ثابتة تتوافق مع متطلبات العقود ومواصفاتها."),
                     [(T("About", "من نحن"), "about.html"), (T("Quality Control", "ضبط الجودة"), None)], "header-canopy.jpg") + f'''
<section class="section">
  <div class="container layout-side">
    <div>
      <div class="prose reveal">
        <span class="eyebrow">{T("QA / QC", "ضمان وضبط الجودة")}</span>
        <h2>{T("Strict conformance, at every stage of construction.", "التزام صارم بالمطابقة في كل مراحل التنفيذ.")}</h2>
        <p class="lead">{T("Hemamco is committed to providing a consistent quality of work performance that meets the acceptable quality standards set out in our Quality Control Plan, conforming to the contract requirements and specifications in all matters.",
                           "تلتزم هممكو بتقديم أداء عمل بجودة ثابتة يلبّي معايير الجودة المعتمدة في خطة ضبط الجودة لدينا، ويتوافق مع متطلبات العقد ومواصفاته في جميع الأمور.")}</p>
        <p>{T("The Quality Control Program was established to ensure that all activities are performed in strict conformance with the approved construction drawings and all applicable standards and requirements of the specifications.",
              "أُنشئ برنامج ضبط الجودة لضمان تنفيذ جميع الأنشطة بمطابقة تامة للمخططات الإنشائية المعتمدة وجميع المعايير والمتطلبات المعمول بها في المواصفات.")}</p>
      </div>
      <div class="grid grid-2" style="margin-top:40px">
        {panel("users", T("Responsibility", "المسؤولية"), T("The Quality Control System Manager and team hold overall responsibility for maintaining the program and ensuring all construction activities proceed as per contract requirements.", "يتولى مدير نظام ضبط الجودة وفريقه المسؤولية الكاملة عن الحفاظ على البرنامج وضمان سير جميع أنشطة التنفيذ وفق متطلبات العقد."))}
        {panel("shield", T("Authority to stop work", "صلاحية إيقاف العمل"), T("The QC Department, in consent with the Project Manager, is fully authorised to stop any activity not in compliance with contract specifications. Disputes are resolved between the Project Manager and the QC Manager.", "تملك إدارة ضبط الجودة، بالتنسيق مع مدير المشروع، الصلاحية الكاملة لإيقاف أي نشاط غير مطابق لمواصفات العقد، وتُحلّ الخلافات بين مدير المشروع ومدير ضبط الجودة."), "d1")}
        {panel("layers", T("Company-wide", "على مستوى الشركة"), T("The Quality Control Program is binding on all Hemamco personnel and is implemented without alteration or deviation.", "برنامج ضبط الجودة ملزم لجميع منسوبي هممكو ويُطبَّق دون تعديل أو انحراف."))}
        {panel("award", T("Safe &amp; healthy workplace", "بيئة عمل آمنة وصحية"), T("Hemamco is committed to providing its employees with a safe and healthy working environment through clearly defined goals, objectives and tactics.", "تلتزم هممكو بتوفير بيئة عمل آمنة وصحية لموظفيها من خلال أهداف وغايات وأساليب محددة بوضوح."), "d1")}
      </div>
    </div>
    {side("quality.html")}
  </div>
</section>
{cta()}'''
    write("quality.html", site_title(T("Quality Control Policy", "سياسة ضبط الجودة")),
          T("Hemamco Quality Control Program — strict conformance to approved drawings, standards and specifications.", "برنامج ضبط الجودة في هممكو — مطابقة صارمة للمخططات والمعايير والمواصفات المعتمدة."), body)

def page_org():
    body = page_hero(T("Organization Chart", "الهيكل التنظيمي"), T("A clear structure from executive management to site operations.", "هيكل واضح من الإدارة التنفيذية إلى عمليات المواقع."),
                     [(T("About", "من نحن"), "about.html"), (T("Organization Chart", "الهيكل التنظيمي"), None)], "header-dusk.jpg") + f'''
<section class="section bg-soft">
  <div class="container">
    <div class="chart-frame reveal">
      <h3>{T("Company Organization Chart", "الهيكل التنظيمي للشركة")}</h3>
      <a href="{PIMG("org.jpg")}" data-lightbox data-caption="{T("Company Organization Chart", "الهيكل التنظيمي للشركة")}"><img src="{PIMG("org.jpg")}" alt="{T("Hemamco company organization chart", "الهيكل التنظيمي لشركة هممكو")}"></a>
    </div>
    <div class="chart-frame reveal">
      <h3>{T("Operation Organization Chart", "الهيكل التنظيمي للعمليات")}</h3>
      <a href="{PIMG("org1.jpg")}" data-lightbox data-caption="{T("Operation Organization Chart", "الهيكل التنظيمي للعمليات")}"><img src="{PIMG("org1.jpg")}" alt="{T("Hemamco operation organization chart", "الهيكل التنظيمي لعمليات هممكو")}"></a>
    </div>
  </div>
</section>
{cta()}'''
    write("org.html", site_title(T("Organization Chart", "الهيكل التنظيمي")),
          T("Hemamco company and operations organization charts.", "الهيكل التنظيمي لشركة هممكو وعملياتها."), body)

def page_services():
    details = [
        ("civil", T("Civil &amp; Earth Works", "الأعمال المدنية والترابية"), "svc-civil.jpg",
         [T("Civil engineering and earthworks with special expertise in site development, roads, asphalting and substation buildings.", "الهندسة المدنية والأعمال الترابية بخبرة خاصة في تطوير المواقع والطرق والسفلتة ومباني المحطات الفرعية."),
          T("Our team-oriented philosophy, value engineering, solid QA/QC and overall professionalism are recognised as a benchmark of industry standard.", "ويُعدّ نهجنا القائم على العمل الجماعي والهندسة القيمية وضبط الجودة المتين والاحترافية الشاملة معيارًا مرجعيًا في القطاع.")],
         [T("Site development &amp; grading", "تطوير المواقع والتسوية"), T("Roads &amp; asphalt paving", "الطرق والسفلتة"), T("Drainage &amp; sewerage", "التصريف والصرف الصحي"), T("Perimeter fencing &amp; gates", "الأسوار المحيطة والبوابات")]),
        ("piping", T("Mechanical &amp; Piping", "الأعمال الميكانيكية والأنابيب"), "svc-piping.jpg",
         [T("Within sectors such as oil and gas, mining and metals, chemical processing and water, we provide a complete construction service — engineering, procurement, fabrication and field erection for mechanical, piping and electrical installation works through to commissioning.",
            "في قطاعات النفط والغاز والتعدين والمعادن والمعالجة الكيميائية والمياه، نقدّم خدمة إنشاء متكاملة تشمل الهندسة والتوريد والتصنيع والتركيب الميداني للأعمال الميكانيكية والأنابيب والتركيبات الكهربائية حتى التشغيل.")],
         [T("Pipeline construction", "إنشاء خطوط الأنابيب"), T("Plant shutdowns", "إيقاف المصانع للصيانة"), T("Tank maintenance", "صيانة الخزانات"), T("Commissioning support", "دعم التشغيل")]),
        ("fabrication", T("Fabrication", "التصنيع"), "svc-fabrication.jpg",
         [T("Our Dammam fabrication facility is supervised by highly skilled mechanical engineers. Expertise spans oil &amp; gas pipe spooling, process pipework, modular, skid-mounted and containerised fabrication, plate work for tanks, vessels and ducting, and heavy structural steel for mining, crane beams and platforms.",
            "يشرف على منشأة التصنيع في الدمام مهندسون ميكانيكيون ذوو كفاءة عالية، وتشمل خبراتنا تصنيع وصلات أنابيب النفط والغاز، وأنابيب العمليات، والوحدات المعيارية والمحمولة والمعبأة في حاويات، وأعمال الصفائح للخزانات والأوعية والمجاري، والهياكل الفولاذية الثقيلة للتعدين وعوارض الرافعات والمنصات."),
          T("The fully equipped, covered 10,000 m² workshop includes CNC milling machines, lathes, large radial drills, coil cutting, mechanical saws, steel cutting and bending machines and a full range of welding equipment.",
            "وتضم الورشة المغطاة والمجهزة بالكامل بمساحة 10,000 م² آلات تفريز CNC، ومخارط، ومثاقب شعاعية كبيرة، وآلات قص اللفائف، ومناشير ميكانيكية، وآلات قص وثني الحديد، ومجموعة كاملة من معدات اللحام.")],
         [T("Pipe spooling", "تصنيع وصلات الأنابيب"), T("Skids &amp; modules", "الوحدات المحمولة والمعيارية"), T("Tanks &amp; vessels", "الخزانات والأوعية"), T("Heavy structural steel", "الهياكل الفولاذية الثقيلة")]),
        ("electrical", T("Electrical Works", "الأعمال الكهربائية"), "svc-electrical.jpg",
         [T("A wide range of electrical engineering tasks including overhead and underground power lines, fibre optic installation, switchgear and controls in substations, commercial and residential building wiring and street lighting — plus material, labour and construction cost estimation for budget preparation.",
            "مجموعة واسعة من أعمال الهندسة الكهربائية تشمل خطوط الكهرباء الهوائية والأرضية، وتركيب الألياف الضوئية، ولوحات المفاتيح وأنظمة التحكم في المحطات الفرعية، وتمديدات المباني التجارية والسكنية، وإنارة الشوارع، إضافة إلى تقدير تكاليف المواد والعمالة والإنشاء لإعداد الميزانيات.")],
         [T("Overhead &amp; underground lines", "الخطوط الهوائية والأرضية"), T("Substation switchgear", "لوحات المحطات الفرعية"), T("Fibre optics", "الألياف الضوئية"), T("Street lighting", "إنارة الشوارع")]),
        ("steel", T("Steel Erection", "تركيب الهياكل الفولاذية"), "svc-steel.jpg",
         [T("Steel erection for heavy-duty high-rise structures, metal buildings and signage. Steel erection is often the skeletal core of bridges, office buildings and commercial, retail and industrial structures.",
            "تركيب الهياكل الفولاذية للمنشآت الشاهقة الثقيلة والمباني المعدنية واللوحات. وغالبًا ما تمثّل الهياكل الفولاذية العمود الفقري للجسور والمباني المكتبية والمنشآت التجارية والصناعية.")],
         [T("Pipe racks &amp; platforms", "حوامل الأنابيب والمنصات"), T("Metal buildings", "المباني المعدنية"), T("Industrial structures", "المنشآت الصناعية"), T("Telecom &amp; power towers", "أبراج الاتصالات والكهرباء")]),
    ]
    det = ""
    for i, (key, title, img, paras, bullets) in enumerate(details):
        det += f'''<div class="svc-detail{" flip" if i % 2 else ""}" id="{key}">
  <div class="media reveal"><img src="{IMG(img)}" alt="{title}" loading="lazy"></div>
  <div class="reveal d1"><div class="no">0{i + 1}</div><h2>{title}</h2>{"".join(f"<p>{p}</p>" for p in paras)}<ul class="checklist">{"".join(CHECK(b) for b in bullets)}</ul></div>
</div>'''
    mini = lambda icn, h, p, d="": f'<div class="mini reveal {d}"><div class="ic">{ic(icn)}</div><h3>{h}</h3><p>{p}</p></div>'
    body = page_hero(T("Our Services", "خدماتنا"), T("Leading engineering &amp; construction services — on schedule, within budget and to the highest quality.", "خدمات هندسية وإنشائية رائدة — في الموعد وضمن الميزانية وبأعلى جودة."),
                     [(T("Services", "خدماتنا"), None)], "header-steel.jpg") + f'''
<section class="section-sm">
  <div class="container">
    <div class="section-head center reveal" style="margin-bottom:0">
      <span class="eyebrow">{T("Leading engineering &amp; construction", "ريادة في الهندسة والإنشاءات")}</span>
      <h2>{T("From small works to multi-million riyal projects", "من الأعمال الصغيرة إلى المشاريع بملايين الريالات")}</h2>
      <p class="lead">{T("Since 2006 Hemamco has executed projects of every scale. On schedule, within budget, quality workmanship, teamwork and client satisfaction have always been our primary business ethics.",
                         "منذ عام 2006 نفّذت هممكو مشاريع بمختلف الأحجام. وكان الالتزام بالموعد والميزانية وجودة التنفيذ والعمل الجماعي ورضا العملاء دائمًا في صميم أخلاقيات عملنا.")}</p>
    </div>
  </div>
</section>
<section style="padding-bottom:40px"><div class="container">{det}</div></section>
<section class="section bg-soft" id="fireproofing">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">{T("Specialist services", "خدمات متخصصة")}</span><h2>{T("Supporting capabilities", "قدرات مساندة")}</h2></div>
    <div class="mini-grid">
      {mini("brush", T("Painting Works", "أعمال الدهانات"), T("Sandblasting and painting of any type of material, with protective coatings for industrial assets.", "السفع الرملي ودهان جميع أنواع المواد، مع طلاءات واقية للأصول الصناعية."))}
      {mini("flame", T("Fireproofing Works", "أعمال الحماية من الحريق"), T("Fabrication and installation of fireproofing materials and equipment such as sprinkler control systems.", "تصنيع وتركيب مواد ومعدات الحماية من الحريق مثل أنظمة التحكم بالرشاشات."), "d1")}
      {mini("crane", T("Rigging &amp; Maintenance", "أعمال الرفع والصيانة"), T("Complex rigging including multiple heavy crane lifts, instrument installation, repair welding and forklift supply.", "أعمال رفع معقدة تشمل الرفع بعدة رافعات ثقيلة، وتركيب الأجهزة، ولحام الإصلاح، وتوفير الرافعات الشوكية."), "d2")}
      {mini("tower", T("Telecom &amp; Power Towers", "أبراج الاتصالات والكهرباء"), T("Installation of telecommunication and power supply towers across the Eastern Province.", "تركيب أبراج الاتصالات وإمداد الطاقة في أنحاء المنطقة الشرقية."))}
      {mini("building", T("Building Construction", "تشييد المباني"), T("Residential, commercial and institutional buildings including MEP and finishing works.", "المباني السكنية والتجارية والمؤسسية بما في ذلك الأعمال الكهروميكانيكية والتشطيب."), "d1")}
      {mini("coins", T("Financial Strength", "ملاءة مالية"), T("A stable, reputable financial position, ready to finance the smooth completion of projects. Bank references available on request.", "مركز مالي مستقر وموثوق قادر على تمويل إنجاز المشاريع بسلاسة، والمراجع البنكية متاحة عند الطلب."), "d2")}
    </div>
  </div>
</section>
{cta()}'''
    write("service.html", site_title(T("Services", "خدماتنا")),
          T("Civil & earth works, mechanical & piping, fabrication, electrical, steel erection, painting, fireproofing and rigging services in Saudi Arabia.",
            "الأعمال المدنية والترابية والميكانيكية والأنابيب والتصنيع والأعمال الكهربائية وتركيب الهياكل الفولاذية والدهانات والحماية من الحريق والرفع في المملكة."), body)

def page_ongoing():
    n = len(ONGOING)
    body = page_hero(T("Ongoing Projects", "المشاريع الجارية"),
                     T(f"{n} active contracts across oil, gas and pipeline works.", f"{n} عقود جارية في أعمال النفط والغاز وخطوط الأنابيب."),
                     [(T("Projects", "المشاريع"), "project.html"), (T("Ongoing", "الجارية"), None)], "hero-refinery.jpg") + f'''
<section class="section bg-soft"><div class="container">{project_rows()}</div></section>
{cta()}'''
    write("ongoing.html", site_title(T("Ongoing Projects", "المشاريع الجارية")),
          T("Hemamco's ongoing projects, with client, contract value, service and completion for each.",
            "مشاريع هممكو الجارية، مع العميل وقيمة العقد ونوع الخدمة ونسبة الإنجاز لكل مشروع."), body)

def page_projects():
    card = lambda href, img, icn, h, p, link, d="": f'<a href="{href}" class="svc-card reveal {d}" style="color:inherit"><div class="img"><img src="{PIMG(img)}" alt="" loading="lazy"><span class="icon">{ic(icn)}</span></div><div class="body"><h3>{h}</h3><p>{p}</p><span class="link-arrow">{link} {arrow()}</span></div></a>'
    n_done, n_live = len(COMPLETED), len(ONGOING)
    body = page_hero(T("Our Projects", "مشاريعنا"), T("Two decades of delivery for the Kingdom’s leading organisations.", "عقدان من الإنجاز لكبرى الجهات في المملكة."),
                     [(T("Projects", "المشاريع"), None)], "hero-desert-site.jpg") + f'''
{stats_block("section-sm bg-soft")}
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      {card("ongoing.html", "project-big-img2.jpg", "clock", T("Ongoing Projects", "المشاريع الجارية"), T(f"{n_live} active contracts, with completion shown for each.", f"{n_live} عقود جارية، مع نسبة الإنجاز لكل منها."), T("View ongoing", "عرض المشاريع الجارية"))}
      {card("completed.html", "project-big-img6.jpg", "check", T("Completed Projects", "المشاريع المنجزة"), T(f"{n_done} completed contracts since 2006. Stated values total {STATED_MILLION_TEXT} million, excluding open purchase orders.", f"{n_done} عقدًا منجزًا منذ 2006. مجموع القيم المذكورة {STATED_MILLION_TEXT} مليون، دون أوامر الشراء المفتوحة."), T("View record", "عرض السجل"), "d1")}
      {card("gallery.html", "project-big-img12.jpg", "layers", T("Project Gallery", "معرض المشاريع"), T("Photographs from our sites in Ras Tanura, Ras Al-Khair, Al-Khobar and beyond.", "صور من مواقعنا في رأس تنورة ورأس الخير والخبر وغيرها."), T("Open gallery", "فتح المعرض"), "d2")}
    </div>
  </div>
</section>
<section class="section bg-soft"><div class="container"><div class="section-head reveal"><span class="eyebrow">{T("In progress", "قيد التنفيذ")}</span><h2>{T("Ongoing projects", "المشاريع الجارية")}</h2></div>{project_rows()}</div></section>
{cta()}'''
    write("project.html", site_title(T("Projects", "المشاريع")),
          T("Hemamco projects overview — ongoing, completed and gallery.", "نظرة عامة على مشاريع هممكو — الجارية والمنجزة ومعرض الصور."), body)

def page_completed():
    rows = "".join(
        "<tr>"
        f'<td class="sl">{i}</td>'
        f"<td><strong>{lines(project)}</strong></td>"
        f"<td>{lines(client)}</td>"
        f"<td>{lines(value)}</td>"
        f"<td>{lines(service)}</td>"
        f'<td style="white-space:nowrap">{E(date(dt))}</td>'
        f'<td><span class="badge-done">{T("Completed", "منجز")}</span></td>'
        "</tr>"
        for i, (project, client, value, service, dt) in enumerate(COMPLETED, 1))
    n = len(COMPLETED)
    body = page_hero(T("Completed Projects", "المشاريع المنجزة"), T("A proven track record of delivery across the Kingdom.", "سجل حافل بالإنجازات في أنحاء المملكة."),
                     [(T("Projects", "المشاريع"), "project.html"), (T("Completed", "المنجزة"), None)], "header-canopy.jpg") + f'''
<section class="section bg-soft">
  <div class="container">
    <div class="table-wrap reveal">
      <div class="table-tools">
        <div class="count">{T(f'Showing <span data-count-for="t-completed">{n}</span> of {n} projects', f'عرض <span data-count-for="t-completed">{n}</span> من {n} مشروعًا')}</div>
        <label class="search-input">{ic("search")}<span class="sr-only">{T("Search projects", "ابحث في المشاريع")}</span><input type="search" placeholder="{T("Search project, client or service…", "ابحث بالمشروع أو العميل أو نوع الخدمة…")}" data-table-search="t-completed"></label>
      </div>
      <div class="table-scroll">
        <table class="data" id="t-completed">
          <thead><tr><th class="sl">{T("No.", "م")}</th><th>{T("Project", "المشروع")}</th><th>{T("Client", "العميل")}</th><th>{T("Contract value", "قيمة العقد")}</th><th>{T("Type of service", "نوع الخدمة")}</th><th>{T("Start date", "تاريخ البدء")}</th><th>{T("Status", "الحالة")}</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
      <div class="table-foot"><span>{T("Stated value, excluding open purchase orders", "القيمة المذكورة، دون أوامر الشراء المفتوحة")}</span><span>{T(f"{STATED_MILLION_TEXT} million", f"{STATED_MILLION_TEXT} مليون")}</span></div>
    </div>
  </div>
</section>
{cta()}'''
    write("completed.html", site_title(T("Completed Projects", "المشاريع المنجزة")),
          T("Full list of Hemamco completed projects, clients, services and contract values.", "القائمة الكاملة لمشاريع هممكو المنجزة وعملائها وخدماتها وقيم العقود."), body)

def page_gallery():
    items = "".join(f'''<a class="proj-card reveal" href="{PIMG(f"project-big-img{n}.jpg")}" data-lightbox data-caption="{L(title)} — {L(loc)}" data-cat="{cat}">
  <img src="{PIMG(f"project-img{n}.jpg")}" alt="{L(title)}" loading="lazy">
  <div class="info"><h3>{L(title)}</h3><div class="meta">{L(loc)}</div></div>
</a>''' for n, title, loc, cat in GALLERY)
    body = page_hero(T("Project Gallery", "معرض المشاريع"), T("Our teams at work on sites across the Kingdom.", "فرقنا أثناء العمل في مواقع مختلفة من المملكة."),
                     [(T("Projects", "المشاريع"), "project.html"), (T("Gallery", "المعرض"), None)], "header-dusk.jpg") + f'''
<section class="section">
  <div class="container">
    <div class="filters reveal">
      <button class="active" data-filter="all">{T("All works", "جميع الأعمال")}</button>
      <button data-filter="civil">{T("Civil", "مدنية")}</button>
      <button data-filter="mechanical">{T("Mechanical", "ميكانيكية")}</button>
      <button data-filter="steel">{T("Steel &amp; Structural", "هياكل فولاذية وإنشائية")}</button>
      <button data-filter="electrical">{T("Electrical", "كهربائية")}</button>
    </div>
    <div class="gallery">{items}</div>
  </div>
</section>
{cta()}'''
    write("gallery.html", site_title(T("Project Gallery", "معرض المشاريع")),
          T("Photo gallery of Hemamco civil, mechanical, steel and electrical works in Saudi Arabia.", "معرض صور لأعمال هممكو المدنية والميكانيكية والفولاذية والكهربائية في المملكة."), body)

def page_manpower():
    mp = ""
    for group, items in MANPOWER:
        sub = sum(q for _, q in items)
        tr = "".join(f'<tr><td>{L(n)}</td><td class="num">{q}</td></tr>' for n, q in items)
        mp += f'''<div class="table-wrap reveal">
  <div class="table-tools"><div class="count">{L(group)}</div><span class="badge-done" style="background:var(--navy-50);color:var(--navy-700)">{sub} {T("staff", "موظفًا")}</span></div>
  <table class="data"><thead><tr><th>{T("Job description", "المسمى الوظيفي")}</th><th class="num">{T("Quantity", "العدد")}</th></tr></thead><tbody>{tr}</tbody></table>
</div>'''
    body = page_hero(T("Manpower", "القوى العاملة"), T(f"A workforce of {TOTAL_STAFF:,} skilled professionals ready to mobilise.", f"قوى عاملة تضم {TOTAL_STAFF:,} من المهنيين المهرة الجاهزين للانطلاق."),
                     [(T("Resources", "الموارد"), None), (T("Manpower", "القوى العاملة"), None)], "header-steel.jpg") + f'''
<section class="section bg-soft">
  <div class="container">
    {res_tabs("manpower.html")}
    <div class="grid grid-2" style="align-items:start">{mp}</div>
    <div class="table-wrap reveal" style="margin-top:28px"><div class="table-foot"><span>{T("Total manpower", "إجمالي القوى العاملة")}</span><span>{TOTAL_STAFF:,}</span></div></div>
  </div>
</section>
{cta()}'''
    write("manpower.html", site_title(T("Manpower", "القوى العاملة")),
          T(f"Hemamco manpower list — {TOTAL_STAFF} managers, engineers, QA/QC, HSE and skilled trades.", f"القوى العاملة في هممكو — {TOTAL_STAFF} من المدراء والمهندسين ومختصي الجودة والسلامة والحرفيين المهرة."), body)

def page_equipment():
    rows = "".join(f'<tr><td><strong>{L(n)}</strong></td><td class="muted">{L(c)}</td><td class="num">{q}</td></tr>' for n, c, q in EQUIPMENT)
    body = page_hero(T("Equipment", "المعدات"), T(f"An owned fleet of {TOTAL_EQUIP} units for earthmoving, lifting, transport and site support.", f"أسطول مملوك يضم {TOTAL_EQUIP} وحدة لأعمال الحفر والرفع والنقل ودعم المواقع."),
                     [(T("Resources", "الموارد"), None), (T("Equipment", "المعدات"), None)], "header-dusk.jpg") + f'''
<section class="section bg-soft">
  <div class="container">
    {res_tabs("equipment.html")}
    <div class="table-wrap reveal">
      <div class="table-tools">
        <div class="count">{T(f'Showing <span data-count-for="t-equip">{len(EQUIPMENT)}</span> equipment types', f'عرض <span data-count-for="t-equip">{len(EQUIPMENT)}</span> نوعًا من المعدات')}</div>
        <label class="search-input">{ic("search")}<span class="sr-only">{T("Search equipment", "ابحث في المعدات")}</span><input type="search" placeholder="{T("Search equipment…", "ابحث في المعدات…")}" data-table-search="t-equip"></label>
      </div>
      <div class="table-scroll">
        <table class="data" id="t-equip"><thead><tr><th>{T("Equipment description", "وصف المعدة")}</th><th>{T("Capacity", "السعة")}</th><th class="num">{T("Quantity", "العدد")}</th></tr></thead><tbody>{rows}</tbody></table>
      </div>
      <div class="table-foot"><span>{T("Total units", "إجمالي الوحدات")}</span><span>{TOTAL_EQUIP}</span></div>
    </div>
  </div>
</section>
{cta()}'''
    write("equipment.html", site_title(T("Equipment", "المعدات")),
          T("Hemamco equipment list — dump trucks, bulldozers, loaders, graders, cranes, generators and more.", "قائمة معدات هممكو — شاحنات قلابة وجرافات ولوادر وممهدات ورافعات ومولدات وغيرها."), body)

def page_contact():
    ci = lambda icn, k, v: f'<div class="ci-item"><div class="ic">{ic(icn)}</div><div><div class="k">{k}</div>{v}</div></div>'
    opts = [T("Civil &amp; Earth Works", "الأعمال المدنية والترابية"), T("Mechanical &amp; Piping", "الأعمال الميكانيكية والأنابيب"), T("Fabrication", "التصنيع"),
            T("Steel Erection", "تركيب الهياكل الفولاذية"), T("Electrical Works", "الأعمال الكهربائية"), T("Painting &amp; Fireproofing", "الدهانات والحماية من الحريق"),
            T("Rigging &amp; Maintenance", "الرفع والصيانة"), T("General Enquiry", "استفسار عام")]
    body = page_hero(T("Contact Us", "اتصل بنا"), T("Tell us about your project — our team will respond within one business day.", "أخبرنا عن مشروعك، وسيرد فريقنا خلال يوم عمل واحد."),
                     [(T("Contact", "اتصل بنا"), None)], "khobar-tower.jpg") + f'''
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info reveal">
        <span class="eyebrow">{T("Get in touch", "تواصل معنا")}</span>
        <h3>{T("Head office — Dammam", "المقر الرئيسي — الدمام")}</h3>
        <p>{T("We work across the Eastern Province and the wider Kingdom of Saudi Arabia.", "نعمل في جميع أنحاء المنطقة الشرقية والمملكة العربية السعودية.")}</p>
        {ci("pin", T("Address", "العنوان"), f'<div class="v">{T("P.O. Box 9334, Dammam 32273<br>Kingdom of Saudi Arabia", "ص.ب 9334، الدمام 32273<br>المملكة العربية السعودية")}</div>')}
        {ci("phone", T("Phone", "الهاتف"), f'<a class="v" href="tel:+966138174333">{PHONE}</a>')}
        {ci("mail", T("Email", "البريد الإلكتروني"), '<a class="v" href="mailto:info@hemamco.com">info@hemamco.com</a>')}
        {ci("clock", T("Working hours", "ساعات العمل"), f'<div class="v">{T("Sunday – Thursday, 7:30 AM – 5:00 PM", "الأحد – الخميس، 7:30 ص – 5:00 م")}</div>')}
      </div>
      <form class="form reveal d1" action="{P}contact.php" method="post" data-ajax data-fail="{T("Sorry, the message could not be sent. Please email info@hemamco.com.", "عذرًا، تعذّر إرسال الرسالة. يرجى مراسلتنا على info@hemamco.com.")}">
        <input type="hidden" name="lang" value="{LANG}">
        <h3>{T("Request a quote", "اطلب عرض سعر")}</h3>
        <p style="margin-bottom:26px">{T("Share a few details and we’ll get back to you.", "شاركنا بعض التفاصيل وسنعود إليك.")}</p>
        <div class="row">
          <div class="field"><label for="f-name">{T("Full name", "الاسم الكامل")}</label><input id="f-name" name="name" required autocomplete="name"></div>
          <div class="field"><label for="f-email">{T("Email", "البريد الإلكتروني")}</label><input id="f-email" name="email" type="email" dir="ltr" required autocomplete="email"></div>
        </div>
        <div class="row">
          <div class="field"><label for="f-phone">{T("Phone", "الهاتف")}</label><input id="f-phone" name="phone" type="tel" dir="ltr" required autocomplete="tel"></div>
          <div class="field"><label for="f-subject">{T("Service", "الخدمة")}</label>
            <select id="f-subject" name="subject" required>
              <option value="">{T("Select a service…", "اختر الخدمة…")}</option>
              {"".join(f"<option>{o}</option>" for o in opts)}
            </select></div>
        </div>
        <div class="field"><label for="f-msg">{T("Project details", "تفاصيل المشروع")}</label><textarea id="f-msg" name="message" required></textarea></div>
        <button type="submit" class="btn btn-primary">{T("Send message", "إرسال الرسالة")} {arrow()}</button>
        <div class="form-msg" role="status"></div>
      </form>
    </div>
    <div class="map reveal">
      <iframe title="{T("Hemamco location — Dammam", "موقع هممكو — الدمام")}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Dammam,Saudi+Arabia&amp;hl={LANG}&amp;output=embed"></iframe>
    </div>
  </div>
</section>'''
    write("contact.html", site_title(T("Contact Us", "اتصل بنا")),
          T("Contact Hemamco Company Limited, Dammam — +966 13 817 4333, info@hemamco.com.", "تواصل مع شركة هممكو المحدودة، الدمام — ‎+966 13 817 4333، info@hemamco.com."), body)

PAGES = [page_home, page_about, page_safety, page_quality, page_org, page_services, page_ongoing,
         page_projects, page_completed, page_gallery, page_manpower, page_equipment, page_contact]

for LANG, P in (("en", ""), ("ar", "../")):
    for fn in PAGES:
        fn()
print("staff", TOTAL_STAFF, "equip", TOTAL_EQUIP, "completed", len(COMPLETED), "ongoing", len(ONGOING), "stated_million", STATED_MILLION_TEXT)
