// FUNÇÃO PARA COPIAR A CHAVE PIX COM FEEDBACK VISUAL
function copiarPix() {
  const pixInput = document.getElementById("pixKey");
  const copyFeedback = document.getElementById("copyFeedback");
  const btnCopyPix = document.getElementById("btnCopyPix");

  // Copia o valor para a área de transferência
  navigator.clipboard.writeText(pixInput.value).then(() => {
    // Exibe o texto de confirmação
    copyFeedback.style.display = "block";
    btnCopyPix.innerText = "Copiado! ✓";
    btnCopyPix.style.backgroundColor = "#28a745";

    // Retorna ao estado normal após 3 segundos
    setTimeout(() => {
      copyFeedback.style.display = "none";
      btnCopyPix.innerText = "Copiar Chave";
      btnCopyPix.style.backgroundColor = "";
    }, 3000);
  }).catch(err => {
    // Fallback caso a API moderna de clipboard falhe
    pixInput.select();
    document.execCommand("copy");
    alert("Chave PIX copiada: " + pixInput.value);
  });
}

// LOG DE INICIALIZAÇÃO
console.log("Portal Lar dos Idosos WB carregado com sucesso.");
