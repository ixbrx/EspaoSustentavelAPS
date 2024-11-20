
document.getElementById('menu-toggle').addEventListener('click', function() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('hidden'); 
    
   
    if (!navbar.classList.contains('hidden')) {
        navbar.classList.add('visible'); 
    } else {
        navbar.classList.remove('visible'); 
    }
});


document.getElementById('calculadora-form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const formData = new FormData(this); 

    
    fetch('/calcular', {
        method: 'POST',
        body: formData 
    })
    .then(response => response.json()) 
    .then(data => {
       
        document.getElementById('emissoes').innerText = `Emissões totais de CO₂: ${data.emissoes_totais.toFixed(2)} toneladas`;
        document.getElementById('creditos').innerText = `Créditos de carbono necessários: ${data.creditos_carbono.toFixed(2)} créditos de carbono.`;
        document.getElementById('resultado').style.display = 'block'; 
    })
    .catch(error => console.error('Erro:', error)); 
});
