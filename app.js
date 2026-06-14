// Project filter chips
(function () {
  var chips = document.querySelectorAll('.chip');
  var cards = document.querySelectorAll('.card');
  function apply(filter) {
    cards.forEach(function (c) {
      var cats = (c.getAttribute('data-cats') || '');
      var show = filter === 'All' || cats.indexOf(filter) !== -1;
      c.classList.toggle('hide', !show);
    });
  }
  chips.forEach(function (ch) {
    ch.addEventListener('click', function () {
      chips.forEach(function (x) { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); });
      ch.classList.add('on'); ch.setAttribute('aria-pressed', 'true');
      apply(ch.getAttribute('data-filter'));
    });
    ch.setAttribute('aria-pressed', ch.classList.contains('on') ? 'true' : 'false');
  });
})();
