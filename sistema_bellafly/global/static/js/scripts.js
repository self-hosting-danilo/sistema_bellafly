// Menu lateral
function toggleMenu() {
    const menu = document.getElementById("menu");
    const overlay = document.getElementById("overlay");
    menu.classList.toggle("show");
    overlay.classList.toggle("show");
}
function closeMenu() {
    document.getElementById("menu").classList.remove("show");
    document.getElementById("overlay").classList.remove("show");
}

// -------------------------
// CARRINHO
// -------------------------
let cart = JSON.parse(localStorage.getItem("cart")) || [];

function renderCart() {
    const cartItems = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");
    const cartCount = document.getElementById("cart-count");
    cartItems.innerHTML = "";

    if (cart.length === 0) {
    cartItems.innerHTML = "<p>Seu carrinho está vazio.</p>";
    cartTotal.innerHTML = "";
    cartCount.textContent = "0";
    return;
    }

    let total = 0;
    let count = 0;

    cart.forEach((item, index) => {
    total += item.preco * item.quantidade;
    count += item.quantidade;
    cartItems.innerHTML += `
        <div>
        ${item.nome} - R$ ${item.preco.toFixed(2)} x ${item.quantidade}
        <button onclick="removeFromCart(${index})">❌</button>
        </div>
    `;
    });

    cartTotal.innerHTML = `<h3>Total: R$ ${total.toFixed(2)}</h3>`;
    cartCount.textContent = count;
    localStorage.setItem("cart", JSON.stringify(cart));
}

function removeFromCart(index) {
    cart.splice(index, 1);
    renderCart();
}

// Adicionar ao carrinho
document.querySelectorAll('.add-to-cart').forEach(btn => {
    btn.addEventListener('click', function() {
    const nome = this.dataset.nome;
    const preco = parseFloat(this.dataset.preco.replace(",", "."));
    const existing = cart.find(item => item.nome === nome);

    if (existing) {
        existing.quantidade += 1;
    } else {
        cart.push({ nome, preco, quantidade: 1 });
    }

    renderCart();
    });
});

function sendCartToWhatsApp() {
    if (cart.length === 0) {
    alert("Seu carrinho está vazio!");
    return;
    }

    let mensagem = "🛍️ Meu Pedido Bellafly:%0A%0A";
    let total = 0;

    cart.forEach(item => {
    mensagem += `• ${item.nome} - R$ ${item.preco.toFixed(2)} x ${item.quantidade}%0A`;
    total += item.preco * item.quantidade;
    });

    mensagem += `%0A💰 Total: R$ ${total.toFixed(2)}`;

    const telefone = "557981718236";
    const url = `https://wa.me/${telefone}?text=${mensagem}`;
    window.open(url, "_blank");
}

function toggleCart() {
    document.getElementById("cart-sidebar").classList.toggle("show");
    document.getElementById("cart-overlay").classList.toggle("show");
}

function clearCart() {
    if (confirm("Tem certeza que deseja limpar o carrinho?")) {
    cart = [];
    localStorage.removeItem("cart");
    renderCart();
    }
}

// Inicializa carrinho
renderCart();