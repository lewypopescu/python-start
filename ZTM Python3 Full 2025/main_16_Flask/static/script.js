console.log("Butterfly Project JS loaded 🦋");

document.addEventListener("DOMContentLoaded", () => {
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");
  const saved = localStorage.getItem("theme");
  if (saved) root.setAttribute("data-theme", saved);
  toggle?.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "dark" ? "" : "dark";
    next
      ? root.setAttribute("data-theme", next)
      : root.removeAttribute("data-theme");
    next
      ? localStorage.setItem("theme", next)
      : localStorage.removeItem("theme");
  });

  const timeline = document.getElementById("timeline");
  if (!timeline) return;

  fetch("/api/stages")
    .then((r) => r.json())
    .then((items) => {
      timeline.innerHTML = items
        .map(
          (x) => `
        <article class="card">
          <h3>${x.emoji} ${x.key}</h3>
          <p>${x.desc}</p>
          <div class="actions">
            <button class="btn open-modal"
                    data-img="${x.img}"
                    data-cap="${x.emoji} ${x.key} — ${x.fact}">
              Show fact
            </button>
          </div>
        </article>
      `
        )
        .join("");
    })
    .then(() => initModal())
    .catch((err) => {
      console.error(err);
      timeline.innerHTML = `<p>Could not load stages right now.</p>`;
    });
});

function initModal() {
  const modal = document.getElementById("modal");
  const img = document.getElementById("modal-img");
  const cap = document.getElementById("modal-cap");
  const closeBtn = modal.querySelector(".modal__close");
  const backdrop = modal.querySelector(".modal__backdrop");

  const open = (src, caption) => {
    img.src = src;
    img.alt = caption;
    cap.textContent = caption;
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    closeBtn.focus();
  };

  const close = () => {
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    img.src = "";
  };

  document.addEventListener("click", (e) => {
    const btn = e.target.closest(".open-modal");
    if (btn) {
      open(btn.dataset.img, btn.dataset.cap);
    }
    if (e.target === backdrop || e.target === closeBtn) close();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.getAttribute("aria-hidden") === "false")
      close();
  });
}
