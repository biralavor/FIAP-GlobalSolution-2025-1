async function loadComponent(elementId, componentPath) {
    try {
        const response = await fetch(componentPath);
        const html = await response.text();
        document.getElementById(elementId).innerHTML = html;
    } catch (error) {
        console.error(`Error loading component ${componentPath}:`, error);
    }
}

// Load all components when the page loads
document.addEventListener('DOMContentLoaded', async () => {
    // Load components first
    await loadComponent('header-component', 'components/header.html');
    await loadComponent('footer-component', 'components/footer.html');
    
    // Initialize the app after components are loaded
    new SirenaApp();
});
