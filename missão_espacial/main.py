from relatorio_missao import RelatorioDeMissao

def main():
    print("Teste do Robô Explorador")
    
    relatorio = RelatorioDeMissao("Xablau", "Marte", 87, (
        ("temperatura", -50),
        ("radiação", 2.5),
    ))
    
    print(relatorio)  # Mostra as informações do robô
    print(f"Resumo das leituras: {relatorio.resumo()}")
    print(f"Contagem de leituras: {relatorio.contagem_leituras()}")
    
    print("Fim do Teste")

if __name__ == "__main__":
    main()