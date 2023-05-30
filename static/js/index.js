const link = document.querySelector('.custom-link');

link.addEventListener('mouseenter', function() {
  link.style.color = '#FF4500';
});

link.addEventListener('mouseleave', function() {
  link.style.color = '#E66D22';
});
