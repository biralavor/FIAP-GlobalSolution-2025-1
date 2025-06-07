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

        Reporte reporte1 = new Reporte(1, "Incêndio na floresta", "2025-05-30", "14:30", localizacao1, "Incêndio");
        Reporte reporte2 = new Reporte(2, "Alagamento na cidade", "2025-06-07", "09:00", localizacao2, "Alagamento");
        Reporte reporte3 = new Reporte(3, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento");
        Reporte reporte4 = new Reporte(4, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento");
        Reporte reporte5 = new Reporte(5, "Deslizamento de terra", "2025-10-07", "11:15", localizacao2, "Deslizamento");

        // Exibir informações do reporte
        System.out.println("ID do Reporte: " + reporte1.getIdReporte());
        System.out.println("Descrição: " + reporte1.getDescricao());
        System.out.println("Data: " + reporte1.getData());
        System.out.println("Hora: " + reporte1.getHora());
        System.out.println("Localização: " + reporte1.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte1.getTipoReporte());
        
        System.out.println("ID do Reporte: " + reporte2.getIdReporte());
        System.out.println("Descrição: " + reporte2.getDescricao());
        System.out.println("Data: " + reporte2.getData());
        System.out.println("Hora: " + reporte2.getHora());
        System.out.println("Localização: " + reporte2.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte2.getTipoReporte());

        System.out.println("ID do Reporte: " + reporte3.getIdReporte());
        System.out.println("Descrição: " + reporte3.getDescricao());
        System.out.println("Data: " + reporte3.getData());
        System.out.println("Hora: " + reporte3.getHora());
        System.out.println("Localização: " + reporte3.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte3.getTipoReporte());

        System.out.println("ID do Reporte: " + reporte4.getIdReporte());
        System.out.println("Descrição: " + reporte4.getDescricao());
        System.out.println("Data: " + reporte4.getData());
        System.out.println("Hora: " + reporte4.getHora());
        System.out.println("Localização: " + reporte4.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte4.getTipoReporte());

        System.out.println("ID do Reporte: " + reporte5.getIdReporte());
        System.out.println("Descrição: " + reporte5.getDescricao());
        System.out.println("Data: " + reporte5.getData());
        System.out.println("Hora: " + reporte5.getHora());
        System.out.println("Localização: " + reporte5.getLocalizacao().getNomeRua());
        System.out.println("Tipo de Reporte: " + reporte5.getTipoReporte());

        ReporteList listaReportes = new ReporteList(10);
        listaReportes.addToReporteList(reporte1);
        listaReportes.addToReporteList(reporte2);
        listaReportes.addToReporteList(reporte3);
        listaReportes.addToReporteList(reporte4);
        listaReportes.addToReporteList(reporte5);

        listaReportes.calculoConfiabilidade();
        listaReportes.reporteListPrinter();
    }
}
