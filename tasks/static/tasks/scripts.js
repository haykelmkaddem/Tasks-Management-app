document.addEventListener("DOMContentLoaded", function() {
    const tagButtons = document.querySelectorAll('.tag-button');
    
    tagButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const tagId = this.getAttribute('data-tag-id');
        const checkbox = document.getElementById('tag_' + tagId);
        
        checkbox.checked = !checkbox.checked;
        
        if (checkbox.checked) {
          this.classList.remove('btn-secondary');
          this.classList.add('btn-success');
        } else {
          this.classList.remove('btn-success');
          this.classList.add('btn-secondary');
        }
      });
    });
  });
  