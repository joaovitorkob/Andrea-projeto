function classificar() {
    let idade = document.getElementById("idade").value;

    // Verificação de campo vazio
    if (idade === "") {
        alert("Por favor, insira uma idade.");
        return;
    }

    idade = Number(idade);

    // Validação
    if (idade < 0 || idade > 120) {
        alert("Idade inválida! Digite um valor entre 0 e 120.");
        return;
    }

    // Classificação e redirecionamento
    if (idade < 12) {
        window.location.href = "criança.html";
    } else if (idade >= 12 && idade < 18) {
        window.location.href = "jovem.html";
    } else {
        window.location.href = "adulto.html";
    }
}