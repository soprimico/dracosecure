"""Generate the static pages for DracoSecure.

Edit this file, then run `python3 gen.py` to rebuild index.html,
services.html, pricing.html and contact.html.
"""

import json
from html import escape

BRAND = "DracoSecure"
DOMAIN = "www.dracosecure.com"
BASE = f"https://{DOMAIN}/"
EMAIL = "hello@dracosecure.com"

PAGES = [
    (
        "index.html",
        "Managed WordPress maintenance and security",
        "DracoSecure provides managed WordPress maintenance, security and 24/7 monitoring for businesses that depend on their website.",
    ),
    (
        "services.html",
        "WordPress maintenance and security services",
        "Explore DracoSecure WordPress services: updates, firewall, backups, malware remediation, monitoring and WooCommerce performance.",
    ),
    (
        "pricing.html",
        "Plans and pricing",
        "Transparent monthly pricing for managed WordPress maintenance and security. Plans from €97/month, or €77/month billed annually.",
    ),
    (
        "contact.html",
        "Contact and security audit booking",
        "Contact DracoSecure to book a WordPress security audit or a managed maintenance plan. We reply within one business day.",
    ),
]

NAV_ITEMS = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("pricing.html", "Pricing"),
    ("contact.html", "Contact"),
]


def nav_for(filename):
    return "".join(
        f'<a href="{f}"' + (' aria-current="page"' if f == filename else "") + f">{label}</a>"
        for f, label in NAV_ITEMS
    )


def footer_links():
    return "".join(f'<a href="{f}">{label}</a>' for f, label in NAV_ITEMS)


def page(filename, body):
    meta = dict((f, (title, description)) for f, title, description in PAGES)
    title, description = meta[filename]
    full_title = f"{title} | {BRAND}"
    url = BASE if filename == "index.html" else BASE + filename
    e = escape

    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": full_title,
        "description": description,
        "url": url,
        "inLanguage": "en",
        "publisher": {
            "@type": "Organization",
            "name": BRAND,
            "url": BASE,
            "email": EMAIL,
            "logo": BASE + "assets/logo.png",
        },
    }
    structured_data = json.dumps(schema, indent=2, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#070708">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/logo.png">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(full_title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{BASE}assets/logo.png">
<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&amp;family=Barlow:wght@400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">
{structured_data}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
<div class="w nav">
<a class="brand" href="index.html"><img src="assets/logo.png" alt="">{BRAND}</a>
<button class="tg" id="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav id="site-nav">{nav_for(filename)}<a class="btn sm" href="contact.html">Book an audit</a></nav>
</div>
</header>
<main id="main">
{body}
</main>
<footer>
<div class="w">
<div class="fg">
<div><a class="brand" href="index.html"><img src="assets/logo.png" alt="">{BRAND}</a><p>Managed WordPress maintenance and security for businesses that depend on their website.</p></div>
<div><h4>Pages</h4>{footer_links()}</div>
<div><h4>Services</h4><a href="services.html">WordPress management</a><a href="services.html">WordPress security</a><a href="services.html">Backups and recovery</a></div>
<div><h4>Contact</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="contact.html">Book a security audit</a></div>
</div>
<div class="copy"><span>© 2026 {BRAND}. All rights reserved.</span><span>Specialists in WordPress security.</span></div>
</div>
</footer>
<script src="script.js" defer></script>
</body>
</html>
'''
    with open(filename, "w", encoding="utf-8") as handle:
        handle.write(html)


CTA = '''<section><div class="w"><div class="cb">
<h2>Protect your WordPress investment</h2>
<p>Managed plans start at €97 per month, or €77 per month with annual billing. We onboard a limited number of new clients each month to keep response times predictable.</p>
<a class="btn" href="pricing.html">View plans and pricing</a>
</div></div></section>'''

HOME_CARDS = [
    (
        "WordPress management",
        "Scheduled updates of WordPress core, themes and plugins, tested on a staging copy before release.",
    ),
    (
        "WordPress security",
        "Web application firewall, wp-admin hardening, login protection and continuous vulnerability scanning.",
    ),
    (
        "Backups and recovery",
        "Off-site backups of files and database, with verified restores and one-step rollback.",
    ),
    (
        "24/7 monitoring",
        "Uptime, file integrity and blocklist monitoring with immediate alerts to your team.",
    ),
    (
        "Malware remediation",
        "Complete cleanup of compromised WordPress sites, root-cause analysis and post-incident hardening.",
    ),
    (
        "Performance and WooCommerce",
        "Caching, database optimization and Core Web Vitals tuning, including WooCommerce stores.",
    ),
]

HOME = '''
<div class="hero"><div class="w hg"><div>
<span class="pill">WordPress security &amp; maintenance specialists</span>
<h1>Managed WordPress. <em>Fully protected.</em></h1>
<p class="sub">DracoSecure maintains, secures and monitors your company’s WordPress website, so your business stays online and your customers’ data stays safe.</p>
<div class="cta"><a class="btn" href="pricing.html">View plans &amp; pricing</a><a class="btn o" href="contact.html">Book a security audit</a></div>
<p class="note">Plans from €97/month · €77/month with annual billing</p>
</div>
<div class="shield" aria-label="Example of blocked activity"><img src="assets/logo.png" alt="DracoSecure shield"><ul class="feed">
<li><span><b>Blocked</b> brute force on wp-login.php</span><i>03:12</i></li>
<li><span><b>Blocked</b> SQL injection on /?s=</span><i>03:47</i></li>
<li><span><b>Removed</b> malware from a plugin</span><i>04:05</i></li>
<li><span><b>Patched</b> vulnerable plugin</span><i>06:30</i></li>
<li><span><b>Verified</b> daily backup</span><i>07:00</i></li>
</ul></div></div></div>
<div class="w"><div class="strip"><span>Core updates</span><span>Plugin patching</span><span>Firewall</span><span>Backups</span><span>Monitoring</span></div></div>
<section><div class="w">
<h2>Complete WordPress care</h2>
<p class="lead">One specialist team responsible for the stability and security of your site.</p>
<div class="g3">{cards}</div>
</div></section>
<section class="alt"><div class="w">
<h2>Our process</h2>
<p class="lead">A structured engagement, from first assessment to ongoing management.</p>
<div class="steps">
<div class="step"><h3>Audit</h3><p>A paid security assessment of your WordPress installation, with a prioritized remediation report.</p></div>
<div class="step"><h3>Secure</h3><p>We resolve critical issues, harden the installation and deploy backups and monitoring.</p></div>
<div class="step"><h3>Maintain</h3><p>Ongoing updates, monitoring and monthly reporting under a managed plan.</p></div>
</div></div></section>
<section><div class="w"><div class="band">
<div><strong>24/7</strong><span>monitoring on every plan above Essential</span></div>
<div><strong>&lt; 1 h</strong><span>incident response on Professional and Business</span></div>
<div><strong>Daily</strong><span>off-site backups on Professional and Business</span></div>
<div><strong>30 days</strong><span>satisfaction guarantee on every plan</span></div>
</div></div></section>
<section class="alt"><div class="w">
<h2>Why businesses choose DracoSecure</h2>
<p class="lead">The reasons our clients entrust their WordPress sites to us.</p>
<div class="g3">
<div class="card"><h3>WordPress only</h3><p>We do one thing. Our processes, tooling and engineers are dedicated exclusively to WordPress.</p></div>
<div class="card"><h3>Predictable cost</h3><p>A fixed monthly fee replaces unplanned emergency invoices after an incident.</p></div>
<div class="card"><h3>Accountable service</h3><p>Defined response times, monthly reports and a named technical contact on our higher plans.</p></div>
</div></div></section>{cta}'''.format(
    cards="".join(f'<div class="card"><h3>{title}</h3><p>{text}</p></div>' for title, text in HOME_CARDS),
    cta=CTA,
)

SERVICES = [
    (
        "WordPress management",
        ["Core, theme and plugin updates", "Staging tests before each release", "PHP and database maintenance", "Monthly maintenance report"],
    ),
    (
        "WordPress security",
        ["Web application firewall", "Brute-force and bot blocking", "Two-factor authentication and hardening", "XML-RPC and wp-admin protection"],
    ),
    (
        "Backups and recovery",
        ["Daily off-site backups", "Weekly restore verification", "One-step rollback", "Disaster recovery plan"],
    ),
    (
        "24/7 monitoring",
        ["Uptime checks every minute", "File integrity monitoring", "Alerts by email or Slack", "Blocklist and reputation checks"],
    ),
    (
        "Malware remediation",
        ["Full infection removal", "Root-cause analysis", "Search engine warning removal", "Post-incident hardening"],
    ),
    (
        "Performance and WooCommerce",
        ["Caching and image optimization", "Core Web Vitals tuning", "WooCommerce checkout protection", "Multisite support on Business"],
    ),
]

SERVICES_HTML = '''<div class="page-hero"><div class="w">
<h1>WordPress services</h1>
<p>Management, security and recovery for WordPress, delivered by a dedicated specialist team.</p>
</div></div>
<section><div class="w"><div class="g3">{cards}</div></div></section>{cta}'''.format(
    cards="".join(
        "<div class=\"card\"><h3>{}</h3><ul>{}</ul></div>".format(
            title, "".join(f"<li>{item}</li>" for item in items)
        )
        for title, items in SERVICES
    ),
    cta=CTA,
)


def plan(name, description, monthly, annual, daily_month, daily_annual, features, button, featured=False):
    tag = '<span class="tag">Most selected</span>' if featured else ""
    classes = "plan hot" if featured else "plan"
    button_class = "btn" if featured else "btn o"
    return f'''<div class="{classes}">
{tag}<h3>{name}</h3>
<p class="subtle">{description}</p>
<div class="price"><span data-m="x" data-mo="{monthly}" data-a="{annual}">{monthly}</span><small> per month</small></div>
<p class="pd"><span data-m="x" data-mo="{daily_month}" data-a="{daily_annual}">{daily_month}</span></p>
<ul>{''.join(f'<li>{item}</li>' for item in features)}</ul>
<a class="{button_class}" href="contact.html">{button}</a>
</div>'''


COMPARE = [
    ("Updates", "Monthly", "Weekly", "Daily"),
    ("Backups", "Weekly", "Daily", "Daily, off-site"),
    ("Firewall", "Standard", "Advanced", "Advanced"),
    ("24/7 monitoring", "Not included", "Included", "Included"),
    ("Malware remediation", "Not included", "Included", "Included"),
    ("WordPress sites", "1", "1", "Up to 10"),
    ("Support", "Email", "Priority, within 1 h", "Dedicated contact, within 1 h"),
]

def compare_cell(cell):
    kind = "y" if cell == "Included" else "n" if cell == "Not included" else ""
    return f'<td class="{kind}">{cell}</td>' if kind else f"<td>{cell}</td>"


compare_rows = "".join(
    f"<tr><td>{row[0]}</td>" + "".join(compare_cell(cell) for cell in row[1:]) + "</tr>"
    for row in COMPARE
)

VALUE_ITEMS = [
    ("Weekly updates with staging tests", "€80"),
    ("Advanced WordPress firewall", "€60"),
    ("Daily off-site backups", "€45"),
    ("24/7 monitoring and alerts", "€70"),
    ("Malware remediation coverage", "€90"),
    ("Priority support", "€67"),
]

value_rows = "".join(f"<tr><td>{item}</td><td>{price}</td></tr>" for item, price in VALUE_ITEMS)

FAQ = [
    (
        "Do I need to change my hosting provider?",
        "No. We work with your current host and recommend a migration only when it is technically justified.",
    ),
    (
        "Can I cancel at any time?",
        "Monthly plans can be cancelled with 30 days’ notice. Annual plans are covered by our 30-day satisfaction guarantee.",
    ),
    (
        "What happens if my site is already compromised?",
        "We begin with a malware remediation engagement, then transition your site to the plan that fits your needs.",
    ),
    (
        "Will updates affect my site’s functionality?",
        "Every update is tested on a staging copy first, and a rollback point is always available.",
    ),
    (
        "Is the security audit credited against a plan?",
        "Yes. The audit fee is deducted from your first annual plan invoice.",
    ),
]

PRICING_HTML = '''<div class="page-hero"><div class="w">
<h1>Plans and pricing</h1>
<p>Clear monthly pricing for professional WordPress management and security. Every plan includes a 30-day satisfaction guarantee.</p>
</div></div>
<section><div class="w">
<div class="tgl" role="group" aria-label="Billing period"><button class="on" type="button" data-m="m" aria-pressed="true">Monthly</button><button type="button" data-m="a" aria-pressed="false">Annual <span class="save">Save 20%</span></button></div>
<div class="g3">{plans}</div>
<p class="note center">Prices exclude VAT. Annual plans are billed once per year.</p>
</div></section>
<section class="alt"><div class="w">
<h2>The value of Professional</h2>
<p class="lead">What the same protection would cost if purchased as separate services.</p>
<div class="scroll"><table class="vs">{value_rows}
<tr class="tot"><td>Total if purchased separately</td><td><span class="was">€412 per month</span></td></tr>
<tr class="tot"><td>DracoSecure Professional</td><td>€197 per month</td></tr>
</table></div>
</div></section>
<section><div class="w">
<h2>Compare plans</h2>
<p class="lead">A detailed view of what each plan includes.</p>
<div class="scroll"><table><tr><th></th><th>Essential</th><th>Professional</th><th>Business</th></tr>{compare_rows}</table></div>
</div></section>
<section class="alt"><div class="w"><div class="card">
<h3>WordPress Security Audit</h3>
<p>A one-time professional assessment of your WordPress installation, with a prioritized remediation report. <b class="k">€297</b> one-time, credited in full against any annual plan.</p>
<p style="margin-top:20px"><a class="btn" href="contact.html">Book the audit</a></p>
</div></div></section>
<section><div class="w">
<h2>Frequently asked questions</h2>
<p class="lead">Answers to common questions before you begin.</p>
{faq}
</div></section>'''.format(
    plans="".join(
        [
            plan(
                "Essential",
                "For single company websites",
                "€97",
                "€77",
                "Less than €3.30 per day",
                "Less than €2.60 per day, billed annually",
                ["Monthly updates", "Weekly backups", "Standard firewall", "Email support"],
                "Select Essential",
            ),
            plan(
                "Professional",
                "For businesses that depend on their site",
                "€197",
                "€157",
                "Less than €6.60 per day",
                "Less than €5.30 per day, billed annually",
                [
                    "Weekly updates with staging tests",
                    "Daily off-site backups",
                    "Advanced firewall",
                    "24/7 monitoring",
                    "Malware remediation included",
                    "Response within one hour",
                ],
                "Select Professional",
                featured=True,
            ),
            plan(
                "Business",
                "For stores and multi-site operations",
                "€497",
                "€397",
                "Less than €16.60 per day",
                "Less than €13.30 per day, billed annually",
                [
                    "Up to 10 WordPress sites",
                    "Daily updates and off-site backups",
                    "Response within one hour",
                    "Monthly security reports",
                    "Dedicated technical contact",
                ],
                "Select Business",
            ),
        ]
    ),
    value_rows=value_rows,
    compare_rows=compare_rows,
    faq="".join(f"<details><summary>{question}</summary><p>{answer}</p></details>" for question, answer in FAQ),
)

CONTACT_HTML = f'''<div class="page-hero"><div class="w">
<h1>Contact</h1>
<p>Tell us about your WordPress site. A member of our team will respond within one business day.</p>
</div></div>
<section><div class="w ct">
<div class="info">
<h2>Book your engagement</h2>
<p>Select a plan or book a WordPress security audit. We will confirm scope and next steps by email.</p>
<p><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><b>Response time</b>Within one business day</p>
<p><b>Compromised site</b>Select the emergency option for priority handling.</p>
</div>
<form id="f" data-email="{EMAIL}">
<label for="n">Full name</label><input id="n" name="n" required autocomplete="name">
<label for="e">Work email</label><input id="e" type="email" name="e" required autocomplete="email">
<label for="u">WordPress site address</label><input id="u" name="u" placeholder="https://yourcompany.com" required>
<label for="s">Service of interest</label><select id="s" name="s"><option>Essential plan</option><option>Professional plan</option><option>Business plan</option><option>WordPress Security Audit</option><option>Emergency malware remediation</option></select>
<label for="m">Additional details</label><textarea id="m" name="m" rows="4"></textarea>
<button class="btn" type="submit">Submit request</button>
<p class="form-note">Submitting opens your email app with the request ready to send. We do not store form data on this site.</p>
<p id="ok" class="status" role="status" hidden>Your email app will open with the request ready to send.</p>
</form>
</div></section>'''

page("index.html", HOME)
page("services.html", SERVICES_HTML)
page("pricing.html", PRICING_HTML)
page("contact.html", CONTACT_HTML)

print("Generated: index.html, services.html, pricing.html, contact.html")
