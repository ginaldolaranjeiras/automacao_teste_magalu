Funcionalidade: Adicionar produto da busca ao carrinho
    Como cliente
    Quero adicionar um produto ao carrinho
    Para armazenar os itens buscados para compra

    @funcional @adicionar-carrinho
    Cenário: Deve adicionar um item com sucesso
        Dado que estou na página de busca
        Quando quando clico no primeiro item
        E clico em adicionar à sacola
        Então sou direcionado para página do carrinho
        E o produto está contido no carrinho