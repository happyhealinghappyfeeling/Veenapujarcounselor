// =============== Navbar Scroll Highlight ===============
let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll(".navbar a");

window.onscroll = () => {
  let top = window.scrollY;

  sections.forEach((sec) => {
    let offset = sec.offsetTop - 150;
    let height = sec.offsetHeight;
    let id = sec.getAttribute("id");

    if (top >= offset && top < offset + height) {
      navLinks.forEach((link) => {
        link.classList.remove("active");
        document
          .querySelector(`.navbar a[href*=${id}]`)
          .classList.add("active");
      });
    }
  });

  // Sticky Header
  let header = document.querySelector(".header");
  header.classList.toggle("sticky", window.scrollY > 100);

  // Scroll-to-Top button visibility
  let topBtn = document.querySelector(".top");
  topBtn.classList.toggle("show", window.scrollY > 500);
};

// =============== Smooth Scroll Navigation ===============
document.querySelectorAll(".navbar a").forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector(link.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// =============== Scroll-to-Top Button ===============
const scrollTopBtn = document.querySelector(".top");
scrollTopBtn.addEventListener("click", (e) => {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: "smooth" });
});

// =============== Typed.js Animation ===============
const typed = new Typed(".logo", {
  strings: ["happy healing happy feeling", "Veena Pujar", "Behavioural Counseling Professional"],
  typeSpeed: 90,
  backSpeed: 60,
  backDelay: 1200,
  loop: true,
});

// =============== Reveal Animation (Scroll Animation) ===============
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("reveal");
      }
    });
  },
  { threshold: 0.15 }
);




// # user details submission block-CODE (15)

// CSRF helper
    // function getCookie(name) {
    //   const value = `; ${document.cookie}`;
    //   const parts = value.split(`; ${name}=`);
    //   if (parts.length === 2) return parts.pop().split(';').shift();
    // }
    // const csrftoken = getCookie('csrftoken');

    // document.getElementById('ajaxSubmit').addEventListener('click', function () {
    //   const form = document.getElementById('ajaxForm');
    //   const data = new URLSearchParams(new FormData(form)).toString();

    //   fetch("{% url 'counApp:submit_contact_ajax' %}", {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/x-www-form-urlencoded',
    //       'X-CSRFToken': csrftoken,
    //       'X-Requested-With': 'XMLHttpRequest'
    //     },
    //     body: data
    //   }).then(r => r.json())
    //     .then(json => {
    //       if (json.status === 'ok') {
    //         document.getElementById('ajaxResult').textContent = 'Saved (id: ' + json.id + ')';
    //         form.reset();
    //       } else {
    //         document.getElementById('ajaxResult').textContent = 'Errors: ' + JSON.stringify(json.errors || json);
    //       }
    //     })
    //     .catch(err => document.getElementById('ajaxResult').textContent = 'Fetch error: ' + err);
    // });
