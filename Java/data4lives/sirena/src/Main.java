public class Main {
    public static void main(String[] args){

        // Criando endereçoes
        Localizacao localizacao1 = new Localizacao();
        localizacao1.setIdLocalizacao(1);
        localizacao1.setNomeRua("Rua das Flores");
        localizacao1.setCoordenadas("-23.123456, -46.123456");

        Localizacao localizacao2 = new Localizacao();
        localizacao2.setIdLocalizacao(2);
        localizacao2.setNomeRua("Avenida das Árvores");
        localizacao2.setCoordenadas("-23.234567, -46.234567");

        Localizacao localizacao3 = new Localizacao();
        localizacao3.setIdLocalizacao(3);
        localizacao3.setNomeRua("Rua das Palmeiras");
        localizacao3.setCoordenadas("-23.345678, -46.345678");

        // Criando reportes
        Reporte reporte1 = new Reporte(1, "Incêndio na floresta", "2025-05-30", "14:30", localizacao1, "Incêndio", true, true);
        Reporte reporte2 = new Reporte(2, "Alagamento na cidade", "2025-06-07", "09:00", localizacao2, "Alagamento", false, true);
        Reporte reporte3 = new Reporte(3, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento", false, false);
        Reporte reporte4 = new Reporte(4, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento", false, false);
        Reporte reporte5 = new Reporte(5, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento", false, false);

        // Exibir informações de cada reporte
        reporte1.reportePrinter();
        reporte2.reportePrinter();
        reporte3.reportePrinter();
        reporte4.reportePrinter();
        reporte5.reportePrinter();

        // Criando uma lista de reportes e adicionando os reportes criados
        ReporteList listaReportes = new ReporteList(10);
        listaReportes.addToReporteList(reporte1);
        listaReportes.addToReporteList(reporte2);
        listaReportes.addToReporteList(reporte3);
        listaReportes.addToReporteList(reporte4);
        listaReportes.addToReporteList(reporte5);

        // Calculando confiabilidade e prioridade
        Prioridade prioridade = new Prioridade();
        prioridade.defineGrauPrioridade(reporte1.isPessoaEmPerigo(), reporte1.isViaIntransitavel());
        prioridade.defineGrauPrioridade(reporte2.isPessoaEmPerigo(), reporte2.isViaIntransitavel());
        prioridade.defineGrauPrioridade(reporte3.isPessoaEmPerigo(), reporte3.isViaIntransitavel());
        prioridade.defineGrauPrioridade(reporte4.isPessoaEmPerigo(), reporte4.isViaIntransitavel());
        prioridade.defineGrauPrioridade(reporte5.isPessoaEmPerigo(), reporte5.isViaIntransitavel());
        Confiabilidade confiabilidade = new Confiabilidade();
        confiabilidade.calculoConfiabilidade(listaReportes);
        listaReportes.reporteListPrinter();

        // Criando policial e bombeiro
        Policial policial1 = new Policial("João Silva", "123456789", "Policial Militar", "11912345678", localizacao3, "Sargento","Moema" , "PMSP1234");
        Policial policial2 = new Policial("Ana Oliveira", "456123789", "Policial Civil", "11911223344", localizacao2, "Investigadora", "Centro", "PCSP3421");

        Bombeiro bombeiro1 = new Bombeiro("Maria Oliveira", "987654321", "Corpo de Bombeiros", "11987654321", localizacao2, "Busca e Salvamento Urbano", "Pinheiros", "CBSP5678");
        Bombeiro bombeiro2 = new Bombeiro("Lucas Fernandes", "159753468", "Corpo de Bombeiros", "11988776655", localizacao2, "Salvamento em Altura", "Jardins", "CBSP9021");

        policial1.autoridadePrinter();
        policial2.autoridadePrinter();
        bombeiro1.autoridadePrinter();  
        bombeiro2.autoridadePrinter();

        // Criando ocorrências
        Ocorrencia ocorrencia1 = new Ocorrencia(localizacao1, "11:20", confiabilidade, prioridade, new Autoridade[]{policial1, bombeiro1});
        Ocorrencia ocorrencia2 = new Ocorrencia(localizacao2, "12:30", confiabilidade, prioridade, new Autoridade[]{policial2, bombeiro2});

        ocorrencia1.atenderOcorrencia(reporte1, "11:30", new Autoridade[]{policial1, bombeiro1});
        ocorrencia2.atenderOcorrencia(reporte3, "12:45", new Autoridade[]{policial2, bombeiro2});
        ocorrencia2.ocorrenciaPrinter();
    }
}
