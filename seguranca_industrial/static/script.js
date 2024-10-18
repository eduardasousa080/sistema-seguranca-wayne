const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');
const registerForm = document.getElementById('registerForm');

registerBtn.addEventListener('click', () => {
    container.classList.add('active');
});

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
});

// Adicionando o evento de envio do formulário de registro
registerForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita o comportamento padrão de envio do formulário

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Envie os dados para o servidor
    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password }),
        });

        const data = await response.json();
        if (response.ok) {
            alert('Conta criada com sucesso!'); // Mensagem de sucesso
            // Redirecionar ou limpar o formulário
            registerForm.reset();
        } else {
            alert(data.message || 'Erro ao criar conta'); // Mensagem de erro
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao criar conta. Tente novamente.'); // Mensagem de erro genérico
    }
});
