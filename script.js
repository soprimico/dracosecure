const toggle = document.getElementById('nav-toggle');
const nav = document.getElementById('site-nav');

function setMenu(open) {
  if (!toggle || !nav) return;
  nav.classList.toggle('open', open);
  toggle.setAttribute('aria-expanded', String(open));
  toggle.textContent = open ? 'Close' : 'Menu';
}

toggle?.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));

document.addEventListener('click', event => {
  if (nav?.classList.contains('open') && !nav.contains(event.target) && !toggle?.contains(event.target)) {
    setMenu(false);
  }
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) {
    setMenu(false);
    toggle?.focus();
  }
});

const form = document.getElementById('f');
form?.addEventListener('submit', event => {
  event.preventDefault();

  const data = new FormData(form);
  const name = String(data.get('n') || '').trim();
  const body = [
    `Name: ${name}`,
    `Email: ${String(data.get('e') || '').trim()}`,
    `WordPress site: ${String(data.get('u') || '').trim()}`,
    `Service: ${String(data.get('s') || '').trim()}`,
    '',
    String(data.get('m') || '').trim(),
  ].join('\n');

  const subject = `Enquiry from ${name} — DracoSecure`;
  const address = form.dataset.email || 'hello@dracosecure.com';
  window.location.href = `mailto:${address}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

  const status = document.getElementById('ok');
  if (status) status.hidden = false;
});

const billingButtons = document.querySelectorAll('.tgl button');
billingButtons.forEach(button => {
  button.addEventListener('click', () => {
    const annual = button.dataset.m === 'a';
    billingButtons.forEach(other => {
      const active = other === button;
      other.classList.toggle('on', active);
      other.setAttribute('aria-pressed', String(active));
    });

    document.querySelectorAll('[data-m]').forEach(element => {
      if (element.tagName !== 'BUTTON') {
        element.textContent = annual ? element.dataset.a : element.dataset.mo;
      }
    });
  });
});
