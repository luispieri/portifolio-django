/**
 * JavaScript principal do portfólio
 * 
 * Este arquivo contém toda a funcionalidade JavaScript do site:
 * - Formulário de contato com envio via AJAX
 * - Sistema de tema claro/escuro
 * - Menu mobile responsivo  
 * - Animações e efeitos visuais
 * - Funcionalidade de copiar email
 * 
 * Executa quando a página termina de carregar
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Portfolio JavaScript carregado!');
    // ===============================================
    // SISTEMA DE TEMA CLARO/ESCURO
    // ===============================================
    
    // Elementos do botão de mudança de tema
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const html = document.documentElement; // Elemento <html>
    
    // Verifica se há tema salvo no navegador, senão usa tema escuro
    const currentTheme = localStorage.getItem('theme') || 'dark';
    html.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);
    
    /**
     * Atualiza o ícone do botão de tema
     * @param {string} theme - 'light' ou 'dark'
     */
    function updateThemeIcon(theme) {
        if (theme === 'light') {
            themeIcon.innerHTML = '◑'; // Ícone para tema claro
        } else {
            themeIcon.innerHTML = '◐'; // Ícone para tema escuro
        }
    }
    
    // Adiciona evento de clique no botão de tema (se existir)
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            // Pega o tema atual
            const currentTheme = html.getAttribute('data-theme');
            // Alterna entre claro e escuro
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            // Aplica o novo tema
            html.setAttribute('data-theme', newTheme);
            // Salva no navegador para lembrar na próxima visita
            localStorage.setItem('theme', newTheme);
            // Atualiza o ícone
            updateThemeIcon(newTheme);
        });
    }

    // ===============================================
    // MENU MOBILE (HAMBURGER)
    // ===============================================
    
    // Elementos do menu mobile
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    // Adiciona funcionalidade de abrir/fechar menu mobile
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            // Alterna a classe 'hidden' (mostra/esconde o menu)
            mobileMenu.classList.toggle('hidden');
        });
    }

    // ===============================================
    // SCROLL SUAVE PARA LINKS INTERNOS
    // ===============================================
    
    // Adiciona scroll suave para todos os links que apontam para #alguma-coisa
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault(); // Impede o comportamento padrão
            
            // Encontra o elemento de destino
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                // Faz scroll suave até o elemento
                target.scrollIntoView({
                    behavior: 'smooth', // Animação suave
                    block: 'start'      // Alinha no topo
                });
            }
        });
    });

    // ===============================================
    // FORMULÁRIO DE CONTATO (AJAX)
    // ===============================================
    
    // Elemento do formulário de contato
    const contactForm = document.getElementById('contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            // Impede o envio normal do formulário (que recarregaria a página)
            e.preventDefault();
            
            // Coleta os dados do formulário
            const formData = new FormData(this);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                message: formData.get('message')
            };
            
            console.log('📬 Enviando formulário:', data);

            // Envia via AJAX para o servidor Django
            fetch('/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // Token CSRF necessário para segurança do Django
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: JSON.stringify(data) // Converte dados para JSON
            })
            .then(response => response.json()) // Converte resposta para JSON
            .then(data => {
                if (data.status === 'success') {
                    // Sucesso: mostra mensagem verde e limpa formulário
                    showMessage(data.message, 'success');
                    contactForm.reset();
                } else {
                    // Erro: mostra mensagem vermelha
                    showMessage(data.message, 'error');
                }
            })
            .catch(error => {
                // Erro de conexão: mostra mensagem genérica
                console.error('❌ Erro no formulário:', error);
                showMessage('Erro ao enviar mensagem. Tente novamente.', 'error');
            });
        });
    }

    /**
     * Exibe mensagem de feedback para o usuário
     * @param {string} message - Texto da mensagem
     * @param {string} type - 'success' ou 'error'
     */
    function showMessage(message, type) {
        // Cria um elemento div para a mensagem
        const messageDiv = document.createElement('div');
        
        // Define as classes CSS baseadas no tipo (sucesso = verde, erro = vermelho)
        messageDiv.className = `fixed top-20 right-6 z-50 p-4 rounded-lg shadow-lg ${
            type === 'success' 
                ? 'bg-green-100 text-green-800 border border-green-200' 
                : 'bg-red-100 text-red-800 border border-red-200'
        }`;
        
        // Define o texto da mensagem
        messageDiv.textContent = message;
        
        // Adiciona a mensagem na página
        document.body.appendChild(messageDiv);
        
        // Remove a mensagem após 5 segundos
        setTimeout(() => {
            messageDiv.remove();
        }, 5000);
    }

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.project-card, .experience-item, .skill-item').forEach(el => {
        observer.observe(el);
    });

    // Função para mostrar pop-up estilizado
    function showPopup(element) {
        if (element) {
            element.classList.remove('hidden');
            setTimeout(function() {
                element.classList.add('hidden');
            }, 2000);
        }
    }
    // Copiar e-mail do rodapé
    const emailCopyBtn = document.getElementById('email-copy');
    const emailCopiedMsg = document.getElementById('email-copied-message');
    if (emailCopyBtn) {
        emailCopyBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const email = 'luisdpieri@gmail.com';
            if (navigator.clipboard) {
                navigator.clipboard.writeText(email).then(function() {
                    showPopup(emailCopiedMsg);
                });
            }
        });
    }
    // Copiar e-mail da sidebar direita
    const fixedEmailCopyBtn = document.getElementById('fixed-email-copy');
    const fixedEmailCopiedMsg = document.getElementById('fixed-email-copied-message');
    if (fixedEmailCopyBtn) {
        fixedEmailCopyBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const email = 'luisdpieri@gmail.com';
            if (navigator.clipboard) {
                navigator.clipboard.writeText(email).then(function() {
                    showPopup(fixedEmailCopiedMsg);
                });
            }
        });
    }

    // ===============================================
    // SISTEMA DE TROCA DE IDIOMA (CLIENT-SIDE)
    // ===============================================
    
    // Adiciona funcionalidade aos links de troca de idioma
    document.querySelectorAll('a[href*="set-language"]').forEach(languageLink => {
        languageLink.addEventListener('click', function(e) {
            e.preventDefault(); // Impede navegação normal
            
            // Extrai o idioma da URL
            const url = new URL(this.href);
            const language = url.searchParams.get('language');
            const currentPath = window.location.pathname;
            
            console.log(`🌍 Mudando idioma para: ${language}, Path atual: ${currentPath}`);
            
            // Determina nova URL baseada no idioma
            let newPath;
            
            if (language === 'en') {
                // Mudando para inglês
                if (currentPath.startsWith('/en/')) {
                    newPath = currentPath; // Já está em inglês
                } else if (currentPath === '/') {
                    newPath = '/en/';
                } else {
                    newPath = '/en' + currentPath;
                }
            } else {
                // Mudando para português
                if (currentPath.startsWith('/en/')) {
                    newPath = currentPath.substring(3); // Remove '/en'
                    if (newPath === '') newPath = '/';
                } else {
                    newPath = currentPath; // Já está em português
                }
            }
            
            // Salva preferência de idioma
            localStorage.setItem('preferred_language', language);
            
            console.log(`🔄 Redirecionando para: ${newPath}`);
            
            // Redireciona para nova URL
            window.location.href = newPath;
        });
    });
    
    // Aplica idioma preferido ao carregar a página
    const preferredLanguage = localStorage.getItem('preferred_language');
    const currentPath = window.location.pathname;
    
    if (preferredLanguage === 'en' && !currentPath.startsWith('/en/') && currentPath !== '/en') {
        // Usuário prefere inglês mas está em português
        let englishPath;
        if (currentPath === '/') {
            englishPath = '/en/';
        } else {
            englishPath = '/en' + currentPath;
        }
        console.log(`🌍 Auto-redirect para inglês: ${englishPath}`);
        window.location.href = englishPath;
    } else if (preferredLanguage === 'pt-br' && currentPath.startsWith('/en/')) {
        // Usuário prefere português mas está em inglês
        let portuguesePath = currentPath.substring(3);
        if (portuguesePath === '') portuguesePath = '/';
        console.log(`🌍 Auto-redirect para português: ${portuguesePath}`);
        window.location.href = portuguesePath;
    }
});