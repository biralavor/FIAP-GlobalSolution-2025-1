public class Main {
    public static void main(String[] args){
        // Exemplo de uso das classes

        Localizacao localizacao1 = new Localizacao();
        localizacao1.setIdLocalizacao(1);
        localizacao1.setNomeRua("Floresta Nacional");
        localizacao1.setCoordenadas("-23.123456, -46.123456");

        Localizacao localizacao2 = new Localizacao();
        localizacao2.setIdLocalizacao(2);
        localizacao2.setNomeRua("Centro");
        localizacao2.setCoordenadas("-23.234567, -46.234567");

        Confiabilidade confiabilidadePadrao = new Confiabilidade();
        confiabilidadePadrao.setIdConfiabilidade(1);
        confiabilidadePadrao.setGrauConfiabilidade("Indefinido");
        Reporte reporte1 = new Reporte(1, "Incêndio na floresta", "2025-05-30", "14:30", localizacao1, "Incêndio", confiabilidadePadrao, "Pendente");
        Reporte reporte2 = new Reporte(2, "Alagamento na cidade", "2025-06-07", "09:00", localizacao2, "Alagamento", confiabilidadePadrao, "Pendente");
        Reporte reporte3 = new Reporte(3, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento", confiabilidadePadrao, "Pendente");

        ReporteList reporteList = new ReporteList(3);
        reporteList.addReporte(reporte1);
        reporteList.addReporte(reporte2);
        reporteList.addReporte(reporte3);

        // Exibir informações do reporte
        System.out.println("ID do Reporte: " + reporte1.getIdReporte());
        System.out.println("Descrição: " + reporte1.getDescricao());
        System.out.println("Data: " + reporte1.getData());
        System.out.println("Hora: " + reporte1.getHora());
        System.out.println("Localização: " + reporte1.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte1.getTipoReporte());
        System.out.println("Confiabilidade: " + reporte1.getConfiabilidade().getGrauConfiabilidade());
        System.out.println("Status: " + reporte1.getStatus());

        System.out.println("ID do Reporte: " + reporte2.getIdReporte());
        System.out.println("Descrição: " + reporte2.getDescricao());
        System.out.println("Data: " + reporte2.getData());
        System.out.println("Hora: " + reporte2.getHora());
        System.out.println("Localização: " + reporte2.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte2.getTipoReporte());
        System.out.println("Confiabilidade: " + reporte2.getConfiabilidade().getGrauConfiabilidade());
        System.out.println("Status: " + reporte2.getStatus());

        System.out.println("ID do Reporte: " + reporte3.getIdReporte());
        System.out.println("Descrição: " + reporte3.getDescricao());
        System.out.println("Data: " + reporte3.getData());
        System.out.println("Hora: " + reporte3.getHora());
        System.out.println("Localização: " + reporte3.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte3.getTipoReporte());
        System.out.println("Confiabilidade: " + reporte3.getConfiabilidade().getGrauConfiabilidade());
        System.out.println("Status: " + reporte3.getStatus());

        // Exemplo de uso do método grauConfiabilidade
        Confiabilidade confiabilidade = new Confiabilidade();
        reporteList.grauConfiabilidade(reporteList.getReportes(), confiabilidade);
        System.out.println("Grau de Confiabilidade: " + confiabilidade.getGrauConfiabilidade());
        // Exibir todos os reportes
        System.out.println("\nLista de Reportes:");
        for (Reporte reporte : reporteList.getReportes()) {
            System.out.println("ID: " + reporte.getIdReporte() + ", Descrição: " + reporte.getDescricao() + ", Localização: " + reporte.getLocalizacao().getNomeRua() + ", Tipo: " + reporte.getTipoReporte() + ", Confiabilidade: " + reporte.getConfiabilidade().getGrauConfiabilidade() + ", Status: " + reporte.getStatus());
        }

    }
}
