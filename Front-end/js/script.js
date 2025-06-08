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
        this.menuToggle?.addEventListener('click', () => {
            this.toggleMobileMenu();
        });
        
        this.setupCTAButtons();
        
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
        const data4lifeButton = document.querySelector('.data4life-button');
        const registerButton = document.querySelector('.register-button');

        whatsappButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.handleWhatsAppClick();
            });
        });
        
        if (lucasButton) {
            lucasButton.addEventListener('click', () => {
                window.location.href = 'page-conhecaLucas.html';
            });
        }
        
        if (learnMoreButton) {
            learnMoreButton.addEventListener('click', () => {
                window.location.href = 'page-sirena.html';
            });
        }

        if (data4lifeButton) {
            data4lifeButton.addEventListener('click', () => {
                window.location.href = 'page-quemsomos.html';
            });
        }

        if (registerButton) {
            registerButton.addEventListener('click', () => {
                window.location.href = 'signin-autoridade.html';
            });
        }
    }

    handleWhatsAppClick() {
        const whatsappUrl = `https://t.me/Hideki_1TDSPX_2025_bot`;
        window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    }
}

new SirenaApp();