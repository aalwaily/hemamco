/* HEMAMCO — site behaviour (no dependencies) */
(function () {
  "use strict";
  var body = document.body;

  // Sticky header shadow + back-to-top
  var header = document.querySelector(".site-header");
  var toTop = document.querySelector(".to-top");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("scrolled", y > 10);
    if (toTop) toTop.classList.toggle("show", y > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0 }); });

  // Mobile menu
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      // open the menu directly under the header, wherever the page is scrolled
      if (header) document.documentElement.style.setProperty("--nav-top", header.getBoundingClientRect().bottom + "px");
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  function closeMenu() {
    body.classList.remove("nav-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });
  document.querySelectorAll(".nav-wrap a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (!a.parentElement.classList.contains("has-dd")) closeMenu();
    });
  });
  document.querySelectorAll(".nav > li.has-dd > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width: 960px)").matches) {
        e.preventDefault();
        a.parentElement.classList.toggle("open");
      }
    });
  });

  // Hero slider
  var slides = document.querySelectorAll(".hero-slide");
  var dots = document.querySelectorAll(".hero-dots button");
  var texts = document.querySelectorAll(".hero-text");
  if (slides.length > 1) {
    var cur = 0, timer;
    function go(n) {
      slides[cur].classList.remove("active");
      if (dots[cur]) dots[cur].classList.remove("active");
      if (texts[cur]) texts[cur].hidden = true;
      cur = (n + slides.length) % slides.length;
      slides[cur].classList.add("active");
      if (dots[cur]) dots[cur].classList.add("active");
      if (texts[cur]) texts[cur].hidden = false;
    }
    function start() { clearInterval(timer); timer = setInterval(function () { go(cur + 1); }, 7000); }
    dots.forEach(function (d, i) { d.addEventListener("click", function () { go(i); start(); }); });
    start();
  }

  // Reveal on scroll
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -60px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // Counters
  var counters = document.querySelectorAll("[data-count]");
  function runCounter(el) {
    var to = parseInt(el.getAttribute("data-count"), 10), t0 = null, dur = 1600;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))).toLocaleString("en-US");
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { runCounter(en.target); co.unobserve(en.target); }
      });
    }, { threshold: .4 });
    counters.forEach(function (el) { co.observe(el); });
  }

  // Table search
  document.querySelectorAll("[data-table-search]").forEach(function (input) {
    var table = document.getElementById(input.getAttribute("data-table-search"));
    var countEl = document.querySelector("[data-count-for='" + table.id + "']");
    var rows = table.tBodies[0].rows;
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase(), shown = 0;
      for (var i = 0; i < rows.length; i++) {
        var hit = rows[i].textContent.toLowerCase().indexOf(q) > -1;
        rows[i].style.display = hit ? "" : "none";
        if (hit) shown++;
      }
      if (countEl) countEl.textContent = shown;
    });
  });

  // Gallery filter
  var filterBtns = document.querySelectorAll(".filters button");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      filterBtns.forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var f = btn.getAttribute("data-filter");
      document.querySelectorAll(".gallery .proj-card").forEach(function (c) {
        c.classList.toggle("hide", f !== "all" && (c.getAttribute("data-cat") || "").indexOf(f) === -1);
      });
    });
  });

  // Lightbox
  var lbLinks = Array.prototype.slice.call(document.querySelectorAll("[data-lightbox]"));
  if (lbLinks.length) {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.innerHTML =
      '<button class="lb-close" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>' +
      '<button class="lb-prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>' +
      '<figure style="margin:0"><img alt=""><figcaption></figcaption></figure>' +
      '<button class="lb-next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></button>';
    body.appendChild(lb);
    var lbImg = lb.querySelector("img"), lbCap = lb.querySelector("figcaption"), idx = 0;
    function visible() { return lbLinks.filter(function (a) { return a.offsetParent !== null; }); }
    function show(i) {
      var list = visible(); if (!list.length) return;
      idx = (i + list.length) % list.length;
      lbImg.src = list[idx].getAttribute("href");
      lbCap.textContent = list[idx].getAttribute("data-caption") || "";
    }
    lbLinks.forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        show(visible().indexOf(a));
        lb.classList.add("open");
      });
    });
    function close() { lb.classList.remove("open"); }
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
  }

  // Contact / quote form -> contact.php (returns {type, msg})
  document.querySelectorAll("form[data-ajax]").forEach(function (form) {
    var msg = form.querySelector(".form-msg");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var btn = form.querySelector("[type=submit]");
      btn.disabled = true;
      msg.className = "form-msg";
      fetch(form.getAttribute("action"), { method: "POST", body: new FormData(form) })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          msg.textContent = res.msg;
          msg.className = "form-msg " + (res.type === "success" ? "ok" : "err");
          if (res.type === "success") form.reset();
        })
        .catch(function () {
          msg.textContent = form.getAttribute("data-fail") || "Sorry, the message could not be sent. Please email info@hemamco.com.";
          msg.className = "form-msg err";
        })
        .then(function () { btn.disabled = false; });
    });
  });

  var yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();
})();
