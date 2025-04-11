let tabelaCriada = false; // Variável para controlar se a tabela foi criada

document.getElementById('meuFormulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtenha os valores dos campos
    const codigo = document.getElementById('codigo').value;
    const marca = document.getElementById('marca').value;
    const tipo = document.getElementById('tipo').value;
    const categoria = document.getElementById('categoria').value;
    const preco = document.getElementById('preco').value;
    const custo = document.getElementById('custo').value;
    const obs = document.getElementById('obs').value;

    // Crie a tabela
    const tabela = document.createElement('table');

        if (!tabelaCriada) {  // Adicione a classe apenas na primeira criação da tabela
            tabela.innerHTML = `
                <thead>
                    <tr>
                        <th>Código</th>
                        <th>Marca</th>
                        <th>Tipo</th>
                        <th>Categoria</th>
                        <th>Preço</th>
                        <th>Custo</th>
                        <th>Observação</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>${codigo}</td>
                        <td>${marca}</td>
                        <td>${tipo}</td>
                        <td>${categoria}</td>
                        <td>${preco}</td>
                        <td>${custo}</td>
                        <td>${obs}</td>
                    </tr>
                </tbody>
            `;
            tabelaCriada = true; // Atualiza a variável para indicar que a tabela foi criada - Marca como criada
        } else { // Se a tabela já foi criada, apenas adiciona uma nova linha
            tabela.innerHTML = `
                <tbody>
                    <tr>
                        <td>${codigo}</td>
                        <td>${marca}</td>
                        <td>${tipo}</td>
                        <td>${categoria}</td>
                        <td>${preco}</td>
                        <td>${custo}</td>
                        <td>${obs}</td>
                    </tr>
                </tbody>
            `;
        }

    // Adicione a tabela ao div de resultados
    document.getElementById('resultados').appendChild(tabela);
});
