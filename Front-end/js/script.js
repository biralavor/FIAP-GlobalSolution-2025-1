class SirenaApp {
    constructor() {
        this.menuToggle = document.getElementById('menuToggle');
        this.mobileMenu = document.getElementById('mobileMenu');
        this.isMenuOpen = false;
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        // Mobile menu toggle
        this.menuToggle?.addEventListener('click', () => {
            this.toggleMobileMenu();
        });
        
        // CTA button interactions
        this.setupCTAButtons();
        
        // Window resize handler
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 768 && this.isMenuOpen) {
                this.closeMobileMenu();
            }
        });
    }
    
    toggleMobileMenu() {
        this.isMenuOpen = !this.isMenuOpen;
        
        if (this.isMenuOpen) {
            this.openMobileMenu();
        } else {
            this.closeMobileMenu();
        }
    }
    
    openMobileMenu() {
        this.menuToggle.classList.add('active');
        this.mobileMenu.classList.add('active');
        document.body.style.overflow = 'hidden';
        this.isMenuOpen = true;
    }
    
    closeMobileMenu() {
        this.menuToggle.classList.remove('active');
        this.mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
        this.isMenuOpen = false;
    }
    
    setupCTAButtons() {
        const whatsappButtons = document.querySelectorAll('.whatsapp-button');
        const lucasButton = document.querySelector('.lucas-button');
        const learnMoreButton = document.querySelector('.learn-more-button');
        
        // WhatsApp buttons
        whatsappButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.handleWhatsAppClick();
            });
        });
        
        // L.U.C.A.S. button
        if (lucasButton) {
            lucasButton.addEventListener('click', () => {
                window.location.href = 'page-conhecaLucas.html';
            });
        }
        
        // Learn more button
        if (learnMoreButton) {
            learnMoreButton.addEventListener('click', () => {
                window.location.href = 'page-sirena.html';
            });
        }
    }
    
    handleWhatsAppClick() {
        const whatsappUrl = `https://t.me/Hideki_1TDSPX_2025_bot`;
        window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    }
}

// Initialize the app directly since script is at end of body
new SirenaApp();