async function loadComponent(elementId, componentPath) {
    try {
        const response = await fetch(componentPath);
        const html = await response.text();
        document.getElementById(elementId).innerHTML = html;
    } catch (error) {
        console.error(`Error loading component ${componentPath}:`, error);
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    await loadComponent('header-component', 'components/header.html');
    await loadComponent('footer-component', 'components/footer.html');
    
    new SirenaApp();
});
