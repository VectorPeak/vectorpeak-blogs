(() => {
  const BEIAN_TEXT = "宁ICP备2026000657号";
  const BEIAN_URL = "https://beian.miit.gov.cn/";
  const GITHUB_URL = "https://github.com/VectorPeak";
  const WECHAT_QR_URL = "/images/contact/wechat-qr.jpg";

  function ensureStyles() {
    if (document.getElementById("vectorpeak-footer-contact-style")) return;

    const style = document.createElement("style");
    style.id = "vectorpeak-footer-contact-style";
    style.textContent = `
      .vectorpeak-footer-contact {
        display: inline-flex;
        align-items: center;
        gap: 10px;
      }

      .vectorpeak-footer-contact a,
      .vectorpeak-footer-contact button {
        color: rgb(107, 114, 128) !important;
        opacity: 0.48;
      }

      .vectorpeak-footer-contact a:hover,
      .vectorpeak-footer-contact button:hover {
        opacity: 0.9;
      }

      .vectorpeak-footer-contact a {
        display: inline-flex !important;
        align-items: center;
        justify-content: center;
        width: 18px !important;
        height: 18px !important;
      }

      .vectorpeak-footer-contact svg {
        width: 18px !important;
        height: 18px !important;
        color: currentColor !important;
        fill: currentColor !important;
      }

      .vectorpeak-footer-contact svg * {
        fill: currentColor !important;
      }

      .vectorpeak-footer-wechat {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 18px;
        height: 18px;
        border: 0;
        padding: 0;
        background: transparent;
        cursor: pointer;
      }

      footer#footer a[href*="mintlify.com"],
      footer a[href*="mintlify.com"] {
        opacity: 0.48;
      }

      footer#footer a[href*="mintlify.com"]:hover,
      footer a[href*="mintlify.com"]:hover {
        opacity: 0.9;
      }

      .vectorpeak-footer-beian {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        display: inline-flex;
        align-items: center;
        font-size: 14px;
        line-height: 20px;
        text-decoration: none;
        opacity: 0.48;
        white-space: nowrap;
      }

      .vectorpeak-footer-beian:hover {
        opacity: 0.9;
      }

      .vectorpeak-wechat-modal[hidden] {
        display: none;
      }

      .vectorpeak-wechat-modal {
        position: fixed;
        inset: 0;
        z-index: 2147483647;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 24px;
      }

      .vectorpeak-wechat-backdrop {
        position: absolute;
        inset: 0;
        background: rgba(15, 23, 42, 0.42);
        backdrop-filter: blur(3px);
      }

      .vectorpeak-wechat-dialog {
        position: relative;
        width: min(360px, 100%);
        border-radius: 16px;
        background: white;
        padding: 22px;
        box-shadow: 0 24px 60px rgba(15, 23, 42, 0.22);
        text-align: center;
      }

      .dark .vectorpeak-wechat-dialog {
        background: rgb(17, 24, 39);
      }

      .vectorpeak-wechat-close {
        position: absolute;
        top: 10px;
        right: 10px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        border: 0;
        border-radius: 999px;
        background: transparent;
        color: inherit;
        cursor: pointer;
        font-size: 20px;
        line-height: 1;
        opacity: 0.55;
      }

      .vectorpeak-wechat-close:hover {
        background: rgba(148, 163, 184, 0.16);
        opacity: 0.9;
      }

      .vectorpeak-wechat-title {
        margin: 4px 36px 14px;
        font-size: 16px;
        font-weight: 600;
        color: rgb(17, 24, 39);
      }

      .dark .vectorpeak-wechat-title {
        color: white;
      }

      .vectorpeak-wechat-qr {
        display: block;
        width: min(280px, 100%);
        height: auto;
        margin: 0 auto;
        border-radius: 12px;
      }
    `;
    document.head.appendChild(style);
  }

  function createWechatIcon() {
    const icon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    icon.setAttribute("viewBox", "0 0 24 24");
    icon.setAttribute("width", "18");
    icon.setAttribute("height", "18");
    icon.setAttribute("aria-hidden", "true");
    icon.innerHTML = `
      <path fill="currentColor" d="M9.7 4.5C5.5 4.5 2 7.3 2 10.8c0 2 1.1 3.8 2.8 4.9l-.7 2.1 2.5-1.2c.9.3 1.9.5 3.1.5h.5c-.2-.6-.4-1.2-.4-1.9 0-3.2 3.2-5.8 7.1-5.8h.5C16.6 6.6 13.5 4.5 9.7 4.5Zm-2.6 4.9c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1Zm5.2 0c-.6 0-1-.4-1-1s.4-1 1-1 1 .4 1 1-.4 1-1 1Zm4.5 1.4c-3.1 0-5.6 2-5.6 4.5s2.5 4.5 5.6 4.5c.8 0 1.6-.1 2.3-.4l2 1-.6-1.7c1.3-.9 2.1-2.1 2.1-3.5 0-2.4-2.6-4.4-5.8-4.4Zm-1.8 3.7c-.5 0-.8-.3-.8-.8s.3-.8.8-.8.8.3.8.8-.3.8-.8.8Zm3.6 0c-.5 0-.8-.3-.8-.8s.3-.8.8-.8.8.3.8.8-.3.8-.8.8Z"/>
    `;
    return icon;
  }

  function ensureModal() {
    let modal = document.getElementById("vectorpeak-wechat-modal");
    if (modal) return modal;

    modal = document.createElement("div");
    modal.id = "vectorpeak-wechat-modal";
    modal.className = "vectorpeak-wechat-modal";
    modal.hidden = true;
    modal.innerHTML = `
      <div class="vectorpeak-wechat-backdrop" data-wechat-close></div>
      <div class="vectorpeak-wechat-dialog" role="dialog" aria-modal="true" aria-labelledby="vectorpeak-wechat-title">
        <button class="vectorpeak-wechat-close" type="button" aria-label="关闭微信二维码" data-wechat-close>×</button>
        <div id="vectorpeak-wechat-title" class="vectorpeak-wechat-title">微信联系</div>
        <img class="vectorpeak-wechat-qr" src="${WECHAT_QR_URL}" alt="微信二维码" />
      </div>
    `;
    modal.addEventListener("click", (event) => {
      if (event.target instanceof HTMLElement && event.target.dataset.wechatClose !== undefined) {
        modal.hidden = true;
      }
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") modal.hidden = true;
    });
    document.body.appendChild(modal);
    return modal;
  }

  function enhanceFooter() {
    ensureStyles();

    const footer = document.querySelector("footer#footer, footer");
    if (!footer) return;

    const githubLink = footer.querySelector(`a[href="${GITHUB_URL}"]`);
    if (!githubLink || githubLink.dataset.vectorpeakFooter === "true") return;

    const container = document.createElement("span");
    container.className = "vectorpeak-footer-contact";

    githubLink.dataset.vectorpeakFooter = "true";
    githubLink.title = "GitHub";
    githubLink.ariaLabel = "GitHub";

    const wechatButton = document.createElement("button");
    wechatButton.type = "button";
    wechatButton.className = "vectorpeak-footer-wechat";
    wechatButton.title = "微信二维码";
    wechatButton.ariaLabel = "微信二维码";
    wechatButton.appendChild(createWechatIcon());
    wechatButton.addEventListener("click", () => {
      ensureModal().hidden = false;
    });

    footer.style.position = "relative";

    githubLink.parentNode.insertBefore(container, githubLink);
    container.append(githubLink, wechatButton);

    if (!footer.querySelector(".vectorpeak-footer-beian")) {
      const beianLink = document.createElement("a");
      beianLink.className = "vectorpeak-footer-beian";
      beianLink.href = BEIAN_URL;
      beianLink.target = "_blank";
      beianLink.rel = "noopener noreferrer";
      beianLink.textContent = BEIAN_TEXT;
      beianLink.title = BEIAN_TEXT;
      beianLink.ariaLabel = BEIAN_TEXT;
      footer.appendChild(beianLink);
    }
  }

  enhanceFooter();
  document.addEventListener("DOMContentLoaded", enhanceFooter);

  const observer = new MutationObserver(enhanceFooter);
  observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
  });
})();
