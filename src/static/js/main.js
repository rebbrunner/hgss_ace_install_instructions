function collapse() {
    const nav = document.querySelector('nav');
    const links = document.querySelectorAll('.navlink');
    nav.classList.toggle('open');
    document.body.classList.toggle('menu-open');
    nav.classList.toggle('mobile')
    links.forEach(function(link) {
        link.classList.toggle('hidden');
    })
}
