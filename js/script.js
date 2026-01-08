document.addEventListener('DOMContentLoaded', () => {
    const profileImg = document.getElementById('profileImg');
    const fileUpload = document.getElementById('fileUpload');
    const changePicBtn = document.querySelector('label[for="fileUpload"]');

    if (changePicBtn) {
        changePicBtn.addEventListener('click', () => {
            fileUpload.click();
        });
    }

    if (fileUpload) {
        fileUpload.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                profileImg.src = URL.createObjectURL(file);
            }
        });
    }
});
// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.mobile-nav-toggle');
    const sidebar = document.querySelector('.sidebar');

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            sidebar.classList.toggle('sidebar-visible');
        });
    }
    
    // Optional: Close sidebar when clicking outside of it on mobile
    document.addEventListener('click', (event) => {
        if (sidebar && sidebar.classList.contains('sidebar-visible')) {
            if (!sidebar.contains(event.target) && !navToggle.contains(event.target)) {
                sidebar.classList.remove('sidebar-visible');
            }
        }
    });
});